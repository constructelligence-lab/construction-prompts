---
title: Productivity assumption stress test
section: Estimating and takeoff
slug: productivity-assumption-stress-test
models: [ChatGPT, Claude, Gemini]
tags: [productivity, labour, risk]
updated: 2026-09-24
---

## Use it when

An estimate depends on production rates you have assumed rather than measured, and you want to
know how much of the margin is riding on them.

## The prompt

```text
You are a labour planner for {{trade_scope}} work.

Our estimate assumes:
{{assumed_rates_and_quantities}}

Basis for those assumptions: {{basis}}
Our own history on similar work: {{historical_rates}}
Crew composition planned: {{crew_plan}}

Stress test the assumptions:
1. Which assumption does the most damage if it is wrong by 15 percent?
2. Which are most likely to be wrong on this job given the conditions I described?
3. For each, what is the early indicator that would tell me within four weeks?
4. What would the labour cost be at 85 percent, 100 percent and 115 percent of the
   assumed productivity, all else equal?

Give me the sensitivity as a table, then the two assumptions worth measuring on site
rather than arguing about.
```

## What good output looks like

- Identifies which assumption drives the outcome rather than treating all as equally risky.
- Proposes measurable early indicators, which is what turns a risk into a managed one.
- Shows the arithmetic so you can check it, and does not pretend to know your rates.

## Follow-ups

- "Build me the weekly tracking sheet for the two indicators you chose."
- "What crew change would recover the 85 percent case, and what would it cost?"
- "Rewrite the sensitivity table as something I can show a client without exposing our margin."

## Guardrails

Labour rate and margin information should stay out of consumer tier tools. The sensitivity is only
as good as the range you supply, and it must be rebuilt with your own measured rates once the job
has four weeks of data.
