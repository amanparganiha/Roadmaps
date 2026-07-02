# Learning for VL-JEPA

# A Video-First Curriculum for Mastering the Concepts Behind "LiveJEPA" (VL-JEPA Real-Time Video Captioning)

## TL;DR

- **Follow a 7-phase, ~80–110 hour sequence that builds bottom-up**: foundations/embeddings → Transformers & vision encoders → JEPA core idea → contrastive learning/CLIP → text embeddings & decoding (SONAR) → clustering & the selective-decoding math → video understanding/streaming/metrics, capped by reading the VL-JEPA paper (arXiv 2512.10942) itself.
- **The three most project-critical clusters are (C) JEPA/embedding prediction, (D) contrastive learning + CLIP/InfoNCE, and (F) clustering + selective decoding** — these are the actual mechanics of how LiveJEPA predicts text embeddings and decides *when* to decode them into a caption during a live stream. Transformers/ViT (B) and video metrics like CIDEr (G) are essential supporting knowledge; SONAR/EmbeddingGemma background (E) and tooling (H) are lighter-weight.
- **Lead with the best-in-class video creators**: 3Blue1Brown (intuition for attention/embeddings), Andrej Karpathy (build-a-Transformer in code), Yannic Kilcher (JEPA/V-JEPA paper walkthroughs), StatQuest (clustering), Stanford CS224n (rigor), and the Hugging Face course (tooling) — each paired with 1–2 canonical papers/blogs.

## Key Findings

**LiveJEPA sits on top of VL-JEPA**, a vision-language model from Meta FAIR (arXiv 2512.10942, "VL-JEPA: Joint Embedding Predictive Architecture for Vision-language," ICLR 2026) that, instead of autoregressively generating caption tokens, **predicts continuous embeddings of the target text** and only invokes a lightweight text decoder "when needed." This single architectural choice is why the whole curriculum is organized around *embedding spaces* rather than token generation. The paper reports that **selective decoding reduces decoding operations by ~2.85× versus uniform decoding** while maintaining performance, and that VL-JEPA's embedding space natively supports open-vocabulary classification, text-to-video retrieval, and discriminative VQA. The model is built from a **V-JEPA video encoder**, a **predictor initialized from a Llama decoder transformer**, an **InfoNCE-style alignment loss**, and a **SONAR-style invertible text embedding space** that can be decoded back to text.

The student marked five clusters unfamiliar. Mapping them to the project:

1. **JEPA/embedding-space ideas** → the core thesis (predict in representation space, not pixels/tokens).
2. **Transformers & vision encoders** → the V-JEPA ViT encoder and the Llama-initialized predictor.
3. **Contrastive learning/InfoNCE** → the loss that aligns predicted embeddings with target text embeddings; CLIP is the canonical reference and the project uses CLIP-style evaluation.
4. **Clustering & selective-decoding math** → the novel real-time contribution: grouping/segmenting the predicted-embedding stream and triggering a decode only on meaningful change (a variance/change-point flavored idea).
5. **Video understanding/streaming + metrics (CIDEr)** → the task framing and how captions are scored.

What follows is the sequenced plan. Each phase notes **criticality** (🔴 critical / 🟡 important / 🟢 background), the **best video resource(s) with working links, channel, and duration**, **supporting reading**, and a **time budget**.

## Details

### Phase 0 — Orientation (½ day, ~3–4 h) 🔴

Read the thing you're working toward *first*, lightly, so every later concept has a hook.

- **Read (skim):** VL-JEPA paper abstract + figures — https://arxiv.org/abs/2512.10942 (PDF: https://arxiv.org/pdf/2512.10942). Authors: Delong Chen et al., Meta FAIR.
- **Blog (plain-English overview):** "VL-JEPA is a lean, fast vision-language model that rivals the giants," Ben Dickson, TechTalks — https://bdtechtalks.com/2026/01/03/meta-vl-jepa-vision-language-model/
- **Goal:** be able to state in one sentence what LiveJEPA does and why "predict the embedding, decode only when needed" matters for real-time captioning. Don't worry about understanding the mechanics yet.

### Phase 1 — Foundations: embeddings, similarity, PyTorch refresher (~10–14 h) 🔴 (embeddings) / 🟡 (PyTorch)

