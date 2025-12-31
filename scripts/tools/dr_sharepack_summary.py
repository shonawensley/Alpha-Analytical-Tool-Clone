"""
Summarize Digit Reduction outputs from a sharepack into Markdown/JSON with source labels.

Usage:
  python3 scripts/tools/dr_sharepack_summary.py --sharepack sharepacks/2025-06-21/OntarioCanada4/digit_reduction/OntarioCanada4 [--md-out out.md] [--json-out out.json]

What it does:
  - Maps winners (Midday/Evening/Combined) from `*_winner_stamp.json` (SSOT) to literal + canonical.
  - Reads analyzer_v2 per_item/top/meta, winner_flags/hits/map/overlay, reducer scores/report (if present).
  - Reports winner evidence/ranks with explicit source labels, including **any vs final** semantics.
  - Lists top candidates and coverage gaps (missing flags/hits) per variant.
  - Emits Markdown for Part 2 (paste under step 0) and optional JSON.

Notes:
  - Assumes the sharepack follows the DR lean outputs contract (analyzer_v2/*, winners/*, reducer scores/report).
  - Skips GA/TX/WV if they lack tables (handled by caller).
"""

import argparse
import itertools
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd


def normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    return digits.zfill(3) if len(digits) <= 3 else digits


def canonical_of_literal(literal: str) -> str:
    literal = normalize_pick3_literal(literal)
    if not literal:
        return ""
    return "".join(sorted(literal))


def permuted_triads(canonical: str) -> set[str]:
    canonical = normalize_pick3_literal(canonical)
    if len(canonical) != 3 or not canonical.isdigit():
        return set()
    return {"".join(p) for p in set(itertools.permutations(canonical, 3))}


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def read_flags_hits(root: Path, stamp: str, variant: str) -> Dict[str, pd.DataFrame]:
    winners_dir = root / "analyzer_v2" / "winners"
    flags_path = winners_dir / f"{stamp}_{variant}_winner_flags.csv"
    hits_path = winners_dir / f"{stamp}_{variant}_winner_hits.csv"
    flags = pd.read_csv(flags_path) if flags_path.exists() else pd.DataFrame()
    hits = pd.read_csv(hits_path) if hits_path.exists() else pd.DataFrame()
    return {"flags": flags, "hits": hits}


def detect_latest_stamp(winners_dir: Path) -> Optional[str]:
    if not winners_dir.exists():
        return None
    stamps = sorted({p.name.split("_")[0] for p in winners_dir.glob("*_winner_stamp.json")})
    if not stamps:
        stamps = sorted({p.name.split("_")[0] for p in winners_dir.glob("*_winner_flags.csv")})
    if not stamps:
        return None
    return stamps[-1]


def read_winner_stamp(root: Path, stamp: str, variant: str) -> Optional[Dict[str, Any]]:
    winners_dir = root / "analyzer_v2" / "winners"
    stamp_path = winners_dir / f"{stamp}_{variant}_winner_stamp.json"
    if not stamp_path.exists():
        return None
    return load_json(stamp_path)


