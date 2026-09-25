# -*- coding: utf-8 -*-
"""Генератор SEO-книги: агентство нянь в Сануре (Бали), Google, EN + RU."""
import itertools, re
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation

DATE = "2026-09-25"
DOMAIN = "https://[domain]"

# ---------------------------------------------------------------- ХАБЫ
HUBS = {
    "H01": ("Childcare in Sanur", "/guides/childcare/", "Как выбрать и нанять няню, безопасность, цены, форматы ухода"),
    "H02": ("Sanur with Kids: Things to Do", "/guides/things-to-do/", "Досуг, пляжи, парки, активности по возрастам"),
    "H03": ("Family Stays in Sanur", "/guides/where-to-stay/", "Отели, виллы, районы, kids club"),
    "H04": ("Health & Safety for Kids in Bali", "/guides/health-safety/", "Врачи, аптеки, солнце, вода, прививки, безопасность"),
    "H05": ("Family Food in Sanur", "/guides/food/", "Рестораны, кафе, детское питание, продукты"),
    "H06": ("Travel Logistics with Kids", "/guides/travel-logistics/", "Перелёт, визы, транспорт, прокат детского снаряжения"),
    "H07": ("Day Trips from Sanur with Kids", "/guides/day-trips/", "Поездки на день по Бали и островам"),
    "H08": ("Expat Family Life in Sanur", "/guides/expat-family/", "Школы, сады, плейгруппы, жизнь и бюджет"),
}

# ---------------------------------------------------------------- 150 СТАТЕЙ
# (hub, slug, H1, main_kw, [supporting kws], [H2...], audience, stage)
A = []
def art(h, slug, h1, kw, sup, h2, aud="Туристы-семьи", stage="Информационный"):
    A.append(dict(hub=h, slug=slug, h1=h1, kw=kw, sup=sup, h2=h2, aud=aud, stage=stage))

# H01 Childcare (25)
art("H01","how-to-hire-a-nanny-in-sanur","How to Hire a Nanny in Sanur: Step-by-Step Guide for Parents","how to hire a nanny in sanur",["hire nanny sanur","find a nanny in sanur","nanny sanur bali"],["Agency, villa network or freelancer: three ways to find a nanny","What to ask before you book","Checking references and background","Trial session: how to run the first meeting","Agreeing on hours, rules and payment"],"Семьи на отдыхе","Выбор")
art("H01","babysitter-vs-nanny-bali","Babysitter vs Nanny in Bali: Which Do You Need?","babysitter vs nanny bali",["difference between babysitter and nanny","nanny or babysitter holiday"],["Definitions: babysitter, nanny, au pair","Hourly help vs daily care","Which fits a 1-week holiday","Which fits a 3-month stay","Price difference in Bali"],"Семьи на отдыхе","Выбор")
art("H01","nanny-prices-bali","How Much Does a Nanny Cost in Bali in 2026?","nanny cost bali",["babysitter price bali","how much is a nanny in bali","babysitting rates sanur"],["Hourly, daily and monthly rates","What affects the price","Extra costs: transport, overtime, late night","Agency vs freelance price","Tipping etiquette"],"Семьи на отдыхе","Выбор")
art("H01","is-it-safe-to-hire-a-nanny-in-bali","Is It Safe to Hire a Nanny in Bali? A Parent's Safety Checklist","is it safe to hire a nanny in bali",["safe babysitter bali","trusted nanny bali"],["Real risks and how agencies reduce them","Background and ID checks","First aid and CPR certification","Pool and beach supervision rules","Red flags during the trial"],"Семьи на отдыхе","Выбор")
art("H01","questions-to-ask-a-nanny","25 Questions to Ask a Nanny Before Booking in Bali","questions to ask a nanny",["nanny interview questions","babysitter interview questions"],["Experience and age groups","Safety and emergencies","Daily routine and discipline","Food, allergies and medicines","Language and communication"],"Семьи на отдыхе","Выбор")
art("H01","night-nanny-bali","Night Nanny in Bali: When You Need One and How It Works","night nanny bali",["overnight babysitter bali","night babysitter sanur"],["What a night nanny does","Newborns and sleep routines","Hours, rates and rest breaks","Room set-up in a hotel or villa","How to hand over the evening"],"Семьи с младенцами","Выбор")
art("H01","newborn-care-bali","Newborn Care in Bali: Travelling and Getting Help with a Baby Under 3 Months","newborn nanny bali",["baby nurse bali","infant care bali"],["Is Bali OK for a newborn","Newborn-trained nannies: what to check","Feeding, sterilising and bathing abroad","Heat and sun for newborns","Paediatric contacts in Sanur"],"Семьи с младенцами","Информационный")
art("H01","live-in-nanny-bali","Live-In Nanny in Bali: Costs, Contracts and Expectations","live in nanny bali",["full time nanny bali","live in babysitter sanur"],["Live-in vs live-out","Monthly salary and days off","Room, meals and household rules","Written agreement essentials","Handling holidays like Nyepi and Galungan"],"Экспаты","Выбор")
art("H01","nanny-for-expats-sanur","Hiring a Long-Term Nanny as an Expat in Sanur","long term nanny sanur",["expat nanny bali","permanent nanny bali"],["Trial month structure","Salary benchmarks and THR bonus","Legal aspects of household staff","Keeping a good nanny","When to change nanny"],"Экспаты","Выбор")
art("H01","travel-nanny-bali","Travel Nanny in Bali: Taking a Nanny on Day Trips and Island Hops","travel nanny bali",["nanny for day trips bali","holiday nanny bali"],["What a travel nanny covers","Costs of transport, tickets and meals","Car seats and trip safety","Island trips: Nusa Penida, Gili, Lombok","Planning nap times on the road"])
art("H01","babysitter-for-wedding-bali","Babysitting at Weddings and Events in Bali","wedding babysitter bali",["event babysitting bali","kids club for wedding bali"],["How event childcare works","Ratio of sitters to children","Kids' corner set-up","Evening and late-night hours","Booking timelines"],"Организаторы событий","Выбор")
art("H01","hotel-babysitting-sanur","Hotel Babysitting in Sanur: In-House Service vs Independent Nanny","hotel babysitting sanur",["babysitting service hotel bali","resort babysitter sanur"],["What hotels usually offer","Typical hotel rates","Independent nanny coming to your hotel","Hotel rules for external sitters","Which to choose"])
art("H01","nanny-for-twins-bali","Nanny Help for Twins and Multiple Children in Bali","nanny for twins bali",["babysitter for 3 kids bali"],["When one nanny is not enough","Ratios by age","Splitting routines","Cost for siblings","Outings with several kids"],"Семьи с несколькими детьми")
art("H01","special-needs-babysitter-bali","Babysitters for Children with Special Needs in Bali","special needs babysitter bali",["autism babysitter bali","sen nanny bali"],["What experience to ask for","Sharing a care plan","Sensory-friendly places in Sanur","Medical info handover","Honest limits of holiday childcare"],"Семьи с особыми детьми")
art("H01","nanny-first-aid-cpr-bali","Why First Aid and CPR Training Matters for Nannies in Bali","nanny first aid bali",["babysitter cpr certified bali"],["What paediatric first aid covers","Drowning risk and water rescue","Where Bali nannies get certified","How to verify a certificate","Your own emergency card"])
art("H01","english-speaking-nanny-bali","English-Speaking Nanny in Bali: How Good Is the English Really?","english speaking nanny bali",["english nanny sanur"],["Levels of English you will meet","Testing language in the interview","Using simple instructions and apps","Kids learning Bahasa Indonesia","Russian-speaking and other languages"])
art("H01","russian-speaking-nanny-bali","Russian-Speaking Nanny in Bali","russian speaking nanny bali",["няня говорящая по-русски бали"],["Where to find Russian-speaking nannies","Local nannies with basic Russian","Bilingual kids","Price differences","Checking references in community chats"],"Русскоязычные семьи")
art("H01","nanny-house-rules","House Rules for Your Holiday Nanny: A Printable Template","nanny house rules",["babysitter instructions template"],["Screen time and sweets","Pool, beach and street rules","Sleep and nap routine","Emergency contacts","Downloadable template"])
art("H01","first-day-with-new-nanny","The First Day with a New Nanny: How to Help Your Child Adjust","first day with new nanny",["child separation anxiety babysitter"],["Prepare your child","Overlap hour together","Handover checklist","Short first absence","Feedback after the first day"])
art("H01","nanny-tipping-bali","Tipping Nannies and Babysitters in Bali","tipping babysitter bali",["how much to tip nanny bali"],["Is tipping expected","Typical amounts","Gifts vs cash","Tips for long-term nannies","THR bonus explained"])
art("H01","au-pair-bali","Au Pair in Bali: Is It Possible?","au pair bali",["au pair indonesia"],["What an au pair is","Visa realities in Indonesia","Alternatives: nanny, helper","Costs compared","Who this fits"],"Экспаты")
art("H01","kids-club-vs-nanny","Resort Kids Club vs Private Nanny in Sanur","kids club vs nanny",["kids club sanur"],["What kids clubs offer","Age limits and hours","Private nanny advantages","Combining both","Cost comparison"])
art("H01","nanny-reviews-how-to-read","How to Read Nanny Reviews and Spot Fake Recommendations","nanny reviews bali",["babysitter bali reviews"],["Where reviews come from","Facebook group recommendations","Warning signs","Asking for direct references","Our review policy"])
art("H01","date-night-sanur","Date Night in Sanur: Where to Go While the Nanny Watches the Kids","date night sanur",["romantic dinner sanur","couples night out sanur"],["Sunset dinners","Spa for two","Rooftop and beach bars","Timing with bedtime","Booking the sitter"],"Родители")
art("H01","become-a-nanny-bali","How to Become a Nanny in Bali: Skills Families Look For","nanny job bali",["babysitter job sanur","lowongan baby sitter bali"],["Skills and experience","Training and first aid","English for childcare","Working with foreign families","Applying to an agency"],"Соискатели","Информационный")

