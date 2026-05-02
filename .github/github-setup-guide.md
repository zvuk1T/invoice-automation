# 🚀 GITHUB SETUP GUIDE
## Kako postaviti GitHub repo koristeći GitHub CLI (gh)
### Lieutenant Commander Data & Science Officer Spock
### Datum: 02.05.2026

---

## 🧠 Mental Model — prije nego počnemo

```
GitHub CLI (gh)  →  "Daljinski upravljač za GitHub — sve radimo iz terminala" 🎮
git              →  "Lokalni dnevnik promjena na laptopu" 📓
GitHub           →  "Biblioteka na internetu gdje čuvamo kopiju" 🌐

Tok podataka:
Laptop (git) ──── git push ────► GitHub (cloud)
Laptop (git) ◄─── git pull ──── GitHub (cloud)
```

---

## 📋 PREDUSLOVI

Prije ovog vodiča, mora biti završeno:
- [ ] `git init` — lokalni repo inicijalizovan
- [ ] Barem jedan `git commit` — ima šta da se pošalje
- [ ] GitHub nalog kreiran na github.com

---

## 🛠️ KORAK 1 — Instalacija GitHub CLI

### Šta je GitHub CLI?
GitHub CLI (`gh`) je alat koji ti omogućava da upravljaš GitHub-om direktno iz terminala — bez otvaranja browsera.

### Instalacija na macOS:
```bash
brew install gh
```

**Šta ova komanda radi:**
- `brew` → Homebrew, paket menadžer za macOS (kao App Store za terminal)
- `install gh` → instalira GitHub CLI alat

**Očekivani output:**
```
==> Installing gh
✅ gh installed successfully
```

---

## 🔑 KORAK 2 — Prijava na GitHub

```bash
gh auth login
```

**Šta ova komanda radi:**
- Otvara interaktivni proces prijave
- Pitaće te nekoliko pitanja — odgovori kako je opisano ispod

**Odgovori na pitanja:**
```
? Where do you use GitHub?          → GitHub.com
? What is your preferred protocol?  → HTTPS
? How would you like to authenticate? → Login with a web browser
```

Otvori se browser → potvrdi prijavu → vratiš se u terminal.

**Provjera da li si prijavljen:**
```bash
gh auth status
```
Treba pisati: `Logged in to github.com`

---

## 🏗️ KORAK 3 — Kreiranje GitHub repo-a

```bash
gh repo create invoice-automation --public --source=. --remote=origin --push
```

**Objašnjenje svake opcije:**
- `gh repo create` → "Kreiraj novi repo na GitHub-u" 🏗️
- `invoice-automation` → naziv repo-a na GitHub-u
- `--public` → repo je vidljiv svima (portfolio!)
- `--source=.` → koristi trenutni folder kao izvor
- `--remote=origin` → poveži lokalni repo sa GitHub-om (naziv veze = "origin")
- `--push` → odmah pošalji sve commitove na GitHub

**Alternativa `--private`:** Ako ne želiš da repo bude javan, koristi `--private` umjesto `--public`.

**Očekivani output:**
```
✓ Created repository zvuk1T/invoice-automation on GitHub
✓ Added remote origin
✓ Pushed commits to github.com/zvuk1T/invoice-automation
```

---

## ✅ KORAK 4 — Provjera

```bash
gh repo view --web
```

**Šta ova komanda radi:**
- Otvara tvoj GitHub repo direktno u browseru 🌐
- Možeš odmah vidjeti sve fajlove na GitHub-u

---

## 🔄 SVAKODNEVNI WORKFLOW (nakon setup-a)

```bash
# 1. Pripremi fajlove
git add .

# 2. Snimi promjene lokalno
git commit -m "Opis što si uradio"

# 3. Pošalji na GitHub
git push
```

---

## ⚠️ ČESTI PROBLEMI

### Problem: `brew: command not found`
**Uzrok:** Homebrew nije instaliran na macOS-u.
**Rješenje:** Instaliraj Homebrew prvo:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Problem: `gh: command not found` nakon instalacije
**Uzrok:** Terminal nije osvježen.
**Rješenje:** Zatvori i ponovo otvori terminal, pa pokušaj opet.

---

## 🧠 MASTER MENTAL MODEL

```
brew install gh          →  "Instaliraj daljinski upravljač"     🎮
gh auth login            →  "Prijavi se u GitHub iz terminala"   🔑
gh repo create ...       →  "Kreiraj repo i pošalji sve odjednom" 🚀
git push                 →  "Pošalji nove commitove na GitHub"    📤
gh repo view --web       →  "Otvori repo u browseru i provjeri"  👀
```

---

*Vodič kreiran: 02.05.2026 | Projekt: invoice-automation*
