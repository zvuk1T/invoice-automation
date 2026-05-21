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
"""
pd.ExcelWriter opens the file. We write to it, then it automatically
saves and closes when we exit the "with" block.
"""
with pd.ExcelWriter(INPUT_FILE, engine="openpyxl") as writer: 
    df.to_excel(writer, sheet_name=SHEET_NAME, index=False)

print("\nDone. File saved successfully.")


# -------------------------------------------
# FUNCTION: update_from_pdf_data
# -------------------------------------------

def update_from_pdf_data(pdf_records):
    """
    Takes a list of records extracted from PDFs
    and updates the matching rows in the Excel file.

    Matching is done by contract_number.
    Updated columns: date, period, invoice_number, fiscal_number, amount

    Prints a report of what was updated, what was skipped, and what was not found.
    """
    # Read the current Excel file
    df = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)

    # Convert contract_number column to string for safe comparison
    # (Excel stores numbers as int, PDF extracts them as string)
    # lstrip("0") removes leading zeros so "0120" == "120"
    df["contract_number"] = df["contract_number"].astype(str).str.strip().str.rstrip(".").str.lstrip("0")

    # Convert monthly columns to object type so they can hold text values
    # (they are float64 when empty in Excel)
    for col in ["date", "period", "invoice_number", "fiscal_number", "amount"]:
        df[col] = df[col].astype(object)

    updated = []
    not_found = []

    for record in pdf_records:
        contract = str(record.get("contract_number", "")).strip().rstrip(".").lstrip("0")

        # Find the matching row in Excel
        mask = df["contract_number"] == contract

        if mask.any():
            # Update the 5 monthly columns
            df.loc[mask, "date"]           = record.get("date")
            df.loc[mask, "period"]         = record.get("period")
            df.loc[mask, "invoice_number"] = record.get("invoice_number")
            df.loc[mask, "fiscal_number"]  = record.get("fiscal_number")
            df.loc[mask, "amount"]         = record.get("amount")
            updated.append(contract)
        else:
            not_found.append(f"{contract} ({record.get('source_file', '?')})")

    # Save the updated Excel file
    with pd.ExcelWriter(INPUT_FILE, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name=SHEET_NAME, index=False)

    # Report
    print(f"\n✅ Updated:   {len(updated)} rows")
    if not_found:
        print(f"⚠️  Not found in Excel: {len(not_found)} records")
        for item in not_found:
            print(f"   - contract_number: {item}")
    else:
        print("✅ All records matched successfully.")

    return df


# -------------------------------------------
# RUN AS STANDALONE TEST
# -------------------------------------------
if __name__ == "__main__":
    from pdf_extractor import extract_all_pdfs

    FOLDER = "data/APRIL 2026"
    print(f"Extracting data from PDFs in '{FOLDER}'...")
    pdf_records = extract_all_pdfs(FOLDER)

    print("\nUpdating Excel file...")
    update_from_pdf_data(pdf_records)
    print("\nExcel file updated successfully.")