# H02 Things to do (30)
art("H02","things-to-do-in-sanur-with-kids","Things to Do in Sanur with Kids: The Complete Family Guide","things to do in sanur with kids",["sanur with kids","sanur family activities","sanur for families"],["Beaches","Parks and playgrounds","Water activities","Rainy-day ideas","Evening activities","Sample 3-day plan"])
art("H02","sanur-beach-with-kids","Sanur Beach with Kids: Best Spots, Tides and Safety","sanur beach kids",["best beach sanur for kids","sanur beach family"],["Why Sanur is calm","Best stretches for small kids","Low tide and reef","Shade, toilets and parking","Safety rules"])
art("H02","sanur-beach-path","Walking and Cycling the Sanur Beach Path with a Stroller","sanur beach path",["sanur boardwalk","stroller sanur"],["Route and distance","Stroller-friendly sections","Bike hire with child seats","Stops along the way","Best time of day"])
art("H02","sanur-playgrounds","Playgrounds in Sanur: Free and Paid Options","playground sanur",["kids play area sanur","indoor playground sanur"],["Beach playgrounds","Cafe play areas","Indoor soft play","Age suitability","Map"])
art("H02","rainy-day-sanur-kids","Rainy Day Activities in Sanur with Kids","rainy day sanur kids",["indoor activities sanur"],["Indoor play centres","Craft and cooking classes","Cinemas and malls nearby","Museums","Home activities"])
art("H02","bali-with-toddlers","Bali with a Toddler: What Works in Sanur","bali with toddler",["sanur with toddler","toddler activities bali"],["Why Sanur for toddlers","Daily rhythm in the heat","Best toddler activities","Gear to bring","Nap-friendly outings"],"Семьи с малышами")
art("H02","bali-with-a-baby","Bali with a Baby: Practical Guide for Sanur","bali with baby",["sanur with baby","travel bali with infant"],["Is Bali baby-friendly","Where to stay","Heat, sun and feeding","Baby gear hire","Getting help with a nanny"],"Семьи с младенцами")
art("H02","sanur-with-teenagers","Sanur with Teenagers: Activities That Aren't Boring","sanur with teenagers",["teen activities bali"],["Surf and kitesurf lessons","Snorkel and dive courses","Cycling","Cafes and hangouts","Day trips they'll like"])
art("H02","kitesurfing-sanur-kids","Kitesurfing and Windsurfing in Sanur for Kids","kitesurfing sanur kids",["kite school sanur"],["Season and wind","Minimum age","Schools and prices","Safety equipment","What parents do meanwhile"])
art("H02","snorkeling-sanur-kids","Snorkeling in Sanur with Kids","snorkeling sanur kids",["snorkeling sanur"],["Best spots and tides","Boat trips","Gear for kids","Safety","Coral etiquette"])
art("H02","sup-sanur-kids","Stand-Up Paddleboarding in Sanur with Children","sup sanur",["paddle board sanur kids"],["Why Sanur suits SUP","Rental and prices","Kids on board","Best time","Safety"])
art("H02","swimming-lessons-sanur","Swimming Lessons for Kids in Sanur","swimming lessons sanur",["kids swim school bali"],["Private vs group lessons","Age groups","Pools used","Prices","What to bring"])
art("H02","bali-zoo-with-kids","Bali Zoo with Kids: Worth the Trip from Sanur?","bali zoo kids",["bali zoo from sanur"],["Getting there from Sanur","Tickets and packages","Animal encounters","Best time and duration","Tips with toddlers"])
art("H02","bali-safari-park-kids","Bali Safari and Marine Park with Kids","bali safari park kids",["taman safari bali"],["Distance from Sanur","Tickets","Water park section","Night safari","Food and shade"])
art("H02","bali-bird-park-kids","Bali Bird Park with Kids","bali bird park",["bird park bali kids"],["What to see","Tickets","Duration","Accessibility","Combine with nearby"])
art("H02","waterbom-bali-kids","Waterbom Bali with Kids: Tips for Families from Sanur","waterbom bali kids",["waterbom from sanur"],["Distance and transport","Slides by age","Tickets and cabanas","Food and lockers","Best day to go"])
art("H02","sea-turtle-sanur","Turtle Conservation Near Sanur: Serangan Turtle Centre","turtle conservation sanur",["serangan turtle"],["What the centre does","Visiting with kids","Ethics","Hatchling release","Getting there"])
art("H02","mangrove-tour-sanur","Mangrove Tour Near Sanur with Kids","mangrove tour sanur",["mangrove forest bali kids"],["Kayak or boardwalk","Age suitability","Tides","What to bring","Prices"])
art("H02","sanur-kite-festival","Bali Kite Festival in Sanur: A Family Guide","bali kite festival",["kite festival sanur"],["When it happens","Where to watch","Kids and crowds","Photo tips","Other festivals"])
art("H02","cooking-class-kids-sanur","Kids' Cooking Classes in Sanur","cooking class sanur kids",["bali cooking class family"],["Formats","Ages","Menu examples","Prices","Allergies"])
art("H02","art-craft-classes-sanur","Art and Craft Classes for Kids in Sanur","kids art class sanur",["batik class kids bali","craft workshop sanur"],["Batik and painting","Silver and wood","Ages","Duration","Booking"])
art("H02","sanur-night-market-kids","Sanur Night Market with Kids","sanur night market",["pasar malam sindhu"],["What to eat","Hygiene tips","Kid-friendly dishes","Cash and prices","Best time"])
art("H02","bali-culture-for-kids","Balinese Culture for Kids: Temples, Dance and Ceremonies","bali culture kids",["kecak dance kids","temple visit with kids bali"],["Temple etiquette with kids","Dance shows","Ceremonies you'll see in Sanur","Offerings explained","Questions kids ask"])
art("H02","sanur-3-day-itinerary-family","3-Day Sanur Itinerary for Families","sanur itinerary family",["3 days in sanur"],["Day 1","Day 2","Day 3","Adjustments by age","Budget"])
art("H02","sanur-1-week-family","One Week in Sanur with Kids","one week in sanur",["7 days sanur family"],["Pace","Beach days","Day trips","Rest days","Nanny time for parents"])
art("H02","free-things-sanur-kids","Free Things to Do in Sanur with Kids","free things to do sanur",["cheap activities sanur kids"],["Beach and path","Playgrounds","Sunrise","Temples","Markets"])
art("H02","sanur-sunrise-kids","Sunrise in Sanur with Kids: Best Spots","sunrise sanur",["sindhu beach sunrise"],["Best beaches for sunrise","Timing by month","Breakfast after","Photography","Early wake-up tips"])
art("H02","birthday-party-sanur","Kids' Birthday Party in Sanur: Venues and Ideas","birthday party sanur",["kids party bali","birthday venue sanur"],["Venues","Party organisers","Cakes","Entertainers","Budget"],"Родители","Выбор")
art("H02","sanur-kids-events-calendar","Kids' Events in Sanur: Monthly Calendar","sanur events",["kids events bali"],["Regular weekly events","Holidays","Festivals","Where to check","Seasonality"])
art("H02","bali-animals-kids","Animal Experiences in Bali: Ethical Choices for Kids","animal experiences bali",["elephant bali ethical"],["Ethical criteria","Recommended places","Places to avoid","Age suitability","Near Sanur"])

