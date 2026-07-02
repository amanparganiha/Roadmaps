# FDE Question & Answer Bank

Detailed questions **with answers** for every FDE round. Don't memorize — rehearse out loud until you can explain each in your own words. Questions marked ⭐ come up in almost every loop.

---

## Part 1 — LLM & AI stack (technical screen + system design follow-ups)

### ⭐ Q1. Explain how an LLM works to a smart non-technical customer.
**Answer:** "An LLM is a program trained on a huge amount of text to do one thing extremely well: predict the next word given everything before it. Do that billions of times during training and it internalizes grammar, facts, and reasoning patterns. When you ask it a question, it generates the answer one token at a time, each choice informed by your prompt and what it has generated so far. Two consequences matter for your business: it doesn't 'look things up' — it generates, so it can be confidently wrong (that's why we add retrieval and checks) — and it's probabilistic, so we design systems around verification, not blind trust."
*Why this answer works: it's accurate, jargon-free, and pivots to deployment implications — exactly the FDE skill being tested.*

### ⭐ Q2. RAG vs fine-tuning vs prompt engineering — when do you use each?
**Answer:** Decision order is prompt → RAG → fine-tune:
- **Prompt engineering** first: zero infra, instant iteration. Solves tone, format, task instructions, few-shot patterns. Exhaust this before anything else.
- **RAG** when the model needs *knowledge it doesn't have*: private docs, fresh data, citations. Knowledge stays updatable without retraining, and you get source attribution — usually mandatory in enterprise.
- **Fine-tuning** when the model needs a *behavior/skill* prompts can't reliably produce: strict output formats, domain-specific style, or latency/cost pressure (a small fine-tuned model replacing a big prompted one). It does not reliably add facts — that's the classic misuse.
- In practice you combine them: fine-tune for format, RAG for knowledge, prompts for task framing.

### ⭐ Q3. What is a context window and what are its practical implications?
**Answer:** The maximum number of tokens (prompt + response) the model can attend to in one call. Implications: (1) you can't dump the whole knowledge base in — hence retrieval to select only relevant chunks; (2) cost and latency scale with input size, so stuffing the context wastes money; (3) models attend unevenly across very long contexts, so put critical instructions and the most relevant content near the start or end; (4) long conversations need summarization or truncation strategies or they exhaust the window.

### Q4. What are embeddings and how does semantic search work?
**Answer:** An embedding maps text to a vector such that semantically similar texts land close together. Semantic search: embed all documents offline and store the vectors; at query time embed the query and find nearest neighbors by cosine similarity. Unlike keyword search it matches *meaning* ("reset my password" matches "credential recovery procedure"). Production tip that earns points: hybrid search (keyword BM25 + vector) usually beats either alone, because exact identifiers (error codes, product names) are where pure vector search fails.

### ⭐ Q5. The customer's chatbot is hallucinating. Walk through your mitigation strategy.
**Answer:** Layered, in order of leverage:
1. **Ground it** — RAG so answers come from retrieved sources; instruct "answer only from the provided context; if it's not there, say you don't know."
2. **Require citations** — forcing the model to cite passage IDs both reduces fabrication and makes errors auditable.
3. **Tune retrieval** — most "hallucinations" are actually retrieval misses: the model never got the right passage. Check retrieval quality first before blaming the model.
4. **Add evals** — a test set of known Q&A pairs, measure groundedness (an LLM-judge checking "is every claim supported by the sources?"), track it per release.
5. **Guardrails for high-stakes paths** — confidence thresholds, human review queues for low-confidence answers, and scoped refusals.
Never promise zero hallucination — promise a measured rate and a mitigation process. That honesty is itself an FDE interview signal.

