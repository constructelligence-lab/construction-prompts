---
title: Unit rate sanity check
section: Estimating and takeoff
slug: unit-rate-sanity-check
models: [ChatGPT, Claude, Gemini]
tags: [estimating, pricing, review]
updated: 2026-09-24
---

## Use it when

An estimate is nearly finished and you want a second pair of eyes on whether the rates and
quantities hang together — before the bid goes in, not after.

## The prompt

```text
You are a chief estimator reviewing a colleague's bid for {{project_type}} in
{{region}}.

The line items are:
{{line_items_with_quantities_and_rates}}

Basis of the estimate: {{basis_notes}}
Labour rates used: {{labour_rates}}
Price date and escalation assumption: {{price_basis}}

Review it for internal consistency only. Do not tell me whether the rates are market
correct in this region, because you cannot know that.

Instead tell me:
1. Any line where the quantity and the rate do not make sense together.
2. Any code or item that looks missing for this scope and project type.
3. Where the arithmetic is inconsistent between similar lines.
4. The three figures I should check against my own data before submitting.

Present findings as a table: line, what looks wrong, why, what to check.
```

## What good output looks like

- Catches missing scope and unit mismatches rather than inventing market prices.
- Flags its own uncertainty explicitly instead of sounding authoritative about your region.
- Produces a checklist you can run through in 20 minutes, with the owner named for each check.

## Follow-ups

- "Rank those findings by how much money they could move in either direction."
- "Draft the questions I should ask the estimator who prepared this."
- "Which of these would a competitor be most likely to catch, and use against us?"

## Guardrails

Never treat the model as a pricing service: it does not know current market rates, and it will
produce a confident number if asked. Keep bid pricing out of consumer tier tools, and verify every
quantity and rate against your own data before submission.
