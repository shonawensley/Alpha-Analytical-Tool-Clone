"""
Summarize Hot Zones sharepack outputs into Markdown/JSON with source labels.

Usage:
  python3 scripts/tools/hot_zones_sharepack_summary.py --sharepack sharepacks/2025-06-21/OntarioCanada4/hot_zones/OntarioCanada4 [--md-out out.md] [--json-out out.json]

What it does:
  - Reads Hot Zones brain outputs (per_lane.csv, top_lanes.csv, meta.json).
  - Reads winners lens (YYYY-MM-DD_hot_zones_winner_map.json/csv).
  - Attempts to load literal winners from the sibling Stable metrics.json (central results mirror).
    If not found, you may pass --winners \"678,517\" (Midday,Evening).
  - Maps literal→canonical, checks winner presence/rank in top_lanes and per_lane,
    and reports EB/ES/VB/VS-style evidence using per_lane flags.
  - Lists top candidates with evidence tags and coverage gaps.

All facts are labeled by source file so the block can be pasted into Part 2.
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd


def canonical_of_literal(literal: str) -> str:
    return "".join(sorted(str(literal)))


def load_winners_from_stable(date_dir: Path, state: str) -> Optional[Dict[str, str]]:
    metrics_path = date_dir / state / "stable" / state / f"{state}_metrics.json"
    if not metrics_path.exists():
        return None
    metrics = json.loads(metrics_path.read_text())
    winners = metrics.get("winners") or []
    winners = [str(w) for w in winners]
    mapping = {}
    if len(winners) >= 1:
        mapping["Midday"] = winners[0]
    if len(winners) >= 2:
        mapping["Evening"] = winners[1]
    return mapping


def summarize_winner_variant(
    label: str,
    literal: str,
    top_lanes: pd.DataFrame,
    per_lane: pd.DataFrame,
    winner_map: pd.DataFrame,
    winner_map_file_present: bool,
) -> Dict:
    canonical = canonical_of_literal(literal)

    # Rank top_lanes by score_mean desc
    tl = top_lanes.copy()
    tl["rank"] = tl["score_mean"].rank(method="min", ascending=False).astype(int)
    tl_rows = tl[tl["triad"].astype(str).isin([literal, canonical])]
    tl_present = not tl_rows.empty
    best_tl_rank = int(tl_rows["rank"].min()) if tl_present else None

    # Per-lane evidence for this triad
    pl_rows = per_lane[per_lane["triad"].astype(str).isin([literal, canonical])]
    pl_present = not pl_rows.empty
    has_straight = bool(pl_rows.get("has_straight", pd.Series([], dtype=int)).any()) if pl_present else False
    has_vt_straight = bool(pl_rows.get("has_vt_straight", pd.Series([], dtype=int)).any()) if pl_present else False

    # Winner map presence (top-20 lanes snapshot)
    wm_rows = winner_map[winner_map["triad"].astype(str).isin([literal, canonical])]
    wm_present = not wm_rows.empty

    gaps = []
    if not tl_present:
        gaps.append("missing_from_top_lanes")
    if not pl_present:
        gaps.append("missing_from_per_lane")
    if winner_map_file_present and not wm_present:
        gaps.append("winner_not_in_winner_map")
    if not winner_map_file_present:
        gaps.append("winner_map_file_missing")

    return {
        "label": label,
        "literal": literal,
        "canonical": canonical,
        "top_lanes": {"present": tl_present, "best_rank": best_tl_rank, "source": "hot_zones_top_lanes.csv"},
        "per_lane": {"present": pl_present, "has_straight": has_straight, "has_vt_straight": has_vt_straight, "source": "hot_zones_per_lane.csv"},
        "winner_map": {
            "file_present": winner_map_file_present,
            "triad_present": wm_present,
            "source": "hot_zones_winner_map.json/csv",
        },
        "gaps": gaps,
    }


def make_markdown(state: str, date: str, winners_info: List[Dict], top_candidates: pd.DataFrame) -> str:
    lines: List[str] = []
    lines.append(f"# Hot Zones Summary — {state} ({date})")
    for w in winners_info:
        lines.append(f"\n## {w['label']} winner {w['literal']} (canonical {w['canonical']})")
        if w["top_lanes"]["present"]:
            lines.append(f"- Top lanes ({w['top_lanes']['source']}): present, best rank {w['top_lanes']['best_rank']}")
        else:
            lines.append(f"- Top lanes ({w['top_lanes']['source']}): not present")
        if w["per_lane"]["present"]:
            lines.append(f"- Per-lane ({w['per_lane']['source']}): has_straight={w['per_lane']['has_straight']} has_vt_straight={w['per_lane']['has_vt_straight']}")
        else:
            lines.append(f"- Per-lane ({w['per_lane']['source']}): not present")
        lines.append(
            f"- Winner map ({w['winner_map']['source']}): file_present={w['winner_map']['file_present']} | triad_present={w['winner_map']['triad_present']}"
        )
        if w["gaps"]:
            lines.append(f"- Coverage gaps: {', '.join(w['gaps'])}")

    lines.append("\n## Top candidate lanes (hot_zones_top_lanes.csv, Top 10)")
    tc = top_candidates.copy()
    tc["rank"] = tc["score_mean"].rank(method="min", ascending=False).astype(int)
    for _, row in tc.sort_values("score_mean", ascending=False).head(10).iterrows():
        lines.append(
            f"- rank {int(row['rank']):>4} | triad {row['triad']} | vt_triad {row['vt_triad']} | score_mean {row['score_mean']} | tags {row['evidence_tags']}"
        )
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sharepack", required=True, help="Path to hot_zones/<STATE>/<STATE>")
    ap.add_argument("--md-out", help="Markdown output path")
    ap.add_argument("--json-out", help="JSON output path")
    ap.add_argument("--winners", help="Comma-separated literal winners Midday,Evening if stable metrics not available")
    args = ap.parse_args()

    sharepack = Path(args.sharepack)
    # sharepack path: sharepacks/<DATE>/<STATE>/hot_zones/<STATE>
    state_name = sharepack.parents[1].name if len(sharepack.parents) >= 2 else sharepack.name
    date_dir = sharepack.parents[2] if len(sharepack.parents) >= 3 else None

    top_lanes = pd.read_csv(sharepack / f"{state_name}_hot_zones_top_lanes.csv")
    per_lane = pd.read_csv(sharepack / f"{state_name}_hot_zones_per_lane.csv")
    meta = json.loads((sharepack / f"{state_name}_hot_zones_meta.json").read_text())

    date = meta.get("date") or "unknown"

    # winner map list
    winner_map_path_json = sharepack / f"{date}_hot_zones_winner_map.json"
    winner_map_path_csv = sharepack / f"{date}_hot_zones_winner_map.csv"
    winner_map_file_present = winner_map_path_csv.exists() or winner_map_path_json.exists()
    if winner_map_path_csv.exists():
        winner_map_df = pd.read_csv(winner_map_path_csv)
    elif winner_map_path_json.exists():
        winner_map_df = pd.DataFrame(json.loads(winner_map_path_json.read_text()))
    else:
        winner_map_df = pd.DataFrame()

    winners = load_winners_from_stable(date_dir, state_name) if date_dir else None
    if winners is None and args.winners:
        parts = [p.strip() for p in args.winners.split(",") if p.strip()]
        winners = {}
        if len(parts) >= 1:
            winners["Midday"] = parts[0]
        if len(parts) >= 2:
            winners["Evening"] = parts[1]

    winners_info: List[Dict] = []
    if winners:
        for label, literal in winners.items():
            winners_info.append(
                summarize_winner_variant(
                    label,
                    literal,
                    top_lanes,
                    per_lane,
                    winner_map_df,
                    winner_map_file_present=winner_map_file_present,
                )
            )

    md = make_markdown(state_name, date, winners_info, top_lanes)
    if args.md_out:
        Path(args.md_out).write_text(md)
    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(
                {
                    "state": state_name,
                    "date": date,
                    "winners": winners_info,
                },
                indent=2,
                default=lambda o: o.item() if hasattr(o, "item") else str(o),
            )
        )
    if not args.md_out:
        print(md)


if __name__ == "__main__":
    main()
