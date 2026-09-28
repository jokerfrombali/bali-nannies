# -*- coding: utf-8 -*-
"""Static site generator: Sanur nanny agency, EN (root) + RU (/ru/). Guide plan comes from build_seo.py."""
import html, urllib.parse, pathlib, shutil

HERE = pathlib.Path(__file__).parent
ns = {"__file__": str(HERE/"build_seo.py")}
import sys; sys.path.insert(0, str(HERE))
from areas import AREAS
import trust_blocks as TBm
import rentals as RM
import prices as PR
import json as _json
AREA_CREDITS = _json.loads((HERE/"src/img/areas/credits.json").read_text(encoding="utf-8"))
exec((HERE/"build_seo.py").read_text(encoding="utf-8").split("# ---------------------------------------------------------------- СЕМАНТИКА")[0], ns)
A, HUBS = ns["A"], ns["HUBS"]
for i, a in enumerate(A, 1): a["id"] = f"A{i:03d}"

# ---- настройки бизнеса (заполнить)
BRAND = "Bali Nannies"
WA = "6287763685959"           # номер WhatsApp: 62…, без +
WA_SHOW = "+62 877-6368-5959"
INDEXING = False   # False = сайт закрыт от поисковиков (meta noindex + robots.txt Disallow). True — при запуске на домене.
EMAIL = "hello@example.com"   # заглушка: пока содержит example.com — на сайте не показывается
EMAIL_OK = "example.com" not in EMAIL
DOMAIN = "https://[domain]"     # после покупки домена
OUT = HERE/"site"
CSS = (HERE/"src/style.css").read_text(encoding="utf-8") + TBm.CSS + RM.CSS + PR.CSS
import hashlib
CSS_V = hashlib.md5(CSS.encode()).hexdigest()[:8]
WA_SVG = (HERE/"src/wa.svg").read_text(encoding="utf-8")

SERVICES = ["hourly-babysitter","day-nanny","night-nanny","newborn-nanny","travel-nanny","hotel-villa-babysitting","event-babysitting","long-term-nanny"]
ICONS = ["🕒","☀️","🌙","👶","🚤","🏝️","🎉","🏡"]
LIVE_ARTICLE = "A026"   # статья-образец

