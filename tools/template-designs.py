"""Industry-specific compositions. Loaded by gen-templates.py with its shared data/helpers."""
PHOTOS = {
 'dental': ('photo-1629909613654-28e377c37b09', 'Bright, welcoming dental treatment room'),
 'salon': ('photo-1562322140-8baeececf3df', 'Stylist blow-drying a client’s hair in a bright salon'),
 'cafe': ('photo-1501339847302-ac426a4a7cbb', 'Sunlit café with warm wood and welcoming tables'),
 'coffee': ('photo-1495474472287-4d71bcdd2085', 'Freshly brewed coffee and a slow morning'),
 'auto': ('photo-1486262715619-67b85e0b08d3', 'Close-up of a vehicle engine during maintenance'),
 'fitness': ('photo-1534438327276-14e5300c3a48', 'Strength training equipment in a gym'),
 'pet': ('photo-1552053831-71594a27632d', 'Friendly golden retriever enjoying the outdoors'),
 'cat': ('photo-1573865526739-10659fec78a5', 'Curious cat looking toward the camera'),
}

def photo(key, cls='', eager=False):
    pid, alt = PHOTOS[key]
    return f'<img class="{cls}" src="https://images.unsplash.com/{pid}?auto=format&amp;fit=crop&amp;w=1600&amp;q=85" alt="{alt}" width="1600" height="1200" {"fetchpriority=high" if eager else "loading=lazy"} />'

def action(d, text=None, href='#book', secondary=False):
    return f'<a class="button {"secondary" if secondary else ""}" href="{href}">{e(text or d["book_label"])} <span aria-hidden="true">↗</span></a>'

def heading(kicker, title, body=''):
    return f'<div class="section-heading"><p class="eyebrow">{kicker}</p><h2>{title}</h2>{f"<p>{body}</p>" if body else ""}</div>'

def services(d, title, mode='cards', kicker='Care, with clarity'):
    rows = ''.join(f'<li><span class="service-number">0{i+1}</span><div><h3>{e(n)}</h3><p>{e(note)}</p></div><strong>{e(p)}</strong><a href="#book" aria-label="Choose {e(n)}">↗</a></li>' for i,(n,p,note) in enumerate(d['services']))
    return f'<section id="services" class="section services {mode}">{heading(kicker,title)}<ul class="service-list">{rows}</ul></section>'

def about(d, title=None):
    cards = ''.join(f'<article><span class="index">0{i+1}</span><h3>{e(t)}</h3><p>{e(b)}</p></article>' for i,(t,b) in enumerate(d['about']))
    return f'<section id="about" class="section about">{heading("A little more human",title or e(d["about_title"]))}<div class="principles">{cards}</div></section>'

def reviews(d):
    return '<section class="section reviews" aria-label="Sample customer reviews">' + ''.join(f'<figure><span class="eyebrow">Kind words · sample review</span><blockquote>“{e(q)}”</blockquote><figcaption>— {e(n)}</figcaption></figure>' for n,q in d['reviews']) + '</section>'

def booking(d, title, intro):
    return f'<section id="book" class="section booking"><div>{heading("Let’s make it a date",title,intro)}<p class="booking-phone">Prefer a conversation?<br /><a href="tel:{d["phone_tel"]}">{e(d["phone"])}</a></p></div><div class="form-panel">{form(d,"button",note_class="form-note",label_class="form-label")}</div></section>'

def location(d):
    hours=''.join(f'<div><dt>{e(day)}</dt><dd>{e(time)}</dd></div>' for day,time in d['hours'])
    return f'<section id="location" class="section location"><div>{heading("In the neighborhood",e(d["city"]))}<address>{e(d["address"])}<br /><span>{e(d["landmark"])}</span></address><dl class="hours">{hours}</dl><div class="contact-links"><a href="{maps_link(d)}">Get directions ↗</a><a href="https://{d["messenger"]}">Messenger ↗</a><a href="{viber(d)}">Viber ↗</a></div></div>{map_iframe(d,"location-map")}</section>'

def faq(d):
    rows=''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in d['faqs'])
    return f'<section id="faq" class="section faq">{heading("Good to know","Before you visit.")}<div>{rows}</div></section>'