# H03 Where to stay (15)
art("H03","family-hotels-sanur","Best Family Hotels in Sanur","family hotel sanur",["sanur hotel with kids club","kid friendly hotel sanur"],["What makes a hotel family-friendly","Beachfront options","Budget options","Kids club comparison","Babysitting availability"],"Туристы-семьи","Выбор")
art("H03","family-villas-sanur","Family Villas in Sanur: What to Check Before Booking","family villa sanur",["villa sanur kids","pool fence villa bali"],["Pool safety","Bedrooms and cots","Kitchen","Location","Nanny room"],"Туристы-семьи","Выбор")
art("H03","pool-safety-villa-bali","Villa Pool Safety in Bali: A Parent's Checklist","pool safety bali villa",["pool fence bali"],["Fences and covers","Supervision rules","Floaties vs vests","Drowning signs","Renting a pool fence"])
art("H03","where-to-stay-in-sanur","Where to Stay in Sanur: North, Central or South?","where to stay in sanur",["sanur areas","best area sanur"],["North Sanur","Central Sanur/Sindhu","South Sanur/Mertasari","Inland vs beachfront","For long stays"])
art("H03","sanur-vs-nusa-dua-families","Sanur vs Nusa Dua for Families","sanur vs nusa dua",["nusa dua or sanur kids"],["Beaches","Hotels","Food and walking","Prices","Verdict by family type"])
art("H03","sanur-vs-canggu-families","Sanur vs Canggu for Families","sanur vs canggu",["canggu or sanur family"],["Vibe and traffic","Beaches","Schools","Cost","Verdict"])
art("H03","sanur-vs-ubud-families","Sanur vs Ubud with Kids","sanur vs ubud",["ubud or sanur family"],["Climate","Activities","Stays","Split your trip?","Verdict"])
art("H03","best-area-bali-families","Best Area in Bali for Families","best area in bali for families",["where to stay in bali with kids"],["Sanur","Nusa Dua","Jimbaran","Ubud","Canggu","How to decide"])
art("H03","hotels-with-kids-club-bali","Hotels with Kids Clubs near Sanur","kids club hotel sanur",["resort kids club bali"],["What to compare","Ages and fees","Hotels in Sanur","Alternatives","Nanny + hotel combo"])
art("H03","long-term-rental-sanur-family","Long-Term Rentals in Sanur for Families","long term rental sanur",["monthly villa sanur","rent house sanur"],["Prices by month","Areas","Contracts","Checks with kids","Utilities"],"Экспаты","Выбор")
art("H03","family-apartments-sanur","Family Apartments and Guesthouses in Sanur","apartment sanur",["guesthouse sanur family"],["When apartments fit","Budget ranges","Kitchens","Noise","Booking tips"])
art("H03","cot-high-chair-hotel-bali","Cots, High Chairs and Baby Amenities in Bali Hotels","baby cot hotel bali",["baby friendly hotel bali"],["What to request","Safety of cots","Renting gear instead","Bath and sterilising","Checklist"])
art("H03","villa-staff-bali","Villa Staff in Bali: Housekeepers, Cooks and Nannies","villa staff bali",["villa nanny bali"],["Who does what","Villa-provided nannies","Pros and cons","Costs","Etiquette"])
art("H03","quiet-hotels-sanur-babies","Quiet Hotels in Sanur for Babies","quiet hotel sanur",["hotel sanur baby"],["Noise sources","Room choice","Blackout","Nearby clinics","Picks"])
art("H03","sanur-accommodation-budget","Family Accommodation Budget in Sanur","sanur accommodation prices",["cost of hotel sanur"],["Budget tiers","Seasonality","What's included","Hidden costs","Saving tips"])

# H04 Health & safety (20)
art("H04","paediatrician-sanur","Paediatricians and Kids' Clinics in Sanur","pediatrician sanur",["kids doctor sanur","children clinic sanur"],["Clinics in Sanur","International hospitals nearby","Home visits","Costs and insurance","What to bring"],"Все семьи","Информационный")
art("H04","hospitals-near-sanur","Hospitals Near Sanur for Children","hospital sanur",["international hospital bali kids","emergency sanur"],["Nearest emergency options","International vs local","Ambulance","Insurance","Emergency numbers"])
art("H04","bali-belly-kids","Bali Belly in Kids: Prevention and When to See a Doctor","bali belly kids",["diarrhea child bali"],["Causes","Prevention","Hydration","Warning signs","Pharmacy items"])
art("H04","sun-safety-kids-bali","Sun Safety for Kids in Bali","sun protection kids bali",["sunscreen bali kids"],["UV index","Hours to avoid","Clothing","Sunscreen","Heat stroke"])
art("H04","dengue-kids-bali","Dengue and Mosquitoes: Protecting Kids in Bali","dengue bali kids",["mosquito repellent kids bali"],["Risk by season","Repellents by age","Nets and rooms","Symptoms","Vaccine info (verify)"])
art("H04","vaccinations-kids-bali","Vaccinations for Kids Travelling to Bali","vaccines for bali kids",["bali travel vaccinations children"],["Routine vaccines","Recommended extras","Rabies","Timing","Sources to check"])
art("H04","rabies-bali-kids","Rabies in Bali: What Parents Should Know","rabies bali",["dog bite bali child"],["Risk","Avoiding animals","After a bite","Where to get PEP","Monkeys"])
art("H04","water-safety-sanur","Water Safety for Kids in Sanur","water safety bali kids",["drowning prevention bali"],["Sea and tides","Pools","Supervision rules","Swim aids","Teaching kids"])
art("H04","pharmacy-sanur","Pharmacies in Sanur: Kids' Medicines and What to Ask For","pharmacy sanur",["apotek sanur","kids medicine bali"],["Where to find","Common medicines","Names in Indonesia","Prescriptions","Night pharmacies"])
art("H04","travel-insurance-kids-bali","Travel Insurance for Kids in Bali","travel insurance bali kids",["insurance for family bali"],["What to cover","Evacuation","Activities","Claims","Checklist"])
art("H04","first-aid-kit-bali-kids","First Aid Kit for Bali with Kids","first aid kit bali",["travel medicine kit kids"],["Essentials","Bali-specific items","Buy locally","Storage in heat","Printable list"])
art("H04","drinking-water-bali-kids","Is Tap Water Safe in Bali for Kids?","tap water bali",["drinking water bali baby"],["Tap water","Bottled vs refill","Formula prep","Brushing teeth","Ice"])
art("H04","jet-lag-kids-bali","Jet Lag in Kids after Flying to Bali","jet lag kids bali",["baby jet lag bali"],["How long it lasts","Light and schedule","Naps","Night waking","Using a night nanny"])
art("H04","heat-rash-kids-bali","Heat Rash and Skin Issues in Kids in Bali","heat rash bali",["baby rash tropical"],["Heat rash","Bites","Sunburn","Fungal","When to see a doctor"])
art("H04","road-safety-kids-bali","Road Safety with Kids in Bali: Scooters, Cars and Walking","road safety bali kids",["kids on scooter bali"],["Scooter risks","Car seats","Crossing roads","Drivers","Sanur specifics"])
art("H04","monkeys-kids-bali","Monkeys and Kids in Bali: Safety Rules","monkey forest kids",["uluwatu monkeys children"],["Where monkeys are","Rules","Bites","Belongings","Better alternatives"])
art("H04","sea-lice-jellyfish-sanur","Jellyfish and Sea Stings in Sanur","jellyfish sanur",["sea lice bali"],["Season","Symptoms","First aid","Prevention","When to worry"])
art("H04","child-emergency-plan-bali","Emergency Plan for Families in Bali","emergency bali",["bali emergency numbers"],["Numbers","Hospital route","Documents","Nanny briefing","Printable card"])
art("H04","volcano-earthquake-bali-family","Volcanoes and Earthquakes in Bali: Family Preparedness","bali volcano safety",["earthquake bali what to do"],["Risk context","Official sources","What to do","Airport disruptions","Kit"])
art("H04","kids-dentist-sanur","Kids' Dentist in Sanur","dentist sanur kids",["pediatric dentist bali"],["Options","Costs","Emergencies","Language","Insurance"])

# H05 Food (12)
art("H05","kid-friendly-restaurants-sanur","Kid-Friendly Restaurants in Sanur","kid friendly restaurants sanur",["family restaurants sanur","restaurant with playground sanur"],["With playgrounds","Beachfront","Healthy picks","Budget","Evening options"])
art("H05","cafes-with-play-area-sanur","Cafes with Play Areas in Sanur","cafe play area sanur",["kids cafe sanur"],["List","Age range","Food","Prices","Tips"])
art("H05","baby-food-bali","Baby Food and Formula in Bali: What You Can Buy","baby formula bali",["baby food sanur"],["Formula brands","Jars and pouches","Organic","Where to buy","Bring or buy"],"Семьи с младенцами")
art("H05","supermarkets-sanur","Supermarkets in Sanur for Families","supermarket sanur",["grocery sanur"],["Main stores","Imported goods","Delivery apps","Prices","Kids items"])
art("H05","picky-eaters-bali","Picky Eaters in Bali: Local Food Kids Actually Like","food for kids bali",["indonesian food kids"],["Safe starter dishes","Spice level phrases","Fruit","Snacks","Hygiene"])
art("H05","allergies-bali-kids","Food Allergies in Bali: Travelling with an Allergic Child","food allergy bali",["nut allergy bali"],["Allergy cards in Bahasa","Hidden ingredients","Restaurants","Epipens","Hospitals"])
art("H05","healthy-food-sanur","Healthy Food Spots in Sanur for Families","healthy food sanur",["vegan sanur","organic sanur"],["Cafes","Markets","Smoothies","Delivery","Budget"])
art("H05","food-delivery-sanur","Food Delivery in Sanur: Gojek, Grab and More","food delivery sanur",["gofood sanur"],["Apps","Payments","Kids options","Hygiene","Tips"])
art("H05","breakfast-sanur-kids","Breakfast Spots in Sanur for Early-Rising Kids","breakfast sanur",["best breakfast sanur"],["Open early","Beachfront","Budget","Kids menu","Parking"])
art("H05","fruit-bali-kids","Tropical Fruit in Bali for Kids","bali fruit",["tropical fruits bali"],["Fruit by season","Washing","Allergies","Markets","Prices"])
art("H05","bakeries-sanur","Bakeries and Birthday Cakes in Sanur","bakery sanur",["birthday cake sanur"],["Bakeries","Cake orders","Allergy-friendly","Prices","Delivery"])
art("H05","eating-out-budget-sanur","Eating Out Budget in Sanur for a Family","food prices sanur",["cost of food sanur"],["Warung prices","Mid-range","Western","Groceries","Saving tips"])

