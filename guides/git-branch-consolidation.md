# 🌿 Git Branch Consolidation — Two Branches → One

> **Project:** Invoice Automation Tool · **Stardate:** 20260620
> **In one line:** collapsed a two-branch repo (`main` + `client-web-app`) into a
> single `main` branch — **without taking the live web app offline.**

> 📖 **Want the full educational walkthrough** (mental models, every command
> explained, the reasoning behind each decision)? See the detailed version:
> `know-thyself-data/docs/git-branch-consolidation.md`.

---

## 🎯 The problem

The project had two branches for one solo developer:

| Branch | Job |
|---|---|
| `main` | Local pipeline (`python main.py` → PDFs) |
| `client-web-app` | Flask web app, deployed to Render.com |

Every shared change (e.g. `templates/invoice.html`) had to be **manually copied**
between branches. That is friction with no upside.

**Root cause:** a *false assumption* — "I need a separate branch to run the
pipeline locally." Not true: **any branch can run `main.py`**. Once the assumption
fell, the second branch had no reason to exist.

**Decision:** consolidate to a single `main` branch.

---

## 🔍 Proof before action

No merging or deleting on a hunch. Three checks first:

1. `git log client-web-app..main` → **empty** → `main` had no unique work to lose.
2. `git merge-base --is-ancestor main client-web-app` → **true** → a clean
   fast-forward was possible.
3. `cat render.yaml` → Render was deploying from `client-web-app` → this dictated
   the **order** of every step (repoint the live app *before* deleting anything).

---

## 🪜 The six safe steps

Order chosen so the live app **always** had a valid branch to deploy from:

1. **Commit** the last work on `client-web-app` (`ec41192`).
2. **Fast-forward** `main`: `git merge client-web-app --ff-only` → `main` now has everything.
3. **Repoint** `render.yaml`: `branch: client-web-app` → `branch: main` (`6f938a0`).
4. **Push:** `git push origin main`.
5. **Flip Render** to `main` in the dashboard → **verify "service is live 🎉"** from `6f938a0`.
6. **Delete** the old branch (local + remote) — only after Step 5 proved it was redundant.

> The old branch stayed a safety net until the live app was *proven* to run from
> `main`. No moment of downtime.

---

## 🐛 The gotcha — `git branch -d` vs `-D`

- `git branch -d client-web-app` was **refused**: *"not fully merged."*
- **Why:** `-d` checks if the branch is merged into its **own upstream**
  (`origin/client-web-app`) — *not* into `main`. Our commit was on `main`, so `-d`
  complained even though nothing could be lost.
- **The safe fix:** prove it first, then force.
  ```bash
  git branch -a --contains ec41192   # proof: commit lives on main + origin/main
  git branch -D client-web-app       # force-delete, deliberately, with reason
  ```

---

## ✅ The result

- **One branch: `main`** — runs both the local pipeline and the live web app.
- **Render deploys from `main`** — every push redeploys the site.
- **No more porting** — one commit updates both paths at once.
- **Zero downtime** during the entire migration.

---

*Documented by Spock · Lieutenant Commander Data (zvuk1T) · Stardate 20260620*
