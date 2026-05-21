import pandas as pd

# -------------------------------------------
# EXCEL UTILITIES
# This file contains all operations we perform
# on the Excel data file:
# - Rename column headers to English names
# - (future) validate data
# - (future) filter rows by month/period
# -------------------------------------------

INPUT_FILE = "data/stan_na_dan_klijenti_racuni.xlsx"
SHEET_NAME = "Sheet2"

# Mapping: old Serbian name → new English name
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

# Read the Excel file
df = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)

# Show columns before renaming
print("Columns BEFORE rename:")
print(list(df.columns))

# Rename columns
df.rename(columns=COLUMN_RENAME_MAP, inplace=True)

# Show columns after renaming
print("\nColumns AFTER rename:")
print(list(df.columns))

# Save back to the same file, same sheet
with pd.ExcelWriter(INPUT_FILE, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name=SHEET_NAME, index=False)

print("\nDone. File saved successfully.")