# H06 Travel logistics (18)
art("H06","flying-to-bali-with-baby","Flying to Bali with a Baby","flying to bali with baby",["long haul flight baby bali"],["Choosing flights","Bassinets","Feeding on board","Transit","Arrival at DPS"],"Семьи с младенцами","Планирование")
art("H06","bali-visa-kids","Bali Visa and Entry Rules for Children","bali visa kids",["visa on arrival bali child","bali tourist levy children"],["Visa options","Passport validity","Levy","Customs","Official sources"],"Все семьи","Планирование")
art("H06","airport-to-sanur","Bali Airport to Sanur with Kids","airport to sanur",["dps to sanur","transfer sanur"],["Distance","Transfer options","Car seats","Prices","Arrival tips"])
art("H06","car-seat-bali","Car Seats in Bali: Rent, Bring or Book a Driver with One","car seat bali",["car seat rental bali"],["The law and reality","Rental","Drivers","Travel seats","Tips"])
art("H06","baby-equipment-hire-bali","Baby Equipment Hire in Sanur","baby equipment hire bali",["stroller rental bali","cot hire sanur"],["What you can rent","Prices","Delivery","Hygiene","Bring vs rent"])
art("H06","stroller-bali","Stroller or Carrier in Bali?","stroller bali",["baby carrier bali"],["Pavements","Sanur path","Best types","Carrier tips","Rental"])
art("H06","packing-list-bali-kids","Bali Packing List for Kids","packing list bali kids",["what to pack bali baby"],["Clothes","Health","Gear","Buy locally","Printable"])
art("H06","best-time-bali-families","Best Time to Visit Bali with Kids","best time to visit bali with kids",["bali weather by month","school holidays bali"],["Dry vs wet season","Sanur weather","Crowds","Prices","Holidays"])
art("H06","getting-around-sanur","Getting Around Sanur with Kids","getting around sanur",["transport sanur"],["Walking","Bikes","Taxis and apps","Drivers","Scooters"])
art("H06","hire-driver-bali-family","Hiring a Private Driver in Bali for Families","private driver bali",["bali driver with car seat"],["Pricing","Full vs half day","Car seats","Vetting","Itineraries"])
art("H06","sanur-fast-boat-kids","Fast Boats from Sanur with Kids","fast boat sanur",["sanur to nusa penida boat kids"],["Destinations","Safety","Seasickness","Tickets","Life jackets"])
art("H06","sim-card-bali","SIM Cards and Internet in Bali for Families","sim card bali",["esim bali"],["Options","Prices","Coverage in Sanur","Apps you need","Tips"])
art("H06","money-bali-family","Money in Bali: Cash, Cards and ATMs","money bali",["atm sanur"],["Cash vs card","ATMs","Scams","Tipping","Budgeting"])
art("H06","bali-holiday-budget-family","Bali Family Holiday Budget","bali family holiday cost",["how much bali trip family"],["Flights","Stay","Food","Activities","Nanny"],"Туристы-семьи","Планирование")
art("H06","nyepi-with-kids","Nyepi (Silent Day) with Kids in Bali","nyepi with kids",["nyepi bali tourists"],["What happens","Rules","Ogoh-ogoh night","Planning food","Keeping kids busy"])
art("H06","bali-school-holidays","Bali During School Holidays: What to Expect","bali school holidays",["bali christmas family"],["Peak periods","Prices","Booking ahead","Crowds in Sanur","Alternatives"])
art("H06","bali-phrases-parents","Useful Bahasa Indonesia Phrases for Parents","bahasa indonesia phrases",["basic indonesian phrases"],["Greetings","At restaurants","At the doctor","With the nanny","Numbers"])
art("H06","travel-with-kids-apps-bali","Useful Apps for Families in Bali","apps for bali",["gojek grab bali"],["Transport","Food","Maps","Translation","Health"])

# H07 Day trips (15)
art("H07","day-trips-from-sanur-kids","Day Trips from Sanur with Kids","day trips from sanur",["sanur day trip family"],["Under 1 hour","1–2 hours","Islands","Tips for car rides","Nanny on trips"])
art("H07","nusa-lembongan-with-kids","Nusa Lembongan with Kids from Sanur","nusa lembongan kids",["lembongan day trip family"],["Boat","Beaches","Activities","Stay overnight?","Safety"])
art("H07","nusa-penida-with-kids","Nusa Penida with Kids: Is It Worth It?","nusa penida kids",["nusa penida family"],["Roads and stairs","What to skip","Best spots","Tours","Verdict"])
art("H07","ubud-day-trip-kids","Ubud Day Trip from Sanur with Kids","ubud with kids",["ubud day trip sanur"],["Route","Rice terraces","Monkey forest caution","Swings","Lunch"])
art("H07","tegenungan-waterfall-kids","Waterfalls near Sanur for Kids","waterfall near sanur",["tegenungan waterfall kids"],["Nearest waterfalls","Stairs","Swimming","Safety","Timing"])
art("H07","rice-terraces-kids","Rice Terraces with Kids","tegalalang with kids",["jatiluwih family"],["Which terraces","Walks","Heat","Swings","Photos"])
art("H07","uluwatu-with-kids","Uluwatu with Kids","uluwatu kids",["uluwatu temple family"],["Temple and monkeys","Kecak","Beaches","Distance","Tips"])
art("H07","kintamani-kids","Kintamani and Mount Batur with Kids","kintamani kids",["mount batur family"],["Views","Hot springs","Jeep tours","Age limits","Weather"])
art("H07","bedugul-kids","Bedugul and Botanic Garden with Kids","bedugul kids",["bali botanic garden kids"],["Botanic garden","Treetop adventure","Temple","Cool weather","Food"])
art("H07","amed-with-kids","Amed with Kids","amed kids",["amed snorkeling family"],["Getting there","Snorkel","Stay","Food","Pace"])
art("H07","gili-islands-kids","Gili Islands with Kids","gili islands kids",["gili air family"],["Which Gili","Boats","No cars","Stay","Medical"])
art("H07","lovina-dolphins-kids","Lovina Dolphins with Kids","lovina dolphins",["lovina family"],["Ethics","Boat","Timing","Stay","Alternatives"])
art("H07","jimbaran-with-kids","Jimbaran and Nusa Dua with Kids","jimbaran kids",["nusa dua day trip"],["Beaches","Seafood dinner","Parks","Distance","Tips"])
art("H07","denpasar-with-kids","Denpasar with Kids: Museums, Malls and Markets","denpasar kids",["denpasar family attractions"],["Museum","Malls","Markets","Parks","Traffic"])
art("H07","private-tour-bali-family","Private Family Tours in Bali","private tour bali family",["bali tour with kids"],["Tour types","Pricing","Guides","Nanny joining","Custom plans"])

