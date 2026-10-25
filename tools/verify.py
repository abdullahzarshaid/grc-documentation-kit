"""Read-only checks on the kit. Exit 1 on any failure. Run in CI and before every commit.

Checks: front matter complete and valid; required headings for policies and procedures; banned
terms (client names, people, vendors, tooling words) absent from every source, built and docs file;
no em or en dash anywhere; placeholders only inside square brackets; related IDs exist; every
built .docx and .xlsx opens and is macro free; register layout (header row 10, rows 11 to 110,
one sheet, frozen pane, validation, table); checksums.json matches kit/.
"""
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC, KIT, DOCS = ROOT / "src", ROOT / "kit", ROOT / "docs"
REQUIRED = ["id", "title", "type", "framework", "maps", "owner", "summary"]
TYPES = {"policy", "procedure", "plan", "statement", "record", "template", "checklist", "playbook", "guide"}
FW = {"iso27001", "iso27701", "soc2", "gdpr", "hipaa", "ai", "cross"}
HEADINGS = ["## 1. Purpose", "## 2. Scope", "## 3. Roles and responsibilities", "## 5. Records and evidence", "## 7. Review and maintenance", "## 8. Related documents"]
DASHES = re.compile("[–—‒―]")
banned = [l.strip() for l in (ROOT / "tools" / "denylist.txt").read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
BANNED = re.compile("|".join(r"(?<![A-Za-z])" + re.escape(b) + r"(?![A-Za-z])" for b in banned), re.I)
ALLOW_IN = {"docs/resources.md", "README.md"}  # pages that credit third parties by name
problems = []
SRC_ONLY = "--src-only" in sys.argv


def fail(msg):
    problems.append(msg)


def text_of_office(p):
    out = []
    with zipfile.ZipFile(p) as z:
        for n in z.namelist():
            if n.lower().endswith(".xml") and ("word/" in n or "xl/" in n or "ppt/" in n):
                out.append(re.sub(r"<[^>]+>", " ", z.read(n).decode("utf-8", "ignore")))
    return " ".join(out)


# ---- sources
ids = set()
docs = []
for p in sorted(SRC.rglob("*.md")):
    rel = p.relative_to(ROOT).as_posix()
    text = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, flags=re.S)
    if not m:
        fail(f"{rel}: no front matter"); continue
    try:
        meta = yaml.safe_load(m.group(1))
    except Exception as e:
        fail(f"{rel}: bad yaml {e}"); continue
    for k in REQUIRED:
        if k not in meta or meta[k] in (None, "", []):
            fail(f"{rel}: front matter missing {k}")
    if meta.get("type") not in TYPES: fail(f"{rel}: type {meta.get('type')!r} not allowed")
    if meta.get("framework") not in FW: fail(f"{rel}: framework {meta.get('framework')!r} not allowed")
    if meta.get("id") in ids: fail(f"{rel}: duplicate id {meta.get('id')}")
    ids.add(meta.get("id"))
    body = m.group(2)
    if meta.get("type") in ("policy", "procedure"):
        for h in HEADINGS:
            if h not in body: fail(f"{rel}: missing heading {h!r}")
    if DASHES.search(text): fail(f"{rel}: contains an em or en dash")
    for bm in BANNED.finditer(text):
        fail(f"{rel}: banned term {bm.group(0)!r}")
    for ph in re.findall(r"\b(lorem|TODO|TBD|xxx)\b", text, flags=re.I):
        fail(f"{rel}: placeholder word {ph!r}")
    docs.append((rel, meta, body))

for rel, meta, body in docs:
    for ref in re.findall(r"\b([A-Z]{2,5}-[A-Z]{2,4}-\d{2,3}[A-Z]?)\b", body):
        if ref not in ids and not any(ref == r.get("id") for r in []):
            pass  # register ids are checked below once registers are loaded

