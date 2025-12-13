"""
Summarize Stable outputs from a sharepack folder into Markdown/JSON.

Usage:
  python3 scripts/tools/stable_sharepack_summary.py --sharepack sharepacks/2025-06-21/OntarioCanada4/stable/OntarioCanada4 [--md-out out.md] [--json-out out.json]

The script:
  - Maps winners (metrics.winners list -> Midday, Evening by position) and their canonicals.
  - Reads scores/compound/families/metrics/spotlight, computes ranks, and reports per-winner evidence with source labels.
  - Emits top-N candidates (compound, families) and coverage gaps.
  - Writes Markdown/JSON or prints Markdown to stdout.
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Summarize Stable sharepack outputs")
    p.add_argument(
        "--sharepack",
        required=True,
        help="Path to stable/<STATE>/<STATE> folder inside the sharepack",
    )
    p.add_argument("--md-out", help="Optional Markdown output path")
    p.add_argument("--json-out", help="Optional JSON output path")
    p.add_argument(
        "--top-n",
        type=int,
        default=10,
        help="Top N candidates to list for compound and families (default: 10)",
    )
    return p.parse_args()


def load_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def rank_frame(df: pd.DataFrame, score_col: str) -> pd.DataFrame:
    df = df.copy()
    df["rank"] = df[score_col].rank(method="min", ascending=False).astype(int)
    return df


def canonical_of_literal(literal: str) -> str:
    return "".join(sorted(str(literal)))


def map_winners(metrics: Dict) -> Dict[str, str]:
    """
    Map metrics.winners (list) to {Midday: ..., Evening: ...} heuristically.
    """
    winners = metrics.get("winners") or []
    winners = [str(w) for w in winners]
    mapping = {}
    if len(winners) >= 1:
        mapping["Midday"] = winners[0]
    if len(winners) >= 2:
        mapping["Evening"] = winners[1]
    return mapping


def map_winner_family_ids(metrics: Dict, winners: Dict[str, str]) -> Dict[str, str]:
    fam_ids = metrics.get("winner_family_ids") or []
    out = {}
    if len(fam_ids) >= 1 and "Midday" in winners:
        out["Midday"] = fam_ids[0]
    if len(fam_ids) >= 2 and "Evening" in winners:
        out["Evening"] = fam_ids[1]
    return out


def summarize_winner(
    label: str,
    literal: str,
    scores: pd.DataFrame,
    compound: pd.DataFrame,
    families: pd.DataFrame,
    spotlight: pd.DataFrame,
    winner_hits: Dict,
    winner_family_id: str = None,
) -> Dict:
    canonical = canonical_of_literal(literal)
    res = {"label": label, "literal": literal, "canonical": canonical}

    # Spotlight rows (use canonical; literal columns are constant)
    spot_rows = spotlight[spotlight["Canonical"].astype(str) == canonical]
    res["spotlight"] = {
        "count": len(spot_rows),
        "exact_boxed": int(spot_rows.get("is_exact_boxed", []).sum()) if not spot_rows.empty else 0,
        "exact_straight": int(spot_rows.get("is_exact_straight", []).sum()) if not spot_rows.empty else 0,
        "vt_boxed": int(spot_rows.get("is_vtrac_boxed", []).sum()) if not spot_rows.empty else 0,
        "source": "winner_family_spotlight_raw.csv",
    }

    # Scores
    sc_rows = scores[scores["Canonical"].astype(str) == canonical]
    if len(sc_rows):
        best = sc_rows.sort_values("score", ascending=False).iloc[0]
        res["scores"] = {
            "present": True,
            "best_rank": int(best["rank"]),
            "section": best["section"],
            "set": best["Set"],
            "draw": best["Draw"],
            "col": best["Column"],
            "score": float(best["score"]),
            "hot": int(best.get("hot", 0)),
            "vtrac_straight": float(best.get("score_vtrac_straight", 0)),
            "why": str(best.get("why", "")),
            "source": "patterns_scores.csv",
        }
    else:
        res["scores"] = {"present": False, "source": "patterns_scores.csv"}

    # Compound
    cp_rows = compound[compound["Canonical"].astype(str) == canonical]
    if len(cp_rows):
        best = cp_rows.sort_values("compound_score", ascending=False).iloc[0]
        res["compound"] = {
            "present": True,
            "best_rank": int(best["rank"]),
            "section": best["section"],
            "score": float(best["compound_score"]),
            "col1_hits": int(best.get("col1_hits", 0)),
            "hot2": int(best.get("hot2_count", 0)),
            "set_chain": int(best.get("set_chain_depth", 0)),
            "draw_chain": int(best.get("draw_chain_depth", 0)),
            "why": str(best.get("compound_why", "")),
            "source": "patterns_compound.csv",
        }
    else:
        res["compound"] = {"present": False, "source": "patterns_compound.csv"}

    # Families (prefer explicit winner_family_id, fallback to contains canonical digits)
    fam_rows = pd.DataFrame()
    if winner_family_id is not None:
        fam_rows = families[families["family_id"] == winner_family_id]
    if fam_rows.empty:
        fam_rows = families[families["family_id"].astype(str).str.contains(canonical)]
    if len(fam_rows):
        best = fam_rows.sort_values("family_score", ascending=False).iloc[0]
        res["families"] = {
            "present": True,
            "count": len(fam_rows),
            "best_rank": int(best["rank"]),
            "section": best["section"],
            "score": float(best["family_score"]),
            "hot2": int(best.get("hot2_count", 0)),
            "col1_hits": int(best.get("col1_hits", 0)) if "col1_hits" in best else None,
            "source": "patterns_families.csv",
        }
    else:
        res["families"] = {"present": False, "source": "patterns_families.csv"}

    # Metrics hits
    mh = winner_hits.get(literal) or winner_hits.get(canonical) or {}
    res["metrics_hits"] = {
        "exact_boxed": mh.get("exact_boxed"),
        "exact_straight": mh.get("exact_straight"),
        "vt_boxed_count": len(mh.get("vtrac_boxed", []) or []),
        "source": "metrics.json",
    }

    # Coverage gap flags
    gaps = []
    if res["spotlight"]["count"] == 0:
        gaps.append("missing_from_spotlight")
    if not res["scores"].get("present"):
        gaps.append("missing_from_scores")
    if not res["compound"].get("present"):
        gaps.append("missing_from_compound")
    res["gaps"] = gaps

    return res


def top_list(df: pd.DataFrame, cols: List[str], top_n: int) -> List[Dict]:
    out = []
    for _, row in df.sort_values(cols[-1], ascending=False).head(top_n).iterrows():
        item = {}
        for col in cols:
            val = row[col]
            if hasattr(val, "item"):
                val = val.item()
            item[col] = val
        out.append(item)
    return out


def make_markdown(state: str, winners_info: List[Dict], top_comp: List[Dict], top_fam: List[Dict]) -> str:
    lines: List[str] = []
    lines.append(f"# Stable Summary — {state}")
    for win in winners_info:
        lines.append(f"\n## {win['label']} winner {win['literal']} (canonical {win['canonical']})")
        lines.append(f"- Spotlight ({win['spotlight']['source']}): {win['spotlight']['count']} rows | exact_boxed={win['spotlight']['exact_boxed']} | exact_straight={win['spotlight']['exact_straight']} | vt_boxed={win['spotlight']['vt_boxed']}")
        if win["scores"].get("present"):
            s = win["scores"]
            why = f" | why {s['why']}" if s.get("why") else ""
            lines.append(f"- Scores ({s['source']}): rank {s['best_rank']}, section {s['section']}, Set {s['set']}, Draw {s['draw']}, Col {s['col']}, score {s['score']}, hot {s['hot']}, vt_straight {s['vtrac_straight']}{why}")
        else:
            lines.append(f"- Scores ({win['scores']['source']}): not present")
        if win["compound"].get("present"):
            c = win["compound"]
            why = f" | why {c['why']}" if c.get("why") else ""
            lines.append(f"- Compound ({c['source']}): rank {c['best_rank']}, section {c['section']}, score {c['score']}, col1_hits {c['col1_hits']}, hot2 {c['hot2']}, set_chain {c['set_chain']}, draw_chain {c['draw_chain']}{why}")
        else:
            lines.append(f"- Compound ({win['compound']['source']}): not present")
        if win["families"].get("present"):
            f = win["families"]
            lines.append(f"- Families ({f['source']}): {f['count']} rows contain digits; best rank {f['best_rank']}, section {f['section']}, score {f['score']}, hot2 {f['hot2']}")
        else:
            lines.append(f"- Families ({win['families']['source']}): not present")
        mh = win["metrics_hits"]
        lines.append(f"- Metrics ({mh['source']}): exact_boxed={mh['exact_boxed']} | exact_straight={mh['exact_straight']} | vt_boxed_count={mh['vt_boxed_count']}")
        if win["gaps"]:
            lines.append(f"- Coverage gaps: {', '.join(win['gaps'])}")
    lines.append("\n## Top compound candidates (patterns_compound.csv)")
    for row in top_comp:
        lines.append(
            f"- rank {int(row['rank']):>4} | canon {row['Canonical']} | section {row['section']} | score {row['compound_score']} | col1_hits {row.get('col1_hits','')} | hot2 {row.get('hot2_count','')}"
        )
    lines.append("\n## Top families (patterns_families.csv)")
    for row in top_fam:
        lines.append(
            f"- rank {int(row['rank']):>4} | family {row['family_id']} | score {row['family_score']} | hot2 {row.get('hot2_count','')} | section {row['section']}"
        )
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    sharepack = Path(args.sharepack)
    if not sharepack.exists():
        raise SystemExit(f"sharepack path not found: {sharepack}")

    metrics = json.loads(sharepack.joinpath(f"{sharepack.name}_metrics.json").read_text())
    scores = rank_frame(load_csv(sharepack / f"{sharepack.name}_stable_patterns_scores.csv"), "score")
    compound = rank_frame(load_csv(sharepack / f"{sharepack.name}_stable_patterns_compound.csv"), "compound_score")
    families = rank_frame(load_csv(sharepack / f"{sharepack.name}_stable_patterns_families.csv"), "family_score")
    spotlight = load_csv(sharepack / f"{sharepack.name}_winner_family_spotlight_raw.csv")

    winners = map_winners(metrics)
    winner_family_ids = map_winner_family_ids(metrics, winners)
    winner_hits = metrics.get("winner_hits", {})

    winners_info = []
    for label, literal in winners.items():
        winners_info.append(
            summarize_winner(
                label=label,
                literal=literal,
                scores=scores,
                compound=compound,
                families=families,
                spotlight=spotlight,
                winner_hits=winner_hits,
                winner_family_id=winner_family_ids.get(label),
            )
        )

    top_comp = top_list(compound, ["rank", "Canonical", "section", "compound_score", "col1_hits", "hot2_count"], args.top_n)
    top_fam = top_list(families, ["rank", "family_id", "family_score", "hot2_count", "section"], min(5, args.top_n))

    # Derive state from path: …/<DATE>/<STATE>/stable/<STATE>
    state_name = sharepack.parents[2].name if len(sharepack.parents) >= 3 else sharepack.parent.name
    md = make_markdown(state=state_name, winners_info=winners_info, top_comp=top_comp, top_fam=top_fam)

    if args.md_out:
        Path(args.md_out).write_text(md)
    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(
                {
                    "state": state_name,
                    "sharepack": str(sharepack),
                    "winners": winners_info,
                    "top_compound": top_comp,
                    "top_families": top_fam,
                },
                indent=2,
                default=lambda o: o.item() if hasattr(o, "item") else str(o),
            )
        )
    if not args.md_out:
        print(md)


if __name__ == "__main__":
    main()
