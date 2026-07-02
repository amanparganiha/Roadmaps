# Forward Deployed Engineer (FDE)

## What the role is

A Forward Deployed Engineer is a software engineer embedded directly with customers. Instead of building one product for everyone, you take your company's platform (Palantir Foundry, Claude, OpenAI's APIs, Databricks) into a specific customer's messy real-world environment and make it deliver value — writing integration code, building RAG pipelines and agents, running workshops, and owning the outcome end-to-end.

Palantir invented the role; in 2025–2026 OpenAI, Anthropic, Databricks, Google, and most serious AI startups adopted it because deploying AI into enterprises requires someone who is half engineer, half consultant.

## Who hires FDEs

| Company | Flavor |
|---|---|
| Palantir | The original. Heavy on decomposition and ambiguity. Foundry/AIP deployments. |
| OpenAI | Production LLM systems on their APIs; heavy focus on evals ("how do you know it's working?"). |
| Anthropic | Applied AI team; Claude integrations, MCP servers, agents; mission alignment matters. |
| Databricks | Data-flavored: Spark, SQL, lakehouse architecture, customer workshops. |
| AI startups | Broadest scope — you may be the entire deployment team. Easiest entry point for early-career. |

## The skills profile (T-shaped)

- **Deep bar**: strong practical coding (usually Python) — you must build working software fast.
- **Broad bar**: SQL and data pipelines, APIs, cloud basics, LLM stack (prompting, RAG, agents, evals, MCP).
- **Vertical bar (what actually differentiates FDEs)**: decomposing vague problems, communicating with non-technical stakeholders, radical ownership, product sense.

## What's in this package

| File | What it's for |
|---|---|
| [roadmap.md](roadmap.md) | 6-week intensive study plan (~3–4 hrs/day) with checkboxes |
| [interview-prep.md](interview-prep.md) | Interview loops by company, question bank, final-week drill schedule |
| [qa-bank.md](qa-bank.md) | Detailed questions **with answers**: LLM stack, coding walkthroughs, worked design & decomposition examples |
| [resources.md](resources.md) | Every free resource + free certifications, with why-this-one notes |

## How to use it

1. Work through `roadmap.md` top to bottom, checking off tasks. Don't skip milestone projects — they *are* the prep (FDE interviews test building, not trivia).
2. Read `interview-prep.md` at the start (know what you're training for), then live in it during week 6.
3. Everything links to a free resource. If a link dies, run `python tools/check_links.py roadmaps/fde/` and find a replacement in `resources.md` alternatives.

**Realistic expectation for a student**: big labs (OpenAI/Anthropic) rarely hire FDEs straight out of school — target Palantir new-grad FDE (called Forward Deployed Software Engineer), Databricks, and AI startups first. The same prep covers all of them, and startup FDE experience is the standard springboard to lab FDE roles in 1–2 years.
