# -*- coding: utf-8 -*-
"""Проверка переводов: структура как у en.source.json, плейсхолдеры {s}/{loc} на месте, нет непереведённых длинных строк."""
import json, pathlib, re, sys
D = pathlib.Path(__file__).parent
src = json.loads((D/"en.source.json").read_text(encoding="utf-8"))
KEEP = {"WhatsApp", "Bali Nannies", "English · Bahasa"}

def walk(a, b, path, errs, same):
    if type(a) is not type(b):
        errs.append(f"{path}: type {type(a).__name__} != {type(b).__name__}"); return
    if isinstance(a, dict):
        if set(a) != set(b): errs.append(f"{path}: keys differ {sorted(set(a)^set(b))[:5]}")
        for k in a.keys() & b.keys(): walk(a[k], b[k], f"{path}.{k}", errs, same)
    elif isinstance(a, list):
        if len(a) != len(b): errs.append(f"{path}: len {len(a)} != {len(b)}")
        for i,(x,y) in enumerate(zip(a,b)): walk(x, y, f"{path}[{i}]", errs, same)
    elif isinstance(a, str):
        for ph in re.findall(r"\{\w+\}", a):
            if ph not in b: errs.append(f"{path}: lost {ph}")
        if a == b and len(a) > 12 and a not in KEEP and not re.fullmatch(r"[\W\d]+", a): same.append(path)

ok = True
for f in sorted(D.glob("*.json")):
    if f.name == "en.source.json": continue
    try: tr = json.loads(f.read_text(encoding="utf-8"))
    except Exception as e: print(f.stem, "JSON ERROR", e); ok=False; continue
    errs, same = [], []
    walk(src, tr, f.stem, errs, same)
    print(f"{f.stem}: {'OK' if not errs else 'ERR'} | errors {len(errs)} | untranslated {len(same)}")
    for e in errs[:8]: print("   ", e)
    for s_ in same[:5]: print("    same:", s_)
    ok &= not errs
sys.exit(0 if ok else 1)
