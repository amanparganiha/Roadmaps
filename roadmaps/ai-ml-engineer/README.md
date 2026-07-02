# AI/ML Engineer

## What the role is

An AI/ML Engineer builds, ships, and maintains machine learning systems in production. In 2026 the role has two overlapping flavors:

- **Classic MLE**: trains and deploys models — feature pipelines, training, serving, monitoring (recommendation, ranking, forecasting, vision).
- **AI Engineer (GenAI)**: builds on top of foundation models — RAG pipelines, agents, fine-tuning, eval harnesses, LLM serving. This is where most entry-level hiring happens now.

Entry-level interviews test both: you need classic ML fundamentals *and* the modern LLM stack. Companies stopped asking candidates to recite gradient descent; they now test whether you can design a system, measure whether it works, and debug it when it breaks in production.

## Who hires

| Segment | Notes |
|---|---|
| Big tech (Google, Meta, Amazon, Microsoft) | Formal MLE ladders; heaviest on fundamentals + ML system design; some DSA rounds. |
| AI-native companies (OpenAI, Anthropic, Mistral, Cohere) | Rarely entry-level; strong engineering bar; get there via 1–2 years elsewhere. |
| Startups & scale-ups | Most realistic entry point; GenAI-heavy (RAG, agents, evals); portfolio matters more than pedigree. |
| Non-tech enterprises (banks, retail, health) | Underrated: less competition, classic ML + increasingly GenAI. |

## The skills profile

- **Fundamentals**: linear algebra & stats intuition, classic ML (regression, trees, clustering, bias/variance, cross-validation), deep learning basics.
- **Engineering**: solid Python, pandas/NumPy, PyTorch, SQL, Git, Docker basics, one cloud.
- **Modern stack (2026 must-have)**: transformers/LLMs, RAG, fine-tuning vs prompting judgment, eval frameworks, agents.
- **Production sense**: serving, monitoring, drift, cost/latency trade-offs, debugging models that were fine yesterday.

## What's in this package

| File | What it's for |
|---|---|
| [roadmap.md](roadmap.md) | 6-week intensive study plan (~3–4 hrs/day) with checkboxes |
| [interview-prep.md](interview-prep.md) | Round types, question bank, ML system design framework, final-week drills |
| [qa-bank.md](qa-bank.md) | Detailed questions **with answers**: ML fundamentals, deep learning, LLMs, from-scratch code, worked system design |
| [resources.md](resources.md) | Every free resource + free certifications, with why-this-one notes |

## How to use it

1. Follow `roadmap.md` in order — it builds classic ML → deep learning → LLMs → production, each on top of the last.
2. The milestone projects become your portfolio; entry-level MLE hiring is portfolio-driven.
3. Read `interview-prep.md` up front, drill from it in week 6.
4. Links break; run `python tools/check_links.py roadmaps/ai-ml-engineer/` and swap in alternatives from `resources.md`.

**Overlap note:** weeks 1 and 4 share material with the [FDE package](../fde/) (Python/SQL, RAG/evals). If you prepare both roles, do this roadmap first — AI/ML prep is a superset of the FDE technical bar; FDE adds the customer/decomposition layer on top.