def summarize_variant(
    variant: str,
    per_item: pd.DataFrame,
    top: pd.DataFrame,
    stamp_data: Optional[Dict[str, Any]],
    flags: pd.DataFrame,
    hits: pd.DataFrame,
    reducer_scores: pd.DataFrame = None,
) -> Dict:
    # Winner + semantics are anchored by stamp JSON (SSOT).
    raw_winner = (stamp_data or {}).get("winner") or ""
    literal = normalize_pick3_literal(raw_winner) or "unknown"
    raw_canon = (stamp_data or {}).get("winner_canon") or ""
    canonical = normalize_pick3_literal(raw_canon) or (canonical_of_literal(literal) if literal != "unknown" else "unknown")
    winner_variants = permuted_triads(canonical) | {literal, canonical}
    stamp_counts = (stamp_data or {}).get("counts") or {}
    items_total = int(stamp_counts.get("items_total") or 0)

    # Flags summary ("any" semantics + VT boxed/straight flags)
    flags_sum = {"rows": int(len(flags)), "source": "winner_flags.csv"}
    for col in [
        "dr_win_exact",
        "dr_win_vtrac",
        "dr_win_drop_exact",
        "dr_win_drop_vtrac",
        "dr_win_family_exact",
        "dr_win_family_vtrac",
        "dr_win_vt_boxed",
        "dr_win_vt_straight",
    ]:
        if col in flags.columns:
            flags_sum[col] = int(flags[col].fillna(0).sum())
        else:
            flags_sum[col] = None

    # Hits summary ("final" semantics; do NOT filter by final_value == winner)
    hits_sum = {"rows": int(len(hits)), "source": "winner_hits.csv"}
    for col in [
        "final_exact_match",
        "final_vtrac_match",
        "final_drop_exact_match",
        "final_drop_vtrac_match",
        "final_family_exact_match",
        "final_family_vtrac_match",
        "final_vt_boxed",
        "final_vt_straight",
    ]:
        if col in hits.columns:
            hits_sum[col] = int(hits[col].fillna(0).sum())
        else:
            hits_sum[col] = None

    # per_item evidence (best ranks for match flags in this variant)
    pi_variant = per_item
    if "variant" in per_item.columns:
        pi_variant = per_item[per_item["variant"].astype(str) == variant]
    pi_present = not pi_variant.empty
    pi_best_rank_exact = None
    pi_best_rank_vtrac = None
    if pi_present and "area_rank" in pi_variant.columns:
        if "dr.win_exact" in pi_variant.columns and (pi_variant["dr.win_exact"].fillna(0) > 0).any():
            pi_best_rank_exact = int(pi_variant.loc[pi_variant["dr.win_exact"].fillna(0) > 0, "area_rank"].min())
        if "dr.win_vtrac" in pi_variant.columns and (pi_variant["dr.win_vtrac"].fillna(0) > 0).any():
            pi_best_rank_vtrac = int(pi_variant.loc[pi_variant["dr.win_vtrac"].fillna(0) > 0, "area_rank"].min())

    # top candidates presence (does the winner triad appear as a candidate pattern?)
    top_variant = top
    if "variant" in top.columns:
        top_variant = top[top["variant"].astype(str) == variant]
    winner_in_top = False
    top_best_rank = None
    rows_total = int(len(top_variant))
    winner_score_v2 = None
    top_score_v2 = None
    winner_rank_fraction = None
    winner_score_ratio_to_top = None
    winner_score_delta_from_top = None

    if rows_total and "score_v2" in top_variant.columns:
        try:
            top_score_v2 = float(pd.to_numeric(top_variant["score_v2"], errors="coerce").fillna(0).max())
        except Exception:
            top_score_v2 = None

    if not top_variant.empty and "best_pattern" in top_variant.columns:
        patterns = top_variant["best_pattern"].astype(str).map(normalize_pick3_literal)
        winner_rows = top_variant[patterns.isin(winner_variants)]
        winner_in_top = not winner_rows.empty
        if winner_in_top and "rank" in winner_rows.columns:
            top_best_rank = int(pd.to_numeric(winner_rows["rank"], errors="coerce").min())
        if winner_in_top and "score_v2" in winner_rows.columns:
            try:
                winner_score_v2 = float(pd.to_numeric(winner_rows["score_v2"], errors="coerce").fillna(0).max())
            except Exception:
                winner_score_v2 = None

    if top_best_rank is not None and rows_total:
        winner_rank_fraction = float(top_best_rank) / float(rows_total)
    if winner_score_v2 is not None and top_score_v2 not in (None, 0):
        winner_score_ratio_to_top = float(winner_score_v2) / float(top_score_v2)
        winner_score_delta_from_top = float(top_score_v2) - float(winner_score_v2)

    # Reducer scores (optional)
    reducer_present = reducer_scores is not None and not reducer_scores.empty

    gaps = []
    if stamp_data is None:
        gaps.append("missing_stamp_json")
    if flags_sum["rows"] == 0:
        gaps.append("missing_flags")
    if hits_sum["rows"] == 0:
        gaps.append("missing_hits")
    if not pi_present:
        gaps.append("missing_per_item")
    if top.empty:
        gaps.append("missing_top")

    return {
        "variant": variant,
        "literal": literal,
        "canonical": canonical,
        "stamp": {"present": stamp_data is not None, "items_total": items_total, "counts": stamp_counts, "source": "winner_stamp.json"},
        "flags": flags_sum,
        "hits": hits_sum,
        "per_item": {
            "present": pi_present,
            "best_area_rank_exact_any": pi_best_rank_exact,
            "best_area_rank_vtrac_any": pi_best_rank_vtrac,
            "source": "analyzer_v2_per_item.csv",
        },
        "top": {
            "winner_present": winner_in_top,
            "winner_best_rank": top_best_rank,
            "rows_total": rows_total,
            "winner_rank_fraction": winner_rank_fraction,
            "winner_score_v2": winner_score_v2,
            "top_score_v2": top_score_v2,
            "winner_score_ratio_to_top": winner_score_ratio_to_top,
            "winner_score_delta_from_top": winner_score_delta_from_top,
            "source": "analyzer_v2_top_candidates.csv",
        },
        "reducer_present": reducer_present,
        "gaps": gaps,
    }


