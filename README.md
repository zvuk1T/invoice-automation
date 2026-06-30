# 📄 Business Document Automation Tool

> A Python/Flask web application that transforms structured business data into ready-to-use PDF documents through an automated digital workflow.

---

## 🎯 Project Purpose

This project demonstrates how repetitive document generation in a small business environment can be automated by converting structured input data into standardized PDF documents.

The application provides a simple web interface for uploading structured business data and downloading generated PDF documents as a ZIP archive.

Built as a learning project and real-world automation tool for a small real estate business.

---

## 💼 Business Context

Small businesses often spend significant time preparing repetitive administrative documents manually. This creates unnecessary operational friction, increases the chance of errors, and makes recurring office processes harder to scale.

This project turns that workflow into a repeatable digital process:

```text
structured business data → HTML/CSS template → PDF documents → ZIP download
```

The goal is not only to generate documents, but to show how practical automation can support business efficiency, data-driven digital transformation, and better internal workflows.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Automation, application logic and data processing |
| pandas | Reading structured tabular input data |
| Jinja2 | Rendering business data into HTML templates |
| WeasyPrint | Converting HTML/CSS templates into PDF documents |
| Flask | Web application layer — upload data, download generated documents |
| Render.com | Cloud hosting of the web application |

---

## 🗂️ Project Structure

```text
invoice-automation/
├── data/            ← Local input data folder, ignored for privacy
├── templates/       ← HTML/CSS templates and upload page
├── output/          ← Generated PDF files, ignored by Git
├── main.py          ← Local pipeline: structured data → PDF documents
├── app.py           ← Flask web app: upload input data → download ZIP
├── build.sh         ← Render.com build script, installs WeasyPrint system libraries
├── render.yaml      ← Render.com deployment configuration
├── requirements.txt ← Python dependencies
└── .github/         ← Project guides and development instructions
```

---

## 🚀 Current Status

- [x] Project structure created
- [x] HTML/CSS document template
- [x] Python data-loading and document-generation pipeline
- [x] PDF generation with WeasyPrint
- [x] Flask web application deployed on Render.com
- [x] ZIP download workflow
- [x] Branded upload page
- [x] Render.com deployment files (`build.sh`, `render.yaml`)
- [ ] Packaging as `.exe` for local desktop use (future option)

---

## 🌐 Deployment

- **Local pipeline:** `python main.py` — generates PDF documents locally in `output/`
- **Web app:** Flask app (`app.py`) — upload structured input data, download ZIP with generated PDFs
- **Cloud:** Render.com — auto-deploys from `main`
- **Live URL:** https://e-agency-invoice-automation.onrender.com

---

## 🧭 Architecture — Single `main` Branch

One branch holds both workflows:

1. The local pipeline (`main.py`) for local document generation.
2. The Flask web app (`app.py`) for browser-based upload and ZIP download.

Both workflows reuse the same template logic, so one template update affects both local and web-based generation.

**History:** the project briefly used two branches (`main` + `client-web-app`). For a solo developer, that split created extra porting work without practical benefit, so the branches were consolidated into a single `main` branch. The full reasoning is documented in `guides/git-branch-consolidation.md`.

---

## 🐛 Problems Solved

| Problem | Solution |
|---------|----------|
| PDF generation required system libraries not available on Render.com by default | Added `build.sh` to install required WeasyPrint dependencies such as pango, cairo, libffi and libjpeg |
| Browser uploads send file-like objects instead of local file paths | Reused the same data-loading logic because pandas can handle both local paths and in-memory file objects |
| Render.com free tier has an ephemeral filesystem | Switched the web app workflow to in-memory PDF and ZIP generation using `BytesIO` |
| Public repository must not expose real business or client data | Added `.gitignore` rules for local data, generated files and private assets |

---

## 🔒 Privacy Note

This public repository is intended as a portfolio and learning project. Real client data, generated business documents and private assets are excluded from version control.

The public code demonstrates the workflow and architecture, while sensitive operational data remains local/private.

---

## 🧠 What This Project Demonstrates

- Data-driven workflow automation
- Business process digitalization
- Structured data processing with Python
- Template-based document generation
- Flask web application development
- In-memory file processing for cloud deployment
- Practical small-business digital transformation

---

## 📝 Guides & Mission Protocol

- `.github/copilot-instructions.md` — Spock & Data mission protocol, session rules
- `guides/git-best-practices.md` — branching, commits, push workflow and mental models
- `captains-log/` — session logs, what/why/next

---

## 🖖 Mission Statement

*All sessions are a collaborative mission: Spock (mentor) and Data (student) work together to boldly go where no one has gone before.*
