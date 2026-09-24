---
title: Render critique before it goes to the client
section: Visualisation and rendering
slug: render-critique-before-client
models: [ChatGPT, Claude, Gemini]
tags: [rendering, review, presentation]
updated: 2026-09-24
---

## Use it when

You are about to send a visual to a client and want a hard critique first — one that finds the
things an architect, a planner or a contractor would spot immediately.

## The prompt

```text
You are a critical design reviewer looking at a render before it is shown to a client.

What the image shows: {{image_description}}
Design intent: {{design_intent}}
Audience: {{audience}}
What we want them to take away: {{desired_takeaway}}

List the things that would undermine the image with this audience. For each: what it is,
why it matters to that audience, and how to fix it in one sentence.

Cover: architectural credibility (proportions, junctions, structural logic),
environmental credibility (light, shadow, reflections, entourage), planning or code
implausibility, and the things that mislead the client about cost or constructability.

Then say what the image does well and should not be changed. Do not compliment the
design; critique the image.
```

## What good output looks like

- Finds implausibilities an experienced eye catches in two seconds — spans that cannot work,
  junctions that would not build, light coming from two directions.
- Distinguishes "this looks wrong" from "this misleads the client about money", which are different
  problems with different fixes.
- Names what to leave alone, so an iteration does not break what already works.

## Follow-ups

- "Rewrite the top three fixes as instructions for the person producing the render."
- "What would a planner object to, and how would we answer it?"
- "Which single change would most improve the client's impression, if we only have time for one?"

## Guardrails

A critique is an opinion, and the design decisions behind the image belong to the design team. Never
ship a visual with a labelled claim attached, such as floor areas or specification statements, unless
the numbers come from the drawings.
