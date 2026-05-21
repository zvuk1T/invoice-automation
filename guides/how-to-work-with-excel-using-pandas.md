# How to Rename Excel Column Headers with Python

## What and Why

When we receive an Excel file with column names in Serbian (e.g. `BR. UGOVORA`, `IME I PREZIME`),
our Python code cannot easily work with those names — they have spaces, special characters, and accents.

**Solution:** Rename all column headers to clean English variable names (e.g. `contract_number`, `owner_name`).
This is done **once** using a Python script. After this, the Excel file is ready to be read by `main.py`.

---

## Libraries Used

| Library | Why |
|---|---|
| `pandas` | Reads Excel into a table in memory, allows easy column renaming |
| `openpyxl` | pandas uses this internally to read/write `.xlsx` files |

Install them (if not already installed):
```bash
source venv/bin/activate
pip install pandas openpyxl
```

---

## The Script: `rename_columns.py`

```python
import pandas as pd

INPUT_FILE = "data/stan_na_dan_klijenti_racuni.xlsx"
SHEET_NAME = "Sheet2"

COLUMN_RENAME_MAP = {
    "BR. UGOVORA":        "contract_number",
    "DATUM POTPISIVANJA": "date",
    "NAZIV OBJEKTA":      "apartment_name",
    "IME I PREZIME":      "owner_name",
    "ADRESA":             "address",
    "OBRAČ. PERIOD":      "period",
    "BR. FAKTURE":        "invoice_number",
    "BR. FISK. RAČUNA":   "fiscal_number",
    "IZNOS (KM)":         "amount",
}

df = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)
df.rename(columns=COLUMN_RENAME_MAP, inplace=True)

with pd.ExcelWriter(INPUT_FILE, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name=SHEET_NAME, index=False)
```

---

## Step-by-Step Explanation

```
pd.read_excel(...)        →  "Load the Excel file into memory as a table"  🧠
df.rename(columns={...})  →  "Replace each old column name with a new one"  ✏️
pd.ExcelWriter(...)       →  "Open the file for writing"  📂
df.to_excel(...)          →  "Save the updated table back to the file"  💾
index=False               →  "Do not add row numbers (0,1,2...) as a column"  🚫
```

---

## How to Run

```bash
source venv/bin/activate
python rename_columns.py
```

**Expected output:**
```
Columns BEFORE rename:
['BR. UGOVORA', 'DATUM POTPISIVANJA', 'NAZIV OBJEKTA', ...]

Columns AFTER rename:
['contract_number', 'date', 'apartment_name', ...]

Done. File saved successfully.
```

---

## Troubleshooting

| Problem | Cause | Solution |
|---|---|---|
| `ModuleNotFoundError: pandas` | pandas not installed, or venv not activated | Run `source venv/bin/activate` first |
| Column not renamed | Old name in map doesn't match exactly | Check for typos, extra spaces, accent characters |
| `PermissionError` | Excel file is open in another program | Close the Excel file, then re-run |

---

## Mental Model

```
Excel file  →  pandas reads it into memory (like copying a table to RAM)  🧠
                        ↓
            rename columns (find & replace on headers only)  ✏️
                        ↓
            write back to disk (overwrite original file)  💾
```

Think of `pandas` as a very smart assistant that can read a spreadsheet, make changes, and save it back — all without you touching the file manually.

---

## Decision Log

- **Why English column names?** Python variable names cannot have spaces or special characters.
  English names make the code readable and avoids encoding issues.
- **Why overwrite the same file?** We are working with a copy in `data/` — the original is kept separately.
- **Why `index=False`?** Without it, pandas adds an extra column (0, 1, 2...) at the start — we don't want that.
