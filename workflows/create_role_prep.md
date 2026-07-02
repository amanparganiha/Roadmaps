# Workflow: Create Role Prep Package

## Objective

Produce a complete, self-contained interview prep package for a target job role, stored as markdown in `roadmaps/<role-slug>/`. The package must let a student / early-career candidate prepare intensively (4–6 weeks, ~3–4 hrs/day) using **only free resources**.

## Required Inputs

- **Role name** (e.g., "Forward Deployed Engineer", "AI/ML Engineer")
- **Candidate level** (default: student / early-career — include fundamentals)
- **Timeline** (default: 4–6 weeks intensive)

## Tools

- `WebSearch` / `WebFetch` (built-in) — research role, interview loops, and resources
- `tools/check_links.py` — verify every URL in the finished docs resolves

## Steps

### 1. Research the role
Search for the role definition and skill expectations. Prioritize primary sources:
- Live job postings from companies known for the role (careers pages, LinkedIn)
- Company engineering blogs describing the role
Capture: core responsibilities, must-have skills, nice-to-haves, companies hiring, seniority expectations for entry level. Save raw notes to `.tmp/<role-slug>-research.md`.

### 2. Research the interview process
Search Glassdoor, Blind, Reddit (r/csMajors, r/leetcode, r/MachineLearning), and interview-experience blog posts for the **actual interview loop** at the top 3–5 companies for this role. Capture: stages, round types, real questions asked, evaluation criteria, timelines.

### 3. Curate free resources
For each skill area from step 1, find the best free resource. Rules:
- Free or free-tier only (audit-mode MOOCs count; "free trial requires card" does not)
- Prefer resources with strong reputations (fast.ai, NeetCode, DeepLearning.AI short courses, Hugging Face courses, Anthropic Academy, CS50, MIT OCW, roadmap.sh)
- One primary resource per topic + at most one alternative — avoid choice paralysis
- Note estimated completion time for each

### 4. Write the five docs in `roadmaps/<role-slug>/`
- `README.md` — what the role is, who hires, skills snapshot, how to use the package
- `roadmap.md` — week-by-week plan with checkbox tasks; every task links to a resource from `resources.md`; each week ends with a milestone/mini-project; total load must fit the timeline
- `interview-prep.md` — interview loop by company, question bank by round type, final-week drill schedule
- `qa-bank.md` — detailed questions **with full answers** per round type: fundamentals Q&A, coding walkthroughs with code, one worked system-design example, behavioral skeletons. Mark near-universal questions with ⭐. Answers should be interview-ready (3–8 sentences), not textbook chapters.
- `resources.md` — curated links grouped by topic, each with a one-line "why" and time estimate; include a "Free certifications" section (freeCodeCamp, Kaggle, Hugging Face, Databricks Academy, etc.)

### 5. Verify and build the UI
- Run: `python tools/check_links.py roadmaps/<role-slug>/` — fix or replace dead links until clean. Spot-check that every roadmap task's link exists in `resources.md`.
- Run: `python tools/build_ui.py` — regenerates `roadmaps/index.html` (single-file browser UI with role tabs, collapsible Q&A, persistent checkboxes). Any new role directory is picked up automatically; add its display name to `ROLE_TITLES` in the tool for a clean tab label.

## Expected Outputs

- `roadmaps/<role-slug>/` with the five docs above, all links verified
- Entry added to `roadmaps/README.md` index
- `roadmaps/index.html` rebuilt

## Edge Cases & Lessons Learned

- **Glassdoor/Blind often block automated fetches** — rely on search-result snippets and secondary writeups (blog posts, YouTube mock interviews) when direct fetch fails.
- **Course URLs churn** — always run the link checker; prefer stable landing pages over deep lecture links.
- **YouTube links**: the link checker can't detect deleted videos reliably (YouTube returns 200); prefer official channel/playlist pages.
