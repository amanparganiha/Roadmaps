# Computer Vision Engineer Roadmap — 6 Weeks Intensive (~3–4 hrs/day)

**Prerequisite:** [AI/ML Engineer roadmap](../ai-ml-engineer/roadmap.md) weeks 1–3 (Python/NumPy, classic ML, PyTorch + backprop) or the equivalent Krish Naik course sections. Every task links to a free resource (details in [resources.md](resources.md)).

---

## Week 1 — Image fundamentals + OpenCV (with free official cert)

**Goal:** think in pixels; be fluent in OpenCV.

- [ ] Day 1–3: [OpenCV Bootcamp](https://opencv.org/university/free-opencv-course/) — the free official course: image/video manipulation, filtering, edge detection, object detection & tracking, face detection, DNN module. Finish it and **collect the free certificate**. *(~3 hrs of video + do every notebook)*
- [ ] Day 3–5: Go deeper on fundamentals with the [OpenCV Python tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html): color spaces, thresholding, morphology, contours, histograms, geometric transforms, feature matching (ORB/SIFT).
- [ ] Day 5–6: Classical CV mini-drills (no deep learning allowed): count coins in an image; deskew a scanned document; isolate one color object from video.
- [ ] Day 7: Read how convolution/filters actually work — [CS231n notes on convolution](https://cs231n.github.io/convolutional-networks/) (first half; the CNN part continues next week).

**Milestone project:** a **document scanner** (detect page edges → perspective transform → adaptive threshold → readable output) or **lane detector** on dashcam footage — classical CV only, OpenCV, with a README showing before/after frames. Portfolio piece CV-1. *(~5 hrs)*

---

## Week 2 — CNNs + training craft

**Goal:** understand and train CNNs properly; this is the depth interviews probe.

- [ ] Day 1–3: [CS231n](https://cs231n.github.io/) — CNN notes + lectures (convolution arithmetic, receptive fields, pooling, architectures: ResNet ideas). Watch the [lecture videos](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU) selectively; the written notes are the gold.
- [ ] Day 3–4: [OpenCV's free PyTorch Bootcamp](https://opencv.org/university/free-pytorch-course/) — second free official cert; consolidates PyTorch training loops on vision tasks.
- [ ] Day 4–6: Training craft, hands-on in PyTorch: transfer learning from a pretrained ResNet ([PyTorch tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)), data augmentation, LR schedules, early stopping. Log experiments properly.
- [ ] Day 7: Interpretability: apply Grad-CAM to your model; write 5 sentences on what it attends to and one failure it explains.

**Milestone project:** fine-tune a classifier on a *real* dataset (defects, plant disease, X-ray — pick from [Kaggle](https://www.kaggle.com/datasets)) — augmentation ablation (with/without), confusion matrix, Grad-CAM panel, 300-word error analysis. Portfolio piece CV-2. *(~5 hrs)*

---

## Week 3 — Object detection & segmentation

**Goal:** own the IoU/mAP/NMS layer and train custom detectors — the most-asked CV interview topics.

- [ ] Day 1–2: Theory first, from scratch: implement **IoU**, **NMS**, and read how **mAP** is computed (worked answers in [qa-bank.md](qa-bank.md)). Understand anchor-based vs anchor-free, one-stage vs two-stage.
- [ ] Day 2–4: Train a custom [YOLO detector (Ultralytics docs)](https://docs.ultralytics.com/) on your own dataset — label ~200 images with [Roboflow's free tier](https://roboflow.com/) or [Label Studio](https://labelstud.io/) (open source).
- [ ] Day 5–6: Segmentation: semantic vs instance vs panoptic; train/fine-tune a U-Net or run [SAM](https://github.com/facebookresearch/segment-anything) for promptable segmentation; combine SAM with your detector.
- [ ] Day 7: Evaluation deep-dive on your detector: PR curves per class, failure gallery (small objects? occlusion? lighting?), one targeted fix, re-measure.

**Milestone project:** end-to-end **custom detector** (your dataset → labeled → trained → evaluated with mAP + failure analysis + the one-fix iteration). This is the project interviewers will grill — know every choice. Portfolio piece CV-3. *(~6 hrs)*

---

## Week 4 — Modern vision: ViT, CLIP, SAM, VLMs

**Goal:** the 2026 differentiator layer.

- [ ] Day 1–2: [Hugging Face Community Computer Vision Course](https://huggingface.co/learn/computer-vision-course/unit0/welcome/welcome) — Vision Transformer units: patch embeddings, attention for images, ViT vs CNN trade-offs.
- [ ] Day 3–4: CLIP: how contrastive image-text pretraining enables zero-shot classification; build a zero-shot classifier and compare against your week-2 supervised model on the same data.
- [ ] Day 5–6: [OpenCV's free Vision-Language Model Bootcamp](https://opencv.org/university/vision-language-model-bootcamp/) — third free official cert: CLIP → VLMs for captioning/detection.
- [ ] Day 7: Skim one modern topic that matches your target segment: video understanding / 3D basics / diffusion-for-vision — HF CV course has units for each. **Thesis synergy: the [VL-JEPA concepts track](../vl-jepa-concepts/roadmap.md) phases 2–4 (transformers, JEPA, CLIP) overlap this week — do them together. Prep the thesis as an interview asset with [qa-bank Q21](qa-bank.md).**

**Milestone project:** **semantic image search** over your own photo folder (CLIP embeddings + cosine search + simple UI) *or* a zero-shot quality-inspection demo. Portfolio piece CV-4. *(~5 hrs)*

---

## Week 5 — Production CV: real-time, edge, system design

**Goal:** the production sense that separates hired from rejected.

- [ ] Day 1–2: Real-time pipeline: webcam → detector → tracker (ByteTrack/OpenCV trackers) → overlay, measuring FPS honestly; find and fix your bottleneck (resolution? batch? model size?).
- [ ] Day 3–4: Deployment: export to [ONNX](https://onnxruntime.ai/) → quantize → benchmark CPU latency before/after; read how [TensorRT](https://developer.nvidia.com/tensorrt)-style optimization works conceptually.
- [ ] Day 5: Domain shift — the #1 production CV failure: why models die when the camera/lighting/site changes; mitigation (augmentation matched to deployment, continual eval sets, monitoring confidence distributions).
- [ ] Day 6–7: CV system design practice (framework in [interview-prep.md](interview-prep.md)) — two timed 45-min designs on [Excalidraw](https://excalidraw.com/): "factory defect detection line" and "retail shelf monitoring".

**Milestone:** real-time demo video (screen capture) + latency table (FP32 vs quantized) + one polished system-design doc. Portfolio piece CV-5. *(~5 hrs)*

---

## Week 6 — Interviews + OpenCV contribution push

**Goal:** convert to offers, and start the open-source track you planned.

- [ ] Drill [qa-bank.md](qa-bank.md) daily: 5 concept questions out loud + 1 from-scratch coding rep (IoU, NMS, convolution — rotate).
- [ ] 2× timed CV system designs (new prompts: parking occupancy, medical segmentation pipeline).
- [ ] 1× project deep-dive rehearsal on your detector (CV-3) with a friend grilling: "why this augmentation? why is mAP@0.5 misleading? what breaks at night?"
- [ ] General coding stays warm: 1–2 [NeetCode](https://neetcode.io/roadmap) problems/day.
- [ ] **OpenCV contribution track**: read the [contribution guide](https://github.com/opencv/opencv/wiki/How_to_contribute), build OpenCV from source once, pick 2–3 [good first issues](https://github.com/opencv/opencv/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) (docs/tutorials/Python tests are realistic entries), submit one small PR. Expect slow review — that's normal; the PR link goes on your résumé the day it's *opened*.
- [ ] Portfolio README linking CV-1…CV-5 + the three OpenCV certs + your PR; apply (manufacturing QA and video-analytics startups are the friendliest entry points; perception teams after).

**Final milestone:** full self-run loop — CV coding (60') → CV depth Q&A (45') → system design (60') → project deep-dive (30') → behavioral (30'). Rubric in [interview-prep.md](interview-prep.md).