T = {
"en": dict(
  prefix="", html_lang="en", other="ru", other_label="RU", locale="en",
  wa_default="Hi! I'd like to book a nanny in Bali.",
  wa_service="Hi! I'm interested in: {s}. Dates: ",
  nav=["Services","Rentals","Areas","Prices","Safety","Guides"], safety_nav="Safety", home="Home",
  svc=[("Hourly babysitter","Dinner out, spa, a surf lesson — from 6 hours."),("Full-day nanny","Beach, pool, naps and meals while you get a real holiday."),("Night nanny","Settling, feeds and night wakings so you can sleep."),("Newborn & baby care","Nannies experienced with babies under 12 months."),("Travel nanny","Joins your family on day trips and island hops."),("Hotel & villa babysitting","We come to your hotel or villa across Bali."),("Weddings & events","Kids' corner and sitters for celebrations."),("Long-term nanny","For expat families living in Bali.")],
  wa_btn="Chat on WhatsApp", wa_short="WhatsApp", book="Book on WhatsApp", see_prices="See prices", prices="Prices",
  title_home="Nanny & Babysitter in Bali — Sanur, Canggu, Ubud & more", desc_home="English-speaking, first-aid trained nannies and babysitters across Bali: Sanur, Canggu, Seminyak, Ubud, Uluwatu, Nusa Dua. Hotel & villa visits, night nannies, day trips. Book in minutes on WhatsApp.",
  eyebrow="Bali · Indonesia", h1="Trusted nannies for your family holiday in Bali",
  lead="English-speaking, first-aid trained babysitters who come to your hotel or villa — so you can enjoy dinner, the spa or a quiet sunrise.",
  trust=["Background-checked","First aid & CPR","Reply within 15 min"], chip="🟢 Nanny available tonight", photo="Nanny playing with a child in a swimming pool",
  svc_h="Care that fits your trip", svc_p="From a single evening to a full season in Bali.",
  steps_h="Booked in three messages", steps=[("Message us on WhatsApp","Tell us dates, hours, kids' ages and where you're staying."),("Meet your nanny","We send a profile and a short intro. Want a video call first? Just ask."),("Enjoy your time","She arrives at your hotel or villa. Photo updates on WhatsApp, pay after the session.")],
  safe_h="Safety isn't a feature. It's the job.", safe_p="Every nanny is interviewed in person, reference-checked and trained before her first family.", safe_btn="Our safety standards",
  safe_list=["ID and reference checks","Paediatric first aid & CPR","Pool and beach supervision rules","Trial meeting before the first booking"],
  faq_h="Questions parents ask", faq=[("How quickly can I book?","Often the same day. For evenings and peak season (July–August, Christmas) message us 2–3 days ahead."),("Do your nannies speak English?","Yes — every nanny communicates comfortably in English. We tell you each nanny's level honestly."),("Are nannies first-aid trained?","Every nanny holds a current paediatric first aid & CPR certificate. We can show it before your booking."),("Where do you work?","Across South Bali and Ubud — Sanur, Canggu, Seminyak, Kuta, Jimbaran, Uluwatu, Nusa Dua, Denpasar and Ubud. Hotels, villas and homes."),("How do I pay?","Cash (IDR) or bank transfer after the session. No deposit for single bookings."),("Can a nanny look after my newborn?","Yes. We match babies with nannies who have specific newborn experience.")],
  guides_h="Sanur with kids", guides_p="Local guides from people who spend every day on these beaches.", n_guides="guides",
  final_h="Need a nanny in Bali?", final_p="Tell us your dates — we'll reply with an available nanny.", final_btn="Message us on WhatsApp",
  services_t="Nanny Services in Bali", services_h="Our services", services_d="Hourly babysitters, full-day and night nannies, newborn care and travel nannies across Bali.",
  svc_title="{s} in Bali", svc_h1="{s} in Bali", check="Check availability", how="How it works", faq_short="FAQ",
  prices_t="Nanny & Babysitter Prices in Bali", prices_h="Simple, transparent prices", prices_p="No deposit for single bookings. Pay after the session.", th=["Service","Rate","Minimum"], price_note="Transport within the nanny's area included; longer trips by agreement.", quote="Get a quote",
  hiw_t="How Booking Works", hiw_d="Book a nanny in Bali in three WhatsApp messages.",
  safety_t="Our Safety Standards", safety_d="How we select, check and train every nanny in Bali.",
  safety_body=[("Selection","In-person interview, ID check, at least two references from previous families."),("Training","Current paediatric first aid & CPR certificate. Pool and beach supervision rules."),("On every booking","Handover checklist, emergency contacts, WhatsApp updates.")],
  faq_t="Frequently asked questions", faq_d="Answers about booking a nanny in Bali.",
  careers_nav="Become a nanny", careers_t="Nanny Jobs in Bali", careers_h="Become a nanny", careers_p="We work with experienced, English-speaking nannies across Bali. First aid training provided.", apply="Apply on WhatsApp", apply_msg="Hi! I would like to apply as a nanny.",
  guides_t="Sanur Family Guides", guides_hh="Sanur family guides", soon="coming soon",
  company="Company", services_f="Services", guides_f="Guides", foot_p="Trusted English-speaking nannies and babysitters for families across Bali.",
  hubs={h:v[0] for h,v in HUBS.items()},
),
"ru": dict(
  prefix="ru/", html_lang="ru", other="en", other_label="EN", locale="ru",
  wa_default="Здравствуйте! Хочу забронировать няню на Бали.",
  wa_service="Здравствуйте! Интересует: {s}. Даты: ",
  nav=["Услуги","Прокат","Районы","Цены","Безопасность","Гайды"], safety_nav="Безопасность", home="Главная",
  svc=[("Няня на час","Ужин, спа, урок сёрфинга — от 6 часов."),("Няня на весь день","Пляж, бассейн, сон и еда, пока у вас настоящий отпуск."),("Ночная няня","Укладывание, кормления и ночные пробуждения — а вы высыпаетесь."),("Няня для малыша","Няни с опытом ухода за детьми до года."),("Няня в поездки","Едет с семьёй на экскурсии и острова."),("Няня в отель или виллу","Приедем в ваш отель или виллу по всему Бали."),("Свадьбы и мероприятия","Детская зона и няни на праздники."),("Няня на длительный срок","Для семей, которые живут на Бали.")],
  wa_btn="Написать в WhatsApp", wa_short="WhatsApp", book="Забронировать в WhatsApp", see_prices="Цены", prices="Цены",
  title_home="Няня на Бали — Санур, Чангу, Убуд и другие районы", desc_home="Проверенные няни с сертификатом первой помощи по всему Бали: Санур, Чангу, Семиньяк, Убуд, Улувату, Нуса Дуа. Приезд в отель и виллу, ночные няни, поездки. Бронь за пару минут в WhatsApp.",
  eyebrow="Бали · Индонезия", h1="Надёжные няни для семейного отдыха на Бали",
  lead="Опытные няни с сертификатом первой помощи приедут в ваш отель или виллу — а вы спокойно поужинаете, сходите в спа или встретите рассвет вдвоём.",
  trust=["Проверенные няни","Первая помощь и СЛР","Ответ за 15 минут"], chip="🟢 Няня свободна сегодня вечером", photo="Няня играет с ребёнком в бассейне",
  svc_h="Помощь под ваш формат отдыха", svc_p="От одного вечера до целого сезона на Бали.",
  steps_h="Бронь в три сообщения", steps=[("Напишите в WhatsApp","Даты, часы, возраст детей и где вы живёте."),("Познакомьтесь с няней","Пришлём профиль и короткое знакомство. Нужен видеозвонок — устроим."),("Отдыхайте","Няня приезжает в отель или виллу. Фото в WhatsApp, оплата после смены.")],
  safe_h="Безопасность — это не опция. Это наша работа.", safe_p="Каждую няню мы лично собеседуем, проверяем рекомендации и обучаем до первой семьи.", safe_btn="Наши стандарты безопасности",
  safe_list=["Проверка документов и рекомендаций","Детская первая помощь и СЛР","Правила присмотра у бассейна и на пляже","Знакомство до первой брони"],
  faq_h="Частые вопросы родителей", faq=[("Как быстро можно забронировать?","Часто — в тот же день. На вечер и в высокий сезон (июль–август, Новый год) лучше написать за 2–3 дня."),("Няни говорят по-русски?","Все няни свободно общаются на английском. Русскоязычных нянь подбираем по запросу — честно скажем, есть ли свободная."),("У нянь есть навыки первой помощи?","У каждой няни действующий сертификат детской первой помощи и СЛР. Покажем до брони."),("Где вы работаете?","Юг Бали и Убуд — Санур, Чангу, Семиньяк, Кута, Джимбаран, Улувату, Нуса Дуа, Денпасар и Убуд. Отели, виллы и дома."),("Как оплатить?","Наличными (рупии) или переводом после смены. Без предоплаты для разовых броней."),("Няня посидит с новорождённым?","Да. Для малышей подбираем нянь с опытом ухода за новорождёнными.")],
  guides_h="Санур с детьми", guides_p="Гайды от людей, которые каждый день на этих пляжах.", n_guides="статей",
  final_h="Нужна няня на Бали?", final_p="Напишите даты — ответим, кто из нянь свободен.", final_btn="Написать в WhatsApp",
  services_t="Услуги нянь на Бали", services_h="Наши услуги", services_d="Няня на час, на день, ночная няня, уход за малышами и няня в поездки по всему Бали.",
  svc_title="{s} на Бали", svc_h1="{s} на Бали", check="Узнать, кто свободен", how="Как это работает", faq_short="Вопросы",
  prices_t="Цены на няню на Бали", prices_h="Простые и понятные цены", prices_p="Без предоплаты за разовые брони. Оплата после смены.", th=["Услуга","Цена","Минимум"], price_note="Дорога в пределах района няни включена, дальние выезды — по договорённости.", quote="Узнать цену",
  hiw_t="Как забронировать няню", hiw_d="Бронь няни на Бали — три сообщения в WhatsApp.",
  safety_t="Стандарты безопасности", safety_d="Как мы отбираем, проверяем и обучаем нянь на Бали.",
  safety_body=[("Отбор","Личное собеседование, проверка документов, минимум две рекомендации от семей."),("Обучение","Действующий сертификат детской первой помощи и СЛР. Правила присмотра у воды."),("На каждой смене","Чек-лист передачи ребёнка, экстренные контакты, отчёты в WhatsApp.")],
  faq_t="Частые вопросы", faq_d="Ответы о бронировании няни на Бали.",
  careers_nav="Работа няней", careers_t="Работа няней на Бали", careers_h="Работа няней", careers_p="Ищем опытных нянь со знанием английского или русского. Обучение первой помощи — за наш счёт.", apply="Откликнуться в WhatsApp", apply_msg="Здравствуйте! Хочу работать няней.",
  guides_t="Гайды для семей в Сануре", guides_hh="Гайды для семей в Сануре", soon="скоро",
  company="Компания", services_f="Услуги", guides_f="Гайды", foot_p="Надёжные няни и бебиситтеры для семей по всему Бали.",
  hubs={"H01":"Няня в Сануре","H02":"Санур с детьми: чем заняться","H03":"Где жить с детьми","H04":"Здоровье и безопасность","H05":"Еда для семьи","H06":"Перелёт и логистика","H07":"Поездки из Санура","H08":"Жизнь в Сануре с детьми"},
)}

