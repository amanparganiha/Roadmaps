# FDE Roadmap — 6 Weeks Intensive (~3–4 hrs/day)

Every task links to a free resource (details and alternatives in [resources.md](resources.md)).
Weeks 1–2 build fundamentals, 3–4 build the AI stack, 5–6 build interview-specific muscle.
If you already know a topic, do its milestone anyway — if it's easy, skip ahead.

---

## Week 1 — Python, Git, SQL foundations

**Goal:** write clean Python fast, use Git naturally, query data confidently.

- [ ] Day 1–3: [CS50P](https://cs50.harvard.edu/python/) — do lectures 0–5 (functions, conditionals, loops, exceptions, libraries). Skip what you know; do the problem sets, not just videos. *(~3 hrs/day)*
- [ ] Day 3: [Learn Git Branching](https://learngitbranching.js.org/) — main + remote lessons. *(2 hrs)*
- [ ] Day 4–5: CS50P lectures 6–8 (file I/O, regex, OOP) + problem sets.
- [ ] Day 5–7: [SQLBolt](https://sqlbolt.com/) all lessons, then [SQL Practice](https://www.sql-practice.com/) — 20+ queries including JOINs and GROUP BY. *(~2 hrs/day)*
- [ ] Daily from Day 4: 1 easy problem on [NeetCode](https://neetcode.io/roadmap) (Arrays & Hashing) to warm up.

**Milestone project:** a CLI tool in Python that reads a CSV (find any dataset on [Kaggle](https://www.kaggle.com/datasets)), loads it into SQLite, and answers questions via SQL (e.g., "top 10 X by Y"). Commit it to GitHub with a README. *(~4 hrs)*

---

## Week 2 — DSA patterns + practical backend

**Goal:** handle a practical coding round; FDE coding is practical, not competitive.

- [ ] Day 1–5: [NeetCode roadmap](https://neetcode.io/roadmap) — Arrays & Hashing, Two Pointers, Sliding Window, Stack, Binary Search. Watch the pattern video, then solve 3–4 problems per pattern (~25 problems total). *(~2 hrs/day)*
- [ ] Day 1–4: [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) — through path/query params, request bodies, and response models. *(~1.5 hrs/day)*
- [ ] Day 5: Learn to call external APIs properly: [Real Python — API Integration](https://realpython.com/api-integration-in-python/) (auth, pagination, error handling, retries).
- [ ] Day 6–7: **Practical coding drills** (these mimic real FDE coding rounds — see [interview-prep.md](interview-prep.md)):
  - [ ] Build a rate limiter (token bucket) in plain Python with tests.
  - [ ] Write a robust CSV parser that survives malformed rows and reports errors.

**Milestone project:** a FastAPI service exposing your Week 1 dataset — 3 endpoints, input validation, meaningful error responses, README with curl examples. *(~4 hrs)*

---

## Week 3 — LLM fundamentals: prompting, APIs, tool use

**Goal:** be fluent in the LLM developer stack — the core of every 2026 FDE role.

- [ ] Day 1–2: [Anthropic Docs — Get started + Prompt engineering](https://docs.anthropic.com/) — read the full prompt engineering section; free tier API key is enough for exercises. Alternative track: [Prompting Guide](https://www.promptingguide.ai/).
- [ ] Day 2–3: [Anthropic courses repo](https://github.com/anthropics/courses) — work through the API fundamentals and prompt engineering interactive tutorials (Jupyter notebooks, free).
- [ ] Day 4: Structured output + tool use / function calling — Anthropic docs tool-use section, plus the [OpenAI Cookbook](https://cookbook.openai.com/) function-calling examples (know both providers' idioms).
- [ ] Day 5–6: [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) — chapters 1–2 (how transformers/tokenizers actually work; enough depth to answer "explain how an LLM works" credibly).
- [ ] Day 7: Read about production concerns: rate limiting, batching, caching, streaming, token costs — Anthropic/OpenAI docs sections on each. Write a one-page cheat sheet in your own words.

**Milestone project:** a CLI chatbot with tool use — it can answer questions about your Week 1 dataset by *deciding* to call your Week 2 API (function calling), with streamed responses and graceful API-error handling. *(~5 hrs)*

---

## Week 4 — RAG, agents, evals (the take-home simulator)

**Goal:** build the exact artifacts FDE take-homes ask for: a RAG system, an agent, an eval harness.

- [ ] Day 1–2: [DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses/) — take one RAG-focused short course (all free, ~1.5 hrs each).
- [ ] Day 2–3: Build a minimal RAG pipeline **from scratch, no framework**: chunk documents → embed → store in SQLite/numpy → retrieve top-k → answer with citations. Understanding beats frameworks in interviews.
- [ ] Day 4: [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) — unit 1 (agent fundamentals) + skim one framework unit.
- [ ] Day 5: [Model Context Protocol docs](https://modelcontextprotocol.io/) — read the intro and build the quickstart MCP server (Anthropic FDE postings name MCP explicitly).
- [ ] Day 6–7: **Evals** — the highest-leverage differentiator: read [Anthropic docs on evals](https://docs.anthropic.com/) (define success criteria, build eval sets) and [Hamel Husain — Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/). Then build a small eval harness for your RAG app: 15 question/expected-answer pairs, automated scoring (exact match + LLM-as-judge), a results table.

**Milestone project (treat as a real take-home, 5-hour budget):** "A customer wants to ask questions about their internal docs." Build RAG over a public doc set, an eval harness proving it works, and record a 5-minute walkthrough video (OpenAI's real take-home format includes video). *(~5 hrs)*

---

## Week 5 — System design, decomposition, customer skills

**Goal:** train the rounds that actually fail FDE candidates.

- [ ] Day 1–2: [System Design Primer](https://github.com/donnemartin/system-design-primer) — study the core concepts section (load balancing, caching, queues, DB scaling). You need vocabulary and trade-offs, not exhaustive depth.
- [ ] Day 2–3: LLM system design: sketch (on [Excalidraw](https://excalidraw.com/)) a production architecture for "enterprise chatbot over 1M internal documents, 10k users" — include ingestion, retrieval, guardrails, evals/monitoring, cost & latency budgets, auth/trust boundaries. Then compare against a reference: search "LLM system design" on the [Exponent blog](https://www.tryexponent.com/blog).
- [ ] Day 3–5: **Decomposition practice** — the Palantir-signature round (~40% pass rate). Learn the framework in [interview-prep.md](interview-prep.md), then write full decompositions (45 min timed, on paper/Excalidraw) for three prompts:
  - [ ] "A hospital network wants to reduce ER wait times."
  - [ ] "An airline wants to use AI to reduce flight delays."
  - [ ] "A bank wants to automate its loan-document review."
- [ ] Day 6: Product/customer sense: read Palantir's own writing on the FDE model — [Palantir blog](https://blog.palantir.com/) ("Forward Deployed Engineers" / open-ended interview posts) — and the [Exponent FDE interview guide](https://www.tryexponent.com/blog/forward-deployed-engineer-interview-the-definitive-2026-guide-fde).
- [ ] Day 7: Draft your 6–8 STAR behavioral stories (template in [interview-prep.md](interview-prep.md)).

**Milestone:** one polished decomposition writeup + your architecture diagram, explained out loud to a friend (or recorded) in under 10 minutes.

---

## Week 6 — Interview drills

**Goal:** convert knowledge into performance. Live in [interview-prep.md](interview-prep.md) this week — it has the day-by-day drill schedule.

- [ ] 2× mock coding interviews on [Pramp](https://www.pramp.com/) (free peer mocks).
- [ ] 1× timed practical coding drill daily (rotate: rate limiter, log parser, streaming consumer, mini-RAG — question bank in interview-prep.md).
- [ ] 2× timed decomposition cases (new prompts, 45 min hard stop).
- [ ] 1× client-simulation role-play with a friend: present your Week 4 project, have them push back ("too expensive", "it hallucinated yesterday", "why not fine-tune?").
- [ ] Rehearse STAR stories out loud; refine the weak ones.
- [ ] Polish GitHub: all 4 milestone projects with READMEs — this is your portfolio; FDE hiring managers read it.
- [ ] Apply: Palantir new-grad FDSE, Databricks, and 10+ AI startups (filter "forward deployed" on job boards).

**Final milestone:** a complete self-run mock loop in one day — coding (60 min) → system design (60 min) → decomposition (45 min) → behavioral (45 min). Score yourself with the rubrics in interview-prep.md.