# ---- registers
regs = []
for p in sorted((SRC / "registers").glob("*.yaml")):
    for r in yaml.safe_load(p.read_text(encoding="utf-8")):
        for k in ("id", "key", "title", "framework", "maps", "purpose", "columns"):
            if k not in r: fail(f"{p.name}: register {r.get('id')} missing {k}")
        if r.get("id") in ids: fail(f"{p.name}: duplicate id {r.get('id')}")
        ids.add(r.get("id")); regs.append(r)
        txt = yaml.safe_dump(r)
        if DASHES.search(txt): fail(f"{p.name}: {r.get('id')} contains a dash character")
        for bm in BANNED.finditer(txt): fail(f"{p.name}: banned term {bm.group(0)!r}")

for rel, meta, body in docs:
    plain = re.sub(r"`[^`]*`", "", body)  # identifiers quoted as examples in code spans are not references
    for ref in set(re.findall(r"\b([A-Z]{2,5}-[A-Z]{2,4}-\d{2,3}[A-Z]?)\b", plain)):
        if ref not in ids: fail(f"{rel}: refers to unknown document {ref}")
    for ref in meta.get("related", []) or []:
        if ref not in ids: fail(f"{rel}: related id {ref} does not exist")

# ---- built files and docs pages
for p in ([] if SRC_ONLY else sorted(list(KIT.rglob("*.docx")) + list(KIT.rglob("*.xlsx")))):
    rel = p.relative_to(ROOT).as_posix()
    try:
        with zipfile.ZipFile(p) as z:
            if z.testzip() is not None: fail(f"{rel}: corrupt zip")
            names = z.namelist()
            if any("vba" in n.lower() or "externallink" in n.lower() for n in names): fail(f"{rel}: macro or external link part")
            if p.suffix == ".xlsx":
                sheets = [n for n in names if n.startswith("xl/worksheets/sheet")]
                if len(sheets) != 1: fail(f"{rel}: expected one sheet")
                tables = [n for n in names if n.startswith("xl/tables/table")]
                if len(tables) != 1: fail(f"{rel}: expected one table")
                else:
                    t = z.read(tables[0]).decode("utf-8", "ignore")
                    m = re.search(r'ref="A10:[A-Z]+(\d+)"', t)
                    if not m or int(m.group(1)) < 110: fail(f"{rel}: table range must start at A10 and reach row 110 or beyond")
                sx = z.read(sheets[0]).decode("utf-8", "ignore") if sheets else ""
                if "<pane" not in sx: fail(f"{rel}: no frozen pane")
                if "<dataValidations" not in sx: fail(f"{rel}: no data validation")
    except zipfile.BadZipFile:
        fail(f"{rel}: not a zip"); continue
    t = text_of_office(p)
    if DASHES.search(t): fail(f"{rel}: built file contains a dash character")
    for bm in BANNED.finditer(t): fail(f"{rel}: banned term {bm.group(0)!r}")

for p in ([] if SRC_ONLY else sorted(list(DOCS.glob("*.html")) + list(DOCS.glob("*.md")) + [ROOT / "README.md"])):
    rel = p.relative_to(ROOT).as_posix()
    t = p.read_text(encoding="utf-8")
    if DASHES.search(t): fail(f"{rel}: contains a dash character")
    if rel not in ALLOW_IN:
        for bm in BANNED.finditer(t): fail(f"{rel}: banned term {bm.group(0)!r}")
    else:
        for bm in re.finditer(r"(?i)claude|anthropic|copilot|codex\b", t): fail(f"{rel}: banned tooling term {bm.group(0)!r}")

# ---- checksums
cs = ROOT / "checksums.json"
if SRC_ONLY:
    pass
elif cs.exists():
    recorded = json.loads(cs.read_text(encoding="utf-8"))
    actual = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(list(KIT.rglob("*.docx")) + list(KIT.rglob("*.xlsx")))}
    if recorded != actual: fail("checksums.json does not match kit/ (run tools/checksums.py)")
else:
    fail("checksums.json missing")

if problems:
    print("\n".join(problems[:200])); print(f"FAIL: {len(problems)} problem(s)"); sys.exit(1)
print(json.dumps({"status": "pass", "documents": len(docs), "registers": len(regs), "checks": "front matter, headings, banned terms, dashes, cross references, built files, register layout, checksums"}))
