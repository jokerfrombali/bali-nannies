# -*- coding: utf-8 -*-
"""Цены (IDR) и конвертер валют. Заполненные тарифы — от заказчика 28.09.2026; остальные пока «по запросу»."""

RATE_HOUR = 120_000
EXTRA_CHILD = 25_000   # +IDR/час за второго ребёнка (частная разница няни 100k→125k)
PRICES = {
    "hourly-babysitter":       dict(idr=RATE_HOUR, unit="hour", min_h=5, extra_child=EXTRA_CHILD),
    "day-nanny":               dict(idr=RATE_HOUR * 10, unit="day", hours=10),
    "night-nanny":             dict(idr=1_700_000, unit="night"),
    "hotel-villa-babysitting": dict(idr=RATE_HOUR, unit="hour", min_h=5, extra_child=EXTRA_CHILD),
    "event-babysitting":       dict(idr=RATE_HOUR, unit="hour", min_h=5, meal=True),
    "travel-nanny":            dict(idr=RATE_HOUR, unit="hour", min_h=5, travel=True),
}

# запасные курсы IDR→валюта (open.er-api.com, 28.09.2026); на странице подтягиваются свежие
FALLBACK = {"IDR":1,"USD":5.6e-05,"EUR":4.9e-05,"AUD":8e-05,"GBP":4.2e-05,"SGD":7.1e-05,"RUB":0.004701,"CNY":0.000377,"INR":0.005354,"KRW":0.075662,"JPY":0.008807}
FALLBACK_DATE = "2026-09-28"
CURRENCIES = ["IDR","USD","EUR","AUD","GBP","SGD","RUB","CNY","INR","KRW","JPY"]
DEFAULT_CUR = {"en":"USD","ru":"RUB","zh":"CNY","hi":"INR","ko":"KRW","ja":"JPY","fr":"EUR","de":"EUR","es":"EUR","it":"EUR","nl":"EUR","id":"IDR"}

P = {
 "en": dict(per_hour="/ hour", per_day="/ day", min_h="min. {n} hours", day_note="{n} hours, e.g. 10:00–20:00", on_request="On request", show_in="Show prices in", approx="Approximate conversion. You pay in IDR.", min_total="Minimum booking"),
 "ru": dict(per_hour="/ час", per_day="/ день", min_h="минимум {n} часов", day_note="{n} часов, например 10:00–20:00", on_request="По запросу", show_in="Показать цены в", approx="Пересчёт примерный. Оплата в рупиях (IDR).", min_total="Минимальная бронь"),
 "zh": dict(per_hour="/ 小时", per_day="/ 天", min_h="最少 {n} 小时", day_note="{n} 小时，例如 10:00–20:00", on_request="价格请咨询", show_in="显示货币", approx="换算仅供参考，实际以印尼盾（IDR）支付。", min_total="最低预订"),
 "hi": dict(per_hour="/ घंटा", per_day="/ दिन", min_h="कम से कम {n} घंटे", day_note="{n} घंटे, जैसे 10:00–20:00", on_request="पूछने पर", show_in="कीमत इस मुद्रा में दिखाएँ", approx="रूपांतरण अनुमानित है। भुगतान IDR में होता है।", min_total="न्यूनतम बुकिंग"),
 "ko": dict(per_hour="/ 시간", per_day="/ 일", min_h="최소 {n}시간", day_note="{n}시간 (예: 10:00–20:00)", on_request="문의", show_in="표시 통화", approx="환산 금액은 참고용이며, 결제는 인도네시아 루피아(IDR)로 합니다.", min_total="최소 예약 금액"),
 "ja": dict(per_hour="/ 時間", per_day="/ 日", min_h="最低{n}時間", day_note="{n}時間（例：10:00–20:00）", on_request="お問い合わせ", show_in="表示通貨", approx="換算は目安です。お支払いはインドネシアルピア（IDR）です。", min_total="最低ご予約料金"),
 "fr": dict(per_hour="/ heure", per_day="/ jour", min_h="{n} heures minimum", day_note="{n} heures, ex. 10h00–20h00", on_request="Sur demande", show_in="Afficher les prix en", approx="Conversion indicative. Paiement en roupies (IDR).", min_total="Réservation minimale"),
 "de": dict(per_hour="/ Stunde", per_day="/ Tag", min_h="mind. {n} Stunden", day_note="{n} Stunden, z. B. 10:00–20:00", on_request="Auf Anfrage", show_in="Preise anzeigen in", approx="Ungefähre Umrechnung. Bezahlt wird in IDR.", min_total="Mindestbuchung"),
 "es": dict(per_hour="/ hora", per_day="/ día", min_h="mínimo {n} horas", day_note="{n} horas, p. ej. 10:00–20:00", on_request="Bajo consulta", show_in="Ver precios en", approx="Conversión aproximada. Pagas en rupias (IDR).", min_total="Reserva mínima"),
 "it": dict(per_hour="/ ora", per_day="/ giorno", min_h="minimo {n} ore", day_note="{n} ore, es. 10:00–20:00", on_request="Su richiesta", show_in="Mostra i prezzi in", approx="Conversione indicativa. Si paga in rupie (IDR).", min_total="Prenotazione minima"),
 "nl": dict(per_hour="/ uur", per_day="/ dag", min_h="minimaal {n} uur", day_note="{n} uur, bijv. 10:00–20:00", on_request="Op aanvraag", show_in="Toon prijzen in", approx="Omrekening is een schatting. Je betaalt in IDR.", min_total="Minimale boeking"),
 "id": dict(per_hour="/ jam", per_day="/ hari", min_h="minimal {n} jam", day_note="{n} jam, mis. 10.00–20.00", on_request="Sesuai permintaan", show_in="Tampilkan harga dalam", approx="Konversi hanya perkiraan. Pembayaran dalam Rupiah (IDR).", min_total="Pemesanan minimum"),
}