def shell(d, style, content, nav):
    fonts='family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&family=DM+Serif+Display:ital@0;1&family=Barlow+Condensed:wght@500;600;700;800&family=Space+Mono:wght@400;700'
    links=''.join(f'<a href="#{anchor}">{label}</a>' for anchor,label in nav)
    brands={'dental':'<span class="brand-symbol">✳</span> marikina<span>smile.</span>', 'salon':'bea’s<span class="brand-sub">SALON & NAIL BAR</span>', 'cafe':'kapé lola<span class="brand-sub">YOUR NEIGHBORHOOD CAFÉ</span>', 'auto':'DIEGO’S<span class="brand-sub">AUTO CARE / CALOOCAN</span>', 'fitness':'LAKAS<span class="brand-sub">STRENGTH STUDIO</span>', 'pet':'<span class="brand-symbol">✳</span> paws & co.'}
    return head(d,fonts,'').replace('</head>', '<link rel="stylesheet" href="/assets/templates/industries.css" /></head>') + f'''
<body class="industry {style}"><a class="skip-link" href="#main">Skip to content</a>
<div class="demo-strip"><span>FICTIONAL DEMO · {e(d['industry'])}</span><a href="/services/templates/">All templates ↗</a></div>
<header class="site-header"><a class="wordmark" href="#main" aria-label="{e(d['name'])}">{brands[style]}</a><nav aria-label="Main navigation">{links}</nav>{action(d)}<button class="menu-toggle" aria-label="Open navigation" aria-expanded="false" aria-controls="mobile-menu">☰</button></header>
<nav id="mobile-menu" class="mobile-menu" aria-label="Mobile navigation" hidden>{links}<a href="#book">{e(d['book_label'])}</a></nav>
<main id="main">{content}</main><footer class="site-footer"><div><p class="footer-name">{e(d['name'])}</p><p>{e(d['hero_kicker'])}</p></div><div>{footer_credit(d,'')}<p>Fictional business · Sample prices & reviews · Photography: Unsplash</p><a href="/services/#pricing">Make this your business website ↗</a></div></footer>
<div class="mobile-actions"><a href="tel:{d['phone_tel']}">Call us</a>{action(d)}</div>
<script>
const toggle=document.querySelector('.menu-toggle'),menu=document.querySelector('.mobile-menu');
toggle.addEventListener('click',()=>{{const open=toggle.getAttribute('aria-expanded')==='true';toggle.setAttribute('aria-expanded',String(!open));menu.hidden=open;toggle.setAttribute('aria-label',open?'Open navigation':'Close navigation');}});
menu.addEventListener('click',ev=>{{if(ev.target.closest('a')){{menu.hidden=true;toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','Open navigation');}}}});
document.addEventListener('keydown',ev=>{{if(ev.key==='Escape'&&!menu.hidden){{menu.hidden=true;toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','Open navigation');toggle.focus();}}}});
document.querySelectorAll('[data-service]').forEach(a=>a.addEventListener('click',()=>{{document.querySelector('[name=service]').value=a.dataset.service;}}));
const date=document.querySelector('[name=date]'); const today=new Date();date.min=[today.getFullYear(),String(today.getMonth()+1).padStart(2,'0'),String(today.getDate()).padStart(2,'0')].join('-');
</script>''' + SCRIPT

