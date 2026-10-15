#!/usr/bin/env python3
"""Refresh _data/publications.json from NASA ADS.

Run by .github/workflows/update-publications.yml (weekly, or by hand from the Actions tab).
Needs an ADS API token in the ADS_TOKEN environment variable
(create one at https://ui.adsabs.harvard.edu/user/settings/token).

The CV page (_includes/my-resume-after.html) groups the papers using
_data/publication_groups.yml; first-author papers are detected here.
Only the standard library is used, so the workflow needs no installs.
"""
import html
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import date

ORCID = "0000-0003-3312-909X"
SURNAME = "Anbajagane"
QUERY = f'(orcid:"{ORCID}" OR author:"{SURNAME}, D") doctype:(article OR eprint)'
FIELDS = "bibcode,title,author,pubdate,pub,identifier,doi,citation_count"
API = "https://api.adsabs.harvard.edu/v1/search/query"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_data", "publications.json")

SKIP_TITLE = re.compile(r"^(erratum|corrigendum|publisher'?s note)", re.I)
ARXIV_ID = re.compile(r"^arXiv:(\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7})$", re.I)


def short_name(full):
    """'Anbajagane, Dhayaa' -> 'D. Anbajagane'; 'To, Chun-Hao' -> 'C.-H. To'."""
    last, sep, first = full.partition(",")
    if not sep:
        return full.strip()
    initials = []
    for part in first.split():
        pieces = [p for p in part.split("-") if p]
        if pieces and pieces[0][0].isalpha():
            initials.append("-".join(p[0] + "." for p in pieces))
    return " ".join(initials + [last.strip()])


def format_authors(authors):
    """Short author list with this author in bold, in the style of the PDF CV."""
    names = [short_name(a) for a in authors]
    me = next((i for i, a in enumerate(authors) if a.strip().lower().startswith(SURNAME.lower())), None)
    if len(names) <= 5:
        shown, et_al = names, False
    elif me is not None and me < 6:
        shown, et_al = names[: max(me + 1, 3)], True
    else:
        shown, et_al = names[:3], True
    parts = [f"<strong>{html.escape(n)}</strong>" if i == me else html.escape(n) for i, n in enumerate(shown)]
    return ", ".join(parts) + (", et al." if et_al else "")


def title_html(title):
    """Escape the title but keep ADS's <sup>/<sub> tags, and turn $...$ into MathJax \\(...\\)."""
    out = html.escape(title.replace("~", " "), quote=False)
    out = re.sub(r"&lt;(/?)(sup|sub)&gt;", lambda m: f"<{m.group(1)}{m.group(2).lower()}>", out, flags=re.I)
    return re.sub(r"\$([^$]+)\$", r"\\(\1\\)", out)


def h_index(citations):
    cites = sorted((c or 0 for c in citations), reverse=True)
    return sum(1 for i, c in enumerate(cites, 1) if c >= i)


def build_record(doc):
    """Turn one ADS search result into the record the CV page renders."""
    title = (doc.get("title") or [""])[0]
    authors = doc.get("author") or []
    if not title or not authors or SKIP_TITLE.match(title):
        return None
    arxiv = next((m.group(1) for i in doc.get("identifier") or [] if (m := ARXIV_ID.match(i))), "")
    doi = (doc.get("doi") or [""])[0]
    journal = doc.get("pub") or ""
    if journal.lower() == "arxiv e-prints":
        journal = ""
    bibcode = doc.get("bibcode") or ""
    if arxiv:
        url = f"https://arxiv.org/abs/{arxiv}"
    elif doi:
        url = f"https://doi.org/{doi}"
    else:
        url = f"https://ui.adsabs.harvard.edu/abs/{bibcode}"
    pubdate = doc.get("pubdate") or ""
    return {
        "bibcode": bibcode,
        "arxiv": arxiv,
        "title_html": title_html(title),
        "authors_html": format_authors(authors),
        "first_author": authors[0].strip().lower().startswith(SURNAME.lower()),
        "journal": journal,
        "year": pubdate[:4],
        "pubdate": pubdate,
        "url": url,
        "ads_url": f"https://ui.adsabs.harvard.edu/abs/{bibcode}" if bibcode else "",
        "citations": doc.get("citation_count"),
    }


def build_output(docs, source):
    papers = {}
    for doc in docs:
        rec = build_record(doc)
        if not rec:
            continue
        key = rec["arxiv"] or rec["bibcode"] or rec["title_html"]
        # ADS can list a preprint and its journal version separately; keep the better-cited one.
        if key not in papers or (rec["citations"] or 0) > (papers[key]["citations"] or 0):
            papers[key] = rec
    ordered = sorted(papers.values(), key=lambda p: p["pubdate"], reverse=True)
    first = [p for p in ordered if p["first_author"]]
    have_cites = any(p["citations"] is not None for p in ordered)
    stats = {
        "papers": len(ordered),
        "first_author": len(first),
        "citations": sum(p["citations"] or 0 for p in ordered) if have_cites else None,
        "h_index": h_index(p["citations"] for p in ordered) if have_cites else None,
        "first_author_citations": sum(p["citations"] or 0 for p in first) if have_cites else None,
        "first_author_h_index": h_index(p["citations"] for p in first) if have_cites else None,
    }
    return {"updated": date.today().isoformat(), "source": source, "stats": stats, "papers": ordered}


def write_if_changed(out):
    """Write only when papers or stats changed, so unchanged weeks make no commit."""
    try:
        with open(OUT, encoding="utf-8") as f:
            old = json.load(f)
        if old.get("papers") == out["papers"] and old.get("stats") == out["stats"] and old.get("source") == out["source"]:
            print("No changes.")
            return
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"Wrote {len(out['papers'])} papers to {OUT}")


def fetch_ads(token):
    params = urllib.parse.urlencode({"q": QUERY, "fl": FIELDS, "rows": 500, "sort": "date desc"})
    req = urllib.request.Request(f"{API}?{params}", headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)["response"]["docs"]


def main():
    token = os.environ.get("ADS_TOKEN")
    if not token:
        sys.exit("ADS_TOKEN is not set; add it as a repository secret (see the script docstring).")
    docs = fetch_ads(token)
    if not docs:
        sys.exit("ADS returned no papers; leaving _data/publications.json unchanged.")
    write_if_changed(build_output(docs, "NASA ADS"))


if __name__ == "__main__":
    main()
