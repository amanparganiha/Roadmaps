# FDE Interview Prep

What the loops look like, what each round tests, real question types, and the week-6 drill schedule.

---

## The generic FDE loop (5–8 stages, 3–6 weeks)

1. **Recruiter screen** (30 min) — background, motivation, comp alignment
2. **Hiring manager screen** (45–60 min) — past projects, ownership stories
3. **Coding** (60 min) — practical engineering, not LeetCode hard
4. **System design** (60 min) — real deployment architecture
5. **Decomposition / case study** (45–60 min) — vague enterprise problem
6. **Client simulation** (45 min) — role-play with a "customer"
7. **Behavioral** (45 min) — STAR stories, culture fit

## Company-specific loops

### Palantir (FDSE — best new-grad entry point)
- Loop: recruiter → technical phone screen → onsite of 3–5 rounds (coding in Python, system design/data architecture, 1–2 behavioral/culture).
- **The decomposition round is the differentiator**: ~40% pass rate, ~30% of total weight. A vague customer problem, 45–60 min, graded on *process* not conclusion.
- Read their published guidance on open-ended questions ([Palantir blog](https://blog.palantir.com/)).

### OpenAI
- ~7 stages compressed into 3–4 weeks: recruiter → technical screen → 2 coding rounds → LLM system design → behavioral customer-empathy → values conversation.
- **Take-home**: ~5 hours building on their APIs (RAG system, agent, or eval harness) + a **video walkthrough**. Follow-ups go deep on design choices: RAG vs fine-tuning vs prompting, guardrails, evals.
- Signature question energy: *"How do you know it's working?"* — always have an eval answer.
- Production depth expected: rate limiting, batching, caching, prompt robustness, token cost & latency budgets.

### Anthropic (Applied AI)
- 5 stages: recruiter → technical phone screen → take-home or live coding → **customer-conversation simulation** → onsite system design.
- The customer-conversation round filters ~60% of candidates who passed coding — practice the client role-play seriously.
- System design skews toward **eval harnesses** ("can you measure whether Claude is actually helping this customer?") more than RAG architecture.
- Coding is practical: rate limiters, distributed queues. Mission alignment is genuinely screened.

### Databricks
- Data-flavored: Spark, SQL, data modeling, lakehouse architecture, plus customer-workshop collaboration scenarios.

---

## Question bank by round

### Coding (practical)
- Build a rate limiter (token bucket / sliding window) with tests.
- Parse a messy CSV/log file; handle malformed rows; report errors usefully.
- Consume a paginated/streaming API with retries and backoff.
- Build a minimal RAG pipeline: chunk → embed → retrieve → answer.
- Deduplicate/join two messy datasets (the "customer data is garbage" special).
- **Graded on:** clean code, narrating your thinking, catching your own bugs, handling edge cases without being told.

### System design
- "Design a chatbot over a customer's 1M internal documents for 10k employees."
- "Design the data pipeline to sync a customer's on-prem SQL Server into our platform daily."
- "A customer wants an agent that files support tickets automatically. Design it, including guardrails."
- **Graded on:** data flow mapping, trust boundaries/auth, observability, failure modes, cost/latency budgets, and proposing a *walking-skeleton MVP first* then iterating.

### Decomposition / case (train hardest for this)
Prompts are deliberately vague: *"A shipping company wants to reduce fuel costs."* / *"A hospital wants to cut ER wait times."*

**The framework:**
1. **Clarify before solving** (5–10 min): Who is the user? What does success look like, in numbers? What data exists? What constraints (regulatory, timeline, budget)?
2. **State assumptions explicitly** when answers aren't available.
3. **Decompose** the problem into 3–5 workstreams; draw the map.
4. **Prioritize** — which piece first and *why* (value × feasibility).
5. **Propose a minimal end-to-end slice** (walking skeleton) before any grand architecture.
6. **Name trade-offs and risks** transparently; say what would change your mind.

**Instant-fail behaviors:** jumping straight to a solution, no clarifying questions, ignoring the user, treating it as a tech-stack quiz.

### Client simulation
- "Present your solution to our CTO" (they play a skeptical CTO).
- "The model gave a wrong answer in the customer's demo yesterday. The VP is angry. Handle the call."
- "The customer demands a feature that's a bad idea. Respond."
- **Strong patterns:** diagnostic questions before proposals, ownership language ("I'll own getting you an answer by Friday"), calibrated commitments (never overpromise), translating tech → business impact, delivering bad news with a plan attached.

### Behavioral (prepare 6–8 STAR stories)
Cover these themes (one story can cover two):
1. Owned something end-to-end, including parts that weren't your fault
2. Dealt with a difficult stakeholder/teammate
3. Made a call with incomplete information
4. Were wrong and reversed course
5. Delivered under a hard deadline
6. Explained something technical to a non-technical person
7. Went beyond the ask because it was right for the user/customer
8. Failed, and what you changed afterwards

Format: Situation (2 sentences) → Task → Action (the bulk — *your* actions, "I" not "we") → Result (with a number if possible).

---

## Week-6 drill schedule

| Day | Drill (~3–4 hrs) |
|---|---|
| 1 | Timed practical coding (rate limiter, 60 min) + rehearse 4 STAR stories out loud |
| 2 | [Pramp](https://www.pramp.com/) mock #1 + review; timed decomposition case (45 min, new prompt) |
| 3 | LLM system design solo (60 min on Excalidraw, explain out loud) + rehearse other 4 STAR stories |
| 4 | Client simulation with a friend (they play angry VP) + timed coding (log parser) |
| 5 | Pramp mock #2 + timed decomposition case #2 |
| 6 | **Full self-run loop:** coding 60' → design 60' → decomposition 45' → behavioral 45'. Score honestly. |
| 7 | Patch weakest round; polish GitHub READMEs; send applications |

## Self-scoring rubric (per round, 1–4)

- **1** — Needed prompting to make progress; froze on edge cases or pushback
- **2** — Reached an answer but skipped clarification/tests/trade-offs
- **3** — Solid process: clarified, structured, verified, communicated
- **4** — Hire signal: also flagged risks unprompted, proposed evals/next steps, made it a conversation

Anything ≤2 gets a targeted retry the next day.

---

## Sources worth reading in full (all free)

- [Exponent — FDE Interview: The Definitive 2026 Guide](https://www.tryexponent.com/blog/forward-deployed-engineer-interview-the-definitive-2026-guide-fde)
- [Palantir blog](https://blog.palantir.com/) — their own posts on FDEs and open-ended interviews
- [Glassdoor — Palantir FDSE interview reports](https://www.glassdoor.com/Interview/Palantir-Technologies-Forward-Deployed-Software-Engineer-Interview-Questions-EI_IE236375.0,21_KO22,56.htm) (real recent questions; needs free account)
- [The New Stack — Why OpenAI and Anthropic are hiring FDE teams](https://thenewstack.io/forward-deployed-engineers-ai/)
