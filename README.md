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

| Prompt | Use it when | Tags |
| --- | --- | --- |
| [**Bid qualification: go or no-go**](prompts/01-preconstruction/01-bid-go-no-go.md) | An invitation to bid lands and you need a defensible recommendation before you spend a week estimating it. | `bidding` `risk` `preconstruction` |
| [**Constructability risk review of a drawing set**](prompts/01-preconstruction/02-constructability-risk-review.md) | You are pricing or planning a job and want a structured list of buildability questions before the bid goes in. | `preconstruction` `drawings` `risk` |
| [**Programme and sequencing options**](prompts/01-preconstruction/03-programme-and-sequencing-options.md) | You have a target completion date and a rough scope, and you want the plausible sequencing options on the table before you build a CPM schedule. | `preconstruction` `programme` `sequencing` |

### Estimating and takeoff

*Sanity checks, pricing narratives, and the questions an estimator should be asked.*

| Prompt | Use it when | Tags |
| --- | --- | --- |
| [**Unit rate sanity check**](prompts/02-estimating/01-unit-rate-sanity-check.md) | An estimate is nearly finished and you want a second pair of eyes on whether the rates and quantities hang together — before the bid goes in, not after. | `estimating` `pricing` `review` |
| [**Takeoff review checklist**](prompts/02-estimating/02-takeoff-review-checklist.md) | A takeoff has been produced — by a person, by software, or by one of the tools in our [open source construction tools](https://github.com/constructelligence-lab/open-source-construction-tools) list — and it needs a review that is actually systematic. | `takeoff` `quantities` `quality` |
| [**Change order pricing narrative**](prompts/02-estimating/03-change-order-pricing-narrative.md) | The numbers are agreed internally and now need to be presented so they are hard to argue with — typically for a priced change that a client or a subcontractor will scrutinise. | `change-orders` `commercial` `pricing` |
| [**Productivity assumption stress test**](prompts/02-estimating/04-productivity-assumption-stress-test.md) | An estimate depends on production rates you have assumed rather than measured, and you want to know how much of the margin is riding on them. | `productivity` `labour` `risk` |

### Architecture and design

*Briefs, specifications, code checks and design review preparation.*

| Prompt | Use it when | Tags |
| --- | --- | --- |
| [**Design brief from a client conversation**](prompts/03-architecture/01-design-brief-from-conversation.md) | You have come out of a client meeting with scattered notes and need a written brief that the client can confirm or correct before design work starts. | `brief` `client` `architecture` |
| [**Specification section draft**](prompts/03-architecture/02-specification-section-draft.md) | You need a first draft of a specification section structure so you are editing rather than staring at an empty document — with the understanding that the technical content is yours, not the model's. | `specification` `documentation` `quality` |
| [**Code and accessibility checklist for a design review**](prompts/03-architecture/03-code-and-accessibility-checklist.md) | You want a structured set of compliance questions to work through for a design, recognising that the model does not know your local code and must not be treated as knowing it. | `code` `accessibility` `compliance` |
| [**Design review agenda that finds problems**](prompts/03-architecture/04-design-review-agenda.md) | You are running a design or coordination review and want an agenda that surfaces conflicts rather than walking through the drawings in order. | `coordination` `meetings` `design` |

### Visualisation and rendering

*Image prompts, iteration, and the words that go around a render.*

| Prompt | Use it when | Tags |
| --- | --- | --- |
| [**Photorealistic exterior render prompt**](prompts/04-visualisation/01-photorealistic-exterior-render.md)<br>*ChatGPT, Gemini only* | You need a client-ready exterior visual quickly, before the model is advanced enough for a proper render, or to explore a façade direction. | `rendering` `visualisation` `marketing` |
| [**Interior render: iteration prompt**](prompts/04-visualisation/02-interior-render-iteration.md)<br>*ChatGPT, Gemini only* | The first interior image is close but wrong — the light, the proportions or the materials — and you want to change one thing at a time rather than regenerate from scratch. | `rendering` `interior` `iteration` |
| [**Render critique before it goes to the client**](prompts/04-visualisation/03-render-critique-before-client.md) | You are about to send a visual to a client and want a hard critique first — one that finds the things an architect, a planner or a contractor would spot immediately. | `rendering` `review` `presentation` |

### Engineering

*Structural and MEP sense checks, always with an engineer and never instead of one.*

| Prompt | Use it when | Tags |
| --- | --- | --- |
| [**Structural load path sanity check**](prompts/05-engineering/01-load-path-sanity-check.md) | You are preparing for a coordination or value-engineering discussion and want the obvious load path and stability questions on the table. | `structure` `review` `engineering` |
| [**MEP coordination and clash triage**](prompts/05-engineering/02-mep-coordination-clash-triage.md) | You have a clash report or a coordination problem list and need to decide which clashes matter, in what order to resolve them, and who should move. | `mep` `coordination` `bim` |

### Scheduling and planning

*Narratives, look-aheads and the records a delay claim is built from.*

| Prompt | Use it when | Tags |
| --- | --- | --- |
| [**Schedule narrative for the owner**](prompts/06-scheduling/01-schedule-narrative-for-owner.md) | The monthly schedule update is done and needs the narrative section: what moved, why, what you are doing about it, and what you need — without excuses and without jargon. | `schedule` `reporting` `communication` |
| [**Three-week lookahead constraint sweep**](prompts/06-scheduling/02-lookahead-constraint-sweep.md) | You are building the next three-week lookahead and want to remove constraints before they stop work, rather than reporting them after the fact. | `lookahead` `field` `planning` |

### Site and field operations

*Turning messy field notes into records somebody can act on.*

| Prompt | Use it when | Tags |
| --- | --- | --- |
| [**Daily report from messy field notes**](prompts/07-site-operations/01-daily-report-from-notes.md) | The day's notes are a mix of texts, voice-note reminders and scribbles, and the report needs to be written before you go home — with the facts intact and nothing invented. | `field` `records` `daily-report` |
| [**RFI drafting that gets answered**](prompts/07-site-operations/02-rfi-drafting.md) | Something on site does not match the drawings and you need an RFI that is clear enough to be answered first time, with the schedule impact stated. | `rfi` `documents` `coordination` |

### Safety and compliance

*Task-specific safety documents, written with a competent person.*

| Prompt | Use it when | Tags |
| --- | --- | --- |
| [**Job safety analysis from a task description**](prompts/08-safety/01-jsha-from-task-description.md) | You are preparing a task-specific safety analysis and want a structured first draft to edit with the crew, rather than starting from a template that says nothing about this job. | `safety` `jsha` `field` |
| [**Toolbox talk from a real near miss**](prompts/08-safety/02-toolbox-talk-from-near-miss.md) | Something nearly went wrong on this site and you want a five-minute talk that lands with the crew, rather than a generic briefing they have heard ten times. | `safety` `training` `briefing` |

### Contracts and commercial

*Notices, risk reviews and payment narratives, drafted for review.*

| Prompt | Use it when | Tags |
| --- | --- | --- |
| [**Contract risk review preparation**](prompts/09-commercial/01-contract-risk-review.md) | A contract or subcontract is on your desk and you want the risk topics organised before it goes to your lawyer, so the expensive hours are spent on judgement rather than on reading out loud. | `contracts` `risk` `commercial` |
| [**Notice letter draft**](prompts/09-commercial/02-notice-letter-draft.md) | An event has occurred and the contract requires written notice. | `notices` `claims` `correspondence` |

### Business development

*Case studies, proposals and the writing that wins the next job.*

| Prompt | Use it when | Tags |
| --- | --- | --- |
| [**Project case study from the facts**](prompts/10-business-development/01-case-study-from-facts.md) | You have finished a job worth writing about and need a case study for the website, a proposal or a prequalification pack — without inventing anything and without breaching confidentiality. | `marketing` `case-study` `bd` |
| [**Tailoring a proposal to the client's actual concerns**](prompts/10-business-development/02-proposal-tailoring.md) | You have a standard proposal structure and a specific client, and you want the document to answer what *they* are worried about instead of repeating your company history. | `proposals` `bidding` `bd` |

### Automation and analysis

*For the person who would rather script it than retype it.*

| Prompt | Use it when | Tags |
| --- | --- | --- |
| [**IFC data extraction script**](prompts/11-automation/01-ifc-data-extraction-script.md) | You need a repeatable way to pull data out of IFC models — quantities, spaces, properties — instead of clicking through them, and you would rather review code than write the boilerplate. | `ifc` `bim` `python` `automation` |
| [**Job cost analysis in Python or pandas**](prompts/11-automation/02-job-cost-analysis-in-python.md) | Your accounting system will give you a job cost export but not the analysis you want, and the work is repetitive enough to script rather than rebuild in a spreadsheet every month. | `job-cost` `python` `analysis` `automation` |
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

<!-- begin:family -->
## More from Constructelligence

Open construction resources from the same team, all maintained alongside this one:

| Repository | What it is |
| --- | --- |
| [AI in construction](https://github.com/constructelligence-lab/ai-in-construction) | A practical guide to AI in construction: what works today, what the data has to look like, the risks, and a 90-day plan. |
| [Construction data migration](https://github.com/constructelligence-lab/construction-data-migration) | A guide and toolkit for moving a contractor between systems, and proving nothing was lost. |
| [Construction project records](https://github.com/constructelligence-lab/construction-project-records) | Open schemas, templates and a checker for RFIs, submittals, change events, daily reports and punch lists. |
| [Construction reference data](https://github.com/constructelligence-lab/construction-data) | Cost codes, units, waste factors, pay units, trade sequence, glossary and metric formulas in CSV. |
| [Construction reference MCP server](https://github.com/constructelligence-lab/construction-mcp) | An offline MCP server that gives AI assistants construction reference data and calculators. |
| [Construction agent skills](https://github.com/constructelligence-lab/construction-agent-skills) | 28 installable agent skills for Claude Code and any agent that reads SKILL.md. |
| [Open source construction tools](https://github.com/constructelligence-lab/open-source-construction-tools) | Open source software for BIM, CAD, scheduling and site work, verified against the GitHub API. |

<!-- end:family -->

---

*Maintained by [Constructelligence](https://constructelligence.co) — building the AI infrastructure for
construction.*
