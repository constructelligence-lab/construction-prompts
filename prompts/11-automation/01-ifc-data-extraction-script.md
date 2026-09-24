---
title: IFC data extraction script
section: Automation and analysis
slug: ifc-data-extraction-script
models: [ChatGPT, Claude, Gemini]
tags: [ifc, bim, python, automation]
updated: 2026-09-24
---

## Use it when

You need a repeatable way to pull data out of IFC models — quantities, spaces, properties — instead
of clicking through them, and you would rather review code than write the boilerplate.

## The prompt

```text
You are a BIM automation developer writing a Python script using IfcOpenShell.

Goal: {{goal}}
Input: {{ifc_file_or_model_description}}
Output needed: {{output_format}}
Environment: {{python_version_and_os}}

Write a script that:
1. Opens the IFC file and reports the schema version and the project name.
2. Extracts {{elements}} with their {{properties_or_quantities}}.
3. Groups the results by {{grouping}} and totals the quantities.
4. Writes the output to {{output_format}} with a header row naming each field.
5. Prints a summary: how many elements were found, how many were skipped, and any
   element types it did not recognise.

Requirements: report skipped or unrecognised elements rather than failing silently,
handle a missing property without crashing, and keep the extraction logic in one function
so I can change the element filter. Add comments explaining the IFC concepts used, and
tell me which parts depend on how the model was authored.
```

## What good output looks like

- Reports what it skipped, which is the difference between a useful extraction and a misleading one.
- Comments explain the IFC concepts, so you can adapt it rather than just run it.
- Flags where the result depends on modelling conventions — quantity takeoffs from models almost
  always do.

## Follow-ups

- "Add a dry-run mode that lists what would be extracted without writing a file."
- "Add a check for elements that are duplicated or modelled twice, and report them separately."
- "Now write the equivalent using the web-ifc or IfcOpenShell command line, so I can compare."

## Guardrails

Quantities extracted from a model are only as good as the modelling discipline behind them. Never
let a script output become a bid quantity without a person reconciling it against the drawings, and
keep model files with client confidentiality obligations inside your own systems.
