# AI/ML Engineer Question & Answer Bank

Detailed questions **with answers** for every round. Rehearse out loud until you can explain each without reading. ⭐ = appears in almost every loop.

---

## Part 1 — Classic ML fundamentals (breadth round)

### ⭐ Q1. Explain the bias–variance tradeoff.
**Answer:** Bias is error from a model too simple to capture the real pattern (underfitting — bad on train *and* test). Variance is error from a model so flexible it fits noise (overfitting — great on train, bad on test). Total error ≈ bias² + variance + irreducible noise; making a model more expressive trades bias for variance. **Diagnose with learning curves:** high train error → high bias (add features, bigger model); large train/validation gap → high variance (more data, regularization, simpler model). Modern nuance worth adding: very large neural nets can defy the classic U-curve (double descent), but the diagnostic workflow is still how you debug in practice.

### ⭐ Q2. How do you detect and prevent overfitting?
**Answer:** Detect: validation performance much worse than training, or metrics that degrade on truly held-out data. Prevent — in rough order of preference: (1) more/better data (including augmentation); (2) regularization (L1/L2, dropout for nets); (3) early stopping on validation loss; (4) reduce model capacity; (5) cross-validation to make sure you're measuring honestly; (6) for trees/ensembles: limit depth, min samples per leaf. Key interview add: make sure it's actually overfitting and not **leakage** — a feature that encodes the label will show the same symptom on deployment.

### ⭐ Q3. L1 vs L2 regularization — difference, and why does L1 produce sparsity?
**Answer:** Both penalize large weights: L1 adds λ·Σ|w|, L2 adds λ·Σw². L2 shrinks all weights smoothly toward zero but rarely *to* zero; L1 drives some weights exactly to zero, doing built-in feature selection. Why: L1's penalty has a constant gradient (±λ) regardless of weight size, so it keeps pushing small weights all the way to zero — geometrically, the diamond-shaped L1 constraint has corners on the axes where solutions land. Use L1 when you suspect many irrelevant features or need interpretability; L2 as the default; elastic net for both.

### ⭐ Q4. Logistic regression vs decision trees vs gradient boosting — when and why?
**Answer:** - **Logistic regression**: the baseline. Fast, interpretable coefficients, well-calibrated probabilities, works with limited data. Linear boundary only — needs manual feature interactions. Regulated industries love it.
- **Decision tree** (single): captures nonlinearity and interactions automatically, handles mixed types, no scaling needed — but high variance; rarely deployed alone.
- **Gradient boosting** (XGBoost/LightGBM): the tabular-data workhorse — usually the accuracy winner on structured data, robust to feature scale and moderate messiness. Costs: more tuning, less interpretable (use SHAP), can overfit small noisy data.
**Interview-winning framing:** "I'd start with logistic regression as the baseline; if nonlinear patterns show in errors, move to gradient boosting; deep learning for tabular usually isn't worth it."

### ⭐ Q5. Precision vs recall — and pick one to optimize for cancer screening vs spam filtering.
**Answer:** Precision = of predicted positives, how many are truly positive (TP/(TP+FP)) — cost of false alarms. Recall = of actual positives, how many we caught (TP/(TP+FN)) — cost of misses. **Cancer screening: recall** — a missed cancer can be fatal, a false positive costs a follow-up test; but state the trade-off: too many false positives cause harm too (anxiety, unnecessary procedures), so you tune a threshold, not just max recall. **Spam: precision** — a real email in the spam folder (false positive) is worse than one spam getting through. F1 combines both; use it when costs are balanced. The general answer interviewers want: *the metric follows from the business cost of each error type* — always ask which error is more expensive.

### Q6. What's the problem with accuracy on imbalanced data, and what do you do instead?
**Answer:** With 1% fraud, "predict never-fraud" scores 99% accuracy while catching nothing. Use precision/recall, PR-AUC (better than ROC-AUC under heavy imbalance), and per-class metrics. Handling: (1) fix the metric first; (2) class weights / cost-sensitive loss (simplest and often enough); (3) resampling — oversample minority (SMOTE) or undersample majority — on the **training set only**, never validation/test; (4) threshold tuning on the PR curve to hit the business's operating point; (5) if positives are ultra-rare, consider anomaly-detection framing. Never evaluate on resampled data — report metrics on the true distribution.

