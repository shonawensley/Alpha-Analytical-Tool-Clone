#!/usr/bin/env python3
"""
Create an Analysis Arena predictive portfolio report for one day D.

This is a reporting-only tool:
- reads existing predictive sharepack artifacts
- summarizes cross-state Brain 1 / Brain 2 posture
- keeps Candidate Universe / Play Card visible as the downstream control arm

It does NOT rerun analyzers or rebuild sharepacks.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

from scripts.tools.brain2_rank_contract import (
    DISPLAY_ORDER_SOURCE_INPUT_ROSTER,
    analytical_rank,
    rank_contract_from_row,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS2_PREDICTIVE_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "RUNS_2" / "PREDICTIVE"
FINAL_DOCS_DIR = REPO_ROOT / "docs" / "AAT9_KIT" / "FINAL VALIDATION" / "final docs"
SYSTEM_MAP_PATH = FINAL_DOCS_DIR / "AAT9_ANALYSIS_ARENA_BRANCH__SYSTEM_MAP.md"
OPERATING_FLOW_PATH = FINAL_DOCS_DIR / "AAT9_ANALYSIS_ARENA_OPERATING_FLOW__FRESH_RUNS.md"
CADENCE_QUICKSTART_PATH = FINAL_DOCS_DIR / "AAT9_ANALYSIS_ARENA_FRESH_RUNS_CADENCE__QUICKSTART.md"
ARENA_CONTRACT_PATH = FINAL_DOCS_DIR / "AAT9_AGGREGATED_ANALYSIS_ARENA_CONTRACT_v0.md"
TRANSLATION_TEMPLATE_PATH = FINAL_DOCS_DIR / "AAT9_TRANSLATION_SANDBOX_TEMPLATE__ANALYSIS_ARENA_BRANCH.md"


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_json(path: Path) -> object:
    return json.loads(_read_text(path))


def _try_read_json(path: Path) -> object | None:
    if not path.exists():
        return None
    return _read_json(path)


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _load_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def _normalize_pick3(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _canon(value: str) -> str:
    v = _normalize_pick3(value)
    return "".join(sorted(v)) if v else ""


def _profile_suffix(profile: str) -> str:
    p = str(profile or "mixed").strip()
    return "" if p == "mixed" else f"__{p}"


def _normalize_experiment_tag(value: str) -> str:
    raw = str(value or "").strip()
    if raw.lower() in {"", "-", "none", "null"}:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw).strip("_-")
    if not cleaned:
        raise SystemExit(f"Invalid experiment tag: {value!r}")
    return cleaned[:60]


def _tag_suffix(experiment_tag: str) -> str:
    return f"__{experiment_tag}" if experiment_tag else ""


def _analysis_artifact_path(
    state_dir: Path,
    *,
    stem: str,
    profile: str,
    experiment_tag: str,
    ext: str,
) -> Path:
    out_suffix = _profile_suffix(profile)
    tag_suffix = _tag_suffix(experiment_tag)
    tagged = state_dir / "analysis" / f"{stem}{out_suffix}{tag_suffix}.{ext}"
    if tagged.exists():
        return tagged
    return state_dir / "analysis" / f"{stem}{out_suffix}.{ext}"


def _ordered_unique(values: Sequence[str]) -> List[str]:
    seen: set[str] = set()
    out: List[str] = []
    for value in values:
        value = str(value or "").strip()
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def _candidate_universe_path(state_dir: Path, *, profile: str, experiment_tag: str) -> Path:
    return state_dir / f"candidate_universe{_profile_suffix(profile)}{_tag_suffix(experiment_tag)}.json"


def _play_card_path(state_dir: Path, *, profile: str, experiment_tag: str) -> Path:
    return state_dir / f"play_card{_profile_suffix(profile)}{_tag_suffix(experiment_tag)}.json"


def _load_candidate_universe_summary_tagged(
    state_dir: Path,
    *,
    profile: str,
    prefer_experiment_tags: Sequence[str],
) -> Tuple[int, int, List[str], int, List[str]]:
    cu: Optional[Path] = None
    for tag in prefer_experiment_tags:
        cand = _candidate_universe_path(state_dir, profile=profile, experiment_tag=tag)
        if cand.exists():
            cu = cand
            break
    if cu is None:
        return 0, 0, [], 0, []
    raw = _read_json(cu)
    if not isinstance(raw, dict):
        return 0, 0, [], 0, []
    packs = raw.get("packs")
    packs_list = packs if isinstance(packs, list) else []
    union_count = raw.get("union_combos_count")
    try:
        union_count_int = int(union_count)
    except Exception:
        union = raw.get("union_combos")
        union_count_int = len(union) if isinstance(union, list) else 0

    dd_canon: set[str] = set()
    support: Dict[str, int] = {}
    for p in packs_list:
        if not isinstance(p, dict):
            continue
        method_id = str(p.get("method_id") or "")
        canonicals = p.get("canonicals") or []
        if isinstance(canonicals, list):
            uniq: set[str] = set()
            for c in canonicals:
                cc = _canon(str(c))
                if cc:
                    uniq.add(cc)
            for cc in uniq:
                support[cc] = support.get(cc, 0) + 1

        if method_id != "due_doubles":
            continue
        for c in canonicals or []:
            cc = _canon(str(c))
            if cc:
                dd_canon.add(cc)

    top_support_count = max(support.values(), default=0)
    top_support = [c for c, n in sorted(support.items(), key=lambda x: (-x[1], x[0])) if n == top_support_count][:3]
    return len(packs_list), union_count_int, sorted(dd_canon), top_support_count, top_support


def _load_play_card_cut(
    state_dir: Path,
    *,
    profile: str,
    strategy: str,
    budget: int,
    prefer_experiment_tags: Sequence[str],
) -> Tuple[int, List[str], List[str], List[int], List[str], Optional[Path]]:
    bkey = f"B{int(budget)}"
    for tag in prefer_experiment_tags:
        pc = _play_card_path(state_dir, profile=profile, experiment_tag=tag)
        if not pc.exists():
            continue
        raw = _read_json(pc)
        if not isinstance(raw, dict):
            continue
        strategies = raw.get("strategies")
        if not isinstance(strategies, dict):
            continue
        strat = strategies.get(strategy)
        if not isinstance(strat, dict):
            continue
        card = strat.get(bkey)
        if not isinstance(card, dict):
            continue

        combos_raw = card.get("combos") or []
        combos: List[str] = []
        seen: set[str] = set()
        for value in combos_raw:
            combo = _normalize_pick3(str(value))
            if not combo or combo in seen:
                continue
            combos.append(combo)
            seen.add(combo)

        boxed = sorted({_canon(str(x)) for x in (card.get("boxed_canonicals") or []) if _canon(str(x))})
        try:
            boxed_count = int(card.get("boxed_canonicals_count"))
        except Exception:
            boxed_count = len(boxed)

        vtrac_pack_indices: List[int] = []
        vtrac_pack_combos: List[str] = []
        vtrac_pack = card.get("vtrac_pack")
        if isinstance(vtrac_pack, dict):
            indices_raw = vtrac_pack.get("indices")
            if isinstance(indices_raw, list):
                for x in indices_raw:
                    try:
                        vtrac_pack_indices.append(int(x))
                    except Exception:
                        continue
            try:
                idx = int(vtrac_pack.get("index"))
            except Exception:
                idx = None
            if idx is not None and idx not in vtrac_pack_indices:
                vtrac_pack_indices.append(idx)
            pack_raw = vtrac_pack.get("pack_combos") or []
            if isinstance(pack_raw, list):
                vtrac_pack_combos = [_normalize_pick3(str(x)) for x in pack_raw if _normalize_pick3(str(x))]

        return boxed_count, boxed, combos, sorted(set(vtrac_pack_indices)), vtrac_pack_combos, pc

    return 0, [], [], [], [], None


def _pack_label(pack_indices: Sequence[int], pack_combos: Sequence[str]) -> str:
    uniq = sorted({int(x) for x in (pack_indices or []) if str(x).strip().isdigit()})
    if not uniq:
        return "-"
    size = len(list(pack_combos or []))
    if len(uniq) == 1:
        return f"{uniq[0]}({size})" if size else str(uniq[0])
    head = ",".join(str(x) for x in uniq[:4])
    suffix = "…" if len(uniq) > 4 else ""
    return f"idx[{len(uniq)}]:{head}{suffix}({size})" if size else f"idx[{len(uniq)}]:{head}{suffix}"


def _parse_profit_alerts_for_state(rows: Sequence[Dict[str, str]], *, state_key: str) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for row in rows:
        if (row.get("StateKey") or "").strip() != state_key:
            continue
        suggested = (row.get("Suggested") or "").strip()
        implied_raw = (row.get("ImpliedSet") or "").strip()
        combos: List[str] = []
        if implied_raw.startswith("["):
            try:
                implied = json.loads(implied_raw)
            except Exception:
                implied = []
            if isinstance(implied, list):
                combos = sorted({_normalize_pick3(str(x)) for x in implied if _normalize_pick3(str(x))})
        try:
            strength = int((row.get("Strength") or "0").strip() or "0")
        except Exception:
            strength = 0
        out.append(
            {
                "variant": (row.get("Variant") or "").strip() or "Unknown",
                "alert_id": (row.get("AlertId") or "").strip() or "?",
                "strength": strength,
                "suggested": suggested,
                "canonical": _canon((row.get("Canonical") or "").strip()),
                "combos": combos,
            }
        )
    out.sort(key=lambda item: (-int(item["strength"]), item["variant"], item["alert_id"], item["suggested"]))
    return out


def _ranked_values(items: Any, *, value_key: str = "value", limit: int = 3) -> List[str]:
    if not isinstance(items, list):
        return []
    out: List[str] = []
    for item in items[:limit]:
        if isinstance(item, Mapping):
            value = item.get(value_key)
        else:
            value = item
        value_s = str(value or "").strip()
        if value_s:
            out.append(value_s)
    return out


def _load_arena_state_summary(state_dir: Path, *, profile: str, experiment_tag: str) -> Dict[str, Any]:
    aggregated_path = _analysis_artifact_path(
        state_dir,
        stem="aggregated_analysis_arena",
        profile=profile,
        experiment_tag=experiment_tag,
        ext="json",
    )
    sandbox_path = _analysis_artifact_path(
        state_dir,
        stem="translation_sandbox_seed",
        profile=profile,
        experiment_tag=experiment_tag,
        ext="json",
    )
    aggregated = _try_read_json(aggregated_path)
    sandbox = _try_read_json(sandbox_path)
    arena = (aggregated or {}).get("arena_synthesis") if isinstance(aggregated, Mapping) else {}
    brain2 = (sandbox or {}).get("brain2_context") if isinstance(sandbox, Mapping) else {}
    scoreboard = (brain2 or {}).get("scoreboard_row") if isinstance(brain2, Mapping) else {}
    rank_contract = rank_contract_from_row(scoreboard if isinstance(scoreboard, Mapping) else {})
    top_profit = []
    for row in (brain2.get("top_profit_alerts") or [])[:3] if isinstance(brain2, Mapping) else []:
        if not isinstance(row, Mapping):
            continue
        top_profit.append(
            ":".join(
                part
                for part in [
                    str(row.get("variant") or "").strip(),
                    str(row.get("alert_id") or "").strip(),
                    str(row.get("canonical") or "").strip(),
                ]
                if part
            )
        )
    return {
        "aggregated_json": aggregated_path,
        "sandbox_json": sandbox_path,
        "top_canonicals": _ranked_values((arena or {}).get("dominant_canonicals")),
        "top_families": _ranked_values((arena or {}).get("dominant_families")),
        "top_vtrac": _ranked_values((arena or {}).get("dominant_vtrac_indices")),
        "reinforced": _ranked_values((arena or {}).get("context_reinforced_canonicals")),
        "analytical_rank": rank_contract.get("analytical_rank"),
        "rank_signal_valid": rank_contract.get("rank_signal_valid"),
        "rank_integrity_status": rank_contract.get("rank_integrity_status"),
        "input_order": (
            scoreboard.get("input_order") or scoreboard.get("input_rank")
            if isinstance(scoreboard, Mapping)
            else None
        ),
        "legacy_static_rank": (
            scoreboard.get("legacy_static_rank") or scoreboard.get("score_rank")
            if isinstance(scoreboard, Mapping)
            else None
        ),
        "role": scoreboard.get("role") if isinstance(scoreboard, Mapping) else "",
        "bucket": scoreboard.get("targeting_bucket") if isinstance(scoreboard, Mapping) else "",
        "tracker": scoreboard.get("tracker_posture") if isinstance(scoreboard, Mapping) else "",
        "positional_hint": scoreboard.get("positional_hint") if isinstance(scoreboard, Mapping) else "",
        "profit_hint": scoreboard.get("profit_alert_hint") if isinstance(scoreboard, Mapping) else "",
        "due_hint": scoreboard.get("due_double_hint") if isinstance(scoreboard, Mapping) else "",
        "blackapple_hint": scoreboard.get("blackapple_reco_hint") if isinstance(scoreboard, Mapping) else "",
        "survivor_hint": scoreboard.get("survivor_hint") if isinstance(scoreboard, Mapping) else "",
        "consensus_hint": scoreboard.get("r_consensus_hint") if isinstance(scoreboard, Mapping) else "",
        "top_profit": top_profit,
    }


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Create a cross-state predictive portfolio for the Analysis Arena branch.")
    ap.add_argument("--date", required=True, help="Predictive results/sharepack date D (YYYY-MM-DD)")
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Sharepacks root directory (default: sharepacks/_predictive)",
    )
    ap.add_argument("--profile", choices=["mixed", "tool_only", "profit_only"], default="tool_only")
    ap.add_argument("--experiment-tag", default="arena_v0")
    ap.add_argument(
        "--rank-by",
        choices=["arena_first", "tool_first", "profit_alerts"],
        default=None,
        help="Ranking mode (default: arena_first).",
    )
    ap.add_argument("--out", default=None, help="Override output path.")
    ap.add_argument("--force", action="store_true", help="Overwrite an existing report.")
    ap.add_argument("--top-n-alerts", type=int, default=3)
    ap.add_argument("--top-n-due-doubles", type=int, default=6)
    ap.add_argument("--play-strategy-b12", default="analysis_prefix")
    ap.add_argument("--play-strategy-b24", default="vtrac_pack_boxed_first_laneonly_presetB")
    ap.add_argument(
        "--play-strategy-b36",
        default="v0_2_default_multi_pack_packheavy_spine4_index_tail_spinecap6_spine_taper_6644_split_spine_methods_tail_score_total_first_tail_spread_top14_pos18_22_tail_xlens_inject_methods18_packs22",
    )
    ap.add_argument(
        "--prefer-experiment-tags",
        default=None,
        help="Optional comma-separated experiment tags to prefer for Candidate Universe / Play Card lookup.",
    )
    return ap.parse_args()


def main() -> None:
    args = parse_args()

    sharepacks_root = Path(args.sharepacks_root)
    if not sharepacks_root.is_absolute():
        sharepacks_root = (REPO_ROOT / sharepacks_root).resolve()
    day_dir = sharepacks_root / args.date
    if not day_dir.exists():
        raise SystemExit(f"Missing sharepack day dir: {_safe_rel(day_dir)}")

    cc_dir = day_dir / "control_center"
    pa_rows = _load_csv_rows(cc_dir / "profit_alerts.csv")
    states = sorted(p.name for p in day_dir.iterdir() if p.is_dir() and p.name != "control_center")
    if not states:
        raise SystemExit(f"No states found under: {_safe_rel(day_dir)}")

    profile = str(args.profile or "tool_only").strip()
    experiment_tag = _normalize_experiment_tag(args.experiment_tag)
    rank_by = str(args.rank_by or "arena_first").strip()

    raw_prefer = str(args.prefer_experiment_tags or "").strip()
    prefer_tags: List[str] = [experiment_tag] if experiment_tag else []
    if raw_prefer:
        prefer_tags = []
        for part in raw_prefer.split(","):
            part = part.strip()
            tag = _normalize_experiment_tag(part) if part and part.lower() not in {"-", "none", "null"} else ""
            if tag not in prefer_tags:
                prefer_tags.append(tag)
    if "" not in prefer_tags:
        prefer_tags.append("")
    if "vtracpack_v1" not in prefer_tags:
        prefer_tags.append("vtracpack_v1")

    b12_strategy = str(args.play_strategy_b12).strip() or "analysis_prefix"
    b24_strategy = str(args.play_strategy_b24).strip() or "vtrac_pack_boxed_first_laneonly_presetB"
    b36_strategy = str(args.play_strategy_b36).strip()

    RUNS2_PREDICTIVE_DIR.mkdir(parents=True, exist_ok=True)
    default_out = RUNS2_PREDICTIVE_DIR / (
        f"{args.date}__PREDICTIVE_PORTFOLIO{_profile_suffix(profile)}{_tag_suffix(experiment_tag)}.md"
    )
    out_path = Path(args.out) if args.out else default_out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not args.force:
        raise SystemExit(f"Predictive portfolio already exists: {_safe_rel(out_path)} (use --force to overwrite).")

    table_rows: List[Dict[str, Any]] = []
    for input_order, state_key in enumerate(states, start=1):
        state_dir = day_dir / state_key
        alerts = _parse_profit_alerts_for_state(pa_rows, state_key=state_key)
        packs_count, union_count, dd_canon, top_support_count, top_support = _load_candidate_universe_summary_tagged(
            state_dir,
            profile=profile,
            prefer_experiment_tags=prefer_tags,
        )
        b12_boxed_count, b12_boxed, b12_combos, _, _, _ = _load_play_card_cut(
            state_dir,
            profile=profile,
            strategy=b12_strategy,
            budget=12,
            prefer_experiment_tags=prefer_tags,
        )
        _, _, _, b24_pack_indices, b24_pack_combos, b24_src = _load_play_card_cut(
            state_dir,
            profile=profile,
            strategy=b24_strategy,
            budget=24,
            prefer_experiment_tags=prefer_tags,
        )
        _, _, _, b36_pack_indices, b36_pack_combos, b36_src = _load_play_card_cut(
            state_dir,
            profile=profile,
            strategy=b36_strategy,
            budget=36,
            prefer_experiment_tags=prefer_tags,
        )
        arena = _load_arena_state_summary(state_dir, profile=profile, experiment_tag=experiment_tag)

        top_alerts = alerts[: max(0, int(args.top_n_alerts))]
        alert_labels: List[str] = []
        alert_strength_sum = 0
        for alert in top_alerts:
            alert_strength_sum += int(alert["strength"])
            canon_label = alert["canonical"] or (alert["combos"][0] if alert["combos"] else "-")
            alert_labels.append(
                f"{alert['variant']}:{alert['alert_id']}:{alert['suggested']}:{canon_label}"
            )

        arena_rank_int = analytical_rank(arena)
        legacy_arena_rank = arena.get("legacy_static_rank")

        top_support_label = (
            f"{top_support_count}:{' '.join(top_support)}" if top_support_count and top_support else ("0" if packs_count else "-")
        )
        arena_row_label = (
            f"analytical=#{arena_rank_int} {arena.get('role') or '-'} / {arena.get('bucket') or '-'} / {arena.get('tracker') or '-'}"
            if arena_rank_int is not None
            else f"analytical=unavailable legacy=#{legacy_arena_rank or '-'} {arena.get('role') or '-'} / {arena.get('bucket') or '-'} / {arena.get('tracker') or '-'}"
        )

        table_rows.append(
            {
                "StateKey": state_key,
                "input_order": int(arena.get("input_order") or input_order),
                "alerts_count": len(alerts),
                "alerts_strength_sum_top": alert_strength_sum,
                "alerts_top": "; ".join(alert_labels) if alert_labels else "-",
                "candidate_union": union_count,
                "candidate_packs": packs_count,
                "candidate_top_support": int(top_support_count),
                "candidate_top_support_label": top_support_label,
                "due_doubles_canon": " ".join(dd_canon[: max(0, int(args.top_n_due_doubles))]) if dd_canon else "-",
                "due_doubles_count": len(dd_canon),
                "play_b12_boxed": f"{b12_boxed_count}:{' '.join(b12_boxed[:3])}" if b12_boxed_count else ("0" if b12_combos else "-"),
                "play_b24_pack": _pack_label(b24_pack_indices, b24_pack_combos),
                "play_b36_pack": _pack_label(b36_pack_indices, b36_pack_combos),
                "play_b24_src": _safe_rel(b24_src) if b24_src else "-",
                "play_b36_src": _safe_rel(b36_src) if b36_src else "-",
                "arena_rank": arena_rank_int,
                "arena_legacy_rank": legacy_arena_rank,
                "arena_rank_signal_valid": bool(arena.get("rank_signal_valid")),
                "arena_row_label": arena_row_label,
                "arena_top": " ".join(arena.get("top_canonicals") or []) or "-",
                "arena_vtrac": " ".join(arena.get("top_vtrac") or []) or "-",
                "arena_reinforced": " ".join(arena.get("reinforced") or []) or "-",
                "tracker_hint": " | ".join(
                    part
                    for part in [
                        str(arena.get("positional_hint") or "").strip(),
                        str(arena.get("profit_hint") or "").strip(),
                        str(arena.get("due_hint") or "").strip(),
                        str(arena.get("blackapple_hint") or "").strip(),
                        str(arena.get("survivor_hint") or "").strip(),
                        str(arena.get("consensus_hint") or "").strip(),
                    ]
                    if part
                )
                or "-",
                "top_profit": " ; ".join(arena.get("top_profit") or []) or "-",
            }
        )

    if rank_by == "profit_alerts":
        table_rows.sort(
            key=lambda r: (
                -int(r["alerts_count"]),
                -int(r["alerts_strength_sum_top"]),
                int(r["candidate_union"]),
                str(r["StateKey"]),
            )
        )
    elif rank_by == "tool_first":
        table_rows.sort(
            key=lambda r: (
                -int(r.get("candidate_top_support") or 0),
                int(r["candidate_union"]),
                -int(r.get("due_doubles_count") or 0),
                -int(r["candidate_packs"]),
                str(r["StateKey"]),
            )
        )
    else:
        if any(bool(row.get("arena_rank_signal_valid")) and row.get("arena_rank") is not None for row in table_rows):
            table_rows.sort(
                key=lambda r: (
                    0 if bool(r.get("arena_rank_signal_valid")) and r.get("arena_rank") is not None else 1,
                    int(r.get("arena_rank") or 9999),
                    str(r["StateKey"]),
                )
            )
        else:
            # Deterministic display order only; do not substitute another heuristic.
            table_rows.sort(key=lambda r: (int(r.get("input_order") or 9999), str(r["StateKey"])))

    has_valid_arena_rank = any(
        bool(row.get("arena_rank_signal_valid")) and row.get("arena_rank") is not None
        for row in table_rows
    )
    if rank_by == "arena_first" and has_valid_arena_rank:
        display_order_source = "ANALYTICAL_RANK"
        display_order_is_analytical = True
    elif rank_by == "arena_first":
        display_order_source = DISPLAY_ORDER_SOURCE_INPUT_ROSTER
        display_order_is_analytical = False
    else:
        display_order_source = f"{rank_by.upper()}_HEURISTIC_NON_ANALYTICAL"
        display_order_is_analytical = False
    for display_order, row in enumerate(table_rows, start=1):
        row["display_order"] = display_order
        row["display_order_source"] = display_order_source
        row["display_order_is_analytical"] = display_order_is_analytical

    lines: List[str] = []
    lines.append(f"# Analysis Arena Predictive Portfolio — D={args.date}")
    lines.append("")
    lines.append("Purpose")
    lines.append("- Cross-state pre-results triage for the Analysis Arena branch.")
    lines.append("- Brain 1 / Brain 2 posture is surfaced first; Candidate Universe / Play Card remain the downstream control arm.")
    lines.append(f"- Profile: `{profile}` | experiment tag: `{experiment_tag or 'untagged'}` | rank_by: `{rank_by}`")
    if rank_by == "arena_first" and not has_valid_arena_rank:
        lines.append(
            "- Rank integrity: `NOT_EVALUABLE / INVALID_STATIC_ORDER`; "
            f"display order source is `{display_order_source}` and carries no analytical meaning."
        )
    lines.append("")
    lines.append("SSOT anchors")
    lines.append(f"- Arena system map: `{_safe_rel(SYSTEM_MAP_PATH)}`")
    lines.append(f"- Arena operating flow: `{_safe_rel(OPERATING_FLOW_PATH)}`")
    lines.append(f"- Arena cadence quickstart: `{_safe_rel(CADENCE_QUICKSTART_PATH)}`")
    lines.append(f"- Aggregated arena contract: `{_safe_rel(ARENA_CONTRACT_PATH)}`")
    lines.append(f"- Translation sandbox companion: `{_safe_rel(TRANSLATION_TEMPLATE_PATH)}`")
    lines.append("")
    lines.append("Evidence roots")
    lines.append(f"- Predictive sharepacks root: `{_safe_rel(sharepacks_root)}`")
    lines.append(f"- Control Center profit alerts: `{_safe_rel(cc_dir / 'profit_alerts.csv')}`")
    lines.append(f"- Arena state artifact pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/aggregated_analysis_arena{_profile_suffix(profile)}{_tag_suffix(experiment_tag)}.json`")
    lines.append(f"- Translation sandbox seed pattern: `sharepacks/_predictive/<D>/<STATE>/analysis/translation_sandbox_seed{_profile_suffix(profile)}{_tag_suffix(experiment_tag)}.json`")
    lines.append("")
    lines.append("## Portfolio Table")
    lines.append("")
    lines.append("| State | Arena row | Arena top | Reinforced | Tracker hints | Alerts | CU union | B12 boxed | B24 pack | B36 pack |")
    lines.append("|---|---|---|---|---|---:|---:|---|---|---|")
    for row in table_rows:
        lines.append(
            "| {StateKey} | {arena_row_label} | {arena_top} | {arena_reinforced} | {tracker_hint} | {alerts_count} | {candidate_union} | {play_b12_boxed} | {play_b24_pack} | {play_b36_pack} |".format(
                **row
            )
        )
    lines.append("")
    lines.append("## Arena-First Board Snapshot")
    lines.append("")
    valid_arena_rows = [
        item
        for item in table_rows
        if bool(item.get("arena_rank_signal_valid")) and item.get("arena_rank") is not None
    ]
    for row in sorted(valid_arena_rows, key=lambda value: (int(value["arena_rank"]), value["StateKey"]))[:8]:
        lines.append(
            f"- **{row['StateKey']}**: `{row['arena_row_label']}` | canonicals `{row['arena_top'] or '-'}` | vtrac `{row['arena_vtrac'] or '-'}` | top_profit `{row['top_profit']}`"
        )
    lines.append("")
    lines.append("## Control Arm Snapshot")
    lines.append("")
    lines.append("These are still baseline/control-arm surfaces, not the definition of arena truth.")
    lines.append("")
    for row in table_rows[:10]:
        lines.append(
            f"- **{row['StateKey']}**: CU packs=`{row['candidate_packs']}` union=`{row['candidate_union']}` top_support=`{row['candidate_top_support_label']}` due=`{row['due_doubles_canon']}`"
        )
    lines.append("")
    lines.append("## Play Card Defaults")
    lines.append("")
    lines.append(f"- B12 strategy: `{b12_strategy}`")
    lines.append(f"- B24 strategy: `{b24_strategy}`")
    lines.append(f"- B36 strategy: `{b36_strategy}`")
    lines.append("")
    for row in table_rows:
        if row["play_b24_pack"] != "-" or row["play_b36_pack"] != "-":
            lines.append(
                f"- **{row['StateKey']}**: B24 `{row['play_b24_pack']}` (src `{row['play_b24_src']}`) | B36 `{row['play_b36_pack']}` (src `{row['play_b36_src']}`)"
            )
    lines.append("")
    lines.append("## Analyst Notes")
    lines.append("")
    lines.append("- Which states are strongest from the arena-first lens?: `...`")
    lines.append("- Which states are strongest only from the control-arm lens?: `...`")
    lines.append("- Any state where tracker hints materially outran the control arm?: `...`")
    lines.append("- Any rank-integrity or source-provenance gap to record?: `...`")
    lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote: {_safe_rel(out_path)}")


if __name__ == "__main__":
    main()
