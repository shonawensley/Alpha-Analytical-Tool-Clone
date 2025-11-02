#!/usr/bin/env python3
"""
V-TRAC validator → compact scorer/exporter.

Reads one or more folders of `validation_report.json` files (emitted by the
enhanced validator), computes per-section confidence scores using overlap,
right-column stability, consensus rescue, section/state priors, and light
token-ledger promotion, then exports a compact CSV/JSON suitable for sharing
or downstream aggregation.

Examples
--------
    python TOOLS/vtrac_score_and_export.py
    python TOOLS/vtrac_score_and_export.py data/outputs/analysis/vtrac_validation \
        --config configs/vtrac_score_config.json \
        --out-dir data/outputs/analysis/vtrac_validation \
        --verbose
"""

from __future__ import annotations

import argparse
import json
import logging
import math
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set, Tuple

DEFAULT_INPUTS = [
    "data/outputs/analysis/vtrac_validation",
    "data/outputs/analysis/vtrac",
]

DEFAULT_WEIGHTS: Dict[str, float] = {
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

DEFAULT_COL_WEIGHTS: Dict[int, float] = {
    7: 0.5,
    6: 0.7,
    5: 0.9,
    4: 1.1,
    3: 1.6,
    2: 2.0,
    1: 2.4,
}

DEFAULT_SECTION_PRIORS: Dict[str, float] = {
    "Combined": DEFAULT_WEIGHTS["combined_prior"],
    "Midday": 1.0,
    "Evening": 1.0,
}


def parse_bool(value) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value > 0
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "t", "yes", "y"}
    return False


def to_int(value) -> int:
    if isinstance(value, bool):
        return int(value)
    try:
        return int(value)
    except Exception:
        return 0


def to_float(value) -> float:
    if isinstance(value, bool):
        return float(int(value))
    try:
        return float(value)
    except Exception:
        return 0.0


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


def load_config(path: str | None) -> Dict[str, Dict]:
    if not path:
        return {
            "weights": {},
            "col_weights": {},
            "section_priors": {},
            "state_priors": {},
        }
    config_path = Path(path)
    try:
        data = json.loads(config_path.read_text())
        return {
            "weights": data.get("weights", {}),
            "col_weights": data.get("col_weights", {}),
            "section_priors": data.get("section_priors", {}),
            "state_priors": data.get("state_priors", {}),
        }
    except Exception as exc:  # pragma: no cover - defensive
        logging.warning("Could not load config %s (%s)", config_path, exc)
        return {
            "weights": {},
            "col_weights": {},
            "section_priors": {},
            "state_priors": {},
        }


def stable_score(stable_cols: Iterable[int], col_weights: Dict[int, float]) -> float:
    return sum(col_weights.get(int(col), 0.0) for col in stable_cols)


def build_global_token_ledger(staged_docs: List[dict]) -> Tuple[Dict[str, Set[str]], Dict[str, Dict[str, int]]]:
    token_states: Dict[str, Set[str]] = defaultdict(set)
    token_sections_by_state: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for entry in staged_docs:
        state = entry["__state__"]
        winners_map = entry["__sections__"]["winners_tokens"]
        analyzer_map = entry["__sections__"]["analyzer_tokens"]
        for section in winners_map:
            union_tokens = winners_map[section] | analyzer_map.get(section, set())
            for token in union_tokens:
                token_states[token].add(state)
                token_sections_by_state[state][token] += 1
    return token_states, token_sections_by_state


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
    summaries = (payload.get("section_summaries") or {}).get(section, {})

    mask_drop = metrics.get("mask_drop_count")
    doubles = metrics.get("double_hits")
    if doubles is None:
        doubles = metrics.get("doubles_hit_count", 0)

    return {
        "hot": signals.get("hot"),
        "superhot": signals.get("superhot"),
        "hot_count": summaries.get("hot_count"),
        "superhot_count": summaries.get("superhot_count"),
        "stable_cols": [to_int(c) for c in signals.get("stable_columns") or []],
        "consensus_col1": parse_bool(signals.get("consensus_col1")),
        "consensus_col2": parse_bool(signals.get("consensus_col2")),
        "mask_drop": mask_drop if mask_drop is not None else 0,
        "mirror": parse_bool(metrics.get("mirror_supported")),
        "doubles": doubles if doubles is not None else 0,
    }


