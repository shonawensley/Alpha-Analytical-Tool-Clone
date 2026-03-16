#!/usr/bin/env python3
"""Export a compact casepack for the strongest DR promotion-gap anchors.

This is intentionally diagnostic only. It reads the frozen gold-day audit CSVs,
selects rows where DR clearly saw the winner lane but failed to promote it near
the top, and emits a markdown casepack with direct artifact paths for review.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
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


def _resolve_repo_path(raw: str) -> Optional[Path]:
    text = str(raw or "").strip()
    if not text:
        return None
    path = REPO_ROOT / text
    return path if path.exists() else None


def _winner_html_from_json(raw: str) -> Optional[Path]:
    json_path = _resolve_repo_path(raw)
    if json_path is None:
        return None
    html_path = json_path.with_suffix(".html")
    return html_path if html_path.exists() else None


def _is_anchor(row: Dict[str, str], *, cluster_limit: int) -> bool:
    if row.get("winner_json_status") != "matched_literal":
        return False
    if _to_int(row.get("vtrac_any"), 0) <= 0:
        return False
    cluster_rank = _to_int(row.get("cluster_winner_vtrac_rank"), 999)
    if cluster_rank <= cluster_limit:
        return False
    return True


def _sorted_anchors(rows: Sequence[Dict[str, str]], *, cluster_limit: int, limit: int) -> List[Dict[str, str]]:
    anchors = [row for row in rows if _is_anchor(row, cluster_limit=cluster_limit)]
    anchors.sort(
        key=lambda row: (
            -_to_float(row.get("winner_json_signal_score")),
            -_to_int(row.get("winner_json_ls_signal_cells")),
            -_to_int(row.get("winner_json_ls_variants_with_signal")),
            _to_int(row.get("cluster_winner_vtrac_rank"), 999),
            row.get("date", ""),
            row.get("state", ""),
            row.get("variant", ""),
        )
    )
    return anchors[:limit]


def _emit_section(lines: List[str], *, title: str, rows: Sequence[Dict[str, str]]) -> None:
    lines.append(f"## {title}")
    lines.append("")
    if not rows:
        lines.append("_None_")
        lines.append("")
        return
    for row in rows:
        winner_html = _winner_html_from_json(row.get("winner_html_json", ""))
        winner_json = _resolve_repo_path(row.get("winner_html_json", ""))
        overlay_html = _resolve_repo_path(row.get("winner_overlay_html", ""))
        stamp_json = _resolve_repo_path(row.get("winner_stamp_json", ""))
        lines.append(
            f"### {row.get('date','')} / {row.get('state','')} / {row.get('variant','')} / {row.get('winner','')} / VT {row.get('winner_vtrac_index','')}"
        )
        lines.append(
            f"- cluster_rank: `{row.get('cluster_winner_vtrac_rank') or '-'}` ({row.get('cluster_rank_band') or 'unranked'}) | trace: `{row.get('trace_winner_vtrac_rank') or '-'}` | corridor: `{row.get('corridor_winner_vtrac_rank') or '-'}` | gateway: `{row.get('gateway_winner_vtrac_rank') or '-'}` | assigned_box: `{row.get('box_winner_vtrac_rank') or '-'}` ({row.get('box_rank_band') or 'unranked'}) | fusion: `{row.get('fusion_winner_vtrac_rank') or '-'}` ({row.get('fusion_rank_band') or 'unranked'}) | best_visible: `{row.get('best_surface_winner_vtrac_rank') or '-'}` ({row.get('best_surface_rank_band') or 'unranked'})"
        )
        lines.append(
            f"- signal_score: `{row.get('winner_json_signal_score') or '0'}` | ls_signal_cells: `{row.get('winner_json_ls_signal_cells') or '0'}` | ls_variants: `{row.get('winner_json_ls_variants_with_signal') or '0'}` | alignment: `{row.get('alignment_class') or ''}`"
        )
        lines.append(
            f"- attractors: trace `{row.get('top_trace_family_1') or '-'}` | corridor `{row.get('top_corridor_family_1') or '-'}` | double `{row.get('top_double_pattern_1') or '-'}` | cluster_gap `{row.get('cluster_score_gap') or '-'}` | gateway_gap `{row.get('gateway_score_gap') or '-'}` | box_gap `{row.get('box_score_gap') or '-'}` | fusion_gap `{row.get('fusion_score_gap') or '-'}`"
        )
        if winner_html is not None:
            lines.append(f"- winner_html: `{winner_html}`")
        if winner_json is not None:
            lines.append(f"- winner_json: `{winner_json}`")
        if overlay_html is not None:
            lines.append(f"- overlay_html: `{overlay_html}`")
        if stamp_json is not None:
            lines.append(f"- stamp_json: `{stamp_json}`")
        lines.append("")


def build_casepack(
    *,
    dev_csv: Path,
    holdout_csv: Path,
    out_md: Path,
    cluster_limit: int,
    dev_limit: int,
    holdout_limit: int,
) -> None:
    dev_rows = _load_rows(dev_csv)
    holdout_rows = _load_rows(holdout_csv)
    dev_anchors = _sorted_anchors(dev_rows, cluster_limit=cluster_limit, limit=dev_limit)
    holdout_anchors = _sorted_anchors(holdout_rows, cluster_limit=cluster_limit, limit=holdout_limit)

    lines: List[str] = []
    lines.append("# DR Promotion Gap Casepack")
    lines.append("")
    lines.append("- Purpose: review the strongest winner-aware DR promotion misses from the frozen gold-day audits.")
    lines.append(
        f"- Selection rule: `winner_json_status=matched_literal`, `vtrac_any>0`, `cluster_winner_vtrac_rank>{cluster_limit}` or unranked."
    )
    lines.append("- Audit rows now use a broader `top20` instrumentation view, so anchors may be visible-but-under-promoted instead of fully unranked.")
    lines.append(f"- Development anchors: `{len(dev_anchors)}`")
    lines.append(f"- Holdout anchors: `{len(holdout_anchors)}`")
    lines.append("")

    _emit_section(lines, title="Development", rows=dev_anchors)
    _emit_section(lines, title="Holdout", rows=holdout_anchors)

    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Export a DR promotion-gap casepack from frozen audit CSVs.")
    ap.add_argument("--dev-csv", default=str(RUNS_DIR / "2026-03-15__DR_GOLD_DAY_AUDIT__DEV__V1_1.csv"))
    ap.add_argument("--holdout-csv", default=str(RUNS_DIR / "2026-03-15__DR_GOLD_DAY_AUDIT__HOLDOUT__V1_1.csv"))
    ap.add_argument("--out-md", default=str(RUNS_DIR / "2026-03-15__DR_PROMOTION_GAP_CASEPACK.md"))
    ap.add_argument("--cluster-limit", type=int, default=5)
    ap.add_argument("--dev-limit", type=int, default=15)
    ap.add_argument("--holdout-limit", type=int, default=15)
    return ap.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    build_casepack(
        dev_csv=Path(args.dev_csv),
        holdout_csv=Path(args.holdout_csv),
        out_md=Path(args.out_md),
        cluster_limit=int(args.cluster_limit),
        dev_limit=int(args.dev_limit),
        holdout_limit=int(args.holdout_limit),
    )
    print(f"casepack={args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
