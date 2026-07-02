# AI/ML Engineer Interview Prep

Round types, question banks, the ML system design framework, and the week-6 drill schedule.

---

## The typical entry-level loop

1. **Recruiter screen** (30 min)
2. **Technical phone screen** (60 min) — ML concepts + light coding
3. **Onsite loop** (3–4 rounds over 1–3 days):
   - ML coding (implement from scratch / data manipulation)
   - ML breadth & depth (fundamentals Q&A + follow-the-thread deep dives)
   - ML system design (45–60 min — the highest-weight round in 2026)
   - Project deep-dive (your portfolio, grilled)
4. **Behavioral** (30–45 min)

Some big-tech loops add a general DSA round (LeetCode medium level). Startups often replace it with a practical take-home (frequently RAG/eval flavored — your week 4 milestone is direct practice).

**The 2026 shift:** interviewers care less about definitions, more about system design over models you don't control, retrieval and evaluation judgment, production debugging, and cost/latency trade-offs. Responsible-AI questions (bias audits, SHAP/LIME explainability) now appear as technical questions, not values chat.

---

## Question bank by round

### ML coding
- Implement linear regression with gradient descent (NumPy only). Follow-up: add L2 regularization.
- Implement k-means / k-NN / logistic regression from scratch.
- Given a messy DataFrame: clean it, engineer features, avoid leakage — narrate your choices.
- Implement train/validation split with stratification; explain why stratify.
- Compute precision/recall/F1 from raw predictions without sklearn.
- Practice source: [Deep-ML](https://www.deep-ml.com/) mirrors this round almost exactly.

### ML breadth (know these cold — answer out loud as if teaching)
- Bias vs variance; how you detect and fix each.
- Overfitting: five ways to reduce it, and when each applies.
- L1 vs L2 regularization; why L1 produces sparsity.
- Logistic regression vs decision tree vs gradient boosting — when and why.
- How does backpropagation work? (You built it in week 3 — say so.)
- BatchNorm / dropout — what problem does each solve?
- Precision vs recall: pick one to optimize for cancer screening vs spam. Why?
- Class imbalance: what you actually do (and why accuracy is the wrong metric).
- Cross-validation variants; when time-series CV is mandatory.
- How do transformers work? Attention in one whiteboard drawing.
- Fine-tuning vs RAG vs prompt engineering — cost/freshness/control trade-offs.
- What are embeddings? How would you build semantic search?
- How do you evaluate an LLM application when there's no single right answer?
- What is drift? How do you detect a model quietly degrading in production?
- Explain SHAP/LIME at a high level; when would a stakeholder demand them?

### ML depth (they pull one thread from your resume/projects)
Whatever you list, expect five "why"s deep: why this chunk size, why this metric, why not a simpler baseline, what failed first, what would you do with 10× data. Rehearse your portfolio pieces to that depth — especially the RAG + evals project.

### ML system design (train hardest here)
Prompts: *"Design a spam filter"*, *"Design a feed-ranking system"*, *"Design fraud detection for payments"*, *"Design a support-bot over company docs"*, *"Design an eval pipeline for an LLM feature."*

**Framework** (from [Chip Huyen's booklet](https://huyenchip.com/machine-learning-systems-design/toc.html)):
1. **Clarify & frame** (5–10 min): users, scale, latency budget, cost constraints; is ML even needed? What's the *business* metric vs the *model* metric?
2. **Data**: sources, labels (who labels? how much? how fresh?), feature pipeline, leakage risks.
3. **Baseline first**: rules/heuristics or logistic regression before deep anything — say this explicitly, it's a hire signal.
4. **Model & training**: candidate models with trade-offs; how you'd validate offline.
5. **Serving**: batch vs online, latency/cost estimates, caching, fallbacks when the model or API fails.
6. **Evaluation & monitoring**: offline metrics → online A/B → drift detection → feedback loops. For LLM systems: eval sets, LLM-as-judge, guardrails.
7. **Iterate**: what you'd measure to decide the next improvement.

**Instant-fail behaviors:** jumping to "I'd fine-tune an LLM" before framing; no baseline; no evaluation story; ignoring cost/latency.

### Behavioral (6 STAR stories)
Themes: a project you owned end-to-end · a technical decision you got wrong · handling ambiguous requirements · a deadline crunch · explaining ML to a non-technical person · a conflict or pushback you navigated. Format: Situation (2 sentences) → Task → Action (bulk, "I" not "we") → Result (numbers if possible).

---

## Week-6 drill schedule

| Day | Drill (~3–4 hrs) |
|---|---|
| 1 | 2 Deep-ML problems + ML breadth self-quiz (first 8 questions, out loud) + 2 NeetCode |
| 2 | Timed ML system design #1 (spam filter, 45') + rehearse 3 STAR stories |
| 3 | [Pramp](https://www.pramp.com/) mock #1 + review; ML breadth quiz (last 7 questions) |
| 4 | Project deep-dive rehearsal with a friend grilling you + 2 Deep-ML problems |
| 5 | Timed ML system design #2 (LLM support bot, 45') + Pramp mock #2 |
| 6 | **Full self-run loop:** ML coding 60' → breadth 45' → system design 60' → project 30' → behavioral 30' |
| 7 | Patch the weakest round; polish portfolio README; send applications |

## Self-scoring rubric (per round, 1–4)

- **1** — Stalled without hints; answered definitions but couldn't apply them
- **2** — Correct but shallow: no trade-offs, no baseline, no eval story
- **3** — Structured, justified choices, connected model metrics to business outcomes
- **4** — Hire signal: proactively raised failure modes, monitoring, cost — and adjusted when challenged

Anything ≤2 gets a targeted retry the next day.

---

## Free deep-dive reading

- [Chip Huyen — Introduction to ML Interviews Book](https://huyenchip.com/ml-interviews-book/) — free online; the interview-landscape chapters are excellent for calibration.
- [Chip Huyen — ML Systems Design booklet](https://huyenchip.com/machine-learning-systems-design/toc.html) — free; read fully in week 5.
- [Evidently AI — ML system design case database](https://www.evidentlyai.com/ml-system-design) — 300+ real company case studies.
- [Google — Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml) — production ML wisdom; quotable in design rounds.
