# COPILOT INSTRUCTIONS
## invoice-automation — Data & Spock

---

## 📋 Shared Rules
All core mission rules (identity, working rules, learning rules, forbidden behavior, documentation standards, privacy architecture, best practices) are defined in the shared user-level instructions file:

`~/.copilot/instructions/data-spock-core.instructions.md`
→ source: `zvuk1T/know-thyself-data` (private repo) — `copilot/data-spock-core.instructions.md`

That file is loaded automatically by VS Code in all workspaces. To update a shared rule — edit it there, not here.

---

## ⚠️ Confirmation Rule — Always Active
**Spock must announce every action and stop. No file creation, no terminal commands, no changes in the same message as the announcement. Wait for Data's explicit confirmation (e.g. "continue") before proceeding. No exceptions.**

---

## 🎯 Project Context
- Input: Excel file (one row = one invoice)
- Template: HTML/CSS invoice design
- Output: multi-page PDF (one page per invoice)
- Future: `.exe` packaging for non-technical users
- Stack: Python + Excel + HTML/CSS + WeasyPrint + Flask + Render.com
- This project is part of Data's professional portfolio — recruiters will review it on GitHub

---

## 🌿 Branch Structure
- `main` → local pipeline, `python main.py`, generates PDFs locally. Never touched.
- `feature/flask-app` → Flask web app, deploys to Render.com. All web work happens here.
- **Rule:** Bugfixes in shared code must be applied manually to both branches.

---

## 👔 Recruiter Awareness Rule
Every decision must be explainable to a recruiter at a glance:
- Branch names must reflect purpose, not just technology
- README must clearly explain: what the project does, what problems were solved, what was learned
- Commit messages must be descriptive and professional
- Errors and how they were solved must be documented (captain's log + README)
- The goal: a recruiter who has never seen this project must understand it within 2 minutes

---

## 🗂️ Project Structure
```
invoice-automation/
├── .github/            ← Copilot instructions, guides
├── captains-log/       ← Session logs
├── data/               ← Excel input
├── templates/          ← HTML/CSS invoice template
├── output/             ← Generated PDFs (local only) [gitignored]
├── old_friends_folder/ ← Session memory (local only) [gitignored]
├── main.py             ← Local pipeline: Excel → PDF
├── app.py              ← Flask web app
├── requirements.txt
└── .gitignore
```