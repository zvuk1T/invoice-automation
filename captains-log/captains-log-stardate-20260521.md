# 🚀 CAPTAIN'S LOG - STARDATE 20260521
## Project: Invoice Automation Tool
### Science Officer: Spock | Mission Specialist: Lieutenant Commander Data (zvuk1T)

---

## 📋 SESSION SUMMARY

**Session Date:** 21.05.2026
**Session Status:** ✅ Excel file prepared, utilities script created, guide written
**Current Phase:** Phase 3 in progress — Excel data ready for use in Python

---

## ✅ WHAT WE ACCOMPLISHED TODAY

### Part 0 — Bug fix (session start)
- Fixed YAML frontmatter error in `.github/prompts/new-month.prompt.md` ✅
- Fixed YAML frontmatter error in `.github/prompts/update-captains-log.prompt.md` ✅
- **Problem:** apostrophe inside single-quoted YAML string (`'captain\'s'`) causes parse error
- **Solution:** switched to double quotes (`"captain's"`) — apostrophe is safe inside double quotes

### Part 1 — Repo cleanup (earlier session)
- Restored `copilot-instructions.md` to correct location `.github/` ✅
- Added `data/*.pdf` to `.gitignore` — GDPR/privacy protection ✅
- Updated `requirements.txt` — added `pdfplumber`, comments translated to English ✅
- Committed captain's logs from sessions 20260510 and 20260520 ✅
- Updated `copilot-instructions.md`:
  - Rule 2: terminal commands use VS Code's built-in Continue/Cancel dialog ✅
  - Added Spock voice definition to Identity section ✅
- Updated `git-best-practices.md`:
  - New section: `⚡ CHAINED COMMANDS` — explains `&&` operator ✅
  - New section: `When to commit` — one commit = one logical unit ✅

### Part 3 — PDF extraction and Excel population
- Reviewed all 36 PDF invoices from `data/APRIL 2026/` ✅
- Created `pdf_extractor.py` — extracts all invoice fields from PDF text ✅
- Handled edge cases: leading zeros in contract numbers, broken "Ugovorb r." typo in one PDF ✅
- `invoice_number` format changed to `2026-05-0003` (YYYY-MM-NNNN) — sortable, unambiguous ✅
- 36/36 PDFs matched and Excel updated successfully ✅
- Added `data/*.xlsx` to `.gitignore` — GDPR protection ✅

---

## 📊 FINAL EXCEL COLUMN NAMES

| English (code) | Serbian (original) |
|---|---|
| `contract_number` | BR. UGOVORA |
| `date` | DATUM POTPISIVANJA |
| `apartment_name` | NAZIV OBJEKTA |
| `owner_name` | IME I PREZIME |
| `address` | ADRESA |
| `period` | OBRAČ. PERIOD |
| `invoice_number` | BR. FAKTURE |
| `fiscal_number` | BR. FISK. RAČUNA |
| `amount` | IZNOS (KM) |

### Part 4 — HTML invoice template (Step 5)
- Created `templates/invoice.html` — fully styled Jinja2 invoice template ✅
- Modern design: clean layout, professional typography, A4 proportional width (760px) ✅
- Brand color `#bb0033` applied via CSS variables in `:root` ✅
- CSS variables defined: `--primary`, `--primary-dark`, `--primary-light`, `--ink`, `--ink-muted`, `--border` ✅
- Jinja2 variables wired: `{{ invoice_number }}`, `{{ date }}`, `{{ period }}`, `{{ contract_number }}`, `{{ fiscal_number }}`, `{{ owner_name }}`, `{{ apartment_name }}`, `{{ address }}`, `{{ amount }}` ✅
- All CSS comments written in English (per copilot-instructions.md) ✅
- Fixed duplicate `</style>` block that appeared after one of the edit operations ✅
- Template sections: HEADER → META ROW → RECIPIENT CARD → ITEMS TABLE → TOTAL BOX → NOTE → FOOTER ✅
- Logo/stamp/signature placeholders: NOT YET ADDED — waiting for PNG exports from user's Illustrator file

---

## 📍 WHERE WE STOPPED

`templates/invoice.html` complete (no logo yet). Committed end of session 20260521.

---

## 🔜 NEXT STEP (Start here next session)

**Step 5 continued: Add logo, stamp and signature to the HTML template**

- User needs to export from `templates/template invoice rebuild v02 test.pdf` (Illustrator source):
  - `logo.png` → save to `templates/assets/`
  - `stamp.png` → save to `templates/assets/`
  - `signature.png` → save to `templates/assets/`
- Then add `<img>` tags to `invoice.html` header (logo) and footer (stamp + signature)
- After that: connect template to Excel data via Python + Jinja2 (Step 6)

---

## 🧠 KEY LEARNINGS TODAY

- `copilot-instructions.md` must be in `.github/` — Copilot reads it automatically from there
- One commit = one logical unit of work (not one per day, not one per line)
- `&&` in terminal = "do this, and if it succeeds — do the next thing"
- Captain's log should be written before closing a session, not after opening the next one
- `pandas` reads Excel into memory as a "DataFrame" — like a table you can manipulate with code
- `df.rename(columns={...})` replaces column names using a dictionary (old → new)
- `index=False` in `to_excel()` prevents pandas from adding an unwanted row-number column
- CSV has encoding risk with special characters (č, š, ž) — `.xlsx` is safer for this project
- `data/*.xlsx` must be in `.gitignore` — contains real client names and addresses (GDPR)
- `zfill(4)` pads a number with leading zeros to 4 digits: `"3".zfill(4)` → `"0003"`
- Invoice number format `YYYY-MM-NNNN` is sortable and unambiguous (not confused with a date)
- `pdfplumber` extracts raw text from PDF — regex then finds the specific values we need
- PDF text can have typos/broken spacing — regex must be flexible enough to handle variations
- To run a prompt file: type `#` in Copilot Chat and select the file from the dropdown — `/filename` is plain text, not a command
- YAML single-quoted strings cannot contain apostrophes — use double quotes instead: `"captain's"` ✅
- CSS variables in `:root` → define a color once, use it everywhere with `var(--name)` — one change updates the entire design
- `display: flex` + `justify-content: space-between` → places two elements on opposite sides of a row
- `border-collapse: collapse` on a table → removes double lines between cells
- `opacity: 0.7` → makes an element semi-transparent (useful for secondary text on colored backgrounds)
- WeasyPrint prefers inline CSS — external stylesheets can cause rendering issues in PDF output
- All code comments must be in English per copilot-instructions.md — even in HTML/CSS files

---

## 🖖 SPOCK'S NOTE

*"Naming things correctly is not cosmetic — it determines whether the code is readable six months from now."*

**Next session start:**
> In Copilot Chat, type `#` and select `new-session.prompt.md` from the dropdown.
> Do NOT type `/new-session.prompt.md` — that is plain text, not a command.
