#!/usr/bin/env python3
"""
Audit RUNS portal + integration log references for broken paths.

This is a "mechanical sanity check" so context resets don't strand people on missing docs.

Reads:
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md

Writes:
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__PORTAL_LINK_AUDIT.md
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SRC_ROOT = REPO_ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


_CODE_SPAN_RE = re.compile(r"`([^`]+)`")
_MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


@dataclass(frozen=True)
class Ref:
    source_file: str
    raw: str
    normalized: str
    exists: bool


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _is_placeholder(ref: str) -> bool:
    if "<" in ref or ">" in ref:
        return True
    if "..." in ref:
        return True
    if "*" in ref:
        return True
    return False


def _is_candidate_path(ref: str) -> bool:
    if not ref:
        return False
    if "://" in ref:
        return False
    if _is_placeholder(ref):
        return False
    prefixes = (
        "docs/",
        "scripts/",
        "sharepacks/",
        "data/",
        "src/",
        "alpha_analytical/",
        "modules/",
        "tests/",
        "briefings/",
        ".codex/",
    )
    return ref.startswith(prefixes)


def _normalize_ref_to_path(ref: str) -> Optional[str]:
    raw = ref.strip()
    if not _is_candidate_path(raw):
        return None
    # Strip anchors and common path:line conventions.
    candidate = raw.split("#", 1)[0]
    if candidate.startswith("scripts/") and " --" in candidate:
        candidate = candidate.split(" ", 1)[0]
    m = re.match(r"^(?P<path>.+?):\d+(?::\d+)?$", candidate)
    if m:
        candidate = m.group("path")
    return candidate


def _exists_in_repo(rel_path: str) -> bool:
    if not rel_path:
        return False
    path = (REPO_ROOT / rel_path).resolve()
    try:
        path.relative_to(REPO_ROOT)
    except ValueError:
        return False
    return path.exists()


def _extract_refs(text: str) -> Iterable[str]:
    for m in _CODE_SPAN_RE.finditer(text):
        yield m.group(1).strip()
    for m in _MD_LINK_RE.finditer(text):
        yield m.group(1).strip()


def _audit_file(path: Path) -> List[Ref]:
    source_rel = _safe_rel(path)
    text = _read_text(path)
    out: List[Ref] = []
    seen: set[Tuple[str, str]] = set()
    for raw in _extract_refs(text):
        normalized = _normalize_ref_to_path(raw)
        if normalized is None:
            continue
        key = (source_rel, normalized)
        if key in seen:
            continue
        seen.add(key)
        out.append(
            Ref(
                source_file=source_rel,
                raw=raw,
                normalized=normalized,
                exists=_exists_in_repo(normalized),
            )
        )
    return out


def _render_report(refs: Sequence[Ref], *, files: Sequence[str], output_rel: str) -> str:
    total = len(refs)
    missing = [r for r in refs if not r.exists]
    ok = total - len(missing)

    lines: List[str] = []
    lines.append("# v0.2 Portal Link Audit (Generated)")
    lines.append("")
    lines.append("Purpose: verify that RUNS navigation docs don’t point to missing artifacts.")
    lines.append("")
    lines.append(f"Inputs:")
    for f in files:
        lines.append(f"- `{f}`")
    lines.append("")
    lines.append(f"Output: `{output_rel}`")
    lines.append("")
    lines.append(f"Refs (existing/total): **{ok}/{total}**")
    if not missing:
        lines.append("")
        lines.append("No broken refs found (for checkable repo paths).")
        return "\n".join(lines).rstrip() + "\n"

    lines.append("")
    lines.append("## Broken refs")
    for r in missing:
        lines.append(f"- `{r.source_file}` → `{r.normalized}`")
    lines.append("")
    lines.append("## Notes")
    lines.append("- This audit only checks repo-local paths (docs/scripts/sharepacks/data/etc).")
    lines.append("- Placeholders like `<D>` are ignored.")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Audit RUNS portal/integration references for broken paths.")
    parser.add_argument(
        "--files",
        nargs="+",
        default=[
            str(REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "PORTAL.md"),
            str(REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "V0_2__INTEGRATION_LOG.md"),
        ],
    )
    parser.add_argument(
        "--output",
        default=str(REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "V0_2__PORTAL_LINK_AUDIT.md"),
    )
    args = parser.parse_args(argv)

    paths = [Path(p) for p in args.files]
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    refs: List[Ref] = []
    for path in paths:
        if not path.exists():
            raise SystemExit(f"Missing input file: {path}")
        refs.extend(_audit_file(path))

    output_rel = _safe_rel(output_path)
    files_rel = [_safe_rel(p) for p in paths]
    report = _render_report(refs, files=files_rel, output_rel=output_rel)
    output_path.write_text(report, encoding="utf-8")
    print(f"Wrote {output_rel}")
    if any(not r.exists for r in refs):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
