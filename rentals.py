# -*- coding: utf-8 -*-
"""Прокат детского оборудования и ограждения бассейнов (EN/RU).
Цены — заглушки [IDR —]; ориентир рынка (сент. 2026, по сайтам прокатов): кроватка ~100 000 IDR/день,
ограждение бассейна ~200–250 000 IDR/день, установка 30–60 мин. Заполнить реальными тарифами."""

CATS = [
 dict(slug="pool-fence", icon="🛡️",
  en=("Pool fences","Removable child-safety fence installed around your villa pool."),
  ru=("Ограждение бассейна","Съёмное защитное ограждение вокруг бассейна виллы."),
  items_en=["Removable mesh fence, ~1.2 m high","Self-closing, self-latching gate","Installed around the full pool edge","Removed at check-out, no damage"],
  items_ru=["Съёмная сетка высотой ~1,2 м","Калитка с самозакрывающимся замком","Устанавливаем по всему периметру бассейна","Снимаем при выезде без следов"]),
 dict(slug="sleep", icon="🛏️",
  en=("Cots & sleep","Full-size cots, travel cots and bassinets with fresh linen."),
  ru=("Кроватки и сон","Кроватки, манежи-кроватки и люльки со свежим бельём."),
  items_en=["Full-size cot with mattress","Travel cot / playpen","Bassinet for newborns","Portable blackout blinds","White-noise machine","Baby monitor"],
  items_ru=["Кроватка с матрасом","Манеж-кроватка","Люлька для новорождённых","Переносные блэкаут-шторы","Генератор белого шума","Радионяня"]),
 dict(slug="strollers", icon="👶",
  en=("Strollers & carriers","Light travel strollers, doubles and baby carriers."),
  ru=("Коляски и переноски","Лёгкие прогулочные, двойные коляски и эргорюкзаки."),
  items_en=["Compact travel stroller","All-terrain stroller for beach paths","Double stroller","Ergonomic baby carrier","Stroller fan & rain cover"],
  items_ru=["Компактная прогулочная коляска","Коляска для пляжных дорожек","Коляска для двойни","Эргорюкзак","Вентилятор и дождевик для коляски"]),
 dict(slug="car-seats", icon="🚗",
  en=("Car seats","Infant, convertible and booster seats — fitted for you."),
  ru=("Автокресла","Люльки, автокресла и бустеры — установим за вас."),
  items_en=["Infant capsule (0–13 kg)","Convertible seat (0–18 kg)","Forward-facing seat (9–25 kg)","Booster (15–36 kg)","Fitted into your driver's car on request"],
  items_ru=["Автолюлька (0–13 кг)","Автокресло 0–18 кг","Автокресло 9–25 кг","Бустер 15–36 кг","Установим в машину вашего водителя"]),
 dict(slug="feeding-bath", icon="🍼",
  en=("Feeding & bath","High chairs, sterilisers and baby baths."),
  ru=("Кормление и купание","Стульчики, стерилизаторы и ванночки."),
  items_en=["High chair","Travel booster seat","Bottle steriliser","Bottle warmer","Baby bath & bath seat","Breast pump (sealed kit)"],
  items_ru=["Стульчик для кормления","Дорожный стульчик-бустер","Стерилизатор бутылочек","Подогреватель","Ванночка и горка для купания","Молокоотсос (новый комплект)"]),
 dict(slug="play", icon="🧸",
  en=("Play & safety","Toy packs, play mats and baby-proofing kits."),
  ru=("Игры и безопасность","Наборы игрушек, коврики и защита для дома."),
  items_en=["Age-matched toy pack","Play mat & bouncer","Baby gate for stairs","Socket covers & corner guards","Pool & beach toy set","Life vest for kids"],
  items_ru=["Набор игрушек по возрасту","Развивающий коврик и шезлонг","Ворота на лестницу","Заглушки для розеток и уголки","Игрушки для бассейна и пляжа","Детский спасательный жилет"]),
]