def compute_cross_section_echo(tokens_map: Dict[str, Set[str]]) -> Dict[str, int]:
    echo: Dict[str, int] = {}
    sections = list(tokens_map.keys())
    for name in sections:
        mine = tokens_map[name]
        others = set().union(*(tokens_map[other] for other in sections if other != name)) if len(sections) > 1 else set()
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


def main() -> int:
    parser = argparse.ArgumentParser(description="V-TRAC validator → compact scorer/exporter")
    parser.add_argument(
        "paths",
        nargs="*",
        default=DEFAULT_INPUTS,
        help="Files/directories containing validation_report.json (searches recursively).",
    )
    parser.add_argument(
        "--config",
        help="Optional JSON overriding weights/priors (see configs/vtrac_score_config.json).",
    )
    parser.add_argument(
        "--out-dir",
        help="Directory for vtrac_compact_report.{json,csv}. Defaults to first resolved input directory.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose (DEBUG) logging output.",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(levelname)s %(message)s")

    reports = discover_reports(args.paths)
    if not reports:
        logging.error("No validation_report.json files found under %s", ", ".join(args.paths))
        return 1

    config = load_config(args.config)

    weights = {**DEFAULT_WEIGHTS, **{k: float(v) for k, v in config["weights"].items()}}
    col_weights = {**DEFAULT_COL_WEIGHTS, **{int(k): float(v) for k, v in config["col_weights"].items()}}
    section_priors = {**DEFAULT_SECTION_PRIORS, **{str(k): float(v) for k, v in config["section_priors"].items()}}
    state_priors = {str(k): float(v) for k, v in config["state_priors"].items()}

    output_dir = Path(args.out_dir) if args.out_dir else reports[0].parent
    output_dir.mkdir(parents=True, exist_ok=True)

    staged: List[dict] = []
    for report_path in reports:
        payload = json.loads(report_path.read_text())
        state = payload.get("state") or report_path.parent.name
        date = payload.get("generated_at", "")
        section_names = list((payload.get("sections") or {}).keys())

        winners_tokens_by_section: Dict[str, Set[str]] = {}
        analyzer_tokens_by_section: Dict[str, Set[str]] = {}

        for section in section_names:
            winners_tokens, analyzer_tokens = tokens_for_section(payload, section)
            winners_tokens_by_section[section] = set(winners_tokens)
            analyzer_tokens_by_section[section] = set(analyzer_tokens)

        staged.append(
            {
                "__path__": report_path,
                "__state__": state,
                "__date__": date,
                "__sections__": {
                    "winners_tokens": winners_tokens_by_section,
                    "analyzer_tokens": analyzer_tokens_by_section,
                },
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
        section_names = list((payload.get("sections") or {}).keys())

        raw_mask_values: List[float] = []
        raw_doubles_values: List[float] = []
        tokens_map: Dict[str, Set[str]] = {}
        section_cache: Dict[str, dict] = {}

        for section in section_names:
            winners_tokens, analyzer_tokens = tokens_for_section(payload, section)
            metrics = metrics_for_section(payload, section)
            tokens_map[section] = set(winners_tokens) | set(analyzer_tokens)
            section_cache[section] = {
                "winners_tokens": winners_tokens,
                "analyzer_tokens": analyzer_tokens,
                "metrics": metrics,
            }
            raw_mask_values.append(to_float(metrics["mask_drop"]))
            raw_doubles_values.append(to_float(metrics["doubles"]))

        mask_min, mask_max = (min(raw_mask_values), max(raw_mask_values)) if raw_mask_values else (0.0, 0.0)
        doubles_min, doubles_max = (min(raw_doubles_values), max(raw_doubles_values)) if raw_doubles_values else (0.0, 0.0)
        echo_by_section = compute_cross_section_echo(tokens_map)

        state_prior = state_priors.get(state, 1.0)

        for section in section_names:
            cache_entry = section_cache[section]
            winners_tokens = cache_entry["winners_tokens"]
            analyzer_tokens = cache_entry["analyzer_tokens"]
            metrics = cache_entry["metrics"]

            overlap = len(set(winners_tokens) & set(analyzer_tokens))
            stable_cols = metrics["stable_cols"]
            stability_value = stable_score(stable_cols, col_weights)
            consensus_count = int(metrics["consensus_col1"]) + int(metrics["consensus_col2"])

            hot_count = metrics["hot_count"]
            superhot_count = metrics["superhot_count"]
            hot_value = to_int(hot_count) if hot_count is not None else to_int(metrics["hot"])
            superhot_value = to_int(superhot_count) if superhot_count is not None else to_int(metrics["superhot"])
            hot_norm = min(hot_value / 8.0, 1.0) if hot_value else 0.0
            super_norm = min(superhot_value / 12.0, 1.0) if superhot_value else 0.0

            mask_norm = norm01(to_float(metrics["mask_drop"]), mask_min, mask_max)
            mirror_value = 1.0 if metrics["mirror"] else 0.0
            doubles_norm = norm01(to_float(metrics["doubles"]), doubles_min, doubles_max)
            echo_value = echo_by_section.get(section, 0)

            components: List[Tuple[str, float, float]] = [
                ("overlap", weights["overlap"], float(overlap)),
                ("stable", weights["stable"], stability_value),
                ("consensus", weights["consensus"], float(consensus_count) if stable_cols else 0.0),
                ("echo", weights["token_echo"], float(echo_value)),
                ("hot", weights["hot"], hot_norm),
                ("superhot", weights["super"], super_norm),
                ("mask_drop", weights["mask"], mask_norm),
                ("mirror", weights["mirror"], mirror_value),
                ("doubles", weights["doubles"], doubles_norm),
            ]

            base_score = sum(weight * value for _, weight, value in components)
            section_prior = section_priors.get(section, 1.0)
            score = base_score * section_prior * state_prior

            flags: List[str] = []
            rescue_multiplier = 1.0
            if overlap == 0 and consensus_count >= 1 and stable_cols:
                rescue_multiplier = weights["rescue_multiplier"]
                score *= rescue_multiplier
                flags.append("weak_positive_rescue")
            if overlap == 0:
                flags.append("zero_overlap")

            tier = tier_from_overlap(overlap)

            union_tokens = set(winners_tokens) | set(analyzer_tokens)
            token_scores: List[Tuple[float, str]] = []
            for token in union_tokens:
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

            straights = straight_list_for_section(payload, section)

            why_parts: List[str] = [
                f"{label}={value:.3f}*{weight:.2f}->{weight * value:.2f}"
                for (label, weight, value) in components
                if value > 0.0
            ]
            why_parts.append(f"section_prior={section_prior:.2f}")
            if not math.isclose(state_prior, 1.0):
                why_parts.append(f"state_prior={state_prior:.2f}")
            if not math.isclose(rescue_multiplier, 1.0):
                why_parts.append(f"rescue_multiplier={rescue_multiplier:.2f}")

            rows.append(
                {
                    "date": date,
                    "state": state,
                    "section": section,
                    "overlap": overlap,
                    "stable_cols_count": len(stable_cols),
                    "stable_cols": stable_cols,
                    "consensus_col1": metrics["consensus_col1"],
                    "consensus_col2": metrics["consensus_col2"],
                    "cross_section_echo": echo_value,
                    "hot_count": hot_value,
                    "superhot_count": superhot_value,
                    "mask_drop": metrics["mask_drop"],
                    "mirror_supported": metrics["mirror"],
                    "double_hits": metrics["doubles"],
                    "confidence_score": round(score, 3),
                    "tier": tier,
                    "flags": flags,
                    "top_tokens": winners_tokens,
                    "recommended_tokens": recommended_tokens,
                    "top_straights": straights,
                    "section_prior": section_prior,
                    "state_prior": state_prior,
                    "why": "; ".join(why_parts),
                    "source": report_path.name,
                }
            )

    out_json = output_dir / "vtrac_compact_report.json"
    out_csv = output_dir / "vtrac_compact_report.csv"

    out_json.write_text(json.dumps(rows, indent=2))

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
        "section_prior",
        "state_prior",
        "why",
        "source",
    ]

    def csv_escape(value) -> str:
        text = value if isinstance(value, str) else json.dumps(value, separators=(",", ":"))
        if any(ch in text for ch in {",", '"', "\n"}):
            text = '"' + text.replace('"', '""') + '"'
        return text

    with out_csv.open("w", encoding="utf-8", newline="") as handle:
        handle.write(",".join(headers) + "\n")
        for row in rows:
            handle.write(",".join(csv_escape(row[column]) for column in headers) + "\n")

    logging.info("Wrote %d rows", len(rows))
    logging.info(" - JSON: %s", out_json)
    logging.info(" - CSV : %s", out_csv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
