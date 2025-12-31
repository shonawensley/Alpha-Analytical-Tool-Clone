"""
Summarize V-TRAC sharepack outputs into Markdown/JSON with source labels.

Usage:
  python3 scripts/tools/vtrac_sharepack_summary.py --sharepack sharepacks/2025-06-21/OntarioCanada4/vtrac/OntarioCanada4 [--md-out out.md] [--json-out out.json]

What it does:
  - Reads enhanced analyzer bundle JSON (<STATE>_vtrac_enhanced_*.json) and validation_report.{json,md} if present.
  - Reports top indices and straights with scores + evidence features (source: enhanced JSON).
  - Reports per-section summaries (hot/superhot, consensus, stable columns, ring votes, analyzer metrics).
  - If winners artifacts exist in the sibling winners sharepack folder, includes a winners lens summary
    (source: winners VTRAC report JSON/HTML), keeping brain vs winners provenance explicit.
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List, Optional


def load_enhanced_json(sharepack: Path) -> Dict:
    files = sorted(sharepack.glob("*_vtrac_enhanced_*.json"))
    if not files:
        raise SystemExit("No enhanced vtrac JSON found in sharepack")
    return json.loads(files[-1].read_text())

def load_winners_lens(winners_dir: Path) -> Optional[List[Dict]]:
    """Load latest winners VTRAC report JSONs per winner_combo if present."""
    if not winners_dir.exists():
        return None
    json_files = sorted(winners_dir.glob("*_vtrac*_winner_*.json"))
    if not json_files:
        return None
    # Pick the most recent JSON per winner_combo based on embedded timestamp
    by_winner: Dict[str, Dict] = {}
    for jf in json_files:
        data = json.loads(jf.read_text())
        winner = str(data.get("winner_combo"))
        ts = data.get("timestamp") or jf.stem.split("_")[-1]
        current = by_winner.get(winner)
        if current is None or str(ts) > str(current.get("timestamp", "")):
            by_winner[winner] = {**data, "_file": jf.name}
    return list(by_winner.values())


def make_markdown(
    state: str,
    stamp: str,
    top_indices: List[Dict],
    top_straights: List[str],
    section_summaries: Dict,
    indices_ranked: List[Dict],
    winners_lens: Optional[List[Dict]] = None,
) -> str:
    lines: List[str] = []
    lines.append(f"# V-TRAC Summary — {state} (stamp {stamp})")
    lines.append("\n## Top indices (from enhanced JSON)")
    for entry in top_indices:
        idx = entry.get("index")
        score = entry.get("score")
        feats = entry.get("evidence", {}).get("features", [])
        why = ", ".join([f"{f['name']}={f['value']}" for f in feats[:4]])  # show first few features
        lines.append(f"- index {idx} | score {score} | features: {why}")
    lines.append("\n## Top straights (from enhanced JSON)")
    lines.append(", ".join(top_straights[:10]))
    lines.append("\n## Section summaries")
    for sec, summary in section_summaries.items():
        lines.append(f"- {sec}: hot={summary.get('hot_count')} superhot={summary.get('superhot_count')} consensus_col1={summary.get('consensus_col1')} consensus_col2={summary.get('consensus_col2')}")
    if winners_lens:
        lines.append("\n## Winners lens (from winners VTRAC report JSON/HTML)")
        for w in winners_lens:
            lens_rank = w.get("rank")
            lens_score = w.get("score")
            lines.append(
                f"- winner {w.get('winner_combo')} | index {w.get('index')} | file {w.get('_file')} | "
                f"rank {lens_rank} score {lens_score} | stats keys: {', '.join((w.get('stats') or {}).keys())}"
            )
        lines.append("\n## Winner index placement (in enhanced JSON rankings)")
        idx_pos = {e.get("index"): i for i, e in enumerate(indices_ranked)}
        top_index_score = None
        if indices_ranked:
            try:
                top_index_score = float(indices_ranked[0].get("score") or 0)
            except Exception:
                top_index_score = None
        for w in winners_lens:
            idx = w.get("index")
            winner_combo = str(w.get("winner_combo"))
            if idx not in idx_pos:
                lines.append(f"- winner {winner_combo} | index {idx}: not found in indices_ranked")
                continue
            entry = indices_ranked[idx_pos[idx]]
            rank = idx_pos[idx] + 1
            score = entry.get("score")
            rank_fraction = float(rank) / float(len(indices_ranked)) if indices_ranked else None
            score_ratio = None
            score_delta = None
            try:
                if score is not None and top_index_score not in (None, 0):
                    score_ratio = float(score) / float(top_index_score)
                    score_delta = float(top_index_score) - float(score)
            except Exception:
                score_ratio = None
                score_delta = None
            straights = entry.get("straights") or []
            in_straights = any(
                isinstance(s, dict) and str(s.get("straight")) == winner_combo for s in straights
            )
            top_s = []
            for s in sorted(
                [s for s in straights if isinstance(s, dict)],
                key=lambda x: x.get("score", 0),
                reverse=True,
            )[:3]:
                try:
                    top_s.append(f"{s.get('straight')} ({round(float(s.get('score', 0)), 3)})")
                except Exception:
                    top_s.append(f"{s.get('straight')} ({s.get('score')})")
            top_s_str = ", ".join(top_s) if top_s else "(none)"
            lines.append(
                f"- winner {winner_combo} | index {idx} rank {rank}/{len(indices_ranked)} (rank_frac {rank_fraction}) | "
                f"score {score} (top {top_index_score}, ratio {score_ratio}, delta {score_delta}) | "
                f"winner_in_index_straights={in_straights} | top_index_straights: {top_s_str}"
            )
        lines.append("  - Note: winners lens lives under the winners sharepack and is generated post-results.")
    else:
        lines.append("\n## Winners lens")
        lines.append("- No winners VTRAC report JSONs found alongside this analyzer sharepack.")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sharepack", required=True, help="Path to vtrac/<STATE>/<STATE> sharepack folder")
    ap.add_argument("--md-out", help="Markdown output path")
    ap.add_argument("--json-out", help="JSON output path")
    ap.add_argument("--top-n", type=int, default=10, help="Top N indices/straights to show")
    args = ap.parse_args()

    sharepack = Path(args.sharepack)
    # sharepack path: sharepacks/<DATE>/<STATE>/vtrac/<STATE>
    state_name = sharepack.parents[1].name if len(sharepack.parents) >= 2 else sharepack.name
    date_dir = sharepack.parents[2] if len(sharepack.parents) >= 3 else None
    enhanced = load_enhanced_json(sharepack)
    stamp = enhanced.get("timestamp", "")

    indices_ranked = enhanced.get("indices_ranked", [])
    top_indices = indices_ranked[: args.top_n]
    top_straights = enhanced.get("top_straights", [])[: args.top_n]
    section_summaries = enhanced.get("section_summaries", {})

    winners_lens = None
    if date_dir is not None:
        winners_dir = date_dir / state_name / "winners" / state_name
        winners_lens = load_winners_lens(winners_dir)

    md = make_markdown(
        state_name,
        stamp,
        top_indices,
        top_straights,
        section_summaries,
        indices_ranked=indices_ranked,
        winners_lens=winners_lens,
    )
    if args.md_out:
        Path(args.md_out).write_text(md)
    if args.json_out:
        winners_digest = None
        winner_index_placements = None
        if winners_lens:
            winners_digest = []
            idx_pos = {e.get("index"): i for i, e in enumerate(indices_ranked)}
            top_index_score = None
            if indices_ranked:
                try:
                    top_index_score = float(indices_ranked[0].get("score") or 0)
                except Exception:
                    top_index_score = None

            winner_index_placements = []
            for w in winners_lens:
                winner_combo = str(w.get("winner_combo"))
                idx = w.get("index")
                winners_digest.append(
                    {
                        "winner_combo": winner_combo,
                        "index": idx,
                        "rank": w.get("rank"),
                        "score": w.get("score"),
                        "timestamp": w.get("timestamp"),
                        "file": w.get("_file"),
                        "stats_keys": sorted((w.get("stats") or {}).keys()),
                    }
                )
                if idx in idx_pos:
                    rank = idx_pos[idx] + 1
                    score = indices_ranked[idx_pos[idx]].get("score")
                    rank_fraction = float(rank) / float(len(indices_ranked)) if indices_ranked else None
                    score_ratio = None
                    score_delta = None
                    try:
                        if score is not None and top_index_score not in (None, 0):
                            score_ratio = float(score) / float(top_index_score)
                            score_delta = float(top_index_score) - float(score)
                    except Exception:
                        score_ratio = None
                        score_delta = None
                    winner_index_placements.append(
                        {
                            "winner_combo": winner_combo,
                            "index": idx,
                            "index_rank": rank,
                            "indices_total": len(indices_ranked),
                            "rank_fraction": rank_fraction,
                            "index_score": score,
                            "top_index_score": top_index_score,
                            "score_ratio_to_top": score_ratio,
                            "score_delta_from_top": score_delta,
                        }
                    )

        Path(args.json_out).write_text(
            json.dumps(
                {
                    "state": state_name,
                    "stamp": stamp,
                    "top_indices": top_indices,
                    "top_straights": top_straights,
                    "section_summaries": section_summaries,
                    "winners_lens": winners_digest,
                    "winner_index_placements": winner_index_placements,
                },
                indent=2,
            )
        )
    if not args.md_out:
        print(md)


if __name__ == "__main__":
    main()