FLOWER = ('<svg class="flower" viewBox="0 0 40 40" aria-hidden="true"><g fill="currentColor">'
  + "".join(f'<path transform="rotate({k*72} 20 20)" d="M20 20C13.5 16 12.5 5 19 2.2c5.2-1.6 8.3 4.4 5.6 10.6C23.6 15.3 22 18 20 20z"/>' for k in range(5))
  + '</g><circle cx="20" cy="20" r="3.6" fill="#F6C453"/></svg>')
LANG_HINT = {"en":"View in English","ru":"Открыть на русском","zh":"切换到中文","hi":"हिन्दी में देखें","ko":"한국어로 보기","ja":"日本語で見る","fr":"Voir en français","de":"Auf Deutsch ansehen","es":"Ver en español","it":"Vedi in italiano","nl":"Bekijk in het Nederlands","id":"Lihat dalam Bahasa Indonesia"}
import json as _jh
HINT_JS = ("(()=>{const K='bn_lang_hint';const mark=()=>{try{localStorage.setItem(K,'1')}catch(e){}};"
  "document.querySelectorAll('.lang-pop a[lang]').forEach(a=>a.addEventListener('click',mark));"
  "try{if(localStorage.getItem(K))return}catch(e){}"
  "const cur=document.documentElement.lang.slice(0,2).toLowerCase(),links={};"
  "document.querySelectorAll('.lang-pop a[lang]').forEach(a=>links[a.getAttribute('lang')]=a.href);"
  "const pref=(navigator.languages&&navigator.languages.length?navigator.languages:[navigator.language||'']).map(l=>l.toLowerCase().replace(/^in\b/,'id').slice(0,2)).find(l=>links[l]);"
  "if(!pref||pref===cur)return;const T=" + _jh.dumps(LANG_HINT, ensure_ascii=False) + ";"
  "const d=document.createElement('div');d.className='lang-hint';d.setAttribute('lang',pref);"
  "d.innerHTML='<svg viewBox=\"0 0 24 24\" aria-hidden=\"true\"><circle cx=\"12\" cy=\"12\" r=\"9\"/><path d=\"M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9M12 3c-2.5 2.6-3.8 5.6-3.8 9s1.3 6.4 3.8 9\"/></svg>';"
  "const a=document.createElement('a');a.href=links[pref];a.textContent=T[pref];a.addEventListener('click',mark);"
  "const x=document.createElement('button');x.type='button';x.setAttribute('aria-label','Close');x.textContent='✕';"
  "x.addEventListener('click',()=>{mark();d.classList.remove('show');setTimeout(()=>d.remove(),300)});"
  "d.append(a,x);document.body.appendChild(d);setTimeout(()=>d.classList.add('show'),900)})();")
HDR_JS = ("(()=>{const bg=document.querySelector('.burger'),nv=document.getElementById('mainnav'),gl=document.querySelector('.globe'),lm=document.querySelector('.lang-menu');"
  "bg.addEventListener('click',e=>{e.stopPropagation();const o=nv.classList.toggle('open');bg.setAttribute('aria-expanded',o);document.body.classList.toggle('nav-open',o);lm.classList.remove('open')});"
  "gl.addEventListener('click',e=>{e.stopPropagation();const o=lm.classList.toggle('open');gl.setAttribute('aria-expanded',o);nv.classList.remove('open');document.body.classList.remove('nav-open')});"
  "document.addEventListener('click',e=>{if(!lm.contains(e.target))lm.classList.remove('open')});"
  "addEventListener('keydown',e=>{if(e.key==='Escape'){lm.classList.remove('open');nv.classList.remove('open');document.body.classList.remove('nav-open')}})})();"
  "(()=>{const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});"
  "const els=[...document.querySelectorAll('main section, .reveal')];els.forEach(el=>{if(el.getBoundingClientRect().top>innerHeight){el.classList.add('pre');io.observe(el)}});"
  "const chk=()=>els.forEach(el=>{if(el.classList.contains('pre')&&el.getBoundingClientRect().top<innerHeight*.95)el.classList.add('in')});addEventListener('scroll',chk,{passive:true})})();"
  "(()=>{const b=document.querySelector('.hdr-wa'),t=document.querySelector('main .cta-row')||document.querySelector('main h1');"
  "if(!b||!t)return;new IntersectionObserver(([e])=>b.classList.toggle('show',!e.isIntersecting&&e.boundingClientRect.top<0)).observe(t)})()")
AREA_LD = ",".join(f'{{"@type":"Place","name":"{a["en"]}, Bali"}}' for a in AREAS)

def wa(text): return f"https://wa.me/{WA}?text={urllib.parse.quote(text)}"
def hub_slug(h): return HUBS[h][1].split("/")[2]

SM = {"en": dict(title="Site map", desc="Every page of Bali Nannies in one place."),
      "ru": dict(title="Карта сайта", desc="Все страницы Bali Nannies в одном месте.")}
VID = {"en": dict(alt="Our nanny with a smiling baby at a Bali villa", play="Play video", label="Watch 30 sec"),
       "ru": dict(alt="Наша няня с улыбающимся малышом на вилле на Бали", play="Смотреть видео", label="Смотреть 30 сек")}