for _l,_d in {'en': {'per_night': '/ night', 'extra_child': '+{x} / hour for a 2nd child', 'meal': 'Over 5 hours: a meal for the nanny, please', 'travel': 'Transport, tickets and accommodation paid by the family'}, 'ru': {'per_night': '/ ночь', 'extra_child': '+{x} / час за второго ребёнка', 'meal': 'Больше 5 часов: питание для няни за счёт семьи', 'travel': 'Дорога, билеты и проживание — за счёт семьи'}, 'zh': {'per_night': '/ 晚', 'extra_child': '第二个孩子每小时加 {x}', 'meal': '超过 5 小时：请为保姆提供一餐', 'travel': '交通、门票及住宿由家庭承担'}, 'hi': {'per_night': '/ रात', 'extra_child': 'दूसरे बच्चे के लिए +{x} / घंटा', 'meal': '5 घंटे से ज़्यादा: नैनी के लिए भोजन परिवार की ओर से', 'travel': 'यात्रा, टिकट और ठहरने का ख़र्च परिवार का'}, 'ko': {'per_night': '/ 1박', 'extra_child': '둘째 아이 시간당 +{x}', 'meal': '5시간 초과 시: 시터 식사를 제공해 주세요', 'travel': '교통비·입장권·숙박비는 가족 부담'}, 'ja': {'per_night': '/ 泊', 'extra_child': 'お子さま2人目は1時間あたり +{x}', 'meal': '5時間を超える場合：シッターのお食事をご用意ください', 'travel': '交通費・チケット代・宿泊費はご家族のご負担'}, 'fr': {'per_night': '/ nuit', 'extra_child': '+{x} / heure pour un 2e enfant', 'meal': 'Au-delà de 5 heures : un repas pour la nounou', 'travel': 'Transport, billets et hébergement à la charge de la famille'}, 'de': {'per_night': '/ Nacht', 'extra_child': '+{x} / Stunde für ein 2. Kind', 'meal': 'Ab 5 Stunden: bitte eine Mahlzeit für die Nanny', 'travel': 'Fahrt, Tickets und Unterkunft zahlt die Familie'}, 'es': {'per_night': '/ noche', 'extra_child': '+{x} / hora por un 2.º niño', 'meal': 'Más de 5 horas: una comida para la niñera', 'travel': 'Transporte, entradas y alojamiento a cargo de la familia'}, 'it': {'per_night': '/ notte', 'extra_child': '+{x} / ora per un 2° bambino', 'meal': 'Oltre 5 ore: un pasto per la tata', 'travel': 'Trasporti, biglietti e alloggio a carico della famiglia'}, 'nl': {'per_night': '/ nacht', 'extra_child': '+{x} / uur voor een 2e kind', 'meal': 'Langer dan 5 uur: graag een maaltijd voor de nanny', 'travel': 'Vervoer, tickets en verblijf betaalt het gezin'}, 'id': {'per_night': '/ malam', 'extra_child': '+{x} / jam untuk anak ke-2', 'meal': 'Lebih dari 5 jam: mohon sediakan makan untuk pengasuh', 'travel': 'Transportasi, tiket, dan penginapan ditanggung keluarga'}}.items(): P[_l].update(_d)

def idr(n): return f"IDR {n:,}".replace(",", " ") if False else f"IDR {n:,}"

