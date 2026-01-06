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
import re
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd


def canonical_of_literal(literal: str) -> str:
    return "".join(sorted(str(literal)))


def normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


def _results_label_from_state(state_name: str) -> str:
    base = re.sub(r"\d+$", "", state_name or "")
    if base.lower().startswith("ontariocanada"):
        return "Ontario"
    words = re.findall(r"[A-Z][a-z]*|[A-Z]+(?![a-z])", base) or [base]
    return " ".join(words).strip()


def load_winners_from_results(results_date: str, state_name: str) -> Optional[Dict[str, str]]:
    """
    Prefer the tab-structured results file so we preserve Midday vs Evening on one-winner days.
    """
    results_path = Path("data/results") / f"{results_date}.txt"
    if not results_path.exists():
        return None
    target = _results_label_from_state(state_name)

    def norm(label: str) -> str:
        return re.sub(r"[^a-z0-9]+", "", (label or "").lower())

    def first_tri(token: str) -> str | None:
        if not token:
            return None
        direct = re.findall(r"\d{3}", token)
        if direct:
            return direct[0]
        digits = "".join(ch for ch in str(token) if ch.isdigit())
        if len(digits) < 3:
            return None
        if len(digits) == 3:
            return digits
        if len(digits) % 3 != 0:
            return None
        return digits[:3]

    mapping: Dict[str, str] = {}
    for raw in results_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line:
            continue
        header = line.lower()
        if header.startswith(("state", "pick", "midday", "evening")):
            continue
        parts = line.split("\t")
        if not parts:
            continue
        label = parts[0].strip()
        if norm(label) != norm(target):
            continue
        midday = first_tri(parts[1]) if len(parts) >= 2 else None
        evening = first_tri(parts[2]) if len(parts) >= 3 else None
        if midday:
            mapping["Midday"] = midday
        if evening:
            mapping["Evening"] = evening
        return mapping or None
    return None


def load_winners_from_stable(date_dir: Path, state: str) -> Optional[Dict[str, str]]:
    metrics_path = date_dir / state / "stable" / state / f"{state}_metrics.json"
    if not metrics_path.exists():
        return None
    metrics = json.loads(metrics_path.read_text())
    winners = metrics.get("winners") or []
    winners = [normalize_pick3_literal(w) for w in winners]
    winners = [w for w in winners if w]
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
    literal = normalize_pick3_literal(literal)
    canonical = canonical_of_literal(literal)

    # Rank top_lanes by score_mean desc
    tl = top_lanes.copy()
    tl["rank"] = tl["score_mean"].rank(method="min", ascending=False).astype(int)
    rows_total = int(len(tl))
    top_score_mean = float(tl["score_mean"].max()) if rows_total else None
    tl_rows = tl[tl["triad"].astype(str).isin([literal, canonical])]
    tl_present = not tl_rows.empty
    best_tl_rank = int(tl_rows["rank"].min()) if tl_present else None
    winner_score_mean = float(tl_rows["score_mean"].max()) if tl_present else None
    winner_rank_fraction = float(best_tl_rank) / float(rows_total) if best_tl_rank is not None and rows_total else None
    winner_score_ratio_to_top = float(winner_score_mean) / float(top_score_mean) if winner_score_mean is not None and top_score_mean not in (None, 0) else None
    winner_score_delta_from_top = float(top_score_mean) - float(winner_score_mean) if winner_score_mean is not None and top_score_mean is not None else None

    # Per-lane evidence for this triad
    pl_rows = per_lane[per_lane["triad"].astype(str).isin([literal, canonical])]
    pl_present = not pl_rows.empty
    has_straight = bool(pl_rows.get("has_straight", pd.Series([], dtype=int)).any()) if pl_present else False
    has_vt_straight = bool(pl_rows.get("has_vt_straight", pd.Series([], dtype=int)).any()) if pl_present else False

    # Winner map presence (top-20 lanes snapshot)
    wm_rows = winner_map[winner_map["triad"].astype(str).isin([literal, canonical])]
    wm_present = not wm_rows.empty

    gaps = []
    notes: List[str] = []
    if not tl_present:
        gaps.append("missing_from_top_lanes")
    if not pl_present:
        gaps.append("missing_from_per_lane")
    if not winner_map_file_present:
        gaps.append("winner_map_file_missing")
    if winner_map_file_present and not wm_present:
        # Winner map is a top-N snapshot (default limit=20 + guard rows). Absence here is not a pipeline failure.
        if best_tl_rank is not None and best_tl_rank > 20:
            notes.append("winner_not_in_top20_winner_map (expected when winner rank > 20)")
        else:
            notes.append("winner_not_in_top20_winner_map (note: map is a top-20 snapshot)")

    return {
        "label": label,
        "literal": literal,
        "canonical": canonical,
        "top_lanes": {
            "present": tl_present,
            "best_rank": best_tl_rank,
            "rows_total": rows_total,
            "winner_rank_fraction": winner_rank_fraction,
            "winner_score_mean": winner_score_mean,
            "top_score_mean": top_score_mean,
            "winner_score_ratio_to_top": winner_score_ratio_to_top,
            "winner_score_delta_from_top": winner_score_delta_from_top,
            "source": "hot_zones_top_lanes.csv",
        },
        "per_lane": {"present": pl_present, "has_straight": has_straight, "has_vt_straight": has_vt_straight, "source": "hot_zones_per_lane.csv"},
        "winner_map": {
            "file_present": winner_map_file_present,
            "triad_present": wm_present,
            "scope": "top20+guard_hits",
            "limit": 20,
            "source": "hot_zones_winner_map.json/csv",
        },
        "gaps": gaps,
        "notes": notes,
    }


