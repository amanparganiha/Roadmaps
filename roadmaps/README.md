# Role Prep Roadmaps

Intensive (4–6 week, ~3–4 hrs/day) interview prep packages built from **free resources only**, aimed at student / early-career candidates.

**👉 Easiest way to read everything: open [`index.html`](index.html) in your browser** — role tabs, collapsible Q&A, clickable checkboxes with saved progress. Rebuild it after editing any markdown: `python tools/build_ui.py`

## Roles

| Role | Package | One-line pitch |
|---|---|---|
| Forward Deployed Engineer | [fde/](fde/) | Half engineer, half consultant — deploy AI into real customer environments (Palantir, OpenAI, Anthropic, Databricks). |
| AI/ML Engineer | [ai-ml-engineer/](ai-ml-engineer/) | Build and ship ML/LLM systems in production — classic ML fundamentals + the 2026 GenAI stack. |
| Computer Vision Engineer | [computer-vision-engineer/](computer-vision-engineer/) | OpenCV → CNNs → detection/segmentation → CLIP/SAM/VLMs → edge deployment. Builds on AI/ML weeks 1–3. |
| Remote AI Career (strategy) | [remote-ai-career/](remote-ai-career/) | Convert the skills into a well-paid remote job: positioning, pipeline, freelance route, negotiation scripts. |
| VL-JEPA Concepts (thesis) | [vl-jepa-concepts/](vl-jepa-concepts/) | The 7-phase curriculum behind the LiveJEPA M.Tech thesis: JEPA, InfoNCE/CLIP, SONAR, selective decoding. |

## Each package contains

- **README.md** — what the role is, who hires, the skills profile
- **roadmap.md** — week-by-week checkbox plan; every task links to a free resource; weekly milestone projects that become your portfolio
- **interview-prep.md** — real interview loops by company, question banks by round, drill schedules, scoring rubrics
- **qa-bank.md** — detailed questions **with full answers**: fundamentals, coding walkthroughs with code, worked system-design/decomposition examples, behavioral skeletons
- **resources.md** — every resource used, with a why-this-one note and time estimate, plus free certifications

## How to use

1. Pick a role, read its README, then work through roadmap.md top to bottom.
2. Doing both? Do **AI/ML Engineer first** — its technical prep is a superset of the FDE bar; FDE adds decomposition + customer skills on top (weeks 5–6 of the FDE plan).
3. Check links stay alive: `python tools/check_links.py roadmaps/`

## Adding a new role

Follow `workflows/create_role_prep.md` — research the role → research the interview loop → curate free resources → write the four docs → verify links → add a row to the table above.
