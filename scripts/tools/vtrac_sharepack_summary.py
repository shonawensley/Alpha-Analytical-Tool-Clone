"""
Summarize V-TRAC enhanced sharepack outputs into Markdown/JSON with source labels.

Usage:
  python3 scripts/tools/vtrac_sharepack_summary.py --sharepack sharepacks/2025-06-21/OntarioCanada4/vtrac/OntarioCanada4 [--md-out out.md] [--json-out out.json]

What it does:
  - Reads enhanced bundle JSON (<STATE>_vtrac_enhanced_*.json) and validation_report.{json,md} if present.
  - Reports top indices and straights with scores + why/evidence tags (source: enhanced JSON).
  - Reports section summaries (hot/superhot, consensus, ring votes, analyzer metrics).
  - If winner_map/flags are present (not in this bundle), it would include winner coverage; for now this bundle is analyzer-only.
"""

import argparse
import json
from pathlib import Path
from typing import Dict, List


def load_enhanced_json(sharepack: Path) -> Dict:
    files = sorted(sharepack.glob("*_vtrac_enhanced_*.json"))
    if not files:
        raise SystemExit("No enhanced vtrac JSON found in sharepack")
    return json.loads(files[-1].read_text())


def make_markdown(state: str, stamp: str, top_indices: List[Dict], top_straights: List[str], section_summaries: Dict) -> str:
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
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sharepack", required=True, help="Path to vtrac/<STATE>/<STATE> sharepack folder")
    ap.add_argument("--md-out", help="Markdown output path")
    ap.add_argument("--json-out", help="JSON output path")
    ap.add_argument("--top-n", type=int, default=10, help="Top N indices/straights to show")
    args = ap.parse_args()

    sharepack = Path(args.sharepack)
    state_name = sharepack.parent.name if sharepack.parent else sharepack.name
    enhanced = load_enhanced_json(sharepack)
    stamp = enhanced.get("timestamp", "")

    top_indices = enhanced.get("indices_ranked", [])[: args.top_n]
    top_straights = enhanced.get("top_straights", [])[: args.top_n]
    section_summaries = enhanced.get("section_summaries", {})

    md = make_markdown(state_name, stamp, top_indices, top_straights, section_summaries)
    if args.md_out:
        Path(args.md_out).write_text(md)
    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(
                {
                    "state": state_name,
                    "stamp": stamp,
                    "top_indices": top_indices,
                    "top_straights": top_straights,
                    "section_summaries": section_summaries,
                },
                indent=2,
            )
        )
    if not args.md_out:
        print(md)


if __name__ == "__main__":
    main()
