# 📚 GIT BEST PRACTICES — Learning Book
## Lieutenant Commander Data & Science Officer Spock
### Invoice Automation Project — Started: 02.05.2026

---

> *"The more you learn, the more you understand. The more you understand, the less you fear."*
> — Science Officer Spock

---

## 🌱 BASICS — Setting Up Git

### Initialize a Git repository
```bash
git init
```
- `git init` → "Reci laptopu: ovaj folder sada prati historiju promjena" 📁
- Kreira skriveni `.git` folder — tu živi cijela historija projekta
- Radi se **samo jednom** po projektu

---

### Rename initial branch from master to main
```bash
git branch -m master main
```
- `git branch -m master main` → "Preimenuj branch kao što preimenujemo folder" 🏷️
- **Zašto:** `main` je moderni standard (GitHub koristi `main` od 2020.)
- `master` je zastarjeli naziv — izbjegavaj ga u novim projektima

---

### Check which branch you are on
```bash
git branch
```
- `git branch` → "Pokaži mi koji branch koristim" 👀
- Zvjezdica `*` pokazuje aktivni branch

---

## 📦 DAILY WORKFLOW — Snimanje promjena

### Stage all changes
```bash
git add .
```
- `git add .` → "Složi SVE izmijenjene fajlove u kutiju, pripremi za snimanje" 📦
- Tačka `.` znači "sve u trenutnom folderu"
- Možeš dodati i jedan fajl: `git add main.py`

---

### Commit — snimi promjene
```bash
git commit -m "Kratka poruka o tome šta si uradio"
```
- `git commit -m "..."` → "Zatvori kutiju i nalijepi natpis" 🏷️
- `-m` znači "message" — poruka koja opisuje šta si uradio
- **Dobra poruka:** `"Add invoice HTML template"`
- **Loša poruka:** `"changes"` ili `"fix"`

---

### When to commit — the professional standard

**One commit = one logical unit of work.** 🎯

Not "one commit per day". Not "commit every small change". When you finish something that works — commit it.

| ✅ Good commit | ❌ Bad commit |
|---|---|
| `"Add invoice HTML template"` | `"work in progress"` |
| `"Fix PDF export for special characters"` | `"changes"` |
| `"Update gitignore and requirements"` | `"various stuff"` |

**Why this matters:**
- If something breaks, you can go back to exactly the right point 🔙
- Git history becomes readable — you see *what* was done and *why*
- Other developers (or future you) can understand the project

**Mental model:**
```
Commit = checkpoint in a video game 🎮
Too few checkpoints → lose a lot of progress when you die
Too many checkpoints → meaningless saves every 5 seconds
Right amount → one checkpoint per completed level
```

---

### Check status — vidi šta je izmijenjeno
```bash
git status
```
- `git status` → "Pokaži mi šta je izmijenjeno a nije još snimljeno" 🔍
- `nothing to commit` = sve je snimljeno ✅
- Zeleni fajlovi = staged (u kutiji, spremni za commit)
- Crveni fajlovi = unstaged (izmijenjeni ali nisu u kutiji)

---

## 🌐 GITHUB — Slanje na internet

### Connect local repo to GitHub
```bash
git remote add origin https://github.com/USERNAME/REPO-NAME.git
```
- `git remote add origin` → "Povezi moj lokalni projekat sa GitHub adresom" 🌐
- `origin` je naziv za GitHub vezu (standardni naziv)
- Radi se **samo jednom** po projektu

---

### Push — pošalji na GitHub
```bash
git push -u origin main
```
- `git push` → "Pošalji sve commitove na GitHub" 🚀
- `-u origin main` → "Zapamti da uvijek šaljem na `main` branch"
- Nakon prvog puta, dovoljno je samo: `git push`

---

### Pull — preuzmi promjene sa GitHub-a
```bash
git pull
```
- `git pull` → "Preuzmi najnovije promjene sa GitHub-a na laptop" ⬇️
- Korisno kada radiš na više računara ili u timu

---

## 🔍 PREGLED HISTORIJE

### Vidi historiju commitova
```bash
git log --oneline
```
- `git log --oneline` → "Pokaži mi sve checkpointe u jednoj liniji" 📜
- Svaki red = jedan commit sa ID-om i porukom

---

## ⚡ CHAINED COMMANDS — Više komandi u jednoj liniji

### What is `&&`?
`&&` → "Uradi ovo, a ako uspije — uradi sljedeće" 🔗

If the first command fails, the rest **will not run**. This is a safety mechanism.

---

### Commit and push a specific file
```bash
git add path/to/file.md && git commit -m "your message" && git push
```

**What each part does:**
- `git add path/to/file.md` → "Stavi samo ovaj jedan fajl u kutiju" 📦
- `&&` → "Ako to uspije, nastavi"
- `git commit -m "your message"` → "Zatvori kutiju i nalijepi natpis" 🏷️
- `&&` → "Ako to uspije, nastavi"
- `git push` → "Pošalji na GitHub" 🚀

**Real example from this project:**
```bash
git add .github/copilot-instructions.md && git commit -m "chore: add Spock voice definition to Identity section" && git push
```

**When to use specific file vs. `git add .`:**
- `git add .` → when you want to commit ALL changed files
- `git add specific/file.md` → when you want to commit only ONE file, and leave others for later

---

## ⚠️ ČESTI PROBLEMI I RJEŠENJA

*(Ovo popunjavamo kada naiđemo na probleme)*

---

## 🧠 MASTER MENTAL MODEL

```
Laptop (lokalno)          GitHub (internet)
─────────────────         ─────────────────
git init                → Pripremi folder za praćenje
git add .               → Složi u kutiju
git commit -m "..."     → Zatvori i nalijepi natpis
git push                → Pošalji kutiju u biblioteku 🚀
git pull                → Preuzmi iz biblioteke na laptop ⬇️
```

---

*Fajl se ažurira tokom projekta — svaki novi problem i rješenje se dodaje ovdje.*
