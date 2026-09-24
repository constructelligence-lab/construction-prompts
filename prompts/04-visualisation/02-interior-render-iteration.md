---
title: Interior render: iteration prompt
section: Visualisation and rendering
slug: interior-render-iteration
models: [ChatGPT, Gemini]
tags: [rendering, interior, iteration]
updated: 2026-09-24
---

## Use it when

The first interior image is close but wrong — the light, the proportions or the materials — and you
want to change one thing at a time rather than regenerate from scratch.

## The prompt

```text
Refine the previous interior image. Change only what is listed; keep the geometry,
camera and mood otherwise identical.

Room: {{room_type}}, approximately {{room_size}}.
What is right about the current image: {{what_to_keep}}.
What must change: {{what_to_change}}.
Materials to keep: {{materials}}.
Lighting to keep: {{lighting}}.

Specific changes:
1. {{change_one}}
2. {{change_two}}
3. {{change_three}}

Keep: realistic scale for {{room_type}}, believable ceiling height, no furniture
floating, consistent light direction from {{light_source}}, photographic exposure.
Avoid: text, logos, fisheye distortion, duplicated furniture, impossible joinery.
```

## What good output looks like

- Only the requested things changed, which is how you keep a client-approved image recognisable.
- Realistic daylight behaviour for the room type: an office at {{time}} should not look like a
  showroom lit for a brochure.
- Believable scale cues — door heights, furniture, ceiling grid — because that is what clients
  actually read.

## Follow-ups

- "Now produce the same room at {{time_of_day}} with blinds half closed."
- "Give me the same image with a wider camera and the ceiling visible."
- "Describe the changes a client is most likely to ask for based on this image."

## Guardrails

Keep an approved version of any image a client has signed off, so an iteration cannot overwrite the
record. Never present an interior image as a specification of finishes — schedules and
specifications govern, not pictures.