### ⭐ Q6. How do you evaluate an LLM application? ("How do you know it's working?")
**Answer:** This is OpenAI's favorite question. Structure:
1. **Define success with the customer in business terms** (deflection rate, time saved, accuracy on their gold cases) before any technical metric.
2. **Build an eval set**: 50–200 real examples with expected outcomes — sourced from the customer's actual tickets/docs, not synthetic only.
3. **Automate scoring**: exact/fuzzy match where answers are deterministic; **LLM-as-judge** with a rubric for open-ended answers (validate the judge against ~30 human-labeled samples first).
4. **Evaluate components separately**: retrieval (does the right chunk appear in top-k? — recall@k) vs generation (is the answer faithful to the chunks?). Otherwise you can't debug.
5. **Run on every change** — prompts are code; a prompt tweak that helps one case silently breaks others. CI for prompts.
6. **Close the loop in production**: thumbs up/down, sampled human review, drift monitoring; feed failures back into the eval set.

### Q7. What is MCP (Model Context Protocol) and why does it matter?
**Answer:** An open protocol (from Anthropic) standardizing how AI applications connect to external tools and data sources. An MCP server exposes tools/resources (query the CRM, search the wiki); any MCP-compatible client can use them without custom integration code per pairing — "USB-C for AI integrations." For FDEs it matters because customer deployments are mostly integration work: build one MCP server for a customer system and every agent/assistant in the org can use it. Anthropic FDE job postings name shipping MCP servers as a core deliverable.

### Q8. What is an agent, and when would you *not* use one?
**Answer:** An agent is an LLM in a loop with tools: it decides an action, executes, observes results, and repeats until done — the model does the orchestration. Don't use one when the workflow is known and fixed: if the steps are "always extract → validate → file the ticket," write a pipeline with one LLM call per step — cheaper, faster, debuggable, and reliability compounds (95% per step across 5 autonomous decisions is ~77%). Use agents when paths genuinely vary per input and can't be enumerated. Interview signal: engineers who reach for the simplest thing that works.

### Q9. How do you manage cost and latency in a production LLM system?
**Answer:** - **Model routing**: small/fast model for easy cases (classification, routing), big model only where quality demands it.
- **Caching**: prompt caching for repeated system prompts and doc contexts (huge in RAG); response caching for repeated queries.
- **Prompt size discipline**: retrieval instead of context-stuffing; trim boilerplate; token budgets per component.
- **Streaming** to cut *perceived* latency; **batching** for offline workloads (batch APIs are ~50% cheaper).
- **Measure first**: per-request token logs by feature, then optimize the actual top cost drivers.

### Q10. Temperature and other sampling parameters — what do they do?
**Answer:** Temperature scales the randomness of next-token selection: low (0–0.3) → deterministic, repeatable — right for extraction, classification, code, factual Q&A; higher (0.7–1.0) → varied, creative — right for brainstorming and drafting. Enterprise default is low. Related: top-p (sample from smallest set of tokens with cumulative probability p), max_tokens (hard response cap — set it to control cost), stop sequences. Reproducibility note: even temperature 0 isn't perfectly deterministic across runs/versions — build evals rather than relying on fixed outputs.

---

## Part 2 — Coding round walkthroughs

The bar: working code, narrated thinking, edge cases caught unprompted, tests offered at the end.

### ⭐ Q11. Build a rate limiter.
**Talk track:** clarify scope first — "Per-client or global? In-process or distributed? What should happen on limit — reject or queue?" Then: "I'll start with a token bucket per client, in-process, rejecting over-limit calls — and note how it extends to Redis for multi-instance."

```python
import time

class TokenBucket:
    def __init__(self, rate: float, capacity: int):
        self.rate = rate          # tokens added per second
        self.capacity = capacity  # burst size
        self.tokens = float(capacity)
        self.last = time.monotonic()   # monotonic: immune to clock changes

    def allow(self) -> bool:
        now = time.monotonic()
        self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.rate)
        self.last = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
```

**Edge cases to name unprompted:** thread safety (wrap in a lock), `time.monotonic()` vs `time.time()` (clock jumps), burst behavior at t=0 (full bucket is usually desired), distributed version (atomic Redis Lua script), and what the caller does on `False` (backoff with jitter). Offer tests: burst of `capacity` allowed, next call rejected, allowed again after `1/rate` seconds.

