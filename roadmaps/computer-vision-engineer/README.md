# Computer Vision Engineer

## What the role is

A Computer Vision Engineer builds systems that understand images and video: detecting defects on production lines, reading medical scans, powering robot/vehicle perception, tracking objects in video, and increasingly wiring vision-language models (CLIP, SAM, VLMs) into products. In 2026 the role spans two layers:

- **Classical + deep CV core**: image processing (OpenCV), CNNs, object detection, segmentation, tracking — still the daily bread of most CV jobs.
- **Modern vision stack**: vision transformers, CLIP-style zero-shot models, SAM, and multimodal VLMs — the fastest-growing interview topic.

CV is more *specialized* than generalist AI/ML: fewer openings, but also fewer qualified candidates, and demand is expanding fast (manufacturing inspection, healthcare imaging, autonomy, video analytics).

## Who hires

| Segment | Notes |
|---|---|
| Autonomy & robotics (Tesla, Zoox, drone/robotics startups) | Perception teams; strongest engineering bar; C++ often appears. |
| Manufacturing / industrial QA | Defect detection, metrology; underrated, lots of openings, practical OpenCV + detection skills. |
| Healthcare imaging | Segmentation-heavy; regulatory awareness is a plus. |
| Big tech (Meta, Apple, NVIDIA, Google) | AR/VR, camera pipelines, foundation vision models; MLE loop + CV depth. |
| Retail/security video analytics | Detection + tracking + edge deployment; startup-heavy, portfolio-driven. |

## Prerequisites (don't skip)

This track **builds on the [AI/ML Engineer roadmap](../ai-ml-engineer/roadmap.md) weeks 1–3** (Python/NumPy, classic ML basics, PyTorch + backprop). If you're following the Krish Naik course, its Python/ML/DL sections cover the same ground — finish those first, then start here.

## The skills profile

- **Core**: image fundamentals (color spaces, filtering, edges, transforms), OpenCV fluency, CNNs and training craft (augmentation, transfer learning), detection (IoU/mAP/NMS, YOLO-family), segmentation.
- **Modern (2026 must-have)**: ViT, CLIP zero-shot, SAM, VLM basics.
- **Production**: ONNX export, quantization, real-time video pipelines, latency budgets on edge hardware, drift/domain-shift debugging.
- **Interview extras**: implement IoU/NMS/convolution from scratch; CV system design (a camera-to-decision pipeline).

## What's in this package

| File | What it's for |
|---|---|
| [roadmap.md](roadmap.md) | 6-week intensive CV plan (~3–4 hrs/day) on top of the AI/ML fundamentals |
| [interview-prep.md](interview-prep.md) | CV interview loops, question bank by round, drill schedule |
| [qa-bank.md](qa-bank.md) | Detailed questions **with answers**: fundamentals, from-scratch code (IoU, NMS, convolution), worked system design |
| [resources.md](resources.md) | Free resources + the three **free official OpenCV certifications** |

## Why this track pairs well with your OpenCV contribution plan

Weeks 1–2 make you a fluent OpenCV *user* (the free official bootcamp + a real project), which is exactly the base you need before contributing: you'll recognize real issues, understand the module layout, and can credibly pick up `good first issue` tickets. Week 6 includes a structured contribution push.
