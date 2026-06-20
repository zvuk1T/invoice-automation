# 🚀 CAPTAIN'S LOG — STARDATE 20260620
## Project: Invoice Automation Tool
### Science Officer: Spock | Mission Specialist: Lieutenant Commander Data (zvuk1T)

---

## 🧭 READ THIS FIRST — Next-session quick start

You (next Spock) are continuing **client revisions, round 1** — a set of **7
aesthetic changes** to the invoice design, requested by the client from an
annotated photo of a printed invoice.

**Before doing anything, read these 3 files in order:**
1. `client-revisions-round-1.md` ← the master plan + full change list (the brain)
2. `templates/invoice.html` ← the ONLY file we will edit for all 7 changes
3. This captain's log ← session context + technical notes below

**Then:** announce the next step (implement change **#1**), STOP, and wait for
Data's explicit confirmation. Do not edit and announce in the same message.

> ⚠️ **Nothing has been implemented yet.** All 7 changes are still ⬜ To do.
> Today's session was: gather context → capture the change list → save it safely.

---

## 📍 WHERE WE ARE

- **Phase:** Phase 5 (Flask web app) is **live and complete**.
  App URL: `https://e-agency-invoice-automation.onrender.com`
- **Now:** Client Revisions Round 1 — implementing 7 aesthetic tweaks to the invoice.
- **Branch:** `client-web-app` (NOT `main`). All this work happens here.
- **Status:** Change list captured & committed. Implementation not yet started.

---

## ✅ WHAT WE ACCOMPLISHED TODAY

1. **Gathered full project context** — read `app.py`, `main.py`, `invoice.html`
   (all 501 lines), `upload.html`, and the `templates/assets/` folder.
2. **Built an architecture/risk map** — which file controls what, and what each
   change can break (see section 2 of `client-revisions-round-1.md`).
3. **Created the tracking document** `client-revisions-round-1.md` — a dedicated
   per-task file (separate from the captain's log) so the plan survives across
   multiple sessions.
4. **Read the client's annotated invoice photo** (`data/IMG-20260620-WA0003.jpg`)
   and translated her handwritten notes into **7 concrete changes**.
5. **Captured all 7 changes** into the change-list table (section 4 of the
   tracking file), including 2 items flagged "to confirm".
6. **Fixed a privacy hole** in `.gitignore` (see lesson learned below).
7. **Committed & pushed** the tracking file + gitignore fix.

---

## 🐛 LESSON LEARNED — Privacy hole in `.gitignore` (caught before commit)

- **Problem:** `git status` showed the client's invoice photo
  `data/IMG-20260620-WA0003.jpg` as **untracked** (not ignored). The `.gitignore`
  rules for `data/` covered `*.pdf` and `*.xlsx` — but **not image files**.
- **Risk:** A blind `git add .` would have pushed a document containing the
  client's personal data (name, address, amounts) to a public portfolio repo.
  GDPR violation + the kind of mistake a recruiter notices.
- **Fix:** Added `data/*.jpg`, `data/*.jpeg`, `data/*.png` to `.gitignore`.
  All future client photos are now auto-protected — not just this one.
- **Verification:** Re-ran `git status` → photo no longer listed. Staged only the
  two intended files explicitly (no `git add .`). Confirmed before commit.
- **Takeaway:** Always `git status` before staging. Stage files explicitly.
  Never trust `git add .` on a repo that touches client data.

---

## 📋 THE 7 CHANGES — quick reference + technical notes

Full table lives in `client-revisions-round-1.md` § 4. Below are the **technical
hints** so you don't have to rediscover them. All edits are in `templates/invoice.html`.

### #1 — Company name reorder  🟢 ✅ confirmed by client
- **In the HTML body** (`.company-name` div):
  - Current: `e-agency LJUBINKA Vuković s.p.`
  - Target:  `e-agency s.p. LJUBINKA Vuković`  ← move `s.p.` to right after `e-agency`
- Pure text swap. Easiest change. Good first step.

### #2 — Bold the company details block  🟢
- CSS selector: `.company-details` (the address / JIB / bank lines).
- Client wrote *"boldovati"* → increase `font-weight` (e.g. 400 → 600) so it's
  more visible. Keep size/color; just weight.

### #3 — Meta row background: pale pink → light gray  🟢
- `.meta-row` uses `background: var(--primary-light);` where
  `--primary-light: #f9f0f3;` (pale pink).
- Client dislikes the pinkish tone → switch to a **light gray of similar
  lightness** (e.g. `#f4f4f6` / `#f5f5f5`).
- ⚠️ **Before editing:** `grep` for `--primary-light` to see if it's used
  elsewhere. Safer to change `.meta-row`'s background directly OR confirm the
  variable is only used here before editing the variable.
- Note: `.meta-row` already has `border-radius: 8px` — it's the visual reference
  for #4b.

### #4a — Add "Obračunski period" to the table  🟢 ⚠️ to confirm
- Table header currently: `PERIOD`. Interpretation: rename header → `OBRAČUNSKI PERIOD`.
- **Confirm exact wording + placement with client** (header label vs a new line).
- Colors stay the same.

### #4b — Round the table corners  🟢
- The items `table` header (`thead`) has **sharp** corners; client wants them
  rounded like the Total box and meta row (`border-radius: 8px`).
- ⚠️ **CSS gotcha:** `table { border-collapse: collapse; }` **ignores**
  `border-radius`. To round a table you must either:
  - set `border-collapse: separate; border-spacing: 0;` + `border-radius` +
    `overflow: hidden` on the table, **or**
  - apply `border-radius` to `thead th:first-child` / `:last-child`.
- **Bordo color is NOT touched** (the old "make the header gray" idea = cancelled).

### #5 — Outline lines → neutral gray  🟢 ⚠️ joint decision, to confirm
- **Context:** Client asked for outline lines in **bordo**. Data & Spock disagree:
  too much bordo. **Our decision: keep outline/structural lines GRAY**, reserve
  bordo only for **fills/accents** (table header fill, Total box fill, and the
  existing red line under the logo — which the client likes and we KEEP).
- **Action:** neutralize the pinkish `--border: #e8d0d8;` → a clean neutral gray
  (~50% black feel, e.g. `#cccccc` / `#bdbdbd`). Affected outline lines:
  `.recipient-card` border, `.footer` top border, `.note` top border, table row
  borders. We do **NOT** make them bordo.
- This is the **one place we push back on the client** — show her the result for approval.

### #6 — Amount `23,40`: NO CHANGE  ✅
- Client circled it as *"good as-is"*. Nothing to do.

### #7 — Signature / stamp block redesign  🟠 (most complex)
- Current footer structure:
  ```html
  <div class="footer-signature">
    S poštovanjem,
    <div class="sig-stamp-wrap">
      <img ... class="stamp-image" />   <!-- pecat.png -->
      <img ... class="sig-image" />     <!-- potpis.png -->
    </div>
    <div class="sig-name">LJUBINKA Vuković</div>
  </div>
  ```
- **Desired order:** `S poštovanjem,` → handwritten signature (potpis) → a
  horizontal line (signatures always sit ABOVE a line) → **`LJUBINKA Vuković`**
  in bordo, **UPPERCASE**.
- `.sig-name` is already bordo (`color: var(--primary)`); add `text-transform:
  uppercase` and an underline/line above it.
- **Also:** better **center & proportion** the stamp (`pecat.png`) + signature
  (`potpis.png`). Currently `.sig-stamp-wrap` is 140×90px, absolutely positioned.
  Data trusts Spock to recompute proportions so it looks balanced. Iterate, then
  show the client.

---

## 🔢 RECOMMENDED WORK ORDER

Top-to-bottom through the invoice (easy to test visually, region by region):

1. **#1** — company name (text)        ← start here
2. **#2** — bold company details (CSS)
3. **#3** — meta row gray background (CSS)
4. **#4a** — table "Obračunski period" (text)
5. **#4b** — table rounded corners (CSS gotcha — see notes)
6. **#5** — outline lines → gray (push-back decision)
7. **#7** — signature/stamp redesign (most complex — do last)

Commit after each change (or each logical group) with a descriptive message.

---

## ⚠️ TWO ITEMS TO CONFIRM WITH CLIENT (not blockers)

These do **not** stop implementation — build our interpretation, then show her:
- **#4a** — exact wording / placement of "Obračunski period".
- **#5** — gray vs bordo for outline lines (our design push-back).

---

## 🧪 HOW TO TEST

- This is the **local** branch logic: run the pipeline to generate PDFs.
  - First configure the Python environment, then run `main.py`.
  - It reads `data/stan_na_dan_klijenti_racuni.xlsx` (Sheet2) and writes PDFs to
    `output/` (gitignored).
- To match the client's photo, open **`output/2026-05-0004.pdf`** (Smilja Tepić)
  and compare visually.
- Spock cannot "see" a PDF directly — **Data opens the PDF (or shares a
  screenshot)** to confirm each change looks right before we move on.
- `output/` and all client data stay local — never committed.

---

## 📏 RULES TO REMEMBER (don't drift)

- **Address the user as "Data"** — not "kapetan". (His explicit preference.)
- **Confirmation Rule:** announce every action, STOP, wait for explicit
  "nastavi/continue". Never act in the same message as the announcement.
- **Privacy:** never commit anything in `data/` (photos, xlsx, pdf now all
  ignored). `git status` before staging; stage explicitly; never `git add .`.
- **Terminals:** always use the run-in-terminal tool — never print commands as
  plain text in chat.
- **Shared code:** `templates/invoice.html` is used by BOTH branches. When round 1
  is finalized on `client-web-app`, **port the same changes to `main`** and tick
  the boxes in `client-revisions-round-1.md` § 5.
- **Docs in English**, conversation with Data in Serbian/Bosnian.

---

## 🌱 GIT STATE (end of session)

- Branch: `client-web-app` — up to date with `origin`.
- Last commit: `15cfca9` — *"docs: add client revisions tracking (round 1) +
  ignore client photos in data/"* (2 files: `client-revisions-round-1.md` new,
  `.gitignore` modified).
- Working tree clean except local/ignored files.
- Previous session log: `captains-log-stardate-20260523.md` (Phase 5 deploy).

---

## ⏭️ NEXT STEP

**Begin implementation with change #1** (company name reorder in
`templates/invoice.html`). Announce it, wait for Data's "nastavi", then edit →
test → commit. Proceed through the work order above.

---

*Logged by Spock · Mission Specialist: Lieutenant Commander Data (zvuk1T) · Stardate 20260620*