def make_markdown(state: str, date: str, winners_info: List[Dict], top_candidates: pd.DataFrame) -> str:
    lines: List[str] = []
    lines.append(f"# Hot Zones Summary — {state} ({date})")
    for w in winners_info:
        lines.append(f"\n## {w['label']} winner {w['literal']} (canonical {w['canonical']})")
        if w["top_lanes"]["present"]:
            lines.append(
                f"- Top lanes ({w['top_lanes']['source']}): present | rank {w['top_lanes']['best_rank']}/{w['top_lanes'].get('rows_total')} "
                f"(rank_frac {w['top_lanes'].get('winner_rank_fraction')}) | "
                f"score_mean {w['top_lanes'].get('winner_score_mean')} (top {w['top_lanes'].get('top_score_mean')}, "
                f"ratio {w['top_lanes'].get('winner_score_ratio_to_top')}, delta {w['top_lanes'].get('winner_score_delta_from_top')})"
            )
        else:
            lines.append(f"- Top lanes ({w['top_lanes']['source']}): not present")
        if w["per_lane"]["present"]:
            lines.append(f"- Per-lane ({w['per_lane']['source']}): has_straight={w['per_lane']['has_straight']} has_vt_straight={w['per_lane']['has_vt_straight']}")
        else:
            lines.append(f"- Per-lane ({w['per_lane']['source']}): not present")
        lines.append(
            f"- Winner map ({w['winner_map']['source']}): file_present={w['winner_map']['file_present']} | triad_present={w['winner_map']['triad_present']} "
            f"(scope {w['winner_map'].get('scope')}, limit {w['winner_map'].get('limit')})"
        )
        if w["gaps"]:
            lines.append(f"- Coverage gaps: {', '.join(w['gaps'])}")
        if w.get("notes"):
            lines.append(f"- Notes: {', '.join(w['notes'])}")

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

    top_lanes = pd.read_csv(sharepack / f"{state_name}_hot_zones_top_lanes.csv", dtype={"triad": str})
    top_lanes["triad"] = top_lanes["triad"].map(normalize_pick3_literal)
    per_lane = pd.read_csv(sharepack / f"{state_name}_hot_zones_per_lane.csv", dtype={"triad": str})
    per_lane["triad"] = per_lane["triad"].map(normalize_pick3_literal)
    meta = json.loads((sharepack / f"{state_name}_hot_zones_meta.json").read_text())

    date = meta.get("date") or "unknown"

    # winner map list
    winner_map_path_json = sharepack / f"{date}_hot_zones_winner_map.json"
    winner_map_path_csv = sharepack / f"{date}_hot_zones_winner_map.csv"
    winner_map_file_present = winner_map_path_csv.exists() or winner_map_path_json.exists()
    if winner_map_path_csv.exists():
        winner_map_df = pd.read_csv(winner_map_path_csv, dtype={"triad": str})
    elif winner_map_path_json.exists():
        winner_map_df = pd.DataFrame(json.loads(winner_map_path_json.read_text()))
    else:
        winner_map_df = pd.DataFrame()

    if not winner_map_df.empty and "triad" in winner_map_df.columns:
        winner_map_df["triad"] = winner_map_df["triad"].map(normalize_pick3_literal)

    results_date = date_dir.name if date_dir else date
    winners = load_winners_from_results(results_date, state_name) if date_dir else None
    if winners is None and date_dir:
        winners = load_winners_from_stable(date_dir, state_name)
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
