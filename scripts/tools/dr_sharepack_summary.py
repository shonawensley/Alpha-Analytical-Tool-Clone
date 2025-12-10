"""
Summarize Digit Reduction outputs from a sharepack into Markdown/JSON with source labels.

Usage:
  python3 scripts/tools/dr_sharepack_summary.py --sharepack sharepacks/2025-06-21/OntarioCanada4/digit_reduction/OntarioCanada4 [--md-out out.md] [--json-out out.json]

What it does:
  - Maps winners (Midday/Evening/Combined) from the winner_flags/hits to literal + canonical.
  - Reads analyzer_v2 per_item/top/meta, winner_flags/hits/map/overlay, reducer scores/report (if present).
  - Reports winner evidence/ranks with explicit source labels.
  - Lists top candidates and coverage gaps (missing flags/hits) per variant.
  - Emits Markdown for Part 2 (paste under step 0) and optional JSON.

Notes:
  - Assumes the sharepack follows the DR lean outputs contract (analyzer_v2/*, winners/*, reducer scores/report).
  - Skips GA/TX/WV if they lack tables (handled by caller).
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List

import pandas as pd


def canonical_of_literal(literal: str) -> str:
    return "".join(sorted(str(literal)))


def read_flags_hits(root: Path, stamp: str, variant: str) -> Dict[str, pd.DataFrame]:
    winners_dir = root / "analyzer_v2" / "winners"
    flags = pd.read_csv(winners_dir / f"{stamp}_{variant}_winner_flags.csv")
    hits = pd.read_csv(winners_dir / f"{stamp}_{variant}_winner_hits.csv")
    return {"flags": flags, "hits": hits}


def detect_latest_stamp(winners_dir: Path) -> str:
    stamps = sorted({p.name.split("_")[0] for p in winners_dir.glob("*_winner_flags.csv")})
    if not stamps:
        raise SystemExit("No winner_flags found in sharepack winners/")
    return stamps[-1]


def summarize_variant(
    variant: str,
    per_item: pd.DataFrame,
    top: pd.DataFrame,
    flags: pd.DataFrame,
    hits: pd.DataFrame,
    reducer_scores: pd.DataFrame = None,
) -> Dict:
    # Winner literal from flags: assume dr_win_exact/dr_win_vtrac rows contain the literal in final_value/hits
    literal = None
    if "winner_literal" in flags.columns:
        literal = str(flags["winner_literal"].iloc[0])
    elif "final_value" in hits.columns:
        literal = str(hits["final_value"].iloc[0])
    else:
        literal = "unknown"
    canonical = canonical_of_literal(literal)

    # Flags summary (4 criteria)
    flags_sum = {
        "rows": len(flags),
        "dr_win_exact": int(flags.get("dr_win_exact", pd.Series([], dtype=int)).sum()),
        "dr_win_vtrac": int(flags.get("dr_win_vtrac", pd.Series([], dtype=int)).sum()),
        "dr_win_vt_boxed": int(flags.get("dr_win_vt_boxed", pd.Series([], dtype=int)).sum()),
        "dr_win_vt_straight": int(flags.get("dr_win_vt_straight", pd.Series([], dtype=int)).sum()),
        "source": "winner_flags.csv",
    }

    # Hits summary (final_* fields)
    hits_rows = hits[hits["final_value"].astype(str) == literal]
    hits_sum = {
        "rows": len(hits_rows),
        "final_exact_match": int(hits_rows.get("final_exact_match", pd.Series([], dtype=int)).sum()),
        "final_vtrac_match": int(hits_rows.get("final_vtrac_match", pd.Series([], dtype=int)).sum()),
        "final_vt_boxed": int(hits_rows.get("final_vt_boxed", pd.Series([], dtype=int)).sum()),
        "final_vt_straight": int(hits_rows.get("final_vt_straight", pd.Series([], dtype=int)).sum()),
        "source": "winner_hits.csv",
    }

    # per_item evidence
    pi_rows = pd.DataFrame()
    if "best_pattern" in per_item.columns:
        pi_rows = per_item[per_item["best_pattern"].astype(str).str.contains(canonical, na=False)]
    elif "box_id" in per_item.columns:
        pi_rows = per_item[per_item["box_id"].astype(str).str.contains(canonical, na=False)]
    pi_present = not pi_rows.empty
    pi_best_rank = int(pi_rows["area_rank"].min()) if pi_present else None

    # top candidates
    top_rows = top[top["best_pattern"].astype(str).str.contains(canonical, na=False)] if "best_pattern" in top.columns else pd.DataFrame()
    top_present = not top_rows.empty
    top_best_rank = int(top_rows["rank"].min()) if top_present else None

    # Reducer scores (optional)
    reducer_present = reducer_scores is not None and not reducer_scores.empty

    gaps = []
    if flags_sum["rows"] == 0:
        gaps.append("missing_flags")
    if hits_sum["rows"] == 0:
        gaps.append("missing_hits")
    if not pi_present:
        gaps.append("missing_per_item")
    if not top_present:
        gaps.append("missing_top")

    return {
        "variant": variant,
        "literal": literal,
        "canonical": canonical,
        "flags": flags_sum,
        "hits": hits_sum,
        "per_item": {"present": pi_present, "best_area_rank": pi_best_rank, "source": "analyzer_v2_per_item.csv"},
        "top": {"present": top_present, "best_rank": top_best_rank, "source": "analyzer_v2_top_candidates.csv"},
        "reducer_present": reducer_present,
        "gaps": gaps,
    }


def top_list(df: pd.DataFrame, cols: List[str], score_col: str, top_n: int) -> List[Dict]:
    out = []
    df_sorted = df.sort_values(score_col, ascending=False).head(top_n)
    for _, row in df_sorted.iterrows():
        item = {}
        for col in cols:
            val = row[col]
            if hasattr(val, "item"):
                val = val.item()
            item[col] = val
        out.append(item)
    return out


def make_markdown(state: str, stamp: str, variants: List[Dict], top_items: List[Dict], top_top: List[Dict]) -> str:
    lines: List[str] = []
    lines.append(f"# Digit Reduction Summary — {state} (stamp {stamp})")
    for v in variants:
        lines.append(f"\n## {v['variant']} winner {v['literal']} (canonical {v['canonical']})")
        lines.append(f"- Flags ({v['flags']['source']}): rows={v['flags']['rows']} | exact={v['flags']['dr_win_exact']} | vtrac={v['flags']['dr_win_vtrac']} | vt_boxed={v['flags']['dr_win_vt_boxed']} | vt_straight={v['flags']['dr_win_vt_straight']}")
        lines.append(f"- Hits ({v['hits']['source']}): rows={v['hits']['rows']} | exact={v['hits']['final_exact_match']} | vtrac={v['hits']['final_vtrac_match']} | vt_boxed={v['hits']['final_vt_boxed']} | vt_straight={v['hits']['final_vt_straight']}")
        if v["per_item"]["present"]:
            lines.append(f"- Per-item ({v['per_item']['source']}): best area_rank={v['per_item']['best_area_rank']}")
        else:
            lines.append(f"- Per-item ({v['per_item']['source']}): not present")
        if v["top"]["present"]:
            lines.append(f"- Top candidates ({v['top']['source']}): best rank={v['top']['best_rank']}")
        else:
            lines.append(f"- Top candidates ({v['top']['source']}): not present")
        lines.append(f"- Reducer scores present: {v['reducer_present']}")
        if v["gaps"]:
            lines.append(f"- Coverage gaps: {', '.join(v['gaps'])}")
    lines.append("\n## Top per_item (analyzer_v2_per_item.csv)")
    for row in top_items:
        lines.append(f"- rank {row['area_rank']:>4} | pattern {row.get('best_pattern', row.get('box_id',''))} | variant {row.get('variant','')} | score_v2 {row.get('score_v2','')} | evidence {row.get('match_types','')}")
    lines.append("\n## Top candidates (analyzer_v2_top_candidates.csv)")
    for row in top_top:
        lines.append(f"- rank {row['rank']:>4} | pattern {row.get('best_pattern','')} | variant {row.get('variant','')} | score {row.get('score','')} | tags {row.get('evidence_tags','')}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sharepack", required=True, help="Path to digit_reduction/<STATE>/<STATE>")
    ap.add_argument("--md-out", help="Markdown output path")
    ap.add_argument("--json-out", help="JSON output path")
    ap.add_argument("--top-n", type=int, default=10, help="Top N rows to show for per_item/top")
    args = ap.parse_args()

    sharepack = Path(args.sharepack)
    state_name = sharepack.parent.name if sharepack.parent else sharepack.name

    per_item = pd.read_csv(sharepack / "analyzer_v2" / f"{sharepack.name}_analyzer_v2_per_item.csv")
    top = pd.read_csv(sharepack / "analyzer_v2" / f"{sharepack.name}_analyzer_v2_top_candidates.csv")
    winners_dir = sharepack / "analyzer_v2" / "winners"
    stamp = detect_latest_stamp(winners_dir)

    variants = []
    for variant in ["Midday", "Evening", "Combined"]:
        flags_hits = read_flags_hits(sharepack, stamp, variant)
        reducer_scores = pd.read_csv(sharepack / f"{sharepack.name}_digit_reduction_scores.csv")
        variants.append(
            summarize_variant(
                variant=variant,
                per_item=per_item,
                top=top,
                flags=flags_hits["flags"],
                hits=flags_hits["hits"],
                reducer_scores=reducer_scores,
            )
        )

    # Derive pattern/variant columns for per_item if missing
    if "best_pattern" in per_item.columns:
        pattern_col = "best_pattern"
    else:
        per_item["best_pattern"] = per_item["box_id"]
        pattern_col = "best_pattern"
    if "variant" not in per_item.columns:
        per_item["variant"] = ""
    if "match_types" not in per_item.columns:
        per_item["match_types"] = ""
    if "score_v2" not in per_item.columns:
        per_item["score_v2"] = per_item.get("score", 0)

    if "variant" not in top.columns:
        top["variant"] = ""
    if "evidence_tags" not in top.columns:
        top["evidence_tags"] = ""

    top_items = top_list(per_item, ["area_rank", pattern_col, "variant", "score_v2", "match_types"], "area_rank", args.top_n)
    top_top = top_list(top, ["rank", "best_pattern", "variant", "score", "evidence_tags"], "score", min(args.top_n, len(top)))

    md = make_markdown(state_name, stamp, variants, top_items, top_top)
    if args.md_out:
        Path(args.md_out).write_text(md)
    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(
                {
                    "state": state_name,
                    "stamp": stamp,
                    "winners": variants,
                    "top_per_item": top_items,
                    "top_candidates": top_top,
                },
                indent=2,
                default=lambda o: o.item() if hasattr(o, "item") else str(o),
            )
        )
    if not args.md_out:
        print(md)


if __name__ == "__main__":
    main()
