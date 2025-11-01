#!/usr/bin/env python3
"""
V-TRAC Validator → Compact Scorer/Exporter

Consumes `validation_report.json` files emitted by the enhanced validator,
computes per-section confidence scores (overlap-first, strict consensus rescue),
lightly promotes recurring token families, and writes a compact CSV/JSON for
sharing or downstream ranking.

Examples:
    python TOOLS/vtrac_score_and_export.py data/outputs/analysis/vtrac_validation
    python TOOLS/vtrac_score_and_export.py data/outputs/analysis/vtrac_validation --output data/outputs/analysis/vtrac_validation
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set, Tuple

WEIGHTS = {
    "overlap": 3.0,
    "stable": 1.6,
    "consensus": 1.0,
    "token_echo": 1.2,
    "hot": 0.25,
    "super": 0.35,
    "mask": 0.8,
    "mirror": 0.5,
    "doubles": 0.3,
    "combined_prior": 1.15,
    "rescue_multiplier": 0.35,
}

COL_W = {7: 0.5, 6: 0.7, 5: 0.9, 4: 1.1, 3: 1.6, 2: 2.0, 1: 2.4}


def as_int_list(cols: Iterable) -> List[int]:
    out: List[int] = []
    for col in cols or []:
        try:
            out.append(int(str(col).strip()))
        except Exception:
            continue
    return out


def norm01(value: float, lo: float, hi: float) -> float:
    if hi <= lo:
        return 0.0
    scaled = (value - lo) / float(hi - lo)
    return max(0.0, min(1.0, scaled))


def discover_reports(paths: Sequence[str]) -> List[Path]:
    reports: Set[Path] = set()
    for raw in paths:
        candidate = Path(raw)
        if candidate.is_file() and candidate.name == "validation_report.json":
            reports.add(candidate.resolve())
        elif candidate.is_dir():
            for report in candidate.rglob("validation_report.json"):
                reports.add(report.resolve())
    return sorted(reports)


def get_section_names(payload: dict) -> List[str]:
    sections = payload.get("sections") or {}
    ordered: List[str] = []
    for canonical in ("Combined", "Midday", "Evening"):
        if canonical in sections:
            ordered.append(canonical)
    for name in sections.keys():
        if name not in ordered:
            ordered.append(name)
    return ordered


def tokens_for_section(payload: dict, section: str) -> Tuple[List[str], List[str]]:
    section_payload = (payload.get("sections") or {}).get(section, {})
    signals = section_payload.get("signals") or {}
    analyzer = section_payload.get("analyzer_signatures") or {}
    winners_tokens = signals.get("top_vtrac_box_signatures") or []
    analyzer_tokens = analyzer.get("primary") or []
    return winners_tokens, analyzer_tokens


def straight_list_for_section(payload: dict, section: str) -> List[str]:
    section_payload = (payload.get("sections") or {}).get(section, {})
    metrics = (section_payload.get("analyzer_metrics") or {}).get("primary") or {}
    straights = metrics.get("top_straights") or []
    if straights and isinstance(straights[0], dict):
        straights = [
            str(entry.get("straight"))
            for entry in sorted(straights, key=lambda e: e.get("score", 0), reverse=True)
            if entry.get("straight") is not None
        ]
    return straights[:3]


def metrics_for_section(payload: dict, section: str) -> Dict[str, object]:
    section_payload = (payload.get("sections") or {}).get(section, {})
    signals = section_payload.get("signals") or {}
    metrics = (section_payload.get("analyzer_metrics") or {}).get("primary") or {}

    mask_drop = metrics.get("mask_drop_count")
    mirror_supported = metrics.get("mirror_supported")
    if isinstance(mirror_supported, (int, float)):
        mirror_supported = mirror_supported > 0

    doubles = metrics.get("double_hits")
    if doubles is None:
        doubles = metrics.get("doubles_hit_count", 0)

    summaries = (payload.get("section_summaries") or {}).get(section, {})

    return {
        "hot": signals.get("hot"),
        "superhot": signals.get("superhot"),
        "hot_count": summaries.get("hot_count"),
        "superhot_count": summaries.get("superhot_count"),
        "stable_cols": as_int_list(signals.get("stable_columns") or []),
        "consensus_col1": bool(signals.get("consensus_col1")),
        "consensus_col2": bool(signals.get("consensus_col2")),
        "mask_drop": mask_drop if mask_drop is not None else 0,
        "mirror": bool(mirror_supported),
        "doubles": doubles if doubles is not None else 0,
    }


def stable_score(stable_cols: List[int]) -> float:
    return sum(COL_W.get(col, 0.0) for col in stable_cols)


def section_prior(section_name: str) -> float:
    return WEIGHTS["combined_prior"] if section_name == "Combined" else 1.0


def compute_cross_section_echo(tokens_map: Dict[str, Set[str]]) -> Dict[str, int]:
    echo: Dict[str, int] = {}
    sections = list(tokens_map.keys())
    for name in sections:
        mine = tokens_map[name]
        others = set().union(
            *[tokens_map[other] for other in sections if other != name]
        ) if len(sections) > 1 else set()
        echo[name] = len(mine & others)
    return echo


def tier_from_overlap(overlap: int) -> str:
    if overlap >= 4:
        return "A"
    if overlap == 3:
        return "B+"
    if overlap == 2:
        return "B"
    if overlap == 1:
        return "C"
    return "Z"


def build_global_token_ledger(staged_docs: List[dict]):
    token_states = defaultdict(set)
    token_sections_by_state = defaultdict(lambda: defaultdict(int))
    for entry in staged_docs:
        state = entry["__state__"]
        sections = entry["__sections__"]["winners_tokens"]
        for section, winners_tokens in sections.items():
            for token in winners_tokens:
                token_states[token].add(state)
                token_sections_by_state[state][token] += 1
    return token_states, token_sections_by_state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        default=["data/outputs/analysis/vtrac_validation"],
        help="Directories/files containing validation_report.json (searched recursively).",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Directory for vtrac_compact_report.{json,csv}. Defaults to the first report's parent directory.",
    )
    return parser.parse_args()


def main(args: argparse.Namespace) -> int:
    reports = discover_reports(args.paths)
    if not reports:
        print("No validation_report.json files found.", file=sys.stderr)
        return 1

    if args.output:
        output_dir = Path(args.output).resolve()
    else:
        output_dir = reports[0].parent
    output_dir.mkdir(parents=True, exist_ok=True)

    staged: List[dict] = []
    for report_path in reports:
        with report_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)

        state = payload.get("state") or report_path.parent.name
        date = payload.get("generated_at") or ""
        section_names = get_section_names(payload)

        winners_tokens_by_section = {}
        for section_name in section_names:
            winners, _ = tokens_for_section(payload, section_name)
            winners_tokens_by_section[section_name] = set(winners)

        staged.append(
            {
                "__path__": report_path,
                "__state__": state,
                "__date__": date,
                "__sect_names__": section_names,
                "__sections__": {"winners_tokens": winners_tokens_by_section},
                "doc": payload,
            }
        )

    token_states, token_sections_by_state = build_global_token_ledger(staged)

    rows: List[dict] = []
    for entry in staged:
        report_path = entry["__path__"]
        payload = entry["doc"]
        state = entry["__state__"]
        date = entry["__date__"]
        section_names = entry["__sect_names__"]

        raw_mask: List[float] = []
        raw_doubles: List[float] = []
        tokens_map: Dict[str, Set[str]] = {}
        section_cache: Dict[str, dict] = {}

        for section_name in section_names:
            winners_tokens, analyzer_tokens = tokens_for_section(payload, section_name)
            tokens_map[section_name] = set(winners_tokens)
            metrics = metrics_for_section(payload, section_name)
            section_cache[section_name] = {
                "winners_tokens": winners_tokens,
                "analyzer_tokens": analyzer_tokens,
                "metrics": metrics,
            }
            raw_mask.append(metrics["mask_drop"])
            raw_doubles.append(metrics["doubles"])

        mask_min, mask_max = (min(raw_mask), max(raw_mask)) if raw_mask else (0, 0)
        dbl_min, dbl_max = (min(raw_doubles), max(raw_doubles)) if raw_doubles else (0, 0)
        echo = compute_cross_section_echo(tokens_map)

        for section_name in section_names:
            cache_entry = section_cache[section_name]
            winners_tokens = cache_entry["winners_tokens"]
            analyzer_tokens = cache_entry["analyzer_tokens"]
            metrics = cache_entry["metrics"]

            overlap = len(set(winners_tokens) & set(analyzer_tokens))
            stable_cols = metrics["stable_cols"]
            stable = stable_score(stable_cols)
            consensus_count = int(metrics["consensus_col1"]) + int(
                metrics["consensus_col2"]
            )

            hot_count = (
                metrics["hot_count"]
                if metrics["hot_count"] is not None
                else (metrics["hot"] if isinstance(metrics["hot"], (int, float)) else 0)
            )
            superhot_count = (
                metrics["superhot_count"]
                if metrics["superhot_count"] is not None
                else (
                    metrics["superhot"]
                    if isinstance(metrics["superhot"], (int, float))
                    else 0
                )
            )

            hot_norm = min(1.0, (hot_count or 0) / 8.0)
            super_norm = min(1.0, (superhot_count or 0) / 12.0)
            mask_norm = norm01(metrics["mask_drop"], mask_min, mask_max)
            mirror_norm = 1.0 if metrics["mirror"] else 0.0
            doubles_norm = norm01(metrics["doubles"], dbl_min, dbl_max)

            score = (
                WEIGHTS["overlap"] * overlap
                + WEIGHTS["stable"] * stable
                + WEIGHTS["consensus"] * (consensus_count if stable_cols else 0)
                + WEIGHTS["token_echo"] * echo.get(section_name, 0)
                + WEIGHTS["hot"] * hot_norm
                + WEIGHTS["super"] * super_norm
                + WEIGHTS["mask"] * mask_norm
                + WEIGHTS["mirror"] * mirror_norm
                + WEIGHTS["doubles"] * doubles_norm
            )
            score *= section_prior(section_name)

            flags: List[str] = []
            if overlap == 0 and consensus_count >= 1 and stable_cols:
                score *= WEIGHTS["rescue_multiplier"]
                flags.append("weak_positive_rescue")

            tier = tier_from_overlap(overlap)
            if overlap == 0:
                flags.append("zero_overlap")

            token_scores: List[Tuple[float, str]] = []
            for token in winners_tokens:
                base = 1.0
                if token in analyzer_tokens:
                    base += 0.5
                local_rep = token_sections_by_state[state].get(token, 0)
                if local_rep > 1:
                    base += 0.2 * (local_rep - 1)
                if len(token_states[token]) >= 3:
                    base += 0.3
                token_scores.append((round(base, 3), token))
            token_scores.sort(reverse=True)
            recommended_tokens = [token for _, token in token_scores][:3]

            straights = straight_list_for_section(payload, section_name)

            rows.append(
                {
                    "date": date,
                    "state": state,
                    "section": section_name,
                    "overlap": overlap,
                    "stable_cols_count": len(stable_cols),
                    "stable_cols": stable_cols,
                    "consensus_col1": metrics["consensus_col1"],
                    "consensus_col2": metrics["consensus_col2"],
                    "cross_section_echo": echo.get(section_name, 0),
                    "hot_count": hot_count,
                    "superhot_count": superhot_count,
                    "mask_drop": metrics["mask_drop"],
                    "mirror_supported": metrics["mirror"],
                    "double_hits": metrics["doubles"],
                    "confidence_score": round(score, 3),
                    "tier": tier,
                    "flags": flags,
                    "top_tokens": winners_tokens,
                    "recommended_tokens": recommended_tokens,
                    "top_straights": straights,
                    "source": report_path.name,
                }
            )

    out_json = output_dir / "vtrac_compact_report.json"
    out_csv = output_dir / "vtrac_compact_report.csv"

    with out_json.open("w", encoding="utf-8") as handle:
        json.dump(rows, handle, indent=2)

    headers = [
        "date",
        "state",
        "section",
        "overlap",
        "stable_cols_count",
        "stable_cols",
        "consensus_col1",
        "consensus_col2",
        "cross_section_echo",
        "hot_count",
        "superhot_count",
        "mask_drop",
        "mirror_supported",
        "double_hits",
        "confidence_score",
        "tier",
        "flags",
        "top_tokens",
        "recommended_tokens",
        "top_straights",
        "source",
    ]

    def csv_escape(value) -> str:
        text = (
            value
            if isinstance(value, str)
            else json.dumps(value, separators=(",", ":"))
        )
        if any(ch in text for ch in [",", '"', "\n"]):
            text = '"' + text.replace('"', '""') + '"'
        return text

    with out_csv.open("w", encoding="utf-8", newline="") as handle:
        handle.write(",".join(headers) + "\n")
        for row in rows:
            line = ",".join(csv_escape(row[column]) for column in headers)
            handle.write(line + "\n")

    print(f"Wrote {len(rows)} rows")
    print(f"- JSON: {out_json}")
    print(f"- CSV : {out_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(parse_args()))
