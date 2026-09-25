# -*- coding: utf-8 -*-
"""Static site generator: Sanur nanny agency, EN (root) + RU (/ru/). Guide plan comes from build_seo.py."""
import html, urllib.parse, pathlib, shutil

HERE = pathlib.Path(__file__).parent
ns = {}
exec((HERE/"build_seo.py").read_text(encoding="utf-8").split("# ---------------------------------------------------------------- СЕМАНТИКА")[0], ns)
A, HUBS = ns["A"], ns["HUBS"]
for i, a in enumerate(A, 1): a["id"] = f"A{i:03d}"

# ---- настройки бизнеса (заполнить)
BRAND = "Sanur Nannies"
WA = "62XXXXXXXXXX"            # номер WhatsApp: 62…, без +
EMAIL = "hello@example.com"
DOMAIN = "https://[domain]"     # после покупки домена
OUT = HERE/"site"
CSS = (HERE/"src/style.css").read_text(encoding="utf-8")
WA_SVG = (HERE/"src/wa.svg").read_text(encoding="utf-8")

SERVICES = ["hourly-babysitter","day-nanny","night-nanny","newborn-nanny","travel-nanny","hotel-villa-babysitting","event-babysitting","long-term-nanny"]
ICONS = ["🕒","☀️","🌙","👶","🚤","🏝️","🎉","🏡"]
LIVE_ARTICLE = "A026"   # статья-образец

