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

---

## 📍 WHERE WE STOPPED

Excel file fully populated with April 2026 data from 36 PDFs. All changes committed and pushed.

---

## 🔜 NEXT STEP (Start here next session)

**Step 5: Build the HTML invoice template**

- Create `templates/invoice.html` using Jinja2
- Design matches the existing PDF invoice layout
- Reference: `data/APRIL 2026/3.APP DIJANA.pdf` as visual reference

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

---

## 🖖 SPOCK'S NOTE

*"Naming things correctly is not cosmetic — it determines whether the code is readable six months from now."*

**Next session start:**
> In Copilot Chat, type `#` and select `new-session.prompt.md` from the dropdown.
> Do NOT type `/new-session.prompt.md` — that is plain text, not a command.
