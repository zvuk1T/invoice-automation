#!/usr/bin/env bash
# =============================================================================
# build.sh — Render.com build script
# =============================================================================
# WHAT THIS FILE DOES:
#   Render.com runs this script ONCE when it builds/deploys the app.
#   It installs system-level libraries that WeasyPrint needs to generate PDFs.
#
# WHY WE NEED THIS:
#   WeasyPrint is not a pure Python library.
#   It depends on system libraries (pango, cairo, etc.) that render fonts
#   and graphics. These libraries must be installed at the OS level —
#   pip install alone is not enough.
#
#   On your laptop: these libraries came pre-installed with macOS.
#   On Render's Linux server: we must install them manually.
#
# WHEN IT RUNS:
#   Render runs build.sh BEFORE starting the app.
#   Order: build.sh → pip install -r requirements.txt → start gunicorn
#
# HOW TO READ BASH COMMANDS:
#   apt-get  → Ubuntu/Linux package manager (like pip, but for the OS) 🐧
#   -y       → "yes to all prompts" — non-interactive install, no manual confirmation
#   &&       → "if this succeeds, run the next command"
# =============================================================================

set -o errexit
# set -o errexit → "if ANY command in this script fails, stop immediately"
# Without this, the script would keep running even after an error.
# Example: if apt-get fails, we do NOT want to continue to pip install.
# This is a safety mechanism — fail fast, fail clearly. 🛑

# --- Step 1: Install WeasyPrint system dependencies ---
# These are the OS-level libraries WeasyPrint needs:
#
#   libpango-1.0-0      → text layout engine (handles fonts, Unicode, line breaks)
#   libpangoft2-1.0-0   → Pango module for FreeType fonts (renders actual font files)
#   libpangocairo-1.0-0 → Pango + Cairo bridge (connects text engine to graphics engine)
#   libcairo2           → 2D graphics engine (draws shapes, lines, PDF pages)
#   libffi-dev          → Foreign Function Interface — lets Python call C libraries
#   libjpeg-dev         → JPEG image support (for logos and photos in PDFs)
#   libopenjp2-7        → JPEG 2000 image support
#   libharfbuzz0b       → font shaping engine (correct rendering of complex scripts)
#
# Mental model:
#   WeasyPrint = a car 🚗
#   These libraries = engine parts (wheels, fuel system, transmission)
#   Without them, the car exists but cannot drive.

apt-get update -y && apt-get install -y \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    libffi-dev \
    libjpeg-dev \
    libopenjp2-7 \
    libharfbuzz0b
# The backslash \ at the end of each line means:
# "this command continues on the next line" — just for readability.
# It is one single apt-get install command split across multiple lines.

# --- Step 2: Install Python packages ---
# pip install -r requirements.txt → installs all packages listed in requirements.txt
# This includes: flask, gunicorn, weasyprint, pandas, jinja2, openpyxl, pdfplumber
pip install -r requirements.txt