### ⭐ Q7. What is data leakage? Give examples and how to prevent it.
**Answer:** Training-time access to information unavailable at prediction time — inflates offline metrics, collapses in production. Classic cases: (1) target leakage — a feature caused by the label ("number of chemo sessions" predicting cancer); (2) preprocessing leakage — fitting scalers/encoders/imputers on the full dataset before splitting (test-set statistics leak in); (3) temporal leakage — random splits on time-series so the model trains on the future; (4) group leakage — same patient/user in both train and test. Prevention: split **first**, fit transforms on train only (sklearn `Pipeline` inside CV does this right), time-based splits for temporal data, group-aware splits, and interrogate any feature that seems too good ("would I know this at prediction time?"). "My model is at 99%" usually means leakage, not genius.

### Q8. Explain cross-validation and when plain k-fold is wrong.
**Answer:** k-fold: split into k folds, train on k−1, validate on the held-out fold, rotate, average — a more reliable estimate than a single split, at k× cost. Wrong when data has structure a random split breaks: **time series** (use forward-chaining/rolling splits — train on past, validate on future only), **grouped data** (GroupKFold so the same user/patient never spans train and validation), **severe imbalance** (stratify folds). Also: do hyperparameter tuning inside the CV loop (nested CV) or your estimate is optimistically biased.

### Q9. How do you handle missing data?
**Answer:** First diagnose *why* it's missing — missing-at-random vs informative missingness (an empty "salary" field on a loan application is signal). Options: (1) drop rows/columns only if few and truly random; (2) simple imputation (median/mode) + a **"was_missing" indicator column** — the indicator often carries the signal; (3) model-based imputation (KNN/iterative) when relationships are strong; (4) tree libraries like XGBoost/LightGBM handle NaNs natively and learn the best direction for them. Fit imputers on train only (leakage). Never silently impute the target.

### Q10. Explain gradient descent and the role of the learning rate.
**Answer:** Iteratively update parameters opposite the loss gradient: w ← w − η·∇L. Variants: batch (all data per step — exact but slow), stochastic (one sample — noisy), mini-batch (the standard compromise). Learning rate η: too high diverges or bounces around the minimum; too low crawls and can stall. In practice: Adam optimizer as default, learning-rate schedules (warmup + decay), and "if training loss explodes, first suspect the learning rate." Bonus point: loss surfaces of neural nets are non-convex — we settle for good local minima, which empirically generalize fine.

### Q11. What is the curse of dimensionality?
**Answer:** As dimensions grow, data becomes exponentially sparse: distances concentrate (nearest and farthest neighbors become nearly equidistant), so distance-based methods (k-NN, k-means) degrade, and the data needed to cover the space explodes. Remedies: feature selection, dimensionality reduction (PCA, or learned embeddings), regularization, and models less sensitive to it (trees split one dimension at a time). Also the reason "just add more features" can *hurt*.

### Q12. Explain PCA in one minute.
**Answer:** Find orthogonal directions of maximum variance (eigenvectors of the covariance matrix), project data onto the top k — compressing correlated features into fewer uncorrelated components while keeping most variance. Uses: visualization, denoising, speeding up downstream models, decorrelating features. Caveats: linear only, scale features first (variance is unit-dependent), components lose interpretability, and max-variance ≠ max-predictive — PCA ignores the label.

---

## Part 2 — Deep learning

### ⭐ Q13. Explain backpropagation like you actually understand it.
**Answer:** "A neural net is a composition of differentiable functions. Forward pass computes the output and loss; backprop applies the chain rule *efficiently*: starting from the loss, walk the computation graph backwards, and each node multiplies the gradient flowing in by its local derivative to pass gradients to its inputs. One backward pass gets ∂loss/∂parameter for every parameter at roughly the cost of the forward pass — that efficiency is what makes training feasible at all. I've implemented it from scratch (micrograd-style): each operation stores its inputs and a `_backward` that routes gradients; you topologically sort the graph and run them in reverse." That last sentence — *and being able to back it up* — is why Karpathy lecture 1 is mandatory in the [roadmap](roadmap.md).

