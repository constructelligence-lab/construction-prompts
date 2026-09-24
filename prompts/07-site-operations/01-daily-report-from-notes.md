---
title: Daily report from messy field notes
section: Site and field operations
slug: daily-report-from-notes
models: [ChatGPT, Claude, Gemini]
tags: [field, records, daily-report]
updated: 2026-09-24
---

## Use it when

The day's notes are a mix of texts, voice-note reminders and scribbles, and the report needs to be
written before you go home — with the facts intact and nothing invented.

## The prompt

```text
You are a site engineer writing today's daily report from my raw notes.

Project: {{project_name}}, report for {{date}}
Weather and site conditions: {{weather_and_conditions}}
Labour on site: {{labour}}
Plant and equipment: {{plant}}
Work completed today: {{work_completed}}
Issues, delays and stoppages: {{issues}}
Instructions received: {{instructions}}
Visitors and inspections: {{visitors}}
Safety observations: {{safety_observations}}

Write the report under these headings: weather and conditions; resources on site; work
carried out; delays and disruption; instructions and communications; visitors and
inspections; safety; outstanding items for tomorrow.

Rules: use only the facts I gave you. Where something is unclear, write [confirm] rather
than filling the gap. Keep the language plain and factual, suitable as a contemporaneous
record. No adjectives about performance and no opinions.
```

## What good output looks like

- No invented detail: unclear items are marked `[confirm]` rather than smoothed over.
- Records delays and instructions precisely, because the daily report is evidence.
- Reads as a factual record, not a story with opinions about how the day went.

## Follow-ups

- "List the items I marked [confirm] as questions to answer before this is filed."
- "Turn the delays section into a chronology with times, ready for the delay file."
- "Summarise this report in three lines for the client's weekly update."

## Guardrails

Daily reports become evidence in delay and defect disputes. Nothing may be added that did not
happen, weather and labour figures must come from real records, and anything that could be read as
an admission or an instruction should be reviewed before it is filed.