def dental(d, view="landing"):
    """Four-page monochrome editorial site. Every page shares the header, drawer navigation, and footer."""
    base='/services/templates/dental-clinic/'
    route=lambda key: base if key=='landing' else base+key+'/'
    book=route('contact')+'#book'
    portrait = '<img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&amp;fit=crop&amp;w=1600&amp;q=85" alt="Woman smiling confidently" width="1600" height="1200" fetchpriority="high" />'
    smile = '<img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&amp;fit=crop&amp;w=1400&amp;q=85" alt="Portrait of a smiling woman" width="1400" height="1200" loading="lazy" />'
    room = photo('dental')
    def book_link(service, text): return f'<a href="{book}" data-service="{e(service)}">{text}</a>'
    detail={'Consultation & check-up':'Exam, digital X-ray if needed, and a written treatment plan with prices. Free on your first visit.',
            'Oral prophylaxis (cleaning)':'Ultrasonic scaling and polishing. Gentle on sensitive gums; we numb if you ask.',
            'Tooth-colored filling':'Composite resin matched to your shade. Done in one sitting, chew on it the same day.',
            'Tooth extraction':'Simple and surgical extractions, including wisdom teeth, with aftercare instructions you can keep.',
            'Teeth whitening':'In-clinic LED whitening, two to four shades brighter in one visit. Take-home trays available.',
            'Metal braces':'Full orthodontic treatment with monthly adjustments. Installment: ₱10,000 down, then monthly.'}
    def prices(tag='h2', full=False):
        rows=''.join(f'<li><span>0{i+1}</span><div><h3>{e(n)}</h3>{f"<p>{e(detail[n])}</p>" if full else ""}<small>{e(note)}</small></div><strong>{e(p)}</strong>{book_link(d["booking_options"][i],"Book <span aria-hidden=\"true\">↗</span>")}</li>' for i,(n,p,note) in enumerate(d['services']))
        intro='Every treatment, what it involves, how long it takes, and what it costs. No surprise add-ons on the chair.' if full else 'Every price is on the page before treatment starts. HMO accepted for consultation and cleaning.'
        return f'<section class="d-prices{" full" if full else ""}" aria-labelledby="prices-title"><div class="d-prices-heading"><{tag} id="prices-title">Care &amp;<br />prices</{tag}><p>{intro}</p>{action(d,"See all services",route("services")) if not full else ""}</div><ul>{rows}</ul></section>'
    # Landing: hero stage, then the commercial substance the demo promises: prices, reviews, hours and location.
    panels = ''.join(f'<div class="care-row"><button class="care-trigger" aria-expanded="false" aria-controls="care-{i}" id="care-button-{i}"><span>0{i+1}</span>{e(title)}<span class="care-toggle" aria-hidden="true">+</span></button><div id="care-{i}" class="care-answer" role="region" aria-labelledby="care-button-{i}" hidden><p>{e(copy)}</p></div></div>' for i,(title,copy) in enumerate(d['about']))
    hero=f'<section class="d-care-stage" aria-label="Welcome to {e(d["name"])}"><div class="d-portrait">{portrait}</div><div class="d-care-rows">{panels}</div><p class="d-intro">{e(d["tagline"])}</p><div class="d-hero-title"><p>{e(d["hero_kicker"])} · {e(d["city"])}</p><h1>Dental<br />Care</h1></div><div class="d-hero-cta"><h2>We believe in the power<br />of your smile.</h2><p>Free consultation on your first visit</p>{action(d,"Book Online",book)}</div></section>'
    quotes=''.join(f'<figure><blockquote>“{e(q)}”</blockquote><figcaption>{e(n)} · sample review</figcaption></figure>' for n,q in d['reviews'])
    hours=''.join(f'<div><dt>{e(day)}</dt><dd>{e(time)}</dd></div>' for day,time in d['hours'])
    visit=f'<section class="d-visit" aria-label="Visit the clinic"><div class="d-visit-photo">{room}</div><div class="d-visit-hours"><h2>Open six<br />days a week</h2><dl>{hours}</dl></div><div class="d-visit-where"><h2>Find us</h2><address>{e(d["address"])}<br /><span>{e(d["landmark"])}</span></address><p><a href="{maps_link(d)}">Get directions ↗</a><a href="tel:{d["phone_tel"]}">{e(d["phone"])} ↗</a></p></div></section>'
    landing=hero+prices()+f'<section class="d-reviews" aria-label="Sample patient reviews">{quotes}</section>'+visit
    # Services: smile gallery stage, implant feature, and the full price list.
    treatments=[('Dental<br />Veneers','Whitening'),('Dental<br />Crowns','Filling'),('Teeth<br />Whitening','Whitening')]
    tiles=''.join(f'<a href="{book}" data-service="{svc}"><h3>{label}</h3><span>0{i+1} ↗</span></a>' for i,(label,svc) in enumerate(treatments))
    gallery=f'<section id="smile" class="d-smile-stage"><div class="d-smile-photo">{smile}</div><div class="d-smile-label"><h3>Smile Gallery</h3><p>Explore cosmetic dental care</p></div><div class="d-smile-title"><h1>Smile<br />makeover</h1></div><div class="d-smile-note"><p>Let’s find the right treatment<br />for the smile you have in mind.</p>{action(d,"Call Us","tel:"+d["phone_tel"])}</div><div class="d-treatment-links">{tiles}</div></section>'
    implant=f'<section class="d-implant"><div><h2>Implant<br />Dentistry</h2><p>Restore missing teeth with a fixed, natural-looking replacement. Dr. Reyes plans every case with a 3D scan, so you know the steps and the cost before anything starts.</p>{action(d,"Book a consultation",book)}</div><div class="d-implant-photo">{room}</div><div class="d-implant-bottom"><span>Single tooth<br />replacement</span><span>Full smile<br />restoration</span><span>Installment<br />plans available</span></div></section>'
    services_page=gallery+prices('h2',full=True)+implant
    # FAQs
    questions=''.join(f'<details><summary><span>0{i+1}</span>{e(q)}<b aria-hidden="true">+</b></summary><p>{e(a)}</p></details>' for i,(q,a) in enumerate(d['faqs']))
    faq_page=f'<section class="d-faq-page"><div class="d-faq-heading"><h1>Frequently<br />Asked<br />Questions</h1><p>Everything you need to feel at ease before your first visit.</p>{action(d,"Contact Us",route("contact"))}</div><div class="d-questions">{questions}</div></section>'
    # Contact: booking form, then where, how to reach us, hours, and the map.
    contact=f'<section class="d-contact-photo">{portrait}<h1>Let’s see<br />that smile.</h1></section><section class="d-book" id="book"><h2>Book Online</h2><p>Pick a service and a time. We confirm by text within the day.</p>{form(d,"button",note_class="form-note",label_class="form-label")}</section><section class="d-contact-info"><div><h2>Find Us</h2><address>{e(d["address"])}<br /><span>{e(d["landmark"])}</span></address><a href="{maps_link(d)}">Get directions ↗</a></div><div><h2>Reach Us</h2><p><a href="tel:{d["phone_tel"]}">{e(d["phone"])}</a></p><p><a href="https://{d["messenger"]}">Messenger ↗</a></p><p><a href="{viber(d)}">Viber ↗</a></p></div><div><h2>Opening Hours</h2><dl>{hours}</dl></div>{map_iframe(d,"d-map")}</section>'
    content={'landing':landing,'services':services_page,'faqs':faq_page,'contact':contact}[view]
    links=''.join(f'<a href="{route(key)}"'+(' aria-current="page"' if key==view else '')+f'><span>0{i+1}</span>{label}<span>↗</span></a>' for i,(key,label) in enumerate([('landing','Landing'),('services','Services'),('faqs','FAQs'),('contact','Contact')]))
    page=head(d,'family=Manrope:wght@400;500;600;700;800','').replace('</head>','<link rel="stylesheet" href="/assets/templates/industries.css" /><link rel="stylesheet" href="/assets/templates/dental.css" /></head>').replace(f'<meta name="theme-color" content="{d["accent"]}" />','<meta name="theme-color" content="#111111" />')
    page+=f'''<body class="industry dental d-pages" data-page="{view}"><a class="skip-link" href="#main">Skip to content</a><div class="demo-strip"><span>FICTIONAL DEMO · {e(d["industry"])}</span><a href="/services/templates/">All templates ↗</a></div><header class="site-header"><a class="wordmark" href="{base}" aria-label="{e(d["name"])} home"><span class="d-logo">MARIKINA<br />SMILE<span>{e(d["hero_kicker"])}</span></span></a><button class="menu-toggle" aria-label="Open navigation" aria-expanded="false" aria-controls="d-navigation">Menu</button><a class="d-header-call" href="tel:{d["phone_tel"]}">Dental emergency? Call {e(d["phone"])}</a></header><nav id="d-navigation" class="d-navigation" aria-label="Main navigation" hidden>{links}<a class="d-nav-book" href="{book}">{e(d["book_label"])} ↗</a></nav><main id="main" tabindex="-1">{content}</main><footer class="d-footer"><nav aria-label="Footer navigation">{links}</nav><p>{e(d["name"])} is a fictional clinic demo · Photography: Unsplash</p><a href="/services/templates/">All templates ↗</a></footer><div class="d-mobile-actions"><a href="tel:{d["phone_tel"]}">Call us</a><a href="{book}">{e(d["book_label"])}</a></div><script src="/assets/templates/dental.js" defer></script></body></html>'''
    return page


