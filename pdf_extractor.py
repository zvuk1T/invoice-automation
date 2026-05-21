import pdfplumber
import re
import os

# -------------------------------------------
# PDF EXTRACTOR
# This file reads all PDF invoices from a folder
# and extracts the data fields we need for Excel.
#
# Fields extracted from each PDF:
#   - contract_number
#   - date
#   - period
#   - invoice_number
#   - fiscal_number
#   - amount
# -------------------------------------------

def extract_data_from_pdf(pdf_path):
    """
    Opens one PDF file and extracts invoice data from its text.
    Returns a dictionary with the extracted fields,
    or None if extraction failed.
    """
    with pdfplumber.open(pdf_path) as pdf:
        # Combine all pages into one block of text
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"

    if not full_text.strip():
        print(f"  WARNING: No text found in {pdf_path}")
        return None

    result = {}

    # --- CONTRACT NUMBER ---
    # Handles: "Ugovor br. 219", "Ugovor br.321a", "Ugovorb r.442", "Broj ugovora:0446"
    contract_match = re.search(
        r'(?:Ugovor\s*b\s*r\.?\s*|Broj ugovora\s*[:\s]+)(\w+)',
        full_text,
        re.IGNORECASE
    )
    result["contract_number"] = contract_match.group(1).strip(".") if contract_match else None

    # --- DATA ROW ---
    # The line with date, period, invoice_number, fiscal_number, amount
    # looks like: "06.05.2026. Apr-26 05/05/2026 668/673 23,4"
    data_match = re.search(
        r'(\d{2}\.\d{2}\.\d{4}\.?)\s+'   # date: 06.05.2026.
        r'(\S+-\d{2,4})\s+'               # period: Apr-26
        r'(\d+/\d+/\d+)\s+'              # invoice_number: 05/05/2026
        r'(\d+/\d+)\s+'                   # fiscal_number: 668/673
        r'([\d,\.]+)',                     # amount: 23,4
        full_text
    )

    if data_match:
        result["date"]           = data_match.group(1).rstrip(".")
        result["period"]         = data_match.group(2)
        # Reformat invoice number: 03/05/2026 → 2026-05-0003
        # Format: YYYY-MM-NNNN (year-month-4digit sequence)
        raw_invoice = data_match.group(3)
        parts = raw_invoice.split("/")
        if len(parts) == 3:
            seq, month, year = parts[0], parts[1], parts[2]
            result["invoice_number"] = f"{year}-{month}-{seq.zfill(4)}"
        else:
            result["invoice_number"] = raw_invoice
        result["fiscal_number"]  = data_match.group(4)
        result["amount"]         = data_match.group(5).replace(",", ".")
    else:
        print(f"  WARNING: Could not find data row in {pdf_path}")
        result["date"] = result["period"] = result["invoice_number"] = None
        result["fiscal_number"] = result["amount"] = None

    return result


def extract_all_pdfs(folder_path):
    """
    Scans a folder for all PDF files,
    extracts data from each one,
    and returns a list of dictionaries.
    """
    results = []

    pdf_files = sorted([
        f for f in os.listdir(folder_path)
        if f.lower().endswith(".pdf")
    ])

    print(f"Found {len(pdf_files)} PDF files in '{folder_path}'")
    print("-" * 50)

    for filename in pdf_files:
        full_path = os.path.join(folder_path, filename)
        print(f"Reading: {filename}")
        data = extract_data_from_pdf(full_path)
        if data:
            data["source_file"] = filename  # track which file this came from
            results.append(data)

    print("-" * 50)
    print(f"Successfully extracted: {len(results)} / {len(pdf_files)} files")
    return results


# -------------------------------------------
# RUN AS STANDALONE TEST
# -------------------------------------------
if __name__ == "__main__":
    FOLDER = "data/APRIL 2026"
    all_data = extract_all_pdfs(FOLDER)

    print("\nSample output (first 3 records):")
    for record in all_data[:3]:
        for key, value in record.items():
            print(f"  {key}: {value}")
        print()
