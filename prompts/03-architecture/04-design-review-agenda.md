---
title: Design review agenda that finds problems
section: Architecture and design
slug: design-review-agenda
models: [ChatGPT, Claude, Gemini]
tags: [coordination, meetings, design]
updated: 2026-09-24
---

## Use it when

You are running a design or coordination review and want an agenda that surfaces conflicts rather
than walking through the drawings in order.

## The prompt

```text
You are chairing a design review for a {{project_type}} project.

Attendees and disciplines: {{attendees}}
Current design stage: {{design_stage}}
Areas of the design that carry the most risk: {{risk_areas}}
Open items carried over: {{open_items}}
Decisions needed this week: {{decisions_needed}}

Build a 60-minute agenda that would actually find problems, not read the drawings back.
For each item: the question to put to the room, the discipline that must answer, the
decision or action expected, and the consequence of leaving it open.

Put the coordination interfaces first, then the decisions with programme impact, then
the rest. Include the five minutes at the start for anything that has gone wrong since
the last review.
```

## What good output looks like

- Front-loads interfaces between disciplines, which is where design problems actually live.
- Each item has a question and an owner, so the meeting produces decisions rather than notes.
- Includes the "what broke since last time" slot, which is what keeps a review honest.

## Follow-ups

- "Rewrite this as the pre-read to send out 24 hours before the meeting."
- "Draft the minutes template that captures decisions, owners and dates from this agenda."
- "Which three items should we resolve in a smaller side meeting instead of the main review?"

## Guardrails

Minutes and decisions become the record of the project. Someone at the meeting owns the output, and
any design decision that leaves the room must be confirmed by the responsible professional.
