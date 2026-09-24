---
title: Toolbox talk from a real near miss
section: Safety and compliance
slug: toolbox-talk-from-near-miss
models: [ChatGPT, Claude, Gemini]
tags: [safety, training, briefing]
updated: 2026-09-24
---

## Use it when

Something nearly went wrong on this site and you want a five-minute talk that lands with the crew,
rather than a generic briefing they have heard ten times.

## The prompt

```text
You are a site safety lead writing a five-minute toolbox talk about something that
actually happened.

What happened: {{near_miss_description}}
Where and when: {{location_and_time}}
What could have happened: {{potential_outcome}}
What we changed afterwards: {{changes_made}}
Audience: {{audience}}

Write the talk in plain language, in this order:
1. What happened, told straight, including how ordinary the start of it was.
2. What would have had to be different for someone to be hurt.
3. The two things this crew should do differently, stated as actions rather than rules.
4. One question to ask the crew, so they talk rather than listen.

Keep it under 250 words, spoken language, no jargon and no blaming anyone. Do not name
the individual involved.
```

## What good output looks like

- Tells the story of how ordinary the conditions were, which is what makes a crew see themselves
  in it.
- Gives two concrete actions rather than a list of rules.
- Ends with a question, turning a briefing into a conversation.

## Follow-ups

- "Add three follow-up questions for a crew that goes quiet on safety discussions."
- "Write the record of the briefing, including the attendance line and the points raised."
- "What might this near miss be telling us about our method or our equipment rather than our people?"

## Guardrails

Talks must reflect what actually happened on this site and must not identify individuals or imply
blame. Investigations and disciplinary matters follow your own procedures, and anything reportable
must be handled through the required channels before it becomes training material.
