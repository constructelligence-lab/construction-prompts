---
title: Contract risk review preparation
section: Contracts and commercial
slug: contract-risk-review
models: [ChatGPT, Claude, Gemini]
tags: [contracts, risk, commercial]
updated: 2026-09-24
---

## Use it when

A contract or subcontract is on your desk and you want the risk topics organised before it goes to
your lawyer, so the expensive hours are spent on judgement rather than on reading out loud.

## The prompt

```text
You are a commercial manager preparing a contract review for a lawyer. You are not
giving legal advice and I will not treat your output as such.

Contract type and parties: {{contract_summary}}
Clauses that concern us: {{concerning_clauses}}
Scope and price basis: {{commercial_terms}}
Programme and completion provisions: {{programme_terms}}
Payment and security provisions: {{payment_terms}}

Build the review agenda:
1. The clauses I must read carefully, with the question each one raises.
2. Where this contract shifts risk away from the standard position and onto us.
3. The provisions I must understand before signing: notices, time bars, payment
   conditions, delay and change mechanisms, termination, and dispute resolution.
4. The five questions to put to my lawyer, with the specific clause for each.

Do not state what the law would say. I want structure and questions, not conclusions.
```

## What good output looks like

- Produces a genuinely structured agenda — notices, time bars, payment, change, termination —
  rather than a heap of concerns.
- Sends specific questions with clause references to the lawyer, which is a better use of them.
- Declines to give legal conclusions, which is the correct boundary.

## Follow-ups

- "Rewrite this as a one-page summary for the directors explaining the top three risks."
- "What questions should we ask the subcontractor about their insurance and bonding?"
- "Turn the notice provisions into a calendar of dates and owners for the job."

## Guardrails

Contracts are legal documents and only your lawyer's advice governs. Never paste contracts under
negotiation into a consumer tier tool, check confidentiality obligations in the underlying
agreement, and treat every clause reference produced as unverified until a person has found it in
the document.
