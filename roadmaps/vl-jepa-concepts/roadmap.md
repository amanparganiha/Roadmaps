# VL-JEPA Curriculum — 6-Week Staging (~80–110 h)

🔴 critical · 🟡 important · 🟢 background. Each week ends with a **benchmark** — don't advance until you pass it (explaining out loud counts; re-watching doesn't).

| Week | Phases | Benchmark to advance |
|---|---|---|
| 1–2 | 0–2: Foundations + Transformers | Sketch the V-JEPA encoder/predictor data flow |
| 3–4 | 3–4: JEPA + Contrastive/CLIP | Explain why embedding prediction avoids blurry-average losses; identify InfoNCE in the paper's loss |
| 5 | 5–6: Text embeddings + selective decoding | Implement a toy "decode-on-change" loop on a synthetic embedding stream |
| 6 | 7–8: Video/streaming + metrics + tooling | Compute CIDEr on a toy caption set; explain Recall@1 |
| — | Capstone | Re-read the whole VL-JEPA paper; understand every component |

---

## Phase 0 — Orientation (½ day, ~3–4 h) 🔴

Read the thing you're working toward *first*, lightly, so every later concept has a hook.

- [ ] Skim the VL-JEPA paper abstract + figures — [arXiv 2512.10942](https://arxiv.org/abs/2512.10942) ([PDF](https://arxiv.org/pdf/2512.10942)). Delong Chen et al., Meta FAIR.
- [ ] Plain-English overview: [Ben Dickson, TechTalks](https://bdtechtalks.com/2026/01/03/meta-vl-jepa-vision-language-model/).
- [ ] **Goal check:** state in one sentence what LiveJEPA does and why "predict the embedding, decode only when needed" matters for real-time captioning.

## Phase 1 — Foundations: embeddings, similarity, PyTorch (~10–14 h) 🔴/🟡

- [ ] **1A** 🔴 [3Blue1Brown — "But what is a GPT?"](https://www.youtube.com/watch?v=yMQPQuz5WpA) (~27 min) — embeddings as directions-carry-meaning; the mental model the whole project rests on. Full refresher if needed: [Neural Networks playlist](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) ch. 1–4.
- [ ] **1A** reading: [Google MLCC — Embeddings module](https://developers.google.com/machine-learning/crash-course/embeddings).
- [ ] **1B** 🔴 Cosine similarity + L2 normalization: [HF CLIP page](https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/clip-and-relatives/clip) + [OpenAI CLIP repo](https://github.com/openai/CLIP) ("cosine similarities × 100"). **Goal:** why normalize before comparing; what "close in embedding space" means numerically.
- [ ] **1C** 🟡 [Karpathy — micrograd](https://karpathy.ai/zero-to-hero.html) (~2h25m) so `backward()`/`zero_grad()` stop being magic; then the official [PyTorch training tutorial](https://docs.pytorch.org/tutorials/beginner/introyt/trainingyt.html) and [Raschka — PyTorch in One Hour](https://sebastianraschka.com/teaching/pytorch-1h/).

## Phase 2 — Transformers & vision encoders (~16–20 h) 🔴

The V-JEPA encoder and Llama predictor are both Transformers — non-negotiable.

- [ ] **2A** [3Blue1Brown — Attention, visually explained](https://www.youtube.com/watch?v=eMlx5fFNoYc) (~26 min): Q/K/V, softmax attention, the −∞ masking trick.
- [ ] **2A** [Karpathy — "Let's build GPT"](https://www.youtube.com/watch?v=kCc8FmEb1nY) (1h56m): implement self-attention, multi-head, positional encoding, causal masking yourself.
- [ ] **2A** rigor (skip if the above feel comfortable): [CS224n 2023 Lecture 8](https://www.youtube.com/watch?v=LWMzyfvuehA) (~1h15m) · [course page](https://web.stanford.edu/class/cs224n/) · [playlist](https://www.youtube.com/playlist?list=PLrLxpnf4DCA86z2XBgBQq2s6sKUTD5Bqm). Reading: Vaswani et al. + [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/).
- [ ] **2B** 🔴 Causal vs bidirectional masks — covered in both videos above. **Project note:** V-JEPA's *encoder* is bidirectional over video patches; the Llama-initialized *predictor* is causal — that difference explains the architecture.
- [ ] **2C** 🔴 ViT: [Dosovitskiy et al., "An Image is Worth 16×16 Words"](https://openreview.net/forum?id=YicbFdNTTy) — the patch idea V-JEPA extends to 3D tubelets. Companions: [HF CV course](https://huggingface.co/learn/computer-vision-course) ViT unit, [CS231n 2024 attention slides](https://cs231n.stanford.edu/slides/2024/lecture_8.pdf).
- [ ] **2D** 🔴 [Yannic Kilcher — V-JEPA explained](https://www.youtube.com/watch?v=7UkJPwz_N_0) (~50 min): encoder, predictor, masking, why feature-space beats pixel prediction (doubles as the bridge to Phase 3).
- [ ] **2D** reading: [V-JEPA 2 paper](https://arxiv.org/abs/2506.09985) (Assran/Bardes et al., Meta). Retain: 1.2B params, ViT-g encoder, >1M hours video (VideoMix22M); 77.3 top-1 on SSv2, 39.7 R@5 on Epic-Kitchens-100; mask-denoising in representation space, L1 loss, stop-gradient + EMA target encoder against collapse. Hands-on: [LearnOpenCV V-JEPA 2 guide](https://learnopencv.com/v-jepa-2-meta-world-model-robotics-guide/).
- [ ] **2D** Llama background (light): decoder-transformer mechanics from Karpathy's video suffice; SONAR's encoder builds on Llama-3.2-1B.

## Phase 3 — JEPA: the core idea (~12–16 h) 🔴 MOST CRITICAL

- [ ] **3A** Yannic Kilcher — "JEPA: A Path Towards Autonomous Machine Intelligence" (~59 min; search the channel by title; [paper](https://openreview.net/forum?id=BZ5a1r-kVsf)): energy-based models, latents, collapse, contrastive vs regularized, JEPA/H-JEPA.
- [ ] **3A** reading: LeCun's position paper + [Rohit Bandaru — JEPA Deep Dive](https://rohitbandaru.github.io/blog/JEPA-Deep-Dive/) (JEPA, I-JEPA, V-JEPA in one place).
- [ ] **3B** 🔴 I-JEPA/V-JEPA papers + [code](https://github.com/facebookresearch/jepa); re-use the Kilcher V-JEPA video's pixel-vs-feature contrast.
- [ ] **3C** 🔴 The central thesis — read VL-JEPA §1–2 *now* with the JEPA background; gentle companion: [Anshul Bakode — "Thinks in Embeddings, Not Words"](https://medium.com/@anshulbakode/vl-jepa-the-vision-language-model-that-thinks-in-embeddings-not-words-ab642801cb01).
- [ ] **3D** 🔴 Collapse + anti-collapse: [VICReg paper](https://arxiv.org/abs/2105.04906) (variance/invariance/covariance; why pull-only objectives collapse) + [AssemblyAI plain-language review](https://www.assemblyai.com/blog/review-vicreg-variance-invariance-covariance-regularization-for-self-supervised-learning). **Note:** VL-JEPA uses InfoNCE (contrastive anti-collapse); the paper flags VICReg/SIGReg as unevaluated alternatives — know both families.

## Phase 4 — Contrastive learning, InfoNCE & CLIP (~12–16 h) 🔴

- [ ] **4A** Yannic Kilcher's SimCLR explainer (search channel; paper: Chen et al. 2020) — positives/negatives, why we push apart. Companion: [InfoNCE explained (Medium)](https://medium.com/@mlshark/infonce-explained-in-details-and-implementations-902f28199ce6).
- [ ] **4B** 🔴 InfoNCE math: van den Oord et al. (CPC paper); formula + mutual-information bound summarized at [EmergentMind](https://www.emergentmind.com/topics/infonce). **Goal:** read VL-JEPA's loss and recognize temperature τ, one positive, many negatives, cosine in the exponent.
- [ ] **4C** 🔴 CLIP: [Aleksa Gordić — CLIP paper explained](https://www.youtube.com/watch?v=fQyHEXZB-nM) + [OpenAI CLIP page](https://openai.com/index/clip/) + Radford et al. Dual encoder, symmetric InfoNCE, 400M pairs. VL-JEPA is benchmarked against CLIP/SigLIP2/Perception Encoder on 8+8 classification/retrieval datasets.
- [ ] **4D** 🟡 Wang & Isola, alignment & uniformity on the hypersphere — why L2-normalization and the sphere matter.

## Phase 5 — Text embeddings & decoding back to text (~6–9 h) 🟡 (SONAR 🔴)

- [ ] **5A** [Intuitive Sentence-BERT (TDS)](https://towardsdatascience.com/an-intuitive-explanation-of-sentence-bert-1984d144a868/) + [sbert.net](https://sbert.net/) (siamese nets, mean pooling, cosine). Ref: Reimers & Gurevych 2019.
- [ ] **5B** 🔴 SONAR — the project's decoding step: [paper](https://arxiv.org/abs/2308.11466) + [GitHub](https://github.com/facebookresearch/SONAR). Retain: single 1024-d space, 200 languages, NLLB-initialized encoder/decoder, mean-pooled fixed-length vector, MSE alignment, decoder inverts the bottleneck via beam search (`TextToEmbeddingModelPipeline` / `EmbeddingToTextModelPipeline`). Companion: [Bryan Teo — SONAR Explained](https://medium.com/@bteo/sonar-explained-a9c99f1376e8).
- [ ] **5C** 🟡 Embedding-to-text inversion generally = seq2seq attending to one bottleneck vector (covered by SONAR).
- [ ] **5D** 🟢 EmbeddingGemma model card — know it exists as an alternative backbone.

## Phase 6 — Clustering & selective decoding (~12–16 h) 🔴 MOST CRITICAL (the original research)

Where LiveJEPA decides *when* to emit a caption.

- [ ] **6A** [StatQuest — Hierarchical clustering](https://www.youtube.com/watch?v=7xHsRkOdVwo) (~11 min) + [k-means](https://www.youtube.com/watch?v=4b5d3muPQmA) (~9 min, contrast) + [scikit-learn clustering guide](https://scikit-learn.org/stable/modules/clustering.html).
- [ ] **6B** 🔴 Ward linkage / variance minimization: [Ward's method (Wikipedia)](https://en.wikipedia.org/wiki/Ward%27s_method) + [merge-cost walkthrough](https://jbhender.github.io/Stats506/F18/GP/Group10.html): Δ(A,B) = (n_A n_B)/(n_A+n_B)·‖m_A − m_B‖² — merge the pair that grows within-cluster variance least; directly the "group consecutive embeddings by minimizing variance" idea.
- [ ] **6C** 🔴 Temporal/connectivity-constrained clustering: [AgglomerativeClustering docs](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html) + [with/without structure example](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering.html) — adjacency-in-time constraint = segmenting a streaming embedding sequence.
- [ ] **6D** 🔴 Change-point detection: [Fraunhofer IESE intro](https://www.iese.fraunhofer.de/blog/change-point-detection/) + [online vs offline CPD](https://techrando.com/2019/08/14/a-brief-introduction-to-change-point-detection-using-python/) — "decode only when a new event occurs" is *online* CPD on the embedding stream. Tool: `ruptures`.
- [ ] **6E** 🟡 Moving averages / smoothing (pandas `.rolling().mean()`): denoise the inter-embedding distance signal before thresholding.
- [ ] **6F** 🔴 **Tie it together in a notebook:** smooth the distance signal → detect a change-point/variance spike ("new event") → one decode per segment. Then **re-read VL-JEPA §4.5** and confirm the paper's exact trigger rule against your implementation *(the ~2.85× figure and event-triggered framing are confirmed; the precise formula must be verified in the PDF)*.

## Phase 7 — Video understanding, streaming & evaluation (~10–14 h) 🔴/🟡

- [ ] **7A** 🟡 [Video captioning survey](https://arxiv.org/pdf/2204.05976) — task framing + BLEU/METEOR/ROUGE-L/CIDEr suite.
- [ ] **7B** 🔴 [VideoLLM-online (CVPR 2024)](https://arxiv.org/abs/2406.11816) — LIVE framework, Streaming EOS prediction ("when to respond"), 5–15 FPS on 3090/A100. The closest published analog: its EOS-trigger vs VL-JEPA's embedding-change trigger — know the contrast cold; it's a thesis-defense question waiting to happen.
- [ ] **7C** 🟢 VQA basics: skim GQA / VQA-v2 dataset pages (VL-JEPA evaluates on GQA, TallyQA, POPE, POPEv2).
- [ ] **7D** 🟡 Text-to-video retrieval + Recall@K.
- [ ] **7E** 🔴 CIDEr (Vedantam et al. 2015): average cosine similarity of TF-IDF-weighted n-grams — distinctive consensus content scores high; range ~0–5 (or ×100). Plus BLEU (n-gram precision + brevity), METEOR (unigram P/R + synonyms), ROUGE-L (LCS recall), SPICE (scene graphs). Comparison: [Labellerr guide](https://www.labellerr.com/blog/image-captioning-evaluation-and-fine-tuning/).

## Phase 8 — Tooling (interleave, ~5–7 h) 🟡

- [ ] [HF course welcome video](https://www.youtube.com/watch?v=00GKzGyWFEs) + [HF LLM course ch. 1–4](https://huggingface.co/learn/llm-course/en/chapter1/1) (`AutoModel`, pipelines, fine-tuning; ~6–8 h). CLIP and SONAR both load via this ecosystem.
- [ ] Paper-reading skill: Andrew Ng's advice + Keshav's three-pass method; Kilcher's walkthroughs model it (abstract → figures → method → experiments).

## Capstone

- [ ] Re-read the entire VL-JEPA paper end-to-end. You should now understand every component — anything still foggy maps back to a phase above; that's your revision list.
