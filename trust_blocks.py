# -*- coding: utf-8 -*-
"""Блоки доверия (EN/RU): проверка нянь, знакомство до встречи, гарантия замены, что няня берёт с собой, анкета перед сменой.
ВАЖНО: формулировки — заготовки. Перед запуском привести в точное соответствие с реальным процессом агентства."""

TB = {
"en": dict(
  hero_trust=["Vetted in person", "Meet your nanny first", "Replacement guarantee", "Pay after the session"],
  vet_h="How we vet every nanny", vet_p="Six steps before a nanny meets her first family. No shortcuts.",
  vet=[("🪪","ID & address check","Passport or KTP verified, home address confirmed."),
       ("📞","Two family references","We call previous families ourselves — not just read letters."),
       ("🤝","In-person interview","Face to face, with childcare scenarios and English check."),
       ("⛑️","Paediatric first aid & CPR","Valid certificate, renewed on schedule. We can show it to you."),
       ("🏊","Water-safety rules","Pool and beach supervision rules signed by every nanny."),
       ("⭐","Trial shift & feedback","First shifts reviewed; families rate every booking.")],
  meet_h="Meet your nanny before she arrives", meet_p="No strangers at your door. Before the booking is confirmed you get:",
  meet=["Her photo, name and years of experience","Languages she speaks and ages she's best with","A short video hello on WhatsApp","A quick video call if you'd like one"],
  card=dict(tag="Example profile", name="Your nanny", meta="7 years · babies & toddlers", langs="English · Bahasa", loves="Loves: swimming, drawing, songs", vid="▶ Video hello · 0:30"),
  guar_h="Replacement guarantee", guar_p="If your nanny is ill or can't make it, we send another vetted nanny — or you don't pay. Your evening stays yours.",
  bring_h="What your nanny brings", bring_p="Kids don't just get supervised — they have fun.",
  bring=[("🎨","Craft kit","Paper, crayons, stickers, simple crafts"),("📚","Picture books","Age-matched stories for bedtime"),("🫧","Pool & beach games","Bubbles, sand toys, water games"),("🧩","Quiet games","Puzzles and cards for the hotel room"),("⛑️","Mini first-aid kit","Plasters, antiseptic, cold pack"),("📱","Photo updates","A few photos on WhatsApp during the shift")],
  check_h="Before every shift we ask", check_p="So nothing important is forgotten. Takes 2 minutes on WhatsApp.",
  check=["Allergies, medicines and health notes","Sleep and meal routine","Is the pool or beach allowed? With what rules?","Screen time and sweets","Your phone and a backup contact","Hotel or villa rules and room number"],
  faq_add=[("What if the nanny cancels?","We send a replacement nanny with the same checks. If we can't, you don't pay."),("Can I see the nanny before booking?","Yes. You get her photo, experience and a short video hello, and can ask for a video call.")],
),
"ru": dict(
  hero_trust=["Лично проверяем каждую", "Знакомство до встречи", "Гарантия замены", "Оплата после смены"],
  vet_h="Как мы проверяем каждую няню", vet_p="Шесть шагов до первой семьи. Без исключений.",
  vet=[("🪪","Документы и адрес","Проверяем паспорт или KTP, подтверждаем адрес проживания."),
       ("📞","Две рекомендации от семей","Сами звоним прошлым семьям, а не просто читаем письма."),
       ("🤝","Личное собеседование","Лицом к лицу: ситуации с детьми и проверка английского."),
       ("⛑️","Детская первая помощь и СЛР","Действующий сертификат с регулярным продлением. Покажем вам."),
       ("🏊","Правила у воды","Каждая няня подписывает правила присмотра у бассейна и на пляже."),
       ("⭐","Пробные смены и отзывы","Первые смены под контролем, семьи оценивают каждую бронь.")],
  meet_h="Знакомство с няней до встречи", meet_p="Никаких незнакомцев у двери. До подтверждения брони вы получаете:",
  meet=["Фото, имя и опыт няни","Языки и возраст детей, с которым она лучше всего работает","Короткое видео-приветствие в WhatsApp","Видеозвонок, если хотите"],
  card=dict(tag="Пример профиля", name="Ваша няня", meta="7 лет опыта · малыши", langs="English · Bahasa", loves="Любит: плавание, рисование, песни", vid="▶ Видео-приветствие · 0:30"),
  guar_h="Гарантия замены", guar_p="Если няня заболела или не может прийти — пришлём другую проверенную няню или вы не платите. Ваш вечер остаётся вашим.",
  bring_h="Что няня приносит с собой", bring_p="Детям не просто присматривают — им интересно.",
  bring=[("🎨","Набор для творчества","Бумага, мелки, наклейки, поделки"),("📚","Книжки с картинками","По возрасту, для сна"),("🫧","Игры для бассейна и пляжа","Мыльные пузыри, формочки, игры в воде"),("🧩","Тихие игры","Пазлы и карточки для номера"),("⛑️","Мини-аптечка","Пластыри, антисептик, охлаждающий пакет"),("📱","Фото в WhatsApp","Несколько фото во время смены")],
  check_h="Перед каждой сменой мы уточняем", check_p="Чтобы ничего важного не забылось. 2 минуты в WhatsApp.",
  check=["Аллергии, лекарства, особенности здоровья","Режим сна и еды","Можно ли в бассейн или на пляж, и по каким правилам","Мультики и сладкое","Ваш телефон и запасной контакт","Правила отеля или виллы, номер комнаты"],
  faq_add=[("Что если няня отменит смену?","Пришлём замену с такими же проверками. Если не сможем — вы не платите."),("Можно познакомиться с няней до брони?","Да. Пришлём фото, опыт и короткое видео-приветствие, можно созвониться по видео.")],
)}

