# AI/ML Engineer Free Resources

Everything the [roadmap](roadmap.md) links to, plus alternatives. All free (audit/free tier at most). One primary per topic — finish, don't collect.

## Python & data wrangling
- **[CS50P — Harvard Python](https://cs50.harvard.edu/python/)** — if fundamentals are shaky. *(selective, ~15 hrs)*
- **[Kaggle Learn](https://www.kaggle.com/learn)** — Pandas, Data Viz, Intro/Intermediate ML micro-courses; in-browser, free certificates. *(~12 hrs total)*

## Math intuition
- **[3Blue1Brown — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)** — vectors to eigenvalues, visually; all you need to *understand* what models do. *(~4 hrs)*
- **[StatQuest (YouTube)](https://www.youtube.com/@statquest)** — stats + ML concepts explained simply; the bias/variance and regularization videos are interview gold. *(~6 hrs selectively)*
- Alt: [Khan Academy — Statistics](https://www.khanacademy.org/math/statistics-probability) for structured stats practice.

## Classic ML
- **[Andrew Ng — ML Specialization](https://www.coursera.org/specializations/machine-learning-introduction)** — the canonical course; audit each course free (click "Audit" at enrollment). Course 1 + half of Course 2 covers the interview core. *(~25 hrs)*
- **[Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)** — faster alternative (~15 hrs), well-produced, good production framing.
- **[scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)** — reference while doing Kaggle work.
- Deeper theory (optional): [Stanford CS229 lectures (YouTube)](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU) + [Shervine's CS229 cheatsheets](https://stanford.edu/~shervine/teaching/cs-229/).
- **Your video track: Krish Naik's Udemy DSAI bootcamp** (purchased) + his [YouTube channel](https://www.youtube.com/@krishnaik06) for anything the course skips. Use it as the *lecture* layer and map each course section to this roadmap's milestone projects (course EDA/ML sections → week 1–2 Kaggle milestones; DL/NLP sections → week 3–4 PyTorch and RAG projects). Passive watching without the projects is the #1 way this prep fails.

## Deep learning
- **[Karpathy — Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)** — backprop → GPT, built from scratch in code. The best "explain how it actually works" prep in existence. *(~16 hrs for lectures 1–4 + GPT)*
- **[PyTorch — Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html)** — official tutorial track. *(~5 hrs)*
- **[fast.ai — Practical Deep Learning for Coders](https://course.fast.ai/)** — top-down complement: ship a model in lesson 1. *(lesson 1–2, ~4 hrs; whole course if you have time after week 6)*

## Transformers & LLMs
- **[Hugging Face LLM Course](https://huggingface.co/learn/llm-course)** — tokenizers, pretrained models, fine-tuning with Trainer. *(~8 hrs for ch. 1–3)*
- **[Anthropic courses (GitHub)](https://github.com/anthropics/courses)** — free notebooks: API, prompting, tool use, evals. *(~6 hrs)*
- **[DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses/)** — free ~1.5 hr courses on fine-tuning, RAG, agents, evals; pick by gap. *(~3 hrs)*
- Alt: [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) if targeting agent-heavy roles.

## Evals
- **[Hamel Husain — Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/)** — the canonical practitioner essay. *(~1 hr)*

## Production ML / MLOps
- **[Made With ML](https://madewithml.com/)** — free end-to-end production ML course (design → data → modeling → deployment → testing → monitoring). *(~10 hrs selectively)*
- **[Docker — Get Started](https://docs.docker.com/get-started/)** — enough Docker to containerize a model server. *(~3 hrs)*
- **[FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)** — the de-facto model-serving framework. *(~4 hrs)*
- **[Google — Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml)** — 43 rules of production ML; quotable in interviews. *(~1 hr)*

## ML system design & interviews
- **[Chip Huyen — ML Systems Design booklet](https://huyenchip.com/machine-learning-systems-design/toc.html)** — free; the framework used in [interview-prep.md](interview-prep.md). *(~4 hrs)*
- **[Chip Huyen — Intro to ML Interviews Book](https://huyenchip.com/ml-interviews-book/)** — free online; landscape, timelines, what companies test. *(~3 hrs selectively)*
- **[Evidently AI — ML system design database](https://www.evidentlyai.com/ml-system-design)** — 300+ real case studies searchable by industry. *(~3 hrs for 5 cases)*

## Practice platforms
- **[Deep-ML](https://www.deep-ml.com/)** — LeetCode-style implement-ML-from-scratch problems; mirrors the ML coding round. *(1/day habit)*
- **[NeetCode Roadmap](https://neetcode.io/roadmap)** — for the general-coding screen; first 2–3 patterns suffice for most MLE loops. *(~10 hrs)*
- **[Kaggle Competitions](https://www.kaggle.com/competitions)** — Getting Started tier for portfolio pieces.
- **[Pramp](https://www.pramp.com/)** — free peer-to-peer mock interviews.
- **[SQLBolt](https://sqlbolt.com/)** + **[SQL Practice](https://www.sql-practice.com/)** — SQL screens are common for MLE.

## Free certifications (résumé line items)

Certificates don't replace the portfolio, but they pass résumé filters and prove initiative. All genuinely free:

- **[freeCodeCamp — Machine Learning with Python](https://www.freecodecamp.org/learn)** — the most substantial fully-free ML certification (TensorFlow-based projects graded in-browser); also Data Analysis with Python.
- **[Kaggle Learn certificates](https://www.kaggle.com/learn)** — Pandas, Intro/Intermediate ML, Feature Engineering micro-certs; earn them naturally during weeks 1–2 of the roadmap.
- **[Hugging Face Agents Course certificate](https://huggingface.co/learn/agents-course)** — pass the GAIA final challenge; strong signal for GenAI-flavored MLE roles.
- **[Databricks Academy — free self-paced trainings](https://www.databricks.com/learn/training/home)** — free Generative AI Fundamentals accreditation; recognized in data-engineering-adjacent MLE roles.
- **[Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)** — no formal cert, but completion + the follow-on [Google Cloud Skills Boost free GenAI badges](https://www.cloudskillsboost.google/) cover the "Google stack" line.
- **[Elements of AI](https://www.elementsofai.com/)** — free University of Helsinki certificate; non-technical but a fine first badge.
- **[Microsoft Learn — AI training paths](https://learn.microsoft.com/en-us/training/)** — free modules/badges toward Azure AI & Data Science fundamentals (training free; proctored exam paid — the free training alone is résumé-relevant).

Priority for MLE: freeCodeCamp ML with Python → Kaggle certs → HF Agents cert. Then stop collecting and build portfolio pieces — interviewers ask about projects, not badges.

## Project fuel
- **[Kaggle Datasets](https://www.kaggle.com/datasets)** — datasets for every milestone.
- **[Excalidraw](https://excalidraw.com/)** — whiteboard for system-design practice.