RT = {
"en": dict(nav="Rentals", h1="Baby equipment hire in Bali", title="Baby Equipment Hire in Bali — Cots, Strollers, Car Seats, Pool Fences",
  lead="Travel light. We deliver clean, checked baby gear to your hotel or villa and set it up — then collect it when you leave.",
  sec_h="Everything for little travellers", from_="from", per_day="/ day",
  how_h="How rental works", how=[("Send your list","On WhatsApp: dates, address and what you need."),("We deliver & set up","Cleaned, sanitised and checked — installed before you arrive if you like."),("We collect","Pick-up from your villa or hotel on the last day.")],
  pack_h="Arrival pack", pack_p="Cot, stroller, car seat and high chair — delivered before you land. The easiest start to a Bali holiday with a baby.",
  combo_h="Rental + nanny", combo_p="Add a nanny to your booking — she'll know every piece of gear already set up in your villa.",
  hygiene=["Cleaned and sanitised after every rental","Checked for wear and recalls","Fresh linen for every cot"],
  ask="Ask what's available", msg="Hi! I'd like to rent baby equipment. Dates: , address: , items: ",
  home_h="Baby gear & pool fences", home_p="Don't fly with a cot and a stroller. We deliver everything to your villa.",
  all="See all rentals",
  pf=dict(title="Pool Fence Hire in Bali — Removable Child-Safety Fence for Villas", h1="Pool fence hire for your Bali villa",
    lead="Most Bali villa pools have no fence. We install a removable child-safety fence around your pool before you arrive — and take it away when you leave.",
    why_h="Why a pool fence matters", why=["Many Bali villas have a pool right outside the bedroom doors — often with no barrier.","Toddlers are fast, and drowning is quiet: it doesn't look like the splashing in films.","A fence gives you a safety layer for the moments you look away — unpacking, cooking, answering the door."],
    what_h="What you get", steps_h="How installation works",
    steps=[("Send photos of the pool","A short video or a few photos on WhatsApp is enough to measure."),("We confirm with the villa","We agree installation with the villa manager if needed."),("Installation in 30–60 min","Fixed around the full pool edge with a self-latching gate."),("Removed at check-out","No drilling marks left behind.")],
    note="A fence is an extra layer of protection, not a replacement for supervision. Always watch children near water.",
    faq=[("Will it damage the villa?","The fence is designed to be removed without leaving marks. Tell us about the pool deck surface and we'll confirm the fitting method."),("Does the villa need to agree?","Usually villa managers welcome it; we can coordinate with them directly."),("Can we still use the pool?","Yes — adults open the gate; it closes and latches by itself."),("How far in advance should I book?","As early as possible in peak season (July–August, Christmas). Installation can be done before you arrive.")],
    msg="Hi! I need a pool fence. Villa area: , dates: , pool size/photos: ", cta="Get a pool fence quote"),
),
"ru": dict(nav="Прокат", h1="Прокат детского оборудования на Бали", title="Прокат детских вещей на Бали — кроватки, коляски, автокресла, ограждение бассейна",
  lead="Летите налегке. Привезём чистое проверенное оборудование в отель или на виллу, соберём — и заберём при выезде.",
  sec_h="Всё для маленьких путешественников", from_="от", per_day="/ день",
  how_h="Как работает прокат", how=[("Пришлите список","В WhatsApp: даты, адрес и что нужно."),("Привезём и соберём","Всё вымыто, обработано и проверено — можем подготовить до вашего приезда."),("Заберём","В последний день заберём с виллы или из отеля.")],
  pack_h="Набор к приезду", pack_p="Кроватка, коляска, автокресло и стульчик — ждут вас ещё до посадки самолёта. Самый простой старт отпуска с малышом.",
  combo_h="Прокат + няня", combo_p="Добавьте к брони няню — она уже будет знать всё оборудование, установленное на вашей вилле.",
  hygiene=["Мойка и дезинфекция после каждого проката","Проверка износа и отзывов производителя","Свежее бельё для каждой кроватки"],
  ask="Узнать о наличии", msg="Здравствуйте! Хочу взять в прокат детские вещи. Даты: , адрес: , что нужно: ",
  home_h="Детские вещи и ограждение бассейна", home_p="Не везите кроватку и коляску в самолёте. Привезём всё на виллу.",
  all="Весь прокат",
  pf=dict(title="Ограждение бассейна на Бали — аренда съёмного детского ограждения для виллы", h1="Ограждение бассейна на вашей вилле",
    lead="У большинства вилл на Бали бассейн без ограждения. Мы установим съёмное детское ограждение до вашего приезда и снимем при выезде.",
    why_h="Зачем нужно ограждение", why=["На многих виллах бассейн прямо за дверью спальни — и никакого барьера.","Малыши очень быстрые, а тонут тихо: это не похоже на всплески из фильмов.","Ограждение страхует в те минуты, когда вы отвлеклись: распаковка, готовка, звонок в дверь."],
    what_h="Что входит", steps_h="Как проходит установка",
    steps=[("Пришлите фото бассейна","Короткое видео или несколько фото в WhatsApp — этого хватит для замера."),("Согласуем с виллой","При необходимости договоримся с управляющим."),("Установка за 30–60 минут","По всему периметру бассейна, с самозакрывающейся калиткой."),("Снимем при выезде","Без следов крепления.")],
    note="Ограждение — дополнительная защита, а не замена присмотра. Всегда следите за детьми у воды.",
    faq=[("Не повредит ли это виллу?","Ограждение рассчитано на снятие без следов. Расскажите о покрытии вокруг бассейна — подтвердим способ крепления."),("Нужно ли согласие виллы?","Обычно управляющие только рады; можем договориться с ними сами."),("Можно ли пользоваться бассейном?","Да — взрослые открывают калитку, она закрывается и защёлкивается сама."),("За сколько бронировать?","В высокий сезон (июль–август, Новый год) — как можно раньше. Установим до вашего приезда.")],
    msg="Здравствуйте! Нужно ограждение бассейна. Район виллы: , даты: , размер/фото бассейна: ", cta="Рассчитать ограждение"),
)}

