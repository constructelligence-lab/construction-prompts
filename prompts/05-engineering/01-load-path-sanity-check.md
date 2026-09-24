---
title: Structural load path sanity check
section: Engineering
slug: load-path-sanity-check
models: [ChatGPT, Claude, Gemini]
tags: [structure, review, engineering]
updated: 2026-09-24
---

## Use it when

You are preparing for a coordination or value-engineering discussion and want the obvious load path
and stability questions on the table. This is a sense check by a person who is not the engineer of
record, and it never replaces their calculation.

## The prompt

```text
You are a structural engineer reviewing a scheme for coordination issues only. You are
not producing design, and I will not use your answer as design.

Scheme: {{structure_description}}
Spans and grid: {{grid_and_spans}}
Primary framing: {{framing_description}}
Lateral stability strategy: {{stability_strategy}}
Foundations and ground conditions: {{foundations}}
Anything unusual: {{special_conditions}}

Tell me the questions I should be able to answer or refer to the engineer of record:
1. Is the vertical load path continuous from roof to foundation for every grid line?
2. Is the lateral system complete, with a clear route to the foundations?
3. Where does the scheme rely on an element that is also architecturally exposed or
   adjustable later?
4. Which interfaces with other disciplines could change the loads?
5. What is missing from my description that an engineer would need before reviewing this?

Format as a question list with the risk if it goes unanswered. Do not give me numbers.
```

## What good output looks like

- Asks about continuity and stability rather than guessing sizes — the failure mode it can catch.
- Names the discipline interfaces that change loads, which is where coordination problems originate.
- Tells you what is missing from your description, which is usually the most useful output.

## Follow-ups

- "Turn this into a checklist for a structural coordination meeting with the architect and the MEP engineer."
- "What long-lead or procurement implications follow from this stability strategy?"
- "Which of these questions should be answered before the next design freeze?"

## Guardrails

No generated output may be used as a structural calculation, and no dimension, size or capacity from
a model may reach a drawing. Design responsibility stays with the engineer of record, whose
calculation and review govern.
