# Roadmaps — Role Prep Tracker

Self-built interview-prep and learning tracker: week-by-week roadmaps, question banks **with answers**, and curated free resources for the roles I'm targeting — plus the learning curriculum behind my M.Tech thesis (LiveJEPA / VL-JEPA).

**📖 Read it:** [`roadmaps/`](roadmaps/README.md) — all content is plain markdown.
**🖥️ Use it:** open [`roadmaps/index.html`](roadmaps/index.html) in a browser — a self-contained UI (no server) with role tabs, collapsible Q&A, clickable checkboxes with saved progress, light/dark themes.

## Tracks

| Track | What it is |
|---|---|
| [Computer Vision Engineer](roadmaps/computer-vision-engineer/README.md) | OpenCV → CNNs → detection/segmentation → CLIP/SAM/VLMs → edge deployment |
| [AI/ML Engineer](roadmaps/ai-ml-engineer/README.md) | Classic ML fundamentals + the GenAI stack (RAG, agents, evals) |
| [Forward Deployed Engineer](roadmaps/fde/README.md) | The customer-facing AI engineering role (Palantir/OpenAI/Anthropic-style) |
| [Remote AI Career](roadmaps/remote-ai-career/README.md) | Strategy: positioning, pipeline, freelancing, salary negotiation |
| [VL-JEPA Concepts](roadmaps/vl-jepa-concepts/README.md) | 7-phase curriculum behind my thesis: JEPA, InfoNCE/CLIP, SONAR, selective decoding |

## How it's built

Markdown is the source of truth; a small Python generator compiles it into the single-file UI:

```
python tools/build_ui.py      # rebuild roadmaps/index.html from the markdown
python tools/check_links.py roadmaps/   # verify every resource link is alive
```

Structure follows a workflows/tools split: `workflows/` holds the SOP for adding a new role track, `tools/` holds the deterministic scripts.
