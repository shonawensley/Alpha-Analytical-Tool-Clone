#!/usr/bin/env python3
"""Build an Aux + Control Center analysis arena from frozen predictive sharepack artifacts.

The arena is intentionally predictive-side and budget-blind. It preserves the
broader structured context already emitted by Aux and Control Center so the
aggregated analysis arena can reason over that context later without forcing it
through the current narrow candidate-universe surfaces.
"""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


VARIANT_ORDER: Tuple[str, ...] = ("Combined", "Midday", "Evening")
LOWER_VARIANT_ORDER: Tuple[str, ...] = ("combined", "midday", "evening")
PAIR_SEVERITY_WEIGHT: Dict[str, int] = {"red": 3, "blue": 2, "purple": 1}
DOUBLE_SEVERITY_WEIGHT: Dict[str, int] = {"B": 2}


def _read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8", errors="replace"))


def _load_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def _safe_rel(path: Path, repo_root: Path) -> str:
    try:
        return str(path.resolve().relative_to(repo_root.resolve()))
    except Exception:
        return str(path)


def _hash_inputs(paths: Sequence[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        digest.update(str(path.name).encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def _to_int(value: object, default: int = 0) -> int:
    try:
        text = str(value or "").strip()
        if not text:
            return int(default)
        return int(float(text))
    except Exception:
        return int(default)


def _to_float(value: object, default: float = 0.0) -> float:
    try:
        text = str(value or "").strip()
        if not text:
            return float(default)
        return float(text)
    except Exception:
        return float(default)


def _variant_title(value: object) -> str:
    raw = str(value or "").strip()
    if not raw:
        return "Unknown"
    lowered = raw.lower()
    if lowered in {"combined", "midday", "evening"}:
        return lowered.title()
    return raw


def _variant_sort_key(value: str) -> Tuple[int, str]:
    try:
        return (VARIANT_ORDER.index(_variant_title(value)), _variant_title(value))
    except ValueError:
        return (len(VARIANT_ORDER), _variant_title(value))


def _severity_weight(value: object, *, double_mode: bool = False) -> int:
    text = str(value or "").strip()
    if double_mode:
        return DOUBLE_SEVERITY_WEIGHT.get(text, 0)
    return PAIR_SEVERITY_WEIGHT.get(text.lower(), 0)


def _normalize_pick3_literal(value: object) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _canon(value: object) -> str:
    digits = _normalize_pick3_literal(value)
    return "".join(sorted(digits)) if digits else ""


def _top_n(items: Sequence[Any], n: int) -> List[Any]:
    return list(items[: max(0, int(n))])


def _parse_json_list_size(value: object) -> int:
    raw = str(value or "").strip()
    if not raw.startswith("["):
        return 0
    try:
        parsed = json.loads(raw)
    except Exception:
        return 0
    return len(parsed) if isinstance(parsed, list) else 0


def _sorted_variants(mapping: Dict[str, Any]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for key in sorted(mapping.keys(), key=_variant_sort_key):
        out[_variant_title(key)] = mapping[key]
    return out


def _top_aggregated_digits(raw: Dict[str, Any], top_n: int) -> Dict[str, List[Dict[str, Any]]]:
    out: Dict[str, List[Dict[str, Any]]] = {}
    for position, rows in raw.items():
        if not isinstance(rows, list):
            continue
        cleaned: List[Dict[str, Any]] = []
        for row in rows:
            if not isinstance(row, dict):
                continue
            cleaned.append(
                {
                    "digit": str(row.get("digit") or ""),
                    "score": round(_to_float(row.get("score")), 6),
                    "tags": [str(tag) for tag in row.get("tags", []) if str(tag)],
                    "occurrences": row.get("occurrences") if isinstance(row.get("occurrences"), list) else [],
                }
            )
        cleaned.sort(key=lambda item: (-float(item.get("score") or 0.0), str(item.get("digit") or "")))
        out[str(position)] = _top_n(cleaned, top_n)
    return out


def _summarize_positional(summary: Dict[str, Any], top_n: int) -> Dict[str, Any]:
    positional = summary.get("positional") if isinstance(summary.get("positional"), dict) else {}
    shortlist = positional.get("shortlist_report") if isinstance(positional.get("shortlist_report"), dict) else {}
    hard_due = positional.get("hard_due_by_variant") if isinstance(positional.get("hard_due_by_variant"), dict) else {}

    shortlist_top: List[Dict[str, Any]] = []
    for row in shortlist.get("candidates", []) if isinstance(shortlist.get("candidates"), list) else []:
        if not isinstance(row, dict):
            continue
        combo = _normalize_pick3_literal(row.get("combo"))
        shortlist_top.append(
            {
                "combo": combo,
                "canonical": _canon(combo) or str(row.get("canonical") or ""),
                "score": round(_to_float(row.get("score")), 6),
                "source": str(row.get("source") or ""),
                "vtrac_index": _to_int(row.get("vtrac_index"), default=-1),
                "tags": [str(tag) for tag in row.get("tags", []) if str(tag)],
            }
        )
    shortlist_top.sort(key=lambda item: (-float(item.get("score") or 0.0), str(item.get("combo") or "")))

    variant_top_digits: Dict[str, Any] = {}
    raw_variant_top = shortlist.get("variant_top_digits") if isinstance(shortlist.get("variant_top_digits"), dict) else {}
    for variant, rows in raw_variant_top.items():
        if not isinstance(rows, list):
            continue
        variant_top_digits[_variant_title(variant)] = _top_n(
            [
                {
                    "position": _to_int(row.get("position"), default=-1),
                    "digit": str(row.get("digit") or ""),
                    "gap": _to_int(row.get("gap"), default=0),
                    "rank": _to_int(row.get("rank"), default=0),
                }
                for row in rows
                if isinstance(row, dict)
            ],
            top_n,
        )

    return {
        "available": bool(shortlist_top or hard_due),
        "hard_due_by_variant": _sorted_variants(
            {
                variant: _top_n(
                    [
                        {
                            "position": _to_int(item.get("position"), default=-1),
                            "digit": str(item.get("digit") or ""),
                            "draws_since": _to_int(item.get("draws_since"), default=0),
                        }
                        for item in rows
                        if isinstance(item, dict)
                    ],
                    top_n,
                )
                for variant, rows in hard_due.items()
                if isinstance(rows, list)
            }
        ),
        "variant_top_digits": _sorted_variants(variant_top_digits),
        "aggregated_digits_top": _top_aggregated_digits(
            shortlist.get("aggregated_digits") if isinstance(shortlist.get("aggregated_digits"), dict) else {}, top_n
        ),
        "shortlist_top": _top_n(shortlist_top, top_n),
        "consensus_notes": _top_n([str(note) for note in shortlist.get("consensus_notes", []) if str(note)], top_n),
        "double_pressure_notes": _top_n(
            [str(note) for note in shortlist.get("double_pressure_notes", []) if str(note)], top_n
        ),
    }


def _flatten_pair_rows(top_by_variant: Dict[str, Any]) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for variant, payload in top_by_variant.items():
        if not isinstance(payload, dict):
            continue
        for bucket in ("repeating", "non_repeating"):
            items = payload.get(bucket)
            if not isinstance(items, list):
                continue
            for item in items:
                if not isinstance(item, dict):
                    continue
                rows.append(
                    {
                        "variant": _variant_title(variant),
                        "bucket": bucket,
                        "pair": str(item.get("pair") or ""),
                        "draws_since": _to_int(item.get("draws_since"), default=0),
                        "severity": str(item.get("severity") or ""),
                        "_sort_weight": _severity_weight(item.get("severity")),
                    }
                )
    rows.sort(key=lambda item: (-int(item["_sort_weight"]), -int(item.get("draws_since") or 0), str(item.get("pair") or "")))
    for row in rows:
        row.pop("_sort_weight", None)
    return rows


def _flatten_multi_variant_alerts(raw: Dict[str, Any], *, double_mode: bool = False) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for literal, variants in raw.items():
        if not isinstance(variants, dict):
            continue
        variant_items: List[Dict[str, Any]] = []
        max_ds = 0
        max_weight = 0
        for variant, payload in variants.items():
            if not isinstance(payload, dict):
                continue
            ds = _to_int(payload.get("draws_since"), default=0)
            sev = str(payload.get("severity") or "")
            variant_items.append(
                {
                    "variant": _variant_title(variant),
                    "severity": sev,
                    "draws_since": ds,
                }
            )
            max_ds = max(max_ds, ds)
            max_weight = max(max_weight, _severity_weight(sev, double_mode=double_mode))
        rows.append(
            {
                "literal": str(literal),
                "variants": sorted(variant_items, key=lambda item: _variant_sort_key(item["variant"])),
                "variant_count": len(variant_items),
                "max_draws_since": max_ds,
                "_sort_weight": max_weight,
            }
        )
    rows.sort(
        key=lambda item: (
            -int(item.get("variant_count") or 0),
            -int(item.get("_sort_weight") or 0),
            -int(item.get("max_draws_since") or 0),
            str(item.get("literal") or ""),
        )
    )
    for row in rows:
        row.pop("_sort_weight", None)
    return rows


def _summarize_pair_band_context(summary: Dict[str, Any], top_n: int) -> Dict[str, Any]:
    pairs = summary.get("pairs") if isinstance(summary.get("pairs"), dict) else {}
    top_by_variant = pairs.get("top_by_variant") if isinstance(pairs.get("top_by_variant"), dict) else {}
    multi_variant = pairs.get("multi_variant_alerts") if isinstance(pairs.get("multi_variant_alerts"), dict) else {}

    by_variant: Dict[str, Any] = {}
    for variant, payload in top_by_variant.items():
        if not isinstance(payload, dict):
            continue
        by_variant[_variant_title(variant)] = {
            "repeating": _top_n([item for item in payload.get("repeating", []) if isinstance(item, dict)], top_n),
            "non_repeating": _top_n([item for item in payload.get("non_repeating", []) if isinstance(item, dict)], top_n),
        }

    top_alerts = _flatten_pair_rows(top_by_variant)
    return {
        "available": bool(by_variant or multi_variant),
        "top_by_variant": _sorted_variants(by_variant),
        "multi_variant_top": _top_n(_flatten_multi_variant_alerts(multi_variant), top_n),
        "top_alerts": _top_n(top_alerts, top_n),
    }


def _summarize_badge_pressure(
    summary: Dict[str, Any],
    *,
    badge_pressure: Optional[Dict[str, Any]],
    top_n: int,
) -> Dict[str, Any]:
    pair_ctx = _summarize_pair_band_context(summary, top_n)
    doubles = summary.get("doubles") if isinstance(summary.get("doubles"), dict) else {}
    double_top = doubles.get("top_by_variant") if isinstance(doubles.get("top_by_variant"), dict) else {}
    double_multi = doubles.get("multi_variant_alerts") if isinstance(doubles.get("multi_variant_alerts"), dict) else {}

    top_combo_alerts: List[Dict[str, Any]] = []
    top_combo_by_variant: Dict[str, Any] = {}
    for variant, rows in double_top.items():
        if not isinstance(rows, list):
            continue
        cleaned = []
        for row in rows:
            if not isinstance(row, dict):
                continue
            cleaned.append(
                {
                    "combo": _normalize_pick3_literal(row.get("combo")),
                    "canonical": _canon(row.get("combo")),
                    "draws_since": _to_int(row.get("draws_since"), default=0),
                    "severity": str(row.get("severity") or ""),
                }
            )
        cleaned.sort(
            key=lambda item: (
                -_severity_weight(item.get("severity"), double_mode=True),
                -int(item.get("draws_since") or 0),
                str(item.get("combo") or ""),
            )
        )
        top_combo_by_variant[_variant_title(variant)] = _top_n(cleaned, top_n)
        for item in cleaned:
            top_combo_alerts.append({"variant": _variant_title(variant), **item})
    top_combo_alerts.sort(
        key=lambda item: (
            -_severity_weight(item.get("severity"), double_mode=True),
            -int(item.get("draws_since") or 0),
            str(item.get("combo") or ""),
        )
    )

    return {
        "available": bool(pair_ctx.get("available") or top_combo_by_variant or (badge_pressure or {}).get("available")),
        "index_pressure": badge_pressure or {"available": False, "by_variant": {}, "midday_evening_intersection": []},
        "top_pair_alerts": pair_ctx.get("top_alerts", []),
        "top_combo_alerts": _top_n(top_combo_alerts, top_n),
        "multi_variant_pairs": pair_ctx.get("multi_variant_top", []),
        "multi_variant_combos": _top_n(_flatten_multi_variant_alerts(double_multi, double_mode=True), top_n),
    }


def _summarize_due_double_families(rows: List[Dict[str, str]], top_n: int) -> Dict[str, Any]:
    if not rows:
        return {"available": False, "by_variant": {}, "max_draws_since_double": 0}

    by_variant: Dict[str, Any] = {}
    max_ds = 0
    for row in rows:
        variant = _variant_title(row.get("Variant"))
        families: List[Dict[str, Any]] = []
        for key, value in row.items():
            if not str(key).startswith("Family ") or not str(value).strip():
                continue
            family_text = str(value)
            family_name, _, examples_text = family_text.partition(":")
            examples = [_normalize_pick3_literal(token.split("(")[0]) for token in examples_text.strip().split() if token]
            examples = [x for x in examples if x]
            families.append(
                {
                    "slot": str(key),
                    "family": family_name.strip(),
                    "examples": _top_n(examples, top_n),
                    "raw": family_text,
                }
            )
        draws_since_double = _to_int(row.get("Draws Since Double"), default=0)
        max_ds = max(max_ds, draws_since_double)
        by_variant[variant] = {
            "draws_since_double": draws_since_double,
            "families": _top_n(families, top_n),
        }

    return {
        "available": bool(by_variant),
        "max_draws_since_double": max_ds,
        "by_variant": _sorted_variants(by_variant),
    }


def _summarize_repeat_watch(summary: Dict[str, Any], rows: List[Dict[str, str]], top_n: int) -> Dict[str, Any]:
    aux_repeat = summary.get("repeat_watch") if isinstance(summary.get("repeat_watch"), dict) else {}
    aux_by_variant = _sorted_variants(
        {
            variant: {
                "current_index": _to_int(payload.get("current_index"), default=-1),
                "current_streak": _to_int(payload.get("current_streak"), default=0),
                "last_repeat_gap": _to_int(payload.get("last_repeat_gap"), default=0),
                "last_repeat_index": _to_int(payload.get("last_repeat_index"), default=-1),
                "max_streak": _to_int(payload.get("max_streak"), default=0),
                "window": _to_int(payload.get("window"), default=0),
            }
            for variant, payload in aux_repeat.items()
            if isinstance(payload, dict)
        }
    )

    cc_rows: List[Dict[str, Any]] = []
    for row in rows:
        cc_rows.append(
            {
                "variant": _variant_title(row.get("Variant")),
                "current_index": _to_int(row.get("Current Index"), default=-1),
                "current_streak": _to_int(row.get("Current Streak"), default=0),
                "heat_index": _to_int(row.get("Heat Index"), default=-1),
                "heat_hazard": round(_to_float(row.get("Heat Hazard")), 6),
                "last_repeat_draws": _to_int(row.get("Last Repeat (draws)"), default=0),
                "max_streak": _to_int(row.get("Max Streak"), default=0),
            }
        )
    cc_rows.sort(
        key=lambda item: (
            -int(item.get("current_streak") or 0),
            -float(item.get("heat_hazard") or 0.0),
            -int(item.get("heat_index") or -1),
            _variant_sort_key(item.get("variant") or ""),
        )
    )

    return {
        "available": bool(aux_by_variant or cc_rows),
        "aux_by_variant": aux_by_variant,
        "control_center_top": _top_n(cc_rows, top_n),
    }


def _summarize_sums(summary: Dict[str, Any], top_n: int) -> Dict[str, Any]:
    sums = summary.get("sums") if isinstance(summary.get("sums"), dict) else {}
    top_by_variant = sums.get("top_by_variant") if isinstance(sums.get("top_by_variant"), dict) else {}
    by_variant: Dict[str, Any] = {}
    for variant, rows in top_by_variant.items():
        if not isinstance(rows, list):
            continue
        cleaned: List[Dict[str, Any]] = []
        for row in rows:
            if not isinstance(row, dict):
                continue
            flags = row.get("flags") if isinstance(row.get("flags"), dict) else {}
            cleaned.append(
                {
                    "sum": _to_int(row.get("sum"), default=-1),
                    "draws_since": _to_int(row.get("draws_since"), default=0),
                    "z": round(_to_float(row.get("z")), 6),
                    "z_tail": round(_to_float(row.get("z_tail")), 6),
                    "flags": {k: bool(v) for k, v in flags.items()},
                }
            )
        cleaned.sort(
            key=lambda item: (
                -int(bool(item["flags"].get("red"))),
                -int(bool(item["flags"].get("blue"))),
                -int(bool(item["flags"].get("purple"))),
                -int(item.get("draws_since") or 0),
                -abs(float(item.get("z_tail") or 0.0)),
                int(item.get("sum") or 0),
            )
        )
        by_variant[_variant_title(variant)] = _top_n(cleaned, top_n)
    return {
        "available": bool(by_variant),
        "top_by_variant": _sorted_variants(by_variant),
    }


def _summarize_blackapple(summary: Dict[str, Any], rows: List[Dict[str, str]], top_n: int) -> Dict[str, Any]:
    blackapple = summary.get("blackapple") if isinstance(summary.get("blackapple"), dict) else {}
    by_variant = blackapple.get("by_variant") if isinstance(blackapple.get("by_variant"), dict) else {}
    aux_by_variant: Dict[str, Any] = {}
    for variant, payload in by_variant.items():
        if not isinstance(payload, dict):
            continue
        triggers = payload.get("triggers") if isinstance(payload.get("triggers"), dict) else {}
        candidates = payload.get("candidates") if isinstance(payload.get("candidates"), list) else []
        aux_by_variant[_variant_title(variant)] = {
            "score": _to_int(payload.get("score"), default=0),
            "trigger_flags": {
                "mirror": bool(triggers.get("mirror")),
                "root_due": triggers.get("root_due") if isinstance(triggers.get("root_due"), list) else [],
                "floating": triggers.get("floating") if isinstance(triggers.get("floating"), list) else [],
                "pairs_remaining_count": _to_int(
                    (triggers.get("pairs") or {}).get("remaining_count") if isinstance(triggers.get("pairs"), dict) else 0,
                    default=0,
                ),
                "pattern": triggers.get("pattern") if isinstance(triggers.get("pattern"), dict) else {},
            },
            "candidates_top": _top_n(
                [
                    {
                        "combo": _normalize_pick3_literal(item.get("combo")),
                        "canonical": _canon(item.get("combo")),
                        "score": _to_int(item.get("score"), default=0),
                        "tags": [str(tag) for tag in item.get("tags", []) if str(tag)],
                    }
                    for item in candidates
                    if isinstance(item, dict)
                ],
                top_n,
            ),
        }

    cc_rows = [
        {
            "variant": _variant_title(row.get("Variant")),
            "ba_score": _to_int(row.get("BA-Score"), default=0),
            "status": str(row.get("Status") or ""),
            "triggers": str(row.get("Triggers") or ""),
            "candidate_count": _to_int(row.get("#Candidates"), default=0),
            "examples": [token for token in str(row.get("Examples") or "").split() if token][:top_n],
        }
        for row in rows
    ]
    cc_rows.sort(
        key=lambda item: (-int(item.get("ba_score") or 0), -int(item.get("candidate_count") or 0), _variant_sort_key(item.get("variant") or ""))
    )

    return {
        "available": bool(aux_by_variant or cc_rows),
        "aux_by_variant": _sorted_variants(aux_by_variant),
        "control_center_top": _top_n(cc_rows, top_n),
    }


def _summarize_profit_alerts(rows: List[Dict[str, str]], top_n: int) -> Dict[str, Any]:
    if not rows:
        return {"available": False, "alert_count": 0, "variants": {}, "top_alerts": []}

    top_alerts: List[Dict[str, Any]] = []
    by_variant: Dict[str, List[Dict[str, Any]]] = {}
    for row in rows:
        variant = _variant_title(row.get("Variant"))
        evidence_summary: Dict[str, Any] = {}
        evidence_raw = str(row.get("Evidence") or "").strip()
        if evidence_raw.startswith("{"):
            try:
                evidence = json.loads(evidence_raw)
            except Exception:
                evidence = {}
            if isinstance(evidence, dict):
                evidence_summary = {
                    "keys": sorted(evidence.keys()),
                    "persistence_set_count": _to_int(evidence.get("persistence_set_count"), default=0),
                    "rowcov": _to_int(evidence.get("rowcov"), default=0),
                    "ba_score": _to_int(evidence.get("ba_score"), default=0),
                    "stable_family_id": str(evidence.get("stable_family_id") or ""),
                    "stable_section": str(evidence.get("stable_section") or ""),
                }
        item = {
            "variant": variant,
            "alert_id": str(row.get("AlertId") or ""),
            "strength": _to_int(row.get("Strength"), default=0),
            "suggested": str(row.get("Suggested") or ""),
            "badges": [token for token in str(row.get("Badges") or "").split("/") if token],
            "canonical": _canon(row.get("Canonical")),
            "implied_set_size": _parse_json_list_size(row.get("ImpliedSet")),
            "evidence_summary": evidence_summary,
        }
        by_variant.setdefault(variant, []).append(item)
        top_alerts.append(item)

    top_alerts.sort(
        key=lambda item: (
            -int(item.get("strength") or 0),
            -int(item.get("implied_set_size") or 0),
            str(item.get("alert_id") or ""),
        )
    )
    variant_payload = {
        variant: _top_n(
            sorted(
                items,
                key=lambda item: (
                    -int(item.get("strength") or 0),
                    -int(item.get("implied_set_size") or 0),
                    str(item.get("alert_id") or ""),
                ),
            ),
            top_n,
        )
        for variant, items in by_variant.items()
    }
    return {
        "available": True,
        "alert_count": len(rows),
        "variants": _sorted_variants(variant_payload),
        "top_alerts": _top_n(top_alerts, top_n),
    }


def _summarize_compound_events(rows: List[Dict[str, str]], top_n: int) -> Dict[str, Any]:
    if not rows:
        return {"available": False, "top_events": []}
    items = [
        {
            "variant": _variant_title(row.get("variant")),
            "top_event": str(row.get("top_event") or ""),
            "priority": _to_int(row.get("priority"), default=0),
            "watchlist_tags": [token for token in str(row.get("watchlist_tags") or "").split(",") if token],
            "candidate_alert_ids": [token for token in str(row.get("candidate_alert_ids") or "").split(",") if token],
            "promoter_alert_ids": [token for token in str(row.get("promoter_alert_ids") or "").split(",") if token],
            "strength_max": _to_int(row.get("strength_max"), default=0),
            "merged_rows_total": _to_int(row.get("merged_rows_total"), default=0),
        }
        for row in rows
    ]
    items.sort(
        key=lambda item: (
            -int(item.get("priority") or 0),
            -int(item.get("strength_max") or 0),
            -int(item.get("merged_rows_total") or 0),
            _variant_sort_key(item.get("variant") or ""),
        )
    )
    return {
        "available": True,
        "top_events": _top_n(items, top_n),
    }


def build_aux_control_center_arena_payload(
    *,
    day_dir: Path,
    state_dir: Path,
    state_key: str,
    results_date: str,
    history_date: str,
    profile: str,
    experiment_tag: str,
    sharepacks_root: Path,
    contains_winners_artifacts: bool,
    repo_root: Path,
    badge_pressure: Optional[Dict[str, Any]] = None,
    top_items: int = 8,
) -> Dict[str, Any]:
    top_n = max(1, int(top_items))
    aux_path = state_dir / "aux" / state_key / "summary.json"
    summary = _read_json(aux_path) if aux_path.exists() else {}

    cc_dir = day_dir / "control_center"
    due_doubles_path = cc_dir / "due_doubles.csv"
    repeat_watch_path = cc_dir / "vtrac_repeat_watch.csv"
    blackapple_path = cc_dir / "blackapple_alerts.csv"
    profit_alerts_path = cc_dir / "profit_alerts.csv"
    compound_events_path = cc_dir / "profit_compound_events.csv"
    meta_path = cc_dir / "meta.json"

    due_doubles_rows = [row for row in _load_csv_rows(due_doubles_path) if str(row.get("StateKey") or "").strip() == state_key]
    repeat_watch_rows = [row for row in _load_csv_rows(repeat_watch_path) if str(row.get("StateKey") or "").strip() == state_key]
    blackapple_rows = [row for row in _load_csv_rows(blackapple_path) if str(row.get("StateKey") or "").strip() == state_key]
    profit_alert_rows = [row for row in _load_csv_rows(profit_alerts_path) if str(row.get("StateKey") or "").strip() == state_key]
    compound_event_rows = [row for row in _load_csv_rows(compound_events_path) if str(row.get("state_key") or "").strip() == state_key]

    inputs: List[Path] = []
    for path in (
        aux_path,
        due_doubles_path,
        repeat_watch_path,
        blackapple_path,
        profit_alerts_path,
        compound_events_path,
        meta_path,
    ):
        if path.exists():
            inputs.append(path)

    extra_badge_paths = []
    if isinstance(badge_pressure, dict):
        for rel in badge_pressure.get("evidence_paths", []) if isinstance(badge_pressure.get("evidence_paths"), list) else []:
            rel_path = repo_root / str(rel)
            if rel_path.exists():
                extra_badge_paths.append(rel_path)
    inputs.extend(extra_badge_paths)

    unique_inputs: List[Path] = []
    seen = set()
    for path in inputs:
        key = str(path.resolve())
        if key in seen:
            continue
        seen.add(key)
        unique_inputs.append(path)

    arena_objects = {
        "aux_positional_pressure": _summarize_positional(summary, top_n),
        "aux_vtrac_pressure": {
            "available": bool(summary.get("vtrac")),
            "overlay_top": _sorted_variants(
                {
                    variant: _top_n(rows, top_n)
                    for variant, rows in (summary.get("vtrac", {}) or {}).get("overlay_top", {}).items()
                    if isinstance(rows, list)
                }
            ),
            "heatboard_top": _sorted_variants(
                {
                    variant: _top_n(rows, top_n)
                    for variant, rows in (summary.get("vtrac", {}) or {}).get("heatboard_top", {}).items()
                    if isinstance(rows, list)
                }
            ),
        },
        "aux_badge_pressure": _summarize_badge_pressure(summary, badge_pressure=badge_pressure, top_n=top_n),
        "aux_pair_band_context": _summarize_pair_band_context(summary, top_n),
        "aux_due_doubles_family_pressure": _summarize_due_double_families(due_doubles_rows, top_n),
        "aux_repeat_watch_context": _summarize_repeat_watch(summary, repeat_watch_rows, top_n),
        "aux_sums_context": _summarize_sums(summary, top_n),
        "aux_blackapple_context": _summarize_blackapple(summary, blackapple_rows, top_n),
        "cc_profit_alert_context": _summarize_profit_alerts(profit_alert_rows, top_n),
        "cc_compound_event_context": _summarize_compound_events(compound_event_rows, top_n),
        "cc_tracker_context": {
            "available": bool(unique_inputs),
            "control_center_meta_path": _safe_rel(meta_path, repo_root) if meta_path.exists() else "",
            "source_counts": {
                "due_doubles_rows": len(due_doubles_rows),
                "repeat_watch_rows": len(repeat_watch_rows),
                "blackapple_rows": len(blackapple_rows),
                "profit_alert_rows": len(profit_alert_rows),
                "compound_event_rows": len(compound_event_rows),
            },
        },
    }

    linked_truth_layers = [
        {
            "label": "aux_summary",
            "path": _safe_rel(aux_path, repo_root) if aux_path.exists() else "",
            "note": "Primary predictive-side Aux SSOT.",
        },
        {
            "label": "control_center_csvs",
            "path": _safe_rel(cc_dir, repo_root) if cc_dir.exists() else "",
            "note": "Due doubles, repeat watch, Blackapple, profit alerts, and compound events.",
        },
        {
            "label": "boxed_vtrac_badge_tables",
            "path": "",
            "note": "Heavy truth layer not fully exported in predictive sharepacks; preserve badge surfaces and leave room for later drill-down exports.",
        },
    ]

    available = any(bool(obj.get("available")) for obj in arena_objects.values() if isinstance(obj, dict))
    payload = {
        "schema_version": "aux_control_center_arena_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "results_date": results_date,
        "history_date": history_date,
        "profile": profile,
        "experiment_tag": experiment_tag,
        "state_key": state_key,
        "sharepack_root": _safe_rel(sharepacks_root, repo_root),
        "sharepack_state_dir": _safe_rel(state_dir, repo_root),
        "contains_winners_artifacts": bool(contains_winners_artifacts),
        "available": available,
        "selection_subset_note": {
            "current_conversion_methods": [
                "aux_positional",
                "aux_vtrac_index_overdue",
                "mirror_pair_closure",
                "due_doubles",
            ],
            "note": "These remain bounded predictive conversion methods and do not define the full Aux / Control Center arena contract.",
        },
        "inputs": [_safe_rel(path, repo_root) for path in unique_inputs],
        "inputs_hash": _hash_inputs(unique_inputs) if unique_inputs else "",
        "linked_truth_layers": linked_truth_layers,
        "arena_objects": arena_objects,
    }
    return payload


def build_aux_control_center_markdown(payload: Dict[str, Any]) -> str:
    arena = payload.get("arena_objects") if isinstance(payload.get("arena_objects"), dict) else {}
    lines: List[str] = []
    lines.append("# Aux + Control Center Arena")
    lines.append("")
    lines.append(f"- state: `{payload.get('state_key', '')}`")
    lines.append(f"- results_date: `{payload.get('results_date', '')}`")
    lines.append(f"- history_date: `{payload.get('history_date', '')}`")
    lines.append(f"- available: `{bool(payload.get('available'))}`")
    lines.append("")

    def add_block(title: str, obj_key: str, bullets: Sequence[str]) -> None:
        obj = arena.get(obj_key) if isinstance(arena.get(obj_key), dict) else {}
        lines.append(f"## {title}")
        lines.append("")
        lines.append(f"- available: `{bool(obj.get('available'))}`")
        for bullet in bullets:
            lines.append(f"- {bullet}")
        lines.append("")

    pos = arena.get("aux_positional_pressure", {}) if isinstance(arena.get("aux_positional_pressure"), dict) else {}
    add_block(
        "Positional Pressure",
        "aux_positional_pressure",
        [
            f"shortlist_top: `{len(pos.get('shortlist_top', []))}`",
            f"hard_due_variants: `{len(pos.get('hard_due_by_variant', {}))}`",
            f"consensus_notes: `{len(pos.get('consensus_notes', []))}`",
        ],
    )

    vtrac = arena.get("aux_vtrac_pressure", {}) if isinstance(arena.get("aux_vtrac_pressure"), dict) else {}
    add_block(
        "VTRAC Pressure",
        "aux_vtrac_pressure",
        [
            f"overlay_variants: `{len(vtrac.get('overlay_top', {}))}`",
            f"heatboard_variants: `{len(vtrac.get('heatboard_top', {}))}`",
        ],
    )

    badge = arena.get("aux_badge_pressure", {}) if isinstance(arena.get("aux_badge_pressure"), dict) else {}
    add_block(
        "Badge Pressure",
        "aux_badge_pressure",
        [
            f"top_pair_alerts: `{len(badge.get('top_pair_alerts', []))}`",
            f"top_combo_alerts: `{len(badge.get('top_combo_alerts', []))}`",
            f"index_pressure_available: `{bool((badge.get('index_pressure') or {}).get('available'))}`",
        ],
    )

    dd = arena.get("aux_due_doubles_family_pressure", {}) if isinstance(arena.get("aux_due_doubles_family_pressure"), dict) else {}
    add_block(
        "Due Doubles Family Pressure",
        "aux_due_doubles_family_pressure",
        [
            f"variants: `{len(dd.get('by_variant', {}))}`",
            f"max_draws_since_double: `{dd.get('max_draws_since_double', 0)}`",
        ],
    )

    profit = arena.get("cc_profit_alert_context", {}) if isinstance(arena.get("cc_profit_alert_context"), dict) else {}
    compound = arena.get("cc_compound_event_context", {}) if isinstance(arena.get("cc_compound_event_context"), dict) else {}
    add_block(
        "Profit Alerts + Compound Events",
        "cc_profit_alert_context",
        [
            f"profit_alert_count: `{profit.get('alert_count', 0)}`",
            f"profit_variants: `{len(profit.get('variants', {}))}`",
            f"compound_events: `{len(compound.get('top_events', []))}`",
        ],
    )

    tracker = arena.get("cc_tracker_context", {}) if isinstance(arena.get("cc_tracker_context"), dict) else {}
    lines.append("## Tracker Context")
    lines.append("")
    lines.append(f"- available: `{bool(tracker.get('available'))}`")
    source_counts = tracker.get("source_counts") if isinstance(tracker.get("source_counts"), dict) else {}
    for key in sorted(source_counts.keys()):
        lines.append(f"- {key}: `{source_counts[key]}`")
    lines.append("")

    lines.append("## Inputs")
    lines.append("")
    for rel in payload.get("inputs", []) if isinstance(payload.get("inputs"), list) else []:
        lines.append(f"- `{rel}`")
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_aux_control_center_files(
    *,
    out_json_path: Path,
    payload: Dict[str, Any],
    write_md: bool = True,
) -> Tuple[Path, Optional[Path]]:
    out_json_path.parent.mkdir(parents=True, exist_ok=True)
    out_json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path: Optional[Path] = None
    if write_md:
        md_path = out_json_path.with_suffix(".md")
        md_path.write_text(build_aux_control_center_markdown(payload), encoding="utf-8")
    return out_json_path, md_path


def build_aux_control_center_signals(payload: Dict[str, Any]) -> Dict[str, Any]:
    arena = payload.get("arena_objects") if isinstance(payload.get("arena_objects"), dict) else {}
    return {
        "available": bool(payload.get("available")),
        "evidence_paths": payload.get("inputs", []),
        "selection_subset_note": payload.get("selection_subset_note", {}),
        "linked_truth_layers": payload.get("linked_truth_layers", []),
        "arena_objects": arena,
    }
