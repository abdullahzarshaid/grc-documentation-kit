"""Record SHA-256 of every built file in kit/ into checksums.json."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = sorted(list((ROOT / "kit").rglob("*.docx")) + list((ROOT / "kit").rglob("*.xlsx")))
data = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(ROOT / "checksums.json").write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
print(f"recorded {len(data)} files")
