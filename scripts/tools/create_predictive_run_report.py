#!/usr/bin/env python3
"""
Create an arena-native per-state predictive run report.

This is the pre-results companion for the Analysis Arena branch. It reads the
frozen predictive-day sharepack and writes a Markdown review shell that is
anchored to:

- aggregated analysis arena
- translation sandbox seed
- raw string/context tool artifacts
- Candidate Universe / Play Card as the control arm

It does NOT rerun analyzers or rebuild sharepacks.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date as _date
from datetime import timedelta
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.tools.brain2_rank_contract import (
    display_order_contract_from_row,
    rank_contract_from_row,
)

RUNS2_PREDICTIVE_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2" / "PREDICTIVE"
FINAL_DOCS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
SYSTEM_MAP_PATH = FINAL_DOCS_DIR / "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md"
OPERATING_FLOW_PATH = FINAL_DOCS_DIR / "AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md"
CADENCE_QUICKSTART_PATH = FINAL_DOCS_DIR / "AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md"
ARENA_CONTRACT_PATH = FINAL_DOCS_DIR / "AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md"
CONTEXT_FEED_PATH = FINAL_DOCS_DIR / "AAT9_FINAL_CONTEXT_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md"
STRING_FEED_PATH = FINAL_DOCS_DIR / "AAT9_FINAL_STRING_TOOL_OUTPUTS__ANALYSIS_ARENA_FEED.md"
TRANSLATION_TEMPLATE_PATH = FINAL_DOCS_DIR / "AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md"


def parse_iso_date(value: str) -> _date:
    try:
        return _date.fromisoformat(value)
    except ValueError as exc:
        raise SystemExit(f"Invalid --date (expected YYYY-MM-DD): {value}") from exc


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> Any:
    return json.loads(read_text(path))


def try_read_json(path: Path) -> Any | None:
    if not path.exists():
        return None
    return read_json(path)


def safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def normalize_tag(value: str) -> str:
    raw = str(value or "").strip()
    if raw.lower() in {"", "-", "none", "null"}:
        return ""
    return raw.replace(" ", "_")


def _profile_suffix(profile: str) -> str:
    p = str(profile or "mixed").strip()
    return "" if p == "mixed" else f"__{p}"


def _tag_suffix(experiment_tag: str) -> str:
    return f"__{experiment_tag}" if experiment_tag else ""


def _preferred_path(base_dir: Path, stem: str, ext: str, *, profile: str, experiment_tag: str) -> Path:
    out_suffix = _profile_suffix(profile)
    tag_suffix = _tag_suffix(experiment_tag)
    tagged = base_dir / f"{stem}{out_suffix}{tag_suffix}.{ext}"
    if tagged.exists():
        return tagged
    untagged = base_dir / f"{stem}{out_suffix}.{ext}"
    return untagged


def _ordered_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        value = str(value or "").strip()
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def _fmt_items(values: Sequence[str], *, empty: str = "_none_") -> str:
    ordered = _ordered_unique(values)
    if not ordered:
        return empty
    return ", ".join(f"`{value}`" for value in ordered)


def _fmt_path(path: Path) -> str:
    suffix = "" if path.exists() else " (missing)"
    return f"[`{safe_rel(path)}`]({path.resolve()}){suffix}"


def _fmt_paths(paths: Sequence[Path], *, empty: str = "_none_") -> str:
    ordered = []
    seen: set[str] = set()
    for path in paths:
        key = str(path.resolve())
        if key in seen:
            continue
        seen.add(key)
        ordered.append(_fmt_path(path))
    if not ordered:
        return empty
    return ", ".join(ordered)


def _ranked_values(items: Any, *, value_key: str = "value", limit: int = 6) -> list[str]:
    if not isinstance(items, list):
        return []
    out: list[str] = []
    for item in items[:limit]:
        if isinstance(item, Mapping):
            value = item.get(value_key)
        else:
            value = item
        value_s = str(value or "").strip()
        if value_s:
            out.append(value_s)
    return out


def _watchlist_summary(items: Any, *, limit: int = 5) -> list[str]:
    if not isinstance(items, list):
        return []
    out: list[str] = []
    for item in items[:limit]:
        if not isinstance(item, Mapping):
            continue
        idx = str(item.get("vtrac_index") or "").strip()
        candidates = ",".join(item.get("candidate_canonicals") or [])
        if idx or candidates:
            out.append(f"{idx}->{candidates or '-'}")
    return out


def _state_regime_summary(state_regime: Any) -> list[str]:
    if not isinstance(state_regime, Mapping):
        return []
    out: list[str] = []
    for key in [
        "dominant_canonical",
        "dominant_family",
        "dominant_vtrac_index",
        "tracker_posture",
        "survivor_pressure",
        "last_remaining",
        "hidden_terminal_support",
    ]:
        if key in state_regime:
            out.append(f"{key}={state_regime.get(key)}")
    return out


def _survivor_summary(data: Any) -> list[str]:
    if not isinstance(data, Mapping) or not data.get("available"):
        return ["available=false"]
    return [
        f"frontier_rows={data.get('frontier_rows', 0)}",
        f"progressions={data.get('progression_count', 0)}",
        f"last_remaining_rows={data.get('last_remaining_rows', 0)}",
        f"hidden_terminal_frontiers={data.get('hidden_terminal_frontier_count', 0)}",
        f"top_frontier_canonicals={','.join((data.get('top_frontier_canonicals') or [])[:6]) or '-'}",
    ]


def _r_consensus_summary(data: Any) -> list[str]:
    if not isinstance(data, Mapping) or not data.get("available"):
        return ["available=false"]
    return [
        f"events={data.get('event_count', 0)}",
        f"signal_class={data.get('signal_strength_class', 'unknown')}",
        f"trial_eligible={data.get('trial_eligible', False)}",
        f"top_tails={','.join((data.get('top_tail_values') or [])[:6]) or '-'}",
        f"top_support={','.join((data.get('top_support_canonicals') or [])[:6]) or '-'}",
    ]


def _candidate_universe_summary(raw: Mapping[str, Any] | None) -> list[str]:
    if not isinstance(raw, Mapping):
        return ["Candidate Universe missing."]
    packs = raw.get("packs")
    packs_count = len(packs) if isinstance(packs, list) else 0
    union_count = raw.get("union_combos_count")
    try:
        union_count_int = int(union_count)
    except Exception:
        union = raw.get("union_combos")
        union_count_int = len(union) if isinstance(union, list) else 0
    return [
        f"packs={packs_count}",
        f"union_combos={union_count_int}",
        f"contains_winners_artifacts={bool(raw.get('contains_winners_artifacts'))}",
    ]


def _play_card_summary(raw: Mapping[str, Any] | None) -> list[str]:
    if not isinstance(raw, Mapping):
        return ["Play Card missing."]
    strategies = raw.get("strategies")
    if not isinstance(strategies, Mapping):
        return ["Play Card has no strategies map."]
    labels: list[str] = []
    for strategy_name, strat in list(strategies.items())[:4]:
        budgets: list[str] = []
        if isinstance(strat, Mapping):
            budgets = [key for key, value in strat.items() if isinstance(value, Mapping)]
        labels.append(f"{strategy_name}[{','.join(budgets[:4]) or '-'}]")
    return labels or ["Play Card strategies unavailable."]


def _due_family_summary(rows: Any, *, limit: int = 4) -> list[str]:
    if not isinstance(rows, list):
        return []
    out: list[str] = []
    for row in rows[:limit]:
        if not isinstance(row, Mapping):
            continue
        variant = str(row.get("variant") or "").strip() or "?"
        draws_since = row.get("draws_since_double")
        families = row.get("families") or []
        family_labels: list[str] = []
        if isinstance(families, list):
            for family in families[:3]:
                if not isinstance(family, Mapping):
                    continue
                label = str(family.get("family") or "").strip()
                if label:
                    family_labels.append(label)
        suffix = f":{','.join(family_labels)}" if family_labels else ""
        out.append(f"{variant}:{draws_since}{suffix}")
    return out


def load_history_date(day_dir: Path, *, results_date: str) -> str:
    meta_path = day_dir / "control_center" / "meta.json"
    if meta_path.exists():
        raw = try_read_json(meta_path)
        if isinstance(raw, Mapping):
            history_date = str(raw.get("history_date") or "").strip()
            if history_date:
                return history_date
    d = parse_iso_date(results_date)
    return (d - timedelta(days=1)).isoformat()


def build_predictive_run_report(
    *,
    results_date: str,
    state: str,
    profile: str,
    experiment_tag: str,
    sharepacks_root: Path,
) -> str:
    day_dir = sharepacks_root / results_date
    state_dir = day_dir / state
    analysis_dir = state_dir / "analysis"
    history_date = load_history_date(day_dir, results_date=results_date)

    aggregated_json = _preferred_path(
        analysis_dir,
        "aggregated_analysis_arena",
        "json",
        profile=profile,
        experiment_tag=experiment_tag,
    )
    aggregated_md = aggregated_json.with_suffix(".md")
    sandbox_json = _preferred_path(
        analysis_dir,
        "translation_sandbox_seed",
        "json",
        profile=profile,
        experiment_tag=experiment_tag,
    )
    sandbox_md = sandbox_json.with_suffix(".md")
    candidate_universe_json = _preferred_path(
        state_dir,
        "candidate_universe",
        "json",
        profile=profile,
        experiment_tag=experiment_tag,
    )
    play_card_json = _preferred_path(
        state_dir,
        "play_card",
        "json",
        profile=profile,
        experiment_tag=experiment_tag,
    )
    play_card_md = play_card_json.with_suffix(".md")
    signals_bundle_json = _preferred_path(
        state_dir,
        "signals_bundle",
        "json",
        profile=profile,
        experiment_tag=experiment_tag,
    )
    aux_summary_json = state_dir / "aux" / state / "summary.json"
    aux_summary_md = state_dir / "aux" / state / "summary.md"

    aggregated = try_read_json(aggregated_json)
    sandbox = try_read_json(sandbox_json)
    candidate_universe = try_read_json(candidate_universe_json)
    play_card = try_read_json(play_card_json)

    arena_synthesis = (aggregated or {}).get("arena_synthesis") or {}
    dominant_canonicals = _ranked_values(arena_synthesis.get("dominant_canonicals"))
    dominant_families = _ranked_values(arena_synthesis.get("dominant_families"))
    dominant_vtrac = _ranked_values(arena_synthesis.get("dominant_vtrac_indices"))
    reinforced = _ranked_values(arena_synthesis.get("context_reinforced_canonicals"))
    context_only = _ranked_values(arena_synthesis.get("context_only_pressure"))
    state_regime = _state_regime_summary(arena_synthesis.get("state_regime"))
    watchlist = _watchlist_summary(arena_synthesis.get("vtrac_literal_watchlist"))
    survivor = _survivor_summary(arena_synthesis.get("stable_survivor_context"))
    consensus = _r_consensus_summary(arena_synthesis.get("r_consensus_context"))

    brain2_context = (sandbox or {}).get("brain2_context") or {}
    scoreboard_row = brain2_context.get("scoreboard_row") or {}
    sandbox_hyp = (sandbox or {}).get("sandbox_hypotheses") or {}

    boxed_seed = [str((row or {}).get("value") or "") for row in (sandbox_hyp.get("diagnostic_boxed_seed") or [])]
    straight_seed = [str((row or {}).get("value") or "") for row in (sandbox_hyp.get("diagnostic_straight_seed") or [])]
    vt_seed = [str((row or {}).get("value") or "") for row in (sandbox_hyp.get("diagnostic_vt_box_seed") or [])]
    top_profit = []
    for row in (brain2_context.get("top_profit_alerts") or [])[:5]:
        if not isinstance(row, Mapping):
            continue
        top_profit.append(
            ":".join(
                part
                for part in [
                    str(row.get("variant") or "").strip(),
                    str(row.get("alert_id") or "").strip(),
                    str(row.get("canonical") or "").strip(),
                    str(row.get("suggested") or "").strip(),
                ]
                if part
            )
        )

    top_compound = []
    for row in (brain2_context.get("compound_events_top") or [])[:4]:
        if not isinstance(row, Mapping):
            continue
        top_compound.append(
            ":".join(
                part
                for part in [
                    str(row.get("variant") or "").strip(),
                    str(row.get("top_event") or "").strip(),
                    f"P{row.get('priority')}" if row.get("priority") is not None else "",
                ]
                if part
            )
        )

    lines: list[str] = []
    lines.append(f"# Analysis Arena Predictive Run Report — {state} — D={results_date} (H={history_date})")
    lines.append("")
    lines.append("Purpose")
    lines.append("- Capture the pre-results state thesis for the Analysis Arena branch from the actual predictive-day sharepack.")
    lines.append("- Preserve Brain 1, Brain 2 carry-through, translation-sandbox seeds, and the downstream control arm in one state-local artifact.")
    lines.append("- This is the arena-era replacement for the older predictive run shell.")
    lines.append("")
    lines.append("Template / SSOT anchors")
    lines.append(f"- Arena system map: {_fmt_path(SYSTEM_MAP_PATH)}")
    lines.append(f"- Arena operating flow: {_fmt_path(OPERATING_FLOW_PATH)}")
    lines.append(f"- Arena cadence quickstart: {_fmt_path(CADENCE_QUICKSTART_PATH)}")
    lines.append(f"- Aggregated arena contract: {_fmt_path(ARENA_CONTRACT_PATH)}")
    lines.append(f"- Context-tool arena feed: {_fmt_path(CONTEXT_FEED_PATH)}")
    lines.append(f"- String-tool arena feed: {_fmt_path(STRING_FEED_PATH)}")
    lines.append(f"- Translation sandbox companion: {_fmt_path(TRANSLATION_TEMPLATE_PATH)}")
    lines.append("")
    lines.append("Scope")
    lines.append(f"- Results date `D`: `{results_date}`")
    lines.append(f"- History date `H`: `{history_date}`")
    lines.append(f"- State: `{state}`")
    lines.append(f"- Predictive sharepacks root: `{safe_rel(sharepacks_root)}`")
    lines.append(f"- State sharepack dir: `{safe_rel(state_dir)}`")
    lines.append(f"- Profile: `{profile}`")
    lines.append(f"- Experiment tag: `{experiment_tag or 'untagged'}`")
    lines.append("")
    lines.append("## File Lock")
    lines.append("")
    lines.append(f"- Aggregated arena JSON: {_fmt_path(aggregated_json)}")
    lines.append(f"- Aggregated arena MD: {_fmt_path(aggregated_md)}")
    lines.append(f"- Translation sandbox JSON: {_fmt_path(sandbox_json)}")
    lines.append(f"- Translation sandbox MD: {_fmt_path(sandbox_md)}")
    lines.append(f"- Candidate Universe JSON: {_fmt_path(candidate_universe_json)}")
    lines.append(f"- Play Card JSON: {_fmt_path(play_card_json)}")
    lines.append(f"- Play Card MD: {_fmt_path(play_card_md)}")
    lines.append(f"- Signals bundle JSON: {_fmt_path(signals_bundle_json)}")
    lines.append(f"- Aux summary JSON: {_fmt_path(aux_summary_json)}")
    lines.append(f"- Aux summary MD: {_fmt_path(aux_summary_md)}")
    lines.append("")
    lines.append("## Raw Tool Review Surfaces")
    lines.append("")
    lines.append(f"- Stable scores CSV: {_fmt_path(state_dir / 'stable' / state / f'{state}_stable_patterns_scores.csv')}")
    lines.append(f"- Stable families CSV: {_fmt_path(state_dir / 'stable' / state / f'{state}_stable_patterns_families.csv')}")
    lines.append(f"- Stable report HTML: {_fmt_path(state_dir / 'stable' / state / f'{state}_stable_patterns_report.html')}")
    lines.append(f"- Digit Reduction scores CSV: {_fmt_path(state_dir / 'digit_reduction' / state / f'{state}_digit_reduction_scores.csv')}")
    lines.append(f"- Digit Reduction report HTML: {_fmt_path(state_dir / 'digit_reduction' / state / f'{state}_digit_reduction_report.html')}")
    lines.append(f"- VTRAC enhanced JSON: {_fmt_paths(sorted((state_dir / 'vtrac' / state).glob(f'{state}_vtrac_enhanced_*.json')), empty='_(none found)_')}")
    lines.append(f"- Hot Zones top lanes CSV: {_fmt_path(state_dir / 'hot_zones' / state / f'{state}_hot_zones_top_lanes.csv')}")
    lines.append("")
    lines.append("## Brain 1 — Aggregated Analysis Arena Snapshot")
    lines.append("")
    lines.append(f"- Dominant canonicals: {_fmt_items(dominant_canonicals)}")
    lines.append(f"- Dominant families: {_fmt_items(dominant_families)}")
    lines.append(f"- Dominant VTRAC indices: {_fmt_items(dominant_vtrac)}")
    lines.append(f"- Context-reinforced canonicals: {_fmt_items(reinforced)}")
    lines.append(f"- Context-only pressure: {_fmt_items(context_only)}")
    lines.append(f"- State regime: {_fmt_items(state_regime)}")
    lines.append(f"- Stable survivor context: {_fmt_items(survivor)}")
    lines.append(f"- R-Consensus context: {_fmt_items(consensus)}")
    lines.append(f"- VTRAC literal watchlist: {_fmt_items(watchlist)}")
    lines.append("")
    lines.append("## Brain 2 Carry-Through / Translation Sandbox")
    lines.append("")
    rank_contract = rank_contract_from_row(scoreboard_row)
    display_contract = display_order_contract_from_row(scoreboard_row)
    scoreboard_summary = [
        f"display_order={display_contract.get('display_order') or '-'}",
        f"legacy_rank={scoreboard_row.get('legacy_static_rank') or scoreboard_row.get('score_rank') or '-'}",
        f"analytical_rank={rank_contract.get('analytical_rank') or '-'}",
        f"rank_integrity={rank_contract.get('rank_integrity_status') or '-'}",
        f"role={scoreboard_row.get('role', '-')}",
        f"bucket={scoreboard_row.get('targeting_bucket', '-')}",
        f"tracker={scoreboard_row.get('tracker_posture', '-')}",
    ]
    lines.append(f"- Scoreboard row: {_fmt_items(scoreboard_summary)}")
    lines.append(f"- Scoreboard top canonicals: {_fmt_items(scoreboard_row.get('top_canonicals') or [])}")
    lines.append(f"- Scoreboard top VTRAC indices: {_fmt_items(scoreboard_row.get('top_vtrac_indices') or [])}")
    lines.append(f"- Positional shortlist top: {_fmt_items([str((row or {}).get('canonical') or '') for row in (brain2_context.get('positional_shortlist_top') or [])])}")
    lines.append(f"- Blackapple recommended canonicals: {_fmt_items(brain2_context.get('blackapple_recommended_canonicals') or [])}")
    lines.append(f"- Profit-alert implied canonicals: {_fmt_items(brain2_context.get('profit_alert_implied_canonicals') or [])}")
    lines.append(f"- Due-double family pressure: {_fmt_items(_due_family_summary(brain2_context.get('due_double_families')))}")
    lines.append(f"- Due-double example canonicals: {_fmt_items(brain2_context.get('due_double_example_canonicals') or [])}")
    lines.append(f"- Top profit alerts: {_fmt_items(top_profit)}")
    lines.append(f"- Top compound events: {_fmt_items(top_compound)}")
    lines.append(f"- Diagnostic boxed seed: {_fmt_items(boxed_seed)}")
    lines.append(f"- Diagnostic straight seed: {_fmt_items(straight_seed)}")
    lines.append(f"- Diagnostic VT-box seed: {_fmt_items(vt_seed)}")
    lines.append("")
    lines.append("## Arena-Preserved Truth vs Control-Arm Expression")
    lines.append("")
    lines.append(
        f"- Arena-preserved boxed canonicals to watch: {_fmt_items(_ordered_unique(dominant_canonicals[:4] + reinforced[:4] + boxed_seed[:8]))}"
    )
    lines.append(
        f"- Arena-preserved straight canonicals to watch: {_fmt_items(_ordered_unique(straight_seed[:8] + reinforced[:4]))}"
    )
    lines.append(
        "- Interpretation rule: Brain 1 dominant canonicals, Brain 2 carry-through, and diagnostic seeds describe what the Arena preserved before results."
    )
    lines.append(
        "- Control-arm rule: Candidate Universe and Play Card remain baseline expression surfaces only; they do not define Arena truth."
    )
    lines.append(
        "- Review test: compare the preserved box/straight pressure above to what the control arm narrows or suppresses below."
    )
    lines.append("")
    lines.append("## Downstream Control Arm Snapshot")
    lines.append("")
    lines.append(f"- Candidate Universe: {_fmt_items(_candidate_universe_summary(candidate_universe if isinstance(candidate_universe, Mapping) else None))}")
    lines.append(f"- Play Card: {_fmt_items(_play_card_summary(play_card if isinstance(play_card, Mapping) else None))}")
    lines.append("")
    lines.append("## Analyst Notes")
    lines.append("")
    lines.append("- Strongest Brain 1 state thesis: `...`")
    lines.append("- Strongest context reinforcement or tracker carry-through: `...`")
    lines.append("- Is this state more boxed, straight, or VT-box leaning?: `...`")
    lines.append("- What did the arena preserve that the control arm may compress later?: `...`")
    lines.append("- Any anomalies, missing artifacts, or drift to check before results?: `...`")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Create an arena-native predictive run report for one state/day.")
    ap.add_argument("--date", required=True, help="Predictive sharepack results date D (YYYY-MM-DD)")
    ap.add_argument("--state", required=True, help="State key (e.g. NewJersey4)")
    ap.add_argument("--profile", default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Predictive sharepacks root directory (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--out",
        default=None,
        help="Override output path (default: RUNS_2/PREDICTIVE/<D>__<STATE>__PREDICTIVE{__profile}{__tag}.md)",
    )
    ap.add_argument("--force", action="store_true", help="Overwrite an existing file (default: refuse).")
    return ap.parse_args()


def main() -> None:
    args = parse_args()
    results_date = parse_iso_date(args.date).isoformat()
    profile = str(args.profile or "tool_only").strip()
    experiment_tag = normalize_tag(args.experiment_tag)

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()

    day_dir = sharepacks_root / results_date
    if not day_dir.exists():
        raise SystemExit(f"Missing sharepack day dir: {safe_rel(day_dir)}")
    state_dir = day_dir / args.state
    if not state_dir.exists():
        raise SystemExit(f"Missing sharepack state dir: {safe_rel(state_dir)}")

    RUNS2_PREDICTIVE_DIR.mkdir(parents=True, exist_ok=True)
    default_out = RUNS2_PREDICTIVE_DIR / (
        f"{results_date}__{args.state}__PREDICTIVE{_profile_suffix(profile)}{_tag_suffix(experiment_tag)}.md"
    )
    out_path = Path(args.out) if args.out else default_out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not args.force:
        raise SystemExit(f"Predictive run report already exists: {safe_rel(out_path)} (use --force to overwrite).")

    report = build_predictive_run_report(
        results_date=results_date,
        state=args.state,
        profile=profile,
        experiment_tag=experiment_tag,
        sharepacks_root=sharepacks_root,
    )
    out_path.write_text(report, encoding="utf-8")
    print(f"Wrote: {safe_rel(out_path)}")


if __name__ == "__main__":
    main()