def salon(d):
    hero=f'''<section class="salon-hero"><div class="salon-title"><p class="eyebrow">Kamuning, Quezon City · Hair / Nails / Lashes</p><h1>A little change.<br /><em>A whole new you.</em></h1></div><div class="salon-image">{photo('salon',eager=True)}<span class="vertical-caption">GOOD HAIR. GOOD ENERGY. ALWAYS YOU.</span></div><div class="salon-intro"><span class="salon-stamp">Your chair<br /><em>is waiting.</em></span><p>Fresh color. A perfect cut. That just-done feeling. Make a little room for yourself at Bea’s.</p>{action(d)}</div></section><div class="salon-ribbon">HAIR THAT MOVES WITH YOU <span>✳</span> NAILS THAT MAKE YOUR DAY <span>✳</span> A LITTLE EVERYDAY LUXURY</div>'''
    return shell(d,'salon',hero+services(d,'The beauty<br /><em>of a little ritual.</em>','editorial','The service edit / 01')+reviews(d)+about(d,'Come as you are.<br /><em>Leave feeling like you.</em>')+booking(d,'Let’s make<br /><em>some time for you.</em>','Tell us what you have in mind. Add your preferred stylist in the notes and we’ll find your chair.')+location(d)+faq(d),[('services','The service edit'),('about','The salon'),('book','Your appointment')])

