# Computer Vision Engineer Interview Prep

CV loops mirror [ML Engineer loops](../ai-ml-engineer/interview-prep.md) — same structure, everything vision-flavored. Use the AI/ML pack for general ML rounds; this file covers what's different.

---

## The typical loop

1. **Recruiter screen** (30 min)
2. **Technical phone screen** (60 min) — CV concepts + a small implement-from-scratch exercise (IoU/NMS territory)
3. **Onsite** (3–4 rounds):
   - **Coding** — general DSA (lighter than SDE loops) *and/or* CV implementations
   - **CV depth** — CNNs, detection, segmentation, modern vision; follow-the-thread on your projects
   - **System design** — a camera-to-decision pipeline (defect detection, video analytics)
   - **Project deep-dive** — your custom detector gets grilled
4. **Behavioral** (30–45 min)

Segment differences: **autonomy/robotics** adds C++ questions and 3D/geometry (calibration, epipolar basics); **medical** leans segmentation + metrics under class imbalance; **manufacturing/analytics startups** lean practical (OpenCV, deployment, edge latency); **big tech** adds a standard DSA round at LeetCode-medium level.

---

## Question bank by round

### CV coding (implement from scratch — practice until automatic)
- Compute IoU between two boxes (then: vectorize over N×M boxes)
- Non-maximum suppression given boxes + scores
- 2D convolution with padding/stride (NumPy, no libraries)
- Bilinear interpolation / image resize
- Connected components or flood fill on a binary mask
- Compute mAP given predictions and ground truth (walk the logic)
- Full worked answers with code: [qa-bank.md](qa-bank.md) Part 3.

### CV depth (know cold)
- Why convolution for images? (parameter sharing, translation equivariance, locality)
- Receptive field: what it is, how to grow it (stride, dilation, depth) and why it matters for small/large objects
- Pooling vs strided conv; what's lost, what's gained
- BatchNorm at train vs inference (classic deployment-bug question)
- Transfer learning: what to freeze, when, and why; when training from scratch is justified
- Data augmentation: which transforms are safe for which tasks (horizontal flip: fine for cats, catastrophic for reading text or chirality-sensitive medical images)
- One-stage vs two-stage detectors; anchor-based vs anchor-free
- IoU / precision-recall / mAP@0.5 vs mAP@[.5:.95] — and when mAP misleads (class imbalance, small objects)
- Why NMS is needed and its failure modes (crowded scenes); soft-NMS idea
- Semantic vs instance vs panoptic segmentation; why Dice/IoU loss over pixel accuracy
- Class imbalance in detection: focal loss intuition
- ViT vs CNN: inductive biases, data requirements, when each wins
- CLIP: how contrastive pretraining gives zero-shot classification; practical uses (search, labeling bootstrap)
- SAM: what "promptable segmentation" means; where it fits in a labeling pipeline
- Domain shift: why the lab model dies on the factory camera, and what you do about it
- Edge deployment: quantization (what breaks), ONNX, latency/accuracy trade-offs, measuring FPS honestly

### System design (the differentiator round)
Prompts: *"Design defect detection for a bottling line (30 bottles/sec)"* · *"Retail shelf-monitoring across 500 stores"* · *"Pedestrian detection for a delivery robot"* · *"Tumor segmentation pipeline for radiology"*

**Framework (adapted from the [ML design framework](../ai-ml-engineer/interview-prep.md)):**
1. **Clarify**: error costs (miss vs false alarm), throughput/latency budget, edge vs cloud, camera control (can you fix lighting/mounting? huge lever), labels available?
2. **Data & labeling plan**: collection at the actual site, labeling workflow (SAM/CLIP to bootstrap), class balance, the eval set must match deployment conditions.
3. **Baseline first**: classical CV or an off-the-shelf pretrained detector before custom training — say it explicitly.
4. **Model & training**: detector choice with trade-offs (small object? speed?), augmentation matched to real variation.
5. **Serving**: edge vs server math (bandwidth of streaming video vs on-device inference), quantized model, tracker to smooth per-frame noise, fallback path.
6. **Monitoring & drift**: confidence-distribution monitoring, periodic sampled human review, retraining loop when cameras/sites/products change.
7. **Iterate**: ship on one line/store, measure, expand.

**Instant-fail behaviors:** jumping to "train a YOLO" before asking about error costs and camera control; no labeling plan; ignoring lighting/domain shift; quoting FPS without hardware context.

### Behavioral
Same 6 STAR stories as [AI/ML prep](../ai-ml-engineer/interview-prep.md); add one CV-specific: a time a model failed *in the field* (or your project's failure-gallery analysis) and how you diagnosed it — data problem vs model problem.

---

## Week-6 drill schedule

| Day | Drill (~3–4 hrs) |
|---|---|
| 1 | IoU + NMS from scratch, timed 40' + 8 depth questions out loud |
| 2 | Timed system design #1 (parking occupancy) + convolution from scratch |
| 3 | [Pramp](https://www.pramp.com/) general-coding mock + 8 more depth questions |
| 4 | Project deep-dive rehearsal (detector CV-3), friend grilling + OpenCV PR work |
| 5 | Timed system design #2 (medical segmentation) + mAP walk-through out loud |
| 6 | **Full self-run loop** (coding 60' → depth 45' → design 60' → project 30' → behavioral 30') |
| 7 | Patch weakest round; polish portfolio; applications |

## Self-scoring rubric (per round, 1–4)

- **1** — Couldn't produce working IoU/NMS or froze on "why convolution"
- **2** — Correct but shallow: no trade-offs, no eval story, quoted metrics without context
- **3** — Structured: clarified constraints, justified choices, connected metrics to deployment reality
- **4** — Hire signal: raised domain shift, labeling strategy, and monitoring unprompted; adjusted under challenge

---

## Free question sources worth drilling from

- [Devinterview-io CV questions (GitHub)](https://github.com/Devinterview-io/computer-vision-interview-questions) — large free bank for breadth sweeps
- [andrewekhalel/MLQuestions (GitHub)](https://github.com/andrewekhalel/MLQuestions) — classic ML/CV technical questions collection
- [Interview Query CV questions](https://www.interviewquery.com/p/computer-vision-interview-questions) — free article tier with worked discussion
