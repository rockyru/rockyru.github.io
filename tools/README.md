# tools/

## `gen-templates.py` — LocalBiz Digital Hub demo sites

Generates the six demo sites under `services/templates/<slug>/index.html`
that the **Templates** section on `/services/` links to. Each demo is a
fictional Metro Manila business showing the full LocalBiz deliverable
(services & prices, booking form, click-to-call / Viber / Messenger, hours
and map, reviews, FAQ) in a design built for that trade.

The pages are **`noindex, nofollow`** on purpose and are not in
`sitemap.xml`: the businesses, prices, and reviews are made up.

### Run

```sh
python3 tools/gen-templates.py
npx tailwindcss@3 -c tailwind.config.js -i tailwind.source.css -o assets/tailwind.css --minify
```

No dependencies beyond Python 3. The Tailwind rebuild is required after
any run because the compiled stylesheet only includes classes it finds in
the HTML (`tailwind.config.js` scans `services/**/*.html`).

Output is deterministic — running it twice with no changes produces no
diff, so `git status` tells you whether an edit actually changed a page.

### Layout of the script

| Part | What it is |
|---|---|
| `INDUSTRIES` | One `dict` per demo. All the words, prices, hours, and colours live here. |
| `head()`, `demo_bar()`, `form()`, `map_iframe()`, `mobile_bar()`, `footer_credit()`, `SCRIPT` | Shared pieces every design uses. Change the booking form here and all six pages pick it up. |
| `dental()`, `salon()`, `cafe()`, `auto()`, `fitness()`, `pet()` | One render function per design. Each returns a full HTML document and carries its own `<style>` block and Google Fonts request. |
| `RENDER` | Maps a slug to its render function. |

### The data fields

| Field | Used for |
|---|---|
| `slug` | Output folder and URL: `services/templates/<slug>/` |
| `industry` | Demo bar and page title |
| `name`, `tagline`, `hero_kicker`, `hero_body` | Hero. The salon design splits `name` on the first space (first word roman, rest italic); the café stacks `hero_kicker` split on ` · ` as the headline. |
| `accent`, `accent_dark`, `tint` | CSS custom properties `--brand`, `--brand-dark`. The auto design overrides these to safety yellow. |
| `city`, `address`, `landmark`, `map_q` | Hours & location section. `map_q` is the Google Maps query for the embed and the Directions link — keep it a street + area, not a fictional building. |
| `phone`, `phone_tel`, `messenger`, `viber` | Call / message buttons. `phone_tel` is E.164 (`+63…`). |
| `book_label`, `verb` | CTA text and the submit button ("Send *visit* request"). |
| `about_title`, `about` | "Why us" heading and three `(title, body)` tuples. |
| `services` | Six `(name, price, note)` tuples. Use `"from ₱…"` when the price depends on inspection. |
| `booking_options` | `<option>`s in the booking form. The fitness design also shows the first five as "this week's schedule". |
| `hours` | `(days, times)` tuples. The first row is the one shown in hero/facts strips. |
| `reviews` | Two `(name, quote)` tuples, labelled "sample review" on the page. |
| `faqs` | Three `(question, answer)` tuples. |

### Adding an industry

1. Add a dict to `INDUSTRIES` with a new `slug`.
2. Either reuse a design (`RENDER["new-slug"] = dental`) or write a new
   render function following the same shape: `head(...) + body + SCRIPT`.
3. Run the two commands above.
4. Add a card by hand to the grids in `services/index.html` (the
   **Templates** section) and `services/templates/index.html` — those
   cards are not generated.

### Changing a design

Each render function's `css` string holds the design's tokens: body
background, type family, `.field` (form inputs), `.btn*` variants. Layout
uses Tailwind utilities inline. Keep sections full-width (`px-5 sm:px-8`,
no `max-w-*` container) to match the rest of the set.

### Demo behaviour

The booking form does not post anywhere: `SCRIPT` intercepts submit,
validates, and shows the "Request received" line. The note under the
button says so. On a client's real site this is replaced with the
email/notification handler.
