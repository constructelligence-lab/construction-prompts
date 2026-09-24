# Construction prompts

A working library of prompts for **ChatGPT, Claude and Gemini**, written for construction and design
work: preconstruction, estimating, architecture, visualisation, engineering, scheduling, site
operations, safety, commercial and business development.

Every prompt is a file with the same five sections — when to use it, the prompt itself, what good
output looks like, follow-ups that sharpen the answer, and guardrails covering what never to paste
and what always to verify. The index below is **generated from those files**, and CI fails if it
drifts, so the library cannot quietly go stale.

<!-- begin:badge -->
![prompts](https://img.shields.io/badge/prompts-28-1f6feb) ![licence](https://img.shields.io/badge/licence-CC%20BY%204.0-2ea043) ![validated](https://img.shields.io/badge/index-validated%20in%20CI-6e7781)
<!-- end:badge -->

## How to use this library

1. **Find the decision, not the topic.** The sections are organised around work you are actually
   doing — pricing a bid, resolving a clash, answering a notice. Start there.
2. **Fill in the `{{placeholders}}`.** Every prompt has variables for the facts the model cannot
   know. Prompts fail far more often from missing context than from missing cleverness.
3. **Read the guardrails before you paste anything.** They say what must never go into a consumer
   tier tool, and what a person still has to check.
4. **Use the follow-ups.** The first answer is a draft. The follow-ups are where the work gets
   done: asking for the rows, the counter-argument, or the thing you have not considered.
5. **Keep it as a draft.** Everything here produces something a named person reviews before it
   leaves the company. That is not a formality, it is the control.

## The library

<!-- begin:index -->
### Preconstruction

*Qualifying work, framing the programme, finding the risk before you price it.*

| Prompt | File | Models | Tags |
| --- | --- | --- | --- |
| **Bid qualification: go or no-go** | [`01-bid-go-no-go.md`](prompts/01-preconstruction/01-bid-go-no-go.md) | ChatGPT, Claude, Gemini | `bidding` `risk` `preconstruction` |
| **Constructability risk review of a drawing set** | [`02-constructability-risk-review.md`](prompts/01-preconstruction/02-constructability-risk-review.md) | ChatGPT, Claude, Gemini | `preconstruction` `drawings` `risk` |
| **Programme and sequencing options** | [`03-programme-and-sequencing-options.md`](prompts/01-preconstruction/03-programme-and-sequencing-options.md) | ChatGPT, Claude, Gemini | `preconstruction` `programme` `sequencing` |

### Estimating and takeoff

*Sanity checks, pricing narratives, and the questions an estimator should be asked.*

| Prompt | File | Models | Tags |
| --- | --- | --- | --- |
| **Change order pricing narrative** | [`03-change-order-pricing-narrative.md`](prompts/02-estimating/03-change-order-pricing-narrative.md) | ChatGPT, Claude, Gemini | `change-orders` `commercial` `pricing` |
| **Productivity assumption stress test** | [`04-productivity-assumption-stress-test.md`](prompts/02-estimating/04-productivity-assumption-stress-test.md) | ChatGPT, Claude, Gemini | `productivity` `labour` `risk` |
| **Takeoff review checklist** | [`02-takeoff-review-checklist.md`](prompts/02-estimating/02-takeoff-review-checklist.md) | ChatGPT, Claude, Gemini | `takeoff` `quantities` `quality` |
| **Unit rate sanity check** | [`01-unit-rate-sanity-check.md`](prompts/02-estimating/01-unit-rate-sanity-check.md) | ChatGPT, Claude, Gemini | `estimating` `pricing` `review` |

### Architecture and design

*Briefs, specifications, code checks and design review preparation.*

| Prompt | File | Models | Tags |
| --- | --- | --- | --- |
| **Code and accessibility checklist for a design review** | [`03-code-and-accessibility-checklist.md`](prompts/03-architecture/03-code-and-accessibility-checklist.md) | ChatGPT, Claude, Gemini | `code` `accessibility` `compliance` |
| **Design brief from a client conversation** | [`01-design-brief-from-conversation.md`](prompts/03-architecture/01-design-brief-from-conversation.md) | ChatGPT, Claude, Gemini | `brief` `client` `architecture` |
| **Design review agenda that finds problems** | [`04-design-review-agenda.md`](prompts/03-architecture/04-design-review-agenda.md) | ChatGPT, Claude, Gemini | `coordination` `meetings` `design` |
| **Specification section draft** | [`02-specification-section-draft.md`](prompts/03-architecture/02-specification-section-draft.md) | ChatGPT, Claude, Gemini | `specification` `documentation` `quality` |

### Visualisation and rendering

*Image prompts, iteration, and the words that go around a render.*

| Prompt | File | Models | Tags |
| --- | --- | --- | --- |
| **Interior render: iteration prompt** | [`02-interior-render-iteration.md`](prompts/04-visualisation/02-interior-render-iteration.md) | ChatGPT, Gemini | `rendering` `interior` `iteration` |
| **Photorealistic exterior render prompt** | [`01-photorealistic-exterior-render.md`](prompts/04-visualisation/01-photorealistic-exterior-render.md) | ChatGPT, Gemini | `rendering` `visualisation` `marketing` |
| **Render critique before it goes to the client** | [`03-render-critique-before-client.md`](prompts/04-visualisation/03-render-critique-before-client.md) | ChatGPT, Claude, Gemini | `rendering` `review` `presentation` |

### Engineering

*Structural and MEP sense checks, always with an engineer and never instead of one.*

| Prompt | File | Models | Tags |
| --- | --- | --- | --- |
| **MEP coordination and clash triage** | [`02-mep-coordination-clash-triage.md`](prompts/05-engineering/02-mep-coordination-clash-triage.md) | ChatGPT, Claude, Gemini | `mep` `coordination` `bim` |
| **Structural load path sanity check** | [`01-load-path-sanity-check.md`](prompts/05-engineering/01-load-path-sanity-check.md) | ChatGPT, Claude, Gemini | `structure` `review` `engineering` |

### Scheduling and planning

*Narratives, look-aheads and the records a delay claim is built from.*

| Prompt | File | Models | Tags |
| --- | --- | --- | --- |
| **Schedule narrative for the owner** | [`01-schedule-narrative-for-owner.md`](prompts/06-scheduling/01-schedule-narrative-for-owner.md) | ChatGPT, Claude, Gemini | `schedule` `reporting` `communication` |
| **Three-week lookahead constraint sweep** | [`02-lookahead-constraint-sweep.md`](prompts/06-scheduling/02-lookahead-constraint-sweep.md) | ChatGPT, Claude, Gemini | `lookahead` `field` `planning` |

### Site and field operations

*Turning messy field notes into records somebody can act on.*

| Prompt | File | Models | Tags |
| --- | --- | --- | --- |
| **Daily report from messy field notes** | [`01-daily-report-from-notes.md`](prompts/07-site-operations/01-daily-report-from-notes.md) | ChatGPT, Claude, Gemini | `field` `records` `daily-report` |
| **RFI drafting that gets answered** | [`02-rfi-drafting.md`](prompts/07-site-operations/02-rfi-drafting.md) | ChatGPT, Claude, Gemini | `rfi` `documents` `coordination` |

### Safety and compliance

*Task-specific safety documents, written with a competent person.*

| Prompt | File | Models | Tags |
| --- | --- | --- | --- |
| **Job safety analysis from a task description** | [`01-jsha-from-task-description.md`](prompts/08-safety/01-jsha-from-task-description.md) | ChatGPT, Claude, Gemini | `safety` `jsha` `field` |
| **Toolbox talk from a real near miss** | [`02-toolbox-talk-from-near-miss.md`](prompts/08-safety/02-toolbox-talk-from-near-miss.md) | ChatGPT, Claude, Gemini | `safety` `training` `briefing` |

### Contracts and commercial

*Notices, risk reviews and payment narratives, drafted for review.*

| Prompt | File | Models | Tags |
| --- | --- | --- | --- |
| **Contract risk review preparation** | [`01-contract-risk-review.md`](prompts/09-commercial/01-contract-risk-review.md) | ChatGPT, Claude, Gemini | `contracts` `risk` `commercial` |
| **Notice letter draft** | [`02-notice-letter-draft.md`](prompts/09-commercial/02-notice-letter-draft.md) | ChatGPT, Claude, Gemini | `notices` `claims` `correspondence` |

### Business development

*Case studies, proposals and the writing that wins the next job.*

| Prompt | File | Models | Tags |
| --- | --- | --- | --- |
| **Project case study from the facts** | [`01-case-study-from-facts.md`](prompts/10-business-development/01-case-study-from-facts.md) | ChatGPT, Claude, Gemini | `marketing` `case-study` `bd` |
| **Tailoring a proposal to the client's actual concerns** | [`02-proposal-tailoring.md`](prompts/10-business-development/02-proposal-tailoring.md) | ChatGPT, Claude, Gemini | `proposals` `bidding` `bd` |

### Automation and analysis

*For the person who would rather script it than retype it.*

| Prompt | File | Models | Tags |
| --- | --- | --- | --- |
| **IFC data extraction script** | [`01-ifc-data-extraction-script.md`](prompts/11-automation/01-ifc-data-extraction-script.md) | ChatGPT, Claude, Gemini | `ifc` `bim` `python` `automation` |
| **Job cost analysis in Python or pandas** | [`02-job-cost-analysis-in-python.md`](prompts/11-automation/02-job-cost-analysis-in-python.md) | ChatGPT, Claude, Gemini | `job-cost` `python` `analysis` `automation` |
<!-- end:index -->

## Anatomy of a prompt here

| Section | What it is for |
| --- | --- |
| **Use it when** | The specific moment this prompt earns its place, in one or two sentences |
| **The prompt** | The text to paste, with `{{variables}}` for your facts and the output format built in |
| **What good output looks like** | How to tell a useful answer from a fluent one |
| **Follow-ups** | Two or three refinements that turn a first draft into something usable |
| **Guardrails** | What never goes into the tool, and what a person must verify afterwards |

Two habits make the difference between these working and not. **Give the model the numbers** — a
prompt asking for a "sanity check on our estimate" gets generic advice; a prompt with your unit
rates, quantities and basis gets an argument you can test. And **ask for the counter-case**, because
a model asked to justify a number will justify it, whether or not it deserves it.

## Model notes

All prompts are written to work on any of the three. Where behaviour differs:

| Situation | ChatGPT | Claude | Gemini |
| --- | --- | --- | --- |
| Long documents (specs, contracts) | Good, watch the context limit | Strong: handles long, dense text well | Good, generous context |
| Structured output (tables, schedules) | Ask explicitly for a table or JSON | Follows a stated schema closely | Ask explicitly, then confirm the format |
| Arithmetic and unit conversions | Verify every number: it will do the maths confidently | Better at showing its working | Verify every number |
| Images and renders | Strong for image generation and critique | Text-side critique is strong; image generation is separate | Good image generation, watch style drift |
| Tone for client-facing writing | Can drift to marketing | Usually plainer and easier to edit | Can drift to marketing |

The rule that covers all three: **the model drafts, a person decides.** Nothing here is a substitute
for an estimator's judgement, an engineer's calculation, a competent person's assessment, or your
lawyer's reading of a contract.

## Ground rules

- **Never paste** contracts under negotiation, pricing or bid strategy, personal or medical data,
  anything under an NDA, or anything a client has asked you to protect.
- **Always verify** quantities, dates, clause references, code sections and any figure that will
  leave the company.
- **Use a business tier** with terms that exclude your data from model training, and a written
  company rule on what may be pasted.
- **A person owns every output.** If nobody's name is on it, it is not ready to send.

## Contributing

Add a file under `prompts/<section>/` with the same five sections, then run:

```bash
python3 scripts/build_index.py    # regenerate the index and badge
python3 scripts/validate.py       # check structure consistency
```

A useful contribution says where the prompt came from — a real job, a real failure mode — and what
it is bad at. Prompts that only sound impressive do not belong here.

## Licence and disclaimer

Prompts and documentation: **CC BY 4.0**. Use them, adapt them, credit the source.

This is general material, not advice for a specific project. Nothing here replaces a competent
person on site, a qualified engineer's calculation, your contracts, or your lawyer, broker and
insurer.

---

*Maintained by [Constructelligence](https://constructelligence.co) — building the AI infrastructure for
construction.*
