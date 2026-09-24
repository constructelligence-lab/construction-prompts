---
title: MEP coordination and clash triage
section: Engineering
slug: mep-coordination-clash-triage
models: [ChatGPT, Claude, Gemini]
tags: [mep, coordination, bim]
updated: 2026-09-24
---

## Use it when

You have a clash report or a coordination problem list and need to decide which clashes matter, in
what order to resolve them, and who should move.

## The prompt

```text
You are an MEP coordinator triaging a clash list for a {{project_type}} project.

Clashes or conflicts:
{{clash_list}}

Ceiling void available: {{void_depth}}
Zones with special requirements: {{special_zones}}
Services with priority established by specification: {{service_priorities}}
Programme pressure: {{programme_notes}}

Triage the list. For each item:
- which service should move, and why that service rather than the other
- whether it is a real clash or a modelling artefact
- the cost and programme consequence of resolving it in the field instead
- who should decide, and by when

Then give me the five items to resolve in the coordination meeting this week, and the
pattern you notice across the list that suggests an underlying cause.
```

## What good output looks like

- Applies consistent priority logic — gravity drainage and duct sizes usually constrain what can
  move — rather than listing everything as equally urgent.
- Separates real conflicts from modelling noise, which is where most of the list usually is.
- Names a cause pattern, which is the output that stops the same clash appearing next week.

## Follow-ups

- "Turn the top five into an agenda with the disciplines that must attend."
- "Draft the coordination note for a clash that requires a design change rather than a move."
- "What should we add to the coordination checklist so this pattern stops recurring?"

## Guardrails

Clash resolution is a design decision. Anything that changes a route, a size or a penetration needs
the responsible discipline's approval, and the required clearances and code-driven separations must
come from the specification, not from a model's suggestion.
