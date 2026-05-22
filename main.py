# =============================================================================
# INVOICE AUTOMATION — main.py
# =============================================================================
# WHAT THIS FILE DOES:
#   This is the brain of the project. It connects all parts together:
#   Excel data → HTML template → PDF output
#
# HOW TO RUN:
#   python main.py
#
# EXPECTED RESULT:
#   One PDF file per invoice row in the output/ folder
# =============================================================================


# --- IMPORTS (libraries we need) ---
import os                          # built-in: file paths, folder creation
import pandas as pd                # reads Excel into a table (DataFrame)
from jinja2 import Environment, FileSystemLoader   # fills HTML templates
from weasyprint import HTML        # converts HTML string → PDF file


# =============================================================================
# STEP 1 — LOAD THE EXCEL FILE
# =============================================================================
# WHY: The Excel file is our data source. Each row = one invoice.
# HOW: We open the file and read it row by row.
# LIBRARY: openpyxl
#
# Example of what one row might look like:
#   | Client Name | Invoice No | Date       | Amount |
#   | Acme Corp   | INV-001    | 02.05.2026 | 500 €  |

def load_excel_data(filepath):
    # pd.read_excel() → opens the Excel file and reads it as a DataFrame
    # DataFrame = like a table in memory (rows and columns)
    # sheet_name="Sheet2" → our data lives on the second sheet
    df = pd.read_excel(filepath, sheet_name="Sheet2")

    # df.to_dict("records") → converts each row into a dictionary
    # Example: {"owner_name": "Ana", "amount": 150, ...}
    # The result is a LIST of those dictionaries — one per invoice row
    records = df.to_dict("records")

    # Split address into two lines for cleaner display on the invoice.
    # Example: "Milana Karanovića 55, 78000 Banja Luka, RS, BiH"
    #   → address_line1 = "Milana Karanovića 55"
    #   → address_line2 = "78000 Banja Luka, RS, BiH"
    #
    # str(addr) → converts to string safely (in case of NaN/empty cell)
    # split(", ", 1) → splits on the FIRST comma+space only (maxsplit=1)
    #   "A, B, C".split(", ", 1) → ["A", "B, C"]  ← only one cut
    for record in records:
        addr = str(record.get("address", ""))
        parts = addr.split(", ", 1)
        record["address_line1"] = parts[0] if len(parts) > 0 else ""
        record["address_line2"] = parts[1] if len(parts) > 1 else ""

        # Format amount to always show 2 decimal places: 23.4 → "23,40"
        # float() → converts Excel value to a number (in case it's stored as string)
        # :.2f   → Python format: 2 digits after the decimal point
        # .replace(".", ",") → European format: dot → comma (23.40 → 23,40)
        try:
            record["amount"] = f"{float(record['amount']):.2f}".replace(".", ",")
        except (ValueError, TypeError):
            pass  # if amount is empty or invalid, leave it as-is

    return records


# =============================================================================
# STEP 2 — FILL THE HTML TEMPLATE WITH DATA
# =============================================================================
# WHY: Our invoice design lives in templates/invoice.html
#      We need to swap placeholder text with real data from Excel.
# HOW: Jinja2 finds placeholders like {{ client_name }} and replaces them.
# LIBRARY: jinja2
#
# Think of it like a Word mail merge — same template, different data each time.

def render_invoice_html(invoice_data):
    # Environment → Jinja2 engine that knows WHERE to look for templates
    # FileSystemLoader("templates") → "look in the templates/ folder"
    env = Environment(loader=FileSystemLoader("templates"))

    # get_template() → loads invoice.html from the templates/ folder
    template = env.get_template("invoice.html")

    # template.render(**invoice_data) → fills every {{ variable }} in the HTML
    # **invoice_data unpacks the dictionary:
    #   {"owner_name": "Ana", "amount": 150} becomes owner_name="Ana", amount=150
    return template.render(**invoice_data)


# =============================================================================
# STEP 3 — CONVERT HTML TO PDF
# =============================================================================
# WHY: The client receives a PDF, not an HTML file.
# HOW: A library takes our filled HTML and renders it as a PDF page.
# LIBRARY: weasyprint (or pdfkit — to be decided)

