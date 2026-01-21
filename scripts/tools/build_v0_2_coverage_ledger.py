#!/usr/bin/env python3
"""
Build a v0.2 "coverage ledger" so we can answer:
  - Did we extract all gold items?
  - Which integration-log items are implemented vs deferred?
  - Do referenced evidence files/scripts actually exist?

This is intentionally reporting-only (docs generation) and does not touch analyzers.

Reads:
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/SUPERBRAIN_V0__GOLD_EXTRACTION.md
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__INTEGRATION_LOG.md
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/PORTAL.md (optional; for "in portal" checks)

Writes:
- docs/AAT9_KIT/FINAL VALIDATION/RUNS/V0_2__COVERAGE_LEDGER.md (default)
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SRC_ROOT = REPO_ROOT / "src"
if SRC_ROOT.exists() and str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


_DATE_HYPHENS = r"[-\u2010\u2011\u2012\u2013\u2014]"
_INTEGRATION_DATE_RE = re.compile(
    rf"^##\s+(?P<date>\d{{4}}{_DATE_HYPHENS}\d{{2}}{_DATE_HYPHENS}\d{{2}})\s+—\s+(?P<title>.+?)\s*$"
)
_GOLD_ENTRY_RE = re.compile(r"^\s*-\s+\*\*(?P<id>GOLD-\d{4})\*\*\s+—\s+(?P<title>.+?)\s*$")
_NEXT_WORK_HEADING_RE = re.compile(r"^##\s+Next work\b", re.IGNORECASE)
_NEXT_WORK_ITEM_RE = re.compile(r"^\s*(?P<n>\d+)\)\s+(?P<title>.+?)\s*$")
_CODE_SPAN_RE = re.compile(r"`([^`]+)`")


@dataclass(frozen=True)
class LedgerItem:
    item_id: str
    source: str
    title: str
    status: str
    in_portal: Optional[bool]
    evidence_refs: List[str]
    evidence_existing: int
    evidence_total: int


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _iter_code_spans(lines: Iterable[str]) -> Iterable[str]:
    for line in lines:
        for m in _CODE_SPAN_RE.finditer(line):
            yield m.group(1).strip()


def _is_checkable_path(ref: str) -> bool:
    if not ref:
        return False
    if "://" in ref:
        return False
    if "<" in ref or ">" in ref:
        return False
    if "..." in ref:
        return False
    if ref.startswith("#"):
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


def _ref_to_path(ref: str) -> Optional[Path]:
    if not _is_checkable_path(ref):
        return None
    # Allow common "path:line" references.
    candidate = ref.split("#", 1)[0]
    if candidate.startswith("scripts/") and " --" in candidate:
        candidate = candidate.split(" ", 1)[0]
    m = re.match(r"^(?P<path>.+?):\d+(?::\d+)?$", candidate)
    if m:
        candidate = m.group("path")
    return (REPO_ROOT / candidate).resolve()


def _check_ref_exists(ref: str) -> bool:
    candidate = _ref_to_path(ref)
    if candidate is None:
        return False
    try:
        candidate.relative_to(REPO_ROOT)
    except ValueError:
        return False
    return candidate.exists()


def _dedupe_preserve_order(values: Sequence[str]) -> List[str]:
    seen = set()
    out: List[str] = []
    for v in values:
        if v in seen:
            continue
        seen.add(v)
        out.append(v)
    return out


def _classify_integration_status(title: str) -> str:
    t = title.lower()
    if "next work" in t or "backlog" in t:
        return "deferred"
    if "harness" in t or "sweep" in t or "experiment" in t or "measured" in t:
        return "harnessed"
    if "implemented" in t or "completed" in t or "contract-locked" in t:
        return "implemented"
    if "new" in t:
        return "implemented"
    return "decisioned"


def _classify_gold_status(evidence_refs: Sequence[str]) -> str:
    t = " ".join(evidence_refs).lower()
    if "harness" in t or "sweep" in t or "experiment" in t:
        return "harnessed"
    return "decisioned"


def _parse_gold_items(text: str, portal_text: Optional[str]) -> List[LedgerItem]:
    lines = text.splitlines()
    items: List[LedgerItem] = []
    starts: List[int] = []
    ids: List[str] = []
    titles: List[str] = []
    for idx, line in enumerate(lines):
        m = _GOLD_ENTRY_RE.match(line)
        if not m:
            continue
        starts.append(idx)
        ids.append(m.group("id"))
        titles.append(m.group("title").strip())
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(lines)
        block = lines[start:end]
        refs = _dedupe_preserve_order([r for r in _iter_code_spans(block) if r])
        existing = sum(1 for r in refs if _check_ref_exists(r))
        status = _classify_gold_status(refs)
        in_portal = None if portal_text is None else (ids[i] in portal_text)
        items.append(
            LedgerItem(
                item_id=ids[i],
                source="gold",
                title=titles[i],
                status=status,
                in_portal=in_portal,
                evidence_refs=refs,
                evidence_existing=existing,
                evidence_total=len(refs),
            )
        )
    return items


def _parse_integration_items(text: str, portal_text: Optional[str]) -> List[LedgerItem]:
    lines = text.splitlines()
    items: List[LedgerItem] = []

    # Dated headings
    starts: List[int] = []
    ids: List[str] = []
    titles: List[str] = []
    used_ids: set[str] = set()

    def _slugify(value: str) -> str:
        prefix = value.split(":", 1)[0].strip() if ":" in value else value.strip()
        slug = re.sub(r"[^a-z0-9]+", "_", prefix.lower()).strip("_")
        return slug[:24] if slug else "entry"

    for idx, line in enumerate(lines):
        m = _INTEGRATION_DATE_RE.match(line)
        if not m:
            continue
        date = m.group("date").replace("\u2011", "-").replace("\u2010", "-").replace("\u2012", "-").replace("\u2013", "-").replace(
            "\u2014", "-"
        )
        starts.append(idx)
        title = m.group("title").strip()
        base = f"V0_2-{date}-{_slugify(title)}"
        item_id = base
        n = 2
        while item_id in used_ids:
            item_id = f"{base}-{n}"
            n += 1
        used_ids.add(item_id)
        ids.append(item_id)
        titles.append(title)

    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(lines)
        block = lines[start:end]
        refs = _dedupe_preserve_order([r for r in _iter_code_spans(block) if r])
        existing = sum(1 for r in refs if _check_ref_exists(r))
        status = _classify_integration_status(titles[i])
        in_portal = None if portal_text is None else (ids[i] in portal_text or titles[i] in portal_text)
        items.append(
            LedgerItem(
                item_id=ids[i],
                source="integration",
                title=titles[i],
                status=status,
                in_portal=in_portal,
                evidence_refs=refs,
                evidence_existing=existing,
                evidence_total=len(refs),
            )
        )

    # Next work items (granular)
    next_heading_idx = None
    for idx, line in enumerate(lines):
        if _NEXT_WORK_HEADING_RE.match(line):
            next_heading_idx = idx
            break
    if next_heading_idx is not None:
        for idx in range(next_heading_idx + 1, len(lines)):
            line = lines[idx]
            if line.startswith("## "):
                break
            m = _NEXT_WORK_ITEM_RE.match(line)
            if not m:
                continue
            n = m.group("n")
            title = m.group("title").strip()
            item_id = f"V0_2-NEXT-{n}"
            block = [line]
            refs = _dedupe_preserve_order([r for r in _iter_code_spans(block) if r])
            existing = sum(1 for r in refs if _check_ref_exists(r))
            in_portal = None if portal_text is None else (item_id in portal_text or title in portal_text)
            items.append(
                LedgerItem(
                    item_id=item_id,
                    source="integration_next",
                    title=title,
                    status="deferred",
                    in_portal=in_portal,
                    evidence_refs=refs,
                    evidence_existing=existing,
                    evidence_total=len(refs),
                )
            )

    return items


def _fmt_yes_no(value: Optional[bool]) -> str:
    if value is None:
        return ""
    return "yes" if value else "no"


def _render_markdown(items: Sequence[LedgerItem], *, output_rel: str) -> str:
    gold = [i for i in items if i.source == "gold"]
    integ = [i for i in items if i.source == "integration"]
    integ_next = [i for i in items if i.source == "integration_next"]

    total_refs = sum(i.evidence_total for i in items)
    total_existing = sum(i.evidence_existing for i in items)

    broken_refs: List[str] = []
    for item in items:
        for ref in item.evidence_refs:
            if _is_checkable_path(ref) and not _check_ref_exists(ref):
                broken_refs.append(f"{item.item_id}: `{ref}`")
    broken_refs = _dedupe_preserve_order(broken_refs)

    lines: List[str] = []
    lines.append("# v0.2 Coverage Ledger (Generated)")
    lines.append("")
    lines.append("Purpose: a single table that proves we didn’t lose v0.2 context.")
    lines.append("")
    lines.append("Status legend (v0.2 language):")
    lines.append("- `implemented`: code/docs change landed (non-analyzer).")
    lines.append("- `harnessed`: measured via a script/harness across windows.")
    lines.append("- `decisioned`: documented/selected posture (defaults/decisions).")
    lines.append("- `deferred`: explicitly queued for later (v0.3+ or next-work).")
    lines.append("")
    lines.append(f"Generated file: `{output_rel}`")
    lines.append("")
    lines.append(f"Evidence refs (existing/total): **{total_existing}/{total_refs}**")
    if broken_refs:
        lines.append("")
        lines.append("## Broken refs (checkable paths only)")
        for ref in broken_refs[:200]:
            lines.append(f"- {ref}")
        if len(broken_refs) > 200:
            lines.append(f"- (truncated; {len(broken_refs)} total)")
    lines.append("")
    lines.append("## Gold Ledger Coverage")
    lines.append("")
    lines.append("| ID | Status | In Portal | Evidence (exists/total) | Title |")
    lines.append("|---|---:|---:|---:|---|")
    for item in gold:
        lines.append(
            "| "
            + " | ".join(
                [
                    item.item_id,
                    item.status,
                    _fmt_yes_no(item.in_portal),
                    f"{item.evidence_existing}/{item.evidence_total}",
                    item.title.replace("|", "\\|"),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## Integration Log Coverage (Dated Entries)")
    lines.append("")
    lines.append("| ID | Status | Evidence (exists/total) | Title |")
    lines.append("|---|---:|---:|---|")
    for item in integ:
        lines.append(
            "| "
            + " | ".join(
                [
                    item.item_id,
                    item.status,
                    f"{item.evidence_existing}/{item.evidence_total}",
                    item.title.replace("|", "\\|"),
                ]
            )
            + " |"
        )
    if integ_next:
        lines.append("")
        lines.append("## Integration Log Coverage (Next Work)")
        lines.append("")
        lines.append("| ID | Status | Title |")
        lines.append("|---|---:|---|")
        for item in integ_next:
            lines.append(
                "| "
                + " | ".join(
                    [
                        item.item_id,
                        item.status,
                        item.title.replace("|", "\\|"),
                    ]
                )
                + " |"
            )
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- This file is generated from the SSOT docs; update the source docs (gold ledger / integration log) first.")
    lines.append("- “Evidence refs” are extracted from markdown code spans; placeholders like `<D>` are ignored for existence checks.")
    return "\n".join(lines).rstrip() + "\n"


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Build the v0.2 coverage ledger (generated markdown).")
    parser.add_argument(
        "--gold-ledger",
        default=str(REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "SUPERBRAIN_V0__GOLD_EXTRACTION.md"),
    )
    parser.add_argument(
        "--integration-log",
        default=str(REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "V0_2__INTEGRATION_LOG.md"),
    )
    parser.add_argument(
        "--portal",
        default=str(REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "PORTAL.md"),
    )
    parser.add_argument(
        "--output",
        default=str(REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS" / "V0_2__COVERAGE_LEDGER.md"),
    )
    args = parser.parse_args(argv)

    gold_path = Path(args.gold_ledger)
    integration_path = Path(args.integration_log)
    portal_path = Path(args.portal)
    output_path = Path(args.output)

    portal_text = _read_text(portal_path) if portal_path.exists() else None

    gold_text = _read_text(gold_path)
    integration_text = _read_text(integration_path)

    items: List[LedgerItem] = []
    items.extend(_parse_gold_items(gold_text, portal_text))
    items.extend(_parse_integration_items(integration_text, portal_text))

    output_rel = _safe_rel(output_path)
    md = _render_markdown(items, output_rel=output_rel)
    _write_text(output_path, md)
    print(f"Wrote {output_rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
