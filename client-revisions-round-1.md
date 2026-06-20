# 📝 CLIENT REVISIONS — ROUND 1
## Project: Invoice Automation Tool
### Tracking document for client-requested changes (start → finish)

> **Branch:** `main` (single-branch model — consolidated Stardate 20260620)
> **Started:** Stardate 20260620
> **Status:** � Round 1 implemented — all changes **committed + pushed**. Awaiting client's round-2 feedback.
> **Type:** Mostly aesthetic (design/layout) changes requested by the client

---

## ⏭️ RESUME HERE — next-session quick start (Stardate 20260620, PART 5)

> This block is the **first thing to read** when resuming. It supersedes older status
> lines. Full session story: captain's log `captains-log-stardate-20260620.md` **PART 5**.

**State of the work:** Round 1 is **DONE, committed, and pushed.** All of the client's
requested changes (#2–#7) plus the color/text design pass are live in `templates/invoice.html`.
The signature/stamp footer was nudged **+3cm lower** per Data's explicit instruction
(`.footer { margin-top: 3cm }`). The invoice was sent to the client for review.

**⚠️ Important lesson from this session (do not repeat):** Spock went off-brief and
spent a long, token-heavy detour redesigning the **vertical proportions** (sticky footer,
`position:fixed`, centering, flex space-between) — something the client **never asked for**.
It broke a layout the client was already happy with. It was fully **reverted**. The only
proportion change kept is Data's simple, explicit one: footer +3cm. **Rule reinforced:
do exactly what the client's notes say — colors and text — and nothing more. Do not invent
design problems.**

**What we are waiting for:** the client (Ljubinka) will likely respond tomorrow with
round-2 feedback. Her annotated photo (`data/IMG-20260620-WA0003.jpg`) raised two of her
**own questions** that only she can answer:
- Table header color: **"tamno siva ili crvena???"** → **DECIDED with Data: keep her bordo
  header** (no change needed).
- "tamno crvena kao gornja" referred to the **divider line we already deleted** → moot,
  nothing to color.

**First move next session:** read the client's new message, add any new requests as
**round-2** rows in the change list below, then implement (colors/text only unless she
explicitly asks for layout). Regenerate via the venv python, open
`output/2026-05-0004.pdf` (Smilja Tepić — matches her annotated photo) to verify.

**Known pre-existing bug (NOT part of design — do not fix inside a design commit):**
`main.py` writes several `output/nan.pdf` files that overwrite each other (rows with
missing invoice numbers). Park on a future "fixes" list.

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
| 2 | Bold the company details block (address / JIB / bank) | Aesthetic (CSS) | 🟢 Low | `invoice.html` | ✅ | **Done + committed.** `.company-details` → `font-weight: 800` (bumped per Data's "+33%"). |
| 3 | Meta row background: pale pink → light gray | Aesthetic (CSS) | 🟢 Low | `invoice.html` | ✅ | **Done + committed.** `.meta-row` now uses `--surface` (light gray) instead of the pinkish `--primary-light`. |
| 4a | Table: add **"Obračunski period"** label | Aesthetic (text) | 🟢 Low | `invoice.html` | ✅ | **Done + committed.** `PERIOD` header → `Obračunski period`. ⚠️ Confirm exact wording/placement with client. |
| 4b | Table: round the corners (like Total box & meta row) | Aesthetic (CSS) | 🟢 Low | `invoice.html` | ✅ | **Done + committed.** Full rounded "card" (all 4 corners). CSS gotcha solved: `border-collapse: separate` + `border-spacing: 0` + `overflow: hidden` (collapse ignores `border-radius`). Bordo untouched. |
| 5 | Outline lines → neutral gray (~50% black) | Aesthetic (CSS) | 🟢 Low | `invoice.html` | ✅ | **Done + committed.** Structural lines → gray tokens; bordo reserved for fills + the one 3px top line. ⚠️ Joint decision — to confirm with client. |
| 6 | Amount `23,40` — no change | — | — | — | ✅ | Client circled it as *"good as-is"*. No action needed. |
| 7 | Signature / stamp block redesign | Aesthetic (layout) | 🟠 Medium | `invoice.html` | ✅ | **Done + committed.** Order: *"S poštovanjem,"* → signature → underline → **LJUBINKA VUKOVIĆ** (bordo, uppercase). Stamp = floating overlay struck over the signature (rotated −8°, ~0.82 opacity), like a real rubber stamp. Footer nudged **+3cm lower** per Data (`.footer { margin-top: 3cm }`). ⚠️ Our interpretation — client has final say. |

> **⚠️ Open before commit:** the **footer divider line** (see "⏭️ RESUME HERE" → Option A).
> Plus design-system extras done this session but not in the per-change rows above:
> **Tier 1** (design tokens + gray consolidation) and **Zone A** (removed the redundant
> stacked bottom line; note → right-aligned caption). All fold into the same single commit.


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
| 20260620 | **Implemented changes #2–#7** in `templates/invoice.html` (bold details, gray meta row, "Obračunski period", rounded table card, gray outlines, signature/stamp overlay) **plus a design-system pass** — Tier 1 (design tokens + gray consolidation) and Zone A (bottom-line cleanup). **All UNCOMMITTED** (working tree only; `git diff --stat` ≈ 114/79). One open decision before commit: the **footer divider line** (→ Option A). Did web design research ("top shouts, bottom whispers"). Chat got context-heavy (a 408 timeout from an oversized web-fetch) → decided to checkpoint docs and resume in a fresh chat. See captain's log **PART 4** + the "⏭️ RESUME HERE" block above. |
| 20260620 | **Round 1 finalized + committed + pushed.** Detour lesson: Spock went off-brief redesigning **vertical proportions** (sticky footer / `position:fixed` / centering / flex) — never requested, broke a layout the client liked → **fully reverted**. Kept only Data's explicit footer **+3cm** (`.footer { margin-top: 3cm }`). Flipped #2–#7 ⬜→✅, updated header status to 🟢, rewrote the RESUME block to **PART 5**. Invoice sent to client; awaiting round-2 feedback. See captain's log **PART 5**. |

---

*Document created by Spock · Mission Specialist: Lieutenant Commander Data (zvuk1T)*