### Q12. Parse a messy CSV robustly.
**Talk track:** "Real customer files have encoding issues, malformed rows, and surprise delimiters — my design goals are: never crash, never silently drop data, always report what was skipped and why."
Key moves: use the `csv` module (never `line.split(',')` — quoted fields contain commas); `encoding="utf-8-sig"` with a `latin-1` fallback; validate each row (column count, type coercion) in a try/except; collect `(line_number, reason, raw_row)` for every reject; return `(good_rows, errors)` and **summarize the error patterns** — that summary is what you'd show the customer. Mention: for 10GB files, stream row-by-row rather than loading into memory.

### Q13. Consume a paginated API with retries.
**Talk track:** pagination loop + retry wrapper with exponential backoff and jitter. Name the behaviors that separate production code from demo code: honor `Retry-After` on 429; retry only retryable statuses (429, 5xx) — never 4xx client errors; cap total attempts; use a session for connection reuse; make it a generator so callers stream pages instead of buffering everything; log request IDs for supportability.

```python
import time, random, requests

def get_with_retries(url, params, max_attempts=5):
    for attempt in range(max_attempts):
        resp = requests.get(url, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 429 or resp.status_code >= 500:
            wait = float(resp.headers.get("Retry-After",
                         (2 ** attempt) + random.random()))
            time.sleep(wait)
            continue
        resp.raise_for_status()   # 4xx: don't retry, fail loudly
    raise RuntimeError(f"gave up after {max_attempts} attempts")
```

