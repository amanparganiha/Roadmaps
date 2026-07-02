# VL-JEPA Quick Reference

Compact index of the curriculum's sources ([full context in roadmap.md](roadmap.md)).

## Primary papers (the spine)
- **[VL-JEPA](https://arxiv.org/abs/2512.10942)** — the paper the thesis builds on (Chen et al., Meta FAIR, ICLR 2026)
- **[V-JEPA 2](https://arxiv.org/abs/2506.09985)** — the video encoder
- **[I-JEPA / V-JEPA code](https://github.com/facebookresearch/jepa)** — reference implementation
- **[VICReg](https://arxiv.org/abs/2105.04906)** — anti-collapse regularization family
- **[SONAR](https://arxiv.org/abs/2308.11466)** + [GitHub](https://github.com/facebookresearch/SONAR) — invertible text embedding space
- **[ViT](https://openreview.net/forum?id=YicbFdNTTy)** — patch tokenization
- **[VideoLLM-online](https://arxiv.org/abs/2406.11816)** — closest streaming-captioning analog
- CLIP (Radford et al.) · SimCLR (Chen et al.) · CPC/InfoNCE (van den Oord et al.) · CIDEr (Vedantam et al.) · [LeCun's JEPA position paper](https://openreview.net/forum?id=BZ5a1r-kVsf)

## Video channels (by what they're best at)
- **[3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)** — intuition: embeddings, attention
- **[Karpathy — Zero to Hero](https://karpathy.ai/zero-to-hero.html)** — build it in code: micrograd, GPT
- **Yannic Kilcher** — paper walkthroughs: [V-JEPA](https://www.youtube.com/watch?v=7UkJPwz_N_0), JEPA position paper, SimCLR
- **[StatQuest](https://www.youtube.com/@statquest)** — clustering: [hierarchical](https://www.youtube.com/watch?v=7xHsRkOdVwo), [k-means](https://www.youtube.com/watch?v=4b5d3muPQmA)
- **[Stanford CS224n](https://web.stanford.edu/class/cs224n/)** — rigor: [2023 Lecture 8, transformers](https://www.youtube.com/watch?v=LWMzyfvuehA)
- **[The AI Epiphany](https://www.youtube.com/watch?v=fQyHEXZB-nM)** — CLIP explained

## Explainers & guides
- [Rohit Bandaru — JEPA Deep Dive](https://rohitbandaru.github.io/blog/JEPA-Deep-Dive/) (best single JEPA read)
- [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) · [TechTalks VL-JEPA overview](https://bdtechtalks.com/2026/01/03/meta-vl-jepa-vision-language-model/) · [LearnOpenCV V-JEPA 2 guide](https://learnopencv.com/v-jepa-2-meta-world-model-robotics-guide/)
- [EmergentMind — InfoNCE](https://www.emergentmind.com/topics/infonce) · [AssemblyAI — VICReg review](https://www.assemblyai.com/blog/review-vicreg-variance-invariance-covariance-regularization-for-self-supervised-learning)

## Tools & docs
- [PyTorch training tutorial](https://docs.pytorch.org/tutorials/beginner/introyt/trainingyt.html) · [Raschka PyTorch-in-1h](https://sebastianraschka.com/teaching/pytorch-1h/)
- [scikit-learn clustering](https://scikit-learn.org/stable/modules/clustering.html) · [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html) · `ruptures` (change-point detection)
- [HF LLM course](https://huggingface.co/learn/llm-course/en/chapter1/1) · [HF CV course](https://huggingface.co/learn/computer-vision-course) · [sbert.net](https://sbert.net/)

## Cross-links
- [CV roadmap](../computer-vision-engineer/roadmap.md) — the general CV foundation running in parallel
- [CV qa-bank Q21](../computer-vision-engineer/qa-bank.md) — JEPA vs MAE vs contrastive, interview-ready
- [Remote strategy](../remote-ai-career/roadmap.md) — write up the thesis publicly when your advisor allows; it's your strongest findable artifact
