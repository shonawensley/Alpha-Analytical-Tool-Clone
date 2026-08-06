#!/usr/bin/env python3
"""Build a compact external-review bundle for Primary Extraction Zone analysis."""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import shutil
import sys
import tempfile
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from alpha_analytical.digit_reduction.analyzer_v2.winners_overlay import (
    MATCH_CSS_CLASS,
    MATCH_ORDER,
    WinnerSpec,
    _highlight_html,
    _summarize_winner_map,
    build_winner_map,
)


DEFAULT_DATE = "2026-03-09"
DEFAULT_BRAIN1_INDEX = (
    REPO_ROOT
    / "docs/AAT9_KIT/FINAL VALIDATION/MASTER_DEEP_REVIEW_SPEC_V2/"
    "phase1_execution/replays/2026-03-09__R_PATTERN_V1/gold_day/brain1/"
    "GOLD_DAY_BRAIN1_INDEX.json"
)
DEFAULT_PACKAGE_ROOT = (
    REPO_ROOT / f"tasks/PRIMARY_EXTRACTION_ZONE_REVIEW__{DEFAULT_DATE}"
)
DEFAULT_OUTPUT = DEFAULT_PACKAGE_ROOT / "EXTERNAL_REVIEW_READY"
DEFAULT_AUX_CORE_ROOT = (
    REPO_ROOT
    / "docs/AAT9_KIT/FINAL VALIDATION/RUNS_2/AUX_CORE_V1"
)

