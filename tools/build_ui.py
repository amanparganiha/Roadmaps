"""Build a single-file HTML UI from the markdown docs in roadmaps/.

Usage:
    python tools/build_ui.py

Reads every roadmaps/<role>/ directory (docs in DOC_ORDER), embeds the
markdown plus an inlined copy of marked.js into roadmaps/index.html.
The result is fully offline: open it by double-clicking. Checkbox progress
persists in the browser's localStorage.
"""

import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROADMAPS = ROOT / "roadmaps"
OUT = ROADMAPS / "index.html"
MARKED_CACHE = ROOT / ".tmp" / "marked.min.js"
MARKED_URL = "https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"

DOC_ORDER = [
    ("README.md", "Overview"),
    ("roadmap.md", "Roadmap"),
    ("interview-prep.md", "Interview Prep"),
    ("qa-bank.md", "Q&A Bank"),
    ("resources.md", "Resources"),
]

ROLE_TITLES = {
    "fde": "Forward Deployed Engineer",
    "ai-ml-engineer": "AI/ML Engineer",
    "computer-vision-engineer": "Computer Vision Engineer",
    "remote-ai-career": "Remote AI Career",
    "vl-jepa-concepts": "VL-JEPA (Thesis)",
}

TASK_RE = re.compile(r"^\s*[-*] \[[ xX]\] ", re.MULTILINE)


def get_marked_js() -> str:
    if MARKED_CACHE.exists():
        return MARKED_CACHE.read_text(encoding="utf-8")
    print(f"Downloading marked.js from {MARKED_URL} ...")
    with urllib.request.urlopen(MARKED_URL, timeout=30) as resp:
        js = resp.read().decode("utf-8")
    MARKED_CACHE.parent.mkdir(exist_ok=True)
    MARKED_CACHE.write_text(js, encoding="utf-8")
    return js


def collect_roles() -> list[dict]:
    roles = []
    for role_dir in sorted(p for p in ROADMAPS.iterdir() if p.is_dir()):
        docs = []
        for filename, title in DOC_ORDER:
            f = role_dir / filename
            if not f.exists():
                continue
            md = f.read_text(encoding="utf-8")
            docs.append({
                "id": filename[:-3],
                "file": filename,
                "title": title,
                "md": md,
                "tasks": len(TASK_RE.findall(md)),
            })
        if docs:
            roles.append({
                "slug": role_dir.name,
                "name": ROLE_TITLES.get(role_dir.name, role_dir.name.replace("-", " ").title()),
                "docs": docs,
            })
    return roles


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Role Prep Roadmaps</title>
<style>
:root {
  --bg: #eef1f6; --panel: #ffffff; --text: #1e2733; --muted: #5d6b7c;
  --accent: #2563eb; --accent-strong: #1d4ed8; --accent-soft: #e9f0fe;
  --border: #e2e8f0; --done: #15803d; --done-soft: #ecf9f1;
  --code-bg: #f5f7fa; --row: #f8fafc;
  --shadow: 0 1px 2px rgba(15,23,42,.05), 0 10px 30px rgba(15,23,42,.06);
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #0b0f15; --panel: #131922; --text: #e9eef5; --muted: #9aa8ba;
    --accent: #6ea3ff; --accent-strong: #8ab4ff; --accent-soft: #1a2436;
    --border: #283242; --done: #4ade80; --done-soft: #13291d;
    --code-bg: #1a2230; --row: #171f2b; --shadow: none;
  }
}
:root[data-theme="dark"] {
  --bg: #0b0f15; --panel: #131922; --text: #e9eef5; --muted: #9aa8ba;
  --accent: #6ea3ff; --accent-strong: #8ab4ff; --accent-soft: #1a2436;
  --border: #283242; --done: #4ade80; --done-soft: #13291d;
  --code-bg: #1a2230; --row: #171f2b; --shadow: none;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--text);
  font-family: "Segoe UI Variable Text", "Segoe UI", -apple-system, BlinkMacSystemFont,
    Roboto, "Helvetica Neue", Arial, sans-serif;
  -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; }
