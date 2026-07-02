# Computer Vision Q&A Bank

Detailed questions **with answers**. ⭐ = near-universal. Shared fundamentals (backprop, BatchNorm, optimizers, bias/variance) live in the [AI/ML qa-bank](../ai-ml-engineer/qa-bank.md) — drill both.

---

## Part 1 — Fundamentals

### ⭐ Q1. Why are convolutions the right tool for images?
**Answer:** Three properties of images map to three properties of convolution: (1) **locality** — nearby pixels are related, and a small kernel looks at local neighborhoods; (2) **translation equivariance** — a cat in the corner is still a cat in the center, and sliding the same kernel everywhere means features are detected regardless of position; (3) **parameter sharing** — one 3×3 kernel (9 weights) scans the whole image instead of a fully-connected layer needing millions of weights per output. Result: far fewer parameters, better generalization, and a built-in prior that matches image structure. Follow-up worth volunteering: ViTs relax these priors and substitute scale — with enough data, learned attention can beat hand-built inductive bias.

### ⭐ Q2. Explain receptive field and why it matters.
**Answer:** The region of the input image that influences one output neuron. A single 3×3 conv sees 3×3 pixels; stacking layers grows it (two 3×3 = 5×5 effective), and stride/pooling/dilation grow it faster. It matters because a network can't reason about objects bigger than its receptive field — a detector whose deepest features see 100×100 pixels will miss a 400-pixel object's global structure. Practical answers interviewers want: detect small objects on high-res feature maps (early layers / FPN), large objects on deep coarse maps; dilated convolutions grow the field without losing resolution (segmentation loves them).

### Q3. What does pooling do, and what's the trade-off vs strided convolutions?
**Answer:** Both downsample: reduce spatial size, grow receptive field, cut compute, add small translation invariance. Max-pooling keeps the strongest activation (cheap, no parameters, biased toward "is the feature present"); strided conv learns *how* to downsample (more expressive, costs parameters). Modern nets mostly use strided convs; the deeper interview point is what's lost either way — precise localization — which is why segmentation architectures add skip connections (U-Net) to recover fine detail.

### ⭐ Q4. Which data augmentations are safe, and when do they break?
**Answer:** Augmentation should simulate variation the model will actually meet, without changing the label. Safe defaults for natural photos: crops, horizontal flip, color jitter, slight rotation/scale, blur/noise. Breakage cases interviewers love: **horizontal flip on text/digits** (mirror-image characters change meaning), **flips in medical imaging** where laterality matters (situs of organs), **heavy color jitter when color *is* the signal** (ripeness, skin lesions, wire colors), rotation for orientation-dependent tasks (satellite "north-up" conventions). For detection, geometric transforms must also transform the boxes. Best practice: build augmentation from the *deployment failure gallery*, not a generic recipe.

### Q5. Transfer learning: what do you freeze and when?
**Answer:** Rule of thumb by data size and domain gap: (1) tiny dataset, similar domain → freeze the backbone, train only the head; (2) medium data → unfreeze the last block(s), lower LR on pretrained layers (discriminative LRs); (3) large data or big domain gap (natural photos → X-ray/thermal) → fine-tune everything, possibly from self-supervised weights; training from scratch is justified only with huge data or exotic inputs (e.g., 7-channel satellite). Always mention: early conv layers learn generic edges/textures that transfer almost universally — that's why freezing them is cheap.

---

## Part 2 — Detection & segmentation

### ⭐ Q6. Explain IoU, and why detection needs it.
**Answer:** Intersection-over-Union = overlap area / union area between predicted and ground-truth boxes — a scale-invariant measure of localization quality in [0,1]. Detection needs it because "correct" isn't binary: a prediction is counted a true positive only if IoU with a ground-truth box exceeds a threshold (0.5 classically). It's also the matching currency inside NMS and inside mAP computation. Nuance worth adding: IoU is harsh on small objects (a 2-pixel shift tanks IoU for a 10-pixel box) — one reason small-object detection is hard to score well.

