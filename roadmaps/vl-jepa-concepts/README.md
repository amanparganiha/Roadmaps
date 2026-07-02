# VL-JEPA Concepts (Thesis Track)

The learning curriculum behind **LiveJEPA** — the M.Tech thesis project: real-time video captioning built on VL-JEPA.

> Source: this track is the formatted version of `LearningForVL-JEPA.md` (project root). That file remains the original; edit *here* going forward so the UI stays current (`python tools/build_ui.py` after edits).

## What the project is

**LiveJEPA sits on top of VL-JEPA** (Meta FAIR, [arXiv 2512.10942](https://arxiv.org/abs/2512.10942), ICLR 2026): instead of autoregressively generating caption tokens, VL-JEPA **predicts continuous embeddings of the target text** and only invokes a lightweight text decoder "when needed." Selective decoding cuts decode operations ~2.85× vs uniform decoding while maintaining performance. The architecture: a **V-JEPA video encoder** + a **predictor initialized from a Llama decoder** + an **InfoNCE-style alignment loss** + a **SONAR-style invertible text embedding space**.

LiveJEPA's original contribution lives in the *when-to-decode* decision: clustering / change-point detection over the predicted-embedding stream, emitting a caption only when a new event occurs.

## The 7-phase curriculum (~80–110 h total)

| Phase | Topic | Criticality |
|---|---|---|
| 0 | Orientation: skim the VL-JEPA paper | 🔴 |
| 1 | Embeddings, similarity, PyTorch refresher | 🔴/🟡 |
| 2 | Transformers & vision encoders (ViT, V-JEPA, Llama) | 🔴 |
| 3 | **JEPA: predicting in representation space** | 🔴 most critical |
| 4 | Contrastive learning, InfoNCE, CLIP | 🔴 |
| 5 | Text embeddings & decoding (SBERT, SONAR) | 🟡 (SONAR 🔴) |
| 6 | **Clustering & selective decoding (the novel contribution)** | 🔴 most critical |
| 7 | Video understanding, streaming, metrics (CIDEr) | 🔴/🟡 |
| 8 | Tooling (Hugging Face) — interleave throughout | 🟡 |

**Triage principle:** Phases 3 and 6 above everything — they are what makes the project novel. If time is short, the irreducible 🔴-only path is ~45–55 h: Phases 0, 2A/2C/2D, 3 (all), 4A–4C, 6 (all), 7B/7E.

## How this track relates to the others

- **[CV roadmap](../computer-vision-engineer/roadmap.md)**: run both in parallel — CV weeks 1–3 build the general foundation (CNNs, detection); this track goes deep where the thesis lives (transformers, SSL, JEPA). CV week 4 (ViT/CLIP) overlaps Phase 2/4 here — do those the same week and each makes the other easier.
- **[CV qa-bank Q21](../computer-vision-engineer/qa-bank.md)**: the interview-ready summary of JEPA vs MAE vs contrastive — your thesis depth-round script.
- **The explain-it-back rule**: this project is being built with Claude Code's help. For every component the AI writes, explain it back in your own words in a running `notes.md`. Whatever you can't explain is the next thing to study from this curriculum. The thesis defense tests you, not the code.

## Caveats (from the original research notes)

- Most video URLs verified; a few (Yannic Kilcher's JEPA video ID, Aleksa Gordić CLIP video, StatQuest durations) should be double-checked on YouTube by title/channel.
- No verified public CS231n transformer lecture video — CS224n 2023 Lecture 8 is the reliable substitute; CS231n 2024 slides linked as written companion.
- **Selective-decoding mechanism**: the paper confirms adaptive/event-triggered decoding (~2.85× fewer decodes), but verify the *exact* trigger rule in §4.5 of the PDF — the clustering/change-point framing in Phase 6 is the right technique family, not a confirmed reproduction of the paper's rule.
- Blog/Medium companions are intuition aids, not authorities — cross-check against the primary papers cited alongside them.
