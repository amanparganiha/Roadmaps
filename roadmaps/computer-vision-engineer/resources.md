# Computer Vision Free Resources

Everything the [roadmap](roadmap.md) links to, plus alternatives. All free. Shared fundamentals (Python, math, PyTorch basics) live in the [AI/ML resources](../ai-ml-engineer/resources.md).

## OpenCV & classical CV
- **[OpenCV Bootcamp](https://opencv.org/university/free-opencv-course/)** — the free *official* OpenCV course with certificate; image/video ops, filtering, detection, tracking, DNN module. *(~3 hrs video + notebooks)*
- **[OpenCV Python tutorials (docs)](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)** — the reference for going deeper: contours, histograms, features, camera calibration. *(dip in as needed)*
- Alt: [Great Learning free CV courses](https://www.mygreatlearning.com/computer-vision/free-courses) — beginner-friendly OpenCV walkthroughs with certificates.

## CNNs & deep learning for vision
- **[CS231n notes](https://cs231n.github.io/)** — the canonical course notes: convolution arithmetic, architectures, training. The single best free CV text. *(~10 hrs)*
- **[CS231n lectures (YouTube)](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)** — video companion (older iterations are fine; fundamentals haven't moved).
- **[OpenCV free PyTorch Bootcamp](https://opencv.org/university/free-pytorch-course/)** — official cert #2; PyTorch training on vision tasks. *(~5 hrs)*
- **[PyTorch transfer learning tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)** — the fine-tuning workflow you'll use in every project. *(~2 hrs)*

## Detection & segmentation
- **[Ultralytics YOLO docs](https://docs.ultralytics.com/)** — train/validate/deploy custom detectors; the industry-default toolkit. *(~4 hrs to first custom model)*
- **[Roboflow](https://roboflow.com/)** (free tier) — dataset labeling/augmentation/hosting; their [blog](https://blog.roboflow.com/) and [notebooks repo](https://github.com/roboflow/notebooks) are excellent free tutorials.
- **[Label Studio](https://labelstud.io/)** — open-source annotation if you outgrow free tiers.
- **[Segment Anything (SAM) — GitHub](https://github.com/facebookresearch/segment-anything)** — model + notebooks; use it for labeling acceleration and mask generation.

## Modern vision (ViT, CLIP, VLMs)
- **[Hugging Face Community Computer Vision Course](https://huggingface.co/learn/computer-vision-course/unit0/welcome/welcome)** — community-built, broad and current: ViT, multimodal, video, 3D, generative units. *(~10 hrs selectively)*
- **[OpenCV Vision-Language Model Bootcamp](https://opencv.org/university/vision-language-model-bootcamp/)** — official cert #3: CLIP → VLM captioning/detection hands-on. *(~4 hrs)*

## Deployment & production
- **[ONNX Runtime docs](https://onnxruntime.ai/)** — export + quantize + benchmark; the portable-deployment default. *(~3 hrs)*
- **[TensorRT overview](https://developer.nvidia.com/tensorrt)** — read conceptually for GPU-edge answers (setup optional).

## Interview drilling
- **[Devinterview-io CV interview questions](https://github.com/Devinterview-io/computer-vision-interview-questions)** — big free question bank for breadth sweeps.
- **[andrewekhalel/MLQuestions](https://github.com/andrewekhalel/MLQuestions)** — classic ML/CV interview question collection.
- **[Interview Query CV questions](https://www.interviewquery.com/p/computer-vision-interview-questions)** — worked discussion, free tier.
- **[Pramp](https://www.pramp.com/)** — free peer mocks for the general coding round.

## Open source (your OpenCV plan)
- **[OpenCV contribution guide](https://github.com/opencv/opencv/wiki/How_to_contribute)** — read before your first PR; coding style + PR process.
- **[OpenCV good first issues](https://github.com/opencv/opencv/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)** — realistic entries: docs/tutorials, Python binding tests, small bug fixes.
- Expect slow reviews (large old C++ codebase); keep an MCP/LangChain contribution running in parallel per the [remote strategy](../remote-ai-career/resources.md).

## Free certifications
- **[OpenCV Bootcamp certificate](https://opencv.org/university/free-opencv-course/)**, **[PyTorch Bootcamp certificate](https://opencv.org/university/free-pytorch-course/)**, **[VLM Bootcamp certificate](https://opencv.org/university/vision-language-model-bootcamp/)** — all three are official OpenCV.org certs, genuinely free, and directly on-brand for a CV engineer résumé. Do these three; they're built into the roadmap weeks 1, 2, and 4.
- [Kaggle Learn — Computer Vision](https://www.kaggle.com/learn) micro-cert as a quick extra.

## Project fuel
- **[Kaggle Datasets](https://www.kaggle.com/datasets)** + [Kaggle CV competitions](https://www.kaggle.com/competitions) — datasets and leaderboard practice.
- **[Papers With Code — CV](https://paperswithcode.com/area/computer-vision)** — find the current SOTA + code for any task when you need it.