This is the leveling-up phase from "basics."

**1A. Embeddings & representation learning (intuition).**

- **Video (primary):** 3Blue1Brown — "But what is a GPT? Visual intro to Transformers" (Chapter 5, Neural Networks series). Channel: 3Blue1Brown. URL: https://www.youtube.com/watch?v=yMQPQuz5WpA. ~27 min. Covers what an embedding vector is and how *directions in high-dimensional space carry meaning* — exactly the mental model the whole project rests on.
- **Video (series):** 3Blue1Brown Neural Networks playlist — https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi (watch the first 1–4 chapters if you want a full refresher on what a neural net is).
- **Supporting reading:** Google ML Crash Course, "Embeddings" module — https://developers.google.com/machine-learning/crash-course/embeddings.

**1B. Cosine similarity, L2 normalization, distance metrics.**

- These are short, mechanical concepts. The CLIP write-ups make them concrete: CLIP scores image-text pairs by **cosine similarity of L2-normalized embeddings**. See the Hugging Face CLIP page — https://huggingface.co/learn/computer-vision-course/en/unit4/multimodal-models/clip-and-relatives/clip — and the OpenAI CLIP repo note that logits are "cosine similarities … times 100" (https://github.com/openai/CLIP).
- **Goal:** understand why embeddings are normalized before comparison and what "close in embedding space" means numerically.

**1C. PyTorch practical refresher.** 🟡

- **Video (primary):** Andrej Karpathy — "The spelled-out intro to neural networks and backpropagation: building micrograd" (Neural Networks: Zero to Hero, Lecture 1). Course hub: https://karpathy.ai/zero-to-hero.html. ~2h25m. Builds an autograd engine from scratch so `nn.Module`/`backward()`/`zero_grad()` stop being magic.
- **Docs (hands-on):** official PyTorch "Training with PyTorch" tutorial (Dataset/DataLoader, loss, optimizer, full training loop) — https://docs.pytorch.org/tutorials/beginner/introyt/trainingyt.html
- **Supporting:** Sebastian Raschka, "PyTorch in One Hour: From Tensors to Training Neural Networks" — https://sebastianraschka.com/teaching/pytorch-1h/

### Phase 2 — Transformers & vision encoders (~16–20 h) 🔴

The V-JEPA encoder and the Llama predictor are both Transformers, so this is non-negotiable.

**2A. The Transformer architecture (attention, self-attention, multi-head, positional encoding).**

- **Video (primary, intuition):** 3Blue1Brown — "Attention in transformers, visually explained" (Chapter 6). Channel: 3Blue1Brown. URL: https://www.youtube.com/watch?v=eMlx5fFNoYc. ~26 min. The best visual explanation of Q/K/V, the softmax attention pattern, and why causal masking sets future positions to −∞.
- **Video (primary, in code):** Andrej Karpathy — "Let's build GPT: from scratch, in code, spelled out." Channel: Andrej Karpathy. URL: https://www.youtube.com/watch?v=kCc8FmEb1nY. 1h56m. You implement self-attention, multi-head attention, positional encoding, and causal masking yourself.
- **Video (rigor/lecture):** Stanford CS224n 2023, Lecture 8 — "Self-Attention and Transformers." Channel: Stanford Online. URL: https://www.youtube.com/watch?v=LWMzyfvuehA. ~1h15m. Course page: https://web.stanford.edu/class/cs224n/. Full 2023 playlist: https://www.youtube.com/playlist?list=PLrLxpnf4DCA86z2XBgBQq2s6sKUTD5Bqm
- **Supporting reading:** Vaswani et al., "Attention Is All You Need" (the original) + Jay Alammar's "The Illustrated Transformer" (https://jalammar.github.io/illustrated-transformer/).

**2B. Causal vs. bidirectional attention masks.** 🔴

- Covered directly in both the 3Blue1Brown attention video (the −∞/softmax masking trick) and Karpathy's GPT build (the `tril` lower-triangular mask). Note for the project: V-JEPA's *encoder* is bidirectional over video patches, while the Llama-initialized *predictor/decoder* uses causal masking — understanding the difference explains the architecture.

**2C. Vision Transformers (ViT) — images/video into tokens/patches.** 🔴