def cafe(d):
    hero=f'''<section class="cafe-hero">{photo('cafe','cafe-backdrop',True)}<div class="cafe-overlay"><p class="eyebrow">Kapitolyo, Pasig · Come on in</p><h1>Good mornings.<br /><em>Long conversations.</em></h1><p>Filipino comfort food. Benguet coffee.<br />A little corner of the neighborhood to call your own.</p>{action(d,'Find your table')}<div class="cafe-hours">BREAKFAST ALL DAY <span>☀</span> COFFEE FROM 7 AM</div></div></section><section class="cafe-welcome section"><p class="eyebrow">Tuloy po kayo.</p><h2>Like Lola’s kitchen.<br /><em>With really good coffee.</em></h2><p>House-cured tapa, a second cup, and no reason to rush. Drop in for breakfast, stay through lunch, or gather your favorite people upstairs.</p></section>'''
    story=f'<section id="about" class="cafe-story">{photo("coffee")}<div>{heading("From the highlands to your cup","Locally grown.<br /><em>Lovingly brewed.</em>","Single-origin Benguet beans, brewed with care. Pair your cup with an all-day Filipino breakfast. Some things are simply better together.")}{action(d,"See what’s cooking","#services")}</div></section>'
    return shell(d,'cafe',hero+services(d,'A few house favorites.','menu','Fresh from our kitchen')+story+booking(d,'Pull up<br /><em>a chair.</em>','A table for two or the whole second floor for twenty. There’s room for your kind of gathering.')+reviews(d)+location(d)+faq(d),[('services','Our menu'),('about','Our coffee'),('location','Drop by')])