PERIOD_ORDER = {"Midday": 0, "Evening": 1}
TABLE_VARIANTS = ("Midday", "Evening", "Combined")
MATCH_LABELS = {
    "exact": "Canonical permutation",
    "vtrac": "VTRAC-related",
    "drop_exact": "Drop-one canonical",
    "drop_vtrac": "Drop-one VTRAC",
    "family_exact": "Three-value canonical",
    "family_vtrac": "Three-value VTRAC",
}
ZONE_1_COLUMNS = {
    ("set3", "draw1"): frozenset({7, 6, 5}),
    ("set2", "draw1"): frozenset({7, 6, 5}),
    ("set1", "draw1"): frozenset({7, 6, 5}),
}
ZONE_2_COLUMNS = {
    ("set1", "draw2"): frozenset({6, 5, 4}),
    ("set1", "draw3"): frozenset({5, 4, 3, 2}),
    ("set1", "draw4"): frozenset({4, 3, 2}),
    ("set1", "draw5"): frozenset({3, 2, 1}),
    ("set1", "draw6"): frozenset({2, 1}),
    ("set1", "draw7"): frozenset({1}),
}
ZONE_ROW_TYPES = frozenset({"r2", "r4", "r6", "r8"})
ZONE_ROW_RE = re.compile(
    r"<tr(?P<attrs>[^>]*)>(?P<body>.*?)</tr>",
    flags=re.IGNORECASE | re.DOTALL,
)
ZONE_CELL_RE = re.compile(
    r"<(?P<tag>t[dh])(?P<attrs>[^>]*)>(?P<content>.*?)</(?P=tag)>",
    flags=re.IGNORECASE | re.DOTALL,
)
HTML_TAG_RE = re.compile(r"<[^>]+>")
EXPECTED_THREE_VARIANT_ZONE_COUNTS = {
    "ZONE_1": 108,
    "ZONE_2": 192,
    "OVERLAP": 0,
    "ANNOTATED_CELLS": 300,
}
ZONE_OVERLAY_STYLE = """
<style>
.extraction-zone-map {
  max-width: 1800px; margin: 10px auto 16px; padding: 10px 14px;
  border: 2px solid #344f5e; background: #f8fbf7; color: #17201d;
  font: 13px/1.4 ui-monospace, SFMono-Regular, Consolas, monospace;
}
.extraction-zone-map p { margin: 4px 0; }
.zone-chip { display: inline-block; padding: 2px 7px; margin-right: 7px; border: 1px solid #777; font-weight: 700; }
.zone-chip-1 { background: #cfe8f2; border-color: #377c98; }
.zone-chip-2 { background: #f6dfad; border-color: #a97616; }
.zone-chip-both { background: linear-gradient(135deg, #cfe8f2 0 50%, #f6dfad 50% 100%); border-color: #536d66; }
td[data-extraction-zones~="ZONE_1"] {
  background: #d9eef6 !important; box-shadow: inset 0 0 0 2px #377c98;
}
td[data-extraction-zones~="ZONE_2"] {
  background: #fae8bd !important; box-shadow: inset 0 0 0 2px #a97616;
}
td[data-extraction-zones~="ZONE_1"][data-extraction-zones~="ZONE_2"] {
  background: linear-gradient(135deg, #d9eef6 0 50%, #fae8bd 50% 100%) !important;
  box-shadow: inset 0 0 0 2px #536d66;
}
</style>
"""
ZONE_OVERLAY_LEGEND = """
<section class="extraction-zone-map">
  <p><strong>Locked extraction-zone map:</strong>
    <span class="zone-chip zone-chip-1">Zone 1 feeder</span>
    <span class="zone-chip zone-chip-2">Zone 2 staircase</span>
  </p>
  <p>Markers cover R2/R4/R6/R8 cells at the locked coordinates. Zone 3 is a
     survivor/repeat/maturity state, not a fixed rectangle, and must be
     identified with coordinate lineage during analysis.</p>
  <p>These doctrine-driven markers are separate from legacy yellow
     long-string Digit Reduction boxes.</p>
</section>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis-date", default=DEFAULT_DATE)
    parser.add_argument("--brain1-index", type=Path, default=DEFAULT_BRAIN1_INDEX)
    parser.add_argument("--winner-root", type=Path)
    parser.add_argument("--replay-root", type=Path)
    parser.add_argument("--aux-core-root", type=Path, default=DEFAULT_AUX_CORE_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--no-zip",
        action="store_true",
        help="Do not create a ZIP beside the output directory.",
    )
    return parser.parse_args()


def repo_path(path: Path) -> Path:
    path = path if path.is_absolute() else REPO_ROOT / path
    resolved = path.resolve()
    resolved.relative_to(REPO_ROOT)
    return resolved


def relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def one_match(paths: list[Path], label: str) -> Path:
    if len(paths) != 1:
        rendered = ", ".join(str(path) for path in paths) or "none"
        raise RuntimeError(f"Expected one {label}; found {len(paths)}: {rendered}")
    return paths[0]


def load_rows(index_path: Path, analysis_date: str) -> list[dict[str, Any]]:
    payload = json.loads(index_path.read_text(encoding="utf-8"))
    if payload.get("analysis_date") != analysis_date:
        raise RuntimeError(
            f"Brain1 index date {payload.get('analysis_date')!r} does not match "
            f"{analysis_date!r}"
        )
    rows = payload.get("rows") or []
    rows = [
        row
        for row in rows
        if row.get("period") in PERIOD_ORDER and row.get("winner")
    ]
    rows.sort(
        key=lambda row: (
            str(row["state_key"]),
            PERIOD_ORDER[str(row["period"])],
        )
    )
    if not rows:
        raise RuntimeError("Brain1 index contains no Midday/Evening outcomes")

    pairs = Counter((row["state_key"], row["period"]) for row in rows)
    duplicates = [pair for pair, count in pairs.items() if count != 1]
    if duplicates:
        raise RuntimeError(f"Duplicate or incomplete state-period rows: {duplicates}")
    return rows


def read_table_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = list(reader.fieldnames or [])
        rows = [
            {field: str(row.get(field) or "") for field in fields}
            for row in reader
        ]
    if not fields:
        raise RuntimeError(f"Table CSV has no header: {path}")
    if not rows:
        raise RuntimeError(f"Table CSV has no rows: {path}")
    return fields, rows


def _plain_cell_text(content: str) -> str:
    return html.unescape(HTML_TAG_RE.sub("", content)).strip()


def _coordinate_zones(
    *, set_name: str, draw: str, row_type: str, column: int
) -> tuple[str, ...]:
    if row_type.strip().lower() not in ZONE_ROW_TYPES:
        return ()
    coordinate = (set_name.strip().lower(), draw.strip().lower())
    zones: list[str] = []
    if column in ZONE_1_COLUMNS.get(coordinate, ()):
        zones.append("ZONE_1")
    if column in ZONE_2_COLUMNS.get(coordinate, ()):
        zones.append("ZONE_2")
    return tuple(zones)


def annotate_extraction_zones(source_html: str) -> tuple[str, dict[str, int]]:
    """Add review-only Zone 1/2 markers without changing cell contents."""
    if "data-extraction-zones=" in source_html:
        raise RuntimeError("Extraction-zone overlay is already present")

    counts = Counter()

    def annotate_row(row_match: re.Match[str]) -> str:
        body = row_match.group("body")
        cells = list(ZONE_CELL_RE.finditer(body))
        if len(cells) < 10 or any(
            cell.group("tag").lower() != "td" for cell in cells[:3]
        ):
            return row_match.group(0)

        set_name, draw, row_type = (
            _plain_cell_text(cell.group("content")) for cell in cells[:3]
        )
        replacements: list[str] = []
        cursor = 0
        for index, cell in enumerate(cells):
            replacements.append(body[cursor : cell.start()])
            rendered_cell = cell.group(0)
            if 3 <= index <= 9:
                column = 7 - (index - 3)
                zones = _coordinate_zones(
                    set_name=set_name,
                    draw=draw,
                    row_type=row_type,
                    column=column,
                )
                if zones:
                    attrs = cell.group("attrs")
                    label = " + ".join(zone.replace("_", " ") for zone in zones)
                    rendered_cell = (
                        f'<td{attrs} data-extraction-zones="{" ".join(zones)}" '
                        f'title="{html.escape(label)}">{cell.group("content")}</td>'
                    )
                    counts["ANNOTATED_CELLS"] += 1
                    for zone in zones:
                        counts[zone] += 1
                    if len(zones) == 2:
                        counts["OVERLAP"] += 1
            replacements.append(rendered_cell)
            cursor = cell.end()
        replacements.append(body[cursor:])
        return (
            f'<tr{row_match.group("attrs")}>{"".join(replacements)}</tr>'
        )

    annotated = ZONE_ROW_RE.sub(annotate_row, source_html)
    summary = {
        key: int(counts.get(key, 0))
        for key in EXPECTED_THREE_VARIANT_ZONE_COUNTS
    }
    if summary != EXPECTED_THREE_VARIANT_ZONE_COUNTS:
        raise RuntimeError(
            "Unexpected extraction-zone overlay coverage: "
            f"expected={EXPECTED_THREE_VARIANT_ZONE_COUNTS}, actual={summary}"
        )
    if "</head>" in annotated:
        annotated = annotated.replace(
            "</head>", ZONE_OVERLAY_STYLE + "</head>", 1
        )
    else:
        annotated = ZONE_OVERLAY_STYLE + annotated
    if "<body>" in annotated:
        annotated = annotated.replace(
            "<body>", "<body>" + ZONE_OVERLAY_LEGEND, 1
        )
    else:
        annotated = ZONE_OVERLAY_LEGEND + annotated
    return annotated, summary


def write_zone_annotated_copy(
    source: Path, destination: Path
) -> dict[str, int]:
    if not source.is_file():
        raise FileNotFoundError(source)
    annotated, summary = annotate_extraction_zones(
        source.read_text(encoding="utf-8")
    )
    destination.write_text(annotated, encoding="utf-8")
    return summary


def render_pre_result_tables(
    *,
    state: str,
    table_sources: Mapping[str, Path],
    output_path: Path,
) -> dict[str, Any]:
    """Render source-faithful three-variant tables without a result join."""
    rendered_sections: list[str] = []
    source_receipts: dict[str, Any] = {}
    expected_fields: list[str] | None = None

    for variant in TABLE_VARIANTS:
        source = table_sources[variant]
        fields, rows = read_table_csv(source)
        if expected_fields is None:
            expected_fields = fields
        elif fields != expected_fields:
            raise RuntimeError(
                f"Table headers differ for {state}: "
                f"{variant}={fields}, expected={expected_fields}"
            )

        header = "".join(f"<th>{html.escape(field)}</th>" for field in fields)
        body_rows = []
        for row in rows:
            cells = "".join(
                f"<td>{html.escape(row[field])}</td>" for field in fields
            )
            body_rows.append(f"<tr>{cells}</tr>")
        rendered_sections.append(
            "\n".join(
                [
                    '<section class="variant-panel">',
                    f"<h2>{html.escape(variant)} Data</h2>",
                    f"<h3>{html.escape(state)} {html.escape(variant)} "
                    "Combined Table</h3>",
                    '<div class="table-scroll">',
                    f"<table><thead><tr>{header}</tr></thead>",
                    f"<tbody>{''.join(body_rows)}</tbody></table>",
                    "</div>",
                    "</section>",
                ]
            )
        )
        source_receipts[variant.lower()] = {
            "source": relative(source),
            "source_sha256": sha256(source),
            "row_count": len(rows),
            "columns": fields,
        }

    provenance = " | ".join(
        f"{variant}: <code>{html.escape(relative(table_sources[variant]))}</code>"
        for variant in TABLE_VARIANTS
    )
    document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(state)} - Frozen Pre-Result Three-Variant Tables</title>
<style>
:root {{ --ink: #17201d; --paper: #f3efe4; --panel: #fffdf6; --line: #b9ad95; --accent: #1e5e53; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; padding: 24px; color: var(--ink); background: var(--paper); font: 14px/1.45 Georgia, serif; }}
header {{ max-width: 1600px; margin: 0 auto 18px; padding: 16px 18px; border: 2px solid var(--accent); background: var(--panel); }}
h1 {{ margin: 0 0 8px; font-size: 24px; }}
header p {{ margin: 5px 0; }}
code {{ font: 12px/1.4 ui-monospace, SFMono-Regular, Consolas, monospace; overflow-wrap: anywhere; }}
.three-variant-layout {{ display: grid; grid-template-columns: repeat(3, minmax(520px, 1fr)); gap: 10px; max-width: 1800px; margin: 0 auto; }}
.variant-panel {{ min-width: 0; padding: 10px; border: 1px solid var(--line); background: var(--panel); }}
.variant-panel h2, .variant-panel h3 {{ margin: 3px 0 8px; }}
.table-scroll {{ overflow-x: auto; }}
table {{ width: 100%; border-collapse: collapse; font: 12px/1.25 ui-monospace, SFMono-Regular, Consolas, monospace; }}
th, td {{ border: 1px solid #777; padding: 4px 5px; text-align: center; white-space: nowrap; }}
th {{ position: sticky; top: 0; background: #e5eee8; }}
@media (max-width: 1200px) {{ .three-variant-layout {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>
<header>
  <h1>{html.escape(state)} - Frozen Pre-Result Three-Variant Tables</h1>
  <p><strong>Claim class:</strong> FROZEN_PRE_RESULT_TABLE_VIEW_RECONSTRUCTION</p>
  <p>This view contains the exact frozen CSV cell values for Midday, Evening,
     and Combined. It performs no result join and applies no target-dependent
     highlighting, ranking, or pattern credit.</p>
  <p><strong>Sources:</strong> {provenance}</p>
</header>
<main class="three-variant-layout">
{''.join(rendered_sections)}
</main>
</body>
</html>
"""
    document, zone_overlay = annotate_extraction_zones(document)
    output_path.write_text(document, encoding="utf-8")
    return {
        "claim_class": "FROZEN_PRE_RESULT_TABLE_VIEW_RECONSTRUCTION",
        "sources": source_receipts,
        "zone_overlay": zone_overlay,
        "output_sha256": sha256(output_path),
    }