CT = {
 "en":dict(title="Contact",h1="Contact us",p="The fastest way to reach us is WhatsApp — we usually reply within 15 minutes.",wa="WhatsApp",email="Email",area="Area",area_v="Bali, Indonesia — Sanur, Canggu, Seminyak, Kuta, Ubud, Uluwatu, Jimbaran, Nusa Dua, Denpasar"),
 "ru":dict(title="Контакты",h1="Контакты",p="Быстрее всего — в WhatsApp, обычно отвечаем в течение 15 минут.",wa="WhatsApp",email="Email",area="Где работаем",area_v="Бали, Индонезия — Санур, Чангу, Семиньяк, Кута, Убуд, Улувату, Джимбаран, Нуса Дуа, Денпасар"),
 "zh":dict(title="联系我们",h1="联系我们",p="最快的方式是 WhatsApp，我们通常在 15 分钟内回复。",wa="WhatsApp",email="邮箱",area="服务区域",area_v="印度尼西亚巴厘岛 — 萨努尔、仓古、水明漾、库塔、乌布、乌鲁瓦图、金巴兰、努沙杜瓦、登巴萨"),
 "hi":dict(title="संपर्क",h1="हमसे संपर्क करें",p="सबसे तेज़ तरीका WhatsApp है — हम आमतौर पर 15 मिनट में जवाब देते हैं।",wa="WhatsApp",email="ईमेल",area="क्षेत्र",area_v="बाली, इंडोनेशिया — Sanur, Canggu, Seminyak, Kuta, Ubud, Uluwatu, Jimbaran, Nusa Dua, Denpasar"),
 "ko":dict(title="문의",h1="문의하기",p="가장 빠른 방법은 WhatsApp이에요. 보통 15분 안에 답장드려요.",wa="WhatsApp",email="이메일",area="서비스 지역",area_v="인도네시아 발리 — 사누르, 짱구, 스미냑, 꾸따, 우붓, 울루와뚜, 짐바란, 누사두아, 덴파사르"),
 "ja":dict(title="お問い合わせ",h1="お問い合わせ",p="いちばん早いのは WhatsApp です。通常15分以内にお返事します。",wa="WhatsApp",email="メール",area="対応エリア",area_v="インドネシア・バリ島 — サヌール、チャングー、スミニャック、クタ、ウブド、ウルワツ、ジンバラン、ヌサドゥア、デンパサール"),
 "fr":dict(title="Contact",h1="Nous contacter",p="Le plus rapide : WhatsApp. Nous répondons en général en 15 minutes.",wa="WhatsApp",email="E-mail",area="Zone",area_v="Bali, Indonésie — Sanur, Canggu, Seminyak, Kuta, Ubud, Uluwatu, Jimbaran, Nusa Dua, Denpasar"),
 "de":dict(title="Kontakt",h1="Kontakt",p="Am schnellsten per WhatsApp – wir antworten meist innerhalb von 15 Minuten.",wa="WhatsApp",email="E-Mail",area="Gebiet",area_v="Bali, Indonesien — Sanur, Canggu, Seminyak, Kuta, Ubud, Uluwatu, Jimbaran, Nusa Dua, Denpasar"),
 "es":dict(title="Contacto",h1="Contacto",p="Lo más rápido es WhatsApp: solemos responder en 15 minutos.",wa="WhatsApp",email="Email",area="Zona",area_v="Bali, Indonesia — Sanur, Canggu, Seminyak, Kuta, Ubud, Uluwatu, Jimbaran, Nusa Dua, Denpasar"),
 "it":dict(title="Contatti",h1="Contattaci",p="Il modo più rapido è WhatsApp: di solito rispondiamo entro 15 minuti.",wa="WhatsApp",email="Email",area="Zona",area_v="Bali, Indonesia — Sanur, Canggu, Seminyak, Kuta, Ubud, Uluwatu, Jimbaran, Nusa Dua, Denpasar"),
 "nl":dict(title="Contact",h1="Contact",p="Het snelst via WhatsApp — meestal reageren we binnen 15 minuten.",wa="WhatsApp",email="E-mail",area="Gebied",area_v="Bali, Indonesië — Sanur, Canggu, Seminyak, Kuta, Ubud, Uluwatu, Jimbaran, Nusa Dua, Denpasar"),
 "id":dict(title="Kontak",h1="Hubungi kami",p="Cara tercepat lewat WhatsApp — biasanya kami membalas dalam 15 menit.",wa="WhatsApp",email="Email",area="Area",area_v="Bali, Indonesia — Sanur, Canggu, Seminyak, Kuta, Ubud, Uluwatu, Jimbaran, Nusa Dua, Denpasar"),
}
AT = {
 "en": dict(nav="Areas", h="Where we work in Bali", p="Our nannies come to hotels, villas and homes across South Bali and Ubud.",
            title="Nanny Service Areas in Bali", title_one="Nanny & Babysitter in {loc}, Bali", h1="Nanny & babysitter in {loc}",
            msg="Hi! I need a nanny in {loc}. Dates: ", other="Other areas"),
 "ru": dict(nav="Районы", h="Где мы работаем на Бали", p="Наши няни приезжают в отели, виллы и дома по всему югу Бали и в Убуд.",
            title="Районы работы нянь на Бали", title_one="Няня {loc}, Бали", h1="Няня {loc}",
            msg="Здравствуйте! Нужна няня, район: {loc}. Даты: ", other="Другие районы"),
}