- **Supporting reading (primary):** Dosovitskiy et al., "An Image is Worth 16×16 Words: Transformers for Image Recognition at Scale" — https://openreview.net/forum?id=YicbFdNTTy. This is the patch-tokenization idea V-JEPA extends to 3D "tubelets."
- **Reference:** Hugging Face Computer Vision Course, ViT unit — https://huggingface.co/learn/computer-vision-course. The Stanford CS231n slide deck "Lecture 8: Attention and Transformers" (https://cs231n.stanford.edu/slides/2024/lecture_8.pdf) is a good written companion.

**2D. The specific models: V-JEPA / V-JEPA 2 and Llama background.** 🔴

- **Video (primary):** Yannic Kilcher — "V-JEPA: Revisiting Feature Prediction for Learning Visual Representations from Video (Explained)." Channel: Yannic Kilcher. URL: https://www.youtube.com/watch?v=7UkJPwz_N_0. ~50 min. Walks through the ViT encoder, the predictor, masking, and *why feature-space prediction beats pixel prediction* — this video doubles as the bridge into Phase 3.
- **Supporting reading:** V-JEPA 2 paper, Assran/Bardes et al., Meta — https://ai.meta.com/research/publications/v-jepa-2-self-supervised-video-models-enable-understanding-prediction-and-planning/ (arXiv 2506.09985). Key facts to retain: it is a **1.2-billion-parameter model with a ViT-g encoder (>1B params) pretrained on >1M hours of video + 1M images from the VideoMix22M dataset**; per arXiv 2506.09985 it reaches **"77.3 top-1 accuracy on Something-Something v2"** (motion understanding) and **"39.7 recall-at-5 on Epic-Kitchens-100"** (action anticipation). Its training objective is mask-denoising in representation space with an L1 loss using a stop-gradient and an EMA (exponential moving average) target encoder to prevent collapse. Hands-on guide: https://learnopencv.com/v-jepa-2-meta-world-model-robotics-guide/.
- **Llama background (light):** the predictor in VL-JEPA is initialized from a Llama decoder transformer; SONAR's own encoder is built on Llama-3.2-1B. A short read of the Llama model card / Karpathy's GPT video already covers the decoder-transformer mechanics you need.

### Phase 3 — JEPA: Joint Embedding Predictive Architecture (the core idea) (~12–16 h) 🔴 MOST CRITICAL

This is the conceptual heart of the project.

**3A. LeCun's vision of world models and JEPA.**