T = {
"en": dict(
  prefix="", html_lang="en", other="ru", other_label="RU", locale="en",
  wa_default="Hi! I'd like to book a nanny in Sanur.",
  wa_service="Hi! I'm interested in: {s}. Dates: ",
  nav=["Services","Prices","How it works","Safety","Sanur guides"], home="Home",
  svc=[("Hourly babysitter","Dinner out, spa, a surf lesson — from 3 hours."),("Full-day nanny","Beach, pool, naps and meals while you get a real holiday."),("Night nanny","Settling, feeds and night wakings so you can sleep."),("Newborn & baby care","Nannies experienced with babies under 12 months."),("Travel nanny","Joins your family on day trips and island hops."),("Hotel & villa babysitting","We come to your hotel or villa anywhere in Sanur."),("Weddings & events","Kids' corner and sitters for celebrations."),("Long-term nanny","For expat families living in Sanur.")],
  wa_btn="Chat on WhatsApp", wa_short="WhatsApp", book="Book on WhatsApp", see_prices="See prices", prices="Prices",
  title_home="Nanny & Babysitter in Sanur, Bali", desc_home="English-speaking, first-aid trained nannies and babysitters in Sanur. Hotel & villa visits, night nannies, day trips. Book in minutes on WhatsApp.",
  eyebrow="Sanur · Bali", h1="Trusted nannies for your family holiday in Sanur",
  lead="English-speaking, first-aid trained babysitters who come to your hotel or villa — so you can enjoy dinner, the spa or a quiet sunrise.",
  trust=["Background-checked","First aid & CPR","Reply within 15 min"], chip="🟢 Nanny available tonight", photo="Nanny playing with a child in a swimming pool",
  svc_h="Care that fits your trip", svc_p="From a single evening to a full season in Bali.",
  steps_h="Booked in three messages", steps=[("Message us on WhatsApp","Tell us dates, hours, kids' ages and where you're staying."),("Meet your nanny","We send a profile and a short intro. Want a video call first? Just ask."),("Enjoy your time","She arrives at your hotel or villa. Photo updates on WhatsApp, pay after the session.")],
  safe_h="Safety isn't a feature. It's the job.", safe_p="Every nanny is interviewed in person, reference-checked and trained before her first family.", safe_btn="Our safety standards",
  safe_list=["ID and reference checks","Paediatric first aid & CPR","Pool and beach supervision rules","Trial meeting before the first booking"],
  faq_h="Questions parents ask", faq=[("How quickly can I book?","Often the same day. For evenings and peak season (July–August, Christmas) message us 2–3 days ahead."),("Do your nannies speak English?","Yes — every nanny communicates comfortably in English. We tell you each nanny's level honestly."),("Are nannies first-aid trained?","Every nanny holds a current paediatric first aid & CPR certificate. We can show it before your booking."),("Where do you work?","Anywhere in Sanur — hotels, villas and homes. Day trips across Bali with our travel nanny service."),("How do I pay?","Cash (IDR) or bank transfer after the session. No deposit for single bookings."),("Can a nanny look after my newborn?","Yes. We match babies with nannies who have specific newborn experience.")],
  guides_h="Sanur with kids", guides_p="Local guides from people who spend every day on these beaches.", n_guides="guides",
  final_h="Need a nanny in Sanur?", final_p="Tell us your dates — we'll reply with an available nanny.", final_btn="Message us on WhatsApp",
  services_t="Nanny Services in Sanur", services_h="Our services", services_d="Hourly babysitters, full-day and night nannies, newborn care and travel nannies in Sanur, Bali.",
  svc_title="{s} in Sanur, Bali", svc_h1="{s} in Sanur", check="Check availability", how="How it works", faq_short="FAQ",
  prices_t="Nanny & Babysitter Prices in Sanur", prices_h="Simple, transparent prices", prices_p="No deposit for single bookings. Pay after the session.", th=["Service","Rate","Minimum"], price_note="Rates for up to 2 children. Transport within Sanur included.", quote="Get a quote",
  hiw_t="How Booking Works", hiw_d="Book a nanny in Sanur in three WhatsApp messages.",
  safety_t="Our Safety Standards", safety_d="How we select, check and train every nanny in Sanur.",
  safety_body=[("Selection","In-person interview, ID check, at least two references from previous families."),("Training","Current paediatric first aid & CPR certificate. Pool and beach supervision rules."),("On every booking","Handover checklist, emergency contacts, WhatsApp updates.")],
  faq_t="Frequently asked questions", faq_d="Answers about booking a nanny in Sanur.",
  careers_nav="Become a nanny", careers_t="Nanny Jobs in Sanur", careers_h="Become a nanny", careers_p="We work with experienced, English-speaking nannies in Sanur. First aid training provided.", apply="Apply on WhatsApp", apply_msg="Hi! I would like to apply as a nanny.",
  guides_t="Sanur Family Guides", guides_hh="Sanur family guides", soon="coming soon",
  company="Company", services_f="Services", guides_f="Guides", foot_p="Trusted English-speaking nannies and babysitters for families in Sanur, Bali.",
  hubs={h:v[0] for h,v in HUBS.items()},
),
"ru": dict(
  prefix="ru/", html_lang="ru", other="en", other_label="EN", locale="ru",
  wa_default="Здравствуйте! Хочу забронировать няню в Сануре.",
  wa_service="Здравствуйте! Интересует: {s}. Даты: ",
  nav=["Услуги","Цены","Как это работает","Безопасность","Гайды по Сануру"], home="Главная",
  svc=[("Няня на час","Ужин, спа, урок сёрфинга — от 3 часов."),("Няня на весь день","Пляж, бассейн, сон и еда, пока у вас настоящий отпуск."),("Ночная няня","Укладывание, кормления и ночные пробуждения — а вы высыпаетесь."),("Няня для малыша","Няни с опытом ухода за детьми до года."),("Няня в поездки","Едет с семьёй на экскурсии и острова."),("Няня в отель или виллу","Приедем в ваш отель или виллу в любой части Санура."),("Свадьбы и мероприятия","Детская зона и няни на праздники."),("Няня на длительный срок","Для семей, которые живут в Сануре.")],
  wa_btn="Написать в WhatsApp", wa_short="WhatsApp", book="Забронировать в WhatsApp", see_prices="Цены", prices="Цены",
  title_home="Няня в Сануре, Бали — бебиситтеры для семей", desc_home="Проверенные няни с сертификатом первой помощи в Сануре. Приезд в отель и виллу, ночные няни, поездки. Бронь за пару минут в WhatsApp.",
  eyebrow="Санур · Бали", h1="Надёжные няни для семейного отдыха в Сануре",
  lead="Опытные няни с сертификатом первой помощи приедут в ваш отель или виллу — а вы спокойно поужинаете, сходите в спа или встретите рассвет вдвоём.",
  trust=["Проверенные няни","Первая помощь и СЛР","Ответ за 15 минут"], chip="🟢 Няня свободна сегодня вечером", photo="Няня играет с ребёнком в бассейне",
  svc_h="Помощь под ваш формат отдыха", svc_p="От одного вечера до целого сезона на Бали.",
  steps_h="Бронь в три сообщения", steps=[("Напишите в WhatsApp","Даты, часы, возраст детей и где вы живёте."),("Познакомьтесь с няней","Пришлём профиль и короткое знакомство. Нужен видеозвонок — устроим."),("Отдыхайте","Няня приезжает в отель или виллу. Фото в WhatsApp, оплата после смены.")],
  safe_h="Безопасность — это не опция. Это наша работа.", safe_p="Каждую няню мы лично собеседуем, проверяем рекомендации и обучаем до первой семьи.", safe_btn="Наши стандарты безопасности",
  safe_list=["Проверка документов и рекомендаций","Детская первая помощь и СЛР","Правила присмотра у бассейна и на пляже","Знакомство до первой брони"],
  faq_h="Частые вопросы родителей", faq=[("Как быстро можно забронировать?","Часто — в тот же день. На вечер и в высокий сезон (июль–август, Новый год) лучше написать за 2–3 дня."),("Няни говорят по-русски?","Все няни свободно общаются на английском. Русскоязычных нянь подбираем по запросу — честно скажем, есть ли свободная."),("У нянь есть навыки первой помощи?","У каждой няни действующий сертификат детской первой помощи и СЛР. Покажем до брони."),("Где вы работаете?","Весь Санур — отели, виллы, дома. Поездки по Бали — с услугой «няня в поездки»."),("Как оплатить?","Наличными (рупии) или переводом после смены. Без предоплаты для разовых броней."),("Няня посидит с новорождённым?","Да. Для малышей подбираем нянь с опытом ухода за новорождёнными.")],
  guides_h="Санур с детьми", guides_p="Гайды от людей, которые каждый день на этих пляжах.", n_guides="статей",
  final_h="Нужна няня в Сануре?", final_p="Напишите даты — ответим, кто из нянь свободен.", final_btn="Написать в WhatsApp",
  services_t="Услуги нянь в Сануре", services_h="Наши услуги", services_d="Няня на час, на день, ночная няня, уход за малышами и няня в поездки — Санур, Бали.",
  svc_title="{s} в Сануре, Бали", svc_h1="{s} в Сануре", check="Узнать, кто свободен", how="Как это работает", faq_short="Вопросы",
  prices_t="Цены на няню в Сануре", prices_h="Простые и понятные цены", prices_p="Без предоплаты за разовые брони. Оплата после смены.", th=["Услуга","Цена","Минимум"], price_note="Цена за 1–2 детей. Дорога по Сануру включена.", quote="Узнать цену",
  hiw_t="Как забронировать няню", hiw_d="Бронь няни в Сануре — три сообщения в WhatsApp.",
  safety_t="Стандарты безопасности", safety_d="Как мы отбираем, проверяем и обучаем нянь в Сануре.",
  safety_body=[("Отбор","Личное собеседование, проверка документов, минимум две рекомендации от семей."),("Обучение","Действующий сертификат детской первой помощи и СЛР. Правила присмотра у воды."),("На каждой смене","Чек-лист передачи ребёнка, экстренные контакты, отчёты в WhatsApp.")],
  faq_t="Частые вопросы", faq_d="Ответы о бронировании няни в Сануре.",
  careers_nav="Работа няней", careers_t="Работа няней в Сануре", careers_h="Работа няней", careers_p="Ищем опытных нянь со знанием английского или русского. Обучение первой помощи — за наш счёт.", apply="Откликнуться в WhatsApp", apply_msg="Здравствуйте! Хочу работать няней.",
  guides_t="Гайды для семей в Сануре", guides_hh="Гайды для семей в Сануре", soon="скоро",
  company="Компания", services_f="Услуги", guides_f="Гайды", foot_p="Надёжные няни и бебиситтеры для семей в Сануре, Бали.",
  hubs={"H01":"Няня в Сануре","H02":"Санур с детьми: чем заняться","H03":"Где жить с детьми","H04":"Здоровье и безопасность","H05":"Еда для семьи","H06":"Перелёт и логистика","H07":"Поездки из Санура","H08":"Жизнь в Сануре с детьми"},
)}