# H08 Expat family (15)
art("H08","international-schools-sanur","International Schools in Sanur","international school sanur",["school sanur","schools in sanur bali"],["Schools in Sanur","Curricula","Fees","Admissions","Visits"],"Экспаты","Выбор")
art("H08","kindergarten-sanur","Kindergartens and Preschools in Sanur","kindergarten sanur",["preschool sanur","daycare sanur"],["Options","Ages","Fees","Languages","Trial days"],"Экспаты","Выбор")
art("H08","daycare-bali","Daycare in Bali vs a Nanny","daycare bali",["childcare centre bali"],["Daycare options","Nanny at home","Cost","Illness","Mix"],"Экспаты","Выбор")
art("H08","playgroups-sanur","Playgroups and Parent Communities in Sanur","playgroup sanur",["mums group sanur","parents sanur"],["Playgroups","Facebook groups","Telegram chats","Events","Making friends"],"Экспаты")
art("H08","moving-to-sanur-with-family","Moving to Sanur with a Family","moving to sanur",["living in sanur with kids","relocate to bali family"],["Why Sanur","Visas","Housing","Schools","Healthcare"],"Экспаты","Планирование")
art("H08","cost-of-living-sanur-family","Cost of Living in Sanur for a Family","cost of living sanur",["cost of living bali family"],["Rent","Schools","Food","Nanny/helper","Healthcare"],"Экспаты","Планирование")
art("H08","visa-families-bali","Long-Stay Visas for Families in Bali","bali visa family",["kitas family bali","second home visa bali"],["Visa types","Dependants","Costs","Agents","Official sources"],"Экспаты","Планирование")
art("H08","homeschooling-bali","Homeschooling and Worldschooling in Bali","homeschooling bali",["worldschooling bali"],["Approaches","Communities","Tutors","Legal","Resources"],"Экспаты")
art("H08","after-school-activities-sanur","After-School Activities in Sanur","activities for kids sanur",["kids classes sanur"],["Sports","Arts","Languages","Swim","Schedules"],"Экспаты")
art("H08","tutors-sanur","Tutors in Sanur: English, Maths and More","tutor sanur",["private tutor bali"],["Subjects","Prices","Finding","Online vs offline","Checks"],"Экспаты")
art("H08","helper-vs-nanny-bali","Pembantu, Helper or Nanny: Household Help in Bali","helper bali",["pembantu bali","housekeeper sanur"],["Roles","Pay","Overlap","Contracts","Culture"],"Экспаты")
art("H08","nanny-salary-bali","Nanny Salary in Bali (Monthly)","nanny salary bali",["babysitter salary bali"],["Salary ranges","Experience premium","Overtime","THR","Benefits"],"Экспаты")
art("H08","working-parents-bali","Remote-Working Parents in Sanur: Childcare Set-Ups","digital nomad family bali",["coworking sanur kids"],["Coworking","Childcare schedules","Nanny + coworking","Budgets","Routines"],"Экспаты")
art("H08","birth-in-bali","Giving Birth in Bali: Hospitals and Postpartum Help","giving birth in bali",["maternity bali","postpartum doula bali"],["Hospitals","Costs","Documents","Postpartum support","Night nanny"],"Экспаты")
art("H08","kids-sports-sanur","Kids' Sports Clubs in Sanur","kids sports sanur",["football kids sanur","gymnastics bali kids"],["Football","Martial arts","Tennis","Surf","Schedules"],"Экспаты")

assert len(A) == 150, len(A)

# ---------------------------------------------------------------- КОММЕРЧЕСКИЕ СТРАНИЦЫ
COMM = [
 ("C01","/","Nanny & Babysitting Agency in Sanur, Bali","nanny sanur",["babysitter sanur","nanny agency sanur","babysitting sanur bali"]),
 ("C02","/services/hourly-babysitter/","Hourly Babysitter in Sanur","babysitter sanur",["hourly babysitter bali","babysitter tonight sanur"]),
 ("C03","/services/day-nanny/","Full-Day Nanny in Sanur","day nanny sanur",["full day nanny bali"]),
 ("C04","/services/night-nanny/","Night Nanny in Sanur","night nanny sanur",["overnight nanny sanur"]),
 ("C05","/services/newborn-nanny/","Newborn & Baby Nanny in Sanur","newborn nanny sanur",["baby nanny sanur"]),
 ("C06","/services/long-term-nanny/","Long-Term & Live-In Nanny for Expat Families","long term nanny bali",["live in nanny sanur"]),
 ("C07","/services/travel-nanny/","Travel Nanny for Day Trips in Bali","travel nanny bali",["nanny day trip bali"]),
 ("C08","/services/event-babysitting/","Event & Wedding Babysitting in Bali","wedding babysitting bali",["event babysitter bali"]),
 ("C09","/services/hotel-villa-babysitting/","Babysitter to Your Hotel or Villa in Sanur","hotel babysitter sanur",["villa babysitter sanur"]),
 ("C10","/prices/","Nanny & Babysitting Prices in Sanur","babysitter price sanur",["nanny rates bali"]),
 ("C11","/how-it-works/","How Booking a Nanny Works","book a nanny bali",["book babysitter sanur"]),
 ("C12","/our-nannies/","Meet Our Nannies","nannies in sanur",[]),
 ("C13","/safety/","Our Safety Standards","safe nanny bali",[]),
 ("C14","/reviews/","Parent Reviews","babysitter sanur reviews",[]),
 ("C15","/faq/","FAQ","",[]),
 ("C16","/book/","Book a Nanny","",[]),
 ("C17","/careers/","Become a Nanny","nanny job sanur",["lowongan baby sitter sanur"]),
 ("C18","/about/","About Us","",[]),
 ("C23","/guides/","Family Guide to Sanur","sanur family guide",[]),
]

# ---------------------------------------------------------------- СЕМАНТИКА
queries = []  # dict(q, lang, intent, page, cluster, source, status, reason)
seen = set()
def addq(q, lang, intent, page, src, status="принято по смыслу", reason="Маркер ветки карты; задача совпадает со страницей"):
    n = re.sub(r"\s+"," ",q.strip().lower())
    if not n or n in seen: return
    seen.add(n)
    queries.append(dict(raw=q, norm=n, lang=lang, intent=intent, page=page, src=src, status=status, reason=reason))

# 1) коммерческие: матрица услуга × гео × модификатор
services_en = ["nanny","babysitter","babysitting","baby sitter","childcare","nanny service","babysitting service","nanny agency","child minder","kids sitter"]
geo = ["sanur","sanur bali","bali","denpasar","sanur beach"]
mods = ["","best","trusted","english speaking","hourly","private","cheap","24 hour","near me","for tourists","for toddlers","for baby","price","cost","rates","book","agency","reviews","recommendations","tonight","weekend","hotel","villa","experienced","certified"]
svc_page = {"nanny":"C01","babysitter":"C02","babysitting":"C01","baby sitter":"C02","childcare":"C01","nanny service":"C01","babysitting service":"C01","nanny agency":"C01","child minder":"C02","kids sitter":"C02"}
mod_page = {"price":"C10","cost":"C10","rates":"C10","cheap":"C10","book":"C11","reviews":"C14","recommendations":"C14","hotel":"C09","villa":"C09","hourly":"C02","tonight":"C02","for baby":"C05"}
for s,g,m in itertools.product(services_en, geo, mods):
    if m=="near me" and g not in ("sanur","bali"): continue
    q = (f"{m} {s} {g}" if m in ("best","trusted","english speaking","hourly","private","cheap","24 hour","experienced","certified") else f"{s} {g} {m}").strip()
    if m=="near me": q=f"{s} near me {g}"
    page = mod_page.get(m, svc_page[s])
    st = "принято по смыслу"
    rs = "Коммерческий маркер: услуга + гео + модификатор"
    if g=="denpasar":
        st="требует проверки"; rs="Денпасар — обслуживается ли реально? Решить с бизнесом; геостраницу не создавать без реального обслуживания"
    if m in ("cheap",):
        st="требует проверки"; rs="Ценовой модификатор; проверить соответствие позиционированию"
    addq(q,"en","Коммерческий",page,"S01",st,rs)
for sv,pg in [("night nanny","C04"),("overnight nanny","C04"),("newborn nanny","C05"),("baby nurse","C05"),("live in nanny","C06"),("full time nanny","C06"),("long term nanny","C06"),("travel nanny","C07"),("holiday nanny","C07"),("wedding babysitter","C08"),("event babysitting","C08"),("kids club for wedding","C08"),("day nanny","C03"),("full day nanny","C03"),("nanny for twins","C01"),("nanny job","C17"),("babysitter job","C17")]:
    for g in ["sanur","bali","sanur bali"]:
        for m in ["","price","agency","english speaking","book"]:
            q = f"{m} {sv} {g}".strip() if m=="english speaking" else f"{sv} {g} {m}".strip()
            addq(q,"en","Коммерческий",pg if m!="price" else "C10","S01")

# 2) индонезийский (соискатели и местные)
for q in ["lowongan baby sitter bali","lowongan baby sitter sanur","lowongan nanny bali","jasa baby sitter bali","jasa baby sitter sanur","baby sitter harian bali","yayasan baby sitter bali","gaji baby sitter bali","lowongan pengasuh anak bali","pengasuh anak sanur"]:
    addq(q,"id","Коммерческий/вакансии","C17","S01","требует проверки","Индонезийский язык: часть запросов — поиск услуги местными, часть — вакансии; решить, нужна ли /id/ версия")

