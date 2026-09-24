---
title: Three-week lookahead constraint sweep
section: Scheduling and planning
slug: lookahead-constraint-sweep
models: [ChatGPT, Claude, Gemini]
tags: [lookahead, field, planning]
updated: 2026-09-24
---

## Use it when

You are building the next three-week lookahead and want to remove constraints before they stop work,
rather than reporting them after the fact.

## The prompt

```text
You are a superintendent planning the next three weeks on a {{project_type}} job.

Work planned for weeks 1 to 3: {{planned_work}}
Known constraints and their status: {{constraints}}
Resource and crew availability: {{resources}}
Weather outlook and seasonal effects: {{weather}}
Approvals, inspections and submittals pending: {{pending_approvals}}

For each work item, tell me:
- whether the constraint is truly cleared, and what evidence would prove it
- who must act, and by what date, for the work to start on time
- the earliest warning sign that it will not be cleared
- what alternative work can absorb the crew if it slips

Then list only the items that need action this week, sorted by how soon they block work.
```

## What good output looks like

- Turns constraints into dated actions with named owners, which is what makes a lookahead useful.
- Includes the "proof of clearance" test, which catches the common case of a constraint marked
  cleared without anyone confirming it.
- Provides a fallback for each crew, so a slip does not become idle time.

## Follow-ups

- "Rewrite this as the one-page lookahead we hand out on Monday morning."
- "What are the three questions to ask each foreman at the Monday meeting?"
- "Which of these constraints should have been raised a month ago, and what does that tell us about our planning lead time?"

## Guardrails

The lookahead belongs to the field team. This output is a starting draft that the superintendent
owns and corrects, and inspection or approval dates must come from the parties who control them.