def convert_html_to_pdf(html_string, output_path):
    # HTML(string=...) → WeasyPrint receives HTML as text (not a file)
    # base_url="templates" → IMPORTANT: tells WeasyPrint where to find
    #   images like assets/logo.png (relative paths in the HTML)
    #   Without this, images would not appear in the PDF.
    HTML(string=html_string, base_url="templates").write_pdf(output_path)


# =============================================================================
# STEP 4 — GENERATE COMBINED PDF (all invoices in one file)
# =============================================================================
# WHY: The client needs one PDF with all invoices for archiving/printing.
# HOW: We collect all rendered HTML strings into a list, then join them
#      into one big HTML document. WeasyPrint converts that into a
#      multi-page PDF — one invoice per page.
#
# page-break-after: always → CSS rule that tells the PDF renderer:
#   "after this invoice block, start a new page"
#   Think of it like inserting a manual page break in Word.

def generate_combined_pdf(invoices, output_path):
    # This list will hold one rendered HTML string per invoice
    pages = []

    for invoice in invoices:
        # Render this invoice into HTML (same function as individual PDFs)
        html = render_invoice_html(invoice)

        # Wrap the invoice HTML in a div with the page-break class.
        # This div tells WeasyPrint: "each invoice = one page".
        pages.append(f'<div class="invoice-page">{html}</div>')

    # Join all invoice pages into one HTML document.
    # The CSS rule page-break-after: always is injected at the top.
    #
    # "\n".join(pages) → connects all page strings with a newline between them
    combined_html = """
    <html>
    <head>
      <meta charset="UTF-8" />
      <style>
        /* page-break-after: always → after each invoice div, start a new PDF page */
        .invoice-page { page-break-after: always; }
      </style>
    </head>
    <body>
    """ + "\n".join(pages) + """
    </body>
    </html>
    """

    # Convert the big combined HTML into one multi-page PDF
    HTML(string=combined_html, base_url="templates").write_pdf(output_path)
    print(f"\n  📄 Combined PDF saved: {output_path}")


# =============================================================================
# STEP 5 — MAIN LOOP (runs everything)
# =============================================================================
# WHY: This is where Steps 1-4 are combined.
#      For each row in Excel → render HTML → save as PDF.
#      Then all invoices → one combined PDF.
# HOW: A simple for-loop goes through every invoice one by one.

def main():
    # Path to the Excel file
    excel_path = "data/stan_na_dan_klijenti_racuni.xlsx"

    # os.makedirs() → creates the output/ folder if it doesn't exist yet
    # exist_ok=True → no error if folder already exists
    os.makedirs("output", exist_ok=True)

    # Step 1: load all invoice rows from Excel
    invoices = load_excel_data(excel_path)
    print(f"Loaded {len(invoices)} invoices from Excel.")

    # Step 2 + 3: loop through every invoice row
    for invoice in invoices:
        # invoice_number is used as the PDF filename
        # str() converts number to string (in case Excel stored it as a number)
        invoice_number = str(invoice.get("invoice_number", "UNKNOWN"))

        # Build the output file path: e.g. output/2026-05-0003.pdf
        output_path = f"output/{invoice_number}.pdf"

        # Fill the HTML template with this invoice's data
        html = render_invoice_html(invoice)

        # Convert the filled HTML to a PDF file
        convert_html_to_pdf(html, output_path)

        print(f"  ✅ Created: {output_path}")

    # After all individual PDFs, generate one combined PDF with all invoices
    combined_path = "output/combined.pdf"
    generate_combined_pdf(invoices, combined_path)

    print(f"\nDone. {len(invoices)} PDF(s) saved to output/.")


# =============================================================================
# ENTRY POINT
# =============================================================================
# WHY: This block runs main() only when you execute this file directly.
#      It prevents main() from running if another file imports this one.
# This is a Python best practice — always include this at the bottom.

if __name__ == "__main__":
    main()
