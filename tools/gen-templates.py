#!/usr/bin/env python3
"""Generate the LocalBiz Digital Hub demo sites under services/templates/.

One entry in INDUSTRIES per demo; one render function per design. Edit the
data (prices, copy, hours) or a design, then:

    python3 tools/gen-templates.py
    npx tailwindcss@3 -c tailwind.config.js -i tailwind.source.css -o assets/tailwind.css --minify

The pages are noindex on purpose: the businesses are fictional. The cards on
/services/ and /services/templates/ are hand-written and link here by slug.
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def e(s):
    return html.escape(s, quote=True)

INDUSTRIES = [
  dict(
    slug="dental-clinic", industry="Dental clinic", name="Marikina Smile Dental",
    tagline="Gentle dentistry for the whole family, five minutes from Riverbanks.",
    accent="#0f766e", accent_dark="#115e59", tint="#f0fdfa",
    city="Marikina City", address="Unit 2F, 118 J.P. Rizal St., Sta. Elena, Marikina City",
    phone="0917 555 0142", phone_tel="+639175550142", messenger="m.me/marikinasmile", viber="09175550142",
    map_q="J.P. Rizal St, Santa Elena, Marikina, Metro Manila",
    hero_kicker="Family & cosmetic dentistry",
    hero_body="Cleanings, fillings, braces, and whitening in a clinic that runs on time. Walk-ins welcome; booked patients are seen first.",
    book_label="Book a visit", verb="visit",
    about_title="Why patients stay with us",
    about=[("On-time appointments","Your slot is your slot. We book with gaps so you are not waiting an hour past your time."),
           ("Prices before treatment","You see the cost on this page and on the chair before anything starts. No surprise add-ons."),
           ("Same dentist every time","Dr. Reyes and Dr. Tan see their own patients, so nobody re-explains their history.")],
    services=[("Consultation & check-up","₱500","20 min"),("Oral prophylaxis (cleaning)","₱1,200","45 min"),("Tooth-colored filling","from ₱1,500","per tooth"),
              ("Tooth extraction","from ₱1,500","per tooth"),("Teeth whitening","₱8,000","90 min"),("Metal braces","from ₱35,000","installment available")],
    booking_options=["Consultation & check-up","Cleaning","Filling","Extraction","Whitening","Braces consultation"],
    hours=[("Monday – Friday","9:00 AM – 6:00 PM"),("Saturday","9:00 AM – 4:00 PM"),("Sunday","Closed")],
    reviews=[("Ana L.","Booked online at 10pm, got a confirmation text in the morning. Cleaning was done by 11. Wala nang hintay."),
             ("Marco D.","First clinic where they told me the price of the filling before sitting me down. Coming back for braces.")],
    faqs=[("Do you accept HMO?","Yes — Maxicare, Intellicare, and PhilCare for consultation and cleaning. Bring your card and a valid ID."),
          ("Can I bring my kids?","Yes. Dr. Tan handles pediatric patients and we have a Saturday morning block for families."),
          ("Do you offer installment for braces?","Yes. A ₱10,000 down payment, then monthly during adjustment visits.")],
    landmark="Above Mercury Drug, across from Marikina Sports Center",
  ),
  dict(
    slug="salon", industry="Salon & nails", name="Bea’s Salon & Nail Bar",
    tagline="Hair, nails, and lashes in Kamuning. Book a chair, skip the wait.",
    accent="#be185d", accent_dark="#9d174d", tint="#fdf2f8",
    city="Quezon City", address="45 K-1st St., Kamuning, Quezon City",
    phone="0920 555 0177", phone_tel="+639205550177", messenger="m.me/beassalonqc", viber="09205550177",
    map_q="K-1st St, Kamuning, Quezon City, Metro Manila",
    hero_kicker="Hair · Nails · Lashes",
    hero_body="Six chairs, four nail stations, and stylists who have been here for years. Pick your service and your time, and your chair is ready when you walk in.",
    book_label="Book a chair", verb="appointment",
    about_title="Why regulars keep coming back",
    about=[("Your stylist, every time","Book with the same person. Ate Bea, Jen, and Rico each have their own regulars."),
           ("Real prices, posted","Rebond, color, and nail prices are on this page. What you see here is what you pay at the counter."),
           ("Open till 8pm","Come after work. Last booking is 7:00 PM on weekdays.")],
    services=[("Haircut & blow-dry","₱350","45 min"),("Hair color (full)","from ₱1,800","2 hr"),("Brazilian blowout","from ₱2,500","2–3 hr"),
              ("Rebond","from ₱3,000","3–4 hr"),("Gel manicure & pedicure","₱750","75 min"),("Classic lash extensions","₱1,200","90 min")],
    booking_options=["Haircut & blow-dry","Hair color","Brazilian blowout","Rebond","Gel mani-pedi","Lash extensions"],
    hours=[("Monday – Saturday","10:00 AM – 8:00 PM"),("Sunday","10:00 AM – 6:00 PM"),("Holidays","Check Facebook for hours")],
    reviews=[("Trisha M.","Booked Jen for color through the site, walked in at 2, walked out at 4. No waiting on the bench for once."),
             ("Karla P.","The gel mani lasted three weeks. Prices are exactly what the website says.")],
    faqs=[("Can I request a specific stylist?","Yes — pick them in the booking form. If they are full that day, we will message you with the next slot."),
          ("Do you take walk-ins?","Yes, but booked clients go first. On Saturdays the wait can be an hour."),
          ("Do you do home service?","For bridal and events only. Message us for a quote.")],
    landmark="Beside 7-Eleven, two doors from Kamuning Bakery",
  ),
  dict(
    slug="cafe", industry="Café & restaurant", name="Kapé Lola",
    tagline="Filipino breakfast, specialty coffee, and a quiet second floor in Kapitolyo.",
    accent="#92400e", accent_dark="#78350f", tint="#fffbeb",
    city="Pasig City", address="21 East Capitol Dr., Kapitolyo, Pasig City",
    phone="0915 555 0163", phone_tel="+639155550163", messenger="m.me/kapelola", viber="09155550163",
    map_q="East Capitol Drive, Kapitolyo, Pasig, Metro Manila",
    hero_kicker="Café · Breakfast all day · Events",
    hero_body="Tapsilog with house-cured tapa, single-origin Benguet beans, and a second floor you can reserve for a meeting or a birthday of twenty.",
    book_label="Reserve a table", verb="reservation",
    about_title="What we do differently",
    about=[("Menu with prices online","Every dish and its price is on this page. No more asking in the comments 'HM po?'"),
           ("Reservations that stick","Reserve a table or the whole second floor online. You get a confirmation, we get a heads-up."),
           ("Open at 7","Breakfast crowd, then laptops, then dinner. Kitchen closes 9:30 PM.")],
    services=[("Tapsilog (house-cured tapa)","₱285","all day"),("Longganisa Lucban silog","₱245","all day"),("Pancit Lola (for sharing)","₱480","serves 3–4"),
              ("Flat white / latte","₱160","hot or iced"),("Pour-over, Benguet single origin","₱190","12 oz"),("Second-floor private use","₱3,000 consumable","up to 20 pax")],
    booking_options=["Table for 2","Table for 4","Table for 6+","Second floor (event)","Catering inquiry"],
    hours=[("Monday – Thursday","7:00 AM – 9:30 PM"),("Friday – Saturday","7:00 AM – 11:00 PM"),("Sunday","7:00 AM – 9:00 PM")],
    reviews=[("Gio R.","Reserved the second floor for my mom's 60th through the site. Booking took a minute, and they called to confirm the menu."),
             ("Mae S.","Quiet enough to work on a Tuesday, coffee is actually good, and the prices are posted so no awkward moments.")],
    faqs=[("Do you take reservations for large groups?","Yes — up to 20 on the second floor. Use the form and pick 'Second floor (event)'."),
          ("Is there parking?","Street parking on East Capitol Dr. and a pay lot behind the building."),
          ("Do you deliver?","Through GrabFood and foodpanda. For bulk breakfast orders, message us a day before.")],
    landmark="Ground floor of the yellow building, across from the barangay hall",
  ),
  dict(
    slug="auto-repair", industry="Auto repair shop", name="Diego’s Auto Care",
    tagline="Honest diagnostics, clear quotes, and a text when your car is ready.",
    accent="#1d4ed8", accent_dark="#1e40af", tint="#eff6ff",
    city="Caloocan City", address="1187 A. Mabini St., Grace Park, Caloocan City",
    phone="0918 555 0129", phone_tel="+639185550129", messenger="m.me/diegosautocare", viber="09185550129",
    map_q="A. Mabini St, Grace Park, Caloocan, Metro Manila",
    hero_kicker="PMS · Brakes · Aircon · Diagnostics",
    hero_body="Preventive maintenance, brakes, aircon, and electrical for Toyota, Mitsubishi, Honda, and Suzuki. Quote before we touch it, photo of the old parts when we're done.",
    book_label="Book a service", verb="service slot",
    about_title="How the shop works",
    about=[("Quote first, always","You approve the price on Messenger or by text before any work starts. No 'nadagdagan po'."),
           ("Photos of what we replaced","Old parts, new parts, side by side, sent to your phone. You know exactly what you paid for."),
           ("Book a bay, not a queue","Pick a morning or afternoon slot online. Your bay is held; you're not fifth in line.")],
    services=[("PMS (oil, filter, 21-point check)","from ₱1,800","1.5 hr"),("Brake pads (front pair)","from ₱2,500","2 hr"),("Aircon cleaning & recharge","from ₱2,000","2 hr"),
              ("Computer diagnostics","₱800","free with repair"),("Battery replacement","from ₱4,500","30 min"),("Wheel alignment","₱1,200","45 min")],
    booking_options=["PMS / oil change","Brakes","Aircon","Diagnostics (check engine light)","Battery","Alignment","Other — describe below"],
    hours=[("Monday – Saturday","8:00 AM – 6:00 PM"),("Sunday","Closed"),("Emergency","Call — we'll tell you honestly if we can take it")],
    reviews=[("Ronnie A.","Sent me the quote on Messenger, I said go, and got a photo of the worn pads an hour later. That's it, that's the review."),
             ("Liza C.","Booked a Saturday morning slot online. Car was ready by lunch. Price matched the website.")],
    faqs=[("What brands do you service?","Toyota, Mitsubishi, Honda, Suzuki, Nissan, and Hyundai. For others, message us with the model first."),
          ("Do you use original parts?","Your choice — we quote both OEM and quality replacement, and tell you the difference."),
          ("Can I wait for my car?","Yes for PMS and aircon. For bigger jobs we'll text you when it's ready.")],
    landmark="Beside Petron, before the Grace Park LRT footbridge",
  ),
  dict(
    slug="fitness-studio", industry="Gym & fitness studio", name="Lakas Strength Studio",
    tagline="Small-group strength coaching in Poblacion. Eight people per class, never more.",
    accent="#ea580c", accent_dark="#c2410c", tint="#fff7ed",
    city="Makati City", address="3F, 5044 P. Burgos St., Poblacion, Makati City",
    phone="0916 555 0188", phone_tel="+639165550188", messenger="m.me/lakasstudio", viber="09165550188",
    map_q="P. Burgos St, Poblacion, Makati, Metro Manila",
    hero_kicker="Strength · Mobility · Small groups",
    hero_body="Coached barbell and kettlebell classes capped at eight. Book your class online, see who's coaching, and cancel up to two hours before without losing the credit.",
    book_label="Book a class", verb="class",
    about_title="Why members stay",
    about=[("Eight per class, always","You get coached every set. Nobody waits for a rack."),
           ("Class schedule online","See this week's classes and coaches on this page, book in one tap, done."),
           ("No lock-in memberships","Class packs or monthly. Pause anytime. It's on the pricing table below.")],
    services=[("Drop-in class","₱600","60 min"),("10-class pack","₱4,500","valid 60 days"),("Unlimited monthly","₱6,500","month to month"),
              ("1-on-1 coaching","₱1,500","60 min"),("Movement assessment","₱1,000","first-timers"),("Corporate / team session","from ₱8,000","up to 12 pax")],
    booking_options=["6:00 AM Strength","7:00 AM Strength","12:15 PM Express","6:00 PM Strength","7:15 PM Kettlebell","Movement assessment (first visit)"],
    hours=[("Monday – Friday","6:00 AM – 9:00 PM"),("Saturday","7:00 AM – 1:00 PM"),("Sunday","Closed")],
    reviews=[("Paolo V.","Booked my first assessment from the site on a Sunday night, got a reply Monday 7am. Six months in."),
             ("Dana K.","I like that the schedule and prices are just on the website. I didn't have to DM anyone to find out.")],
    faqs=[("I've never lifted before. Is this for me?","Yes. Every new member starts with a movement assessment, then joins the 6 PM beginner-friendly block."),
          ("Can I freeze my membership?","Yes — up to 30 days a year, no questions, message us."),
          ("Do you have showers?","Two showers and lockers. Bring your own towel or rent one for ₱50.")],
    landmark="Third floor above the Korean grocery, entrance on the side street",
  ),
  dict(
    slug="pet-clinic", industry="Vet & pet grooming", name="Paws & Co. Vet Clinic",
    tagline="Vaccines, check-ups, and grooming in BF Homes. Book online, no phone tag.",
    accent="#4d7c0f", accent_dark="#3f6212", tint="#f7fee7",
    city="Parañaque City", address="12 Aguirre Ave., BF Homes, Parañaque City",
    phone="0919 555 0154", phone_tel="+639195550154", messenger="m.me/pawsandcovet", viber="09195550154",
    map_q="Aguirre Ave, BF Homes, Parañaque, Metro Manila",
    hero_kicker="Veterinary · Grooming · Vaccines",
    hero_body="Two vets, one groomer, and a waiting room with separate corners for cats and dogs. Pick vet or grooming, pick a time, and we text you a reminder the day before.",
    book_label="Book for your pet", verb="appointment",
    about_title="Why pet owners choose us",
    about=[("Reminders that actually come","Vaccine due? We text you. Appointment tomorrow? We text you. You don't have to remember."),
           ("Prices on the page","Consultation, vaccines, grooming — all priced here. Bring the number, that's the number."),
           ("Grooming with a vet next door","If the groomer spots a skin issue or a tick problem, a vet is ten steps away.")],
    services=[("Consultation","₱500","20 min"),("5-in-1 vaccine (dog)","₱800","incl. consult"),("4-in-1 vaccine (cat)","₱900","incl. consult"),
              ("Full grooming (small dog)","from ₱600","2 hr"),("Full grooming (large dog)","from ₱1,200","3 hr"),("Spay / neuter","from ₱3,500","by appointment")],
    booking_options=["Vet consultation","Vaccination","Grooming — small dog","Grooming — large dog","Grooming — cat","Spay / neuter consult"],
    hours=[("Monday – Saturday","9:00 AM – 7:00 PM"),("Sunday","10:00 AM – 4:00 PM"),("After hours","Call — we'll refer you to a 24-hour clinic if we can't take it")],
    reviews=[("Jenny T.","Booked grooming for two dogs online, got a text reminder the day before, and picked them up smelling great. Price as posted."),
             ("Carlo B.","Our cat's vaccine schedule is texted to us every time. We never miss one anymore.")],
    faqs=[("Do you handle emergencies?","During clinic hours, yes — call first so we can prepare. After hours we refer to a 24-hour partner clinic."),
          ("Can I stay with my pet during grooming?","Yes, there's a viewing window. Most pets are calmer when you're out of sight, though."),
          ("Do you board pets?","Not yet. We can recommend a nearby boarding facility we trust.")],
    landmark="Across from the BF Homes Aguirre gate, beside the bakery",
  ),
]

MARK = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" fill="currentColor" class="h-full w-auto" aria-hidden="true"><path d="M147.22,124.99l.2,22.96-67.4.05-.3-38.21c-5.07,20.91-20.84,36.39-42.43,38-8.19.61-16.08.05-24.72.14l.47-91.57c.12-23.5,19.87-43.14,43.16-43.97,16.52-.59,31.84-.62,48.27.03,23.3.91,41.54,20.86,42.74,43.68.44,8.32.15,15.7.14,24.03l-38.03.34c21.38,4.78,37.72,22.19,37.91,44.54ZM93.69,100.97c4.42-.69,7.11-4.16,6.97-8.38l.05-33.99-33.37.2c-4.77-.18-7.94,3.21-8.36,7.83l.03,34.22,34.68.12Z"/></svg>'

# ---------- shared pieces ----------
def head(d, fonts, css, dark=False):
    url = f"https://rmbergonia.com/services/templates/{d['slug']}/"
    title = f"{d['name']} — {d['industry']} website template"
    desc = f"Demo of the LocalBiz Digital Hub for a {d['industry'].lower()}: services and prices, online booking, click-to-call, hours and map. ₱35,000 one-time, live in 5–7 days."
    return f'''<!doctype html>
<html lang="en" class="scroll-smooth">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{e(title)}</title>
    <meta name="description" content="{e(desc)}" />
    <meta name="author" content="Ruther Bergonia" />
    <!-- Demo of a fictional business: kept out of search on purpose. -->
    <meta name="robots" content="noindex, nofollow" />
    <link rel="canonical" href="{url}" />
    <meta property="og:type" content="website" />
    <meta property="og:title" content="{e(title)}" />
    <meta property="og:description" content="{e(desc)}" />
    <meta name="theme-color" content="{d['accent']}" />
    <link rel="icon" href="/assets/rmb-mark.svg" type="image/svg+xml" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="/assets/tailwind.css" />
    <style>
      :root {{ --brand: {d['accent']}; --brand-dark: {d['accent_dark']}; }}
      html {{ -webkit-font-smoothing: antialiased; }}
      [id] {{ scroll-margin-top: 110px; }}
      a:focus-visible, button:focus-visible, summary:focus-visible {{ outline: 2px solid var(--brand); outline-offset: 3px; }}
      @media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} * {{ transition-duration: .01ms !important; }} }}
{css}
    </style>
  </head>
'''

def demo_bar(d, dark=False):
    bg = "bg-white text-stone-900 border-b border-white/10" if dark else "bg-stone-900 text-white"
    muted = "text-stone-500" if dark else "text-stone-400"
    return f'''    <div class="fixed inset-x-0 top-0 z-50 {bg}">
      <div class="flex flex-wrap items-center justify-between gap-x-6 gap-y-1 px-5 py-2 text-[12px] sm:px-8">
        <p class="flex items-center gap-2 font-medium"><span class="block h-4 w-auto">{MARK}</span><span><span class="hidden sm:inline">Demo &middot; </span>LocalBiz Digital Hub &middot; {e(d['industry'])} &middot; <span class="{muted}">{e(d['name'])} is fictional</span></span></p>
        <p class="flex items-center gap-4 font-semibold"><a href="/services/templates/" class="{muted} underline-offset-4 hover:underline">All templates</a><a href="/services/#pricing" class="underline underline-offset-4">Get this for your business &mdash; &#8369;35,000 &rarr;</a></p>
      </div>
    </div>
'''

def form(d, btn_class, note_class="text-stone-400", done_class="", label_class="text-[12px] font-semibold uppercase tracking-[0.12em]", extra=""):
    opts = "\n".join(f'                <option>{e(o)}</option>' for o in d['booking_options'])
    return f'''          <form id="bookingForm" class="{extra}" novalidate>
            <div class="grid gap-x-8 gap-y-7 sm:grid-cols-2">
              <label class="block {label_class}">Your name<input type="text" name="name" required autocomplete="name" class="field" placeholder="Juan dela Cruz" /></label>
              <label class="block {label_class}">Mobile number<input type="tel" name="phone" required autocomplete="tel" inputmode="tel" class="field" placeholder="0917 000 0000" /></label>
              <label class="block {label_class} sm:col-span-2">Service<select name="service" required class="field">
{opts}
              </select></label>
              <label class="block {label_class}">Preferred date<input type="date" name="date" required class="field" /></label>
              <label class="block {label_class}">Preferred time<select name="time" required class="field"><option>Morning (9–12)</option><option>Afternoon (1–5)</option><option>Evening (after 5)</option></select></label>
              <label class="block {label_class} sm:col-span-2">Notes <span class="font-normal normal-case tracking-normal opacity-60">(optional)</span><textarea name="notes" rows="2" class="field" placeholder="First visit, allergies, plate number, pet's name…"></textarea></label>
            </div>
            <button type="submit" class="{btn_class}">Send {e(d['verb'])} request</button>
            <p class="mt-4 text-[12.5px] {note_class}">Demo &mdash; nothing is sent. On a live site this lands in the owner&rsquo;s email and phone instantly.</p>
            <p id="bookingDone" class="mt-5 hidden text-[15px] font-semibold {done_class}" role="status" aria-live="polite">Request received &mdash; on a live site the owner has it now and you&rsquo;d get a text back within the hour.</p>
          </form>'''

def map_iframe(d, cls):
    q = e(d['map_q']).replace(' ', '+')
    return f'<iframe title="Map to {e(d["name"])}" src="https://www.google.com/maps?q={q}&output=embed" class="{cls}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>'

def maps_link(d): return "https://www.google.com/maps/search/?api=1&query=" + e(d['map_q']).replace(' ', '+')
def viber(d): return f"viber://chat?number=%2B{d['phone_tel'][1:]}"

SCRIPT = '''    <script>
      // Demo only: pretend to submit. A live site posts to the owner's inbox.
      (function () {
        var f = document.getElementById("bookingForm"), done = document.getElementById("bookingDone");
        if (!f) return;
        f.addEventListener("submit", function (ev) {
          ev.preventDefault();
          if (!f.reportValidity()) return;
          done.classList.remove("hidden");
          f.querySelector("button[type=submit]").disabled = true;
          done.scrollIntoView({ behavior: "smooth", block: "nearest" });
        });
      })();
    </script>
  </body>
</html>
'''

def mobile_bar(d, call_cls, book_cls, bg="bg-white/95 border-stone-200"):
    return f'''    <div class="fixed inset-x-0 bottom-0 z-40 grid grid-cols-2 gap-2 border-t {bg} p-3 backdrop-blur-md md:hidden">
      <a href="tel:{d['phone_tel']}" class="{call_cls}">Call</a>
      <a href="#book" class="{book_cls}">{e(d['book_label'])}</a>
    </div>
    <div class="h-16 md:hidden" aria-hidden="true"></div>
'''

def footer_credit(d, cls):
    return f'<p class="{cls}">Demo site by <a href="/" class="underline underline-offset-4">Ruther Bergonia</a> &middot; <a href="/services/" class="underline underline-offset-4">LocalBiz Digital Hub</a></p>'

# ============================================================
# 1. DENTAL — clinical calm: white, hairlines, Inter, huge airy type
# ============================================================
def dental(d):
    css = '''      body { background: #fff; color: #0f172a; font-family: Inter, "Helvetica Neue", Arial, sans-serif; }
      .hair { border-color: #e7e5e4; }
      .field { display:block; width:100%; border:0; border-bottom:1px solid #d6d3d1; background:transparent; padding:.7rem 0; font-size:17px; color:#0f172a; border-radius:0; }
      .field:focus { outline:none; border-bottom-color: var(--brand); }
      .brand { color: var(--brand); }
      .btn { display:inline-flex; align-items:center; justify-content:center; gap:.6rem; padding:1rem 1.75rem; font-size:14px; font-weight:600; letter-spacing:.02em; transition: background .2s, color .2s; }
      .btn-solid { background: var(--brand); color:#fff; } .btn-solid:hover { background: var(--brand-dark); }
      .btn-line { border:1px solid #0f172a; color:#0f172a; } .btn-line:hover { background:#0f172a; color:#fff; }
    '''
    services = "\n".join(f'''          <li class="grid gap-2 border-t hair py-7 md:grid-cols-12 md:items-baseline">
            <p class="text-[13px] text-stone-400 md:col-span-2">{i+1:02d}</p>
            <p class="text-[22px] font-medium tracking-tight md:col-span-6">{e(n)}</p>
            <p class="text-[14px] text-stone-500 md:col-span-2">{e(note)}</p>
            <p class="text-[22px] font-medium tabular-nums md:col-span-2 md:text-right">{e(p)}</p>
          </li>''' for i,(n,p,note) in enumerate(d['services']))
    about = "\n".join(f'''          <div class="border-t hair pt-8"><p class="text-[13px] text-stone-400">0{i+1}</p><h3 class="mt-4 text-[24px] font-medium tracking-tight">{e(t)}</h3><p class="mt-4 text-[16px] leading-relaxed text-stone-500">{e(b)}</p></div>''' for i,(t,b) in enumerate(d['about']))
    hours = "\n".join(f'<li class="flex justify-between border-t hair py-4"><span class="text-stone-500">{e(a)}</span><span class="font-medium">{e(b)}</span></li>' for a,b in d['hours'])
    faqs = "\n".join(f'''          <details class="group border-t hair py-6"><summary class="flex cursor-pointer items-baseline justify-between gap-8 text-[20px] font-medium tracking-tight">{e(q)}<span class="brand text-2xl transition-transform group-open:rotate-45" aria-hidden="true">+</span></summary><p class="mt-4 max-w-2xl text-[16px] leading-relaxed text-stone-500">{e(a)}</p></details>''' for q,a in d['faqs'])
    reviews = "\n".join(f'<figure class="border-t hair pt-8"><blockquote class="text-[22px] font-light leading-snug tracking-tight">&ldquo;{e(q)}&rdquo;</blockquote><figcaption class="mt-6 text-[13px] text-stone-400">{e(w)} &middot; Google review (sample)</figcaption></figure>' for w,q in d['reviews'])
    return head(d, "family=Inter:wght@300;400;500;600", css) + f'''  <body>
{demo_bar(d)}
    <header class="fixed inset-x-0 top-[34px] z-40 border-b hair bg-white/90 backdrop-blur-md">
      <div class="flex items-center justify-between px-5 py-4 sm:px-8">
        <a href="#main" class="text-[15px] font-semibold tracking-tight">{e(d['name'])}</a>
        <nav class="hidden gap-8 text-[14px] text-stone-500 md:flex"><a href="#services" class="hover:text-stone-900">Treatments</a><a href="#about" class="hover:text-stone-900">Clinic</a><a href="#location" class="hover:text-stone-900">Visit</a><a href="#faq" class="hover:text-stone-900">FAQ</a></nav>
        <div class="flex items-center gap-6"><a href="tel:{d['phone_tel']}" class="hidden text-[14px] font-medium sm:block">{e(d['phone'])}</a><a href="#book" class="btn btn-solid !py-2.5 !px-5">{e(d['book_label'])}</a></div>
      </div>
    </header>

    <main id="main" class="pt-[92px]">
      <section class="px-5 pb-24 pt-24 sm:px-8 md:pb-40 md:pt-40">
        <p class="brand text-[13px] font-semibold uppercase tracking-[0.18em]">{e(d['hero_kicker'])}</p>
        <h1 class="mt-8 max-w-[14ch] text-[clamp(2.8rem,8.5vw,8.5rem)] font-light leading-[0.98] tracking-[-0.03em]">{e(d['tagline'])}</h1>
        <div class="mt-16 grid gap-10 md:grid-cols-12">
          <p class="max-w-md text-[18px] leading-relaxed text-stone-500 md:col-span-5">{e(d['hero_body'])}</p>
          <div class="flex flex-wrap gap-3 md:col-span-7 md:justify-end md:self-end"><a href="#book" class="btn btn-solid">{e(d['book_label'])}</a><a href="tel:{d['phone_tel']}" class="btn btn-line">Call {e(d['phone'])}</a></div>
        </div>
      </section>

      <section class="grid border-y hair md:grid-cols-3">
        <div class="border-b hair p-8 md:border-b-0 md:border-r"><p class="text-[12px] uppercase tracking-[0.16em] text-stone-400">Hours</p><p class="mt-3 text-[18px] font-medium">{e(d['hours'][0][0])}<br />{e(d['hours'][0][1])}</p></div>
        <div class="border-b hair p-8 md:border-b-0 md:border-r"><p class="text-[12px] uppercase tracking-[0.16em] text-stone-400">Location</p><p class="mt-3 text-[18px] font-medium">{e(d['address'])}</p></div>
        <div class="p-8"><p class="text-[12px] uppercase tracking-[0.16em] text-stone-400">Reach us</p><p class="mt-3 flex flex-wrap gap-x-6 text-[18px] font-medium"><a href="tel:{d['phone_tel']}" class="hover:underline">Call</a><a href="{viber(d)}" class="hover:underline">Viber</a><a href="https://{d['messenger']}" rel="noopener" class="hover:underline">Messenger</a></p></div>
      </section>

      <section id="services" class="px-5 py-24 sm:px-8 md:py-40">
        <div class="grid gap-10 md:grid-cols-12"><p class="brand text-[13px] font-semibold uppercase tracking-[0.18em] md:col-span-3">Treatments &amp; prices</p><h2 class="text-[clamp(2rem,4.5vw,4rem)] font-light leading-[1.02] tracking-[-0.03em] md:col-span-9">What you pay is what&rsquo;s written here.</h2></div>
        <ul class="mt-20 border-b hair">
{services}
        </ul>
      </section>

      <section id="about" class="bg-stone-50 px-5 py-24 sm:px-8 md:py-40">
        <h2 class="max-w-3xl text-[clamp(2rem,4.5vw,4rem)] font-light leading-[1.02] tracking-[-0.03em]">{e(d['about_title'])}</h2>
        <div class="mt-20 grid gap-12 md:grid-cols-3">
{about}
        </div>
      </section>

      <section id="book" class="px-5 py-24 sm:px-8 md:py-40">
        <div class="grid gap-16 md:grid-cols-12">
          <div class="md:col-span-5"><p class="brand text-[13px] font-semibold uppercase tracking-[0.18em]">Online booking</p><h2 class="mt-6 text-[clamp(2rem,4.5vw,4rem)] font-light leading-[1.02] tracking-[-0.03em]">{e(d['book_label'])}.</h2><p class="mt-8 max-w-md text-[17px] leading-relaxed text-stone-500">Pick a treatment and a time. Your request reaches us the moment you send it; we confirm by text within the hour.</p></div>
          <div class="md:col-span-7">
{form(d, "btn btn-solid mt-12 w-full sm:w-auto", done_class="brand", label_class="text-[12px] font-medium uppercase tracking-[0.14em] text-stone-400")}
          </div>
        </div>
      </section>

      <section id="reviews" class="bg-stone-50 px-5 py-24 sm:px-8 md:py-40">
        <p class="brand text-[13px] font-semibold uppercase tracking-[0.18em]">Patients</p>
        <div class="mt-12 grid gap-12 md:grid-cols-2">
{reviews}
        </div>
      </section>

      <section id="location" class="grid md:grid-cols-2">
        <div class="px-5 py-24 sm:px-8 md:py-40">
          <p class="brand text-[13px] font-semibold uppercase tracking-[0.18em]">Visit</p>
          <h2 class="mt-6 text-[clamp(2rem,4.5vw,4rem)] font-light leading-[1.02] tracking-[-0.03em]">{e(d['city'])}</h2>
          <address class="mt-8 not-italic text-[17px] leading-relaxed text-stone-500">{e(d['address'])}<br />{e(d['landmark'])}</address>
          <ul class="mt-10 border-b hair text-[16px]">
{hours}
          </ul>
          <div class="mt-10 flex flex-wrap gap-3"><a href="tel:{d['phone_tel']}" class="btn btn-solid">Call {e(d['phone'])}</a><a href="{maps_link(d)}" rel="noopener" class="btn btn-line">Directions</a></div>
        </div>
        {map_iframe(d, "h-[380px] w-full md:h-full md:min-h-[600px]")}
      </section>

      <section id="faq" class="px-5 py-24 sm:px-8 md:py-40">
        <div class="grid gap-10 md:grid-cols-12"><p class="brand text-[13px] font-semibold uppercase tracking-[0.18em] md:col-span-3">Questions</p><div class="md:col-span-9">
{faqs}
        </div></div>
      </section>
    </main>

    <footer class="border-t hair px-5 py-10 sm:px-8">
      <div class="flex flex-wrap items-center justify-between gap-6 text-[13px] text-stone-500"><p><span class="font-semibold text-stone-900">{e(d['name'])}</span> &middot; {e(d['address'])}</p>{footer_credit(d, "")}</div>
    </footer>
{mobile_bar(d, "btn btn-line !py-3", "btn btn-solid !py-3")}
''' + SCRIPT

# ============================================================
# 2. SALON — editorial: cream, serif italic display, dotted-leader menu
# ============================================================
def salon(d):
    css = '''      body { background: #f4efe6; color: #17130f; font-family: Inter, "Helvetica Neue", sans-serif; }
      .serif { font-family: "Cormorant Garamond", Georgia, serif; }
      .hair { border-color: #17130f; }
      .field { display:block; width:100%; border:0; border-bottom:1px solid rgba(244,239,230,.4); background:transparent; padding:.7rem 0; font-size:17px; color:#f4efe6; border-radius:0; }
      .field::placeholder { color: rgba(244,239,230,.4); } .field option { color:#17130f; }
      .field:focus { outline:none; border-bottom-color:#f4efe6; }
      .leader { display:flex; align-items:baseline; gap:.75rem; } .leader::after { content:""; order:2; flex:1; border-bottom:1px dotted rgba(23,19,15,.4); transform: translateY(-.35em); } .leader > :last-child { order:3; }
      .btn { display:inline-flex; align-items:center; justify-content:center; padding:1rem 2rem; font-size:13px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; transition: all .2s; }
      .btn-ink { background:#17130f; color:#f4efe6; } .btn-ink:hover { background: var(--brand); }
      .btn-line { border:1px solid #17130f; color:#17130f; } .btn-line:hover { background:#17130f; color:#f4efe6; }
      .btn-cream { background:#f4efe6; color:#17130f; } .btn-cream:hover { background: var(--brand); color:#fff; }
    '''
    services = "\n".join(f'<li class="leader py-4 text-[19px]"><span>{e(n)} <span class="text-[13px] text-stone-500">{e(note)}</span></span><span class="tabular-nums">{e(p)}</span></li>' for n,p,note in d['services'])
    about = "\n".join(f'<div><p class="serif text-[64px] italic leading-none text-stone-400">{i+1}</p><h3 class="serif mt-4 text-[32px] leading-tight">{e(t)}</h3><p class="mt-4 text-[16px] leading-relaxed text-stone-600">{e(b)}</p></div>' for i,(t,b) in enumerate(d['about']))
    hours = "\n".join(f'<li class="leader py-3 text-[16px]"><span>{e(a)}</span><span>{e(b)}</span></li>' for a,b in d['hours'])
    faqs = "\n".join(f'<details class="group border-t hair py-6"><summary class="serif flex cursor-pointer items-baseline justify-between gap-8 text-[28px] leading-tight">{e(q)}<span class="text-2xl transition-transform group-open:rotate-45" aria-hidden="true">+</span></summary><p class="mt-4 max-w-2xl text-[16px] leading-relaxed text-stone-600">{e(a)}</p></details>' for q,a in d['faqs'])
    reviews = "\n".join(f'<figure><blockquote class="serif text-[clamp(1.6rem,3vw,2.4rem)] italic leading-tight">&ldquo;{e(q)}&rdquo;</blockquote><figcaption class="mt-6 text-[12px] uppercase tracking-[0.16em] text-stone-500">{e(w)} &middot; sample review</figcaption></figure>' for w,q in d['reviews'])
    return head(d, "family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Inter:wght@400;500;600", css) + f'''  <body>
{demo_bar(d)}
    <header class="fixed inset-x-0 top-[34px] z-40 border-b hair bg-[#f4efe6]/90 backdrop-blur-md">
      <div class="flex items-center justify-between px-5 py-4 sm:px-8">
        <a href="#main" class="serif text-[22px] italic">{e(d['name'])}</a>
        <nav class="hidden gap-8 text-[12px] uppercase tracking-[0.16em] md:flex"><a href="#services">Menu</a><a href="#about">Salon</a><a href="#location">Visit</a><a href="#faq">FAQ</a></nav>
        <a href="#book" class="btn btn-ink !py-2.5 !px-5">{e(d['book_label'])}</a>
      </div>
    </header>

    <main id="main" class="pt-[92px]">
      <section class="px-5 pb-20 pt-20 sm:px-8 md:pb-32 md:pt-32">
        <p class="text-[12px] uppercase tracking-[0.2em] text-stone-500">{e(d['hero_kicker'])} &middot; {e(d['city'])}</p>
        <h1 class="serif mt-10 text-[clamp(3.5rem,13vw,13rem)] leading-[0.85] tracking-[-0.02em]">{e(d['name'].split(' ')[0])}<br /><span class="italic font-normal">{e(' '.join(d['name'].split(' ')[1:]))}</span></h1>
        <div class="mt-16 grid gap-10 border-t hair pt-10 md:grid-cols-12">
          <p class="serif text-[clamp(1.5rem,2.8vw,2.4rem)] leading-tight md:col-span-7">{e(d['tagline'])}</p>
          <div class="md:col-span-5 md:pl-10"><p class="text-[16px] leading-relaxed text-stone-600">{e(d['hero_body'])}</p><div class="mt-8 flex flex-wrap gap-3"><a href="#book" class="btn btn-ink">{e(d['book_label'])}</a><a href="tel:{d['phone_tel']}" class="btn btn-line">Call</a></div></div>
        </div>
      </section>

      <section id="services" class="border-t hair px-5 py-20 sm:px-8 md:py-32">
        <div class="grid gap-12 md:grid-cols-12">
          <div class="md:col-span-4"><p class="text-[12px] uppercase tracking-[0.2em] text-stone-500">Menu</p><h2 class="serif mt-6 text-[clamp(2.5rem,5vw,5rem)] leading-none">Services<br /><span class="italic">&amp; prices</span></h2><p class="mt-8 max-w-xs text-[15px] leading-relaxed text-stone-600">What you see here is what you pay at the counter. &ldquo;From&rdquo; means we check your hair first and quote before starting.</p></div>
          <ul class="md:col-span-8 md:pt-4">
{services}
          </ul>
        </div>
      </section>

      <section id="about" class="border-t hair px-5 py-20 sm:px-8 md:py-32">
        <h2 class="serif max-w-3xl text-[clamp(2.5rem,5vw,5rem)] leading-none">{e(d['about_title'])}</h2>
        <div class="mt-20 grid gap-14 md:grid-cols-3">
{about}
        </div>
      </section>

      <section id="book" class="bg-[#17130f] px-5 py-20 text-[#f4efe6] sm:px-8 md:py-32">
        <div class="grid gap-16 md:grid-cols-12">
          <div class="md:col-span-5"><p class="text-[12px] uppercase tracking-[0.2em] text-stone-400">Reservations</p><h2 class="serif mt-6 text-[clamp(2.5rem,5vw,5rem)] leading-none">Book<br /><span class="italic">a chair.</span></h2><p class="mt-8 max-w-sm text-[16px] leading-relaxed text-stone-400">Pick your service, your stylist, and your time. Confirmation by text, usually within the hour.</p></div>
          <div class="md:col-span-7">
{form(d, "btn btn-cream mt-12 w-full sm:w-auto", note_class="text-stone-500", done_class="text-[#f4efe6]", label_class="text-[11px] font-medium uppercase tracking-[0.16em] text-stone-400")}
          </div>
        </div>
      </section>

      <section id="reviews" class="border-t hair px-5 py-20 sm:px-8 md:py-32">
        <div class="grid gap-16 md:grid-cols-2">
{reviews}
        </div>
      </section>

      <section id="location" class="grid border-t hair md:grid-cols-2">
        <div class="px-5 py-20 sm:px-8 md:py-32">
          <p class="text-[12px] uppercase tracking-[0.2em] text-stone-500">Visit</p>
          <h2 class="serif mt-6 text-[clamp(2.5rem,5vw,5rem)] leading-none">{e(d['city'])}</h2>
          <address class="mt-8 not-italic text-[16px] leading-relaxed text-stone-600">{e(d['address'])}<br />{e(d['landmark'])}</address>
          <ul class="mt-10">
{hours}
          </ul>
          <div class="mt-10 flex flex-wrap gap-3"><a href="tel:{d['phone_tel']}" class="btn btn-ink">Call</a><a href="{viber(d)}" class="btn btn-line">Viber</a><a href="https://{d['messenger']}" rel="noopener" class="btn btn-line">Messenger</a><a href="{maps_link(d)}" rel="noopener" class="btn btn-line">Directions</a></div>
        </div>
        <div class="border-t hair md:border-l md:border-t-0">{map_iframe(d, "h-[380px] w-full grayscale md:h-full md:min-h-[600px]")}</div>
      </section>

      <section id="faq" class="border-t hair px-5 py-20 sm:px-8 md:py-32">
        <div class="grid gap-10 md:grid-cols-12"><p class="text-[12px] uppercase tracking-[0.2em] text-stone-500 md:col-span-3">Questions</p><div class="md:col-span-9">
{faqs}
        </div></div>
      </section>
    </main>

    <footer class="border-t hair px-5 py-10 sm:px-8">
      <div class="flex flex-wrap items-center justify-between gap-6 text-[13px] text-stone-600"><p class="serif text-[20px] italic text-[#17130f]">{e(d['name'])}</p>{footer_credit(d, "")}</div>
    </footer>
{mobile_bar(d, "btn btn-line !py-3", "btn btn-ink !py-3", "bg-[#f4efe6]/95 border-[#17130f]")}
''' + SCRIPT

# ============================================================
# 3. CAFÉ — warm: Fraunces, big stacked words, full-bleed bands
# ============================================================
def cafe(d):
    css = '''      body { background: #f7f1e7; color: #2a1d12; font-family: Inter, "Helvetica Neue", sans-serif; }
      .disp { font-family: Fraunces, Georgia, serif; font-variation-settings: "SOFT" 100, "WONK" 1; font-weight: 500; letter-spacing: -0.02em; }
      .band { background: var(--brand); color: #fbf5ea; }
      .field { display:block; width:100%; border:1px solid #d9cbb8; background:#fff; padding:.9rem 1rem; font-size:16px; color:#2a1d12; border-radius:1rem; }
      .field:focus { outline:none; border-color: var(--brand); }
      .btn { display:inline-flex; align-items:center; justify-content:center; padding:1rem 1.9rem; font-size:15px; font-weight:600; border-radius:9999px; transition: all .2s; }
      .btn-brand { background: var(--brand); color:#fff; } .btn-brand:hover { background: var(--brand-dark); }
      .btn-line { border:1.5px solid #2a1d12; color:#2a1d12; } .btn-line:hover { background:#2a1d12; color:#f7f1e7; }
      .btn-cream { background:#fbf5ea; color:#2a1d12; } .btn-cream:hover { background:#fff; }
    '''
    menu = "\n".join(f'<li class="flex flex-col justify-between rounded-3xl bg-white/70 p-8"><div><p class="disp text-[26px] leading-tight">{e(n)}</p><p class="mt-2 text-[14px] text-stone-500">{e(note)}</p></div><p class="disp mt-8 text-[30px]">{e(p)}</p></li>' for n,p,note in d['services'])
    about = "\n".join(f'<div class="border-t border-[#2a1d12]/20 pt-8"><h3 class="disp text-[30px] leading-tight">{e(t)}</h3><p class="mt-4 text-[16px] leading-relaxed text-stone-600">{e(b)}</p></div>' for t,b in d['about'])
    hours = "".join(f'<div><p class="text-[12px] uppercase tracking-[0.16em] opacity-70">{e(a)}</p><p class="disp mt-2 text-[28px]">{e(b)}</p></div>' for a,b in d['hours'])
    faqs = "\n".join(f'<details class="group border-t border-[#2a1d12]/20 py-6"><summary class="disp flex cursor-pointer items-baseline justify-between gap-8 text-[26px] leading-tight">{e(q)}<span class="text-2xl transition-transform group-open:rotate-45" aria-hidden="true">+</span></summary><p class="mt-4 max-w-2xl text-[16px] leading-relaxed text-stone-600">{e(a)}</p></details>' for q,a in d['faqs'])
    reviews = "\n".join(f'<figure class="rounded-3xl bg-white/70 p-10"><blockquote class="disp text-[clamp(1.4rem,2.4vw,2rem)] leading-snug">&ldquo;{e(q)}&rdquo;</blockquote><figcaption class="mt-6 text-[13px] text-stone-500">{e(w)} &middot; sample review</figcaption></figure>' for w,q in d['reviews'])
    words = d['hero_kicker'].split(' · ')
    stacked = "<br />".join(e(w) for w in words)
    return head(d, "family=Fraunces:opsz,wght,SOFT,WONK@9..144,400..600,100,1&family=Inter:wght@400;500;600", css) + f'''  <body>
{demo_bar(d)}
    <header class="fixed inset-x-0 top-[34px] z-40 bg-[#f7f1e7]/90 backdrop-blur-md">
      <div class="flex items-center justify-between px-5 py-4 sm:px-8">
        <a href="#main" class="disp text-[24px]">{e(d['name'])}</a>
        <nav class="hidden gap-8 text-[14px] font-medium md:flex"><a href="#services">Menu</a><a href="#about">About</a><a href="#location">Find us</a><a href="#faq">FAQ</a></nav>
        <a href="#book" class="btn btn-brand !py-2.5 !px-5 !text-[14px]">{e(d['book_label'])}</a>
      </div>
    </header>

    <main id="main" class="pt-[92px]">
      <section class="grid gap-10 px-5 pb-20 pt-16 sm:px-8 md:grid-cols-12 md:pb-32 md:pt-28">
        <h1 class="disp text-[clamp(3.4rem,10.5vw,11rem)] leading-[0.88] md:col-span-8">{stacked}</h1>
        <div class="flex flex-col justify-end md:col-span-4"><p class="disp text-[clamp(1.4rem,2.4vw,2rem)] leading-snug">{e(d['tagline'])}</p><p class="mt-6 text-[16px] leading-relaxed text-stone-600">{e(d['hero_body'])}</p><div class="mt-8 flex flex-wrap gap-3"><a href="#book" class="btn btn-brand">{e(d['book_label'])}</a><a href="tel:{d['phone_tel']}" class="btn btn-line">Call</a></div></div>
      </section>

      <section class="band px-5 py-14 sm:px-8"><div class="grid gap-10 sm:grid-cols-2 md:grid-cols-4">{hours}<div><p class="text-[12px] uppercase tracking-[0.16em] opacity-70">Where</p><p class="disp mt-2 text-[22px] leading-tight">{e(d['address'])}</p></div></div></section>

      <section id="services" class="px-5 py-20 sm:px-8 md:py-32">
        <div class="flex flex-wrap items-end justify-between gap-6"><h2 class="disp text-[clamp(2.5rem,6vw,6rem)] leading-none">The menu.</h2><p class="max-w-sm text-[15px] leading-relaxed text-stone-600">Prices are what you pay. No service charge, no &ldquo;HM po?&rdquo; in the comments.</p></div>
        <ul class="mt-16 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
{menu}
        </ul>
      </section>

      <section id="about" class="px-5 py-20 sm:px-8 md:py-32">
        <h2 class="disp max-w-3xl text-[clamp(2.5rem,6vw,6rem)] leading-none">{e(d['about_title'])}</h2>
        <div class="mt-16 grid gap-12 md:grid-cols-3">
{about}
        </div>
      </section>

      <section id="book" class="band px-5 py-20 sm:px-8 md:py-32">
        <div class="grid gap-16 md:grid-cols-12">
          <div class="md:col-span-5"><h2 class="disp text-[clamp(2.5rem,6vw,6rem)] leading-none">Reserve<br />a table.</h2><p class="mt-8 max-w-sm text-[16px] leading-relaxed opacity-80">Tables, the whole second floor, or catering. Your request lands in our inbox the moment you send it; we confirm by text.</p></div>
          <div class="md:col-span-7">
{form(d, "btn btn-cream mt-10 w-full sm:w-auto", note_class="opacity-70", done_class="text-white", label_class="text-[12px] font-medium uppercase tracking-[0.14em] opacity-80")}
          </div>
        </div>
      </section>

      <section id="reviews" class="px-5 py-20 sm:px-8 md:py-32">
        <div class="grid gap-5 md:grid-cols-2">
{reviews}
        </div>
      </section>

      <section id="location" class="grid md:grid-cols-2">
        <div class="px-5 py-20 sm:px-8 md:py-32">
          <h2 class="disp text-[clamp(2.5rem,6vw,6rem)] leading-none">Find us.</h2>
          <address class="mt-8 not-italic text-[17px] leading-relaxed text-stone-600">{e(d['address'])}<br />{e(d['landmark'])}</address>
          <div class="mt-10 flex flex-wrap gap-3"><a href="tel:{d['phone_tel']}" class="btn btn-brand">Call {e(d['phone'])}</a><a href="{viber(d)}" class="btn btn-line">Viber</a><a href="https://{d['messenger']}" rel="noopener" class="btn btn-line">Messenger</a><a href="{maps_link(d)}" rel="noopener" class="btn btn-line">Directions</a></div>
        </div>
        <div class="p-5 sm:p-8"><div class="h-full overflow-hidden rounded-3xl">{map_iframe(d, "h-[380px] w-full md:h-full md:min-h-[520px]")}</div></div>
      </section>

      <section id="faq" class="px-5 py-20 sm:px-8 md:py-32">
        <div class="grid gap-10 md:grid-cols-12"><h2 class="disp text-[clamp(2rem,4vw,3.5rem)] leading-none md:col-span-4">Good to know.</h2><div class="md:col-span-8">
{faqs}
        </div></div>
      </section>
    </main>

    <footer class="px-5 pb-10 pt-4 sm:px-8">
      <div class="flex flex-wrap items-center justify-between gap-6 border-t border-[#2a1d12]/20 pt-8 text-[13px] text-stone-600"><p class="disp text-[20px] text-[#2a1d12]">{e(d['name'])}</p>{footer_credit(d, "")}</div>
    </footer>
{mobile_bar(d, "btn btn-line !py-3", "btn btn-brand !py-3", "bg-[#f7f1e7]/95 border-[#2a1d12]/20")}
''' + SCRIPT

# ============================================================
# 4. AUTO — industrial dark: condensed uppercase, safety-yellow, grid rules
# ============================================================
def auto(d):
    d = dict(d, accent="#facc15", accent_dark="#eab308")
    css = '''      body { background: #0b0b0c; color: #f5f5f4; font-family: Inter, "Helvetica Neue", sans-serif; }
      .cond { font-family: "Barlow Condensed", "Arial Narrow", sans-serif; font-weight: 700; text-transform: uppercase; letter-spacing: -0.01em; }
      .rule { border-color: #2a2a2d; }
      .y { color: var(--brand); }
      .field { display:block; width:100%; border:1px solid #3a3a3e; background:#151517; padding:.85rem 1rem; font-size:16px; color:#f5f5f4; border-radius:0; }
      .field:focus { outline:none; border-color: var(--brand); } .field option { color:#0b0b0c; }
      .btn { display:inline-flex; align-items:center; justify-content:center; padding:1rem 1.75rem; font-family:"Barlow Condensed", sans-serif; font-size:18px; font-weight:700; text-transform:uppercase; letter-spacing:.06em; transition: all .2s; }
      .btn-y { background: var(--brand); color:#0b0b0c; } .btn-y:hover { background:#fff; }
      .btn-line { border:1px solid #f5f5f4; color:#f5f5f4; } .btn-line:hover { background:#f5f5f4; color:#0b0b0c; }
    '''
    services = "\n".join(f'<li class="grid gap-2 border-t rule py-6 md:grid-cols-12 md:items-baseline"><p class="cond text-[14px] text-stone-500 md:col-span-1">{i+1:02d}</p><p class="cond text-[30px] md:col-span-7">{e(n)}</p><p class="text-[14px] text-stone-400 md:col-span-2">{e(note)}</p><p class="cond y text-[30px] tabular-nums md:col-span-2 md:text-right">{e(p)}</p></li>' for i,(n,p,note) in enumerate(d['services']))
    about = "\n".join(f'<div class="border-t rule pt-6 md:border-l md:border-t-0 md:pl-8"><p class="cond y text-[14px]">Rule {i+1:02d}</p><h3 class="cond mt-4 text-[34px] leading-none">{e(t)}</h3><p class="mt-5 text-[15.5px] leading-relaxed text-stone-400">{e(b)}</p></div>' for i,(t,b) in enumerate(d['about']))
    hours = "\n".join(f'<li class="flex justify-between border-t rule py-4 text-[15px]"><span class="text-stone-400">{e(a)}</span><span class="text-right">{e(b)}</span></li>' for a,b in d['hours'])
    faqs = "\n".join(f'<details class="group border-t rule py-6"><summary class="cond flex cursor-pointer items-baseline justify-between gap-8 text-[28px] leading-none">{e(q)}<span class="y text-2xl transition-transform group-open:rotate-45" aria-hidden="true">+</span></summary><p class="mt-4 max-w-2xl text-[15.5px] leading-relaxed text-stone-400">{e(a)}</p></details>' for q,a in d['faqs'])
    reviews = "\n".join(f'<figure class="border-t rule pt-8"><p class="y cond text-[18px]">★★★★★</p><blockquote class="mt-4 text-[20px] leading-snug text-stone-200">&ldquo;{e(q)}&rdquo;</blockquote><figcaption class="cond mt-6 text-[14px] text-stone-500">{e(w)} &middot; sample review</figcaption></figure>' for w,q in d['reviews'])
    return head(d, "family=Barlow+Condensed:wght@600;700;800&family=Inter:wght@400;500", css, dark=True) + f'''  <body>
{demo_bar(d, dark=True)}
    <header class="fixed inset-x-0 top-[34px] z-40 border-b rule bg-[#0b0b0c]/90 backdrop-blur-md">
      <div class="flex items-center justify-between px-5 py-3.5 sm:px-8">
        <a href="#main" class="cond text-[26px] leading-none">{e(d['name'])}</a>
        <nav class="cond hidden gap-8 text-[16px] text-stone-400 md:flex"><a href="#services" class="hover:text-white">Services</a><a href="#about" class="hover:text-white">How we work</a><a href="#location" class="hover:text-white">Shop</a><a href="#faq" class="hover:text-white">FAQ</a></nav>
        <div class="flex items-center gap-5"><a href="tel:{d['phone_tel']}" class="cond hidden text-[18px] sm:block">{e(d['phone'])}</a><a href="#book" class="btn btn-y !py-2 !px-5 !text-[16px]">{e(d['book_label'])}</a></div>
      </div>
    </header>

    <main id="main" class="pt-[90px]">
      <section class="px-5 pb-16 pt-16 sm:px-8 md:pb-28 md:pt-28">
        <p class="cond y text-[16px] tracking-[0.08em]">{e(d['hero_kicker'])}</p>
        <h1 class="cond mt-6 max-w-[16ch] text-[clamp(3.2rem,9.5vw,10rem)] leading-[0.85]">{e(d['tagline'])}</h1>
        <div class="mt-14 grid gap-8 border-t rule pt-8 md:grid-cols-12">
          <p class="max-w-lg text-[17px] leading-relaxed text-stone-400 md:col-span-7">{e(d['hero_body'])}</p>
          <div class="flex flex-wrap gap-3 md:col-span-5 md:justify-end"><a href="#book" class="btn btn-y">{e(d['book_label'])}</a><a href="tel:{d['phone_tel']}" class="btn btn-line">Call</a></div>
        </div>
      </section>

      <section class="grid border-y rule sm:grid-cols-2 md:grid-cols-4">
        <div class="border-b rule p-6 sm:border-r md:border-b-0"><p class="cond text-[14px] text-stone-500">Open</p><p class="cond mt-1 text-[24px]">{e(d['hours'][0][0])}, {e(d['hours'][0][1])}</p></div>
        <div class="border-b rule p-6 md:border-b-0 md:border-r"><p class="cond text-[14px] text-stone-500">Where</p><p class="cond mt-1 text-[24px]">{e(d['city'])}</p></div>
        <div class="border-b rule p-6 sm:border-b-0 sm:border-r"><p class="cond text-[14px] text-stone-500">Quote</p><p class="cond mt-1 text-[24px]">Before any work</p></div>
        <div class="p-6"><p class="cond text-[14px] text-stone-500">Message</p><p class="cond mt-1 flex gap-5 text-[24px]"><a href="{viber(d)}" class="y">Viber</a><a href="https://{d['messenger']}" rel="noopener" class="y">Messenger</a></p></div>
      </section>

      <section id="services" class="px-5 py-16 sm:px-8 md:py-28">
        <h2 class="cond text-[clamp(2.5rem,7vw,7rem)] leading-none">Services <span class="text-stone-500">&amp;</span> prices</h2>
        <ul class="mt-12 border-b rule">
{services}
        </ul>
        <p class="mt-6 text-[14px] text-stone-500">&ldquo;From&rdquo; means the part price depends on your model. You get the exact number on Messenger before we start.</p>
      </section>

      <section id="about" class="border-t rule px-5 py-16 sm:px-8 md:py-28">
        <h2 class="cond text-[clamp(2.5rem,7vw,7rem)] leading-none">{e(d['about_title'])}</h2>
        <div class="mt-14 grid gap-10 md:grid-cols-3">
{about}
        </div>
      </section>

      <section id="book" class="border-t rule bg-[#111113] px-5 py-16 sm:px-8 md:py-28">
        <div class="grid gap-14 md:grid-cols-12">
          <div class="md:col-span-5"><p class="cond y text-[16px]">Book a bay</p><h2 class="cond mt-4 text-[clamp(2.5rem,7vw,7rem)] leading-none">Pick a slot.<br />We hold it.</h2><p class="mt-8 max-w-sm text-[16px] leading-relaxed text-stone-400">Morning or afternoon. Tell us the model and the problem; we confirm by text and quote before we touch anything.</p></div>
          <div class="md:col-span-7">
{form(d, "btn btn-y mt-10 w-full sm:w-auto", note_class="text-stone-500", done_class="y", label_class="cond text-[15px] text-stone-400")}
          </div>
        </div>
      </section>

      <section id="reviews" class="border-t rule px-5 py-16 sm:px-8 md:py-28">
        <div class="grid gap-12 md:grid-cols-2">
{reviews}
        </div>
      </section>

      <section id="location" class="grid border-t rule md:grid-cols-2">
        <div class="px-5 py-16 sm:px-8 md:py-28">
          <h2 class="cond text-[clamp(2.5rem,7vw,7rem)] leading-none">The shop</h2>
          <address class="mt-8 not-italic text-[16px] leading-relaxed text-stone-400">{e(d['address'])}<br />{e(d['landmark'])}</address>
          <ul class="mt-10 border-b rule">
{hours}
          </ul>
          <div class="mt-10 flex flex-wrap gap-3"><a href="tel:{d['phone_tel']}" class="btn btn-y">Call {e(d['phone'])}</a><a href="{maps_link(d)}" rel="noopener" class="btn btn-line">Directions</a></div>
        </div>
        <div class="border-t rule md:border-l md:border-t-0">{map_iframe(d, "h-[380px] w-full invert-[.92] hue-rotate-180 md:h-full md:min-h-[600px]")}</div>
      </section>

      <section id="faq" class="border-t rule px-5 py-16 sm:px-8 md:py-28">
        <div class="grid gap-10 md:grid-cols-12"><h2 class="cond text-[clamp(2rem,4vw,3.5rem)] leading-none md:col-span-3">FAQ</h2><div class="md:col-span-9">
{faqs}
        </div></div>
      </section>
    </main>

    <footer class="border-t rule px-5 py-8 sm:px-8">
      <div class="flex flex-wrap items-center justify-between gap-6 text-[13px] text-stone-500"><p class="cond text-[20px] text-white">{e(d['name'])}</p>{footer_credit(d, "")}</div>
    </footer>
{mobile_bar(d, "btn btn-line !py-3", "btn btn-y !py-3", "bg-[#0b0b0c]/95 border-[#2a2a2d]")}
''' + SCRIPT

# ============================================================
# 5. FITNESS — bold: Bebas Neue, black/white blocks, orange, schedule rows
# ============================================================
def fitness(d):
    css = '''      body { background: #fff; color: #0a0a0a; font-family: Inter, "Helvetica Neue", sans-serif; }
      .bebas { font-family: "Bebas Neue", Impact, sans-serif; letter-spacing: .01em; }
      .o { color: var(--brand); }
      .field { display:block; width:100%; border:2px solid #0a0a0a; background:#fff; padding:.85rem 1rem; font-size:16px; color:#0a0a0a; border-radius:0; }
      .field:focus { outline:none; border-color: var(--brand); }
      .btn { display:inline-flex; align-items:center; justify-content:center; padding:1rem 2rem; font-family:"Bebas Neue", sans-serif; font-size:24px; letter-spacing:.04em; transition: all .2s; }
      .btn-o { background: var(--brand); color:#fff; } .btn-o:hover { background:#0a0a0a; }
      .btn-k { background:#0a0a0a; color:#fff; } .btn-k:hover { background: var(--brand); }
      .btn-w { border:2px solid #0a0a0a; color:#0a0a0a; } .btn-w:hover { background:#0a0a0a; color:#fff; }
      .btn-wl { border:2px solid #fff; color:#fff; } .btn-wl:hover { background:#fff; color:#0a0a0a; }
    '''
    services = "\n".join(f'<li class="grid gap-2 border-t-2 border-black py-6 md:grid-cols-12 md:items-baseline"><p class="bebas text-[clamp(2rem,4vw,3.5rem)] leading-none md:col-span-7">{e(n)}</p><p class="text-[14px] font-medium uppercase tracking-[0.1em] text-stone-500 md:col-span-3">{e(note)}</p><p class="bebas o text-[clamp(2rem,4vw,3.5rem)] leading-none tabular-nums md:col-span-2 md:text-right">{e(p)}</p></li>' for n,p,note in d['services'])
    sched = "\n".join(f'<li class="flex items-baseline justify-between gap-6 border-t border-white/20 py-5"><span class="bebas text-[clamp(1.8rem,3.5vw,3rem)] leading-none">{e(o)}</span><a href="#book" class="text-[13px] font-semibold uppercase tracking-[0.12em] text-white/60 hover:text-white">Book &rarr;</a></li>' for o in d['booking_options'][:5])
    about = "\n".join(f'<div><p class="bebas o text-[80px] leading-none">{i+1:02d}</p><h3 class="bebas mt-2 text-[40px] leading-none">{e(t)}</h3><p class="mt-4 text-[16px] leading-relaxed text-stone-600">{e(b)}</p></div>' for i,(t,b) in enumerate(d['about']))
    hours = "\n".join(f'<li class="flex justify-between border-t-2 border-black py-4"><span class="text-[13px] font-semibold uppercase tracking-[0.1em] text-stone-500">{e(a)}</span><span class="bebas text-[26px] leading-none">{e(b)}</span></li>' for a,b in d['hours'])
    faqs = "\n".join(f'<details class="group border-t-2 border-black py-6"><summary class="bebas flex cursor-pointer items-baseline justify-between gap-8 text-[36px] leading-none">{e(q)}<span class="o transition-transform group-open:rotate-45" aria-hidden="true">+</span></summary><p class="mt-4 max-w-2xl text-[16px] leading-relaxed text-stone-600">{e(a)}</p></details>' for q,a in d['faqs'])
    reviews = "\n".join(f'<figure><blockquote class="bebas text-[clamp(2rem,4vw,3.6rem)] leading-[0.95]">&ldquo;{e(q)}&rdquo;</blockquote><figcaption class="mt-6 text-[13px] font-semibold uppercase tracking-[0.12em] text-stone-500">{e(w)} &middot; sample review</figcaption></figure>' for w,q in d['reviews'])
    return head(d, "family=Bebas+Neue&family=Inter:wght@400;500;600;700", css) + f'''  <body>
{demo_bar(d)}
    <header class="fixed inset-x-0 top-[34px] z-40 border-b-2 border-black bg-white/90 backdrop-blur-md">
      <div class="flex items-center justify-between px-5 py-3 sm:px-8">
        <a href="#main" class="bebas text-[30px] leading-none">{e(d['name'])}</a>
        <nav class="hidden gap-8 text-[13px] font-semibold uppercase tracking-[0.12em] md:flex"><a href="#services">Pricing</a><a href="#schedule">Schedule</a><a href="#about">Why</a><a href="#location">Studio</a></nav>
        <a href="#book" class="btn btn-o !py-2 !px-5 !text-[20px]">{e(d['book_label'])}</a>
      </div>
    </header>

    <main id="main" class="pt-[90px]">
      <section class="px-5 pb-16 pt-16 sm:px-8 md:pb-24 md:pt-24">
        <p class="text-[13px] font-semibold uppercase tracking-[0.18em] o">{e(d['hero_kicker'])} &middot; {e(d['city'])}</p>
        <h1 class="bebas mt-6 max-w-[14ch] text-[clamp(4rem,12vw,13rem)] leading-[0.85]">{e(d['tagline'])}</h1>
        <div class="mt-12 grid gap-8 md:grid-cols-12">
          <p class="max-w-lg text-[17px] leading-relaxed text-stone-600 md:col-span-7">{e(d['hero_body'])}</p>
          <div class="flex flex-wrap gap-3 md:col-span-5 md:justify-end md:self-end"><a href="#book" class="btn btn-o">{e(d['book_label'])}</a><a href="#schedule" class="btn btn-w">Schedule</a></div>
        </div>
      </section>

      <section id="schedule" class="bg-[#0a0a0a] px-5 py-16 text-white sm:px-8 md:py-28">
        <div class="grid gap-12 md:grid-cols-12">
          <div class="md:col-span-4"><h2 class="bebas text-[clamp(3rem,8vw,8rem)] leading-[0.85]">This<br />week.</h2><p class="mt-6 max-w-xs text-[15px] leading-relaxed text-white/60">Every class capped at eight. Book a spot; cancel up to two hours before and keep the credit.</p></div>
          <ul class="border-b border-white/20 md:col-span-8">
{sched}
          </ul>
        </div>
      </section>

      <section id="services" class="px-5 py-16 sm:px-8 md:py-28">
        <h2 class="bebas text-[clamp(3rem,8vw,8rem)] leading-[0.85]">Pricing.<br /><span class="o">No lock-in.</span></h2>
        <ul class="mt-12 border-b-2 border-black">
{services}
        </ul>
      </section>

      <section id="about" class="px-5 py-16 sm:px-8 md:py-28" style="background: var(--brand);">
        <div class="text-white">
          <h2 class="bebas text-[clamp(3rem,8vw,8rem)] leading-[0.85]">{e(d['about_title'])}</h2>
          <div class="mt-14 grid gap-12 md:grid-cols-3">
{about.replace('o text-[80px]', 'text-[80px] text-white/60').replace('text-stone-600','text-white/85')}
          </div>
        </div>
      </section>

      <section id="book" class="px-5 py-16 sm:px-8 md:py-28">
        <div class="grid gap-14 md:grid-cols-12">
          <div class="md:col-span-5"><h2 class="bebas text-[clamp(3rem,8vw,8rem)] leading-[0.85]">Book<br />a class.</h2><p class="mt-6 max-w-sm text-[16px] leading-relaxed text-stone-600">First time? Pick the assessment. Otherwise pick your class and we&rsquo;ll confirm by text.</p></div>
          <div class="md:col-span-7">
{form(d, "btn btn-k mt-10 w-full sm:w-auto", done_class="o", label_class="text-[12px] font-semibold uppercase tracking-[0.14em]")}
          </div>
        </div>
      </section>

      <section id="reviews" class="bg-[#0a0a0a] px-5 py-16 text-white sm:px-8 md:py-28">
        <div class="grid gap-16 md:grid-cols-2">
{reviews.replace('text-stone-500','text-white/50')}
        </div>
      </section>

      <section id="location" class="grid md:grid-cols-2">
        <div class="px-5 py-16 sm:px-8 md:py-28">
          <h2 class="bebas text-[clamp(3rem,8vw,8rem)] leading-[0.85]">The studio.</h2>
          <address class="mt-8 not-italic text-[16px] leading-relaxed text-stone-600">{e(d['address'])}<br />{e(d['landmark'])}</address>
          <ul class="mt-10 border-b-2 border-black">
{hours}
          </ul>
          <div class="mt-10 flex flex-wrap gap-3"><a href="tel:{d['phone_tel']}" class="btn btn-k">Call</a><a href="{viber(d)}" class="btn btn-w">Viber</a><a href="https://{d['messenger']}" rel="noopener" class="btn btn-w">Messenger</a><a href="{maps_link(d)}" rel="noopener" class="btn btn-w">Directions</a></div>
        </div>
        {map_iframe(d, "h-[380px] w-full grayscale contrast-125 md:h-full md:min-h-[600px]")}
      </section>

      <section id="faq" class="px-5 py-16 sm:px-8 md:py-28">
        <div class="grid gap-10 md:grid-cols-12"><h2 class="bebas text-[clamp(2.5rem,5vw,5rem)] leading-none md:col-span-3">FAQ</h2><div class="md:col-span-9">
{faqs}
        </div></div>
      </section>
    </main>

    <footer class="border-t-2 border-black px-5 py-8 sm:px-8">
      <div class="flex flex-wrap items-center justify-between gap-6 text-[13px] text-stone-500"><p class="bebas text-[24px] text-black">{e(d['name'])}</p>{footer_credit(d, "")}</div>
    </footer>
{mobile_bar(d, "btn btn-w !py-2.5", "btn btn-o !py-2.5", "bg-white/95 border-black")}
''' + SCRIPT

# ============================================================
# 6. PET — soft: DM Sans, pale green, big rounded shapes, pills
# ============================================================
def pet(d):
    css = '''      body { background: #f5f8ef; color: #1f2a1a; font-family: "DM Sans", Inter, sans-serif; }
      .g { color: var(--brand); }
      .blob { background: var(--brand); border-radius: 48% 52% 40% 60% / 55% 45% 55% 45%; }
      .field { display:block; width:100%; border:1.5px solid #cfd9c2; background:#fff; padding:.9rem 1.1rem; font-size:16px; color:#1f2a1a; border-radius:1.25rem; }
      .field:focus { outline:none; border-color: var(--brand); }
      .btn { display:inline-flex; align-items:center; justify-content:center; padding:1rem 1.9rem; font-size:15px; font-weight:600; border-radius:9999px; transition: all .2s; }
      .btn-g { background: var(--brand); color:#fff; } .btn-g:hover { background: var(--brand-dark); }
      .btn-w { background:#fff; color:#1f2a1a; border:1.5px solid #cfd9c2; } .btn-w:hover { border-color:#1f2a1a; }
      .card { background:#fff; border-radius: 2rem; }
    '''
    services = "\n".join(f'<li class="card flex items-baseline justify-between gap-6 px-7 py-6"><div><p class="text-[19px] font-semibold tracking-tight">{e(n)}</p><p class="mt-1 text-[13px] text-stone-500">{e(note)}</p></div><p class="text-[19px] font-semibold tabular-nums">{e(p)}</p></li>' for n,p,note in d['services'])
    about = "\n".join(f'<div class="card p-9"><span class="blob block h-10 w-10 opacity-80" aria-hidden="true"></span><h3 class="mt-6 text-[24px] font-semibold tracking-tight">{e(t)}</h3><p class="mt-3 text-[16px] leading-relaxed text-stone-600">{e(b)}</p></div>' for t,b in d['about'])
    hours = "\n".join(f'<li class="flex justify-between border-t border-[#cfd9c2] py-4 text-[16px]"><span class="text-stone-500">{e(a)}</span><span class="font-semibold">{e(b)}</span></li>' for a,b in d['hours'])
    faqs = "\n".join(f'<details class="card group px-8 py-6"><summary class="flex cursor-pointer items-baseline justify-between gap-8 text-[19px] font-semibold tracking-tight">{e(q)}<span class="g text-2xl transition-transform group-open:rotate-45" aria-hidden="true">+</span></summary><p class="mt-4 text-[16px] leading-relaxed text-stone-600">{e(a)}</p></details>' for q,a in d['faqs'])
    reviews = "\n".join(f'<figure class="card p-10"><p class="g text-lg tracking-tight">★★★★★</p><blockquote class="mt-4 text-[22px] leading-snug tracking-tight">&ldquo;{e(q)}&rdquo;</blockquote><figcaption class="mt-6 text-[13px] text-stone-500">{e(w)} &middot; sample review</figcaption></figure>' for w,q in d['reviews'])
    return head(d, "family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700", css) + f'''  <body>
{demo_bar(d)}
    <header class="fixed inset-x-0 top-[34px] z-40 bg-[#f5f8ef]/90 backdrop-blur-md">
      <div class="flex items-center justify-between px-5 py-4 sm:px-8">
        <a href="#main" class="flex items-center gap-3 text-[17px] font-bold tracking-tight"><span class="blob block h-8 w-8" aria-hidden="true"></span>{e(d['name'])}</a>
        <nav class="hidden gap-8 text-[15px] font-medium text-stone-600 md:flex"><a href="#services" class="hover:text-[#1f2a1a]">Services</a><a href="#about" class="hover:text-[#1f2a1a]">Why us</a><a href="#location" class="hover:text-[#1f2a1a]">Visit</a><a href="#faq" class="hover:text-[#1f2a1a]">FAQ</a></nav>
        <a href="#book" class="btn btn-g !py-2.5 !px-5 !text-[14px]">{e(d['book_label'])}</a>
      </div>
    </header>

    <main id="main" class="pt-[92px]">
      <section class="relative overflow-hidden px-5 pb-24 pt-20 sm:px-8 md:pb-40 md:pt-36">
        <span class="blob pointer-events-none absolute -right-24 -top-24 h-[420px] w-[420px] opacity-15 md:h-[640px] md:w-[640px]" aria-hidden="true"></span>
        <p class="g text-[14px] font-semibold">{e(d['hero_kicker'])}</p>
        <h1 class="mt-6 max-w-[16ch] text-[clamp(2.8rem,8vw,7.5rem)] font-bold leading-[0.95] tracking-[-0.035em]">{e(d['tagline'])}</h1>
        <p class="mt-10 max-w-xl text-[18px] leading-relaxed text-stone-600">{e(d['hero_body'])}</p>
        <div class="mt-10 flex flex-wrap gap-3"><a href="#book" class="btn btn-g">{e(d['book_label'])}</a><a href="tel:{d['phone_tel']}" class="btn btn-w">Call {e(d['phone'])}</a><a href="https://{d['messenger']}" rel="noopener" class="btn btn-w">Message</a></div>
      </section>

      <section id="services" class="px-5 py-20 sm:px-8 md:py-32">
        <div class="grid gap-12 md:grid-cols-12">
          <div class="md:col-span-4"><h2 class="text-[clamp(2.2rem,5vw,4.5rem)] font-bold leading-[0.98] tracking-[-0.035em]">Services<br />&amp; prices.</h2><p class="mt-6 max-w-xs text-[16px] leading-relaxed text-stone-600">Vaccines include the consultation. Grooming is &ldquo;from&rdquo; because coat condition changes the time.</p></div>
          <ul class="grid gap-4 md:col-span-8">
{services}
          </ul>
        </div>
      </section>

      <section id="about" class="px-5 py-20 sm:px-8 md:py-32">
        <h2 class="max-w-3xl text-[clamp(2.2rem,5vw,4.5rem)] font-bold leading-[0.98] tracking-[-0.035em]">{e(d['about_title'])}</h2>
        <div class="mt-14 grid gap-5 md:grid-cols-3">
{about}
        </div>
      </section>

      <section id="book" class="px-5 py-20 sm:px-8 md:py-32">
        <div class="card grid gap-14 p-8 sm:p-12 md:grid-cols-12 md:p-16">
          <div class="md:col-span-5"><h2 class="text-[clamp(2.2rem,5vw,4.5rem)] font-bold leading-[0.98] tracking-[-0.035em]">{e(d['book_label'])}.</h2><p class="mt-6 max-w-sm text-[16px] leading-relaxed text-stone-600">Vet or grooming, pick a time, tell us your pet&rsquo;s name. We confirm by text and remind you the day before.</p></div>
          <div class="md:col-span-7">
{form(d, "btn btn-g mt-10 w-full sm:w-auto", done_class="g", label_class="text-[13px] font-semibold")}
          </div>
        </div>
      </section>

      <section id="reviews" class="px-5 py-20 sm:px-8 md:py-32">
        <div class="grid gap-5 md:grid-cols-2">
{reviews}
        </div>
      </section>

      <section id="location" class="px-5 py-20 sm:px-8 md:py-32">
        <div class="grid gap-10 md:grid-cols-2">
          <div>
            <h2 class="text-[clamp(2.2rem,5vw,4.5rem)] font-bold leading-[0.98] tracking-[-0.035em]">Find us in<br />{e(d['city'])}.</h2>
            <address class="mt-8 not-italic text-[17px] leading-relaxed text-stone-600">{e(d['address'])}<br />{e(d['landmark'])}</address>
            <ul class="mt-10 border-b border-[#cfd9c2]">
{hours}
            </ul>
            <div class="mt-10 flex flex-wrap gap-3"><a href="tel:{d['phone_tel']}" class="btn btn-g">Call</a><a href="{viber(d)}" class="btn btn-w">Viber</a><a href="https://{d['messenger']}" rel="noopener" class="btn btn-w">Messenger</a><a href="{maps_link(d)}" rel="noopener" class="btn btn-w">Directions</a></div>
          </div>
          <div class="overflow-hidden rounded-[2rem]">{map_iframe(d, "h-[380px] w-full md:h-full md:min-h-[520px]")}</div>
        </div>
      </section>

      <section id="faq" class="px-5 py-20 sm:px-8 md:py-32">
        <div class="grid gap-10 md:grid-cols-12"><h2 class="text-[clamp(2rem,4vw,3.5rem)] font-bold leading-[0.98] tracking-[-0.035em] md:col-span-4">Before you<br />come in.</h2><div class="grid gap-4 md:col-span-8">
{faqs}
        </div></div>
      </section>
    </main>

    <footer class="px-5 pb-10 pt-4 sm:px-8">
      <div class="flex flex-wrap items-center justify-between gap-6 border-t border-[#cfd9c2] pt-8 text-[13px] text-stone-500"><p class="text-[17px] font-bold text-[#1f2a1a]">{e(d['name'])}</p>{footer_credit(d, "")}</div>
    </footer>
{mobile_bar(d, "btn btn-w !py-3", "btn btn-g !py-3", "bg-[#f5f8ef]/95 border-[#cfd9c2]")}
''' + SCRIPT

RENDER = {"dental-clinic": dental, "salon": salon, "cafe": cafe, "auto-repair": auto, "fitness-studio": fitness, "pet-clinic": pet}
for d in INDUSTRIES:
    out = os.path.join(ROOT, "services", "templates", d["slug"], "index.html")
    open(out, "w").write(RENDER[d["slug"]](d))
    print("wrote", out)