- **Video (primary):** Yannic Kilcher — "JEPA: A Path Towards Autonomous Machine Intelligence (Paper Explained)." Channel: Yannic Kilcher. ~59 min. (Search the Yannic Kilcher channel for this title; paper at https://openreview.net/forum?id=BZ5a1r-kVsf.) Chapters cover energy-based models, latent variables, the collapse problem, contrastive vs. regularized methods, and the JEPA/H-JEPA architecture.
- **Supporting reading:** Yann LeCun, "A Path Towards Autonomous Machine Intelligence" (2022), OpenReview. Plus the excellent deep-dive blog by Rohit Bandaru — https://rohitbandaru.github.io/blog/JEPA-Deep-Dive/ (covers JEPA, I-JEPA, V-JEPA in one place).

**3B. I-JEPA (image) and V-JEPA (video): predicting in representation space.** 🔴

- Re-use the Yannic Kilcher V-JEPA video from 2D (https://www.youtube.com/watch?v=7UkJPwz_N_0) — it explicitly contrasts feature-space prediction with pixel/token reconstruction and explains why autoencoder-style pixel losses produce blurry averages.
- **Supporting reading:** I-JEPA (Assran et al., 2023) and V-JEPA (Bardes et al., 2024) papers; codebase at https://github.com/facebookresearch/jepa.

**3C. Why embedding prediction beats token generation (the central thesis).** 🔴

- This *is* the VL-JEPA contribution: "By learning in an abstract representation space, the model focuses on task-relevant semantics while abstracting away surface-level linguistic variability" (arXiv 2512.10942). Read §1–2 of the VL-JEPA paper now that you have the JEPA background; the Anshul Bakode Medium explainer ("Thinks in Embeddings, Not Words," https://medium.com/@anshulbakode/vl-jepa-the-vision-language-model-that-thinks-in-embeddings-not-words-ab642801cb01) is a gentle companion.

**3D. Self-supervised learning overview + representation collapse + anti-collapse regularization (VICReg).** 🔴

- **Supporting reading (primary):** VICReg paper, Bardes, Ponce & LeCun — https://arxiv.org/abs/2105.04906. The three terms (variance, invariance, covariance) and *why pulling-only objectives collapse to constant vectors* are essential for understanding any JEPA loss. The AssemblyAI review (https://www.assemblyai.com/blog/review-vicreg-variance-invariance-covariance-regularization-for-self-supervised-learning) explains it in plain language.
- **Note on the project:** VL-JEPA uses an InfoNCE alignment loss (contrastive anti-collapse), and the paper itself flags VICReg/SIGReg as alternatives it did not fully evaluate — so know both families.

### Phase 4 — Contrastive learning, InfoNCE & CLIP (~12–16 h) 🔴

The loss that aligns VL-JEPA's predicted embeddings with target text embeddings, and the evaluation paradigm.

**4A. Contrastive learning intuition (positive/negative pairs).**

- **Video (primary):** Yannic Kilcher's SimCLR explainer ("A Simple Framework for Contrastive Learning of Visual Representations") on the Yannic Kilcher channel — establishes positives (augmented views) vs. negatives and why we push apart. (Search the channel; companion paper: SimCLR, Chen et al., 2020.)
- **Supporting reading:** the SimCLR paper, plus the "Contrastive Learning for Beginners: InfoNCE Loss Explained" Medium piece — https://medium.com/@mlshark/infonce-explained-in-details-and-implementations-902f28199ce6

**4B. InfoNCE loss specifically (the math).** 🔴

- **Supporting reading (primary):** van den Oord et al., "Representation Learning with Contrastive Predictive Coding" (the paper that introduced InfoNCE). The key formula — `L = −log[ exp(sim(q,k⁺)/τ) / Σ exp(sim(q,k)/τ) ]` — and the fact that minimizing it maximizes a lower bound on mutual information are well summarized at https://www.emergentmind.com/topics/infonce.
- **Goal:** be able to read VL-JEPA's loss section and recognize the InfoNCE structure (temperature τ, one positive, many negatives, cosine similarity in the exponent).

**4C. CLIP — vision/text alignment in a shared embedding space.** 🔴 (foundational for the project's CLIP-style evaluation)

- **Video (primary):** Aleksa Gordić (The AI Epiphany) — "OpenAI CLIP – Connecting Text and Images | Paper Explained." Channel: The AI Epiphany. URL: https://www.youtube.com/watch?v=fQyHEXZB-nM.
- **Supporting reading:** OpenAI's CLIP page (https://openai.com/index/clip/) and the original Radford et al. CLIP paper. Note the dual-encoder design, symmetric InfoNCE loss, and the 400M image-text pairs (WebImageText). VL-JEPA is benchmarked against CLIP, SigLIP2, and Perception Encoder on 8 classification + 8 retrieval datasets.

**4D. SimCLR / broader contrastive SSL family + alignment & uniformity.** 🟡

- **Supporting reading:** Wang & Isola, "Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere" (2020) — decomposes contrastive loss into *alignment* (positives close) and *uniformity* (features spread on the sphere). This deepens intuition for why L2-normalization and the hypersphere matter.

### Phase 5 — Text embeddings & decoding back to text (~6–9 h) 🟡 (SONAR is project-relevant; EmbeddingGemma is background)

VL-JEPA predicts a text embedding and then *inverts* it to text — so you need the encoder↔decoder embedding idea.

**5A. Sentence embeddings / Sentence-BERT.**

- **Supporting reading (primary):** "An Intuitive Explanation of Sentence-BERT," Towards Data Science — https://towardsdatascience.com/an-intuitive-explanation-of-sentence-bert-1984d144a868/. Plus the SBERT docs/quickstart at https://sbert.net/ (siamese networks, mean pooling, cosine similarity).
- **Reference:** Reimers & Gurevych, "Sentence-BERT" (2019), arXiv 1908.10084.

**5B. SONAR — invertible multilingual sentence embedding space (encoder AND decoder).** 🔴 (directly used by the project's decoding step)

- **Supporting reading (primary):** SONAR paper, Duquenne, Schwenk & Sagot — https://arxiv.org/abs/2308.11466 — and the GitHub README (https://github.com/facebookresearch/SONAR). SONAR is "a single common 1024-dimensional embedding space" covering 200 languages, whose text encoder is initialized with NLLB and decoded via a matching NLLB-initialized text decoder (the `TextToEmbeddingModelPipeline` / `EmbeddingToTextModelPipeline`). Concretely: the encoder yields a fixed-length vector e ∈ ℝ¹⁰²⁴, mean-pooled along the sequence dimension and trained with an MSE alignment loss; the decoder then inverts that single bottleneck vector back to text (via beam search). This encoder/decoder symmetry is exactly the "decode an embedding to a caption" capability LiveJEPA needs.
- **Companion:** Bryan Teo, "SONAR Explained" — https://medium.com/@bteo/sonar-explained-a9c99f1376e8.

**5C. The general idea of embedding-to-text inversion (seq2seq decoders).** 🟡

- Covered by the SONAR decoder above; conceptually it's a seq2seq generator that attends to a single bottleneck vector instead of a variable-length encoder output.

**5D. EmbeddingGemma background.** 🟢

- **Reference:** Google's EmbeddingGemma model card/blog (a compact open text-embedding model). Light reading — know it exists as an alternative text-embedding backbone.

### Phase 6 — Clustering & the selective-decoding math (the novel contribution) (~12–16 h) 🔴 MOST CRITICAL (this is the project's original research)

This is where LiveJEPA decides *when* to emit a caption in a live stream.

**6A. Hierarchical / agglomerative clustering.**

- **Video (primary):** StatQuest with Josh Starmer — "Hierarchical Clustering." URL: https://www.youtube.com/watch?v=7xHsRkOdVwo. ~11 min. Dendrograms, linkage, distance metrics, intuitively.
- **Video (companion):** StatQuest — "K-means clustering." URL: https://www.youtube.com/watch?v=4b5d3muPQmA. ~9 min (useful contrast: partitioning vs. hierarchy).
- **Supporting reading:** scikit-learn clustering user guide — https://scikit-learn.org/stable/modules/clustering.html.

**6B. Ward linkage and variance minimization.** 🔴

- **Supporting reading (primary):** Penn State STAT 505 §14.7 "Ward's Method" (https://online.stat.psu.edu/stat505/lesson/14/14.7) and the Ward's-linkage walkthrough at https://jbhender.github.io/Stats506/F18/GP/Group10.html, which gives the merge-cost formula: Δ(A,B) = Σ‖xᵢ − m_{A∪B}‖² − Σ‖xᵢ − m_A‖² − Σ‖xᵢ − m_B‖² = (n_A n_B)/(n_A+n_B)·‖m_A − m_B‖². Ward merges the pair that increases within-cluster sum-of-squares (variance) the least — directly relevant to "group consecutive predicted embeddings by minimizing variance."

**6C. Temporal / connectivity-constrained clustering.** 🔴

- **Supporting reading (primary):** scikit-learn `AgglomerativeClustering` with a `connectivity` matrix — https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html and the "Agglomerative clustering with and without structure" example (https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_clustering.html). A *temporal connectivity constraint* (only allow merging of adjacent-in-time frames) is exactly how you cluster a streaming embedding sequence into coherent segments.

**6D. Change-point detection in time series (the variance-threshold trigger).** 🔴

- **Supporting reading (primary):** Fraunhofer IESE, "Change Point Detection in Time Series Analysis" — https://www.iese.fraunhofer.de/blog/change-point-detection/ (change in mean/variance/distribution). For online/streaming detection, see the Tech Rando intro (https://techrando.com/2019/08/14/a-brief-introduction-to-change-point-detection-using-python/), which distinguishes offline vs. online CPD — LiveJEPA's "decode only when a new event occurs" is online change-point detection on the predicted-embedding stream.
- **Python tool:** the `ruptures` library for change-point detection.

**6E. Moving averages / signal smoothing.** 🟡

- Short concept: a rolling mean over the embedding-distance signal reduces noise before thresholding. Any intro signal-processing reference (e.g., pandas `.rolling().mean()` docs) suffices.

**6F. scikit-learn AgglomerativeClustering practical usage.** 🔴

- **Supporting reading:** the scikit-learn generated docs in 6C, plus the practical Ward + `AgglomerativeClustering` code in the jbhender walkthrough above.
- **How it ties together (the selective-decoding mechanism):** VL-JEPA produces "continuous streams of target semantic embeddings within sliding windows … selectively decoded by a lightweight y-decoder," emitting "a description only when a new event occurs," cutting decode operations ~2.85× vs. uniform decoding (arXiv 2512.10942). LiveJEPA operationalizes this with clustering/change-detection on the embedding stream: smooth the inter-embedding distance signal, detect a variance/change-point spike (a "new event"), and trigger one decode per detected segment. *(Caveat: the paper's §4.5 states the 2.85× result and the event-triggered framing, but the exact thresholding/clustering formula could not be verified from the abstract/intro alone — confirm the precise rule in §4.5 of https://arxiv.org/pdf/2512.10942.)*

### Phase 7 — Video understanding, streaming & evaluation (~10–14 h) 🔴 (metrics + streaming) / 🟡 (VQA, retrieval)

**7A. Video captioning / dense video captioning overview.** 🟡

- **Supporting reading:** survey "Video Captioning: a comparative review" — https://arxiv.org/pdf/2204.05976 (covers the task and the BLEU/METEOR/ROUGE-L/CIDEr metric suite).

**7B. Streaming / online video understanding (VideoLLM-online).** 🔴

- **Supporting reading (primary):** Chen et al., "VideoLLM-online: Online Video Large Language Model for Streaming Video" (CVPR 2024) — https://arxiv.org/abs/2406.11816. Key ideas: the LIVE (Learning-In-Video-strEam) framework, a **Streaming EOS (end-of-sequence) prediction** mechanism to decide *when to respond*, built on Llama-2/Llama-3, and reported throughput of **"5-10 FPS on RTX 3090 GPU, 10-15 FPS on an A100 GPU"** for a 5-minute clip — described as "the first streaming video LLM." This is the closest published analog to LiveJEPA's "when do I emit a caption" problem; its EOS-trigger contrasts with VL-JEPA's embedding-change trigger.

**7C. Visual Question Answering (VQA) basics.** 🟢

- **Reference:** VL-JEPA is evaluated on GQA, TallyQA, POPE, POPEv2; a short read of the GQA or VQA-v2 dataset pages gives enough grounding.

**7D. Text-to-video retrieval basics + Recall@1.** 🟡

- **Reference:** retrieval ranks candidate videos by embedding similarity to a text query; Recall@K = fraction of queries whose correct item appears in the top-K. VL-JEPA reports retrieval on 8 datasets vs. CLIP/SigLIP2.

**7E. CIDEr (and BLEU, METEOR, ROUGE-L, SPICE).** 🔴

- **Supporting reading (primary):** Vedantam, Zitnick & Parikh, "CIDEr: Consensus-based Image Description Evaluation" (2015). What to retain: **CIDEr computes the average cosine similarity between TF-IDF-weighted n-grams of the candidate and the reference captions** — TF-IDF down-weights common n-grams and rewards distinctive, consensus content; CIDEr scores typically range 0–5 (or ×100). BLEU = n-gram precision with brevity penalty; METEOR = unigram precision/recall with synonyms/stemming; ROUGE-L = longest-common-subsequence recall; SPICE = scene-graph semantic matching. A clear written comparison is at https://www.labellerr.com/blog/image-captioning-evaluation-and-fine-tuning/.

### Phase 8 — Practical tooling (interleave throughout, ~5–7 h) 🟡

**8A. Hugging Face Transformers (loading models, AutoModel).**

- **Video (primary):** the official HuggingFace channel course-intro video, "Welcome to the Hugging Face Course" — https://www.youtube.com/watch?v=00GKzGyWFEs (~3 min), plus the per-task pipeline videos on that channel.
- **Course (primary):** the free Hugging Face LLM/NLP course — https://huggingface.co/learn/llm-course/en/chapter1/1 (Chapters 1–4 cover `AutoModel`, pipelines, fine-tuning; ~6–8 h). The CLIP and SONAR models are both loadable via this ecosystem.

**8B. Reading research papers effectively.**

- **Supporting reading:** Andrew Ng's widely-circulated "How to Read Research Papers" advice and the "three-pass" method (Keshav). For ML specifically, Yannic Kilcher's paper-walkthrough videos (used throughout this plan) model the skill: read abstract → figures → method → experiments.

## Recommendations

**Staged plan and what changes it:**

1. **Weeks 1–2 — Foundations + Transformers (Phases 0–2).** Do Phase 0 on day 1. If the 3Blue1Brown attention video and Karpathy's "Let's build GPT" feel comfortable and you can explain Q/K/V and causal masking in your own words, *skip the CS224n lecture* and move on. **Benchmark to advance:** you can sketch the V-JEPA encoder/predictor data flow.
2. **Weeks 3–4 — JEPA + Contrastive/CLIP (Phases 3–4).** These are the highest-leverage clusters. Watch the two Yannic Kilcher videos back-to-back, then read VICReg and the InfoNCE formula. **Benchmark:** you can explain *why predicting an embedding avoids the blurry-average problem of pixel/token losses*, and you can read VL-JEPA's loss equation and identify it as InfoNCE.
3. **Week 5 — Text embeddings + Clustering/selective decoding (Phases 5–6).** This is the project's novel core. After StatQuest + Ward + change-point reading, **re-read VL-JEPA §4.5 (selective decoding)** and try to reproduce the trigger logic in a notebook with `scikit-learn` `AgglomerativeClustering` (temporal connectivity) and `ruptures`. **Benchmark:** you can implement a toy "decode-on-change" loop over a synthetic embedding stream.
4. **Week 6 — Video/streaming + metrics + tooling (Phases 7–8).** Read VideoLLM-online and the CIDEr paper; wire up Hugging Face to load CLIP and SONAR. **Benchmark:** you can compute CIDEr on a toy caption set and explain Recall@1.
5. **Capstone:** re-read the entire VL-JEPA paper end-to-end. You should now understand every component.

**If time is short**, compress to the 🔴 items only: Phases 0, 2A/2C/2D, 3 (all), 4A–4C, 6 (all), 7B/7E — that's the irreducible path to understanding LiveJEPA (~45–55 h).

**Triage principle:** prioritize *embedding-space prediction (Phase 3)* and *selective decoding (Phase 6)* above everything else — they are what make this project novel. Treat SONAR/EmbeddingGemma (5B/5D), VQA (7C), and the broader SSL family (4D) as background you can read on demand.

## Caveats

- **Exact runtimes/URLs:** Most video URLs and durations were verified; a few are approximate. Specifically, the Yannic Kilcher "JEPA – A Path Towards Autonomous Machine Intelligence" video (~59 min) and the Aleksa Gordić CLIP video URL were confirmed by title/channel but the precise watch-ID or duration should be double-checked on YouTube. StatQuest durations (~9–11 min) are typical-length estimates.
- **No verified current CS231n transformer lecture on YouTube:** Stanford's *publicly posted* CS231n lecture videos are older; the 2024/2025 "Attention and Transformers" lecture is available as slides (https://cs231n.stanford.edu/slides/2024/lecture_8.pdf) but not as a confirmed public video. CS224n 2023 Lecture 8 is the reliable video substitute for rigorous attention/Transformer coverage.
- **Selective-decoding mechanism:** The VL-JEPA paper confirms selective decoding is *adaptive/event-triggered* and yields ~2.85× fewer decode operations, but the precise trigger rule (whether an explicit variance threshold, change-point statistic, or clustering criterion) should be confirmed directly in §4.5 of the PDF rather than taken from secondary summaries. The "clustering + change-point" framing in Phase 6 is the correct *family* of techniques and matches the paper's "decode only when a new event occurs" language, but treat the exact algorithm as something to verify against the source.
- **"LiveJEPA" naming:** This appears to be the student's project name layered on top of VL-JEPA (arXiv 2512.10942). The curriculum targets the published VL-JEPA mechanics plus the streaming/clustering techniques the project name implies; if the project diverges from the paper, adjust Phase 6/7 emphasis accordingly.
- **Some secondary sources are blogs/Medium:** intuition-building blogs (Medium, Towards Data Science) are flagged as companions, not authorities — always cross-check claims against the primary papers cited alongside them.