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
| Excel (.xlsx) | Input data source |
| HTML/CSS | Invoice template design |
| PDF library | Output generation |

---

## 🗂️ Project Structure

```
invoice-automation/
├── data/           ← Excel input file
├── templates/      ← HTML/CSS invoice template
├── output/         ← Generated PDF files
├── main.py         ← Main script
├── requirements.txt← Python dependencies
└── .github/        ← Project guides and instructions
```

---

## 🚀 Status

- [x] Project structure created
- [x] HTML invoice template
- [x] Python + Excel integration
- [x] PDF generation (WeasyPrint)
- [x] Flask web app (Phase 5, branch: feature/flask-app)
- [x] Combined PDF generation
- [x] Branded upload page (upload.html)
- [x] Render.com deployment files (`build.sh`, `render.yaml`)
- [ ] Packaging as `.exe` (future)

---

## 🌐 Deployment

- **Local:** `python main.py` — generates PDFs in `output/`
- **Web app:** Flask app (`app.py`) — upload Excel, download ZIP with PDFs
- **Cloud:** Render.com (free tier) — auto-deploys from `feature/flask-app` branch

---

## 🧭 Branching Strategy

- `main` — lokalna verzija, pokreće se s `python main.py`, generiše PDFove
- `feature/flask-app` — web app verzija, deploya na Render.com

---

## 📝 Guides & Mission Protocol

- `.github/copilot-instructions.md` — Spock & Data mission protocol, session rules
- `guides/git-best-practices.md` — branching, commit, push, mental modeli
- `captains-log/` — session logs, what/why/next

---

## 🖖 Mission Statement

*All sessions are a collaborative mission: Spock (mentor) and Data (student) work together to boldly go where no one has gone before.*

---
