# 📝 CLIENT REVISIONS — ROUND 1
## Project: Invoice Automation Tool
### Tracking document for client-requested changes (start → finish)

> **Branch:** `main` (single-branch model — consolidated Stardate 20260620)
> **Started:** Stardate 20260620
> **Status:** 🟡 In progress — change #1 done; #2–#7 pending
> **Type:** Mostly aesthetic (design/layout) changes requested by the client

---

## 🎯 1. GOAL & CONTEXT

The web app is **live and working** (Phase 5 complete): the client uploads an
Excel file (one row = one invoice) and downloads a ZIP of generated PDF invoices.

The client has reviewed the result and requested a set of changes — **mostly
aesthetic** (colors, spacing, layout, text). This document tracks every change
from request to completion, so nothing is lost across multiple work sessions.

**Why a separate file (not just the captain's log)?**
Client revisions span multiple sessions. A dedicated tracking file keeps the
full plan, the change list, and the status of each item in **one place** —
instead of scattered across daily logs. The captain's log still records each
session and references this file.

---

## 🗺️ 2. ARCHITECTURE MAP — what affects what

Before touching anything, we know where each change "lives" and what it can break.

| File | Controls | Risk | Affects |
|---|---|---|---|
| `templates/invoice.html` | **Invoice appearance** (CSS + layout) | 🟢 Low | **Both paths** (local `main.py` + web `app.py`) |
| `templates/upload.html` | Web upload page appearance | 🟢 Low | Web app only |
| `templates/assets/` | Logo, stamp, signature images | 🟢 Low | Both paths |
| `app.py` | Web logic (upload → ZIP) | 🟠 Medium | Web app only |
| `main.py` | Pipeline (Excel → PDF) | 🔴 High | Local path only |

**Key insight:** Since the changes are mostly aesthetic, almost everything will
happen in `templates/invoice.html` — the **lowest-risk file** (presentation only,
no logic). We can safely change colors, spacing, fonts, layout, and text without
risking the PDF generation. Because we use a **single `main` branch**, one edit to
`invoice.html` updates both the local and web paths at once — no porting needed.

---

## 🔧 3. WORK PROCESS — how we handle client changes

A standard, professional process (also looks good to a recruiter):

1. **📝 Collect ALL changes first.** Don't work blindly one-by-one. Get the full
   list — so we can spot conflicts and avoid duplicate work.
2. **🏷️ Categorize each change** — aesthetic (CSS/text) vs functional (logic).
   This tells us the risk of each immediately.
3. **🔍 Assess impact** — where it lives, what it touches, what could break
   (use the architecture map above).
4. **✏️ Work one at a time, in order** — from easiest/safest to most complex.
5. **🧪 Test after each change** — generate the PDF locally, verify visually,
   then move on.
6. **💾 Commit after each logical change** — descriptive message (recruiter rule).
7. **🔄 At the end:** record the final summary in the captain's log. (No branch
   porting — single `main` branch means each commit already updates both paths.)

---

## 📋 4. CHANGE LIST

> Filled in once the client's full list is provided.
> **Type:** Aesthetic = CSS/text/layout · Functional = logic/data
> **Risk:** 🟢 Low · 🟠 Medium · 🔴 High
> **Status:** ⬜ To do · 🔄 In progress · ✅ Done · ❌ Cancelled

| # | Change | Type | Risk | File(s) | Status | Notes |
|---|---|---|---|---|---|---|
| 1 | Company name reorder → `e-agency s.p. LJUBINKA Vuković` | Aesthetic (text) | 🟢 Low | `invoice.html` | ✅ | Was `e-agency LJUBINKA Vuković s.p.` — moved `s.p.` to right after `e-agency`. Implemented + committed (`ec41192`). Visual PDF test still pending. |
| 2 | Bold the company details block (address / JIB / bank) | Aesthetic (CSS) | 🟢 Low | `invoice.html` | ⬜ | Client wrote *"boldovati"* on the framed block — make text more visible. `.company-details` → heavier `font-weight`. |
| 3 | Meta row background: pale pink → light gray | Aesthetic (CSS) | 🟢 Low | `invoice.html` | ⬜ | `.meta-row` uses `--primary-light` (#f9f0f3). Client dislikes the pinkish tone — switch to a light gray of similar lightness. |
| 4a | Table: add **"Obračunski period"** label | Aesthetic (text) | 🟢 Low | `invoice.html` | ⬜ | Period column. **Interpretation: rename `PERIOD` header → `OBRAČUNSKI PERIOD` — verify exact wording/placement with client.** |
| 4b | Table: round the corners (like Total box & meta row) | Aesthetic (CSS) | 🟢 Low | `invoice.html` | ⬜ | Table header has sharp corners (the diagonal marks) — add `border-radius`. **Colors stay the same — bordo NOT touched** (old "gray header" idea = cancelled). |
| 5 | Outline lines → neutral gray (~50% black) | Aesthetic (CSS) | 🟢 Low | `invoice.html` | ⬜ | Client wanted bordo lines; **we propose gray** for outline/structural lines (`--border`, note & footer borders) so bordo stays reserved for fills/accents. ⚠️ Joint decision — to confirm with client. |
| 6 | Amount `23,40` — no change | — | — | — | ✅ | Client circled it as *"good as-is"*. No action needed. |
| 7 | Signature / stamp block redesign | Aesthetic (layout) | 🟠 Medium | `invoice.html` | ⬜ | Order: *"S poštovanjem,"* → handwritten signature → underline → **"LJUBINKA Vuković"** in bordo, uppercase. Also better center & proportion the stamp + signature. |

---

## ✅ 5. SHARED CODE — now handled by the single-branch model

`templates/invoice.html` is **shared code** — used by both `main.py` (local) and
`app.py` (web). Previously the project had two branches, so every shared-code
change had to be **manually ported** between them.

**This is no longer a concern.** On Stardate 20260620 the project was consolidated
into a **single `main` branch** (full story: `guides/git-branch-consolidation.md`).
Now one commit to `invoice.html` updates both the local and web paths at once —
there is nothing to port.

- [x] Invoice changes reach both paths automatically (single `main` branch)
- [x] Captain's log updated (consolidation documented — PART 3, Stardate 20260620)

---

## 📅 6. PROGRESS JOURNAL

Short, dated references to each session (no duplication — details live above).

| Stardate | Session summary |
|---|---|
| 20260620 | Created this tracking document. Gathered full project context. Defined architecture map + work process. **Captured 7 client changes** from the annotated invoice photo (`data/IMG-20260620-WA0003.jpg`) and filled in the change list. Implementation not yet started. |
| 20260620 | **Implemented change #1** (company name reorder), committed `ec41192`. **Consolidated the two branches (`main` + `client-web-app`) into a single `main`** — Render now deploys from `main`, old branch deleted. Updated this file to the single-branch model (header, architecture map, work process, § 5). |

---

*Document created by Spock · Mission Specialist: Lieutenant Commander Data (zvuk1T)*