def build(lang):
    t = T[lang]
    b = TBm.TB[lang]
    r = RM.RT[lang]
    def btn(text=None, msg=None, cls=""):
        return f'<a class="btn btn-wa {cls}" href="{wa(msg or t["wa_default"])}" target="_blank" rel="noopener">{WA_SVG}{text or t["wa_btn"]}</a>'

    def page(path, title, desc, body, schema="", other_exists=True):
        full = t["prefix"] + path
        depth = full.count("/")
        root = "../" * depth           # корень сайта
        home = root + t["prefix"]      # главная текущего языка
        other_path = T[t["other"]]["prefix"] + path
        alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{DOMAIN}/{T[l]["prefix"]}{path}">' for l in T) + f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{path}">' if other_exists else ""
        here = f'{root}{t["prefix"]}{path}index.html'
        there = f'{root}{other_path}index.html' if other_exists else f'{root}{T[t["other"]]["prefix"]}index.html'
        langs = {l: (LANG_NAMES[l], f'{root}{T[l]["prefix"]}{path}index.html') for l in T}
        globe = ('<div class="lang-menu"><button class="icon-btn globe" type="button" aria-label="Language" aria-haspopup="true" aria-expanded="false">'
                 '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9M12 3c-2.5 2.6-3.8 5.6-3.8 9s1.3 6.4 3.8 9"/></svg>'
                 f'<b>{lang.upper()}</b></button><div class="lang-pop" role="menu">'
                 + "".join('<a role="menuitem" href="'+u+'" lang="'+l+'"'+(' aria-current="true"' if l==lang else '')+'>'+n+'</a>' for l,(n,u) in langs.items()) + '</div></div>')
        switch = f'<a class="lang" href="{root}{other_path}index.html">{t["other_label"]}</a>' if other_exists else f'<a class="lang" href="{root}{T[t["other"]]["prefix"]}index.html">{t["other_label"]}</a>'
        links = ["services","rentals","areas","prices","safety","guides"]
        nav = f"""<header><div class="wrap nav"><a class="logo" href="{home}index.html" aria-label="{BRAND}">Bali{FLOWER}Nannies</a>
<nav class="links" id="mainnav">{''.join(f'<a href="{home}{l}/index.html">{n}</a>' for l,n in zip(links,t["nav"]))}</nav>
<div class="right">{btn(t["wa_short"], cls="btn-sm hdr-wa")}{globe}<button class="icon-btn burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="mainnav"><span></span><span></span><span></span></button></div></div></header>"""
        foot = f"""<footer class="site-foot"><div class="wrap">
<div class="foot-top"><div class="foot-brand"><a class="logo logo-light" href="{home}index.html">Bali{FLOWER}Nannies</a><p>{t["foot_p"]}</p>
<a class="foot-wa" href="{wa(t['wa_default'])}" target="_blank" rel="noopener">{WA_SVG}<span>WhatsApp · {WA_SHOW}</span></a></div>
<nav class="foot-cols">
<div><b>{t["services_f"]}</b>{''.join(f'<a href="{home}services/{s}/index.html">{n}</a>' for s,(n,_) in zip(SERVICES,t["svc"]))}</div>
<div><b>{r["nav"]}</b>{''.join(f'<a href="{home}rentals/{c["slug"]}/index.html">{c[lang][0]}</a>' for c in RM.CATS)}</div>
<div><b>{AT[lang]["nav"]}</b>{''.join(f'<a href="{home}areas/{a["slug"]}/index.html">{a[lang]}</a>' for a in AREAS)}</div>
<div><b>{t["company"]}</b>{''.join(f'<a href="{home}{l}/index.html">{n}</a>' for l,n in zip(["contact","how-it-works","safety","prices","faq","careers","guides"],[CT[lang]["title"],t["how"],t["safety_nav"],t["prices"],t["faq_short"],t["careers_nav"],t["guides_f"]]))}</div>
</nav></div>
<div class="foot-bottom"><span>© 2026 {BRAND} · Bali, Indonesia</span><span><a href="{home}sitemap/index.html">{SM[lang]["title"]}</a>{f' · <a href="mailto:{EMAIL}">{EMAIL}</a>' if EMAIL_OK else ""} · {switch}</span></div>
</div></footer>
<script>{HDR_JS}{HINT_JS}</script>"""
        doc = f"""<!doctype html><html lang="{t['html_lang']}" translate="no"><head><meta charset="utf-8"><meta name="google" content="notranslate">{'' if INDEXING else '<meta name="robots" content="noindex,nofollow,noarchive">'}<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} | {BRAND}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{DOMAIN}/{full}">{alt}
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{root}style.css?v={CSS_V}">{schema}</head><body>{nav}<main>{body.replace("{ROOT}", root)}</main>{foot}</body></html>"""
        f = OUT/full/"index.html"
        f.parent.mkdir(parents=True, exist_ok=True); f.write_text(doc, encoding="utf-8")
        return root, home

    def crumbs(home, *items):
        parts = [f'<a href="{home}index.html">{t["home"]}</a>'] + [f'<a href="{home}{u}index.html">{n}</a>' if u else n for n,u in items]
        return '<div class="crumbs">' + " / ".join(parts) + "</div>"

    def home_rel(path): return "../" * path.count("/")   # от страницы до главной языка

    def services_grid(home):
        return '<div class="grid">' + "".join(f'<a class="card card-img" href="{home}services/{s}/index.html"><img class="thumb" src="{{ROOT}}img/{s}.jpg" alt="" loading="lazy" width="960" height="640"><div class="ico">{i}</div><h3>{n}</h3><p>{d}</p></a>' for s,i,(n,d) in zip(SERVICES,ICONS,t["svc"])) + "</div>"
    area_grid = lambda home: '<div class="area-grid">' + "".join(f'<a class="area-card reveal" href="{home}areas/{a["slug"]}/index.html"><img src="{{ROOT}}img/areas/{a["slug"]}.jpg" alt="{a[lang]}, Bali" loading="lazy" width="1200" height="800"><span class="area-name">{a[lang]}</span><span class="area-lead">{a[lang+"_lead"]}</span></a>' for a in AREAS) + "</div>"
    steps = '<div class="steps">' + "".join(f'<div class="step"><h3>{a}</h3><p>{b}</p></div>' for a,b in t["steps"]) + "</div>"
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in t["faq"] + b["faq_add"])
    hub_cards = lambda home: '<div class="grid">' + "".join(f'<a class="card" href="{home}guides/{hub_slug(h)}/index.html"><h3>{t["hubs"][h]}</h3><p>{sum(1 for a in A if a["hub"]==h)} {t["n_guides"]}</p></a>' for h in HUBS) + "</div>"

    # HOME
    h = ""
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ChildCare","name":"{BRAND}","areaServed":[{AREA_LD}],"telephone":"+{WA}","url":"{DOMAIN}/{t["prefix"]}"}}</script>'
    page("", t["title_home"], t["desc_home"], f"""<div class="wrap hero hero-home"><div><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p>
<div class="cta-row">{btn(t["book"])}<a class="btn btn-ghost" href="prices/index.html">{t["see_prices"]}</a></div>
<ul class="trust trust-ico">{''.join(f'<li><span class="ti" aria-hidden="true">{i}</span>{x}</li>' for i,x in zip(["🛡️","👋","🔄","💳"], b["hero_trust"]))}</ul></div>
<div class="photo hero-video" id="heroVideo"><img class="hv-poster" src="{{ROOT}}img/hero-video-poster.jpg" alt="{VID[lang]['alt']}" width="480" height="848" fetchpriority="high">
<video class="hv-video" muted loop playsinline webkit-playsinline preload="metadata" poster="{{ROOT}}img/hero-video-poster.jpg"><source src="{{ROOT}}video/hero.mp4" type="video/mp4"></video>
<button class="hv-play" type="button" aria-label="{VID[lang]['play']}"><svg class="heart" viewBox="0 0 24 24" aria-hidden="true"><path class="h" d="M12 21.2s-7.6-4.7-9.7-9.5C.8 8.1 3 4.3 6.7 4.3c2.1 0 3.6 1.1 5.3 3 1.7-1.9 3.2-3 5.3-3 3.7 0 5.9 3.8 4.4 7.4-2.1 4.8-9.7 9.5-9.7 9.5z"/><path class="t" d="M10.2 9.4v5.2l4.3-2.6z"/></svg><span>{VID[lang]['label']}</span></button><button class="hv-close" type="button" aria-label="Close">✕</button>
</div></div>
<script>(()=>{{const w=document.getElementById('heroVideo'),v=w.querySelector('video'),b=w.querySelector('.hv-play');
const bd=document.createElement('div');bd.className='vid-backdrop';document.body.appendChild(bd);const stop=()=>{{v.pause();v.controls=false;w.classList.remove('playing');document.body.classList.remove('vid-open')}};const play=()=>{{w.classList.add('playing');const m=matchMedia('(max-width:860px)').matches;if(m){{document.body.classList.add('vid-open');v.controls=true}}v.muted=true;const pr=v.play();if(pr&&pr.catch)pr.catch(()=>{{v.controls=true;if(!m)stop()}})}};bd.addEventListener('click',stop);w.querySelector('.hv-close').addEventListener('click',e=>{{e.stopPropagation();stop()}});
b.addEventListener('click',play);v.addEventListener('click',()=>{{if(!document.body.classList.contains('vid-open'))stop()}});}})()</script>
<section><div class="wrap"><div class="sec-head"><h2>{t["svc_h"]}</h2><p>{t["svc_p"]}</p></div>{services_grid("")}</div></section>
<section><div class="wrap"><div class="sec-head"><h2>{r["home_h"]}</h2><p>{r["home_p"]}</p></div>{RM.fence_banner(lang, "", btn)}
<div style="margin-top:18px">{RM.rent_grid(lang, "", RM.CATS[1:4])}</div><div class="cta-row"><a class="btn btn-ghost" href="rentals/index.html">{r["all"]} →</a></div></div></section>
<section><div class="wrap"><div class="sec-head"><h2>{t["steps_h"]}</h2></div>{steps}</div></section>
<section><div class="wrap"><div class="sec-head"><h2>{AT[lang]["h"]}</h2><p>{AT[lang]["p"]}</p></div>{area_grid("")}</div></section>
<section><div class="wrap">{TBm.meet_html(b, "{ROOT}")}</div></section>
<section><div class="wrap vet-band"><div class="sec-head"><h2>{b["vet_h"]}</h2><p>{b["vet_p"]}</p></div>{TBm.vet_html(b)}
<div class="cta-row" style="margin-bottom:0"><a class="btn btn-ghost" style="color:#fff;border-color:rgba(255,255,255,.35)" href="safety/index.html">{t["safe_btn"]}</a></div></div></section>
<section><div class="wrap">{TBm.guar_html(b)}</div></section>
<section><div class="wrap">{TBm.bring_html(b)}</div></section>
<section><div class="wrap"><div class="sec-head"><h2>{t["faq_h"]}</h2></div>{faq}</div></section>
<section><div class="wrap"><div class="sec-head"><h2>{t["guides_h"]}</h2><p>{t["guides_p"]}</p></div>{hub_cards("")}</div></section>
<div class="final"><h2>{t["final_h"]}</h2><p class="lead" style="margin:0 auto 24px">{t["final_p"]}</p>{btn(t["final_btn"])}</div>""", schema)

    # AREAS
    page("areas/", AT[lang]["title"], AT[lang]["p"], f'<div class="wrap">{crumbs("../",(AT[lang]["nav"],None))}<section><div class="sec-head"><h1>{AT[lang]["h"]}</h1><p>{AT[lang]["p"]}</p></div>{area_grid("../")}</section></div>')
    for k,ar in enumerate(AREAS):
        nm = ar[lang]; loc = ar["ru_in"] if lang=="ru" else ar[lang]
        h1 = AT[lang]["h1"].format(loc=loc); cr = AREA_CREDITS[ar["slug"]]
        credit = f'<p class="credit">Photo: <a href="{cr["page"]}" rel="nofollow noopener" target="_blank">{html.escape(cr["author"][:60])}</a>, {cr["license"]}</p>' if cr["license"]!="CC0" else ""
        others = "".join(f'<a class="pill" href="../{o["slug"]}/index.html">{o[lang]}</a>' for o in AREAS if o is not ar)
        body_txt = "".join(f"<h2>{a}</h2><p>{b}</p>" for a,b in ar[lang+"_txt"])
        page(f"areas/{ar['slug']}/", AT[lang]["title_one"].format(loc=loc), ar[lang+"_lead"], f"""<div class="wrap">{crumbs("../../",(AT[lang]["nav"],"areas/"),(nm,None))}
<div class="hero" style="padding-top:32px"><div><span class="eyebrow">📍 {nm}</span><h1>{h1}</h1><p class="lead">{ar[lang+"_lead"]}</p>
<div class="cta-row">{btn(t["check"], AT[lang]["msg"].format(loc=nm))}<a class="btn btn-ghost" href="../../prices/index.html">{t["prices"]}</a></div></div>
<div><div class="photo"><img src="{{ROOT}}img/areas/{ar["slug"]}.jpg" alt="{nm}, Bali" width="1200" height="800"></div>{credit}</div></div>
<div class="article" style="margin:0">{body_txt}</div>
<section><div class="sec-head"><h2>{t["svc_h"]}</h2></div>{services_grid("../../")}</section>
<section><div class="sec-head"><h2>{AT[lang]["other"]}</h2></div><div class="pills">{others}</div></section></div>""")

    # SITEMAP (HTML)
    groups = [(t["services_f"], [(f"services/{s}/", n) for s,(n,_) in zip(SERVICES,t["svc"])]),
              (r["nav"], [("rentals/", r["h1"])] + [(f"rentals/{c['slug']}/", c[lang][0]) for c in RM.CATS]),
              (AT[lang]["nav"], [(f"areas/{a['slug']}/", a[lang]) for a in AREAS]),
              (t["company"], [("contact/",CT[lang]["title"]),("how-it-works/",t["how"]),("safety/",t["safety_nav"]),("prices/",t["prices"]),("faq/",t["faq_short"]),("careers/",t["careers_nav"])]),
              (t["guides_f"], [(f"guides/{hub_slug(h)}/", t["hubs"][h]) for h in HUBS])]
    sm = "".join(f'<div class="sm-group"><h2>{g}</h2><ul>' + "".join(f'<li><a href="../{u}index.html">{n}</a></li>' for u,n in items) + "</ul></div>" for g,items in groups)
    page("sitemap/", SM[lang]["title"], SM[lang]["desc"], f'<div class="wrap">{crumbs("../",(SM[lang]["title"],None))}<section><div class="sec-head"><h1>{SM[lang]["title"]}</h1><p>{SM[lang]["desc"]}</p></div><div class="sm-grid">{sm}</div></section></div>')

    # RENTALS
    how_r = '<div class="steps">' + "".join(f'<div class="step"><h3>{a}</h3><p>{d}</p></div>' for a,d in r["how"]) + "</div>"
    hyg = '<ul class="hyg">' + "".join(f"<li>{x}</li>" for x in r["hygiene"]) + "</ul>"
    combo = f'<div class="combo"><div><h3>🧳 {r["pack_h"]}</h3><p>{r["pack_p"]}</p></div><div><h3>👩‍🍼 {r["combo_h"]}</h3><p>{r["combo_p"]}</p></div></div>'
    page("rentals/", r["title"], r["lead"], f"""<div class="wrap">{crumbs("../",(r["nav"],None))}
<section style="padding-bottom:24px"><div class="sec-head"><h1>{r["h1"]}</h1><p class="lead">{r["lead"]}</p></div><div class="cta-row">{btn(r["ask"], r["msg"])}</div>{hyg}</section>
<section style="padding-top:24px">{RM.fence_banner(lang, "../", btn)}</section>
<section><div class="sec-head"><h2>{r["sec_h"]}</h2></div>{RM.rent_grid(lang, "../", RM.CATS[1:])}</section>
<section><div class="sec-head"><h2>{r["how_h"]}</h2></div>{how_r}</section><section>{combo}</section></div>""")
    for c in RM.CATS[1:]:
        name, desc = c[lang]
        items = "".join(f"<li>{i}</li>" for i in c["items_"+lang])
        rows = "".join(f"<tr><td>{i}</td><td>[IDR —]{r['per_day']}</td></tr>" for i in c["items_"+lang])
        page(f"rentals/{c['slug']}/", f"{name} — {r['h1']}", desc, f"""<div class="wrap">{crumbs("../../",(r["nav"],"rentals/"),(name,None))}
<div class="hero" style="padding-top:32px"><div><span class="eyebrow">{c["icon"]} {r["nav"]}</span><h1>{name}</h1><p class="lead">{desc} {r["lead"]}</p>
<div class="cta-row">{btn(r["ask"], r["msg"])}</div>{hyg}</div><div class="photo"><img src="{{ROOT}}img/rent/{c["slug"]}.jpg" alt="{name}" width="1200" height="800"></div></div>
<section><table class="price-table"><tr><th>{name}</th><th>{t["th"][1]}</th></tr>{rows}</table></section>
<section><div class="sec-head"><h2>{r["how_h"]}</h2></div>{how_r}</section><section>{combo}</section>
<section><div class="sec-head"><h2>{r["sec_h"]}</h2></div>{RM.rent_grid(lang, "../../", [x for x in RM.CATS if x is not c][:3])}</section></div>""")
    pf = r["pf"]; c0 = RM.CATS[0]
    pf_steps = '<div class="steps" style="grid-template-columns:repeat(4,1fr)">' + "".join(f'<div class="step"><h3>{a}</h3><p>{d}</p></div>' for a,d in pf["steps"]) + "</div>"
    pf_faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in pf["faq"])
    page("rentals/pool-fence/", pf["title"], pf["lead"], f"""<div class="wrap">{crumbs("../../",(r["nav"],"rentals/"),(c0[lang][0],None))}
<div class="hero" style="padding-top:32px"><div><span class="eyebrow">🛡️ {c0[lang][0]}</span><h1>{pf["h1"]}</h1><p class="lead">{pf["lead"]}</p>
<div class="cta-row">{btn(pf["cta"], pf["msg"])}</div></div><div class="photo"><img src="{{ROOT}}img/rent/pool-fence.jpg" alt="{pf["h1"]}" width="1200" height="800"></div></div>
<section><div class="sec-head"><h2>{pf["why_h"]}</h2></div><div class="why-list">{"".join(f"<div>{x}</div>" for x in pf["why"])}</div><p class="safety-note">⚠️ {pf["note"]}</p></section>
<section><div class="sec-head"><h2>{pf["what_h"]}</h2></div><ul class="ticks">{"".join(f"<li>{x}</li>" for x in c0["items_"+lang])}</ul></section>
<section><div class="sec-head"><h2>{pf["steps_h"]}</h2></div>{pf_steps}</section>
<section><table class="price-table"><tr><th>{c0[lang][0]}</th><th>{t["th"][1]}</th></tr><tr><td>{c0["items_"+lang][0]}</td><td>{r["from_"]} [IDR —]{r["per_day"]}</td></tr></table></section>
<section>{combo}</section><section><div class="sec-head"><h2>{t["faq_short"]}</h2></div>{pf_faq}</section></div>""")

    # CONTACT
    ct = CT[lang]
    page("contact/", ct["h1"], ct["p"], f"""<div class="wrap article">{crumbs("../",(ct["title"],None))}<h1>{ct["h1"]}</h1><p class="lead">{ct["p"]}</p>
<div class="contact-card"><div class="cc-row"><span class="cc-k">{ct["wa"]}</span><a class="cc-v" href="{wa(t['wa_default'])}" target="_blank" rel="noopener">{WA_SHOW}</a></div>
{f'<div class="cc-row"><span class="cc-k">{ct["email"]}</span><a class="cc-v" href="mailto:{EMAIL}">{EMAIL}</a></div>' if EMAIL_OK else ""}
<div class="cc-row"><span class="cc-k">{ct["area"]}</span><span class="cc-v">{ct["area_v"]}</span></div></div>
<div class="cta-row">{btn()}</div></div>""")

    # SERVICES
    page("services/", t["services_t"], t["services_d"], f'<div class="wrap">{crumbs("../",(t["services_h"],None))}<section><div class="sec-head"><h1>{t["services_h"]}</h1></div>{services_grid("../")}</section></div>')
    for s,i,(n,d) in zip(SERVICES,ICONS,t["svc"]):
        hm = "../../"
        page(f"services/{s}/", t["svc_title"].format(s=n), f"{t['svc_h1'].format(s=n)}: {d}", f"""<div class="wrap">{crumbs(hm,(t["services_h"],"services/"),(n,None))}
<div class="hero" style="padding-top:32px"><div><span class="eyebrow">{i} {n}</span><h1>{t["svc_h1"].format(s=n)}</h1><p class="lead">{d}</p>{PR.price_line(s, lang)}{PR.js(lang) if s in PR.PRICES else ""}
<div class="cta-row">{btn(t["check"], t["wa_service"].format(s=n))}<a class="btn btn-ghost" href="{hm}prices/index.html">{t["prices"]}</a></div></div>
<div class="photo"><img src="{{ROOT}}img/{s}.jpg" alt="{n}" width="960" height="640"></div></div>
<section><div class="sec-head"><h2>{t["how"]}</h2></div>{steps}</section><section>{TBm.guar_html(b)}</section><section>{TBm.bring_html(b)}</section><section><div class="sec-head"><h2>{t["faq_short"]}</h2></div>{faq}</section></div>""")

    rows = "".join(f"<tr><td>{n}</td><td>{PR.price_cells(sl, lang)[0]}</td><td>{PR.price_cells(sl, lang)[1]}</td></tr>" for sl,(n,_) in zip(SERVICES, t["svc"]))
    page("prices/", t["prices_t"], t["prices_p"], f"""<div class="wrap">{crumbs("../",(t["prices"],None))}<section><div class="sec-head"><h1>{t["prices_h"]}</h1><p>{t["prices_p"]}</p></div>
{PR.cur_select(lang)}<table class="price-table"><tr>{''.join(f'<th>{x}</th>' for x in t["th"])}</tr>{rows}</table>{PR.js(lang)}<p class="note" style="margin-top:14px">{t["price_note"]}</p><div class="cta-row">{btn(t["quote"])}</div></section></div>""")
    page("how-it-works/", t["hiw_t"], t["hiw_d"], f'<div class="wrap">{crumbs("../",(t["how"],None))}<section><div class="sec-head"><h1>{t["how"]}</h1></div>{steps}</section><section>{TBm.meet_html(b, "{ROOT}")}</section><section>{TBm.check_html(b)}</section><section>{TBm.guar_html(b)}</section><div class="cta-row" style="justify-content:center;margin-bottom:64px">{btn()}</div></div>')
    page("safety/", t["safety_t"], t["safety_d"], f'<div class="wrap">{crumbs("../",(t["safety_nav"],None))}<section><div class="vet-band"><div class="sec-head"><h1 style="color:#fff">{t["safety_t"]}</h1><p>{b["vet_p"]}</p></div>{TBm.vet_html(b)}</div></section><section>{TBm.check_html(b)}</section><section>{TBm.guar_html(b)}</section></div><div class="wrap article" style="padding-top:0"><img class="art-img" src="{{ROOT}}img/safety.jpg" alt="{t["safety_t"]}" loading="lazy">' + "".join(f"<h2>{a}</h2><p>{b}</p>" for a,b in t["safety_body"]) + f"{btn()}</div>")
    page("faq/", t["faq_t"], t["faq_d"], f'<div class="wrap article">{crumbs("../",(t["faq_short"],None))}<h1>{t["faq_t"]}</h1>{faq}<div class="cta-row">{btn()}</div></div>')
    page("careers/", t["careers_t"], t["careers_p"], f'<div class="wrap article">{crumbs("../",(t["careers_h"],None))}<h1>{t["careers_h"]}</h1><p>{t["careers_p"]}</p>{btn(t["apply"], t["apply_msg"])}</div>')

    # GUIDES
    page("guides/", t["guides_t"], t["guides_p"], f'<div class="wrap">{crumbs("../",(t["guides_f"],None))}<section><div class="sec-head"><h1>{t["guides_hh"]}</h1></div>{hub_cards("../")}</section></div>')
    for hb in HUBS:
        hs = hub_slug(hb)
        items = "".join((f'<li><a href="{a["slug"]}/index.html">{a["h1"] if lang=="en" else ARTICLES[lang]["h1"]}</a></li>' if a["id"]==LIVE_ARTICLE else
                         (f'<li>{a["h1"]} <span class="soon">· {t["soon"]}</span></li>' if lang=="en" else "")) for a in A if a["hub"]==hb)
        if lang!="en":
            n = sum(1 for a in A if a["hub"]==hb and a["id"]!=LIVE_ARTICLE)
            items += f'<li class="soon">{n} {t["n_guides"]} — {t["soon"]}</li>'
        page(f"guides/{hs}/", t["hubs"][hb], t["guides_p"], f'<div class="wrap">{crumbs("../../",(t["guides_f"],"guides/"),(t["hubs"][hb],None))}<section><div class="sec-head"><h1>{t["hubs"][hb]}</h1></div><ul class="list">{items}</ul></section></div>')

    a = next(x for x in A if x["id"]==LIVE_ARTICLE)
    art = ARTICLES[lang]
    toc = "".join(f'<li><a href="#s{i}">{h}</a></li>' for i,(h,_) in enumerate(art["secs"],1))
    body = "".join(f'<h2 id="s{i}">{h}</h2><p>{p}</p>'  for i,(h,p) in enumerate(art["secs"],1))
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