# 3) русские
RU = [("няня санур","C01"),("няня бали","C01"),("няня на бали","C01"),("няня на бали для ребенка","C01"),("бебиситтер бали","C01"),("бебиситтер санур","C01"),("найти няню на бали","C01"),("агентство нянь бали","C01"),("няня бали отзывы","C01"),("русскоязычная няня бали","C01"),("няня на час бали","C01"),("няня в отель бали","C01"),("няня на виллу бали","C01"),("няня для младенца бали","C04"),("ночная няня бали","C04"),("няня бали цена","C10"),("сколько стоит няня на бали","C10"),("зарплата няни на бали","C10"),("няня с проживанием бали","C06"),("няня на бали на постоянку","C06"),("няня на длительный срок бали","C06"),
      ("санур с детьми","A026"),("бали с детьми","A026"),("куда сходить с детьми санур","A026"),("чем заняться в сануре с детьми","A026"),("пляж санур с детьми","A027"),("санур или нуса дуа с детьми","A060"),("санур или чангу с детьми","A061"),("где жить на бали с детьми","A063"),("отели санур для детей","A056"),("виллы санур с детьми","A057"),("бали с грудничком","A032"),("бали с ребенком до года","A032"),("бали с годовалым ребенком","A031"),("перелет на бали с ребенком","A103"),("виза на бали для ребенка","A104"),("прививки на бали детям","A076"),("педиатр санур","A071"),("детский врач бали","A071"),("больница санур","A072"),("бали белли у ребенка","A073"),("денге бали дети","A075"),("вода на бали ребенку","A082"),("детские рестораны санур","A091"),("детская смесь бали","A093"),("аренда детской коляски бали","A107"),("автокресло бали","A106"),("когда лучше ехать на бали с детьми","A110"),("школы санур","A136"),("детский сад санур","A137"),("международная школа бали","A136"),("переезд на бали с детьми","A140"),("стоимость жизни на бали с семьей","A141"),("нуса пенида с детьми","A123"),("убуд с детьми","A124"),("аквапарк бали с детьми","A041"),("бали зоопарк","A038"),("бали сафари парк","A039"),("ньепи с детьми","A117")]
for q,p in RU: addq(q,"ru","Коммерческий" if p.startswith("C") else "Информационный",p,"S02")

# 4) информационные: из плана статей + производные
for i,a in enumerate(A,1):
    pid=f"A{i:03d}"; a["id"]=pid
    addq(a["kw"],"en","Информационный",pid,"S03")
    for s in a["sup"]:
        lang = "ru" if re.search("[а-я]",s) else ("id" if s.startswith(("lowongan","pasar","apotek","pembantu","taman")) else "en")
        addq(s,lang,"Информационный",pid,"S03")
    k=a["kw"]
    if "sanur" in k: addq(k.replace("sanur","bali"),"en","Информационный",pid,"S03","требует проверки","Расширение Sanur→Bali: может требовать общебалийской страницы; проверить выдачу")
    elif "bali" in k: addq(k.replace("bali","sanur"),"en","Информационный",pid,"S03","требует проверки","Сужение Bali→Sanur: спрос может быть нулевым")
    if not k.startswith(("how","is","what","best","where","when")): addq(f"best {k}","en","Информационный",pid,"S03","требует проверки","Модификатор best: вероятно подборочный формат")
    addq(f"{k} 2026","en","Информационный",pid,"S03","требует проверки","Годовой модификатор; сезонный хвост")

# ---------------------------------------------------------------- НАБЛЮДЕННАЯ ВЫДАЧА (реальные данные этой сессии)
SERP = {
 "nanny sanur bali":["greataupair.com/Hire_Nanny_Babysitter/Aupair_Tutor_Housekeeper/Bali/Sanur.htm","balisbestbabysitting.com/about-us/","balimesaritourguide.com/trusted-nanny-babysitter-services-in-sanur-stress-free-childcare-in-bali/","nannyamedbali.com/the-best-nanny-in-sanur-safe-loving-childcare-for-your-bali-holiday/","balinannyhire.com/services_group/meet-app/","balifamilytravels.com/blog/nanny-hire-bali-reputable","babysitting-nanny-service.com/","balinanny-babbyhire.com/pricing/","bali-nanny.com/"],
 "babysitter bali agency":["villa-finder.com/magazine/finding-babysitter-bali/","finnsbeachclub.com/guides/babysitting-services-bali/","balisbestbabysitting.com/","febylousbali.co.id/","babysitterbali.com/","baliangelholiday.com/","babysitterdibali.com/","balichefhire.com/babysitting-service.html","sunshinesmiles.kids/"],
 "things to do in sanur with kids":["tripadvisor.com/Attractions-g297700-Activities-zft11306-Sanur_Denpasar_Bali.html","tothotornot.com/sanur-with-kids/","baliholidaysecrets.com/things-to-do-in-sanur/","baliuntold.com/destinations/sanur/things-to-do/","travelmadmum.com/sanur-kids/","wanderlog.com/list/geoCategory/140306/best-things-to-do-with-kids-in-sanur","blossomsteakhouse.com/things-to-do-in-sanur-with-kids/","thingstodoinsanur.com/sanur-with-kids/","rebeccapiersol.me/2025/05/things-to-do-with-kids-in-sanur.html"],
 "няня бали санур":["baliforum.ru/p/usluga-nyani-nyani-na-bali-gde-nayti-nyanyu-dlya-rebenka","baliforum.ru/p/sanur-bali","make-trip.ru/indonesia/otdykh-sanur","chinatravel.ru/articles/kurort-sanur-bali/","bali-gid.com/dostoprimechatelnosti/pliazhy/sanur/","byvali.ru/indoneziya/bali/plyazhi/sanur","life-in-travels.ru/beach-sanur-bali/","thebalinannies.com/ru","baliopen.ru/sanur-beach/"],
}
for q,pg in [("nanny sanur bali","C01"),("babysitter bali agency","C01"),("няня бали санур","C01")]:
    addq(q,"ru" if re.search("[а-я]",q) else "en","Коммерческий",pg,"S04")
for q in queries:
    if q["lang"]=="id":
        q.update(status="исключено", reason="Сайт EN + RU; индонезийский вне ядра", page="—")
    elif q["lang"]=="ru":
        q.update(status="принято по смыслу", reason="RU-версия той же страницы (/ru/…), hreflang en↔ru")
    elif " denpasar" in q["norm"] and q["intent"]=="Коммерческий":
        q.update(status="исключено", reason="Зона обслуживания — Санур; Денпасар без реального офиса/геостраницы не продвигаем")
    elif q["norm"].endswith(" 2026"):
        q.update(status="исключено", reason="Годовой хвост: покрывается основной фразой страницы, отдельной задачи нет")
    elif q["status"]=="требует проверки" and "cheap" in q["norm"]:
        q.update(status="принято по смыслу", page="C10", reason="Ценовой интент → страница цен; «cheap» не в тексте, покрываем через прозрачные тарифы")
    elif q["status"]=="требует проверки" and q["norm"].startswith("best "):
        q.update(status="принято по смыслу", reason="Подборочный модификатор, та же задача страницы")
    elif q["status"]=="требует проверки" and "sanur" in q["norm"] and q["page"].startswith("A"):
        q.update(status="принято по смыслу", reason="Сужение до Санура совпадает с позиционированием; спрос может быть низким")
qid = {}
for i,q in enumerate(queries,1):
    q["id"]=f"Q{i:05d}"; qid[q["norm"]]=q["id"]
for q in queries:
    if q["norm"] in SERP: q["serp"]="проверено (веб-поиск, US, 25.09.2026)"
    elif q["norm"]=="things to do in sanur with kids": q["serp"]="проверено (веб-поиск, US, 25.09.2026)"
    else: q["serp"]="не проверено"

# ---------------------------------------------------------------- КНИГА
wb = Workbook()
HDR = Font(bold=True, color="FFFFFF"); FILL = PatternFill("solid", fgColor="2E6B5E")
WARN = PatternFill("solid", fgColor="FCE4D6")
def sheet(name, headers, rows, widths=None):
    ws = wb.create_sheet(name)
    ws.append(headers)
    for c in ws[1]: c.font=HDR; c.fill=FILL; c.alignment=Alignment(wrap_text=True, vertical="top")
    for r in rows: ws.append(list(r))
    ws.freeze_panes="A2"; ws.auto_filter.ref=ws.dimensions
    for i,h in enumerate(headers,1):
        w = (widths or {}).get(h, min(60, max(12, len(str(h))+4)))
        ws.column_dimensions[ws.cell(1,i).column_letter].width = w
    for row in ws.iter_rows(min_row=2):
        for c in row: c.alignment=Alignment(wrap_text=True, vertical="top")
    return ws
wb.remove(wb.active)

