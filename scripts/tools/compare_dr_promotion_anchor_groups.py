#!/usr/bin/env python3
"""Compare DR winner-promotion groups from frozen audit CSVs.

This is diagnostic only. It splits matched winner-aware rows into:

- promoted
- visible_under_promoted
- buried

and emits a markdown summary to guide winner-vs-attractor scoring work.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path
from statistics import median
from typing import Dict, Iterable, List, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS"


def _to_int(value: object, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _to_float(value: object, default: float = 0.0) -> float:
    try:
        text = str(value or "").strip()
        if not text:
            return float(default)
        return float(text)
    except Exception:
        return float(default)


def _load_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _group_name(row: Dict[str, str]) -> Optional[str]:
    if row.get("winner_json_status") != "matched_literal":
        return None
    if _to_int(row.get("vtrac_any"), 0) <= 0:
        return None
    cluster_rank_text = str(row.get("cluster_winner_vtrac_rank") or "").strip()
    best_rank = _to_int(row.get("best_surface_winner_vtrac_rank"), 999)
    if cluster_rank_text:
        cluster_rank = _to_int(cluster_rank_text, 999)
        if cluster_rank <= 5 or best_rank <= 5:
            return "promoted"
        if cluster_rank <= 20:
            return "visible_under_promoted"
    return "buried"


def _top_counter(counter: Counter[str], limit: int = 6) -> List[str]:
    return [f"`{value}` ({count})" for value, count in counter.most_common(limit) if value]


def _median_text(values: Iterable[float]) -> str:
    vals = [float(v) for v in values]
    if not vals:
        return "-"
    return f"{median(vals):.3f}"


def _emit_group(lines: List[str], *, title: str, rows: Sequence[Dict[str, str]]) -> None:
    lines.append(f"## {title}")
    lines.append("")
    if not rows:
        lines.append("_None_")
        lines.append("")
        return

    trace_counter = Counter(str(row.get("top_trace_family_1") or "") for row in rows)
    corridor_counter = Counter(str(row.get("top_corridor_family_1") or "") for row in rows)
    double_counter = Counter(str(row.get("top_double_pattern_1") or "") for row in rows)
    state_counter = Counter(str(row.get("state") or "") for row in rows)
    align_counter = Counter(str(row.get("alignment_class") or "") for row in rows)

    lines.append(f"- rows: `{len(rows)}`")
    lines.append(f"- median signal_score: `{_median_text(_to_float(row.get('winner_json_signal_score')) for row in rows)}`")
    lines.append(f"- median ls_signal_cells: `{_median_text(_to_int(row.get('winner_json_ls_signal_cells')) for row in rows)}`")
    lines.append(f"- median cluster_score_gap: `{_median_text(_to_float(row.get('cluster_score_gap')) for row in rows if str(row.get('cluster_score_gap') or '').strip())}`")
    lines.append(f"- top states: {', '.join(_top_counter(state_counter, limit=5)) or '-'}")
    lines.append(f"- top alignments: {', '.join(_top_counter(align_counter, limit=4)) or '-'}")
    lines.append(f"- top trace attractors: {', '.join(_top_counter(trace_counter)) or '-'}")
    lines.append(f"- top corridor attractors: {', '.join(_top_counter(corridor_counter)) or '-'}")
    lines.append(f"- top double attractors: {', '.join(_top_counter(double_counter)) or '-'}")
    lines.append("")
    lines.append("| Date | State | Var | Winner | VT | Cluster | Best | Signal | LS | Top corridor | Top double |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for row in sorted(
        rows,
        key=lambda item: (
            _to_int(item.get("cluster_winner_vtrac_rank"), 999),
            -_to_float(item.get("winner_json_signal_score")),
            item.get("date", ""),
            item.get("state", ""),
            item.get("variant", ""),
        ),
    )[:12]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row.get("date") or ""),
                    str(row.get("state") or ""),
                    str(row.get("variant") or ""),
                    str(row.get("winner") or ""),
                    str(row.get("winner_vtrac_index") or ""),
                    str(row.get("cluster_winner_vtrac_rank") or "-"),
                    str(row.get("best_surface_winner_vtrac_rank") or "-"),
                    str(row.get("winner_json_signal_score") or "0"),
                    str(row.get("winner_json_ls_signal_cells") or "0"),
                    str(row.get("top_corridor_family_1") or "-"),
                    str(row.get("top_double_pattern_1") or "-"),
                ]
            )
            + " |"
        )
    lines.append("")


def build_report(*, csv_paths: Sequence[Path], out_md: Path) -> None:
    grouped: Dict[str, List[Dict[str, str]]] = {
        "promoted": [],
        "visible_under_promoted": [],
        "buried": [],
    }
    all_rows: List[Dict[str, str]] = []
    for path in csv_paths:
        rows = _load_rows(path)
        all_rows.extend(rows)
        for row in rows:
            name = _group_name(row)
            if name:
                grouped[name].append(row)

    lines: List[str] = []
    lines.append("# DR Winner Promotion Group Compare")
    lines.append("")
    lines.append("- Purpose: split matched, winner-aware DR rows into promoted vs visible-under-promoted vs buried groups.")
    lines.append("- Inputs:")
    for path in csv_paths:
        lines.append(f"  - `{path}`")
    lines.append("")
    lines.append(f"- total audit rows: `{len(all_rows)}`")
    lines.append(f"- matched + vtrac_any rows: `{sum(len(rows) for rows in grouped.values())}`")
    lines.append("")

    _emit_group(lines, title="Promoted", rows=grouped["promoted"])
    _emit_group(lines, title="Visible Under Promoted", rows=grouped["visible_under_promoted"])
    _emit_group(lines, title="Buried", rows=grouped["buried"])

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Compare DR promotion anchor groups from frozen audit CSVs.")
    ap.add_argument(
        "--csv",
        nargs="+",
        default=[
            str(RUNS_DIR / "2026-03-15__DR_GOLD_DAY_AUDIT__DEV__V1_1.csv"),
            str(RUNS_DIR / "2026-03-15__DR_GOLD_DAY_AUDIT__HOLDOUT__V1_1.csv"),
        ],
    )
    ap.add_argument(
        "--out-md",
        default=str(RUNS_DIR / "2026-03-15__DR_WINNER_PROMOTION_LAB__GROUP_COMPARE.md"),
    )
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    build_report(
        csv_paths=[Path(value) for value in args.csv],
        out_md=Path(args.out_md),
    )
    print(f"report={args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
