# 📝 CLIENT REVISIONS — ROUNDS 1 & 2
## Project: Invoice Automation Tool
### Tracking document for client-requested changes (start → finish)

> **Branch:** `main` (single-branch model — consolidated Stardate 20260620)
> **Started:** Stardate 20260620
> **Status:** 🟢 Rounds 1 & 2 implemented + verified. Round 1 committed + pushed; Round 2 in the working tree, ready to commit.
> **Type:** Mostly aesthetic (design/layout) changes requested by the client

---

## ⏭️ RESUME HERE — next-session quick start (Stardate 20260621, PART 6)

> This block is the **first thing to read** when resuming. It supersedes older status
> lines. Full session story: captain's logs `...20260620.md` (PART 5) and `...20260621.md`.

**State of the work:** Rounds 1 and 2 are **DONE and verified.** Round 1 (#1–#7 + the
design-system pass) is committed and pushed (`99c89cc`). Round 2 — a second feedback pass
on the masthead/footer/signature — is implemented in `templates/invoice.html` and sits in
the working tree, ready to commit. See the **ROUND 2** section below for the essence.

**What Round 2 changed (essence — exact values live in the code, not here):** the signer
name was aligned to the masthead casing, "air" was added under the brand line with a
matching pull in the footer so the signature stayed put (the "cancellation trick"), and the
stamp was repositioned so it overlaps the signature without covering the printed name.

**Also done this session (Stardate 20260621):** a documentation pass — the inline comments
in `invoice.html` were reframed from change-history ("client asked X on day Y") to
**teaching comments** that explain the technique, so a student could rebuild the file alone.
This is the new **Learning & Understanding hard rule** + **DIKW** principle in action (see
the core instructions and the learning methodology).

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

## 📋 4B. ROUND 2 — second feedback pass

> A second look at the masthead → body → signature flow. All aesthetic, all in
> `templates/invoice.html`. Exact pixel/mm values live in the code comments (the
> KNOWLEDGE layer); this table keeps only the essence (what changed and why).

| # | Change | Why | Technique |
|---|---|---|---|
| R2-1 | Signer name casing aligned to the masthead | The printed name should read the same as the company name up top, not shout in ALL-CAPS | Casing lives in the HTML text (`LJUBINKA Vuković`), not a `text-transform` rule |
| R2-2 | "Air" added under the brand line — without moving the signature | More breathing room below the masthead, but the footer had to keep its vertical position | The **cancellation trick**: space added to `.header { margin-bottom }` is removed in equal measure from `.footer { margin-top }` |
| R2-3 | Stamp repositioned to overlap the signature, not the printed name | A real rubber stamp is struck over the signature, but must not bury the legible name | Negative `top` pulls the stamp up out of normal flow; `calc()` mixes px + mm |

**Verification:** PDF regenerated and reviewed with Data — approved (*"To je to, dobro je"*).
No values changed after approval; only the code comments were later reframed (see PART 6).

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
| 20260621 | **Round 2 implemented + verified** (masthead air + cancellation trick, signer-name casing aligned to masthead, stamp repositioned) — see §4B. **Documentation pass:** reframed `invoice.html` comments from change-history → teaching comments (technique, not iteration trivia); refreshed the README to the single-branch model. Applied the new **Learning & Understanding hard rule** + **DIKW** principle (core instructions + learning methodology). Round 2 + comment pass sit in the working tree, ready to commit. See captain's log `...20260621.md`. |

---

*Document created by Spock · Mission Specialist: Lieutenant Commander Data (zvuk1T)*
