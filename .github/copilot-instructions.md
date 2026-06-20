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

## 🌿 Branch Structure — Single Branch (`main`)
- **`main` is the only branch.** It holds *everything*: the local pipeline
  (`python main.py` → PDFs) **and** the Flask web app (`app.py` → Render.com).
- **Render deploys from `main`.** Every push to `main` redeploys the live app.
- **No porting between branches.** With one branch there is no "apply the fix to
  the other branch too" — a single commit updates both the local and web paths,
  since they share the same files (e.g. `templates/invoice.html`).
- **History:** the project briefly used a two-branch model (`main` +
  `client-web-app`). It was consolidated into a single `main` on Stardate 20260620
  because the split added complexity with no benefit for a solo developer. Full
  story + reusable playbook: `guides/git-branch-consolidation.md`.

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