### ⭐ Q7. Explain NMS — why it exists and its failure modes.
**Answer:** Detectors emit many overlapping boxes for the same object (dense heads score every anchor/location). NMS cleans up: sort by confidence, keep the top box, suppress all boxes with IoU above a threshold against it, repeat. Failure modes: **crowded scenes** — two genuinely overlapping objects (people in a crowd) get one suppressed; threshold tension (too low → misses in crowds, too high → duplicates survive). Fixes to name: Soft-NMS (decay scores instead of deleting), class-aware NMS, or end-to-end architectures (DETR-family) that learn deduplication and skip NMS entirely. Code in Part 3.

### ⭐ Q8. Walk me through how mAP is computed.
**Answer:** Per class: (1) sort all predictions across the dataset by confidence; (2) walking down that list, mark each prediction TP if it matches an unmatched ground-truth box with IoU ≥ threshold, else FP; (3) at each step compute cumulative precision and recall → a PR curve; (4) AP = area under that curve; (5) mAP = mean over classes. "mAP@[.5:.95]" (COCO) averages this over IoU thresholds 0.5–0.95, rewarding tight localization. When it misleads: dominated by common classes unless per-class is reported; blind to confidence calibration; a model can have great mAP but a terrible operating point for *your* error costs — production picks one threshold from the PR curve, mAP averages them all.

### Q9. One-stage vs two-stage detectors; anchor-based vs anchor-free.
**Answer:** **Two-stage** (Faster R-CNN family): propose regions first, then classify/refine each — historically more accurate, slower. **One-stage** (YOLO/SSD/RetinaNet): predict boxes densely in one pass — faster, and since focal loss fixed the extreme background-imbalance problem, competitive in accuracy; the practical default (YOLO-family) for real-time work. **Anchor-based**: predict offsets from preset box shapes (needs anchor tuning); **anchor-free** (FCOS/CenterNet, modern YOLOs): predict centers/distances directly — simpler, fewer hyperparameters. Honest practical answer: "for most industrial jobs I start with a pretrained modern YOLO and spend my time on data and evaluation, not architecture."

### Q10. Focal loss — what problem does it solve?
**Answer:** Dense one-stage detectors evaluate ~100k locations per image, nearly all easy background. Standard cross-entropy lets that ocean of easy negatives dominate the gradient, drowning the rare hard examples. Focal loss multiplies CE by (1−p)^γ, down-weighting examples the model already gets right, so training focuses on hard cases. It's also the go-to answer for extreme class imbalance in classification generally.

### Q11. Semantic vs instance vs panoptic segmentation; and why Dice/IoU loss?
**Answer:** **Semantic**: label every pixel by class ("road", "person") — instances merge. **Instance**: separate masks per object instance (person-1 vs person-2). **Panoptic**: both — every pixel gets class + instance id. Losses: pixel-wise cross-entropy struggles when the object is 1% of pixels (predicting "all background" is 99% accurate); **Dice/IoU losses** optimize overlap directly and are robust to that imbalance — standard in medical imaging. U-Net's skip connections (encoder detail → decoder) are why it's still the medical default.

### Q12. How would you handle small-object detection?
**Answer:** Multi-pronged: higher input resolution (the biggest single lever, costs latency); FPN-style multi-scale features so small objects are detected on fine maps; tiling/SAHI (slice the image, detect per tile, merge with NMS) for huge images like satellite/PCB; augmentation that pastes small objects; and honest evaluation — report AP-small separately. Also question the camera first: moving it closer or upping resolution is often cheaper than any model fix — a very FDE-flavored answer that CV interviewers also reward.

---

## Part 3 — From-scratch code (the CV coding round)

### ⭐ Q13. IoU between two boxes.
```python
def iou(a, b):
    # boxes as (x1, y1, x2, y2)
    ix1, iy1 = max(a[0], b[0]), max(a[1], b[1])
    ix2, iy2 = min(a[2], b[2]), min(a[3], b[3])
    iw, ih = max(0.0, ix2 - ix1), max(0.0, iy2 - iy1)   # clamp: no overlap → 0
    inter = iw * ih
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter + 1e-9)
```
**Narrate:** the clamp to 0 for disjoint boxes is where most candidates bug out; the epsilon guards degenerate zero-area boxes. Offer the vectorized N×M version with broadcasting — `np.maximum(a[:, None, :2], b[None, :, :2])` — before being asked.