def copy_verified(source: Path, destination: Path) -> None:
    if not source.is_file():
        raise FileNotFoundError(source)
    shutil.copy2(source, destination)
    if sha256(source) != sha256(destination):
        raise RuntimeError(f"Copy verification failed: {source} -> {destination}")


def overlay_banner(
    row: dict[str, Any],
    summary: dict[str, Any],
    *,
    source_report: Path,
    source_training: Path,
) -> str:
    counts = summary["counts"]
    count_parts = [
        f"{MATCH_LABELS[kind]}: {counts.get(f'{kind}_any', 0)}"
        for kind in MATCH_ORDER
    ]
    final_parts = [
        f"{MATCH_LABELS[kind]}: {counts.get(f'{kind}_final', 0)}"
        for kind in MATCH_ORDER
    ]
    earliest = summary["earliest"]
    earliest_parts = [
        f"{MATCH_LABELS[kind]}: step {earliest[kind]}"
        for kind in MATCH_ORDER
        if int(earliest.get(kind, -1)) >= 0
    ]
    legend = " ".join(
        f'<span class="{MATCH_CSS_CLASS[kind]}">{html.escape(MATCH_LABELS[kind])}</span>'
        for kind in MATCH_ORDER
    )
    permutations = ", ".join(summary.get("winner_permutations") or []) or "n/a"
    family = ", ".join(summary.get("winner_vtrac_family") or []) or "n/a"
    boxed_vtrac = row.get("winner_vtrac_index")
    boxed_vtrac_text = f"v{boxed_vtrac}" if boxed_vtrac is not None else "N/A"

    return f"""
<style>
.dr-winner-exact {{ background: rgba(255, 215, 0, 0.85); color: #111; padding: 0 2px; border-radius: 2px; }}
.dr-winner-vtrac {{ background: rgba(255, 140, 0, 0.55); color: #111; padding: 0 2px; border-radius: 2px; }}
.dr-winner-drop-exact {{ border: 1px solid rgba(229, 194, 0, 0.8); background: rgba(255, 215, 0, 0.28); color: #111; padding: 0 2px; border-radius: 2px; }}
.dr-winner-drop-vtrac {{ border: 1px solid rgba(230, 138, 0, 0.8); background: rgba(255, 165, 0, 0.25); color: #111; padding: 0 2px; border-radius: 2px; }}
.dr-winner-family-exact {{ background: rgba(135, 206, 250, 0.3); color: #111; padding: 0 2px; border-radius: 2px; border: 1px solid rgba(90, 162, 201, 0.6); }}
.dr-winner-family-vtrac {{ background: rgba(186, 85, 211, 0.3); color: #111; padding: 0 2px; border-radius: 2px; border: 1px solid rgba(123, 47, 165, 0.6); }}
.pez-review-banner {{ border: 2px solid #31516b; padding: 14px; margin: 12px; background: #eef6fb; color: #17212b; font: 14px/1.45 Arial, sans-serif; }}
.pez-review-banner h1 {{ margin: 0 0 8px; font-size: 20px; }}
.pez-review-banner p {{ margin: 5px 0; }}
.pez-review-banner code {{ background: #dceaf4; padding: 1px 3px; }}
</style>
<section class="pez-review-banner">
  <h1>Digit Reduction Full-Ladder Winner Overlay</h1>
  <p><strong>Target:</strong> {html.escape(str(row["state_key"]))} |
     {html.escape(str(row["period"]))} |
     winner <strong>{html.escape(str(row["winner"]))}</strong> |
     canonical {html.escape(str(row["winner_canonical"]))} |
     boxed VTRAC {html.escape(boxed_vtrac_text)} |
     ordered V-code {html.escape(str(row.get("winner_ordered_vcode") or "N/A"))}</p>
  <p><strong>Scan scope:</strong> all Midday, Evening, and Combined reduction
     ladders in the source stacked report. This is a post-result forensic view,
     not a frozen predictive output.</p>
  <p><strong>Legend:</strong> {legend}</p>
  <p><strong>Rows with evidence:</strong> {" | ".join(count_parts)}</p>
  <p><strong>Final-value evidence:</strong> {" | ".join(final_parts)}</p>
  <p><strong>Earliest reduction step:</strong>
     {" | ".join(earliest_parts) if earliest_parts else "n/a"}</p>
  <p><strong>Winner permutations:</strong> {html.escape(permutations)}</p>
  <p><strong>Winner VTRAC-family variants:</strong> {html.escape(family)}</p>
  <p><strong>Provenance:</strong>
     <code>{html.escape(relative(source_report))}</code> and
     <code>{html.escape(relative(source_training))}</code></p>
</section>
"""


