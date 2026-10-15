#!/usr/bin/env python3
"""Build _data/cv.json (the CV page's sections) from the Overleaf CV source.

Run by .github/workflows/compile-cv.yml after it clones the Overleaf project:

    python3 .github/scripts/cv_from_overleaf.py <path to the Overleaf project>

Each section is one `curve` rubric file, e.g.

    \\begin{rubric}{Awards and Honors}
    \\entry*[2023]
        \\textbf{CCAPP Price Prize,} ``recognizes research excellence...''
    \\end{rubric}

The first \\textbf{...} of an entry is its title. Mentoring entries list one student per
paragraph as `Name [now at], \\textit{project}`. If any section can't be read, the script
exits with an error and leaves _data/cv.json unchanged.
Only the standard library is used, so the workflow needs no installs.
"""
import html
import json
import os
import re
import sys

# Section key (used in cv.md as `cv:<key>`) -> rubric file in the Overleaf project.
SECTIONS = {
    "work": "work.tex",
    "education": "education.tex",
    "teaching": "Teaching.tex",
    "awards": "Awards.tex",
    "service": "Service.tex",
    "mentoring": "Mentoring.tex",
}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_data", "cv.json")

RUBRIC_TITLE = re.compile(r"\\begin\{rubric\}\{([^}]*)\}")
ENTRY = re.compile(r"\\entry\*?\[([^\]]*)\]")
STUDENT = re.compile(r"^(?P<name>[^\[,]+?)\s*(?:\[(?P<now>[^\]]*)\])?\s*,\s*(?P<project>.+)$", re.S)

# Commands rendered as HTML tags around their one argument.
WRAP = {"textbf": "strong", "textit": "em", "emph": "em", "textsc": "span", "texttt": "code", "underline": "u"}
# Commands dropped together with their argument(s).
DROP_ARGS = {"vspace": 1, "hspace": 1, "label": 1, "textcolor": 1, "color": 1}
SYMBOLS = {"&": "&amp;", "$": "$", "%": "%", "_": "_", "#": "#", "{": "{", "}": "}", ",": "\u2009", " ": " ", "\\": "<br>"}
WORDS = {"ldots": "…", "dots": "…", "LaTeX": "LaTeX", "TeX": "TeX", "par": "\n\n", "newline": "<br>"}


def strip_comments(tex):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in tex.splitlines())


def read_arg(s, i):
    """Return (argument, index after it) for a {braced} argument starting at or after i."""
    while i < len(s) and s[i] in " \t\n":
        i += 1
    if i >= len(s) or s[i] != "{":
        return None, i
    depth, j = 0, i
    while j < len(s):
        if s[j] == "\\":
            j += 2
            continue
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1 : j], j + 1
        j += 1
    raise ValueError(f"unbalanced braces near: {s[i:i + 60]!r}")


def latex_html(s):
    """Convert the small subset of LaTeX used in the CV rubrics to HTML."""
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            word = re.match(r"\\([A-Za-z]+)\*?", s[i:])
            if word:
                name, i = word.group(1), i + len(word.group(0))
                if name in WRAP:
                    arg, i = read_arg(s, i)
                    out.append(f"<{WRAP[name]}>{latex_html(arg or '')}</{WRAP[name]}>")
                elif name in ("href", "url"):
                    url, i = read_arg(s, i)
                    text = url
                    if name == "href":
                        text, i = read_arg(s, i)
                    out.append(f'<a href="{html.escape(url or "")}">{latex_html(text or "")}</a>')
                elif name in DROP_ARGS:
                    for _ in range(DROP_ARGS[name]):
                        _, i = read_arg(s, i)
                else:
                    out.append(WORDS.get(name, ""))
                    if name in WORDS or not s[i:i + 1] == "{":
                        while i < len(s) and s[i] in " \t":  # LaTeX eats spaces after a control word
                            i += 1
            else:
                sym = s[i + 1 : i + 2]
                out.append(SYMBOLS.get(sym, html.escape(sym)))
                i += 2
        elif c in "{}":
            i += 1
        elif c == "~":
            out.append("\u00a0")
            i += 1
        elif s.startswith("---", i):
            out.append("—")
            i += 3
        elif s.startswith("--", i):
            out.append("–")
            i += 2
        elif s.startswith("``", i):
            out.append("“")
            i += 2
        elif s.startswith("''", i):
            out.append("”")
            i += 2
        elif c == "$":
            end = s.find("$", i + 1)
            math = s[i + 1 : end] if end > i else ""
            out.append(f"\\({html.escape(math)}\\)")
            i = end + 1 if end > i else len(s)
        else:
            out.append(html.escape(c, quote=False))
            i += 1
    return "".join(out)


def paragraphs(html_text):
    """Split on blank lines (and \\par), collapse whitespace, drop empty paragraphs."""
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", html_text)]
    return [p for p in paras if p]


def format_when(when):
    """'2020 - 2026' -> '2020 – 2026', '2025-' -> '2025 –', '2022-Now' -> '2022 – now'."""
    when = re.sub(r"\s*-\s*", " – ", when.strip()).strip()
    return re.sub(r"\bNow\b", "now", when)


def parse_rubric(tex, mentoring=False):
    tex = strip_comments(tex)
    title = RUBRIC_TITLE.search(tex)
    if not title:
        raise ValueError("no \\begin{rubric}{...}")
    body = tex[title.end() : tex.find("\\end{rubric}") if "\\end{rubric}" in tex else len(tex)]
    marks = list(ENTRY.finditer(body))
    entries = []
    for k, m in enumerate(marks):
        chunk = body[m.end() : marks[k + 1].start() if k + 1 < len(marks) else len(body)]
        entry = {"when": format_when(m.group(1))}
        if mentoring:
            students = []
            for para in re.split(r"\n\s*\n|\\par\b", chunk):
                para = re.sub(r"\\vspace\*?\{[^}]*\}", "", para).strip()
                if not para:
                    continue
                st = STUDENT.match(para)
                if not st:
                    raise ValueError(f"can't read mentoring line: {para[:80]!r}")
                students.append({
                    "name": latex_html(st.group("name")).strip(),
                    "now": latex_html(st.group("now") or "").strip(),
                    "project": re.sub(r"\s+", " ", latex_html(st.group("project"))).strip(),
                })
            entry["students"] = students
        else:
            # Mark the entry's first bold phrase as its title (styled separately on the page).
            content = paragraphs(latex_html(chunk).replace("<strong>", '<strong class="cv-item-title">', 1))
            entry["paragraphs"] = content
        if entry.get("students") or entry.get("paragraphs"):
            entries.append(entry)
    if not entries:
        raise ValueError("no \\entry[...] items found")
    return {"title": latex_html(title.group(1)).strip(), "entries": entries}


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = sys.argv[1]
    files = {f.lower(): f for f in os.listdir(src)}
    sections, errors = {}, []
    for key, name in SECTIONS.items():
        found = files.get(name.lower())
        if not found:
            errors.append(f"{name}: file not found in the Overleaf project")
            continue
        try:
            with open(os.path.join(src, found), encoding="utf-8") as f:
                sections[key] = parse_rubric(f.read(), mentoring=(key == "mentoring"))
        except (ValueError, AttributeError) as e:
            errors.append(f"{found}: {e}")
    if errors:
        sys.exit("Could not read the CV source; _data/cv.json left unchanged.\n" + "\n".join(errors))
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"source": "Overleaf", "sections": sections}, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"Wrote {', '.join(f'{k} ({len(v['entries'])})' for k, v in sections.items())} to {OUT}")


if __name__ == "__main__":
    main()
