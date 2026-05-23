# =============================================================================
# INVOICE AUTOMATION — app.py
# =============================================================================
# WHAT THIS FILE DOES:
#   Flask web server. The client opens a browser, uploads an Excel file,
#   and downloads a ZIP with all generated PDF invoices.
#
# HOW TO RUN LOCALLY:
#   python app.py
#   Then open: http://localhost:5000
#
# ROUTES:
#   GET  /           → serves the upload page (templates/upload.html)
#   POST /generate   → receives Excel, runs pipeline, returns ZIP download
# =============================================================================


# --- IMPORTS ---
import io                          # built-in: work with files in memory (no disk writes)
import os                          # built-in: file paths, read environment variables
import zipfile                     # built-in: create ZIP archives in memory

from flask import Flask, render_template, request, send_file, flash, redirect, url_for
# Flask         → the web framework
# render_template → loads an HTML file from templates/ folder
# request       → gives us access to uploaded files and form data
# send_file     → sends a file (or bytes) back to the browser as a download
# flash         → shows one-time messages to the user (e.g. error notices)
# redirect      → redirects the browser to another route
# url_for       → builds a URL from a route function name

from main import load_excel_data, render_invoice_html
# We reuse the existing pipeline functions from main.py.
# No logic is duplicated — app.py is just a web layer on top.


# =============================================================================
# APP SETUP
# =============================================================================

app = Flask(__name__)

# Secret key is required for flash() messages to work.
# os.environ.get() → reads the value from the server's environment variables
# "invoice-automation-secret" → fallback value used only during local development
# On Render.com, the real SECRET_KEY is auto-generated and injected by render.yaml
app.secret_key = os.environ.get("SECRET_KEY", "invoice-automation-secret")


# =============================================================================
# ROUTE 1 — Upload page
# =============================================================================
# WHY: The client needs a simple page with a file input and a submit button.
# HOW: Flask renders templates/upload.html and returns it to the browser.

@app.route("/")
def index():
    # render_template() → loads upload.html from the templates/ folder
    # Flask automatically looks in the templates/ folder — no path needed.
    return render_template("upload.html")


# =============================================================================
# ROUTE 2 — Generate PDFs and return ZIP
# =============================================================================
# WHY: This is the core of the web app — receive Excel, produce PDFs.
# HOW:
#   1. Save the uploaded Excel to a temporary in-memory buffer
#   2. Run load_excel_data() → get list of invoice dictionaries
#   3. For each invoice: render HTML → convert to PDF bytes (in memory)
#   4. Pack all PDFs into a ZIP (in memory)
#   5. Send ZIP to browser as a download
#
# IMPORTANT — "in memory" means:
#   We never write files to disk on the server.
#   Everything lives in RAM as bytes objects.
#   This is safer and works on free hosting (Render.com has a read-only filesystem).

@app.route("/generate", methods=["POST"])
def generate():
    # --- Step 1: Check that a file was actually uploaded ---
    # request.files["excel_file"] → the uploaded file from the HTML form
    # "excel_file" must match the name="excel_file" attribute in upload.html
    if "excel_file" not in request.files:
        flash("No file selected.")
        return redirect(url_for("index"))

    uploaded_file = request.files["excel_file"]

    # uploaded_file.filename is empty if the user clicked Submit without choosing a file
    if uploaded_file.filename == "":
        flash("No file selected.")
        return redirect(url_for("index"))

    # --- Step 2: Load invoice data from the uploaded Excel file ---
    # io.BytesIO() → wraps the uploaded bytes so pandas can read it
    # without saving it to disk first
    try:
        excel_bytes = io.BytesIO(uploaded_file.read())
        invoices = load_excel_data(excel_bytes)
    except Exception as e:
        flash(f"Error reading Excel file: {e}")
        return redirect(url_for("index"))

    # --- Step 3 + 4: Render each invoice to PDF and pack into ZIP ---
    # zip_buffer → a BytesIO object that acts like a ZIP file in RAM
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for invoice in invoices:
            # Render the HTML for this invoice
            html_string = render_invoice_html(invoice)

            # Convert HTML → PDF bytes (in memory, no file saved to disk)
            # weasyprint's write_pdf() can return bytes when no path is given
            from weasyprint import HTML as WeasyprintHTML
            pdf_bytes = WeasyprintHTML(
                string=html_string,
                base_url=os.path.abspath("templates")
                # base_url → absolute path so WeasyPrint finds logo, stamp, signature
                # os.path.abspath() converts "templates" to full path like
                # "/Users/zeal.v/Desktop/vs_code/invoice-automation/templates"
            ).write_pdf()

            # Build filename for this PDF inside the ZIP
            invoice_number = str(invoice.get("invoice_number", "UNKNOWN"))
            filename = f"{invoice_number}.pdf"

            # zip_file.writestr() → adds bytes directly to ZIP (no disk write)
            # "w" in ZipFile constructor → write mode
            zip_file.writestr(filename, pdf_bytes)

    # --- Step 5: Send ZIP to browser ---
    # Rewind buffer to the beginning before sending
    # (after writing, the pointer is at the end — we must reset it)
    zip_buffer.seek(0)

    return send_file(
        zip_buffer,
        mimetype="application/zip",
        as_attachment=True,           # triggers browser "Save As" dialog
        download_name="invoices.zip"  # filename the user sees in the dialog
    )


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    # debug=True → Flask restarts automatically when you save a file
    # Only use debug=True locally — never in production
    app.run(debug=True)
