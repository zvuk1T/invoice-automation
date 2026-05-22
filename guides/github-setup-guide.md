# 🚀 GITHUB SETUP GUIDE
## How to Set Up a GitHub Repository Using GitHub CLI (gh)
### Lieutenant Commander Data & Science Officer Spock
### Created: 02.05.2026

---

## 🧠 Mental Model — Before We Start

```
GitHub CLI (gh)  →  "A remote control for GitHub — everything done from the terminal" 🎮
git              →  "A local diary of changes on your laptop" 📓
GitHub           →  "An online library where we store a copy of our project" 🌐

Data flow:
Laptop (git) ──── git push ────► GitHub (cloud)
Laptop (git) ◄─── git pull ──── GitHub (cloud)
```

---

## 📋 PREREQUISITES

Before following this guide, make sure:
- [ ] `git init` — local repository initialized
- [ ] At least one `git commit` — something exists to push
- [ ] GitHub account created at github.com

---

## 🛠️ STEP 1 — Install GitHub CLI

### What is GitHub CLI?
GitHub CLI (`gh`) is a tool that lets you manage GitHub directly from the terminal — no browser needed.

### Install on macOS:
```bash
brew install gh
```

**What this command does:**
- `brew` → Homebrew, the macOS package manager (like an App Store for the terminal)
- `install gh` → installs the GitHub CLI tool

**Expected output:**
```
==> Installing gh
✅ gh installed successfully
```

> **Note:** If `brew` is not found, see Troubleshooting → Problem 1 below.

---

## 🔑 STEP 2 — Log In to GitHub

```bash
gh auth login
```

**What this command does:**
- Opens an interactive login process
- Asks a few questions — answer as shown below

**Answers to the prompts:**
```
? Where do you use GitHub?            → GitHub.com
? What is your preferred protocol?    → HTTPS
? Authenticate Git with credentials?  → Yes
? How would you like to authenticate? → Login with a web browser
```

A one-time code appears in the terminal → browser opens → enter the code → confirm → return to terminal.

**Verify that you are logged in:**
```bash
gh auth status
```
Expected: `Logged in to github.com as YOUR_USERNAME`

> **Note:** If you see a `permission denied` error, see Troubleshooting → Problem 3 below.

---

## 🏗️ STEP 3 — Create the GitHub Repository

```bash
gh repo create invoice-automation --public --source=. --remote=origin --push
```

**What each option means:**
- `gh repo create` → "Create a new repo on GitHub" 🏗️
- `invoice-automation` → the name of the repository on GitHub
- `--public` → visible to everyone (great for portfolio!)
- `--source=.` → use the current folder as the source
- `--remote=origin` → connect the local repo to GitHub (the connection is named "origin")
- `--push` → immediately send all commits to GitHub

**Alternative:** Use `--private` instead of `--public` if you don't want the repo to be public.

**Expected output:**
```
✓ Created repository YOUR_USERNAME/invoice-automation on GitHub
✓ Added remote origin
✓ Pushed commits to github.com/YOUR_USERNAME/invoice-automation
```

---

## ✅ STEP 4 — Verify

```bash
gh repo view --web
```

**What this command does:**
- Opens your GitHub repository directly in the browser 🌐
- You can immediately see all files on GitHub

---

## 🔄 DAILY WORKFLOW (after setup)

```bash
# 1. Stage all changed files
git add .

# 2. Save changes locally with a message
git commit -m "Describe what you did"

# 3. Send to GitHub
git push
```

---

## ⚠️ TROUBLESHOOTING — Real Problems We Encountered

### Problem 1: `brew: command not found`
**Cause:** Homebrew is not installed on macOS.
**Solution:** Install Homebrew first:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

### Problem 2: `gh: command not found` after installation
**Cause:** The terminal session was not refreshed after installation.
**Solution:** Close and reopen the terminal, then try again.

---

### Problem 3: `mkdir ~/.config/gh: permission denied`
**When it happens:** After `gh auth login` — authentication completes but this error appears.

**Cause:** The `.config` folder is owned by `root`, not your user account.

**Check who owns the folder:**
```bash
ls -la /Users/YOUR_USERNAME/.config/
```
If it shows `root` instead of your username — that is the cause.

**Solution:**
```bash
sudo chown -R YOUR_USERNAME /Users/YOUR_USERNAME/.config
```
- `sudo` → run as administrator
- `chown -R` → change owner recursively (including all subfolders)
- Then repeat `gh auth login`

**What we learned:** Always check folder ownership when you see `permission denied`.

---

### Problem 4: A folder or file was accidentally pushed to GitHub
**When it happens:** You forgot to add the folder to `.gitignore` before the first push.

**Solution — 3 steps:**

**Step 1:** Add to `.gitignore`:
```
folder_name/
```

**Step 2:** Remove from Git tracking (files stay on your laptop!):
```bash
git rm -r --cached folder_name/
```
- `--cached` → removes from Git only, does NOT delete from laptop 🔒

**Step 3:** Commit and push:
```bash
git add . && git commit -m "Remove folder_name from GitHub" && git push
```

**What we learned:** Always set up `.gitignore` before the first push. Fix it immediately if you forget.

---

## 🧠 MASTER MENTAL MODEL

```
brew install gh          →  "Install the remote control"                    🎮
gh auth login            →  "Log in to GitHub from the terminal"            🔑
gh auth status           →  "Check if you are logged in"                    👀
gh repo create ...       →  "Create a repo and push everything at once"     🚀
git push                 →  "Send new commits to GitHub"                    📤
gh repo view --web       →  "Open the repo in the browser and verify"       🌐
git rm --cached folder/  →  "Remove folder from GitHub, keep it locally"    🗑️
sudo chown -R user path  →  "Fix ownership — take back control of a folder" 🔧
```

---

*Guide created: 02.05.2026 | Project: invoice-automation*
*Based on real experience — all problems in Troubleshooting were actually encountered during setup.*
