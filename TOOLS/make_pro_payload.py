#!/usr/bin/env python3
"""
Generate the lightweight “Pro Share” payload for V-TRAC validation runs.

Reads the validator JSON outputs under
`data/outputs/analysis/vtrac_validation/<STATE>/validation_report.json`
and emits:

* summary.csv – machine friendly roll-up of overlap/hot/superhot/consensus metrics.
* summary.md  – quick human readable digest with key call-outs.
* vtrac_pro_payload.zip – optional bundle containing the summaries plus the raw
  validation reports (and referenced analyzer bundles) for deeper inspection.

This script is intentionally free of side-effects outside the validation output
tree so it is safe to run repeatedly after each analyzer sweep.
"""

from __future__ import annotations

import csv
import json
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

VALIDATION_ROOT = Path("data/outputs/analysis/vtrac_validation")
SUMMARY_CSV = VALIDATION_ROOT / "summary.csv"
SUMMARY_MD = VALIDATION_ROOT / "summary.md"
PAYLOAD_ZIP = VALIDATION_ROOT / "vtrac_pro_payload.zip"
SECTIONS: Tuple[str, ...] = ("Combined", "Midday", "Evening")


def _load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _as_int(value) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def _as_bool(value) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.lower() in {"true", "1", "yes", "y"}
    return bool(value)


def _as_list(value) -> List[str]:
    if isinstance(value, (list, tuple, set)):
        return [str(v) for v in value if isinstance(v, (str, int, float))]
    if isinstance(value, str) and value:
        return [value]
    return []


@dataclass
class SectionSummary:
    overlap_count: int = 0
    overlap_tokens: List[str] = None
    hot: int = 0
    superhot: int = 0
    consensus_col1: bool = False
    consensus_col2: bool = False
    stable_columns: List[str] = None
    analyzer_mask_drop: int = 0
    analyzer_reduction_hits: int = 0
    analyzer_mirror_supported: int = 0
    analyzer_double_hits: int = 0
    analyzer_top_straights: List[str] = None

    def __post_init__(self) -> None:
        if self.overlap_tokens is None:
            self.overlap_tokens = []
        if self.stable_columns is None:
            self.stable_columns = []
        if self.analyzer_top_straights is None:
            self.analyzer_top_straights = []


@dataclass
class StateSummary:
    state: str
    label: str
    analyzer_json: Optional[str]
    picked_html: Optional[str]
    sections: Dict[str, SectionSummary]


def _select_analyzer_label(analyzer_jsons: Dict[str, str]) -> str:
    if "primary" in analyzer_jsons:
        return "primary"
    if analyzer_jsons:
        # Stable ordering for reproducibility
        return sorted(analyzer_jsons.keys())[0]
    return ""


def _extract_section_summary(section_payload: dict, label: str) -> SectionSummary:
    signals = section_payload.get("signals") or {}
    analyzer_signatures = section_payload.get("analyzer_signatures") or {}
    analyzer_metrics = section_payload.get("analyzer_metrics") or {}

    winners_signatures = set(_as_list(signals.get("top_vtrac_box_signatures")))
    analyzer_signature_list = set(_as_list(analyzer_signatures.get(label) or []))
    overlap = sorted(winners_signatures & analyzer_signature_list)

    metrics_for_label = analyzer_metrics.get(label) or {}
    top_straights_payload = metrics_for_label.get("top_straights") or []
    top_straights = []
    for entry in top_straights_payload:
        if isinstance(entry, dict) and "straight" in entry:
            top_straights.append(str(entry["straight"]))

    return SectionSummary(
        overlap_count=len(overlap),
        overlap_tokens=overlap,
        hot=_as_int(signals.get("hot", signals.get("hot_count", 0))),
        superhot=_as_int(signals.get("superhot", signals.get("superhot_count", 0))),
        consensus_col1=_as_bool(signals.get("consensus_col1")),
        consensus_col2=_as_bool(signals.get("consensus_col2")),
        stable_columns=_as_list(signals.get("stable_columns")),
        analyzer_mask_drop=_as_int(metrics_for_label.get("mask_drop_count")),
        analyzer_reduction_hits=_as_int(metrics_for_label.get("reduction_hits")),
        analyzer_mirror_supported=_as_int(metrics_for_label.get("mirror_supported")),
        analyzer_double_hits=_as_int(metrics_for_label.get("double_hits")),
        analyzer_top_straights=top_straights[:6],
    )