# ---- языки из i18n/<code>.json (структура = i18n/en.source.json)
import json as _j
LANG_NAMES = {"en":"English","ru":"Русский","zh":"中文","hi":"हिन्दी","ko":"한국어","ja":"日本語","fr":"Français","de":"Deutsch","es":"Español","it":"Italiano","nl":"Nederlands","id":"Bahasa Indonesia"}
HTML_LANG = {"zh":"zh-CN"}
ARTICLES = {"en": EN_ARTICLE, "ru": RU_ARTICLE}
for _code in [c for c in LANG_NAMES if c not in ("en","ru")]:
    _f = HERE/"i18n"/f"{_code}.json"
    if not _f.exists(): print("skip", _code); continue
    d = _j.loads(_f.read_text(encoding="utf-8"))
    T[_code] = dict(d["T"], prefix=f"{_code}/", html_lang=HTML_LANG.get(_code,_code), other="en", other_label="EN", locale=_code)
    TBm.TB[_code] = d["TB"]; RM.RT[_code] = d["RT"]; AT[_code] = d["AT"]; SM[_code] = d["SM"]; VID[_code] = d["VID"]; ARTICLES[_code] = d["ARTICLE"]
    for c in RM.CATS:
        x = d["CATS"][c["slug"]]; c[_code] = (x["name"], x["desc"]); c["items_"+_code] = x["items"]
    for a in AREAS:
        x = d["AREAS"][a["slug"]]; a[_code] = x["name"]; a[_code+"_lead"] = x["lead"]; a[_code+"_txt"] = x["txt"]

if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
for lang in T: build(lang)
(OUT/"style.css").write_text(CSS, encoding="utf-8")
shutil.copytree(HERE/"src/img", OUT/"img")
shutil.copytree(HERE/"src/video", OUT/"video")
(OUT/".nojekyll").write_text("")
(OUT/"favicon.svg").write_text(FLOWER.replace('class="flower" ','xmlns="http://www.w3.org/2000/svg" ').replace("currentColor","#E8845B"), encoding="utf-8")
(OUT/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n" if INDEXING else "User-agent: *\nDisallow: /\n", encoding="utf-8")
urls = sorted(p.relative_to(OUT).as_posix().replace("index.html","") for p in OUT.rglob("index.html"))
(OUT/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{DOMAIN}/{u}</loc></url>" for u in urls)+"</urlset>", encoding="utf-8")
print(len(urls), "pages ->", OUT)
