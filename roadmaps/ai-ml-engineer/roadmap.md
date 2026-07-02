# AI/ML Engineer Roadmap — 6 Weeks Intensive (~3–4 hrs/day)

Every task links to a free resource (details and alternatives in [resources.md](resources.md)).
Sequence: Python/math → classic ML → deep learning → LLMs → production/MLOps → interview drills.
Milestones become your portfolio — do not skip them.

---

## Week 1 — Python for data, math intuition

**Goal:** fluent NumPy/pandas and enough linear algebra/stats intuition to explain any model you use.

- [ ] Day 1–2: Python check — if you're shaky, do [CS50P](https://cs50.harvard.edu/python/) lectures 0–5 fast; if solid, go straight on.
- [ ] Day 2–4: [Kaggle Learn](https://www.kaggle.com/learn) — Pandas + Data Visualization micro-courses (hands-on, in-browser, free certificates).
- [ ] Day 3–5: [3Blue1Brown — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) — chapters 1–10. Watch actively: pause and predict. *(~4 hrs)*
- [ ] Day 5–7: [StatQuest — Statistics Fundamentals](https://www.youtube.com/@statquest) — distributions, p-values, likelihood; then his ML playlist basics (bias/variance is interview gold). *(~4 hrs)*
- [ ] Daily: 30 min SQL on [SQLBolt](https://sqlbolt.com/) → [SQL Practice](https://www.sql-practice.com/) (MLE interviews include SQL more often than you'd think).

**Milestone project:** pick a [Kaggle dataset](https://www.kaggle.com/datasets) and publish an exploratory-data-analysis notebook: cleaning, 5 meaningful visualizations, 5 written insights. This is portfolio piece #1. *(~4 hrs)*

---

## Week 2 — Classic ML

**Goal:** the supervised-learning core that every ML breadth round tests.

- [ ] Day 1–5: [Andrew Ng — Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) (audit each course free) — Course 1 fully + Course 2 through decision trees. Do the labs. *(~3 hrs/day)*
- [ ] Day 1–5 (parallel, 30 min/day): [StatQuest ML playlist](https://www.youtube.com/@statquest) — watch the video for each concept the same day Ng covers it (two angles beat one).
- [ ] Day 5–6: [Kaggle Learn — Intro to Machine Learning + Intermediate ML](https://www.kaggle.com/learn) — scikit-learn workflow: pipelines, cross-validation, handling missing data/leakage.
- [ ] Day 7: Implement **from scratch in NumPy**: linear regression (gradient descent) and k-means. Then start the habit — 1 problem/day on [Deep-ML](https://www.deep-ml.com/) (LeetCode-style ML-from-scratch problems, free).

**Milestone project:** enter a Kaggle Getting Started competition (e.g., [Spaceship Titanic](https://www.kaggle.com/competitions/spaceship-titanic)) — proper train/validation split, feature engineering, 3 model comparison, submission. Write up what moved the score. Portfolio piece #2. *(~5 hrs)*

---

## Week 3 — Deep learning

**Goal:** understand neural nets from scratch, be productive in PyTorch.

- [ ] Day 1–3: [Karpathy — Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) — lectures 1–2 (micrograd: backprop from scratch; makemore part 1). **Type every line yourself.** This is the single best interview prep for "explain backpropagation." *(~4 hrs/day, dense)*
- [ ] Day 4–5: [PyTorch — Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html) — tensors → datasets → build/train/save models.
- [ ] Day 5–6: Karpathy lecture 3–4 (MLPs, BatchNorm internals — where deep-dive interview questions come from).
- [ ] Day 7: [fast.ai — Practical Deep Learning](https://course.fast.ai/) lesson 1 for the top-down view, and train your first real model with it.

**Milestone project:** train a text or image classifier in PyTorch on a real dataset (e.g., sentiment on IMDB, or a fast.ai vision task) — training curves, a confusion matrix, and a 200-word error analysis (which examples fail and why). Portfolio piece #3. *(~5 hrs)*

---

## Week 4 — Transformers, LLMs, RAG, evals

**Goal:** the GenAI stack that dominates 2026 entry-level hiring.

- [ ] Day 1–2: Karpathy — ["Let's build GPT"](https://karpathy.ai/zero-to-hero.html) (build a transformer from scratch; after this, attention questions are easy).
- [ ] Day 3: [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) — chapters 1–3 (tokenizers, using pretrained models, fine-tuning basics with the Trainer API).
- [ ] Day 4: LLM APIs + prompting: [Anthropic courses repo](https://github.com/anthropics/courses) API + prompt-engineering notebooks (free tier key suffices).
- [ ] Day 5: Build a minimal **RAG pipeline from scratch** (no framework): chunk → embed → store → retrieve top-k → answer with citations.
- [ ] Day 6: **Evals** — read [Hamel Husain — Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) and build an eval harness for your RAG app (15 Q/A pairs, exact-match + LLM-as-judge scoring, results table). Interviewers at every level now ask "how do you know it works?"
- [ ] Day 7: One [DeepLearning.AI short course](https://www.deeplearning.ai/short-courses/) on fine-tuning **or** agents — pick your bigger gap.

**Milestone project:** "docs Q&A with proof it works" — RAG over a public doc set + the eval harness + a README table of eval results before/after one improvement (better chunking, reranking, or prompt change). Portfolio piece #4 — this one gets discussed in interviews. *(~5 hrs)*

---

## Week 5 — Production ML: serving, MLOps, ML system design

**Goal:** the production sense that separates hired from rejected in 2026.

- [ ] Day 1–2: [Made With ML](https://madewithml.com/) — design, data, modeling, and deployment lessons (skim what you know; the testing/monitoring lessons are the differentiator).
- [ ] Day 2–3: Serve your Week 3 or 4 model as a [FastAPI](https://fastapi.tiangolo.com/tutorial/) endpoint; containerize it with [Docker — Get Started](https://docs.docker.com/get-started/).
- [ ] Day 4–5: [Chip Huyen — Machine Learning Systems Design](https://huyenchip.com/machine-learning-systems-design/toc.html) (free booklet) — read fully; learn the framework in [interview-prep.md](interview-prep.md).
- [ ] Day 5–6: Study 5 real case studies from the [Evidently AI ML system design database](https://www.evidentlyai.com/ml-system-design) — pick ones near your interests (recsys, fraud, LLM apps).
- [ ] Day 7: Timed practice — write full ML system designs (45 min each, on [Excalidraw](https://excalidraw.com/)) for two prompts: "design a spam detector for a mail product" and "design a support-ticket answering system with an LLM."

**Milestone:** your served model (Docker + FastAPI, README with `docker run` instructions) + one polished system-design doc. Portfolio piece #5.

---

## Week 6 — Interview drills

**Goal:** performance. The day-by-day schedule and question bank live in [interview-prep.md](interview-prep.md).

- [ ] Daily: 1 [Deep-ML](https://www.deep-ml.com/) from-scratch problem + 1–2 [NeetCode](https://neetcode.io/roadmap) problems (arrays/hashing, two pointers — enough for most MLE coding screens).
- [ ] 3× ML breadth self-quizzes out loud (question bank in interview-prep.md — answer as if teaching).
- [ ] 2× timed ML system design cases (45 min, new prompts).
- [ ] 2× mock interviews on [Pramp](https://www.pramp.com/) (one coding, one you convert to ML discussion with your peer).
- [ ] 1× project deep-dive rehearsal: 10-minute walkthrough of portfolio piece #4, then have a friend grill you ("why this chunk size?", "what if latency doubles?").
- [ ] Prepare 6 STAR behavioral stories (template in interview-prep.md).
- [ ] Polish GitHub + a one-page portfolio README linking all 5 pieces; apply broadly (startups, enterprises, big-tech new-grad MLE).

**Final milestone:** full self-run loop in one day — ML coding (60') → ML breadth (45') → ML system design (60') → project deep-dive (30') → behavioral (30'). Score with the rubric in interview-prep.md.
