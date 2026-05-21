---
mode: 'agent'
description: "Checklist for processing a new month's invoices."
---

We are starting a new invoice month. Work through this checklist one step at a time.
Announce each step, wait for confirmation, then execute.

## Checklist

1. **Create new data folder**
   - Folder name format: `data/MONTH YYYY/` (e.g. `data/MAJ 2026/`)
   - Confirm folder exists before continuing

2. **Add new PDFs**
   - Ask: "Have you added all PDF invoices to the new folder?"
   - Wait for confirmation

3. **Run PDF extractor**
   - Command: `source venv/bin/activate && python pdf_extractor.py`
   - Update `FOLDER` variable in `excel_utils.py` to point to new month's folder
   - Check output: all PDFs matched? Any warnings?

4. **Run Excel update**
   - Command: `python excel_utils.py`
   - Check output: all rows updated? Any not found?

5. **Verify Excel data**
   - Open Excel and spot-check 2-3 rows
   - Ask: "Does the data look correct?"

6. **Update captain's log**
   - Use the `update-captains-log` prompt

7. **Commit and push**
   - Commit message format: `Process MAY 2026 invoices — 36 records updated`

After completing all steps, confirm everything is committed and pushed.