def wa(text): return f"https://wa.me/{WA}?text={urllib.parse.quote(text)}"
def hub_slug(h): return HUBS[h][1].split("/")[2]

def build(lang):
    t = T[lang]
    def btn(text=None, msg=None, cls=""):
        return f'<a class="btn btn-wa {cls}" href="{wa(msg or t["wa_default"])}" target="_blank" rel="noopener">{WA_SVG}{text or t["wa_btn"]}</a>'

    def page(path, title, desc, body, schema="", other_exists=True):
        full = t["prefix"] + path
        depth = full.count("/")
        root = "../" * depth           # корень сайта
        home = root + t["prefix"]      # главная текущего языка
        other_path = T[t["other"]]["prefix"] + path
        alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{DOMAIN}/{T[l]["prefix"]}{path}">' for l in T) + f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{path}">' if other_exists else ""
        switch = f'<a class="lang" href="{root}{other_path}index.html">{t["other_label"]}</a>' if other_exists else f'<a class="lang" href="{root}{T[t["other"]]["prefix"]}index.html">{t["other_label"]}</a>'
        links = ["services","prices","how-it-works","safety","guides"]
        nav = f"""<header><div class="wrap nav"><a class="logo" href="{home}index.html">Sanur<span>.</span>Nannies</a>
<nav class="links">{''.join(f'<a href="{home}{l}/index.html">{n}</a>' for l,n in zip(links,t["nav"]))}</nav>
<div class="right">{switch}{btn(t["wa_short"], cls="btn-sm")}</div></div></header>"""
        foot = f"""<footer><div class="wrap fgrid"><div><div class="logo">{BRAND}</div><p>{t["foot_p"]}</p>{btn()}</div>
<div><b>{t["services_f"]}</b>{''.join(f'<a href="{home}services/{s}/index.html">{n}</a>' for s,(n,_) in list(zip(SERVICES,t["svc"]))[:5])}</div>
<div><b>{t["company"]}</b>{''.join(f'<a href="{home}{l}/index.html">{n}</a>' for l,n in zip(["how-it-works","safety","prices","faq","careers"],[t["how"],t["nav"][3],t["prices"],t["faq_short"],t["careers_nav"]]))}</div>
<div><b>{t["guides_f"]}</b>{''.join(f'<a href="{home}guides/{hub_slug(h)}/index.html">{t["hubs"][h]}</a>' for h in list(HUBS)[:5])}</div></div>
<div class="wrap"><p class="note" style="margin-top:28px">© 2026 {BRAND} · Sanur, Bali · <a href="mailto:{EMAIL}">{EMAIL}</a></p></div></footer>
<a class="fab" href="{wa(t['wa_default'])}" target="_blank" rel="noopener" aria-label="{t['wa_btn']}">{WA_SVG}</a>"""
        doc = f"""<!doctype html><html lang="{t['html_lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} | {BRAND}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{DOMAIN}/{full}">{alt}
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css">{schema}</head><body>{nav}<main>{body.replace("{ROOT}", root)}</main>{foot}</body></html>"""
        f = OUT/full/"index.html"
        f.parent.mkdir(parents=True, exist_ok=True); f.write_text(doc, encoding="utf-8")
        return root, home

    def crumbs(home, *items):
        parts = [f'<a href="{home}index.html">{t["home"]}</a>'] + [f'<a href="{home}{u}index.html">{n}</a>' if u else n for n,u in items]
        return '<div class="crumbs">' + " / ".join(parts) + "</div>"

    def home_rel(path): return "../" * path.count("/")   # от страницы до главной языка

    def services_grid(home):
        return '<div class="grid">' + "".join(f'<a class="card card-img" href="{home}services/{s}/index.html"><img class="thumb" src="{{ROOT}}img/{s}.jpg" alt="" loading="lazy" width="960" height="640"><div class="ico">{i}</div><h3>{n}</h3><p>{d}</p></a>' for s,i,(n,d) in zip(SERVICES,ICONS,t["svc"])) + "</div>"
    steps = '<div class="steps">' + "".join(f'<div class="step"><h3>{a}</h3><p>{b}</p></div>' for a,b in t["steps"]) + "</div>"
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in t["faq"])
    hub_cards = lambda home: '<div class="grid">' + "".join(f'<a class="card" href="{home}guides/{hub_slug(h)}/index.html"><h3>{t["hubs"][h]}</h3><p>{sum(1 for a in A if a["hub"]==h)} {t["n_guides"]}</p></a>' for h in HUBS) + "</div>"

    # HOME
    h = ""
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ChildCare","name":"{BRAND}","areaServed":"Sanur, Bali","telephone":"+{WA}","url":"{DOMAIN}/{t["prefix"]}"}}</script>'
    page("", t["title_home"], t["desc_home"], f"""<div class="wrap hero"><div><span class="eyebrow">{t["eyebrow"]}</span><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p>
<div class="cta-row">{btn(t["book"])}<a class="btn btn-ghost" href="prices/index.html">{t["see_prices"]}</a></div>
<ul class="trust">{''.join(f'<li>{x}</li>' for x in t["trust"])}</ul></div>
<div class="photo"><img src="{{ROOT}}img/hero.jpg" alt="{t['photo']}" width="960" height="640" fetchpriority="high"><div class="chip">{t["chip"]}</div></div></div>
<section><div class="wrap"><div class="sec-head"><h2>{t["svc_h"]}</h2><p>{t["svc_p"]}</p></div>{services_grid("")}</div></section>
<section><div class="wrap"><div class="sec-head"><h2>{t["steps_h"]}</h2></div>{steps}</div></section>
<section><div class="wrap"><div class="band"><div><h2>{t["safe_h"]}</h2><p>{t["safe_p"]}</p><a class="btn btn-ghost" style="color:#fff;border-color:rgba(255,255,255,.35)" href="safety/index.html">{t["safe_btn"]}</a></div>
<ul>{''.join(f'<li>{x}</li>' for x in t["safe_list"])}</ul></div></div></section>
<section><div class="wrap"><div class="sec-head"><h2>{t["faq_h"]}</h2></div>{faq}</div></section>
<section><div class="wrap"><div class="sec-head"><h2>{t["guides_h"]}</h2><p>{t["guides_p"]}</p></div>{hub_cards("")}</div></section>
<div class="final"><h2>{t["final_h"]}</h2><p class="lead" style="margin:0 auto 24px">{t["final_p"]}</p>{btn(t["final_btn"])}</div>""", schema)

    # SERVICES
    page("services/", t["services_t"], t["services_d"], f'<div class="wrap">{crumbs("../",(t["services_h"],None))}<section><div class="sec-head"><h1>{t["services_h"]}</h1></div>{services_grid("../")}</section></div>')
    for s,i,(n,d) in zip(SERVICES,ICONS,t["svc"]):
        hm = "../../"
        page(f"services/{s}/", t["svc_title"].format(s=n), f"{t['svc_h1'].format(s=n)}: {d}", f"""<div class="wrap">{crumbs(hm,(t["services_h"],"services/"),(n,None))}
<div class="hero" style="padding-top:32px"><div><span class="eyebrow">{i} {n}</span><h1>{t["svc_h1"].format(s=n)}</h1><p class="lead">{d}</p>
<div class="cta-row">{btn(t["check"], t["wa_service"].format(s=n))}<a class="btn btn-ghost" href="{hm}prices/index.html">{t["prices"]}</a></div></div>
<div class="photo"><img src="{{ROOT}}img/{s}.jpg" alt="{n}" width="960" height="640"></div></div>
<section><div class="sec-head"><h2>{t["how"]}</h2></div>{steps}</section><section><div class="sec-head"><h2>{t["faq_short"]}</h2></div>{faq}</section></div>""")

    rows = "".join(f"<tr><td>{n}</td><td>[IDR —]</td><td>[—]</td></tr>" for n,_ in t["svc"])
    page("prices/", t["prices_t"], t["prices_p"], f"""<div class="wrap">{crumbs("../",(t["prices"],None))}<section><div class="sec-head"><h1>{t["prices_h"]}</h1><p>{t["prices_p"]}</p></div>
<table class="price-table"><tr>{''.join(f'<th>{x}</th>' for x in t["th"])}</tr>{rows}</table><p class="note" style="margin-top:14px">{t["price_note"]}</p><div class="cta-row">{btn(t["quote"])}</div></section></div>""")
    page("how-it-works/", t["hiw_t"], t["hiw_d"], f'<div class="wrap">{crumbs("../",(t["how"],None))}<section><div class="sec-head"><h1>{t["how"]}</h1></div>{steps}<div class="cta-row">{btn()}</div></section></div>')
    page("safety/", t["safety_t"], t["safety_d"], f'<div class="wrap article">{crumbs("../",(t["nav"][3],None))}<h1>{t["safety_t"]}</h1><img class="art-img" src="{{ROOT}}img/safety.jpg" alt="{t["safety_t"]}" loading="lazy">' + "".join(f"<h2>{a}</h2><p>{b}</p>" for a,b in t["safety_body"]) + f"{btn()}</div>")
    page("faq/", t["faq_t"], t["faq_d"], f'<div class="wrap article">{crumbs("../",(t["faq_short"],None))}<h1>{t["faq_t"]}</h1>{faq}<div class="cta-row">{btn()}</div></div>')
    page("careers/", t["careers_t"], t["careers_p"], f'<div class="wrap article">{crumbs("../",(t["careers_h"],None))}<h1>{t["careers_h"]}</h1><p>{t["careers_p"]}</p>{btn(t["apply"], t["apply_msg"])}</div>')

    # GUIDES
    page("guides/", t["guides_t"], t["guides_p"], f'<div class="wrap">{crumbs("../",(t["guides_f"],None))}<section><div class="sec-head"><h1>{t["guides_hh"]}</h1></div>{hub_cards("../")}</section></div>')
    for hb in HUBS:
        hs = hub_slug(hb)
        items = "".join((f'<li><a href="{a["slug"]}/index.html">{a["h1"] if lang=="en" else RU_ARTICLE["h1"]}</a></li>' if a["id"]==LIVE_ARTICLE else
                         (f'<li>{a["h1"]} <span class="soon">· {t["soon"]}</span></li>' if lang=="en" else "")) for a in A if a["hub"]==hb)
        if lang=="ru":
            n = sum(1 for a in A if a["hub"]==hb and a["id"]!=LIVE_ARTICLE)
            items += f'<li class="soon">{n} {t["n_guides"]} — {t["soon"]}</li>'
        page(f"guides/{hs}/", t["hubs"][hb], t["guides_p"], f'<div class="wrap">{crumbs("../../",(t["guides_f"],"guides/"),(t["hubs"][hb],None))}<section><div class="sec-head"><h1>{t["hubs"][hb]}</h1></div><ul class="list">{items}</ul></section></div>')

    a = next(x for x in A if x["id"]==LIVE_ARTICLE)
    art = EN_ARTICLE if lang=="en" else RU_ARTICLE
    toc = "".join(f'<li><a href="#s{i}">{h}</a></li>' for i,(h,_) in enumerate(art["secs"],1))
    body = "".join(f'<h2 id="s{i}">{h}</h2><p>{p}</p>' + (f'<div class="inline-cta"><div><b>{art["mid_h"]}</b><br><span class="note">{art["mid_p"]}</span></div>{btn(t["book"])}</div>' if i==3 else "") for i,(h,p) in enumerate(art["secs"],1))
    hm = "../../../"
    page(f"guides/{hub_slug(a['hub'])}/{a['slug']}/", art["title"], art["desc"], f"""<div class="wrap article">{crumbs(hm,(t["guides_f"],"guides/"),(t["hubs"][a["hub"]],f"guides/{hub_slug(a['hub'])}/"))}
<h1>{art["h1"]}</h1><p class="note">{art["byline"]}</p><p class="lead">{art["lead"]}</p><img class="art-img" src="{{ROOT}}img/article.jpg" alt="{art['h1']}" width="960" height="1440"><div class="toc"><b>{art["toc"]}</b><ol>{toc}</ol></div>{body}
<div class="inline-cta"><div><b>{t["final_h"]}</b></div>{btn()}</div></div>""",
     f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":"{art["h1"]}","inLanguage":"{lang}","dateModified":"2026-09-25"}}</script>')

EN_ARTICLE = dict(title="Things to Do in Sanur with Kids (2026 Family Guide)", h1="Things to Do in Sanur with Kids: The Complete Family Guide",
 desc="Beaches, playgrounds, water activities and a 3-day plan for families in Sanur, Bali — from a local nanny agency.",
 byline="By [Author], reviewed by [Nanny coordinator] · Updated September 2026", toc="In this guide",
 lead="Sanur is the calmest, most walkable corner of Bali for families: reef-protected water, a flat beachfront path and short distances. Here's how to spend your days there with kids of any age.",
 mid_h="Want an evening to yourselves?", mid_p="A nanny can come to your hotel or villa tonight.",
 secs=[("Beaches","Sanur's reef keeps the water calm, which makes it one of the easiest places in Bali for small children to swim. Sindhu, Semawang and Mertasari beaches are the family favourites. Swim around high tide; at low tide the water drops far out over the reef."),
 ("Parks and playgrounds","Several beachfront cafes along the Sanur path have playgrounds, and there are indoor soft-play options for the hottest hours of the day."),
 ("Water activities","Stand-up paddleboarding, snorkelling trips and swimming lessons all work well in Sanur's calm water. Kitesurfing and windsurfing lessons suit older kids in the windy season."),
 ("Rainy-day ideas","Craft and cooking classes, indoor play centres and malls in nearby Denpasar keep kids busy when the rain comes."),
 ("Evening activities","The Sindhu night market, sunset along the beach path — or a dinner for two while a nanny puts the kids to bed."),
 ("Sample 3-day plan","Day 1: beach morning, pool and nap, sunset walk. Day 2: snorkelling or SUP, then a craft class. Day 3: a day trip to Bali Zoo or a waterpark, with an evening off for parents.")])
RU_ARTICLE = dict(title="Санур с детьми: чем заняться (гайд 2026)", h1="Санур с детьми: чем заняться — полный гайд для семьи",
 desc="Пляжи, детские площадки, активности на воде и план на 3 дня для семей в Сануре, Бали — от местного агентства нянь.",
 byline="Автор: [Автор], проверено: [Координатор нянь] · Обновлено в сентябре 2026", toc="В этом гайде",
 lead="Санур — самый спокойный и удобный для прогулок район Бали: вода защищена рифом, вдоль моря идёт ровная набережная, всё рядом. Рассказываем, как провести здесь дни с детьми любого возраста.",
 mid_h="Хотите вечер вдвоём?", mid_p="Няня приедет в ваш отель или виллу уже сегодня.",
 secs=[("Пляжи","Риф гасит волны, поэтому Санур — одно из самых удобных мест на Бали для купания малышей. Любимые пляжи семей — Синдху, Семаванг и Мертасари. Купаться лучше в прилив: в отлив вода уходит далеко за риф."),
 ("Парки и детские площадки","У многих кафе на набережной есть детские площадки, а в самые жаркие часы выручают крытые игровые центры."),
 ("Активности на воде","Сапборд, снорклинг и уроки плавания отлично подходят для спокойной воды Санура. Кайт и виндсёрфинг — для детей постарше в ветреный сезон."),
 ("Если идёт дождь","Мастер-классы по рукоделию и кулинарии, игровые центры и торговые центры соседнего Денпасара."),
 ("Вечером","Ночной рынок Синдху, закат на набережной — или ужин вдвоём, пока няня укладывает детей."),
 ("План на 3 дня","День 1: утро на пляже, бассейн и дневной сон, вечерняя прогулка. День 2: снорклинг или сап, потом мастер-класс. День 3: поездка в Bali Zoo или аквапарк и свободный вечер для родителей.")])

if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
for lang in T: build(lang)
(OUT/"style.css").write_text(CSS, encoding="utf-8")
shutil.copytree(HERE/"src/img", OUT/"img")
(OUT/".nojekyll").write_text("")
(OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
urls = sorted(p.relative_to(OUT).as_posix().replace("index.html","") for p in OUT.rglob("index.html"))
(OUT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{DOMAIN}/{u}</loc></url>" for u in urls)+"</urlset>", encoding="utf-8")
print(len(urls), "pages ->", OUT)