def top_list(df: pd.DataFrame, cols: List[str], sort_by: str, top_n: int, *, ascending: bool) -> List[Dict]:
    out = []
    if df.empty:
        return out
    df_sorted = df.sort_values(sort_by, ascending=ascending).head(top_n)
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
        if v["stamp"]["present"]:
            c = v["stamp"]["counts"]
            lines.append(
                f"- Stamp ({v['stamp']['source']}): items_total={v['stamp']['items_total']} | "
                f"exact_any={c.get('exact_any')} exact_final={c.get('exact_final')} | "
                f"vtrac_any={c.get('vtrac_any')} vtrac_final={c.get('vtrac_final')} | "
                f"drop_exact_any={c.get('drop_exact_any')} drop_exact_final={c.get('drop_exact_final')} | "
                f"drop_vtrac_any={c.get('drop_vtrac_any')} drop_vtrac_final={c.get('drop_vtrac_final')} | "
                f"family_exact_any={c.get('family_exact_any')} family_exact_final={c.get('family_exact_final')} | "
                f"family_vtrac_any={c.get('family_vtrac_any')} family_vtrac_final={c.get('family_vtrac_final')}"
            )
        else:
            lines.append(f"- Stamp ({v['stamp']['source']}): missing")
        lines.append(
            f"- Flags ({v['flags']['source']}): rows={v['flags']['rows']} | "
            f"exact_any={v['flags'].get('dr_win_exact')} vtrac_any={v['flags'].get('dr_win_vtrac')} | "
            f"drop_exact_any={v['flags'].get('dr_win_drop_exact')} drop_vtrac_any={v['flags'].get('dr_win_drop_vtrac')} | "
            f"family_exact_any={v['flags'].get('dr_win_family_exact')} family_vtrac_any={v['flags'].get('dr_win_family_vtrac')} | "
            f"vt_boxed={v['flags'].get('dr_win_vt_boxed')} vt_straight={v['flags'].get('dr_win_vt_straight')}"
        )
        lines.append(
            f"- Hits ({v['hits']['source']}): rows={v['hits']['rows']} | "
            f"exact_final={v['hits'].get('final_exact_match')} vtrac_final={v['hits'].get('final_vtrac_match')} | "
            f"drop_exact_final={v['hits'].get('final_drop_exact_match')} drop_vtrac_final={v['hits'].get('final_drop_vtrac_match')} | "
            f"family_exact_final={v['hits'].get('final_family_exact_match')} family_vtrac_final={v['hits'].get('final_family_vtrac_match')} | "
            f"vt_boxed={v['hits'].get('final_vt_boxed')} vt_straight={v['hits'].get('final_vt_straight')}"
        )
        if v["per_item"]["present"]:
            lines.append(
                f"- Per-item ({v['per_item']['source']}): best area_rank where exact_any=1 → {v['per_item']['best_area_rank_exact_any']} | "
                f"best area_rank where vtrac_any=1 → {v['per_item']['best_area_rank_vtrac_any']}"
            )
        else:
            lines.append(f"- Per-item ({v['per_item']['source']}): not present")
        lines.append(
            f"- Top candidates ({v['top']['source']}): rows_total={v['top'].get('rows_total')} | "
            f"winner_present={v['top']['winner_present']} | winner_best_rank={v['top']['winner_best_rank']} | "
            f"winner_rank_fraction={v['top'].get('winner_rank_fraction')} | "
            f"winner_score_v2={v['top'].get('winner_score_v2')} top_score_v2={v['top'].get('top_score_v2')} | "
            f"winner_score_ratio_to_top={v['top'].get('winner_score_ratio_to_top')} "
            f"winner_score_delta_from_top={v['top'].get('winner_score_delta_from_top')}"
        )
        lines.append(f"- Reducer scores present: {v['reducer_present']}")
        if v["gaps"]:
            lines.append(f"- Coverage gaps: {', '.join(v['gaps'])}")
    lines.append("\n## Top per_item (analyzer_v2_per_item.csv)")
    for row in top_items:
        lines.append(
            f"- area_rank {row.get('area_rank','')} | variant {row.get('variant','')} | section {row.get('section','')} | "
            f"set {row.get('set','')} draw {row.get('draw','')} col {row.get('col','')} | "
            f"pattern {row.get('pattern','')} | score_v2 {row.get('score_v2','')} | match_types {row.get('match_types','')}"
        )
    lines.append("\n## Top candidates (analyzer_v2_top_candidates.csv)")
    for row in top_top:
        lines.append(
            f"- rank {row.get('rank','')} | variant {row.get('variant','')} | best_pattern {row.get('best_pattern','')} | "
            f"score_v2 {row.get('score_v2','')} | tags {row.get('evidence_tags','')}"
        )
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sharepack", required=True, help="Path to digit_reduction/<STATE>/<STATE>")
    ap.add_argument("--md-out", help="Markdown output path")
    ap.add_argument("--json-out", help="JSON output path")
    ap.add_argument("--top-n", type=int, default=10, help="Top N rows to show for per_item/top")
    args = ap.parse_args()

    sharepack = Path(args.sharepack)
    state_name = sharepack.name

    per_item = pd.read_csv(
        sharepack / "analyzer_v2" / f"{sharepack.name}_analyzer_v2_per_item.csv",
        dtype={"pattern": str, "variant": str},
    )
    top = pd.read_csv(
        sharepack / "analyzer_v2" / f"{sharepack.name}_analyzer_v2_top_candidates.csv",
        dtype={"best_pattern": str, "variant": str},
    )
    if "pattern" in per_item.columns:
        per_item["pattern"] = per_item["pattern"].astype(str).map(normalize_pick3_literal)
    if "best_pattern" in top.columns:
        top["best_pattern"] = top["best_pattern"].astype(str).map(normalize_pick3_literal)

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
    if "rank" not in top.columns:
        top["rank"] = ""
    if "score_v2" not in top.columns:
        top["score_v2"] = top.get("score", 0)

    for col in ["section", "set", "draw", "col", "pattern"]:
        if col not in per_item.columns:
            per_item[col] = ""
    winners_dir = sharepack / "analyzer_v2" / "winners"
    stamp = detect_latest_stamp(winners_dir)

    variants = []
    if stamp:
        for variant in ["Midday", "Evening", "Combined"]:
            flags_hits = read_flags_hits(sharepack, stamp, variant)
            reducer_scores_path = sharepack / f"{sharepack.name}_digit_reduction_scores.csv"
            reducer_scores = pd.read_csv(reducer_scores_path) if reducer_scores_path.exists() else pd.DataFrame()
            stamp_data = read_winner_stamp(sharepack, stamp, variant)
            variants.append(
                summarize_variant(
                    variant=variant,
                    per_item=per_item,
                    top=top,
                    stamp_data=stamp_data,
                    flags=flags_hits["flags"],
                    hits=flags_hits["hits"],
                    reducer_scores=reducer_scores,
                )
            )

    top_items = top_list(
        per_item,
        ["area_rank", "variant", "section", "set", "draw", "col", "pattern", "score_v2", "match_types"],
        "score_v2",
        args.top_n,
        ascending=False,
    )
    top_top = top_list(
        top,
        ["rank", "variant", "best_pattern", "score_v2", "evidence_tags"],
        "score_v2",
        min(args.top_n, len(top)),
        ascending=False,
    )

    md = make_markdown(state_name, stamp or "N/A", variants, top_items, top_top)
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