def _build_state_summary(report_path: Path) -> Optional[StateSummary]:
    payload = _load_json(report_path)
    if not payload:
        return None

    analyzer_jsons: Dict[str, str] = payload.get("analyzer_jsons") or {}
    label = _select_analyzer_label(analyzer_jsons)

    sections: Dict[str, SectionSummary] = {}
    for section in SECTIONS:
        section_payload = payload.get("sections", {}).get(section)
        if not isinstance(section_payload, dict):
            sections[section] = SectionSummary()
            continue
        sections[section] = _extract_section_summary(section_payload, label)

    return StateSummary(
        state=payload.get("state", report_path.parent.name),
        label=label or "n/a",
        analyzer_json=analyzer_jsons.get(label),
        picked_html=payload.get("picked_html"),
        sections=sections,
    )


def _iter_state_reports(root: Path) -> Iterable[Path]:
    if not root.exists():
        return []
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        report = child / "validation_report.json"
        if report.exists():
            yield report


def collect_state_summaries() -> List[StateSummary]:
    summaries: List[StateSummary] = []
    for report in _iter_state_reports(VALIDATION_ROOT):
        summary = _build_state_summary(report)
        if summary:
            summaries.append(summary)
    return sorted(summaries, key=lambda s: s.state)


def write_summary_csv(summaries: Sequence[StateSummary]) -> Path:
    headers = [
        "state",
        "analyzer_label",
        "analyzer_json",
        "picked_html",
    ]
    for section in SECTIONS:
        prefix = section.lower()
        headers.extend(
            [
                f"{prefix}_overlap_count",
                f"{prefix}_overlap_tokens",
                f"{prefix}_hot",
                f"{prefix}_superhot",
                f"{prefix}_consensus_col1",
                f"{prefix}_consensus_col2",
                f"{prefix}_stable_columns",
                f"{prefix}_mask_drop",
                f"{prefix}_reduction_hits",
                f"{prefix}_mirror_supported",
                f"{prefix}_double_hits",
                f"{prefix}_analyzer_top_straights",
            ]
        )

    SUMMARY_CSV.parent.mkdir(parents=True, exist_ok=True)
    with SUMMARY_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(headers)
        for summary in summaries:
            row = [
                summary.state,
                summary.label,
                summary.analyzer_json or "",
                summary.picked_html or "",
            ]
            for section in SECTIONS:
                data = summary.sections.get(section, SectionSummary())
                row.extend(
                    [
                        data.overlap_count,
                        ";".join(data.overlap_tokens),
                        data.hot,
                        data.superhot,
                        int(data.consensus_col1),
                        int(data.consensus_col2),
                        ";".join(data.stable_columns),
                        data.analyzer_mask_drop,
                        data.analyzer_reduction_hits,
                        data.analyzer_mirror_supported,
                        data.analyzer_double_hits,
                        ";".join(data.analyzer_top_straights),
                    ]
                )
            writer.writerow(row)
    return SUMMARY_CSV


def _format_section_md(section: str, data: SectionSummary) -> str:
    parts = [
        f"overlap={data.overlap_count}",
        f"hot={data.hot}",
        f"superhot={data.superhot}",
    ]
    if data.consensus_col1 or data.consensus_col2:
        flags = []
        if data.consensus_col1:
            flags.append("C1")
        if data.consensus_col2:
            flags.append("C2")
        parts.append(f"consensus={'+'.join(flags)}")
    if data.stable_columns:
        parts.append(f"stable_cols={','.join(data.stable_columns)}")
    if data.overlap_tokens:
        parts.append(f"tokens={','.join(data.overlap_tokens[:4])}")
    return f"**{section}:** " + ", ".join(parts)


