---
title: Job cost analysis in Python or pandas
section: Automation and analysis
slug: job-cost-analysis-in-python
models: [ChatGPT, Claude, Gemini]
tags: [job-cost, python, analysis, automation]
updated: 2026-09-24
---

## Use it when

Your accounting system will give you a job cost export but not the analysis you want, and the work
is repetitive enough to script rather than rebuild in a spreadsheet every month.

## The prompt

```text
You are a construction data analyst writing Python with pandas.

Input: a CSV export of job cost detail with these columns:
{{column_list_with_meanings}}

What I want to know:
{{analysis_goals}}

Write a script that:
1. Loads the file and validates the expected columns, failing with a clear message if the
   export format has changed.
2. Cleans the obvious problems and reports what it changed: job number formats, cost code
   padding, duplicate rows, blank coding.
3. Computes {{metrics}} at the levels I asked for.
4. Flags the rows or jobs that meet the warning conditions.
5. Writes a summary CSV and prints a short plain-text report.

Rules: never silently drop rows, always print how many rows were excluded and why, use
only the standard library plus pandas, and show the arithmetic in comments so an
accountant can check it. Also tell me which of my assumptions a finance person should
confirm before we rely on this.
```

## What good output looks like

- Counts and reports every excluded row, so the analysis can be reconciled to the ledger.
- Shows the arithmetic in comments, which is how a controller verifies it without reading code.
- States its assumptions about cost coding and posting lag, because those decide whether the
  numbers mean anything.

## Follow-ups

- "Add a month-over-month trend per job and cost code, and flag anything changing by more than {{threshold}} percent."
- "Add a check for hours coded to a cost code that does not exist in our code list."
- "Turn the summary into a one-page report I can paste into a Monday meeting pack."

## Guardrails

Keep real job cost data inside your own systems: do not paste exports containing rates, margins or
payroll detail into consumer tier tools. The script is a tool, not an accounting record, and
anything it reports must reconcile to the ledger before anyone acts on it.