def build_full_ladder_overlay(
    row: dict[str, Any],
    *,
    source_report: Path,
    source_training: Path,
    output_path: Path,
) -> dict[str, Any]:
    spec = WinnerSpec(
        combo=str(row["winner"]),
        variant=str(row["period"]),
        when=str(row.get("analysis_date") or ""),
    )
    # "Combined" is the analyzer API's all-sections scan mode.
    winner_map = build_winner_map(source_training, spec, variant="Combined")
    summary = _summarize_winner_map(winner_map)
    source_html = source_report.read_text(encoding="utf-8")
    annotated = _highlight_html(source_html, spec)
    banner = overlay_banner(
        row,
        summary,
        source_report=source_report,
        source_training=source_training,
    )
    marker = "<body>"
    if marker in annotated:
        annotated = annotated.replace(marker, marker + banner, 1)
    else:
        annotated = banner + annotated
    output_path.write_text(annotated, encoding="utf-8")
    return {
        "item_count": summary["counts"]["items_total"],
        "counts": summary["counts"],
        "earliest": summary["earliest"],
    }


def write_start_here(
    path: Path,
    *,
    analysis_date: str,
    state_count: int,
    outcome_count: int,
) -> None:
    path.write_text(
        "\n".join(
            [
                f"# External Example Review - {analysis_date}",
                "",
                "This is a review-only convenience package. It does not install new",
                "runtime behavior and it does not replace the authoritative replay,",
                "AUX CORE, or Master Deep Review artifacts.",
                "",
                f"- States: `{state_count}`",
                f"- Outcomes: `{outcome_count}` (`Midday` + `Evening`)",
                "- Source lane: corrected `R_PATTERN_V1` March 9 replay",
                "",
                "## Required Review Order",
                "",
                "1. Open `00_PRE_RESULT_INDEX.html`.",
                "2. Review one state's complete `PRE_RESULT` folder without opening",
                "   its `POST_RESULT` folder.",
                "3. Record the blind interpretation.",
                "4. Open that state's `POST_RESULT` folder for winner-aware forensics.",
                "5. Repeat for the next state.",
                "",
                "`90_POST_RESULT_INDEX.html` reveals the forensic artifacts. Do not",
                "open it before completing the blind pass.",
                "",
                "## PRE_RESULT",
                "",
                "- Three corrected frozen string tables, rendered side by side with no",
                "  target-dependent highlighting. Doctrine-driven Zone 1 and Zone 2",
                "  coordinate markers are present and do not use a result.",
                "- Full all-variant Digit Reduction ladder.",
                "- Midday and Evening Digit Reduction analyzer views.",
                "- Full ten-block AUX CORE report with legend.",
                "",
                "## POST_RESULT",
                "",
                "- Corrected string-table winner/VTRAC forensic view with the same",
                "  doctrine-driven Zone 1 and Zone 2 coordinate markers.",
                "- Full-ladder Digit Reduction winner overlay.",
                "- AUX CORE result join and conversion interpretation.",
                "",
                "## Boundaries and Integrity",
                "",
                "- Pre-result files receive predictive-evidence eligibility only as",
                "  frozen evidence; this package does not claim they are selections.",
                "- Post-result files are reverse-engineering and diagnostic evidence.",
                "  They receive no predictive credit.",
                "- `MANIFEST.json` records source paths, claim classes, and SHA-256",
                "  receipts.",
                "- `MANIFEST.csv` is the compact inventory.",
                "- `00_REVIEW_INDEX.html` is a neutral gateway to the two indexes.",
                "- The authoritative source files were not modified.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_state_guide(path: Path, *, state: str) -> None:
    path.write_text(
        "\n".join(
            [
                f"# {state} External Review Guide",
                "",
                "1. Review every file in `PRE_RESULT` and write the blind read.",
                "2. Only then open `POST_RESULT` for outcome-aware forensics.",
                "",
                "`PRE_RESULT` filenames and content do not include a joined target.",
                "`POST_RESULT` filenames intentionally identify the period and result.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_zone_index(
    path: Path,
    artifacts: Sequence[Mapping[str, Any]],
    *,
    zone: str,
) -> None:
    sections: list[str] = []
    for state in sorted({str(row["state"]) for row in artifacts}):
        state_rows = [
            row
            for row in artifacts
            if row["state"] == state and row["zone"] == zone
        ]
        state_rows.sort(
            key=lambda row: (
                PERIOD_ORDER.get(str(row.get("period")), -1),
                int(row["order"]),
            )
        )
        links: list[str] = []
        for row in state_rows:
            period = str(row.get("period") or "")
            prefix = f"{period} - " if period else ""
            links.append(
                f'<li><a href="{html.escape(str(row["output_path"]))}">'
                f'{html.escape(prefix + str(row["label"]))}</a></li>'
            )
        sections.append(
            f"<section><h2>{html.escape(state)}</h2><ul>{''.join(links)}</ul></section>"
        )
    title = (
        "Pre-Result Blind Review"
        if zone == "PRE_RESULT"
        else "Post-Result Forensic Review"
    )
    warning = (
        "These files contain no joined target. Complete this pass before opening "
        "the post-result index."
        if zone == "PRE_RESULT"
        else "These files reveal outcomes and are for reverse-engineering and "
        "diagnostic analysis only."
    )
    path.write_text(
        f"""<!doctype html>
<html><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<style>
body {{ font: 16px/1.45 Georgia, serif; max-width: 980px; margin: 32px auto; padding: 0 20px; background: #f4efe4; color: #20241f; }}
h1 {{ border-bottom: 3px solid #b94b31; padding-bottom: 8px; }}
section {{ background: #fffaf0; border: 1px solid #cfc3ab; margin: 14px 0; padding: 10px 18px; }}
li {{ margin: 5px 0; }}
a {{ color: #174f68; }}
</style></head><body>
<h1>{html.escape(title)}</h1>
<p>{html.escape(warning)}</p>
"""
        + "\n".join(sections)
        + "\n</body></html>\n",
        encoding="utf-8",
    )


def write_gateway_index(path: Path) -> None:
    path.write_text(
        """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>External Example Review Gateway</title>
<style>
body { font: 18px/1.5 Georgia, serif; max-width: 820px; margin: 48px auto; padding: 0 24px; background: #eee8da; color: #1c2521; }
main { padding: 24px; border: 2px solid #1e5e53; background: #fffdf6; }
a { color: #174f68; font-weight: bold; }
.warning { padding: 12px; border-left: 5px solid #b94b31; background: #f8e8df; }
</style></head><body><main>
<h1>External Example Review Gateway</h1>
<p>Use the two-stage review order. This package is an external-review
convenience layer, not a runtime installation.</p>
<ol>
  <li><a href="00_PRE_RESULT_INDEX.html">Open the blind PRE_RESULT index</a></li>
  <li>Record the blind read for a state.</li>
  <li><a href="90_POST_RESULT_INDEX.html">Open the POST_RESULT forensic index</a></li>
</ol>
<p class="warning"><strong>Boundary:</strong> The second index reveals outcomes.
Do not open it before completing the blind pass.</p>
</main></body></html>
""",
        encoding="utf-8",
    )


def build_bundle(args: argparse.Namespace) -> tuple[Path, Path | None, dict[str, Any]]:
    analysis_date = str(args.analysis_date)
    index_path = repo_path(args.brain1_index)
    winner_root = repo_path(
        args.winner_root
        or REPO_ROOT / "sharepacks/_truth_rpattern_fixed" / analysis_date
    )
    replay_root = repo_path(
        args.replay_root
        or REPO_ROOT / "sharepacks/_replay_rpattern_current" / analysis_date
    )
    aux_core_root = repo_path(args.aux_core_root)
    output_dir = repo_path(args.output_dir)
    if output_dir.exists():
        raise FileExistsError(f"Output already exists: {output_dir}")

    rows = load_rows(index_path, analysis_date)
    states = sorted({str(row["state_key"]) for row in rows})
    expected_outcomes = len(states) * 2
    if len(rows) != expected_outcomes:
        raise RuntimeError(
            f"Expected two outcomes for {len(states)} states; found {len(rows)}"
        )

    aux_manifest_path = aux_core_root / "MANIFEST.json"
    if not aux_manifest_path.is_file():
        raise FileNotFoundError(aux_manifest_path)
    aux_manifest = json.loads(aux_manifest_path.read_text(encoding="utf-8"))
    if aux_manifest.get("errors"):
        raise RuntimeError(
            f"AUX CORE manifest contains errors: {aux_manifest['errors']}"
        )
    aux_states = {
        str(item["state_key"]) for item in aux_manifest.get("states") or []
    }
    missing_aux_states = sorted(set(states) - aux_states)
    if missing_aux_states:
        raise RuntimeError(
            f"AUX CORE manifest is missing states: {missing_aux_states}"
        )

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=f".{output_dir.name}.",
        dir=output_dir.parent,
    ) as temp_dir:
        stage = Path(temp_dir) / output_dir.name
        stage.mkdir()
        artifacts: list[dict[str, Any]] = []

        def record_artifact(
            *,
            state: str,
            zone: str,
            order: int,
            label: str,
            output_path: Path,
            claim_class: str,
            source_paths: Sequence[Path],
            period: str = "",
            winner: str = "",
            extra: Mapping[str, Any] | None = None,
        ) -> None:
            entry = {
                "state": state,
                "zone": zone,
                "order": order,
                "period": period,
                "winner": winner,
                "label": label,
                "output_path": output_path.relative_to(stage).as_posix(),
                "output_sha256": sha256(output_path),
                "claim_class": claim_class,
                "source_paths": [relative(path) for path in source_paths],
                "source_sha256": {
                    relative(path): sha256(path) for path in source_paths
                },
            }
            if extra:
                entry.update(dict(extra))
            artifacts.append(entry)

        rows_by_state = {
            state: [row for row in rows if str(row["state_key"]) == state]
            for state in states
        }
        for state in states:
            state_rows = sorted(
                rows_by_state[state],
                key=lambda row: PERIOD_ORDER[str(row["period"])],
            )
            state_dir = stage / state
            pre_dir = state_dir / "PRE_RESULT"
            post_dir = state_dir / "POST_RESULT"
            pre_dir.mkdir(parents=True)
            post_dir.mkdir()
            write_state_guide(state_dir / "00_STATE_GUIDE.md", state=state)

            table_sources = {
                variant: replay_root
                / state
                / "tables"
                / f"{variant}_Combined.csv"
                for variant in TABLE_VARIANTS
            }
            for source in table_sources.values():
                if not source.is_file():
                    raise FileNotFoundError(source)
            pre_table_output = (
                pre_dir
                / "01_STRING_TABLES__THREE_VARIANT__PRE_RESULT.html"
            )
            table_receipt = render_pre_result_tables(
                state=state,
                table_sources=table_sources,
                output_path=pre_table_output,
            )
            record_artifact(
                state=state,
                zone="PRE_RESULT",
                order=1,
                label="Three-Variant Frozen String Tables",
                output_path=pre_table_output,
                claim_class=str(table_receipt["claim_class"]),
                source_paths=[
                    table_sources[variant] for variant in TABLE_VARIANTS
                ],
                extra={"table_receipt": table_receipt},
            )

            dr_root = replay_root / state / "digit_reduction" / state
            dr_full_source = dr_root / f"{state}_digit_reduction_report_stacked.html"
            dr_training_source = one_match(
                sorted((dr_root / "training").glob("*_digit_reduction_log*.json")),
                f"Digit Reduction training log for {state}",
            )
            full_dr_output = (
                pre_dir
                / "02_DIGIT_REDUCTION__FULL_LADDER__PRE_RESULT.html"
            )
            copy_verified(dr_full_source, full_dr_output)
            record_artifact(
                state=state,
                zone="PRE_RESULT",
                order=2,
                label="Digit Reduction Full Ladder",
                output_path=full_dr_output,
                claim_class="FROZEN_PRE_RESULT_ANALYZER_VIEW",
                source_paths=[dr_full_source],
            )

            for order, period in ((3, "Midday"), (4, "Evening")):
                dr_period_source = (
                    dr_root
                    / "analyzer_v2"
                    / f"{state}_stacked_{period.lower()}.html"
                )
                dr_period_output = (
                    pre_dir
                    / f"0{order}_DIGIT_REDUCTION__{period.upper()}"
                    "__PRE_RESULT.html"
                )
                copy_verified(dr_period_source, dr_period_output)
                record_artifact(
                    state=state,
                    zone="PRE_RESULT",
                    order=order,
                    period=period,
                    label="Digit Reduction Analyzer",
                    output_path=dr_period_output,
                    claim_class="FROZEN_PRE_RESULT_ANALYZER_VIEW",
                    source_paths=[dr_period_source],
                )

            aux_state_root = aux_core_root / "states" / state
            aux_pre_source = aux_state_root / "AUX_CORE__FULL_PRE_RESULT.md"
            aux_pre_output = pre_dir / "05_AUX_CORE__FULL_PRE_RESULT.md"
            copy_verified(aux_pre_source, aux_pre_output)
            record_artifact(
                state=state,
                zone="PRE_RESULT",
                order=5,
                label="AUX CORE Full Ten-Block Report",
                output_path=aux_pre_output,
                claim_class="FROZEN_PRE_RESULT_AUX_CORE_PROJECTION",
                source_paths=[aux_pre_source],
            )

            for row in state_rows:
                period = str(row["period"])
                winner = str(row["winner"]).zfill(3)
                joined_row = {
                    **row,
                    "winner": winner,
                    "analysis_date": analysis_date,
                }
                winner_source = one_match(
                    sorted(
                        (
                            winner_root / state / "winners" / state
                        ).glob(
                            f"{state}_vtrac*_winner_{winner}"
                            "_FIXED_R_PATTERN_V1.html"
                        )
                    ),
                    f"fixed winner HTML for {state} {period} {winner}",
                )
                aux_post_source = (
                    aux_state_root / f"AUX_CORE__{period}__{winner}.md"
                )
                for source in (
                    winner_source,
                    dr_full_source,
                    dr_training_source,
                    aux_post_source,
                ):
                    if not source.is_file():
                        raise FileNotFoundError(source)

                prefix = f"{period}__{winner}"
                winner_output = (
                    post_dir
                    / f"{prefix}__01_STRING_TABLE_WINNER_FORENSIC.html"
                )
                dr_overlay_output = (
                    post_dir
                    / f"{prefix}__02_DR_FULL_LADDER_WINNER_OVERLAY.html"
                )
                aux_post_output = (
                    post_dir / f"{prefix}__03_AUX_CORE_POST_RESULT.md"
                )
                winner_zone_overlay = write_zone_annotated_copy(
                    winner_source, winner_output
                )
                overlay_summary = build_full_ladder_overlay(
                    joined_row,
                    source_report=dr_full_source,
                    source_training=dr_training_source,
                    output_path=dr_overlay_output,
                )
                copy_verified(aux_post_source, aux_post_output)

                record_artifact(
                    state=state,
                    zone="POST_RESULT",
                    order=1,
                    period=period,
                    winner=winner,
                    label="String-Table Winner/VTRAC Forensic",
                    output_path=winner_output,
                    claim_class="POST_RESULT_STRING_TABLE_FORENSIC",
                    source_paths=[winner_source],
                    extra={"zone_overlay": winner_zone_overlay},
                )
                record_artifact(
                    state=state,
                    zone="POST_RESULT",
                    order=2,
                    period=period,
                    winner=winner,
                    label="Digit Reduction Full-Ladder Winner Overlay",
                    output_path=dr_overlay_output,
                    claim_class="POST_RESULT_WINNER_FORENSIC",
                    source_paths=[dr_full_source, dr_training_source],
                    extra={"overlay_summary": overlay_summary},
                )
                record_artifact(
                    state=state,
                    zone="POST_RESULT",
                    order=3,
                    period=period,
                    winner=winner,
                    label="AUX CORE Result Join",
                    output_path=aux_post_output,
                    claim_class="POST_RESULT_AUX_CORE_FORENSIC",
                    source_paths=[aux_post_source],
                )

        pre_artifacts = [
            item for item in artifacts if item["zone"] == "PRE_RESULT"
        ]
        post_artifacts = [
            item for item in artifacts if item["zone"] == "POST_RESULT"
        ]
        for artifact in pre_artifacts:
            if artifact["winner"]:
                raise RuntimeError(
                    f"Pre-result artifact contains a winner field: {artifact}"
                )
            path_parts = Path(str(artifact["output_path"])).parts
            if "PRE_RESULT" not in path_parts:
                raise RuntimeError(
                    f"Pre-result artifact is outside PRE_RESULT: {artifact}"
                )
        for artifact in post_artifacts:
            if not artifact["winner"]:
                raise RuntimeError(
                    f"Post-result artifact lacks a winner field: {artifact}"
                )
            path_parts = Path(str(artifact["output_path"])).parts
            if "POST_RESULT" not in path_parts:
                raise RuntimeError(
                    f"Post-result artifact is outside POST_RESULT: {artifact}"
                )

        write_start_here(
            stage / "00_START_HERE.md",
            analysis_date=analysis_date,
            state_count=len(states),
            outcome_count=len(rows),
        )
        write_gateway_index(stage / "00_REVIEW_INDEX.html")
        write_zone_index(
            stage / "00_PRE_RESULT_INDEX.html",
            artifacts,
            zone="PRE_RESULT",
        )
        write_zone_index(
            stage / "90_POST_RESULT_INDEX.html",
            artifacts,
            zone="POST_RESULT",
        )

        manifest = {
            "schema_version": "primary_extraction_zone_review_bundle_v2",
            "analysis_date": analysis_date,
            "generated_at": datetime.now(UTC).isoformat(timespec="seconds"),
            "state_count": len(states),
            "outcome_count": len(rows),
            "artifact_count": len(artifacts),
            "pre_result_artifact_count": len(pre_artifacts),
            "post_result_artifact_count": len(post_artifacts),
            "source_lane": "R_PATTERN_V1 corrected replay",
            "brain1_index": {
                "path": relative(index_path),
                "sha256": sha256(index_path),
            },
            "winner_root": relative(winner_root),
            "digit_reduction_root": relative(replay_root),
            "aux_core_manifest": {
                "path": relative(aux_manifest_path),
                "sha256": sha256(aux_manifest_path),
            },
            "states": states,
            "artifacts": artifacts,
            "claim_boundary": (
                "PRE_RESULT contains frozen evidence views with no joined target. "
                "POST_RESULT contains outcome-aware reverse-engineering artifacts "
                "and receives zero predictive credit. This package changes no "
                "runtime behavior."
            ),
        }
        (stage / "MANIFEST.json").write_text(
            json.dumps(manifest, indent=2),
            encoding="utf-8",
        )
        csv_fields = [
            "state",
            "zone",
            "order",
            "period",
            "winner",
            "label",
            "output_path",
            "output_sha256",
            "claim_class",
            "source_paths",
            "source_sha256",
        ]
        with (stage / "MANIFEST.csv").open(
            "w",
            encoding="utf-8",
            newline="",
        ) as handle:
            writer = csv.DictWriter(handle, fieldnames=csv_fields)
            writer.writeheader()
            for artifact in artifacts:
                csv_row = {
                    field: artifact.get(field, "") for field in csv_fields
                }
                csv_row["source_paths"] = json.dumps(
                    artifact["source_paths"],
                    separators=(",", ":"),
                )
                csv_row["source_sha256"] = json.dumps(
                    artifact["source_sha256"],
                    sort_keys=True,
                    separators=(",", ":"),
                )
                writer.writerow(csv_row)

        shutil.move(str(stage), str(output_dir))

    archive_path: Path | None = None
    if not args.no_zip:
        archive_path = Path(
            shutil.make_archive(
                str(output_dir),
                "zip",
                root_dir=output_dir.parent,
                base_dir=output_dir.name,
            )
        )

    return output_dir, archive_path, manifest


def main() -> int:
    args = parse_args()
    output_dir, archive_path, manifest = build_bundle(args)
    print(f"bundle={relative(output_dir)}")
    if archive_path:
        print(f"zip={relative(archive_path)}")
    print(f"states={manifest['state_count']}")
    print(f"outcomes={manifest['outcome_count']}")
    print(f"artifacts={manifest['artifact_count']}")
    print(f"pre_result={manifest['pre_result_artifact_count']}")
    print(f"post_result={manifest['post_result_artifact_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