### ⭐ Q14. NMS.
```python
def nms(boxes, scores, iou_thresh=0.5):
    order = sorted(range(len(boxes)), key=lambda i: scores[i], reverse=True)
    keep = []
    while order:
        best = order.pop(0)
        keep.append(best)
        order = [i for i in order if iou(boxes[best], boxes[i]) < iou_thresh]
    return keep
```
**Narrate:** O(n²) worst case — fine for hundreds of boxes, and real systems pre-filter by a confidence threshold first; per-class NMS runs this independently per class. Mention Soft-NMS as the crowded-scene fix (decay scores by IoU instead of deleting).

### ⭐ Q15. 2D convolution in NumPy.
```python
import numpy as np

def conv2d(img, kernel, stride=1, pad=0):
    if pad:
        img = np.pad(img, pad)
    kh, kw = kernel.shape
    oh = (img.shape[0] - kh) // stride + 1
    ow = (img.shape[1] - kw) // stride + 1
    out = np.zeros((oh, ow))
    for y in range(oh):
        for x in range(ow):
            patch = img[y*stride:y*stride+kh, x*stride:x*stride+kw]
            out[y, x] = np.sum(patch * kernel)
    return out
```
**Narrate:** state the output-size formula out loud — (N − K + 2P)/S + 1 — interviewers ask it constantly. Note this is cross-correlation (true convolution flips the kernel; deep learning "conv" never bothers). Know that real implementations use im2col + matrix multiply or FFT for speed.

### Q16. Bilinear interpolation (image resize).
**Answer sketch:** for each output pixel, map back to fractional source coordinates (x, y); take the 4 surrounding pixels; blend horizontally by the fractional x, then vertically by fractional y (weights sum to 1). Edge handling: clamp coordinates to valid range. Say why it matters: it's inside every resize, RoI-Align, and spatial transformer — and RoI-*Align* vs RoI-Pool (no quantization, exact fractional sampling) is a classic follow-up.

---

## Part 4 — Modern vision

### ⭐ Q17. ViT vs CNN — when does each win?
**Answer:** ViT splits the image into patches, embeds them as tokens, and runs a standard transformer — no convolutional priors, so every patch can attend to every other from layer 1 (global context immediately, vs CNNs building it slowly). Trade-off: without locality/equivariance priors, ViTs need much more data or strong pretraining to match CNNs; with large-scale pretraining they scale better and dominate foundation-model land. Practical guidance: small dataset + from-scratch → CNN; fine-tuning big pretrained checkpoints or multimodal work → ViT-based. Hybrid answer for real jobs: "I use whatever pretrained backbone is best-supported; at industrial data scales the data pipeline matters more than CNN-vs-ViT."

### ⭐ Q18. How does CLIP enable zero-shot classification?
**Answer:** CLIP trains an image encoder and a text encoder contrastively on ~400M image-caption pairs: matching pairs pulled together in a shared embedding space, mismatched pushed apart. Zero-shot classification: embed the image, embed text prompts ("a photo of a defective bottle", "a photo of a normal bottle"), pick the closest — no training on your classes at all. Practical uses beyond the party trick: bootstrap labeling (pre-sort unlabeled data), semantic image search, open-vocabulary detection (find objects by description). Limits to name: fine-grained distinctions and counting are weak; prompt wording moves accuracy; domain gap (CLIP saw web photos, not your X-rays).

### Q19. What is SAM and where does it fit a real pipeline?
**Answer:** Segment Anything — a promptable segmentation foundation model: give it a point, box, or (with variants) text, and it returns a high-quality mask for that object, zero-shot. Where it actually fits: **labeling acceleration** (click → mask instead of hand-drawn polygons — 10× faster annotation), mask generation downstream of a detector (detector finds boxes, SAM refines to masks), and interactive tools. Limits: it segments *things* but doesn't know *what* they are (pair with a classifier/CLIP), and it's heavy for real-time edge use (distilled variants exist).