CSS = """
.rent-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.rent-card{background:var(--surface);border:1px solid var(--line);border-radius:22px;overflow:hidden;text-decoration:none;color:inherit;display:flex;flex-direction:column;transition:box-shadow .2s,border-color .2s}
.rent-card:hover{box-shadow:0 12px 30px rgba(27,43,39,.08);border-color:#cfd9d4}
.rent-card img{width:100%;height:auto;aspect-ratio:3/2;object-fit:cover;display:block}
.rent-card .rc{padding:20px 22px 22px}.rent-card h3{margin:0 0 6px}.rent-card p{margin:0 0 12px;color:var(--muted);font-size:.95rem}
.rent-card ul{margin:0;padding:0;list-style:none;font-size:.9rem}.rent-card li{padding:5px 0;border-top:1px solid var(--line)}
.price-tag{display:inline-block;margin-top:12px;font-weight:600;color:var(--brand)}
.fence-hero{display:grid;grid-template-columns:1.2fr 1fr;gap:0;border-radius:32px;overflow:hidden;background:#0E3B4A;color:#E2F1F5}
.fence-hero .fh-txt{padding:48px}.fence-hero h2{color:#fff;font-size:clamp(1.7rem,3vw,2.4rem)}.fence-hero img{width:100%;height:100%;object-fit:cover;min-height:320px}
.fence-hero ul{padding-left:1.1em;margin:0 0 22px}.fence-hero li{margin:.35em 0}
.combo{display:grid;grid-template-columns:1fr 1fr;gap:18px}.combo>div{background:var(--brand-2);border-radius:24px;padding:30px}
.hyg{display:flex;gap:18px;flex-wrap:wrap;color:var(--muted);font-size:.93rem;list-style:none;padding:0;margin:18px 0 0}.hyg li::before{content:"✓ ";color:var(--brand);font-weight:700}
.why-list{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.why-list div{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:22px}
.safety-note{background:#FFF4E8;border-left:4px solid var(--accent);border-radius:12px;padding:16px 20px;margin:24px 0;font-weight:600}
@media(max-width:960px){.rent-grid{grid-template-columns:1fr 1fr}.fence-hero,.combo{grid-template-columns:1fr}.why-list{grid-template-columns:1fr}}
@media(max-width:560px){.rent-grid{grid-template-columns:1fr}.fence-hero .fh-txt{padding:28px}}
"""

def cat_name(c, lang): return c[lang][0]

def rent_grid(lang, home, cats=None):
    out = []
    for c in (cats or CATS):
        name, desc = c[lang]; items = c["items_"+lang][:4]
        out.append(f'<a class="rent-card reveal" href="{home}rentals/{c["slug"]}/index.html"><img src="{{ROOT}}img/rent/{c["slug"]}.jpg" alt="{name}" loading="lazy" width="1200" height="800">'
                   f'<div class="rc"><h3>{c["icon"]} {name}</h3><p>{desc}</p><ul>' + "".join(f"<li>{i}</li>" for i in items) +
                   f'</ul><span class="price-tag">{RT[lang]["from_"]} [IDR —]{RT[lang]["per_day"]}</span></div></a>')
    return '<div class="rent-grid">' + "".join(out) + "</div>"

def fence_banner(lang, home, btn):
    r = RT[lang]; pf = r["pf"]; c = CATS[0]
    return (f'<div class="fence-hero reveal"><div class="fh-txt"><span class="eyebrow">🛡️ {c[lang][0]}</span><h2>{pf["h1"]}</h2><p>{pf["lead"]}</p>'
            f'<ul>' + "".join(f"<li>{i}</li>" for i in c["items_"+lang]) + f'</ul>{btn(pf["cta"], pf["msg"])} '
            f'<a class="btn btn-ghost" style="color:#fff;border-color:rgba(255,255,255,.35)" href="{home}rentals/pool-fence/index.html">→</a></div>'
            f'<img src="{{ROOT}}img/rent/pool-fence.jpg" alt="{pf["h1"]}" loading="lazy"></div>')
