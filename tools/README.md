# Sprntr industry templates

Generate the six fictional demo sites with Python 3:

```sh
python3 tools/gen-templates.py
```

The generator is deterministic. Each page remains `noindex, nofollow`.
The businesses, prices, and reviews are fictional. Forms validate locally;
they never submit or create an appointment.

## Editing

- `gen-templates.py`: business data, metadata, accessible booking form, and demo submission behavior.
- `template-designs.py`: six separate page compositions, photography, section renderers, and mobile navigation.
- `../assets/templates/industries.css`: shared basics followed by clearly marked industry styles and responsive layouts.
- `../services/templates/index.html`: manually maintained gallery with preview images in `assets/templates/`.

Design directions:

| Industry | Composition |
| --- | --- |
| Dental | Four pages (landing, services, FAQs, contact): monochrome editorial type, expanding care rows, price tiles, smile gallery, drawer navigation |
| Salon | Burgundy editorial masthead, asymmetric image and service list |
| Café | Immersive photography, printed menu, coffee story |
| Auto | Dark workshop, yellow signage, process-first layout and technical pricing |
| Fitness | Lime campaign poster, schedule-first layout, membership cards |
| Pet | Overlapping pet portraits, pastel care pathways, rounded surfaces |

Industry styling uses regular CSS, so design changes do not need a Tailwind
rebuild. Existing shared form utilities use the checked-in Tailwind stylesheet.
Photography loads from Unsplash; fonts load from Google Fonts. Both have local
layout/color or font fallbacks. Gallery previews are local screenshots.

After editing, regenerate the pages and check desktop and narrow mobile sizes,
anchor navigation, the mobile menu (including Escape), FAQ disclosures, invalid
form submissions, and valid demo submissions. Schedule booking links preselect
the corresponding class. All booking forms prevent past preferred dates.

To add an industry, add its data, create its composition, register it in `RENDER`,
and add a gallery card. Give it a deliberate layout rather than copying a whole
existing page and changing its palette.

Dental-specific styling lives in `assets/templates/dental.css` and its navigation, care rows,
booking form, and `?service=` preselect in `assets/templates/dental.js`. Its visual direction
is inspired by Bogdan Nikitin / Nixtio’s Dental Clinic Website Design on Dribbble
(shot 20034563), using original implementation and independent stock photography.