### Q20. Your model worked in the lab and fails on the factory camera. Debug it.
**Answer:** Domain shift, worked as a funnel: (1) **look at the failing images first** — 15 minutes of looking beats a week of guessing (different lighting? focus? angle? new product variant?); (2) compare input distributions (brightness/contrast/blur stats, embedding-space distance between lab and field data); (3) check the boring layer — camera auto-exposure/white-balance drift, compression artifacts from the video pipeline, resolution mismatch in preprocessing (a resize-interpolation mismatch between training and serving is a real classic); (4) fix cheapest-first: control the environment (fix exposure, add lighting — hardware beats retraining), match augmentation to observed variation, fine-tune on a few hundred field images; (5) prevent recurrence: an eval set *from the deployment site*, confidence monitoring, and a periodic sampled human review loop.

---

### Q21. Explain self-supervised learning in vision — contrastive vs masked-reconstruction vs JEPA.
**Answer:** SSL learns representations from unlabeled images/video by inventing a pretext task, so you can pretrain on cheap unlabeled data and fine-tune on small labeled sets. Three families: (1) **Contrastive/distillation** (SimCLR, DINO): pull augmented views of the same image together in embedding space — powerful, but depends heavily on augmentation choices (and negatives, for the contrastive variants). (2) **Masked reconstruction** (MAE): mask most patches, reconstruct them *in pixel space* — simple and scalable, but spends capacity modeling pixel-level detail (texture, noise) that downstream tasks rarely need. (3) **JEPA-family** (I-JEPA, V-JEPA for video): predict the *latent representations* of masked regions from visible context, not the pixels — the model learns semantic structure without wasting capacity on appearance detail, and without hand-crafted augmentations. For video, V-JEPA predicts representations of masked spatiotemporal blocks, learning motion and object dynamics from raw video. Why interviewers care: labels are the bottleneck of industrial CV, and SSL pretraining on in-domain unlabeled data (e.g., a factory's own camera feeds) is often the cheapest accuracy win available. If you've built on JEPA (thesis/research), lead with it in depth rounds — be ready to defend latent-prediction vs pixel-reconstruction and describe your eval protocol (linear probe vs fine-tune).

---

## Part 5 — System design: worked example

### ⭐ Q22. "Design defect detection for a bottling line — 30 bottles/second."

**1. Clarify:** defect types (cap, fill level, label, cracks — different problems!); error costs — a missed defect reaching customers vs a good bottle rejected (usually misses are far costlier, so tune for recall with a manual-review lane for borderline); can we control camera and lighting? (yes on a factory line — huge advantage); reject mechanism latency budget (bottle must be flagged before the diverter — maybe 100ms end-to-end).

**2. Exploit the controlled environment:** fixed camera, strobe/backlight, consistent background — this makes classical CV viable for some defects (fill level = edge detection against a backlight is more reliable than any CNN) and makes learned models dramatically easier. Saying "fixed lighting first" is a hire signal.

**3. Baseline → model:** start hybrid — classical checks (fill level, cap presence via template/edges) + one compact detector/classifier for visual defects (label tears, cracks). Pretrained backbone fine-tuned on a few thousand labeled bottle crops; the *labeling plan* matters more: sample from the real line across shifts/products, SAM-assisted annotation, defect taxonomy agreed with QA staff.

**4. Throughput math (do it out loud):** 30 bottles/sec → ~33ms per bottle. Quantized small model on an edge GPU/accelerator at the line (streaming video to cloud at this rate is a bandwidth and latency non-starter). Batch = trigger per bottle via a photoelectric sensor rather than free-running video — simpler and deterministic.

**5. Serving & failure modes:** watchdog on camera health (a dirty lens fails *gradually* — monitor image sharpness/brightness stats); if the model or camera fails, fail *safe* per business rule (divert to manual inspection lane, never silently pass); log every rejected/borderline image.

**6. Monitoring & iteration:** dashboard of reject rate per defect type per shift (a spike at shift change = lighting/procedure, not model); weekly sampled review of passes (miss estimation); retrain trigger on new products; the borderline-review lane continuously generates labeled data — the feedback flywheel.

---

## How to drill this bank

- **Parts 1–2, 4:** 5 questions/day out loud as if teaching; re-derive, don't recite.
- **Part 3:** type each from a blank file weekly until IoU/NMS/conv take <15 minutes combined.
- **Part 5:** whiteboard the bottling case yourself before reading; then do parking-occupancy and shelf-monitoring cold, 45' timed.
- Breadth sweeps: [Devinterview-io CV bank](https://github.com/Devinterview-io/computer-vision-interview-questions) for volume once these are solid.
