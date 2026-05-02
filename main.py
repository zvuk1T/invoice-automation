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
# These will be filled in as we build each step.
# Example libraries we plan to use:
#   - openpyxl  → reads Excel files (.xlsx)
#   - jinja2    → fills HTML templates with data
#   - weasyprint or pdfkit → converts HTML to PDF


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
    # TODO: Open the Excel file at 'filepath'
    # TODO: Read all rows and return them as a list of dictionaries
    # Example: [{"client": "Acme Corp", "invoice_no": "INV-001", ...}, ...]
    pass


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
    # TODO: Load the HTML template from templates/invoice.html
    # TODO: Fill in the placeholders with invoice_data
    # TODO: Return the completed HTML as a string
    pass


# =============================================================================
# STEP 3 — CONVERT HTML TO PDF
# =============================================================================
# WHY: The client receives a PDF, not an HTML file.
# HOW: A library takes our filled HTML and renders it as a PDF page.
# LIBRARY: weasyprint (or pdfkit — to be decided)

def convert_html_to_pdf(html_string, output_path):
    # TODO: Take the HTML string
    # TODO: Convert it to a PDF file
    # TODO: Save the PDF to output_path (e.g. output/INV-001.pdf)
    pass


# =============================================================================
# STEP 4 — MAIN LOOP (runs everything)
# =============================================================================
# WHY: This is where Steps 1-3 are combined.
#      For each row in Excel → render HTML → save as PDF.
# HOW: A simple for-loop goes through every invoice one by one.

def main():
    # TODO: Call load_excel_data() to get all invoices
    # TODO: Loop through each invoice:
    #           html = render_invoice_html(invoice)
    #           convert_html_to_pdf(html, output_path)
    # TODO: Print a success message when all PDFs are generated
    pass


# =============================================================================
# ENTRY POINT
# =============================================================================
# WHY: This block runs main() only when you execute this file directly.
#      It prevents main() from running if another file imports this one.
# This is a Python best practice — always include this at the bottom.

if __name__ == "__main__":
    main()
