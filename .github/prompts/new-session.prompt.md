---
mode: 'agent'
description: "Start a new working session — read the latest captain's log and summarize where we are."
---

<!-- 
  HOW TO RUN THIS PROMPT:
  In Copilot Chat, type # and select "new-session.prompt.md" from the dropdown.
  Do NOT type /new-session.prompt.md — that is plain text and will not execute anything.
-->

Read the latest file from `captains-log/` (highest stardate number).

Then give me a summary in this format:

**📍 Where we are:**
[Current phase and overall project status]

**✅ Last thing we did:**
[Last completed step from WHAT WE ACCOMPLISHED TODAY]

**🔜 Next step:**
[Exact next step from NEXT STEP section]

After the summary, wait for my confirmation before doing anything else.