npages = len(A); acc=[q for q in queries if q["status"]=="принято по смыслу"]; chk=[q for q in queries if q["status"]=="требует проверки"]; exc=[q for q in queries if q["status"]=="исключено"]
serp_ok=[q for q in queries if q["serp"].startswith("проверено")]
by_lang = {l:sum(1 for q in queries if q["lang"]==l) for l in ("en","ru","id")}
sheet("01 Резюме",["Показатель","Значение","Знаменатель","Ограничение","Ближайшее действие"],[
 ("Уникальные кандидаты",len(queries),"—","Сгенерированы по карте маркеров, без выгрузки Keyword Planner/GSC","Прогнать все фразы через Google Keyword Planner (регион: Индонезия/Бали + страны-источники туристов)"),
 ("Принято по смыслу",len(acc),len(queries),"Принятие по смыслу ≠ подтверждённый спрос","Удалить фразы с 0 показов после замера"),
 ("Требует проверки",len(chk),len(queries),"Причины в листе 09","Решить по списку в листе 31"),
 ("Исключено",len(exc),len(queries),"ID, Денпасар, годовые хвосты","Повторно после замера частотности"),
 ("Язык EN / RU / ID",f"{by_lang['en']} / {by_lang['ru']} / {by_lang['id']}","—","Основной рынок Google — англоязычные семьи; RU — второй слой /ru/",""),
 ("Проверенные выдачи Google",len(serp_ok),len(queries),"Веб-поиск из US, не локальная выдача Бали; позиции не для отчёта","Снять SERP по всем принятым через SERP API (гео: Denpasar, mobile)"),
 ("Замеры частотности",0,len(queries),"Keyword Planner / GSC недоступны в сессии; поля пустые, не 0","Заполнить лист 11"),
 ("Информационные статьи",npages,"150","Темы по карте интентов, не по измеренному спросу",""),
 ("Коммерческие страницы",len(COMM),"—","EN + те же страницы в /ru/",""),
 ("Хабы",len(HUBS),"—","",""),
 ("ТЗ-карточки (структура H2, мета, ссылки)",npages,npages,"Объём — ориентир без замера конкурентов; статус «ТЗ подготовлено», не «принято»","Для пилота 15 статей измерить конкурентов и уточнить объём"),
 ("Контент конкурентов проанализирован",0,"—","Не выполнялось","Лист 15 — после SERP-сбора"),
 ("Главное решение","Сайт на EN (Google), хаб-модель «Sanur with Kids» как источник трафика → коммерческие страницы услуг","—","Позиции не гарантируются",""),
])
sheet("02 Паспорт",["Параметр","Значение","Статус","Допущение"],[
 ("Ниша","Агентство нянь и бебиситтеров для семей-туристов и экспатов","дано",""),
 ("Сайт","Новый, домен не выбран","допущение","[domain] в URL"),
 ("Язык","EN (корень) + RU (/ru/), решение заказчика 25.09.2026","дано","Google + международные семьи"),
 ("Регион","Санур (Бали, Индонезия); сопредельно — выезды по Бали","допущение","Реальная зона обслуживания уточнить"),
 ("Поисковая система","Google (все измерения — Keyword Planner, GSC, Google Trends)","дано",""),
 ("Аудитория","B2C: семьи на отдыхе (AU, UK, EU, RU, SG), экспаты с детьми, организаторы свадеб/событий; соискатели","допущение",""),
 ("Целевые действия","Заявка на бронь, WhatsApp-клик, звонок; вакансии — отклик","допущение",""),
 ("Коммерческая ценность","Неизвестно","не дано",""),
 ("Доступные источники","Веб-поиск (Google-подобная выдача, US) — 4 запроса; Keyword Planner/GSC/Ahrefs — нет","факт",""),
 ("Целевой объём","150 статей","дано",""),
 ("CMS","Не выбрана","не дано","Рекомендация: WordPress + Polylang или Next.js/Astro с MDX"),
])
# 03 Структура
rows=[]
for cid,url,h1,kw,sup in COMM: rows.append((cid,url,"/" if cid!="C01" else "","Коммерческая",h1,f"{h1} | [Brand]",f"{h1}. English-speaking, first-aid trained nannies. Book online or via WhatsApp.","новый","1"))
for hid,(n,u,d) in HUBS.items(): rows.append((hid,u,"C23","Хаб",n,f"{n} | [Brand]",d,"новый","1"))
for a in A:
    rows.append((a["id"],f"{HUBS[a['hub']][1]}{a['slug']}/",a["hub"],"Статья",a["h1"],(a["h1"][:55]+" | [Brand]"),f"{a['h1']}: practical tips from a Sanur nanny agency.","новый",""))
sheet("03 Структура",["page_id","URL","parent_page_id","Тип","H1","Title","Description","Существ./новый","Очередь"],rows,{"URL":50,"H1":55,"Title":55,"Description":60})

# 04 План статей + приоритеты
PRIO = {"H01":"1","H02":"1","H04":"2","H03":"2","H06":"2","H05":"3","H07":"3","H08":"2"}
LINK = {"H01":"C01;C10;C11","H02":"C02;C09","H03":"C09","H04":"C13;C05","H05":"C02","H06":"C05;C07","H07":"C07","H08":"C06"}
pilot = {"A001","A003","A004","A006","A026","A027","A031","A032","A056","A057","A071","A091","A110","A121","A136"}
for a in A:
    a["queue"] = "Пилот" if a["id"] in pilot else f"Волна {PRIO[a['hub']]}"
sheet("04 План статей",["page_id","Тема (H1)","Хаб","Аудитория","Этап","Задача","Связанные услуги","Приоритет","Основание","Очередь"],
 [(a["id"],a["h1"],HUBS[a["hub"]][0],a["aud"],a["stage"],f"Ответить на «{a['kw']}»",LINK[a["hub"]],PRIO[a["hub"]],"Близость к услуге и семейный интент Санура; спрос не измерен",a["queue"]) for a in A],{"Тема (H1)":60})
# 05 ТЗ
rows=[]
for a in A:
    qs=[q["id"] for q in queries if q["page"]==a["id"]]
    rows.append((a["id"],a["h1"],a["kw"],"; ".join(qs),f"Раскрыть: {'; '.join(a['h2'])}. Соседние темы — ссылкой в хаб {a['hub']}.",
      "1 200–2 000 слов (ориентир, без замера)","Опыт агентства: реальные случаи, фото с согласия, локальные цены с датой","Инфоблок «Need a nanny while you…» → "+LINK[a["hub"]].split(";")[0],
      "Автор — копирайтер; эксперт — координатор нянь / врач для H04","Факты с датой проверки; цены — из собственных данных; нет выдуманных отзывов","ТЗ подготовлено"))
sheet("05 ТЗ страниц",["page_id","H1","Основной запрос","query_id","Границы","Объём","Собственная польза","CTA","Автор/эксперт","Критерии","Статус"],rows,{"H1":45,"query_id":40,"Границы":70})
# 06 H2
rows=[]
for a in A:
    rows.append((f"{a['id']}-B00",a["id"],"",0,"Intro",f"Answer-first: 2–3 sentences on {a['kw']}","", ""))
    for j,h in enumerate(a["h2"],1): rows.append((f"{a['id']}-B{j:02d}",a["id"],"",j,"H2",h,"",""))
    rows.append((f"{a['id']}-B{len(a['h2'])+1:02d}",a["id"],"",len(a["h2"])+1,"H2","FAQ","Вопросы из «People also ask» после SERP-сбора",""))
    rows.append((f"{a['id']}-B{len(a['h2'])+2:02d}",a["id"],"",len(a["h2"])+2,"CTA","Need a trusted nanny in Sanur?","",LINK[a["hub"]].split(";")[0]))
sheet("06 План H2-H3",["block_id","page_id","parent_block_id","Порядок","Уровень","Заголовок","Тезисы/задача","Ссылка/CTA"],rows,{"Заголовок":55})
# 07
sheet("07 Запросы в тексте",["query_id","query","page_id","Способ покрытия"],[(q["id"],q["norm"],q["page"],"Основной — H1/Title" if any(a["kw"]==q["norm"] for a in A) else "Синоним/раздел, без дословного вхождения") for q in queries if q["page"].startswith("A")])
# 08 перелинковка
rows=[];n=0
for a in A:
    for src,tgt,t in [(a["hub"],a["id"],"хаб→статья"),(a["id"],a["hub"],"статья→хаб")]+[(a["id"],c,"статья→услуга") for c in LINK[a["hub"]].split(";")]:
        n+=1; rows.append((f"L{n:04d}",src,tgt,t,a["h1"] if t=="хаб→статья" else "","план"))
sheet("08 Перелинковка",["link_id","source","target","Тип","Анкор","Статус"],rows)
# 09 Семантика
ws=sheet("09 Семантика",["query_id","Исходная","Нормализованная","Язык","Интент","primary_page_id","Статус","Основание","source_id","SERP","Частотность"],
 [(q["id"],q["raw"],q["norm"],q["lang"],q["intent"],q["page"],q["status"],q["reason"],q["src"],q["serp"],"не измерено") for q in queries],{"Основание":50,"Нормализованная":40})
dv=DataValidation(type="list",formula1='"принято по смыслу,требует проверки,исключено,принято (измерено)"'); ws.add_data_validation(dv); dv.add(f"G2:G{len(queries)+1}")
for r in ws.iter_rows(min_row=2):
    if r[6].value=="требует проверки":
        for c in r: c.fill=WARN