def vet_html(b):
    return f'<div class="vet-grid">' + "".join(f'<div class="vet reveal"><span class="vet-ico">{i}</span><h3>{h}</h3><p>{p}</p></div>' for i,h,p in b["vet"]) + "</div>"

def meet_html(b, root):
    c = b["card"]
    items = "".join(f"<li>{x}</li>" for x in b["meet"])
    return f'''<div class="meet"><div><h2>{b["meet_h"]}</h2><p class="lead">{b["meet_p"]}</p><ul class="ticks">{items}</ul></div>
<div class="phone reveal"><div class="phone-bar">WhatsApp</div><div class="bubble"><span class="tag">{c["tag"]}</span>
<div class="prof"><img src="{root}img/hotel-villa-babysitting.jpg" alt="" loading="lazy"><div><b>{c["name"]}</b><br><small>{c["meta"]}</small></div></div>
<p>🗣 {c["langs"]}<br>💛 {c["loves"]}</p><div class="vid">{c["vid"]}</div></div></div></div>'''

def guar_html(b):
    return f'<div class="guar reveal"><span class="guar-ico">🛡️</span><div><h2>{b["guar_h"]}</h2><p>{b["guar_p"]}</p></div></div>'

def bring_html(b):
    return f'<div class="sec-head"><h2>{b["bring_h"]}</h2><p>{b["bring_p"]}</p></div><div class="bring-grid">' + "".join(f'<div class="bring reveal"><span>{i}</span><b>{h}</b><small>{p}</small></div>' for i,h,p in b["bring"]) + "</div>"

def check_html(b):
    return f'<div class="check-box"><div><h2>{b["check_h"]}</h2><p>{b["check_p"]}</p></div><ol class="check-list">' + "".join(f"<li>{x}</li>" for x in b["check"]) + "</ol></div>"

CSS = """
.vet-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.vet{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:18px;padding:22px}
.vet h3{color:#fff;font-size:1.08rem;margin:10px 0 6px}.vet p{margin:0;font-size:.93rem;color:#C9DBD4}.vet-ico{font-size:1.6rem}
.vet-band{background:var(--brand);color:#EAF3EF;border-radius:32px;padding:56px}.vet-band h2{color:#fff}.vet-band .sec-head p{color:#C9DBD4}
.meet{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center}
.ticks{list-style:none;padding:0;margin:18px 0 0}.ticks li{padding:10px 0 10px 34px;position:relative;border-bottom:1px solid var(--line)}
.ticks li::before{content:"✓";position:absolute;left:0;top:9px;width:24px;height:24px;border-radius:50%;background:var(--brand-2);color:var(--brand);display:grid;place-items:center;font-weight:700;font-size:.85rem}
.phone{max-width:340px;margin:0 auto;background:#ECE5DD;border-radius:32px;padding:0 0 22px;box-shadow:0 30px 60px rgba(27,43,39,.15);overflow:hidden;border:8px solid #1B2B27}
.phone-bar{background:#075E54;color:#fff;padding:14px 18px;font-weight:600;font-size:.9rem}
.bubble{background:#fff;margin:18px 16px 0;border-radius:4px 16px 16px 16px;padding:14px 16px;font-size:.92rem;box-shadow:0 1px 1px rgba(0,0,0,.08)}
.bubble .tag{display:inline-block;font-size:.7rem;background:var(--brand-2);color:var(--brand);padding:2px 8px;border-radius:999px;margin-bottom:10px}
.prof{display:flex;gap:12px;align-items:center;margin-bottom:10px}.prof img{width:52px;height:52px;border-radius:50%;object-fit:cover}
.bubble p{margin:0 0 10px;color:var(--muted)}.vid{background:#1B2B27;color:#fff;border-radius:10px;padding:26px;text-align:center;font-size:.85rem}
.guar{display:flex;gap:22px;align-items:center;background:#FFF4E8;border:1px solid #F5D9B8;border-radius:24px;padding:28px 32px}
.guar h2{font-size:1.5rem;margin:0 0 6px}.guar p{margin:0;color:var(--muted)}.guar-ico{font-size:2.4rem}
.bring-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:14px}
.bring{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:20px 16px;text-align:center;display:flex;flex-direction:column;gap:6px}
.bring span{font-size:1.8rem}.bring small{color:var(--muted);line-height:1.35}
.check-box{display:grid;grid-template-columns:.8fr 1.2fr;gap:36px;background:var(--surface);border:1px solid var(--line);border-radius:28px;padding:40px}
.check-list{margin:0;padding:0;list-style:none;counter-reset:c;display:grid;grid-template-columns:1fr 1fr;gap:10px 24px}
.check-list li{counter-increment:c;padding:12px 0 12px 40px;position:relative;border-bottom:1px dashed var(--line)}
.check-list li::before{content:counter(c);position:absolute;left:0;top:10px;width:28px;height:28px;border-radius:8px;background:var(--brand);color:#fff;display:grid;place-items:center;font-size:.85rem;font-weight:700}
@media(max-width:960px){.vet-grid{grid-template-columns:1fr 1fr}.bring-grid{grid-template-columns:repeat(3,1fr)}.meet,.check-box{grid-template-columns:1fr}.check-list{grid-template-columns:1fr}}
@media(max-width:560px){.vet-grid{grid-template-columns:1fr}.bring-grid{grid-template-columns:1fr 1fr}.vet-band{padding:32px 22px}.guar{flex-direction:column;align-items:flex-start}}
"""
