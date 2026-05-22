# How to Read Terminal Commands
## Invoice Automation Project — Guide for Lieutenant Commander Data

---

## WHY THIS GUIDE EXISTS

When working on this project, we run terminal commands regularly — to activate the environment, run scripts, check output.
Most guides just show *what* to type. This guide explains *what it means* — so you can read any command and understand it, not just copy-paste it.

---

## THE MENTAL MODEL: TERMINAL AS PIPELINE

Think of a terminal command as a **factory assembly line**:

```
[source]  →  [tool]  →  [filter]  →  [destination]
```

Each segment does one job. The output of one becomes the input of the next.

---

## ANATOMY OF A COMMAND — FULL EXAMPLE

```bash
source venv/bin/activate && python main.py 2>&1 | tail -3
```

Breaking it down:

---

### `source venv/bin/activate`

```
source venv/bin/activate  →  "Turn on our Python bubble"  🫧
```

- `venv/` is a folder containing a private Python environment (all our packages: WeasyPrint, pandas, Jinja2)
- Without this, Python would use the system Python — which has none of our packages installed
- `source` means: "run this script **inside** the current shell" (not in a child process)
- **Expected result:** your terminal prompt may show `(venv)` prefix

---

### `&&` — the conditional chain

```
command1 && command2  →  "Do #2, BUT ONLY if #1 succeeded"  🔗
```

- If `source venv/bin/activate` fails → `python main.py` is **never run**
- This prevents running the script with the wrong Python
- Contrast with `;` which runs both commands regardless of success/failure

| Operator | Meaning |
|---|---|
| `&&` | Run next only if previous **succeeded** (exit code 0) |
| `\|\|` | Run next only if previous **failed** |
| `;` | Always run next, no matter what |

---

### `python main.py`

```
python main.py  →  "Run our invoice script"  🐍
```

- Straightforward — executes `main.py` with the active Python interpreter
- Produces output on two channels (see next section)

---

### `2>&1` — merging output channels

This is the most important concept in this guide.

The terminal has **two separate output channels**:

```
Channel 1 (stdout)  →  normal output  →  print(), info messages
Channel 2 (stderr)  →  error output   →  exceptions, warnings
```

Normally, `|` (pipe) only passes **channel 1** to the next command.
Errors on channel 2 would bypass the pipe entirely — you'd see them on screen but they wouldn't be captured.

`2>&1` means: **"redirect channel 2 into channel 1"** — merge them together.

```
stdout (1) ──┐
             ├──→ | (pipe) → next command
stderr (2) ──┘
      ↑
   2>&1 merges here
```

**Why we need it:**
If `main.py` crashes with a Python exception, that error goes to stderr (channel 2).
Without `2>&1`, piping to `tail` would miss the error entirely — you'd see nothing useful.
With `2>&1`, errors and normal output travel together → `tail` captures both.

**Reading the syntax:**
- `2>` means "redirect channel 2 to..."
- `&1` means "...channel 1" (the `&` means "this is a channel number, not a filename")

---

### `|` — the pipe

```
command1 | command2  →  "Feed output of #1 as input to #2"  🚿
```

- Takes everything printed by `python main.py` (both channels, now merged)
- Passes it directly to `tail`
- Nothing is written to a file — it's a live stream

---

### `tail -3` — show only the end

```
tail -3  →  "Show me only the last 3 lines"  ✂️
```

- `tail` shows the end of a stream or file
- `-3` = last 3 lines
- Contrast: `head -3` = first 3 lines

**Why not show everything?**
`main.py` prints one line per invoice — 41 lines total. The important information (success message or error) is always at the end.
Showing only the last 3 lines cuts the noise.

| Command | Shows |
|---|---|
| `tail -3` | Last 3 lines |
| `tail -10` | Last 10 lines |
| `head -3` | First 3 lines |
| `cat` | Everything |

---

## COMPLETE MENTAL MODEL

```
source venv/bin/activate   →  "Turn on our Python environment"        🫧
&&                         →  "Only continue if that succeeded"        🔗
python main.py             →  "Run the invoice script"                 🐍
2>&1                       →  "Merge errors into normal output"        🔀
|                          →  "Feed all output to the next command"    🚿
tail -3                    →  "Show only the last 3 lines"             ✂️
```

**Expected output when everything works:**
```
  📄 Combined PDF saved: output/combined.pdf

Done. 41 PDF(s) saved to output/.
```

**Expected output when something breaks:**
```
Traceback (most recent call last):
  File "main.py", line 47, in ...
KeyError: 'amount'
```
Both cases are captured — because of `2>&1`.

---

## COMMON PATTERNS YOU WILL SEE

### Run and check last lines
```bash
python main.py 2>&1 | tail -5
```

### Run and save all output to a log file
```bash
python main.py 2>&1 > output/run.log
```
- `>` redirects to a file (overwrites)
- `>>` appends to a file

### Check if a package is installed
```bash
pip show weasyprint
```

### See all installed packages
```bash
pip list
```

---

## TROUBLESHOOTING

| Problem | Likely cause | Fix |
|---|---|---|
| `command not found: python` | venv not activated | Run `source venv/bin/activate` first |
| `ModuleNotFoundError` | Wrong Python / venv not active | Check `which python` — should point to venv |
| No output at all | Script failed silently | Remove `\| tail -3` and run again to see full output |
| `(venv)` not showing in prompt | Normal on some shells | Run `which python` to confirm venv is active |

---

## MENTAL MODEL — SUMMARY

```
Terminal channels:
  1 = stdout  →  normal print output
  2 = stderr  →  errors and warnings

Operators:
  &&   →  "and only if success"
  |    →  "pipe output forward"
  2>&1 →  "merge errors into normal output"
  >    →  "write output to file"
  >>   →  "append output to file"
```

---

*Guide created: Stardate 20260522*
*Author: Science Officer Spock*
*For: Lieutenant Commander Data (zvuk1T)*