# 10 Кластеры
pages={**{c[0]:c[2] for c in COMM},**{a["id"]:a["h1"] for a in A}}
sheet("10 Кластеры",["cluster_id","page_id","Название","Число фраз","Проверено SERP"],[(f"K-{p}",p,t,sum(1 for q in queries if q["page"]==p),sum(1 for q in queries if q["page"]==p and q["serp"]!="не проверено")) for p,t in pages.items()])
sheet("11 Частотность",["measurement_id","query_id","Строка","Тип","Значение","Регион","Период","Дата","source","Статус"],[(f"M{i:05d}",q["id"],q["norm"],"Keyword Planner avg monthly","", "Indonesia / AU / UK / RU","", "","", "не измерено — нет доступа") for i,q in enumerate(queries,1)])
sheet("12 Сезонность",["Статус"],[("Не измерено. Использовать Google Trends (гео: Indonesia и страны-источники) + Keyword Planner 24 мес. Гипотеза для проверки: пики — июль–август, декабрь–январь, пасхальные каникулы AU.",)])
rows=[];k=0
for q,urls in SERP.items():
    for p,u in enumerate(urls,1): k+=1; rows.append((f"S{k:04d}",qid.get(q,""),q,DATE,"US (веб-поиск)",p,"https://"+u,u.split("/")[0]))
sheet("13 Выдача",["serp_id","query_id","query","Дата","Регион","Позиция","URL","Домен"],rows,{"URL":70})
sheet("14 Анализ запросов",["query","Вывод"],[
 ("nanny sanur bali","Смешанный: агентства, агрегатор greataupair, SEO-статьи турагентств/нянь из других районов (Amed). Нишевой сайт агентства с локальным контентом конкурентоспособен."),
 ("babysitter bali agency","Коммерческий: сайты агентств + подборки (villa-finder, finnsbeachclub). Нужна посадочная услуги + попадание в подборки (лист 24)."),
 ("things to do in sanur with kids","Информационный-подборочный: Tripadvisor, блоги, wanderlog. Формат — длинный гайд с картой и планом по возрасту."),
 ("няня бали санур","RU: форум baliforum и статьи о пляже Санура; одна прямая услуга (thebalinannies.com/ru). Слабая конкуренция — RU-раздел оправдан."),
])
NA="Не выполнено: требуется SERP-сбор и извлечение страниц. Лист сохранён по схеме ТЗ."
for nm in ["15 Контент конкурентов","16 Заголовки конкурентов","17 Вхождения конкурентов","18 Объёмы и рекоменд."]:
    sheet(nm,["Статус"],[(NA,)])
sheet("19 Материалы и факты",["evidence_id","Что нужно","Ответственный","Статус"],[
 ("E01","Собственные цены (час/день/ночь/месяц) с датой","Владелец","запрошено"),("E02","Сертификаты first aid нянь (скан, с разрешения)","Владелец","запрошено"),
 ("E03","Фото нянь с согласием","Владелец","запрошено"),("E04","Реальные отзывы с источником (Google Business Profile)","Владелец","запрошено"),
 ("E05","Список клиник/больниц — проверить адреса и часы","Редактор","проверить"),("E06","Визовые правила и налог для туристов — imigrasi.go.id, lovebali.baliprov.go.id","Редактор","проверить"),
 ("E07","Правовой статус нянь/агентства (NIB, трудовые договоры)","Юрист","запрошено")])
sheet("20 Каннибализация",["Пара","Риск","Решение"],[
 ("A001 how-to-hire vs C01 главная","Главная — коммерция, статья — процесс","Разные интенты, взаимные ссылки"),
 ("A003 nanny cost vs C10 prices","Высокий","A003 — рынок Бали в целом, C10 — только ваши тарифы; canonical не нужен"),
 ("A147 salary vs A003","Средний","A147 — месячная зарплата для экспатов, A003 — туристические ставки"),
 ("A026 things to do vs A049 3-day itinerary","Средний","Итинерарий — готовый маршрут, гайд — каталог"),
 ("A006 night nanny vs C04","Высокий","Статья — объяснение, услуга — бронь; при слабом росте объединить")])
sheet("21 AI Overviews",["Замечание"],[("Адаптация раздела «Алиса AI» под Google: отслеживать AI Overviews / AI Mode по ключевым запросам вручную или через SERP API; упоминания не гарантируются, специальной разметки для попадания нет.",),("Структура: ответ в первых 2–3 предложениях, таблицы цен, чёткие определения — полезно читателю и для извлечения.",)])
sheet("22 Техника и CMS",["req_id","Требование","Проверка","Приоритет"],[
 ("T01","HTTPS, 301 с www/без www","curl -I","1"),("T02","hreflang en/ru/x-default парами, canonical на себя, <html lang>","Просмотр кода, GSC","1"),
 ("T03","XML sitemap с разделением по языкам, robots.txt","GSC","1"),("T04","Schema: LocalBusiness/ChildCare, Organization, Article, BreadcrumbList, FAQPage только при реальном FAQ","Rich Results Test","2"),
 ("T05","Core Web Vitals мобильные: LCP<2.5s, INP<200ms, CLS<0.1","PageSpeed Insights","1"),("T06","Кнопка WhatsApp + форма, цели GA4","GA4 DebugView","1"),
 ("T07","Автор/эксперт, даты публикации и обновления (E-E-A-T; тема детей — чувствительная)","Ручная","1"),("T08","Хлебные крошки, оглавление, related posts","Ручная","2"),
 ("T09","SSR/статическая генерация контента","Просмотр кода, URL Inspection","1")])
sheet("23 Миграция URL",["Статус"],[("Неприменимо — новый сайт",)])
sheet("24 Локальное и внешнее",["Действие/площадка","Основание","Статус"],[
 ("Google Business Profile (категория Babysitter / Child care agency) с реальным адресом в Сануре","Локальная выдача и карты по «nanny sanur»","к выполнению"),
 ("Отзывы в GBP от реальных клиентов","Ранжирование в Maps","к выполнению"),
 ("villa-finder.com/magazine/finding-babysitter-bali/","Подборка в топе «babysitter bali agency»","кандидат — предложить включение"),
 ("finnsbeachclub.com/guides/babysitting-services-bali/","Подборка в топе","кандидат"),
 ("Отели и виллы Санура — партнёрство (QR в номере)","Прямые лиды + ссылки","кандидат"),
 ("baliforum.ru, RU Telegram-чаты «Бали с детьми»","RU-аудитория","кандидат"),
 ("Facebook-группы Sanur/Bali Expat Parents","Экспаты","кандидат"),
 ("Свадебные организаторы Бали","Event babysitting","кандидат")])
sheet("25 Производство",["page_id","Очередь","Статус"],[(a["id"],a["queue"],"ТЗ подготовлено") for a in A])
sheet("27 Мониторинг",["Что","Где","Когда"],[("Индексация, показы, клики, CTR, позиции по page","Google Search Console","30/60/90 дней"),("Заявки/WhatsApp-клики","GA4","еженедельно"),("Позиции GBP","Local rank tracker","ежемесячно")])
sheet("28 Источники",["source_id","Источник","Дата","Ограничения"],[
 ("S01","Карта маркеров коммерческих запросов (генерация по матрице)",DATE,"Не частотный источник; требует замера"),("S02","Экспертный список RU-запросов",DATE,"Не частотный источник"),
 ("S03","Карта интентов статей",DATE,"Не частотный источник"),("S04","Веб-поиск (4 запроса), выдача US",DATE,"Не локальная выдача Бали; позиции нельзя считать измерением ранжирования")])
sheet("31 Исключения и резерв",["query_id","query","Статус","Причина / проверка"],[(q["id"],q["norm"],q["status"],q["reason"]) for q in chk+exc])
sheet("32 Приёмка",["Проверка","Результат"],[
 ("Баланс кандидатов",f"{len(acc)}+{len(chk)}+{len(exc)}={len(queries)} — "+("сходится" if len(acc)+len(chk)+len(exc)==len(queries) else "НЕ сходится")),("150 уникальных page_id в плане и ТЗ",f"{len(set(a['id'] for a in A))} — да"),
 ("Все query_id → существующий page_id","да" if all(q['page'] in pages for q in queries if q['status']!='исключено') else "НЕТ"),
 ("Частотность измерена","НЕТ — 0 из "+str(len(queries))),("Выдача проверена",f"НЕТ — {len(serp_ok)} из {len(queries)}"),
 ("Итог","Частичный результат: структура, ядро-кандидат, 150 ТЗ-карточек. Не является завершённым исследованием по разделу 18 шаблона.")])
sheet("33 Методика",["Пункт","Описание"],[
 ("Адаптация под Google","Wordstat→Keyword Planner/Trends; Вебмастер→Search Console; Метрика→GA4; Яндекс Бизнес→Google Business Profile; Алиса→AI Overviews; операторы ! [] \"\" не применимы — у Keyword Planner нет операторов, использовать exact match в Ads search terms"),
 ("Нормализация","нижний регистр, схлопывание пробелов, без стемминга"),
 ("Кластеризация","ручная по задаче; после SERP-сбора — пересечение ≥3 URL в топ-10 (порог — настройка)"),
 ("Язык","EN в корне, RU в /ru/ с теми же slug; hreflang en/ru/x-default")])

out = r"D:\Няня\SEO-nanny-agency-Sanur-Google-2026-09-25.xlsx"
wb.save(out); print(out, len(queries), len(acc), len(chk), len(A))
