---
title: Specification section draft
section: Architecture and design
slug: specification-section-draft
models: [ChatGPT, Claude, Gemini]
tags: [specification, documentation, quality]
updated: 2026-09-24
---

## Use it when

You need a first draft of a specification section structure so you are editing rather than staring
at an empty document — with the understanding that the technical content is yours, not the
model's.

## The prompt

```text
You are a specification writer for {{discipline}} work.

I am writing a specification section for {{element_or_system}} on a {{project_type}}
project in {{jurisdiction}}.

What I know:
- Materials and products: {{materials}}
- Performance requirements: {{performance_requirements}}
- Standards and testing regime: {{standards}}
- Installation and workmanship expectations: {{workmanship}}
- What is excluded: {{exclusions}}

Build me an outline for the section using the standard three-part structure, with the
clauses I should cover and one line describing what each clause must decide.

Mark clearly:
- clauses where the requirement must come from the design team, not from general practice
- anything that varies by jurisdiction and must be checked locally
- the coordination items with other sections

Do not invent product names, standards numbers, or test values.
```

## What good output looks like

- Gives you the clause skeleton and the questions each clause answers, without fabricating content.
- Marks the items that must be jurisdiction-checked, instead of asserting a code requirement.
- Names the coordination interfaces, which is where specifications usually fail on site.

## Follow-ups

- "Turn the coordination items into a list of other sections I must cross-check."
- "Draft the submittal requirements clause using the three-part structure."
- "What in this section would a subcontractor be most likely to price as an exclusion?"

## Guardrails

Specifications are contractual. Every requirement, standard reference and test value must come from
an authoritative source you have checked, and the section must be reviewed by the designer
responsible for it before issue.
