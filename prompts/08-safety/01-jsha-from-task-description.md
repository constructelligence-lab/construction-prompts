---
title: Job safety analysis from a task description
section: Safety and compliance
slug: jsha-from-task-description
models: [ChatGPT, Claude, Gemini]
tags: [safety, jsha, field]
updated: 2026-09-24
---

## Use it when

You are preparing a task-specific safety analysis and want a structured first draft to edit with the
crew, rather than starting from a template that says nothing about this job.

## The prompt

```text
You are a safety professional preparing a job safety analysis for review by a competent
person on site.

Task: {{task_description}}
Location and conditions: {{location_conditions}}
Crew and experience level: {{crew}}
Equipment and materials involved: {{equipment}}
Adjacent activities and interfaces: {{adjacent_activities}}
Controls we already have in place: {{existing_controls}}

Produce a first draft with these sections:
1. Task steps, in sequence, as a worker would actually do them (six to ten steps).
2. For each step: the hazards, and the control that removes or reduces each hazard.
3. The controls broken into elimination or substitution, engineering, administrative and
   personal protective equipment, so it is visible where we have relied on PPE.
4. What must be verified before work starts.
5. What would make us stop and reassess.

Mark anything that depends on site-specific conditions I have not told you about.
```

## What good output looks like

- Steps reflect how the work is really done, including the awkward parts, not an idealised method.
- Controls are ranked, so it is obvious where PPE is the only defence left.
- Includes stop-work triggers, which is the part that matters when conditions change at 3pm.

## Follow-ups

- "Rewrite the top three hazards as a pre-task briefing the foreman can deliver in five minutes."
- "What training or certification must be verified for this task, and who verifies it?"
- "What would a regulator or an insurer expect to see recorded for a task like this?"

## Guardrails

A generated analysis is not a risk assessment and never replaces the competent person's judgement on
site. Every control must be checked against the actual location and conditions, the manufacturer's
instructions, the applicable regulations, and the workers doing the task.