### Q14. Build a minimal RAG pipeline live.
**Talk track:** sketch the four stages, then code simply: chunk (fixed-size with overlap — say you'd prefer paragraph-boundary chunking with more time), embed (any embeddings API), store (list of vectors + numpy is fine at interview scale — "I'd reach for a vector DB at ~100k+ chunks, not before"), retrieve (cosine similarity top-k), generate (prompt with numbered chunks, instruct "answer only from context, cite chunk numbers"). Then *offer the eval*: "with 15 more minutes I'd add 10 Q&A pairs and measure retrieval recall@k separately from answer faithfulness" — that sentence is often the strongest hire signal in the round.

---

## Part 3 — System design: worked example

### ⭐ Q15. "Design a chatbot over a customer's 1M internal documents for 10k employees."

**1. Clarify (5 min):** What docs (wikis, PDFs, tickets)? Update rate? Permissions — can every employee see every doc (almost always **no** — this decision dominates the design)? Latency target? Cloud or on-prem constraints? Success metric (deflection? time-to-answer)?

**2. Walking skeleton first:** "V1: ingest one high-value doc source, hybrid search, LLM with citations, measure with 50 gold Q&As — in front of pilot users in 2 weeks. Then iterate." Saying this before the architecture is the FDE signal.

**3. Architecture:**
- **Ingestion**: connectors per source → parse (PDF/HTML → text) → chunk (semantic boundaries, ~500 tokens, overlap) → embed → vector index, **storing ACL metadata on every chunk**. Incremental sync on document change events; nightly full reconciliation.
- **Query path**: user auth → query rewrite (resolve "it/that" from chat history) → hybrid retrieval (BM25 + vector) **filtered by user's permissions at query time** → rerank top-50 → top-5 → prompt with citations required → stream response.
- **Trust boundaries**: retrieval filter enforces ACLs (never let the model see chunks the user can't); PII redaction in logs; prompt-injection awareness for doc content (docs are untrusted input to the prompt).
- **Failure modes**: embedding API down → keyword-only degraded mode; no relevant chunks → honest "not found" beats a guess; per-user rate limits.

**4. Evals & monitoring:** retrieval recall@k on a gold set; groundedness via LLM-judge; thumbs up/down feeding a review queue; dashboards for latency (p95), cost/query, deflection.

**5. Costs (rough numbers earn credibility):** 1M docs ≈ 4M chunks; embedding once ≈ low hundreds of dollars; queries dominated by LLM calls — at 10k employees × a few queries/day × ~3k tokens/query, estimate and name the levers (caching, small-model routing, prompt caching for shared context).

---

## Part 4 — Decomposition: worked example

### ⭐ Q16. "A hospital network wants to reduce ER wait times." (45 min, Palantir-style)

**Phase 1 — Clarify (never skip; ~8 min of questions):**
- "What's driving this now — a specific incident, a regulator, board pressure?" (finds the *real* goal)
- "How is wait time measured — door-to-triage, door-to-doctor, door-to-discharge?" (they differ; pick with the stakeholder)
- "Current baseline and target? Which hospitals — all, or the worst two?"
- "What data exists — EHR timestamps, staffing rosters, bed status? How accessible?"
- "Who owns this problem day-to-day — ER director? What have they already tried?"

**Phase 2 — Decompose the wait (draw this):** total ER time = arrival→triage + triage→bed + bed→doctor + doctor→decision + decision→exit (admit/discharge). Each segment has different causes and owners: triage staffing, bed availability (often blocked by *inpatient* discharge upstream!), physician coverage, lab/imaging turnaround, discharge logistics.

**Phase 3 — Prioritize with data:** "First deliverable: instrument the funnel — a dashboard of time-per-segment per hospital per shift, from EHR timestamps. Cheap, fast, and it tells us where the actual bottleneck is instead of guessing. In many hospitals the surprise finding is 'bed→doctor' blocked by inpatient discharge — meaning the fix isn't in the ER at all."

**Phase 4 — Minimal end-to-end slice:** pick the worst segment at the worst hospital; ship one intervention + measurement loop (e.g., if triage→bed dominates on weekend nights, model bed-turnover and trial a discharge-coordination change; measure against last month's baseline).

**Phase 5 — Risks & trade-offs, stated unprompted:** data quality (timestamps entered late during rushes — validate before trusting), Goodhart's law (optimizing door-to-doctor can create hallway medicine — pair with quality metrics), stakeholder reality (nurses' workflow buy-in beats an elegant model), and "if the data shows the bottleneck is upstream of the ER, the project scope must change — I'd rather renegotiate scope than optimize the wrong thing."

**Grading reality:** interviewers grade the *shape of your process* — clarify → decompose → instrument → prioritize → thin slice → risks. A confident wrong guess at the bottleneck scores worse than "here's how we'd find out in week one."

---

## Part 5 — Client simulation

### ⭐ Q17. "Your demo hallucinated in front of the customer's VP yesterday. The VP is angry on today's call. Go."
**Model answer:** "Thanks for flagging it directly — you're right that answer was wrong, and I understand why it damages confidence. Here's what we know: [one-sentence diagnosis — e.g., the retrieval layer returned an outdated policy doc]. Three things we're doing: fixing that specific failure, adding it to our test suite so it can't regress silently, and reviewing the eval results for this whole category. I want to be straight with you: no AI system will be at 100%, so the plan is a measured accuracy on your own test cases — currently X% — plus citations so every answer is checkable, and human review on the high-stakes paths. I'll send the fix summary and updated numbers by Friday. Can we also pick the 20 questions that matter most to your team, so we over-index the testing where it counts?"
*Structure: acknowledge without groveling → diagnose specifically → systemic fix, not just patch → honest expectation-setting → concrete commitment with a date → pull them into the solution.*

### Q18. "The customer demands a feature you think is a bad idea."
**Answer pattern:** Diagnose before arguing: "Help me understand the workflow where you'd use this" — the request is usually a symptom of a real need with a better solution. Then: restate their goal, show you take it seriously, present the trade-off concretely ("we can do X, but it costs us Y in reliability — here's an alternative reaching the same goal"), and if they still insist and it's not harmful, commit genuinely with agreed success criteria measured after launch. If it *is* harmful (security/compliance), that's a firm no with reasons and an escalation path. Never a bare "no," never a fake "yes."

### Q19. "You'll miss a deadline you committed to. Handle it."
**Answer pattern:** Tell them the moment *you* know — bad news early is a gift, late is a betrayal. Come with a plan, not just an apology: what's done, what's not, why (brief, no blame-shifting), and two options ("full scope by +2 weeks, or the core workflow on the original date and the reporting module two weeks after — I recommend the second; here's why"). Give the customer the decision. Then rebuild trust with visible frequent progress.

### Q20. "Walk me through how you'd run a discovery call with a new customer."
**Answer pattern:** Goal: leave knowing their business problem, success criteria, data reality, and political landscape — not having pitched features. Structure: (1) their world first — "walk me through how this process works today" and where it hurts; (2) quantify the pain (hours, dollars, errors); (3) define success in their numbers; (4) map data and systems (what exists, who owns it, access process); (5) identify the champion and the skeptic; (6) close with a concrete next step owned by a name and a date. Talk ratio ≈ 30/70.

---

## Part 6 — Behavioral (STAR skeletons to adapt)

Prepare 6–8 stories from *your* experience (projects, internships, coursework, clubs count). Below: the shape of a strong answer.

### ⭐ Q21. "Tell me about a time you owned something end-to-end."
**Skeleton:** S: "Team project X was failing because nobody owned integration." T: "I took responsibility for the end-to-end result, not just my module." A: "Mapped the gaps, fixed the two integration bugs *outside* my area, set up a shared test we ran before every merge, coordinated the final demo." R: "Shipped on time; the professor/client specifically called out reliability. Lesson: ownership means the outcome, including parts that 'aren't yours.'"
*FDE-specific: pick a story where you crossed a boundary (technical→people, your code→someone else's) — that's the role.*

### Q22. "Tell me about a time you were wrong."
**Skeleton:** name the belief, what evidence changed your mind, how fast you reversed, what process changed after. "I insisted on architecture A; two weeks of data showed the bottleneck was elsewhere; I said so in standup, we switched to B, and I started prototyping-before-committing for design bets." Interviewers are testing whether you can update — FDEs who can't admit errors to customers are dangerous.

### Q23. "Explain something technical to a non-technical person — how do you do it?"
**Answer pattern:** start from *their* goal, not the technology; use one concrete analogy anchored in their domain; state implications ("what this means for you is…"); check understanding by asking them to make a decision with the information — comprehension shows in decisions, not nods. Then give a 30-second live example (explain RAG to a claims manager: "it's like giving the AI an open-book exam with *your* manuals instead of asking it to answer from memory — so answers cite pages, and updating the manual updates the answers").

### Q24. "Why FDE and not regular software engineering?"
**Answer pattern (make it yours):** "I want the feedback loop of watching real users hit real problems — the moment where the demo meets the customer's messy data is where I learn fastest. I like owning outcomes, not tickets: the FDE deal is 'make it valuable, whatever that takes,' which is more code some days and more listening other days. And 2026 is a once-in-a-career window where deploying AI into real organizations is the industry's bottleneck — I'd rather be where the hard, unsolved part is." Back it with one story where you enjoyed exactly this (a hackathon demo for a real user, a tool you built for a club and iterated on feedback).

---

## How to drill this bank

- **Breadth Qs (1–10):** answer out loud, unscripted, as if teaching. If you stumble, reread the source in [resources.md](resources.md), retry the next day.
- **Coding (11–14):** actually code them, timed at 40 minutes, narrating aloud.
- **Design/decomposition (15–16):** whiteboard on [Excalidraw](https://excalidraw.com/), 45-minute hard stop, then compare against the worked example.
- **Simulation/behavioral (17–24):** rehearse with a friend playing hostile; record yourself once — you'll fix more from one playback than five silent readthroughs.
