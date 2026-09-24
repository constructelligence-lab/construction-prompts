---
title: Code and accessibility checklist for a design review
section: Architecture and design
slug: code-and-accessibility-checklist
models: [ChatGPT, Claude, Gemini]
tags: [code, accessibility, compliance]
updated: 2026-09-24
---

## Use it when

You want a structured set of compliance questions to work through for a design, recognising that
the model does not know your local code and must not be treated as knowing it.

## The prompt

```text
You are a code-literate architect preparing a compliance review agenda.

Project: {{project_type}} in {{jurisdiction}}
Occupancy and use: {{occupancy}}
Key design features: {{design_features}}
Site and access strategy: {{access_strategy}}

List the regulatory and accessibility questions this design must answer, grouped by
topic, with the item that typically catches teams out for each.

Important: do not state what the code requires. I will check the requirements myself in
the current adopted code and local amendments. Your job is to make sure I do not forget
a topic, and to tell me where local amendments most often differ from the model code.

Format: topic, question to answer, who owns it, and whether it typically needs an early
decision to avoid redesign.
```

## What good output looks like

- Produces coverage, not requirements — a list of topics to check, with the trap named.
- Flags which items need deciding early, because those are the expensive ones.
- Refuses to quote code numbers, which is the correct behaviour.

## Follow-ups

- "Which of these items could change the massing or the site layout if answered late?"
- "Turn this into an agenda for a 45-minute review meeting with the design team."
- "What documentation would an authority having jurisdiction expect to see for each item?"

## Guardrails

Codes change and local amendments differ. Verify every item against the adopted code, local
amendments and the authority having jurisdiction, and involve the responsible design professional.
Never rely on a language model for a code requirement.
