# 🚀 CAPTAIN'S LOG - STARDATE 20260523
## Project: Invoice Automation Tool
### Science Officer: Spock | Mission Specialist: Lieutenant Commander Data (zvuk1T)

---

## 📋 SESSION SUMMARY

**Session Date:** 23.05.2026
**Session Status:** 🔄 In progress — Phase 5 started
**Current Phase:** Phase 5 — Flask Web App (in progress)

---

## ✅ WHAT WE ACCOMPLISHED TODAY

### Decision — Two permanent branches
- **Problem:** Data wanted to preserve the working local version while building the web app.
- **Decision:** Two permanent branches:
  - `main` → local pipeline, `python main.py`, generates PDFs. Never touched.
  - `feature/flask-app` → Flask web app, deploys to Render.com.
- **Trade-off documented:** Bugfixes in shared code (e.g. `main.py`) must be applied manually to both branches.

---

### Branch created — `feature/flask-app`
- Command: `git checkout -b feature/flask-app`
- All Phase 5 work happens here.
- `main` branch remains frozen at Phase 4 state.

---

### Instructions fix — `run_in_terminal` rule clarified
- **Problem:** Spock was printing terminal commands as plain text in chat instead of using the `run_in_terminal` tool (which shows Continue/Cancel to the user).
- **Fix:** Rule #2 in `.github/copilot-instructions.md` updated to explicitly state:
  > ALWAYS use the `run_in_terminal` tool — NEVER print terminal commands as plain text in chat.

---

### `guides/git-best-practices.md` — Branching section added
- New section: **🌿 BRANCHING — Rad s granama**
- Covers: why we use branches, `git checkout -b`, `git branch`, `git push -u origin`, when NOT to merge.
- Includes mental model and example from this project.

---

### `app.py` — Created (not yet tested)
- Flask web server with two routes:
  - `GET /` → serves upload page (`templates/upload.html`)
  - `POST /generate` → receives Excel file, runs pipeline, returns ZIP of PDFs
- Reuses `load_excel_data()` and `render_invoice_html()` from `main.py` — no logic duplicated.
- All PDF generation happens **in memory** (no disk writes on server) — compatible with Render.com free tier.

---

## 🐛 ERRORS ENCOUNTERED AND HOW WE SOLVED THEM

| # | Error | Cause | Solution |
|---|---|---|---|
| 1 | Lint error: `Import "flask" could not be resolved` | Flask not yet installed in venv | Expected — will be resolved in next step (pip install flask) |

---

## ⚠️ KNOWN ISSUE — `load_excel_data()` needs adaptation

`load_excel_data()` in `main.py` currently accepts only a file path (string).
Flask uploads provide a `BytesIO` object (file in memory, no path).
**Next step:** Modify `load_excel_data()` to accept both string path and BytesIO.
This is the only required change to `main.py`.

---

## 📍 WHERE WE STOPPED

- `feature/flask-app` branch created ✅
- `app.py` created ✅
- `load_excel_data()` not yet adapted for BytesIO
- Flask not yet installed
- `templates/upload.html` not yet created

## ⏭️ NEXT STEP

**Step 1 of 6 — Adapt `load_excel_data()` in `main.py`**

Change the function signature so it accepts both:
- `filepath` as a string (local use, `python main.py`)
- `filepath` as a `BytesIO` object (Flask upload)

```python
# The fix is one line — pandas read_excel() already handles both:
df = pd.read_excel(filepath, sheet_name="Sheet2")
# filepath can be a path string OR a BytesIO object — pandas handles both natively.
# Only the type hint / comment needs updating. No logic change needed.
```

**Remaining steps:**
2. Add `flask` to `requirements.txt`
3. Install Flask (`pip install flask`)
4. Create `templates/upload.html`
5. Test locally (`python app.py`)
6. Deploy to Render.com