def write_summary_md(summaries: Sequence[StateSummary]) -> Path:
    SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    lines: List[str] = []
    lines.append("# V-TRAC Validator Summary")
    generated = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    lines.append(f"_Generated: {generated}_")
    lines.append("")

    if not summaries:
        lines.append("No validation reports were found under "
                     "`data/outputs/analysis/vtrac_validation/`. "
                     "Run the enhanced analyzer CLI followed by the validator before executing this packer.")
    else:
        for summary in summaries:
            lines.append(f"## {summary.state}")
            lines.append(f"- Analyzer label: `{summary.label}`")
            if summary.analyzer_json:
                lines.append(f"- Analyzer JSON: `{summary.analyzer_json}`")
            if summary.picked_html:
                lines.append(f"- Winners HTML: `{summary.picked_html}`")
            lines.append("")
            for section in SECTIONS:
                data = summary.sections.get(section, SectionSummary())
                lines.append(f"- {_format_section_md(section, data)}")
            lines.append("")

        # Call-out problematic sections for quick triage.
        lines.append("### Flags")
        flagged = False
        for summary in summaries:
            for section in SECTIONS:
                data = summary.sections.get(section, SectionSummary())
                if data.overlap_count == 0 and (data.hot or data.superhot or data.consensus_col1 or data.consensus_col2):
                    lines.append(
                        f"- {summary.state} {section}: zero overlap but signal present "
                        f"(hot={data.hot}, superhot={data.superhot}, consensus={data.consensus_col1 or data.consensus_col2})"
                    )
                    flagged = True
        if not flagged:
            lines.append("- No overlap anomalies detected.")

    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return SUMMARY_MD


def build_payload_zip(summaries: Sequence[StateSummary]) -> Path:
    if PAYLOAD_ZIP.exists():
        PAYLOAD_ZIP.unlink()
    with zipfile.ZipFile(PAYLOAD_ZIP, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for artifact in (SUMMARY_CSV, SUMMARY_MD):
            if artifact.exists():
                zf.write(artifact, artifact.relative_to(VALIDATION_ROOT.parent))

        # Include batch rollups if present
        for name in ("matrix.csv", "findings.md"):
            candidate = VALIDATION_ROOT / name
            if candidate.exists():
                zf.write(candidate, candidate.relative_to(VALIDATION_ROOT.parent))

        # Include per-state reports and referenced analyzer bundles
        for summary in summaries:
            state_dir = VALIDATION_ROOT / summary.state
            for filename in ("validation_report.json", "validation_report.md"):
                path = state_dir / filename
                if path.exists():
                    zf.write(path, path.relative_to(VALIDATION_ROOT.parent))

            if summary.analyzer_json:
                analyzer_path = Path(summary.analyzer_json)
                if not analyzer_path.is_absolute():
                    analyzer_path = (Path.cwd() / analyzer_path).resolve()
                if analyzer_path.exists():
                    try:
                        zf.write(analyzer_path, analyzer_path.relative_to(VALIDATION_ROOT.parent))
                    except ValueError:
                        # Analyzer path may reside outside the validation root; fall back to basename.
                        zf.write(analyzer_path, Path("external") / analyzer_path.name)

    return PAYLOAD_ZIP


def main() -> None:
    summaries = collect_state_summaries()
    write_summary_csv(summaries)
    write_summary_md(summaries)
    build_payload_zip(summaries)
    print(f"Wrote {SUMMARY_CSV}")
    print(f"Wrote {SUMMARY_MD}")
    print(f"Wrote {PAYLOAD_ZIP}")


if __name__ == "__main__":
    main()
