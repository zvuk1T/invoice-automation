# 📄 Invoice Automation Tool

> Automatically generate PDF invoices from Excel data using HTML/CSS templates.

---

## 🎯 Project Purpose

This tool reads an Excel file where each row represents one invoice, applies an HTML/CSS template, and generates a multi-page PDF — one page per invoice.

Built as a learning project and real-world automation tool for a real estate agency.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Automation & logic |
| pandas | Read Excel rows into data |
| Jinja2 | Fill the HTML template per invoice |
| WeasyPrint | Render HTML/CSS → PDF |
| Flask | Web app — upload Excel, download ZIP |
| Render.com | Cloud hosting of the web app |

---

## 🗂️ Project Structure

```
invoice-automation/
├── data/           ← Excel input file
├── templates/      ← HTML/CSS invoice template
├── output/         ← Generated PDF files
├── main.py         ← Local pipeline: Excel → PDF
├── app.py          ← Flask web app: upload Excel → download ZIP
├── build.sh        ← Render.com build script (installs WeasyPrint system libs)
├── render.yaml     ← Render.com deployment config
├── requirements.txt← Python dependencies
└── .github/        ← Project guides and instructions
```

---

## 🚀 Status

- [x] Project structure created
- [x] HTML invoice template
- [x] Python + Excel integration
- [x] PDF generation (WeasyPrint)
- [x] Flask web app (Phase 5) — deployed on Render.com
- [x] Combined PDF generation
- [x] Branded upload page (upload.html)
- [x] Render.com deployment files (`build.sh`, `render.yaml`)
- [ ] Packaging as `.exe` (future)

---

## 🌐 Deployment

- **Local:** `python main.py` — generates PDFs in `output/`
- **Web app:** Flask app (`app.py`) — upload Excel, download ZIP with PDFs
- **Cloud:** Render.com (free tier) — auto-deploys from `main`
- **Live URL:** https://e-agency-invoice-automation.onrender.com

---

## 🧭 Architecture — Single `main` Branch

One branch holds everything: the local pipeline (`python main.py` → PDFs in
`output/`) and the Flask web app (`app.py` → deployed on Render.com). They share
the same invoice template, so one edit updates both paths.

**History:** the project briefly used two branches (`main` + `client-web-app`).
For a solo developer that split added porting work with no benefit, so the
branches were consolidated into a single `main` (full story:
`guides/git-branch-consolidation.md`).

---

## 🐛 Problems Solved

| Problem | Solution |
|---------|----------|
| WeasyPrint requires system libraries not available on Render.com by default | Created `build.sh` to install pango, cairo, libffi, libjpeg before pip install |
| `load_excel_data()` accepted only file paths, Flask sends BytesIO objects | Pandas natively handles both — no code change needed, documented the behaviour |
| PDF generation writes to disk — incompatible with Render.com free tier (ephemeral filesystem) | Switched to in-memory PDF generation using `BytesIO`, ZIP returned directly in HTTP response |
| Render.com defaulted to Python 3.14 — potential compatibility risk | Monitored build — no issues found. `.python-version` file available as fallback if needed |

---

## 📝 Guides & Mission Protocol

- `.github/copilot-instructions.md` — Spock & Data mission protocol, session rules
- `guides/git-best-practices.md` — branching, commit, push, mental modeli
- `captains-log/` — session logs, what/why/next

---

## 🖖 Mission Statement

*All sessions are a collaborative mission: Spock (mentor) and Data (student) work together to boldly go where no one has gone before.*

---
