---
title: Change order pricing narrative
section: Estimating and takeoff
slug: change-order-pricing-narrative
models: [ChatGPT, Claude, Gemini]
tags: [change-orders, commercial, pricing]
updated: 2026-09-24
---

## Use it when

The numbers are agreed internally and now need to be presented so they are hard to argue with —
typically for a priced change that a client or a subcontractor will scrutinise.

## The prompt

```text
You are a commercial manager writing a narrative for a priced change order.

Change: {{change_description}}
Contract basis for pricing: {{contract_clause_or_method}}
Direct cost breakdown: {{cost_breakdown}}
Markups applied and their basis: {{markups}}
Programme effect: {{time_impact}}

Write the narrative that sits above the numbers, in this order:
1. What changed and why, in three sentences, without blame.
2. The method used to price it and why it is the contractually correct method.
3. The cost breakdown in plain words, line by line.
4. The programme effect, or a clear statement that there is none.
5. What we need from the client to proceed.

Tone: factual and unemotional. No adjectives about fairness. Assume the reader is
reasonable and busy. Keep it under 400 words.
```

## What good output looks like

- States the pricing method before the numbers, which is what makes the numbers defensible.
- Avoids grievance language, which is what turns a priced change into a negotiation.
- Ends with a clear ask, so the document does something rather than just recording something.

## Follow-ups

- "Rewrite the same narrative in half the words for a client who reads only the first paragraph."
- "What are the three challenges a client's quantity surveyor would make to this, and how should we answer them?"
- "Produce the covering email for this, under 120 words."

## Guardrails

Never let a drafted narrative imply a contractual entitlement you have not confirmed. Change
procedures, notice periods and pricing methods come from the contract, and anything that goes to a
client should be checked by whoever owns the commercial relationship.