### Q14. Vanishing/exploding gradients — cause and fixes.
**Answer:** Backprop multiplies many local derivatives; in deep nets the product shrinks to ~0 (early layers stop learning) or blows up (unstable training). Fixes, and what each does: **ReLU-family activations** (derivative 1 in the active region, vs sigmoid's ≤0.25); **careful init** (He/Xavier keeps activation scale constant across layers); **BatchNorm/LayerNorm** (re-normalizes activations so gradients stay well-scaled); **residual connections** (gradient highways past layers — the key trick that made 100+ layer nets trainable); **gradient clipping** for explosions (standard in RNNs/transformer training).

### Q15. What do BatchNorm and Dropout do? Train vs inference difference?
**Answer:** **BatchNorm**: normalizes each channel to zero-mean/unit-variance over the mini-batch (then learnable scale/shift) — stabilizes and speeds training, allows higher learning rates. Train: batch statistics; inference: running averages collected during training — a classic source of train/serve bugs. **Dropout**: randomly zeroes activations with probability p during training so units can't co-adapt — an implicit ensemble; at inference dropout is off. Both are why `model.train()` vs `model.eval()` in PyTorch matters — forgetting `eval()` at serving time is a real production bug interviewers love asking about.

### Q16. Adam vs SGD — what does Adam actually do?
**Answer:** Adam keeps per-parameter running averages of gradients (first moment = momentum) and squared gradients (second moment), and scales each parameter's step by 1/√(second moment) — parameters with consistently large gradients get smaller steps, rare/small-gradient parameters get larger ones. Result: fast, robust convergence with little tuning — the practical default (AdamW, which fixes weight-decay handling, for transformers). SGD+momentum can generalize slightly better in some vision tasks but needs careful LR schedules. Honest answer: "AdamW with warmup+cosine decay is the boring correct choice; I'd only deviate with evidence."

### ⭐ Q17. Explain attention and why transformers replaced RNNs.
**Answer:** Attention lets every token directly gather information from every other token, weighted by learned relevance: each token emits a query, key, and value vector; attention weights = softmax(QKᵀ/√d); output = weighted sum of values. Multi-head = several attention patterns in parallel (syntax, coreference, position...). Why it won over RNNs: (1) no sequential bottleneck — RNNs squeeze history through a fixed hidden state and process token-by-token; attention is direct token-to-token and **fully parallel across the sequence**, so training scales to internet-size data; (2) constant path length between any two positions → long-range dependencies actually learnable. Cost: O(n²) in sequence length — the reason long-context is expensive and a whole research area exists around it. (Build one from scratch in Karpathy's GPT lecture and this question becomes easy.)

### Q18. What are embeddings, and how would you build semantic search?
**Answer:** Learned dense vectors where semantic similarity ≈ geometric closeness. Words, sentences, images, users — anything can be embedded. Semantic search: embed the corpus offline → store in a vector index (exact search until ~100k items; approximate-NN like HNSW beyond) → embed the query → top-k by cosine similarity. Production notes: hybrid with keyword search (BM25) for exact identifiers; a cross-encoder reranker over the top-50 lifts quality; chunking strategy matters more than the embedding model choice in most RAG systems.

---

## Part 3 — LLM / GenAI

### ⭐ Q19. Pretraining vs supervised fine-tuning vs RLHF — what does each stage give you?
**Answer:** (1) **Pretraining**: next-token prediction over massive text → raw capability: language, knowledge, reasoning patterns. Produces a document-completer, not an assistant. (2) **Supervised fine-tuning (SFT)**: train on curated (instruction → good response) pairs → teaches the *format* of being helpful. (3) **RLHF/preference tuning**: humans rank outputs; the model is optimized toward preferred responses (via a reward model + RL, or directly via DPO) → nudges tone, helpfulness, and refusal behavior — things easier to *rank* than to *write*. One-liner: "pretraining gives capability, SFT gives the assistant format, preference tuning gives judgment."

### ⭐ Q20. RAG vs fine-tuning — how do you choose?
**Answer:** RAG adds **knowledge** (private/fresh docs, citations, updateable without retraining — the default for enterprise Q&A). Fine-tuning adds **behavior** (format, style, domain reasoning; or distilling a big prompted model into a small cheap one). Fine-tuning is the wrong tool for injecting facts — coverage is unreliable, updates need retraining, no citations. They compose: RAG for the knowledge, a fine-tune for how to use it. Decision heuristic to say out loud: "does the model *not know* something (→ RAG) or *not behave* correctly (→ prompt first, then fine-tune)?"

### ⭐ Q21. How do you evaluate an LLM application when there's no single right answer?
**Answer:** (1) Decompose: for RAG, measure retrieval (recall@k against labeled relevant chunks) separately from generation (faithfulness to retrieved context) — different failure modes, different fixes. (2) Build a **gold set** of 50–200 real examples with reference answers or graded rubrics. (3) **LLM-as-judge** with an explicit rubric (correctness, groundedness, completeness), validated against ~30 human labels before trusting it; use pairwise comparisons (A vs B) — more reliable than absolute scores. (4) Cheap deterministic checks where possible: exact match for extraction, schema validation for structured output, unit tests for generated code. (5) Production: sampled human review + user feedback signals, failures flow back into the gold set. Key sentence: "prompts are code — evals are their test suite, run on every change."

### Q22. What causes hallucinations and how do you reduce them?
**Answer:** The model is trained to produce *plausible* continuations, not verified facts — when the answer isn't well-represented in training or context, it generates the most likely-sounding thing. Reductions, in order of leverage: ground with RAG + "answer only from context" instructions; require citations (auditable and reduces fabrication); check retrieval first — most RAG "hallucinations" are retrieval misses; lower temperature for factual tasks; eval-driven measurement of groundedness per release; guardrails/human review on high-stakes paths. Honest framing: you reduce and *measure* hallucination; you don't eliminate it.

### Q23. What are LoRA and quantization?
**Answer:** **LoRA**: instead of updating all weights during fine-tuning, freeze the model and learn small low-rank matrices (ΔW = A·B, rank r≪d) injected into attention/MLP layers — ~1% of trainable parameters, dramatically cheaper, adapters are swappable per task. **Quantization**: store weights at lower precision (8-bit/4-bit instead of 16) — 2–4× memory reduction with small quality loss, enabling big models on small GPUs. **QLoRA** combines both: fine-tune a 4-bit-quantized model with LoRA adapters — the standard budget fine-tuning recipe, and how you'd do the roadmap's fine-tuning exercises on a free Colab GPU.

### Q24. Explain tokenization and its practical consequences.
**Answer:** Models see subword tokens (BPE-style), not characters or words — common words = 1 token, rare words split into pieces; ~4 characters/token for English. Consequences worth naming: (1) cost and context limits are measured in tokens; (2) classic failure modes — counting letters in a word, arithmetic on long digit strings — trace to tokenization; (3) non-English text and code often tokenize less efficiently (more tokens → more cost); (4) same text, different tokenizer → different counts, so budget with the actual model's tokenizer.

---

## Part 4 — ML coding (from-scratch answers)

Interviewers want: correct core logic, vectorized NumPy, narrated choices, and edge cases named.

### ⭐ Q25. Linear regression with gradient descent (NumPy only).
```python
import numpy as np

def fit_linear_regression(X, y, lr=0.01, epochs=1000):
    X = np.c_[np.ones(len(X)), X]        # bias column
    w = np.zeros(X.shape[1])
    n = len(y)
    for _ in range(epochs):
        grad = (2 / n) * X.T @ (X @ w - y)   # d/dw of MSE
        w -= lr * grad
    return w                              # w[0] = intercept
```
**Narrate:** "MSE loss; its gradient is 2/n·Xᵀ(Xw−y); I fold the bias in as a ones-column. I'd standardize features first — gradient descent on unscaled features converges badly. Sanity checks: loss decreases monotonically for small lr; for the closed form, `np.linalg.lstsq` — I'd mention why we use GD anyway (scales to huge n, generalizes to models with no closed form)."

### ⭐ Q26. k-means from scratch.
```python
def kmeans(X, k, iters=100, seed=0):
    rng = np.random.default_rng(seed)
    centers = X[rng.choice(len(X), k, replace=False)]
    for _ in range(iters):
        d = np.linalg.norm(X[:, None] - centers[None, :], axis=2)  # (n, k)
        labels = d.argmin(axis=1)
        new = np.array([X[labels == j].mean(axis=0) if (labels == j).any()
                        else centers[j] for j in range(k)])
        if np.allclose(new, centers):
            break
        centers = new
    return labels, centers
```
**Edge cases to name:** empty clusters (keep old center or re-seed), sensitivity to init (k-means++ or multiple restarts, keep best inertia), must scale features, k chosen via elbow/silhouette, only finds convex blobs.

### Q27. Precision, recall, F1 without sklearn.
```python
def prf1(y_true, y_pred):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall    = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return precision, recall, f1
```
**Narrate:** division-by-zero guards ("no positive predictions → precision undefined; I return 0 and would log a warning"), and offer the extension: "given probabilities instead of labels, I'd sweep thresholds to trace the PR curve and pick the operating point from business costs."

### Q28. Train/validation split with stratification, from scratch.
**Answer sketch:** group indices by class, shuffle within each class with a seeded RNG, take the same fraction from each class for validation, concatenate. Narrate *why*: with imbalanced classes, a random split can starve validation of the minority class, making metrics meaningless; the seed makes experiments reproducible. Mention `GroupKFold`-style logic if the same user generates multiple rows (group leakage, Q7).

---

## Part 5 — ML system design: worked example

### ⭐ Q29. "Design a spam detector for an email product." (45 min)

**1. Clarify (5 min):** Scale (emails/day)? Latency budget (inline before inbox delivery — say ~100ms)? Cost of each error — false positive (real mail in spam) is far worse than a miss. Existing labels ("report spam" / "not spam" buttons = free labeling stream)? Personalized or global?

**2. Metrics before models:** business metric: user-visible spam rate *and* false-positive rate on legit mail (asymmetric — set FP budget first, e.g., <0.1%). Model metric: precision at a recall floor, PR-AUC. Say explicitly: "threshold tuned to the FP budget, not 0.5."

**3. Baseline first:** rules + a linear model over simple features (sender reputation, auth results SPF/DKIM, keyword/URL stats) — cheap, explainable, and the benchmark any fancy model must beat. This sentence is a hire signal.

**4. Data & features:** labels from user reports (noisy — users misreport; aggregate/weight), text features (subject/body n-grams → embeddings later), sender/infra features (domain age, IP reputation, volume patterns), user-interaction features. Name the leakage trap: features must be computable *at delivery time*.

**5. Model evolution:** logistic regression → gradient boosting on tabular+text features → small transformer on text only if the gap justifies latency/cost. Ensemble text score with infra features.

**6. Serving:** inline scoring service at ~100ms budget: cache sender-level features, precompute reputations, keep the model small; fallback = rules-only path if the model service degrades. Never fail-open silently — log and alert.

**7. The adversarial + feedback loop (what separates senior answers):** spammers adapt → static models decay. Continuous retraining on fresh labels, monitor drift (score distributions, FP-report rate), canary new models on a traffic slice, keep a human-review queue for borderline scores. Also: attackers probe — rate-limit feedback signals so they can't reverse-engineer thresholds.

**8. Close with iteration plan:** "Ship baseline behind the FP budget → instrument → the first month's data tells us whether text or infra features carry more signal → invest there."

---

## Part 6 — Production / MLOps

### ⭐ Q30. Your model performs great offline but poorly in production. Debug it.
**Answer:** Work the funnel in order: (1) **training/serving skew** — is the *same* feature computation running in both places? (most common cause; a pandas transform offline vs a different SQL transform online); (2) **leakage in offline eval** — was the offline number ever real? check split hygiene, temporal splits; (3) **distribution shift** — compare production input distributions to training (new user segment, seasonality, upstream schema change silently nulling a feature); (4) **feedback delay/label mismatch** — are we measuring the same target we trained on? (5) **degenerate slices** — aggregate metrics can hide one segment failing; slice by user type, geography, time. Tooling answer: log features at serving time and replay them offline — if offline model on logged features ≠ production behavior, it's infrastructure; if =, it's data/distribution.

### Q31. What is drift and how do you monitor it?
**Answer:** **Data drift**: input distribution changes (new demographics, upstream changes). **Concept drift**: the input→label relationship changes (fraud tactics evolve). **Label/prior drift**: class balance shifts. Monitoring: statistical distance between live and training feature distributions (PSI/KS per feature), prediction-distribution monitoring (a score histogram that suddenly shifts is an alarm even without labels), delayed-label metric tracking where ground truth eventually arrives, and canary sets. Response: alert thresholds → investigate root cause → retrain on fresh data (scheduled or trigger-based). Key line: "monitor predictions *and* inputs — labels usually arrive too late to be your only signal."

### Q32. Batch vs online serving — how do you choose?
**Answer:** **Batch** (precompute nightly, serve from a table): when predictions are needed on a schedule or for known entities (churn scores, recommendations refreshed daily). Cheap, simple, tolerant of slow models. **Online** (model behind an API): when the input only exists at request time (fraud scoring a live transaction, search ranking). Costs: latency engineering, feature freshness (feature store to avoid skew), autoscaling, fallbacks. Hybrid is common: heavy user embeddings batch-precomputed + light online model combining them with request-time features. Choose by: "when is the input known, and how fresh must the answer be?"

### Q33. How would you A/B test a new model?
**Answer:** Randomize at the right unit (usually user, not request — request-level randomization contaminates user experience and violates independence), define the primary business metric and guardrail metrics up front, run a power calculation for duration (don't peek-and-stop), watch for novelty effects, and check *segment-level* results before shipping (a win on average can lose on a key segment). For risky models: shadow mode first (score silently, compare offline) → canary (1–5% traffic) → ramp. Mention interference honestly if it's a marketplace/social product (treatment users affect control users).

### Q34. Walk through your retraining strategy.
**Answer:** Decide trigger: scheduled (weekly/monthly — simple, predictable) vs performance-triggered (drift/metric alarms — responsive, needs solid monitoring). Pipeline must be fully automated and reproducible: data validation (schema + distribution checks — bad data in, bad model out), training with versioned data/code/params, offline eval against the incumbent on a fixed benchmark *plus* recent data, auto-promote only if it wins with margin, deploy via canary, keep instant rollback. Log everything (model registry). One-liner: "retraining isn't an event, it's a tested pipeline — if retraining scares you, your pipeline isn't done."

### Q35. A stakeholder demands to know why the model rejected a customer. What do you do?
**Answer:** Two levels: (1) **instance-level explanation** — SHAP values show which features pushed this specific prediction and in which direction ("high utilization + short credit history dominated"); LIME is the local-approximation alternative. (2) **process answer** — in regulated domains (credit: adverse-action notices) explainability is a legal requirement, so model choice must anticipate it: either interpretable-by-design (scorecards, monotonic GBMs) or a validated explanation pipeline. Also flag: check the *feature*, not just the math — if the explanation surfaces a proxy for a protected attribute, that's a bias problem to escalate, not explain away.

---

## Part 7 — Behavioral (quick reference)

Same STAR structure as the [FDE bank](../fde/qa-bank.md) Part 6 (ownership, being wrong, deadline, explaining to non-technical people). Two MLE-specific ones:

### Q36. "Tell me about a model/project that failed."
**Skeleton:** pick a real one (Kaggle overfit, a feature that leaked, a project where the baseline won). Structure: what you expected → what happened → how you *diagnosed* it (the part they're hiring) → what changed in your process ("I now always run a leakage audit / always ship the baseline first"). Never pick a fake failure ("I worked too hard").

### Q37. "How do you decide a problem doesn't need ML?"
**Answer pattern:** "If rules solve it to the required quality, rules win — they're debuggable, predictable, and free. ML earns its complexity when the pattern is too nuanced to enumerate, the payoff justifies the infrastructure, and there's data + a feedback loop to keep it healthy. In interviews and at work I say the same thing: baseline first, and let the gap justify the model." Cite Google's Rules of ML #1: don't be afraid to launch without ML.

---

## How to drill this bank

- **Parts 1–3 (breadth):** 5 questions/day out loud, as if teaching. Stumble → reread source in [resources.md](resources.md) → retry tomorrow.
- **Part 4 (coding):** type them from a blank file, timed 30 min each; then daily [Deep-ML](https://www.deep-ml.com/) problems keep it sharp.
- **Part 5 (design):** whiteboard the spam case yourself *before* reading the answer, then diff; repeat weekly with new prompts from [Evidently's case database](https://www.evidentlyai.com/ml-system-design).
- **Parts 6–7:** rehearse with a friend interrupting with "why?" — production questions are conversations, not recitals.