def money(n):
    """Сумма в IDR + место для пересчёта."""
    return f'<span class="money" data-idr="{n}"><b>{idr(n)}</b><small class="conv"></small></span>'

def price_cells(slug, lang):
    p = P[lang]; x = PRICES.get(slug)
    if not x: return f'<span class="muted">{p["on_request"]}</span>', "—"
    unit = {"hour": p["per_hour"], "day": p["per_day"], "night": p["per_night"]}[x["unit"]]
    rate = f'{money(x["idr"])} {unit}'
    extra = []
    if x.get("extra_child"): extra.append(p["extra_child"].format(x=idr(x["extra_child"])))
    if x.get("meal"): extra.append(p["meal"])
    if x.get("travel"): extra.append(p["travel"])
    if extra: rate += "".join(f'<br><span class="note">{e}</span>' for e in extra)
    if x["unit"] == "hour":
        return rate, f'{p["min_h"].format(n=x["min_h"])}<br><span class="note">{p["min_total"]}: </span>{money(x["idr"]*x["min_h"])}'
    if x["unit"] == "day":
        return rate, p["day_note"].format(n=x["hours"])
    return rate, "—"

def price_line(slug, lang):
    """Строка цены для страницы услуги (или пусто)."""
    x = PRICES.get(slug)
    if not x: return ""
    a, b = price_cells(slug, lang)
    return f'<div class="price-line">{a}<span class="pl-sep">·</span><span>{b.split("<br>")[0]}</span></div>'

def cur_select(lang):
    opts = "".join(f'<option value="{c}"{" selected" if c==DEFAULT_CUR[lang] else ""}>{c}</option>' for c in CURRENCIES)
    return (f'<div class="cur-bar"><label for="curSel">{P[lang]["show_in"]}</label> <select id="curSel" class="cur-sel">{opts}</select>'
            f'<span class="note">{P[lang]["approx"]}</span></div>')

def js(lang):
    import json
    return ("<script>(()=>{const FB=" + json.dumps(FALLBACK) + ",DEF=" + json.dumps(DEFAULT_CUR[lang]) + ",LOC=" + json.dumps(lang) + ";"
      "let R=FB;const sel=document.getElementById('curSel');let cur=DEF;"
      "try{const s=localStorage.getItem('bn_cur');if(s&&FB[s])cur=s}catch(e){}"
      "if(sel)sel.value=cur;"
      "const fmt=(v,c)=>{try{return new Intl.NumberFormat(LOC,{style:'currency',currency:c,maximumFractionDigits:(['IDR','KRW','JPY','INR','RUB'].includes(c)?0:2)}).format(v)}catch(e){return v.toFixed(2)+' '+c}};"
      "const paint=()=>document.querySelectorAll('.money').forEach(m=>{const n=+m.dataset.idr,o=m.querySelector('.conv');"
      "o.textContent=(cur==='IDR'||!R[cur])?'':' ≈ '+fmt(n*R[cur],cur)});"
      "paint();if(sel)sel.addEventListener('change',()=>{cur=sel.value;try{localStorage.setItem('bn_cur',cur)}catch(e){}paint()});"
      "fetch('https://open.er-api.com/v6/latest/IDR').then(r=>r.json()).then(d=>{if(d&&d.rates){R=Object.assign({},FB,d.rates);paint()}}).catch(()=>{})})()</script>")

CSS = """
.money b{font-weight:700;color:var(--ink)}.money .conv{color:var(--muted);font-weight:500;margin-left:4px;white-space:nowrap}
.cur-bar{display:flex;flex-wrap:wrap;align-items:center;gap:10px 12px;margin:0 0 16px}
.cur-bar label{font-weight:600}
.cur-sel{font:600 1rem Inter,system-ui,sans-serif;padding:9px 34px 9px 14px;border:1px solid var(--line);border-radius:999px;background:var(--surface);color:var(--ink);-webkit-appearance:none;appearance:none;background-image:linear-gradient(45deg,transparent 50%,var(--ink) 50%),linear-gradient(135deg,var(--ink) 50%,transparent 50%);background-position:calc(100% - 18px) 55%,calc(100% - 13px) 55%;background-size:5px 5px;background-repeat:no-repeat}
.cur-bar .note{flex-basis:100%}
.price-table .muted{color:var(--muted)}
.price-line{display:inline-flex;flex-wrap:wrap;align-items:baseline;gap:6px 8px;background:var(--brand-2);border-radius:14px;padding:10px 16px;margin:4px 0 6px;font-size:1rem}
.pl-sep{color:var(--muted)}
@media(max-width:560px){.price-table td,.price-table th{padding:12px 12px;font-size:.93rem}.money .conv{display:block;margin:2px 0 0}}
"""