def auto(d):
    hero=f'''<section class="auto-hero"><div class="auto-copy"><p class="eyebrow">CALOOCAN’S NEIGHBORHOOD WORKSHOP</p><h1>LESS GUESSWORK.<br /><span>MORE GO.</span></h1><p>Know what’s wrong. Know what it costs.<br />Get back on the road with confidence.</p>{action(d,'Book your bay')}<div class="auto-spec"><span>01 / INSPECT</span><span>02 / APPROVE</span><span>03 / REPAIR</span></div></div>{photo('auto','auto-photo',True)}<div class="auto-photo-label">DIEGO’S AUTO CARE <span>PRECISION. WITHOUT THE PRETENSE.</span></div></section><div class="make-strip"><span>WE KNOW YOUR DRIVE</span><strong>TOYOTA</strong><strong>MITSUBISHI</strong><strong>HONDA</strong><strong>SUZUKI</strong></div>'''
    return shell(d,'auto',hero+about(d,'NO SURPRISES.<br />JUST SOLUTIONS.')+services(d,'THE WORK.<br /><span>THE PRICE.</span>','workshop','Workshop service board')+booking(d,'LET’S GET<br />IT SORTED.','Choose your service. Add your vehicle’s make, model, year, and symptoms in the notes so we can prepare your bay.')+reviews(d)+faq(d)+location(d),[('services','Services + prices'),('about','The process'),('location','The shop')])

def fitness(d):
    hero=f'''<section class="fitness-hero">{photo('fitness','fitness-backdrop',True)}<div class="fitness-title"><p class="eyebrow">SMALL GROUPS. REAL COACHING. POBLACION.</p><h1>FIND<br />YOUR<br /><span>STRONG.</span></h1></div><div class="fitness-hero-side"><span class="giant-eight">08</span><p>PEOPLE MAX.<br />NO HIDING IN THE BACK.</p>{action(d,'Claim your first class')}</div></section><div class="fitness-marquee">SHOW UP. <span>GET STRONGER.</span> REPEAT. <span>SHOW UP.</span></div>'''
    sched=''.join(f'<li><span>0{i+1}</span><h3>{e(o)}</h3><span>Small group · coached</span><a href="#book" data-service="{e(o)}">Book ↗</a></li>' for i,o in enumerate(d['booking_options'][:5]))
    schedule=f'<section id="schedule" class="section schedule">{heading("Your next hour, well spent","MAKE TIME.<br />MAKE PROGRESS.","Sample weekday class lineup. Choose a preferred date when you book; availability is confirmed by the studio.")}<ul>{sched}</ul></section>'
    return shell(d,'fitness',hero+schedule+services(d,'COMMIT TO YOU.<br />NOT A CONTRACT.','memberships','Train on your terms')+about(d,'LESS CROWD.<br />MORE COACHING.')+reviews(d)+booking(d,'YOUR DAY ONE.<br />STARTS HERE.','New to lifting? Choose a movement assessment. Already training? Pick your class and bring your energy.')+location(d)+faq(d),[('schedule','The schedule'),('services','Memberships'),('about','Our way')])

def pet(d):
    hero=f'''<section class="pet-hero section"><div class="hero-copy"><p class="eyebrow">Big hearts for little paws · BF Homes</p><h1>Their happy place.<br /><em>Yours, too.</em></h1><p>From first vaccines to fresh haircuts, a friendly neighborhood team for every chapter of their life.</p>{action(d)}<p class="pet-note">Dogs, cats & the people who love them. ♡</p></div><div class="pet-portraits"><div class="dog-portrait">{photo('pet',eager=True)}</div><div class="cat-portrait">{photo('cat')}</div><span class="pet-sticker">More tail wags.<br />Less worry.</span><span class="pet-spark" aria-hidden="true">✳</span></div></section>'''
    paths=f'<section class="pet-paths section" aria-label="Find the right care"><a href="#services"><span>✚</span><h2>Feeling under<br />the weather?</h2><p>Check-ups & veterinary care ↗</p></a><a href="#services"><span>✂</span><h2>Time for a<br />little pampering?</h2><p>Baths, trims & grooming ↗</p></a><a href="#book"><span>♡</span><h2>A new member<br />of the family?</h2><p>Start their care journey ↗</p></a></section>'
    return shell(d,'pet',hero+paths+about(d,'Good care.<br /><em>From nose to tail.</em>')+services(d,'A little care goes<br />a long way.','pet-services','Healthy pets, happy people')+booking(d,'Let’s meet your<br /><em>best friend.</em>','Pick vet care or grooming, then tell us your pet’s name, species, and age in the notes.')+reviews(d)+faq(d)+location(d),[('services','Care & grooming'),('about','Why paws & co.'),('location','Come say hello')])
