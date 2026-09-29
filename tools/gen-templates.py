#!/usr/bin/env python3
"""Generate the Sprntr demo sites under services/templates/.

Full docs: tools/README.md

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
          ("Do you offer installment for braces?","Yes. A ₱10,000 down payment, then monthly during adjustment visits."),
          ("Do you take walk-ins?","Yes, but booked patients are seen first. Book online or text us and we hold the slot for you."),
          ("Is whitening safe for sensitive teeth?","Usually. We check your enamel first and use a lower-strength gel over two sessions if needed.")],
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
    desc = f"Demo of a Sprntr website for a {d['industry'].lower()}: services and prices, online booking, click-to-call, hours and map. From ₱15,000 one-time, no monthly fees."
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
      <div class="flex items-center justify-between gap-3 px-4 text-[11px] sm:px-8 sm:text-[12px]" style="height:34px">
        <p class="flex items-center gap-2 whitespace-nowrap font-medium"><span class="block h-4 w-auto shrink-0">{MARK}</span><span class="sm:hidden">Demo &middot; {e(d['industry'])}</span><span class="hidden sm:inline">Demo &middot; Sprntr &middot; {e(d['industry'])} &middot; <span class="{muted}">{e(d['name'])} is fictional</span></span></p>
        <p class="flex shrink-0 items-center gap-4 font-semibold"><a href="/services/templates/" class="{muted} hidden underline-offset-4 hover:underline sm:inline">All templates</a><a href="/services/#pricing" class="underline underline-offset-4"><span class="sm:hidden">Get this &mdash; from &#8369;15k &rarr;</span><span class="hidden sm:inline">Get this for your business &mdash; from &#8369;15,000 &rarr;</span></a></p>
      </div>
    </div>
'''

def form(d, btn_class, note_class="text-stone-400", done_class="", label_class="text-[12px] font-semibold uppercase tracking-[0.12em]", extra=""):
    notes_hint = {
        "dental-clinic": "First visit, concerns, or preferred dentist…",
        "salon": "Preferred stylist, hair length, or your desired look…",
        "cafe": "Party size, occasion, and dietary preferences…",
        "auto-repair": "Vehicle make, model, year, and symptoms…",
        "fitness-studio": "Training experience, goals, or preferred coach…",
        "pet-clinic": "Pet’s name, species, age, and reason for visiting…",
    }[d['slug']]
    time_options = ["Morning", "Afternoon"]
    if d['slug'] in ('salon', 'cafe', 'fitness-studio'):
        time_options.append("Evening")
    times = ''.join(f'<option>{slot}</option>' for slot in time_options)
    opts = "\n".join(f'                <option>{e(o)}</option>' for o in d['booking_options'])
    return f'''          <form id="bookingForm" class="{extra}" novalidate>
            <div class="grid gap-x-8 gap-y-7 sm:grid-cols-2">
              <label class="block {label_class}">Your name<input type="text" name="name" required autocomplete="name" class="field" placeholder="Juan dela Cruz" /></label>
              <label class="block {label_class}">Mobile number<input type="tel" name="phone" required autocomplete="tel" inputmode="tel" class="field" placeholder="0917 000 0000" /></label>
              <label class="block {label_class} sm:col-span-2">Service<select name="service" required class="field">
{opts}
              </select></label>
              <label class="block {label_class}">Preferred date<input type="date" name="date" required class="field" /></label>
              <label class="block {label_class}">Preferred time<select name="time" required class="field">{times}</select></label>
              <label class="block {label_class} sm:col-span-2">Notes <span class="font-normal normal-case tracking-normal opacity-60">(optional)</span><textarea name="notes" rows="2" class="field" placeholder="{e(notes_hint)}"></textarea></label>
            </div>
            <button type="submit" class="{btn_class}">Send {e(d['verb'])} request</button>
            <p class="mt-4 text-[12.5px] {note_class}">Demo only &mdash; no appointment is made and nothing is sent.</p>
            <p id="bookingDone" class="mt-5 hidden text-[15px] font-semibold {done_class}" role="status" aria-live="polite">Demo complete &mdash; your form is valid. Nothing was sent or booked.</p>
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
    return f'<p class="{cls}">Demo site by <a href="/" class="underline underline-offset-4">Ruther Bergonia</a> &middot; <a href="/services/" class="underline underline-offset-4">Sprntr</a></p>'

# Compositions live separately so business data and visual design stay easy to edit.
with open(os.path.join(ROOT, "tools", "template-designs.py")) as design_file:
    exec(compile(design_file.read(), design_file.name, "exec"))

RENDER = {"dental-clinic": dental, "salon": salon, "cafe": cafe, "auto-repair": auto, "fitness-studio": fitness, "pet-clinic": pet}
if __name__ == "__main__":
    for d in INDUSTRIES:
        out = os.path.join(ROOT, "services", "templates", d["slug"], "index.html")
        with open(out, "w") as page:
            page.write(RENDER[d["slug"]](d))
        print("wrote", out)

    dental_data = next(d for d in INDUSTRIES if d['slug'] == 'dental-clinic')
    for view in ('services', 'faqs', 'contact'):
        folder = os.path.join(ROOT, 'services', 'templates', 'dental-clinic', view)
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, 'index.html'), 'w') as page:
            page.write(dental(dental_data, view))
