---
title: Constructability risk review of a drawing set
section: Preconstruction
slug: constructability-risk-review
models: [ChatGPT, Claude, Gemini]
tags: [preconstruction, drawings, risk]
updated: 2026-09-24
---

## Use it when

You are pricing or planning a job and want a structured list of buildability questions before the
bid goes in. The model cannot see your drawings, so the value comes from describing the design
decisions accurately and getting back the questions you have not asked.

## The prompt

```text
You are a superintendent with 20 years on {{project_type}} work, reviewing a design for
the first time.

Project: {{project_description}}
Structure: {{structure_description}}
Envelope: {{envelope_description}}
Site constraints: {{site_constraints}}
Programme: {{programme_summary}}
Access and logistics: {{access_notes}}

List the constructability problems you would raise in the first coordination meeting.
For each one:
- the issue, in one sentence
- which trade or discipline it affects
- the consequence if it is missed (cost, programme, safety, or quality)
- the question that resolves it, addressed to the right party

Order them by how expensive they are to fix after the fact, worst first. Finish with the
three items you would want a shop-drawing or fabrication-level review to cover.
```

## What good output looks like

- Questions that a fabricator or foreman would actually raise, not generic "coordinate MEP" filler.
- Sequenced by cost-of-late-discovery, which is the only ordering that changes behaviour.
- Each item names the party who answers it, so the list becomes an agenda rather than a worry.

## Follow-ups

- "Which of these would be cheapest to resolve now at concept stage, and which are unavoidable?"
- "Rewrite the top five as RFIs in our format, with a reference to the drawing or detail needed."
- "What should I have told you about this project that I have not?"

## Guardrails

Do not upload or paste documents that a client has marked confidential. This produces a question
list, not a design review: a competent person still has to check it against the actual drawings,
the specification and the site.