header { position: sticky; top: 0; z-index: 10; background: var(--panel);
  border-bottom: 1px solid var(--border); padding: 0 24px; box-shadow: var(--shadow); }
.header-row { display: flex; align-items: center; gap: 14px; max-width: 1280px;
  margin: 0 auto; flex-wrap: wrap; padding: 10px 0; }
h1.site { font-size: 16px; margin: 0; white-space: nowrap; letter-spacing: .2px; }
.tabs { display: flex; gap: 8px; flex-wrap: wrap; }
.tab { border: 1px solid var(--border); background: transparent; color: var(--muted);
  padding: 8px 16px; border-radius: 999px; cursor: pointer; font-size: 13.5px;
  font-weight: 600; transition: color .15s, border-color .15s, background .15s; }
.tab:hover { color: var(--accent); border-color: var(--accent); }
.tab.active { background: var(--accent); border-color: var(--accent); color: #fff; }
.font-controls { display: flex; gap: 5px; }
.font-controls button { border: 1px solid var(--border); background: transparent;
  color: var(--muted); width: 32px; height: 32px; border-radius: 8px; cursor: pointer;
  font-size: 13px; font-weight: 700; line-height: 1; }
.font-controls button:hover { color: var(--accent); border-color: var(--accent); }
.progress-wrap { margin-left: auto; min-width: 190px; }
.progress-label { font-size: 12px; color: var(--muted); margin-bottom: 4px; }
.progress-bar { height: 8px; background: var(--border); border-radius: 4px; overflow: hidden; }
.progress-fill { height: 100%; background: var(--done); width: 0; transition: width .3s; }
.layout { display: flex; max-width: 1280px; margin: 0 auto; gap: 28px; padding: 28px 24px 64px; }
nav.side { width: 242px; flex-shrink: 0; position: sticky; top: 74px;
  align-self: flex-start; max-height: calc(100vh - 96px); overflow-y: auto; }
.doc-btn { display: block; width: 100%; text-align: left; margin: 3px 0; padding: 9px 14px;
  border: none; background: transparent; color: var(--muted); border-radius: 10px;
  cursor: pointer; font-size: 14px; font-weight: 500; }
.doc-btn:hover { background: var(--accent-soft); color: var(--accent-strong); }
.doc-btn.active { background: var(--accent-soft); color: var(--accent-strong); font-weight: 700; }
.toc { margin: 14px 0 0 6px; padding-left: 12px; border-left: 2px solid var(--border); }
.toc a { display: block; font-size: 12.5px; color: var(--muted); text-decoration: none;
  padding: 4px 8px; border-radius: 6px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.toc a:hover { color: var(--accent); background: var(--accent-soft); }
main { flex: 1; min-width: 0; background: var(--panel); border: 1px solid var(--border);
  border-radius: 16px; padding: 44px 56px 60px; box-shadow: var(--shadow);
  font-size: var(--content-size, 17px); line-height: 1.8; }
main > * { max-width: 76ch; }
main h1 { font-size: 1.75em; line-height: 1.3; margin: 0 0 .7em; padding-bottom: .45em;
  border-bottom: 2px solid var(--border); letter-spacing: -.015em; }
main h2 { font-size: 1.35em; line-height: 1.4; margin: 2.1em 0 .8em; padding-left: .55em;
  border-left: 4px solid var(--accent); letter-spacing: -.01em; }
main h3 { font-size: 1.13em; line-height: 1.45; margin: 1.7em 0 .55em; }
main p { margin: .9em 0; }
main ul, main ol { padding-left: 1.4em; margin: .8em 0; }
main li { margin: .45em 0; }
main li > ul, main li > ol { margin: .3em 0; }
main a { color: var(--accent); text-decoration: none; border-bottom: 1px solid transparent;
  transition: border-color .15s; }
main a:hover { border-bottom-color: var(--accent); }
main strong { font-weight: 650; }
main hr { border: none; border-top: 1px solid var(--border); margin: 2.4em 0; }
main code { background: var(--code-bg); border: 1px solid var(--border);
  padding: .12em .38em; border-radius: 6px; font-size: .85em;
  font-family: "Cascadia Code", Consolas, "JetBrains Mono", Menlo, monospace; }
main pre { background: var(--code-bg); border: 1px solid var(--border);
  padding: 1.1em 1.3em; border-radius: 12px; overflow-x: auto; line-height: 1.6; }
main pre code { border: none; padding: 0; background: none; font-size: .86em; }
main table { border-collapse: collapse; width: 100%; margin: 1.2em 0; font-size: .9em;
  line-height: 1.6; display: block; overflow-x: auto; }
main th, main td { border: 1px solid var(--border); padding: .65em .95em;
  text-align: left; vertical-align: top; }
main th { background: var(--code-bg); }
main tbody tr:nth-child(even) { background: var(--row); }
main blockquote { border-left: 4px solid var(--accent); margin: 1.1em 0;
  padding: .55em 1.15em; color: var(--muted); background: var(--accent-soft);
  border-radius: 0 10px 10px 0; }
main input[type=checkbox] { width: 1.05em; height: 1.05em; margin: .32em .6em 0 0;
  accent-color: var(--done); cursor: pointer; flex-shrink: 0; }
li.task { list-style: none; margin-left: -1.4em; padding: .5em .75em; border-radius: 10px;
  display: flex; align-items: flex-start; transition: background .15s; }
li.task:hover { background: var(--code-bg); }
li.task.done { background: var(--done-soft); }
li.task.done > .task-text { color: var(--muted); text-decoration: line-through; }
li.task .task-text { flex: 1; min-width: 0; }
details.qa { border: 1px solid var(--border); border-radius: 14px; margin: .9em 0;
  padding: 0 1.25em; transition: border-color .15s; }
details.qa > summary { cursor: pointer; font-weight: 650; padding: 1em 0;
  font-size: 1em; line-height: 1.5; list-style: none; display: flex; gap: .6em; }
details.qa > summary::before { content: "▸"; color: var(--accent); flex-shrink: 0;
  transition: transform .15s; }
details.qa[open] > summary::before { transform: rotate(90deg); }
details.qa > summary::-webkit-details-marker { display: none; }
details.qa > summary:hover { color: var(--accent); }
details.qa[open] { background: var(--code-bg); padding-bottom: 1.1em;
  border-color: var(--accent); }
.hint { font-size: .78em; color: var(--muted); margin-bottom: 1.1em; }
.controls { display: flex; gap: 10px; margin-bottom: .6em; }
.controls button { font-size: 12.5px; border: 1px solid var(--border); background: transparent;
  color: var(--muted); border-radius: 8px; padding: 5px 12px; cursor: pointer; }
.controls button:hover { color: var(--accent); border-color: var(--accent); }
@media (max-width: 900px) {
  .layout { flex-direction: column; }
  nav.side { position: static; width: 100%; max-height: none; }
  main { padding: 24px 20px; }
  .progress-wrap { min-width: 140px; }
}
</style>
</head>
<body>
<header>
  <div class="header-row">
    <h1 class="site">🎯 Role Prep Roadmaps</h1>
    <div class="tabs" id="roleTabs"></div>
    <div class="font-controls">
      <button id="fsMinus" title="Smaller text">A−</button>
      <button id="fsPlus" title="Larger text">A+</button>
      <button id="themeToggle" title="Switch light/dark theme">◐</button>
    </div>
    <div class="progress-wrap">
      <div class="progress-label" id="progressLabel"></div>
      <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
    </div>
  </div>
</header>
<div class="layout">
  <nav class="side">
    <div id="docNav"></div>
    <div class="toc" id="toc"></div>
  </nav>
  <main id="content"></main>
</div>
<script>__MARKED_JS__</script>
<script>
const DATA = __DATA_JSON__;

const state = {
  role: localStorage.getItem("rp:role") || DATA.roles[0].slug,
  doc: localStorage.getItem("rp:doc") || DATA.roles[0].docs[0].id,
};

function role() { return DATA.roles.find(r => r.slug === state.role) || DATA.roles[0]; }
function doc() { return role().docs.find(d => d.id === state.doc) || role().docs[0]; }
function ckKey(i) { return `rp:ck:${state.role}:${state.doc}:${i}`; }

function setState(roleSlug, docId) {
  state.role = roleSlug;
  const r = role();
  state.doc = r.docs.some(d => d.id === docId) ? docId : r.docs[0].id;
  localStorage.setItem("rp:role", state.role);
  localStorage.setItem("rp:doc", state.doc);
  render();
}

function renderTabs() {
  const el = document.getElementById("roleTabs");
  el.innerHTML = "";
  for (const r of DATA.roles) {
    const b = document.createElement("button");
    b.className = "tab" + (r.slug === state.role ? " active" : "");
    b.textContent = r.name;
    b.onclick = () => setState(r.slug, state.doc);
    el.appendChild(b);
  }
}

function renderNav() {
  const el = document.getElementById("docNav");
  el.innerHTML = "";
  for (const d of role().docs) {
    const b = document.createElement("button");
    b.className = "doc-btn" + (d.id === state.doc ? " active" : "");
    b.textContent = d.title;
    b.onclick = () => setState(state.role, d.id);
    el.appendChild(b);
  }
}

function updateProgress() {
  const rm = role().docs.find(d => d.id === "roadmap");
  const total = rm ? rm.tasks : 0;
  let done = 0;
  for (let i = 0; i < total; i++) {
    if (localStorage.getItem(`rp:ck:${state.role}:roadmap:${i}`) === "1") done++;
  }
  const pct = total ? Math.round(100 * done / total) : 0;
  document.getElementById("progressFill").style.width = pct + "%";
  document.getElementById("progressLabel").textContent =
    total ? `Roadmap progress: ${done}/${total} (${pct}%)` : "";
}

function fixLinks(container) {
  for (const a of container.querySelectorAll("a[href]")) {
    const href = a.getAttribute("href");
    if (/^https?:/i.test(href)) {
      a.target = "_blank"; a.rel = "noopener";
    } else if (href.endsWith(".md") || href.includes(".md#")) {
      const [path] = href.split("#");
      let targetRole = state.role;
      let file = path;
      const m = path.match(/^\\.\\.\\/([^/]+)\\/(.+)$/);
      if (m) { targetRole = m[1]; file = m[2]; }
      const targetDoc = file.replace(/\\.md$/, "");
      a.href = "javascript:void(0)";
      a.onclick = () => setState(targetRole, targetDoc);
    }
  }
}

function enhanceCheckboxes(container) {
  const boxes = container.querySelectorAll('li input[type="checkbox"]');
  boxes.forEach((box, i) => {
    box.disabled = false;
    const li = box.closest("li");
    li.classList.add("task");
    const span = document.createElement("span");
    span.className = "task-text";
    while (box.nextSibling) span.appendChild(box.nextSibling);
    li.insertBefore(span, box.nextSibling);
    box.checked = localStorage.getItem(ckKey(i)) === "1";
    li.classList.toggle("done", box.checked);
    box.onchange = () => {
      localStorage.setItem(ckKey(i), box.checked ? "1" : "0");
      li.classList.toggle("done", box.checked);
      updateProgress();
    };
  });
  return boxes.length;
}

function accordionize(container) {
  // Wrap each h3 section of the Q&A bank in a collapsible <details>
  const main = container;
  const headers = [...main.querySelectorAll("h3")];
  for (const h of headers) {
    const details = document.createElement("details");
    details.className = "qa";
    const summary = document.createElement("summary");
    summary.textContent = h.textContent;
    details.appendChild(summary);
    const chunk = [];
    let n = h.nextSibling;
    while (n && !(n.nodeType === 1 && /^H[123]$/.test(n.tagName))) {
      chunk.push(n); n = n.nextSibling;
    }
    h.replaceWith(details);
    chunk.forEach(c => details.appendChild(c));
  }
}

function buildToc(container) {
  const toc = document.getElementById("toc");
  toc.innerHTML = "";
  container.querySelectorAll("h2").forEach((h, i) => {
    h.id = "sec-" + i;
    const a = document.createElement("a");
    a.href = "#sec-" + i;
    a.textContent = h.textContent;
    a.title = h.textContent;
    toc.appendChild(a);
  });
}

function render() {
  renderTabs();
  renderNav();
  const el = document.getElementById("content");
  el.innerHTML = marked.parse(doc().md);
  if (state.doc === "qa-bank") {
    const controls = document.createElement("div");
    controls.className = "controls";
    const open = document.createElement("button");
    open.textContent = "Expand all answers";
    const close = document.createElement("button");
    close.textContent = "Collapse all";
    controls.append(open, close);
    accordionize(el);
    el.querySelector("h1").after(controls);
    open.onclick = () => el.querySelectorAll("details.qa").forEach(d => d.open = true);
    close.onclick = () => el.querySelectorAll("details.qa").forEach(d => d.open = false);
    const hint = document.createElement("div");
    hint.className = "hint";
    hint.textContent = "Try answering out loud before opening each answer.";
    controls.after(hint);
  }
  fixLinks(el);
  const n = enhanceCheckboxes(el);
  if (n) {
    const hint = document.createElement("div");
    hint.className = "hint";
    hint.textContent = "☑ Checkboxes are clickable — progress is saved in this browser.";
    el.querySelector("h1").after(hint);
  }
  buildToc(el);
  updateProgress();
  window.scrollTo(0, 0);
}

const FS_MIN = 15, FS_MAX = 21;
let fontSize = parseInt(localStorage.getItem("rp:fs") || "17", 10);
function applyFontSize() {
  fontSize = Math.min(FS_MAX, Math.max(FS_MIN, fontSize));
  document.documentElement.style.setProperty("--content-size", fontSize + "px");
  localStorage.setItem("rp:fs", String(fontSize));
}
document.getElementById("fsMinus").onclick = () => { fontSize--; applyFontSize(); };
document.getElementById("fsPlus").onclick = () => { fontSize++; applyFontSize(); };
applyFontSize();

function effectiveTheme() {
  const set = document.documentElement.getAttribute("data-theme");
  if (set) return set;
  return matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}
function applyTheme(t) {
  if (t) document.documentElement.setAttribute("data-theme", t);
  localStorage.setItem("rp:theme", t || "");
}
const savedTheme = localStorage.getItem("rp:theme");
if (savedTheme) applyTheme(savedTheme);
document.getElementById("themeToggle").onclick = () =>
  applyTheme(effectiveTheme() === "dark" ? "light" : "dark");

marked.use({ gfm: true, breaks: false });
render();
</script>
</body>
</html>
"""


def main() -> int:
    roles = collect_roles()
    if not roles:
        print("No role directories with docs found under roadmaps/")
        return 1
    data = {"roles": roles}
    # <-escape so no `</script>` inside markdown/code can break the page
    data_json = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    marked_js = get_marked_js()
    html = TEMPLATE.replace("__MARKED_JS__", marked_js).replace("__DATA_JSON__", data_json)
    OUT.write_text(html, encoding="utf-8")
    # Root redirect so GitHub Pages serves the UI at the repo's clean URL
    redirect = (ROOT / "index.html")
    redirect.write_text(
        '<!DOCTYPE html><meta charset="utf-8">'
        '<meta http-equiv="refresh" content="0; url=roadmaps/index.html">'
        '<a href="roadmaps/index.html">Open the Role Prep Roadmaps tracker</a>\n',
        encoding="utf-8",
    )
    total_docs = sum(len(r["docs"]) for r in roles)
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB, "
          f"{len(roles)} roles, {total_docs} docs) + root redirect")
    return 0


if __name__ == "__main__":
    sys.exit(main())
