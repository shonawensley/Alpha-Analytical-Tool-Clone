#!/usr/bin/env python3
"""
Create a per-state Candidate Universe / Playset artifact for a frozen sharepack day.

This is an "analysis layer" tool:
- Reads ONLY from frozen sharepack artifacts (no analyzer runs, no table regen).
- Writes a deterministic, gradeable pre-results prediction artifact:
    sharepacks/_predictive/<D>/<STATE>/candidate_universe.json

Safety goals
------------
- Prevent time contamination: if the sharepacks root is predictive, refuse to run if
  winners-dependent artifacts are detected (unless explicitly overridden).
- Deterministic output: stable sorting + inputs_hash.

Usage
-----
python3 scripts/tools/create_candidate_universe.py --date 2026-01-07 --sharepacks-root sharepacks/_predictive
python3 scripts/tools/create_candidate_universe.py --date 2026-01-07 --states NewJersey4
python3 scripts/tools/create_candidate_universe.py --date 2026-01-07 --sharepacks-root sharepacks/_predictive --profile tool_only
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import re
import sys
import textwrap
from collections import Counter
from contextlib import redirect_stdout
from dataclasses import dataclass, field
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

try:
    from modules.vtrac_reference import get_index_set as _vtrac_get_index_set  # type: ignore
    from modules.vtrac_reference import get_vtrac_index as _vtrac_get_index  # type: ignore
except Exception:  # pragma: no cover - may fail in partial environments
    _vtrac_get_index_set = None  # type: ignore
    _vtrac_get_index = None  # type: ignore

from scripts.tools.dr_arena import build_dr_arena_payload, write_dr_arena_files
from scripts.tools.stable_arena import build_stable_arena_payload, write_stable_arena_files
from scripts.tools.aux_control_center_arena import (
    build_aux_control_center_arena_payload,
    build_aux_control_center_signals,
    write_aux_control_center_files,
)


SCHEMA_VERSION = "1.0"
MIRROR_SCHEME = "vtrac_pair"

# VTRAC-pair mirror mapping (difference-5 pairing).
MIRROR_MAP: Dict[str, str] = {
    "0": "5",
    "1": "6",
    "2": "7",
    "3": "8",
    "4": "9",
    "5": "0",
    "6": "1",
    "7": "2",
    "8": "3",
    "9": "4",
}

_DUE_DOUBLES_TOKEN_RE = re.compile(r"(?P<combo>\d{3})\((?P<severity>[RB])(?P<badge>[CME]):(?P<ds>\d+)\)")


def _is_predictive_root(root: Path) -> bool:
    return root.name == "_predictive" or "/_predictive" in str(root).replace("\\", "/")


def _normalize_experiment_tag(value: str) -> str:
    raw = str(value or "").strip()
    if not raw:
        return ""
    raw = raw.replace(" ", "_")
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "", raw)
    cleaned = cleaned.strip("_-")
    if not cleaned:
        raise SystemExit(f"Invalid --experiment-tag: {value!r} (must contain A-Z/a-z/0-9/_/-)")
    return cleaned[:60]


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _read_json(path: Path) -> object:
    return json.loads(_read_text(path))


def _write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _normalize_pick3_literal(value: str) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    if not digits:
        return ""
    digits = digits.zfill(3) if len(digits) <= 3 else digits
    return digits if len(digits) == 3 else ""


def _canon(draw: str) -> str:
    draw = _normalize_pick3_literal(draw)
    if not draw:
        return ""
    return "".join(sorted(draw))


def _digits_only(value: object) -> str:
    return "".join(ch for ch in str(value or "") if ch.isdigit())


def _to_float(value: object, default: float = 0.0) -> float:
    try:
        if value is None or str(value).strip() == "":
            return float(default)
        return float(value)
    except Exception:
        return float(default)


def _to_int(value: object, default: int = 0) -> int:
    try:
        if value is None or str(value).strip() == "":
            return int(default)
        return int(float(value))
    except Exception:
        return int(default)


def _to_bool(value: object) -> bool:
    text = str(value or "").strip().lower()
    if text in {"1", "true", "t", "yes", "y"}:
        return True
    if text in {"0", "false", "f", "no", "n", ""}:
        return False
    try:
        return float(text) != 0.0
    except Exception:
        return False


def _unique_perms(triad: str) -> List[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    return sorted({"".join(p) for p in itertools.permutations(triad, 3)})


def _r_perm_4(triad: str) -> List[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    a, b, c = triad
    return sorted({a + b + c, a + c + b, b + c + a, c + b + a})


def _mirror_digit(d: str) -> str:
    return MIRROR_MAP[d]


def _keep_pair_mirror_third(triad: str) -> List[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    a, b, c = triad
    t1 = a + b + _mirror_digit(c)
    t2 = a + c + _mirror_digit(b)
    t3 = b + c + _mirror_digit(a)
    return sorted({t1, t2, t3})


def _method1_pair_mirror_12(triad: str) -> List[str]:
    combos: List[str] = []
    for t in _keep_pair_mirror_third(triad):
        combos.extend(_r_perm_4(t))
    return sorted(set(combos))


def _vt8_expand_ordered(triad: str) -> List[str]:
    """
    FULL VT8 expansion (8 combos), preserving digit positions:
    expand each digit to its VTRAC-pair (0/5, 1/6, 2/7, 3/8, 4/9).
    """
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    pools: List[List[str]] = []
    for d in triad:
        pools.append(sorted({d, _mirror_digit(d)}))
    out: List[str] = []
    for a in pools[0]:
        for b in pools[1]:
            for c in pools[2]:
                out.append(a + b + c)
    return sorted(set(out))


def _is_double(triad: str) -> bool:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return False
    return len(set(triad)) == 2


def _double_pack_mirror_single_6(triad: str) -> List[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    if not _is_double(triad):
        return _r_perm_4(triad)

    digits = list(triad)
    counts = {d: digits.count(d) for d in set(digits)}
    rep = next(d for d, c in counts.items() if c == 2)
    single = next(d for d, c in counts.items() if c == 1)
    mirrored_single = _mirror_digit(single)
    t2 = rep + rep + mirrored_single
    return sorted(set(_unique_perms(triad) + _unique_perms(t2)))


def _double_pack_mirror_double_6(triad: str) -> List[str]:
    triad = _normalize_pick3_literal(triad)
    if not triad:
        return []
    if not _is_double(triad):
        return _r_perm_4(triad)

    digits = list(triad)
    counts = {d: digits.count(d) for d in set(digits)}
    rep = next(d for d, c in counts.items() if c == 2)
    single = next(d for d, c in counts.items() if c == 1)
    mirrored_rep = _mirror_digit(rep)
    t2 = mirrored_rep + mirrored_rep + single
    return sorted(set(_unique_perms(triad) + _unique_perms(t2)))


def _safe_rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _load_csv_dict_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        return [{k: (v or "") for k, v in row.items()} for row in csv.DictReader(f)]


def _variant_title(raw: str) -> str:
    v = (raw or "").strip().lower()
    if v == "combined":
        return "Combined"
    if v == "midday":
        return "Midday"
    if v == "evening":
        return "Evening"
    return (raw or "").strip() or "Unknown"


@dataclass(frozen=True)
class ControlMeta:
    history_date: str | None
    history_excel_path: str | None
    results_file: str | None


def _load_control_center_meta(day_dir: Path) -> ControlMeta:
    meta_path = day_dir / "control_center" / "meta.json"
    if not meta_path.exists():
        return ControlMeta(None, None, None)
    raw = _read_json(meta_path)
    if not isinstance(raw, dict):
        return ControlMeta(None, None, None)
    return ControlMeta(
        history_date=str(raw.get("history_date") or "") or None,
        history_excel_path=str(raw.get("history_excel_path") or "") or None,
        results_file=str(raw.get("results_file") or "") or None,
    )


def _detect_winners_artifacts(*, day_dir: Path, state_dir: Path) -> List[str]:
    issues: List[str] = []

    # State-level winners lens folder (explicit contamination).
    winners_dir = state_dir / "winners"
    if winners_dir.exists():
        issues.append(f"Found winners dir: {_safe_rel(winners_dir)}")

    # Winners-dependent VTRAC validation reports (explicit contamination).
    state_key = state_dir.name
    vtrac_dir = state_dir / "vtrac" / state_key
    for fname in ("validation_report.md", "validation_report.json"):
        if (vtrac_dir / fname).exists():
            issues.append(f"Found winners-dependent VTRAC validation report: {_safe_rel(vtrac_dir / fname)}")

    # Winners-dependent global VTRAC validation bundle (predictive packs should not carry these).
    for fname in (
        "vtrac_compact_report.json",
        "vtrac_compact_report.csv",
        "vtrac_pro_payload.zip",
        "vtrac_validation_full_payload.zip",
        "summary.csv",
        "summary.md",
    ):
        p = day_dir / fname
        if p.exists():
            issues.append(f"Found global VTRAC validation artifact: {_safe_rel(p)}")

    # Profit Alerts evaluation artifacts depend on real results windows.
    cc_dir = day_dir / "control_center"
    for fname in ("profit_alerts_eval.csv", "profit_alerts_eval.md", "profit_alerts_eval_merged.csv"):
        if (cc_dir / fname).exists():
            issues.append(f"Found winners-dependent Profit Alerts evaluation artifact: {_safe_rel(cc_dir / fname)}")

    return issues


def _hash_inputs(paths: Sequence[Path]) -> str:
    h = hashlib.sha256()
    for path in sorted(paths, key=lambda p: _safe_rel(p)):
        rel = _safe_rel(path)
        h.update(rel.encode("utf-8") + b"\n")
        try:
            data = path.read_bytes()
        except Exception:
            data = _read_text(path).encode("utf-8", errors="replace")
        h.update(str(len(data)).encode("utf-8") + b"\n")
        h.update(data)
        h.update(b"\n")
    return h.hexdigest()


def _top_digits(digits: Iterable[str], *, top_k: int) -> List[str]:
    counts: Dict[str, int] = {}
    for d in digits:
        if d not in MIRROR_MAP:
            continue
        counts[d] = counts.get(d, 0) + 1
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [d for d, _ in ranked[:top_k]]


def _derive_triads_from_envelope(digits: List[str]) -> List[str]:
    uniq = [d for d in digits if d in MIRROR_MAP]
    uniq = sorted(dict.fromkeys(uniq))  # stable dedupe
    if len(uniq) < 3:
        return []
    if len(uniq) == 3:
        return ["".join(sorted(uniq))]
    # take combinations of 3 from the provided digit envelope (usually size 4)
    triads: set[str] = set()
    for comb in itertools.combinations(uniq, 3):
        triads.add("".join(sorted(comb)))
    return sorted(triads)


def _parse_due_doubles(*, day_dir: Path, state_key: str, top_n: int = 4) -> Tuple[List[dict], List[Path]]:
    """
    Parse the Control Center "Due Doubles" board into bounded BOX packs.

    Input:  sharepacks/<root>/<D>/control_center/due_doubles.csv
    Output: pack(s) with canonicals (doubles) expanded to unique perms.

    Note: this board is grouped by VTRAC *double families*, not vtrac_index.
    """
    path = day_dir / "control_center" / "due_doubles.csv"
    rows = _load_csv_dict_rows(path)
    packs: List[dict] = []
    inputs: List[Path] = []
    if not rows:
        return packs, inputs

    inputs.append(path)

    # Aggregate per state+variant row.
    for r in rows:
        if (r.get("StateKey") or "").strip() != state_key:
            continue
        variant = (r.get("Variant") or "").strip() or "Unknown"
        ds_double = (r.get("Draws Since Double") or "").strip()

        # combo -> (severity, ds_max, badges_set, families_set)
        agg: Dict[str, dict] = {}
        for i in range(1, 6):
            cell = (r.get(f"Family {i}") or "").strip()
            if not cell or cell == "-":
                continue
            family_label = cell.split(":", 1)[0].strip() if ":" in cell else ""
            for m in _DUE_DOUBLES_TOKEN_RE.finditer(cell):
                combo = _normalize_pick3_literal(m.group("combo"))
                if not combo:
                    continue
                severity = m.group("severity")
                badge = m.group("badge")
                try:
                    ds = int(m.group("ds"))
                except Exception:
                    ds = 0

                entry = agg.setdefault(
                    combo,
                    {"severity": severity, "ds_max": ds, "badges": set(), "families": set()},
                )
                # Keep the "best" severity/ds for ranking; merge badges/families.
                if entry["severity"] != "R" and severity == "R":
                    entry["severity"] = "R"
                entry["ds_max"] = max(int(entry.get("ds_max") or 0), ds)
                if badge:
                    entry["badges"].add(badge)
                if family_label:
                    entry["families"].add(family_label)

        if not agg:
            continue

        def rank_key(item: Tuple[str, dict]) -> Tuple[bool, int, str]:
            combo, meta = item
            sev = str(meta.get("severity") or "")
            ds = int(meta.get("ds_max") or 0)
            return (sev != "R", -ds, combo)

        ranked = sorted(agg.items(), key=rank_key)
        canonicals = [combo for combo, _ in ranked[: max(0, int(top_n))]]
        if not canonicals:
            continue

        combos: set[str] = set()
        badges: set[str] = set()
        families: set[str] = set()
        for canon in canonicals:
            combos.update(_unique_perms(canon))
            meta = agg.get(canon) or {}
            badges |= set(meta.get("badges") or set())
            families |= set(meta.get("families") or set())

        why_tags = ["due_doubles", f"top_n:{int(top_n)}"]
        if ds_double:
            why_tags.append(f"row_ds:{ds_double}")
        if badges:
            why_tags.append("badges:" + "".join(sorted(badges)))
        if families:
            # Keep it bounded: record only up to 3 family labels.
            fam_sorted = sorted(families)[:3]
            why_tags.extend([f"fam:{f}" for f in fam_sorted])

        pack = {
            "pack_id": f"due_doubles:{variant}",
            "method_id": "due_doubles",
            "variant": variant,
            "play_mode": "BOX",
            "canonicals": canonicals,
            "combos": sorted(combos),
            "combos_count": len(combos),
            "cost_units": len(combos),
            "why_tags": why_tags,
            "transform_chain": [f"due_doubles:{variant}:top{int(top_n)}", "box_expand_unique_perms"],
            "evidence_paths": [_safe_rel(path)],
        }
        packs.append(pack)

    packs.sort(key=lambda p: p["pack_id"])
    return packs, inputs


def _derive_due_doubles_mirror_packs(*, due_packs: Sequence[dict], seed_top_n: int = 1) -> List[dict]:
    """
    Build bounded mirror-double packs from the Due Doubles canonicals.

    This maps directly to the COMBINATION_FORMING3 doubles transforms:
    - mirror the single digit (6 combos total)
    - mirror the repeated digit (6 combos total)

    We intentionally keep it bounded (default: seed_top_n=1) so cost stays measurable.
    """
    if seed_top_n <= 0:
        return []
    out: List[dict] = []
    for p in due_packs:
        if not isinstance(p, dict):
            continue
        canonicals = p.get("canonicals") or []
        if not isinstance(canonicals, list) or not canonicals:
            continue
        variant = str(p.get("variant") or "Unknown")
        evidence_paths = list(p.get("evidence_paths") or [])
        seed = _canon(str(canonicals[0]))
        if not seed or not _is_double(seed):
            continue

        # Mirror single digit (adds a second double triad; 6 perms total).
        ms = _double_pack_mirror_single_6(seed)
        ms_canon = sorted({_canon(c) for c in ms if _canon(c)})
        out.append(
            {
                "pack_id": f"due_doubles_mirror_single:{variant}:seed={seed}",
                "method_id": "due_doubles_mirror_single",
                "variant": variant,
                "play_mode": "BOX",
                "canonicals": ms_canon,
                "combos": ms,
                "combos_count": len(ms),
                "cost_units": len(ms),
                "why_tags": ["due_doubles", "mirror_single", f"seed:{seed}"],
                "transform_chain": [f"due_doubles:{variant}:seed={seed}", "double_pack_mirror_single_6(vtrac_pair)"],
                "evidence_paths": evidence_paths,
            }
        )

        # Mirror repeated digit (adds a second double triad; 6 perms total).
        md = _double_pack_mirror_double_6(seed)
        md_canon = sorted({_canon(c) for c in md if _canon(c)})
        out.append(
            {
                "pack_id": f"due_doubles_mirror_double:{variant}:seed={seed}",
                "method_id": "due_doubles_mirror_double",
                "variant": variant,
                "play_mode": "BOX",
                "canonicals": md_canon,
                "combos": md,
                "combos_count": len(md),
                "cost_units": len(md),
                "why_tags": ["due_doubles", "mirror_double", f"seed:{seed}"],
                "transform_chain": [f"due_doubles:{variant}:seed={seed}", "double_pack_mirror_double_6(vtrac_pair)"],
                "evidence_paths": evidence_paths,
            }
        )

    out.sort(key=lambda p: p.get("pack_id", ""))
    return out


def _parse_profit_alerts(*, day_dir: Path, state_key: str) -> Tuple[List[dict], List[Path]]:
    path = day_dir / "control_center" / "profit_alerts.csv"
    rows = _load_csv_dict_rows(path)
    packs: List[dict] = []
    inputs: List[Path] = []
    if not rows:
        return packs, inputs

    inputs.append(path)
    for r in rows:
        if (r.get("StateKey") or "").strip() != state_key:
            continue
        suggested = (r.get("Suggested") or "").strip()
        if not suggested or suggested == "OVERLAY":
            continue
        implied_raw = (r.get("ImpliedSet") or "").strip()
        if not implied_raw.startswith("["):
            continue
        try:
            implied = json.loads(implied_raw)
        except Exception:
            continue
        if not isinstance(implied, list):
            continue

        combos = sorted({c for c in (_normalize_pick3_literal(x) for x in implied) if c})
        if not combos:
            continue

        variant = (r.get("Variant") or "").strip() or "Unknown"
        alert_id = (r.get("AlertId") or "").strip() or "?"
        canonical = _canon((r.get("Canonical") or "").strip())
        play_mode = "BOX" if suggested == "BOX" else "STRAIGHT"
        badges = (r.get("Badges") or "").strip()
        why_tags = [t for t in badges.split("/") if t] if badges else []
        strength = (r.get("Strength") or "").strip()
        if strength:
            why_tags.append(f"strength:{strength}")

        pack = {
            "pack_id": f"profit_alerts:{variant}:{alert_id}",
            "method_id": "profit_alerts",
            "variant": variant,
            "play_mode": play_mode,
            "canonicals": [canonical] if canonical else sorted({_canon(c) for c in combos}),
            "combos": combos,
            "combos_count": len(combos),
            "cost_units": len(combos),
            "why_tags": ["profit_alerts", *why_tags],
            "transform_chain": [f"profit_alerts:{variant}:{alert_id}:{suggested}:{canonical or '-'}"],
            "evidence_paths": [_safe_rel(path)],
        }
        packs.append(pack)

    packs.sort(key=lambda p: p["pack_id"])
    return packs, inputs


def _parse_stable_top(*, state_dir: Path, state_key: str, top_n: int = 3) -> Tuple[List[dict], List[Path]]:
    stable_scores = state_dir / "stable" / state_key / f"{state_key}_stable_patterns_scores.csv"
    if not stable_scores.exists():
        return [], []

    rows = _load_csv_dict_rows(stable_scores)
    if not rows:
        return [], [stable_scores]

    # Collect best score per canonical per section.
    best: Dict[Tuple[str, str], float] = {}
    for r in rows:
        section = (r.get("section") or "").strip() or "Unknown"
        canon = _normalize_pick3_literal(r.get("Canonical") or "")
        if canon:
            # Stable outputs Canonical may drop leading zeros; zfill handles that.
            canon = canon.zfill(3)
        else:
            canon = _normalize_pick3_literal(str(r.get("Canonical") or ""))
        if not canon:
            continue
        score_raw = (r.get("score") or "").strip()
        try:
            score = float(score_raw)
        except Exception:
            continue
        key = (section, canon)
        best[key] = max(best.get(key, float("-inf")), score)

    packs: List[dict] = []
    for section in sorted({s for s, _ in best.keys()}):
        ranked = [(canon, best[(section, canon)]) for (_, canon) in best.keys() if _ == section]
        ranked.sort(key=lambda t: (-t[1], t[0]))
        picked = [canon for canon, _ in ranked[:top_n]]
        if not picked:
            continue
        combos: set[str] = set()
        for canon in picked:
            combos.update(_unique_perms(canon))
        pack = {
            "pack_id": f"stable_top:{section}",
            "method_id": "stable_top",
            "variant": section,
            "play_mode": "BOX",
            "canonicals": picked,
            "combos": sorted(combos),
            "combos_count": len(combos),
            "cost_units": len(combos),
            "why_tags": ["stable_top", f"top_n:{top_n}"],
            "transform_chain": [f"stable_scores:{section}:top{top_n}", "box_expand_unique_perms"],
            "evidence_paths": [_safe_rel(stable_scores)],
        }
        packs.append(pack)

    packs.sort(key=lambda p: p["pack_id"])
    return packs, [stable_scores]


def _stable_parse_counter_blob(value: object) -> Counter[str]:
    out: Counter[str] = Counter()
    for chunk in str(value or "").split(";"):
        part = chunk.strip()
        if not part:
            continue
        if ":" in part:
            key, raw_count = part.rsplit(":", 1)
            digits = _digits_only(key)
            if not digits:
                continue
            try:
                count = int(float(raw_count))
            except Exception:
                count = 1
            out[digits] += count
        else:
            digits = _digits_only(part)
            if digits:
                out[digits] += 1
    return out


def _stable_top_counter_items(counter: Counter[str], top_n: int = 6) -> List[Dict[str, Any]]:
    items = sorted(counter.items(), key=lambda kv: (-int(kv[1]), kv[0]))
    return [{"canonical": canon, "count": int(count)} for canon, count in items[:top_n]]


def _stable_counter_from_rollup_items(items: object) -> Counter[str]:
    out: Counter[str] = Counter()
    if not isinstance(items, list):
        return out
    for item in items:
        if not isinstance(item, dict):
            continue
        digits = _digits_only(item.get("canonical") or item.get("value"))
        if not digits:
            continue
        try:
            count = int(float(item.get("count") or 0))
        except Exception:
            count = 0
        out[digits] += max(1, count)
    return out


def _stable_frontier_counts(examples: object) -> Dict[str, int]:
    out = {
        "frontier_rows": 0,
        "frontier_set1_rows": 0,
        "frontier_col12_rows": 0,
        "frontier_set1_col12_rows": 0,
    }
    if not isinstance(examples, list):
        return out
    for item in examples:
        if not isinstance(item, dict):
            continue
        set_label = str(item.get("set") or "").strip()
        column = str(item.get("column") or "").strip()
        out["frontier_rows"] += 1
        if set_label == "Set1":
            out["frontier_set1_rows"] += 1
        if column in {"1", "2"}:
            out["frontier_col12_rows"] += 1
        if set_label == "Set1" and column in {"1", "2"}:
            out["frontier_set1_col12_rows"] += 1
    return out


def _stable_select_lane_seed_canonicals(
    *,
    family_id: int,
    support_counter: Counter[str],
    max_cost_units: int,
) -> List[str]:
    if family_id <= 0 or max_cost_units <= 0 or not _vtrac_get_index_set:
        return []
    try:
        lane_combos = sorted(
            {
                _normalize_pick3_literal(x)
                for x in _vtrac_get_index_set(int(family_id))
                if _normalize_pick3_literal(x)
            }
        )
    except Exception:
        lane_combos = []
    lane_canonicals = sorted({_canon(combo) for combo in lane_combos if _canon(combo)})
    if not lane_canonicals:
        return []

    def rank_key(canon: str) -> Tuple[int, int, int, str]:
        support = int(support_counter.get(canon, 0))
        is_non_double = 1 if len(set(canon)) == 3 else 0
        return (-support, is_non_double, _boxed_cost_units(canon), canon)

    picked: List[str] = []
    cost = 0
    for canon in sorted(lane_canonicals, key=rank_key):
        units = _boxed_cost_units(canon)
        if units <= 0:
            continue
        if cost and (cost + units) > int(max_cost_units):
            continue
        if (cost + units) > int(max_cost_units):
            continue
        picked.append(canon)
        cost += units
    return picked


def _build_stable_lane_vote_pack(
    *,
    section: str,
    family_id: int,
    selected_canonicals: List[str],
    method_id: str,
    pack_id: str,
    why_tags: List[str],
    transform_chain: List[str],
    evidence_paths: List[str],
    family_score: float,
    best_compound_score: float,
    source_counter: Counter[str],
    long_counter: Counter[str],
    meta: Dict[str, Any],
) -> Optional[dict]:
    if not selected_canonicals:
        return None
    combos: set[str] = set()
    canonicals: List[str] = []
    for canon in selected_canonicals:
        triad = _normalize_pick3_literal(canon)
        if not triad:
            continue
        canonicals.append(triad)
        combos.update(_unique_perms(triad))
    canonicals = sorted(set(canonicals))
    combos_list = sorted(combos)
    if not combos_list:
        return None
    return {
        "pack_id": pack_id,
        "method_id": method_id,
        "variant": section,
        "play_mode": "BOX",
        "canonicals": canonicals,
        "combos": combos_list,
        "combos_count": len(combos_list),
        "cost_units": len(combos_list),
        "why_tags": why_tags,
        "transform_chain": transform_chain,
        "evidence_paths": evidence_paths,
        "family_id": int(family_id),
        "family_score": round(float(family_score), 3),
        "best_compound_score": round(float(best_compound_score), 3),
        "source_top_canonicals": _stable_top_counter_items(source_counter, top_n=6),
        "source_long_canonicals": _stable_top_counter_items(long_counter, top_n=6),
        **meta,
    }


def _parse_stable_compound_top(
    *,
    state_dir: Path,
    state_key: str,
    top_n: int,
) -> Tuple[List[dict], List[Path]]:
    if int(top_n) <= 0:
        return [], []
    compound_path = state_dir / "stable" / state_key / f"{state_key}_stable_patterns_compound.csv"
    if not compound_path.exists():
        return [], []
    rows = _load_csv_dict_rows(compound_path)
    if not rows:
        return [], [compound_path]

    by_section: Dict[str, List[Dict[str, str]]] = {}
    for row in rows:
        section = (row.get("section") or "").strip() or "Unknown"
        by_section.setdefault(section, []).append(row)

    packs: List[dict] = []
    for section, items in sorted(by_section.items(), key=lambda kv: kv[0]):
        ranked = sorted(
            items,
            key=lambda r: (
                -_to_float(r.get("compound_score") or 0.0),
                -_to_float(r.get("base_max_score") or 0.0),
                _digits_only(r.get("Canonical")),
            ),
        )
        emitted = 0
        for rank_idx, row in enumerate(ranked, start=1):
            canonical = _normalize_pick3_literal(row.get("Canonical") or "")
            if not canonical:
                continue
            family_id = _to_int(row.get("family_id") or 0)
            combos = _unique_perms(canonical)
            if not combos:
                continue
            packs.append(
                {
                    "pack_id": f"stable_compound_top:{section}:canon={canonical}",
                    "method_id": "stable_compound_top",
                    "variant": section,
                    "play_mode": "BOX",
                    "canonicals": [canonical],
                    "combos": combos,
                    "combos_count": len(combos),
                    "cost_units": len(combos),
                    "why_tags": [
                        "stable_compound_top",
                        f"compound_rank:{rank_idx}",
                        f"compound_score:{_to_float(row.get('compound_score')):.3f}",
                        f"family_id:{family_id}",
                        f"top_n:{int(top_n)}",
                    ],
                    "transform_chain": [
                        f"stable_compound:{section}:rank{rank_idx}",
                        "canonical_3digit_direct",
                        "box_expand_unique_perms",
                    ],
                    "evidence_paths": [_safe_rel(compound_path)],
                    "family_id": family_id or None,
                    "compound_score": round(_to_float(row.get("compound_score")), 3),
                    "base_max_score": round(_to_float(row.get("base_max_score")), 3),
                    "set_chain_depth": _to_int(row.get("set_chain_depth")),
                    "draw_chain_depth": _to_int(row.get("draw_chain_depth")),
                    "rows_covered": _to_int(row.get("rows_covered")),
                    "compound_why": str(row.get("compound_why") or ""),
                    "compound_examples": [tok for tok in str(row.get("examples") or "").split(";") if tok],
                }
            )
            emitted += 1
            if emitted >= int(top_n):
                break

    packs.sort(key=lambda p: p.get("pack_id", ""))
    return packs, [compound_path]


def _aggregate_stable_family_lanes(rows: Sequence[Dict[str, str]]) -> Dict[str, List[Dict[str, Any]]]:
    by_key: Dict[Tuple[str, int], Dict[str, Any]] = {}
    for row in rows:
        section = (row.get("section") or "").strip() or "Unknown"
        family_id = _to_int(row.get("family_id") or 0)
        if family_id <= 0:
            continue
        key = (section, family_id)
        entry = by_key.setdefault(
            key,
            {
                "section": section,
                "family_id": family_id,
                "rows_count": 0,
                "family_score_max": 0.0,
                "best_compound_score_max": 0.0,
                "last_remaining_rows": 0,
                "progression_rows": 0,
                "dom_last_rows": 0,
                "frontier_rows": 0,
                "frontier_set1_rows": 0,
                "frontier_col12_rows": 0,
                "frontier_set1_col12_rows": 0,
                "source_counter": Counter(),
                "long_counter": Counter(),
                "frontier_examples": [],
            },
        )
        entry["rows_count"] += 1
        entry["family_score_max"] = max(float(entry["family_score_max"]), _to_float(row.get("family_score")))
        entry["best_compound_score_max"] = max(float(entry["best_compound_score_max"]), _to_float(row.get("best_compound_score")))
        if _to_bool(row.get("last_remaining_3v")):
            entry["last_remaining_rows"] += 1
        if _to_bool(row.get("progression_flag")):
            entry["progression_rows"] += 1
        if _to_bool(row.get("any_dom_last")):
            entry["dom_last_rows"] += 1
        set_label = str(row.get("Set") or "").strip()
        column = str(row.get("Column") or "").strip()
        entry["frontier_rows"] += 1
        if set_label == "Set1":
            entry["frontier_set1_rows"] += 1
        if column in {"1", "2"}:
            entry["frontier_col12_rows"] += 1
        if set_label == "Set1" and column in {"1", "2"}:
            entry["frontier_set1_col12_rows"] += 1
        counter = _stable_parse_counter_blob(row.get("top_canonicals"))
        for canon, count in counter.items():
            if len(canon) == 3:
                entry["source_counter"][canon] += int(count)
            elif len(canon) > 3:
                entry["long_counter"][canon] += int(count)
        entry["frontier_examples"].append(
            {
                "set": str(row.get("Set") or ""),
                "draw": str(row.get("Draw") or ""),
                "column": str(row.get("Column") or ""),
                "family_score": round(_to_float(row.get("family_score")), 3),
                "last_remaining_3v": _to_bool(row.get("last_remaining_3v")),
                "top_canonicals": str(row.get("top_canonicals") or ""),
            }
        )

    out: Dict[str, List[Dict[str, Any]]] = {}
    for (_, _family_id), entry in by_key.items():
        out.setdefault(entry["section"], []).append(entry)
    for section, items in out.items():
        items.sort(
            key=lambda item: (
                -float(item["family_score_max"]),
                -float(item["best_compound_score_max"]),
                -int(item["last_remaining_rows"]),
                -int(item["rows_count"]),
                int(item["family_id"]),
            )
        )
    return out


def _parse_stable_family_vote(
    *,
    state_dir: Path,
    state_key: str,
    top_n: int,
    max_cost_units: int,
) -> Tuple[List[dict], List[Path]]:
    if int(top_n) <= 0 or int(max_cost_units) <= 0:
        return [], []
    if not _vtrac_get_index_set:
        return [], []
    families_path = state_dir / "stable" / state_key / f"{state_key}_stable_patterns_families.csv"
    compound_path = state_dir / "stable" / state_key / f"{state_key}_stable_patterns_compound.csv"
    if not families_path.exists():
        return [], []
    rows = _load_csv_dict_rows(families_path)
    if not rows:
        return [], [families_path]

    by_section = _aggregate_stable_family_lanes(rows)
    evidence_paths = [_safe_rel(families_path)]
    if compound_path.exists():
        evidence_paths.append(_safe_rel(compound_path))

    packs: List[dict] = []
    for section, items in sorted(by_section.items(), key=lambda kv: kv[0]):
        for rank_idx, item in enumerate(items[: int(top_n)], start=1):
            selected = _stable_select_lane_seed_canonicals(
                family_id=int(item["family_id"]),
                support_counter=item["source_counter"],
                max_cost_units=int(max_cost_units),
            )
            pack = _build_stable_lane_vote_pack(
                section=section,
                family_id=int(item["family_id"]),
                selected_canonicals=selected,
                method_id="stable_family_vote",
                pack_id=f"stable_family_vote:{section}:family={int(item['family_id'])}",
                why_tags=[
                    "stable_family_vote",
                    f"family_id:{int(item['family_id'])}",
                    f"family_rank:{rank_idx}",
                    f"family_score:{float(item['family_score_max']):.3f}",
                    f"best_compound:{float(item['best_compound_score_max']):.3f}",
                    f"top_n:{int(top_n)}",
                    f"cap:{int(max_cost_units)}",
                ],
                transform_chain=[
                    f"stable_families:{section}:family={int(item['family_id'])}:rank{rank_idx}",
                    f"stable_lane_vote:cap{int(max_cost_units)}",
                    "box_expand_unique_perms",
                ],
                evidence_paths=evidence_paths,
                family_score=float(item["family_score_max"]),
                best_compound_score=float(item["best_compound_score_max"]),
                source_counter=item["source_counter"],
                long_counter=item["long_counter"],
                meta={
                    "rows_count": int(item["rows_count"]),
                    "last_remaining_rows": int(item["last_remaining_rows"]),
                    "progression_rows": int(item["progression_rows"]),
                    "dom_last_rows": int(item["dom_last_rows"]),
                    "frontier_rows": int(item["frontier_rows"]),
                    "frontier_set1_rows": int(item["frontier_set1_rows"]),
                    "frontier_col12_rows": int(item["frontier_col12_rows"]),
                    "frontier_set1_col12_rows": int(item["frontier_set1_col12_rows"]),
                    "frontier_examples": sorted(
                        item["frontier_examples"],
                        key=lambda row: (-float(row["family_score"]), row["set"], row["draw"], row["column"]),
                    )[:3],
                },
            )
            if pack is not None:
                packs.append(pack)

    packs.sort(key=lambda p: p.get("pack_id", ""))
    return packs, [families_path] + ([compound_path] if compound_path.exists() else [])


def _stable_family_vote_v2_score(
    *,
    item: Dict[str, Any],
    legacy_item: Dict[str, Any],
    legacy_rank: int,
    arena_rank: int,
    leader_total: float,
    leader_compound: float,
) -> Optional[Dict[str, Any]]:
    family_total = _to_float(item.get("family_score_total"))
    family_max = _to_float(item.get("family_score_max"))
    best_compound = _to_float(item.get("best_compound_score_max"))
    progression = max(_to_int(item.get("progression_count")), _to_int(legacy_item.get("progression_rows")))
    last_remaining = max(_to_int(item.get("last_remaining_count")), _to_int(legacy_item.get("last_remaining_rows")))
    dom_last = max(_to_int(item.get("dom_last_count")), _to_int(legacy_item.get("dom_last_rows")))
    frontier_examples = _stable_frontier_counts(item.get("example_boxes"))
    frontier = {
        "frontier_rows": max(int(frontier_examples["frontier_rows"]), _to_int(legacy_item.get("frontier_rows"))),
        "frontier_set1_rows": max(int(frontier_examples["frontier_set1_rows"]), _to_int(legacy_item.get("frontier_set1_rows"))),
        "frontier_col12_rows": max(int(frontier_examples["frontier_col12_rows"]), _to_int(legacy_item.get("frontier_col12_rows"))),
        "frontier_set1_col12_rows": max(
            int(frontier_examples["frontier_set1_col12_rows"]),
            _to_int(legacy_item.get("frontier_set1_col12_rows")),
        ),
    }
    hidden_summary = item.get("hidden_family_reveal_summary") or {}
    order_summary = item.get("order_transform_summary") or {}
    hidden_total = _to_float(hidden_summary.get("reveal_score_total"))
    hidden_hits = _to_int(hidden_summary.get("row_hits"))
    order_total = _to_float(order_summary.get("support_score_total"))
    order_hits = _to_int(order_summary.get("row_hits"))
    family_total_denom = max(family_total, 1.0)
    hidden_density = min(hidden_total / family_total_denom, 20.0)
    order_density = min(order_total / family_total_denom, 20.0)
    rank_gain = max(0, int(legacy_rank) - int(arena_rank))

    has_primary_signal = any(
        (
            progression > 0,
            last_remaining > 0,
            dom_last > 0,
            frontier["frontier_col12_rows"] > 0,
            frontier["frontier_set1_col12_rows"] > 0,
        )
    )
    strong_enough = (
        family_total >= max(80.0, float(leader_total) * 0.30)
        or best_compound >= max(20.0, float(leader_compound) * 0.45)
        or last_remaining > 0
    )
    if not has_primary_signal or not strong_enough:
        return None

    score = (
        family_total
        + family_max
        + best_compound
        + (15.0 * progression)
        + (18.0 * last_remaining)
        + (6.0 * dom_last)
        + (8.0 * frontier["frontier_col12_rows"])
        + (16.0 * frontier["frontier_set1_col12_rows"])
        + (25.0 * rank_gain)
        + (6.0 * hidden_density)
        + (6.0 * order_density)
    )
    return {
        "promotion_score": round(score, 3),
        "family_score_total": round(family_total, 3),
        "family_score_max": round(family_max, 3),
        "best_compound_score_max": round(best_compound, 3),
        "progression_count": progression,
        "last_remaining_count": last_remaining,
        "dom_last_count": dom_last,
        "frontier_rows": int(frontier["frontier_rows"]),
        "frontier_set1_rows": int(frontier["frontier_set1_rows"]),
        "frontier_col12_rows": int(frontier["frontier_col12_rows"]),
        "frontier_set1_col12_rows": int(frontier["frontier_set1_col12_rows"]),
        "hidden_reveal_score_total": round(hidden_total, 3),
        "hidden_reveal_row_hits": hidden_hits,
        "hidden_reveal_density": round(hidden_density, 3),
        "order_transform_support_total": round(order_total, 3),
        "order_transform_row_hits": order_hits,
        "order_transform_density": round(order_density, 3),
        "legacy_rank": int(legacy_rank),
        "rank_gain": int(rank_gain),
    }


def _parse_stable_family_vote_v2(
    *,
    state_dir: Path,
    state_key: str,
    top_n: int,
    legacy_top_n: int,
    max_cost_units: int,
    arena_payload: Optional[Dict[str, Any]],
) -> Tuple[List[dict], List[Path]]:
    if int(top_n) <= 0 or int(max_cost_units) <= 0 or not _vtrac_get_index_set:
        return [], []
    families_path = state_dir / "stable" / state_key / f"{state_key}_stable_patterns_families.csv"
    compound_path = state_dir / "stable" / state_key / f"{state_key}_stable_patterns_compound.csv"
    metrics_path = state_dir / "stable" / state_key / f"{state_key}_metrics.json"
    if not families_path.exists() or arena_payload is None:
        return [], []
    rows = _load_csv_dict_rows(families_path)
    if not rows:
        return [], [families_path]

    legacy_by_section = _aggregate_stable_family_lanes(rows)
    sections = arena_payload.get("sections") or {}
    if not isinstance(sections, dict):
        return [], [families_path]

    evidence_paths = [_safe_rel(families_path)]
    if compound_path.exists():
        evidence_paths.append(_safe_rel(compound_path))
    if metrics_path.exists():
        evidence_paths.append(_safe_rel(metrics_path))

    packs: List[dict] = []
    for section, section_payload in sorted(sections.items(), key=lambda kv: kv[0]):
        if not isinstance(section_payload, dict):
            continue
        family_rollups = section_payload.get("family_rollups_top") or []
        if not isinstance(family_rollups, list) or not family_rollups:
            continue
        legacy_items = legacy_by_section.get(section) or []
        legacy_map = {int(item["family_id"]): item for item in legacy_items}
        legacy_rank_map = {int(item["family_id"]): idx for idx, item in enumerate(legacy_items, start=1)}
        legacy_top_ids = {
            int(item["family_id"])
            for item in legacy_items[: max(0, int(legacy_top_n))]
            if _to_int(item.get("family_id")) > 0
        }
        leader_total = max((_to_float(item.get("family_score_total")) for item in family_rollups), default=0.0)
        leader_compound = max((_to_float(item.get("best_compound_score_max")) for item in family_rollups), default=0.0)

        ranked_candidates: List[Dict[str, Any]] = []
        for arena_rank, rollup in enumerate(family_rollups, start=1):
            if not isinstance(rollup, dict):
                continue
            family_id = _to_int(rollup.get("family_id"))
            if family_id <= 0 or family_id in legacy_top_ids:
                continue
            legacy_item = legacy_map.get(family_id)
            if legacy_item is None:
                continue
            legacy_rank = int(legacy_rank_map.get(family_id, 999999))
            score_meta = _stable_family_vote_v2_score(
                item=rollup,
                legacy_item=legacy_item,
                legacy_rank=legacy_rank,
                arena_rank=arena_rank,
                leader_total=leader_total,
                leader_compound=leader_compound,
            )
            if score_meta is None:
                continue
            support_counter = Counter(legacy_item["source_counter"])
            support_counter.update(_stable_counter_from_rollup_items(rollup.get("top_canonicals")))
            long_counter = Counter(legacy_item["long_counter"])
            for canonical, count in _stable_counter_from_rollup_items(rollup.get("top_canonicals")).items():
                if len(canonical) > 3:
                    long_counter[canonical] += int(count)
            selected = _stable_select_lane_seed_canonicals(
                family_id=family_id,
                support_counter=support_counter,
                max_cost_units=int(max_cost_units),
            )
            if not selected:
                continue
            ranked_candidates.append(
                {
                    "family_id": family_id,
                    "arena_rank": arena_rank,
                    "legacy_rank": legacy_rank,
                    "legacy_item": legacy_item,
                    "rollup": rollup,
                    "support_counter": support_counter,
                    "long_counter": long_counter,
                    "selected": selected,
                    **score_meta,
                }
            )

        ranked_candidates.sort(
            key=lambda item: (
                -float(item["promotion_score"]),
                -int(item["frontier_set1_col12_rows"]),
                -int(item["progression_count"]),
                -float(item["family_score_total"]),
                int(item["family_id"]),
            )
        )
        for promo_rank, item in enumerate(ranked_candidates[: int(top_n)], start=1):
            rollup = item["rollup"]
            pack = _build_stable_lane_vote_pack(
                section=section,
                family_id=int(item["family_id"]),
                selected_canonicals=item["selected"],
                method_id="stable_family_vote_v2",
                pack_id=f"stable_family_vote_v2:{section}:family={int(item['family_id'])}",
                why_tags=[
                    "stable_family_vote_v2",
                    f"family_id:{int(item['family_id'])}",
                    f"promotion_rank:{promo_rank}",
                    f"arena_rank:{int(item['arena_rank'])}",
                    f"legacy_rank:{int(item['legacy_rank'])}",
                    f"rank_gain:{int(item['rank_gain'])}",
                    f"promotion_score:{float(item['promotion_score']):.3f}",
                    f"family_score_total:{float(item['family_score_total']):.3f}",
                    f"best_compound:{float(item['best_compound_score_max']):.3f}",
                    f"progression_count:{int(item['progression_count'])}",
                    f"frontier_col12:{int(item['frontier_col12_rows'])}",
                    f"frontier_set1_col12:{int(item['frontier_set1_col12_rows'])}",
                    f"cap:{int(max_cost_units)}",
                    "promotion_reason:v2_richer_family_gate",
                ],
                transform_chain=[
                    f"stable_arena_family_rollup:{section}:family={int(item['family_id'])}:rank{int(item['arena_rank'])}",
                    f"stable_family_vote_v2:cap{int(max_cost_units)}",
                    "box_expand_unique_perms",
                ],
                evidence_paths=evidence_paths,
                family_score=float(item["family_score_total"]),
                best_compound_score=float(item["best_compound_score_max"]),
                source_counter=item["support_counter"],
                long_counter=item["long_counter"],
                meta={
                    "arena_family_rank": int(item["arena_rank"]),
                    "legacy_family_rank": int(item["legacy_rank"]),
                    "rank_gain": int(item["rank_gain"]),
                    "rows_count": int(item["legacy_item"]["rows_count"]),
                    "last_remaining_rows": int(item["legacy_item"]["last_remaining_rows"]),
                    "progression_rows": int(item["legacy_item"]["progression_rows"]),
                    "dom_last_rows": int(item["legacy_item"]["dom_last_rows"]),
                    "frontier_rows": int(item["frontier_rows"]),
                    "frontier_set1_rows": int(item["frontier_set1_rows"]),
                    "frontier_col12_rows": int(item["frontier_col12_rows"]),
                    "frontier_set1_col12_rows": int(item["frontier_set1_col12_rows"]),
                    "promotion_score": float(item["promotion_score"]),
                    "family_score_total": float(item["family_score_total"]),
                    "family_score_max": float(item["family_score_max"]),
                    "hidden_reveal_score_total": float(item["hidden_reveal_score_total"]),
                    "hidden_reveal_row_hits": int(item["hidden_reveal_row_hits"]),
                    "hidden_reveal_density": float(item["hidden_reveal_density"]),
                    "order_transform_support_total": float(item["order_transform_support_total"]),
                    "order_transform_row_hits": int(item["order_transform_row_hits"]),
                    "order_transform_density": float(item["order_transform_density"]),
                    "top_modal_orders": list(rollup.get("top_modal_orders") or [])[:6],
                    "frontier_examples": list(rollup.get("example_boxes") or [])[:3],
                },
            )
            if pack is not None:
                packs.append(pack)

    packs.sort(key=lambda p: p.get("pack_id", ""))
    return packs, [families_path] + ([compound_path] if compound_path.exists() else []) + ([metrics_path] if metrics_path.exists() else [])


def _parse_stable_last_remaining(
    *,
    state_dir: Path,
    state_key: str,
    top_n: int,
    max_cost_units: int,
) -> Tuple[List[dict], List[Path]]:
    if int(top_n) <= 0 or int(max_cost_units) <= 0:
        return [], []
    if not _vtrac_get_index_set:
        return [], []
    families_path = state_dir / "stable" / state_key / f"{state_key}_stable_patterns_families.csv"
    compound_path = state_dir / "stable" / state_key / f"{state_key}_stable_patterns_compound.csv"
    if not families_path.exists():
        return [], []
    rows = [row for row in _load_csv_dict_rows(families_path) if _to_bool(row.get("last_remaining_3v"))]
    if not rows:
        return [], [families_path]

    by_section = _aggregate_stable_family_lanes(rows)
    evidence_paths = [_safe_rel(families_path)]
    if compound_path.exists():
        evidence_paths.append(_safe_rel(compound_path))

    packs: List[dict] = []
    for section, items in sorted(by_section.items(), key=lambda kv: kv[0]):
        ranked = sorted(
            items,
            key=lambda item: (
                -int(item["last_remaining_rows"]),
                -float(item["family_score_max"]),
                -float(item["best_compound_score_max"]),
                int(item["family_id"]),
            ),
        )
        for rank_idx, item in enumerate(ranked[: int(top_n)], start=1):
            selected = _stable_select_lane_seed_canonicals(
                family_id=int(item["family_id"]),
                support_counter=item["source_counter"],
                max_cost_units=int(max_cost_units),
            )
            pack = _build_stable_lane_vote_pack(
                section=section,
                family_id=int(item["family_id"]),
                selected_canonicals=selected,
                method_id="stable_last_remaining",
                pack_id=f"stable_last_remaining:{section}:family={int(item['family_id'])}",
                why_tags=[
                    "stable_last_remaining",
                    f"family_id:{int(item['family_id'])}",
                    f"survivor_rank:{rank_idx}",
                    f"last_remaining_rows:{int(item['last_remaining_rows'])}",
                    f"family_score:{float(item['family_score_max']):.3f}",
                    f"top_n:{int(top_n)}",
                    f"cap:{int(max_cost_units)}",
                ],
                transform_chain=[
                    f"stable_families_last_remaining:{section}:family={int(item['family_id'])}:rank{rank_idx}",
                    f"stable_lane_vote:cap{int(max_cost_units)}",
                    "box_expand_unique_perms",
                ],
                evidence_paths=evidence_paths,
                family_score=float(item["family_score_max"]),
                best_compound_score=float(item["best_compound_score_max"]),
                source_counter=item["source_counter"],
                long_counter=item["long_counter"],
                meta={
                    "rows_count": int(item["rows_count"]),
                    "last_remaining_rows": int(item["last_remaining_rows"]),
                    "progression_rows": int(item["progression_rows"]),
                    "dom_last_rows": int(item["dom_last_rows"]),
                    "frontier_rows": int(item["frontier_rows"]),
                    "frontier_set1_rows": int(item["frontier_set1_rows"]),
                    "frontier_col12_rows": int(item["frontier_col12_rows"]),
                    "frontier_set1_col12_rows": int(item["frontier_set1_col12_rows"]),
                    "frontier_examples": sorted(
                        item["frontier_examples"],
                        key=lambda row: (-float(row["family_score"]), row["set"], row["draw"], row["column"]),
                    )[:3],
                },
            )
            if pack is not None:
                packs.append(pack)

    packs.sort(key=lambda p: p.get("pack_id", ""))
    return packs, [families_path] + ([compound_path] if compound_path.exists() else [])


def _parse_dr_top(*, state_dir: Path, state_key: str, top_n: int = 3) -> Tuple[List[dict], List[Path]]:
    path = state_dir / "digit_reduction" / state_key / "analyzer_v2" / f"{state_key}_analyzer_v2_top_candidates.csv"
    if not path.exists():
        return [], []
    rows = _load_csv_dict_rows(path)
    if not rows:
        return [], [path]

    by_variant: Dict[str, List[Dict[str, str]]] = {}
    for r in rows:
        variant = (r.get("variant") or "").strip() or "Unknown"
        by_variant.setdefault(variant, []).append(r)

    packs: List[dict] = []
    for variant, items in sorted(by_variant.items(), key=lambda kv: kv[0]):
        # stable ordering: rank then score desc then pattern
        def key_fn(r: Dict[str, str]) -> Tuple[int, float, str]:
            rank = int((r.get("rank") or "999999").strip() or 999999)
            try:
                score = float((r.get("score") or "").strip())
            except Exception:
                score = float("-inf")
            pat = _normalize_pick3_literal(r.get("best_pattern") or "")
            return (rank, -score, pat)

        ordered = sorted(items, key=key_fn)
        combos: List[str] = []
        why: List[str] = []
        for r in ordered:
            if len(combos) >= top_n:
                break
            pat = _normalize_pick3_literal(r.get("best_pattern") or "")
            if not pat:
                continue
            combos.append(pat)
            tags = (r.get("evidence_tags") or "").strip()
            if tags:
                why.extend([t for t in tags.split(",") if t])

        combos = sorted(set(combos))
        if not combos:
            continue
        pack = {
            "pack_id": f"digit_reduction_top:{variant}",
            "method_id": "digit_reduction_analyzer_v2",
            "variant": variant,
            "play_mode": "STRAIGHT",
            "canonicals": sorted({_canon(c) for c in combos if _canon(c)}),
            "combos": combos,
            "combos_count": len(combos),
            "cost_units": len(combos),
            "why_tags": ["digit_reduction", f"top_n:{top_n}", *sorted(set(why))],
            "transform_chain": [f"dr_analyzer_v2:{variant}:top{top_n}"],
            "evidence_paths": [_safe_rel(path)],
        }
        packs.append(pack)

    packs.sort(key=lambda p: p["pack_id"])
    return packs, [path]


@dataclass(frozen=True)
class _DrStepRow:
    step: int
    unique_digits: int
    digits: Tuple[str, ...]


@dataclass(frozen=True)
class _DrCandidateSets:
    singles: Tuple[str, ...]
    doubles: Tuple[str, ...]
    triples: Tuple[str, ...]


@dataclass
class _Dr004PoolAgg:
    score_raw: float = 0.0
    lanes: set[str] = field(default_factory=set)
    earliest_step: Optional[int] = None
    span_max: int = 0
    span_sum: int = 0
    segments: int = 0


def _boxed_cost_units(canon: str) -> int:
    """
    Box closure cost proxy: number of unique permutations.

    - triple: 1
    - double: 3
    - all distinct: 6
    """
    canon = _canon(canon)
    if not canon:
        return 0
    a, b, c = canon
    if a == b == c:
        return 1
    if a == b or b == c:
        return 3
    return 6


def _dr_candidate_sets_for_digits(digits: Tuple[str, ...]) -> _DrCandidateSets:
    if not digits:
        return _DrCandidateSets((), (), ())
    if len(digits) == 1:
        d = digits[0]
        return _DrCandidateSets((), (), (d + d + d,))

    doubles: List[str] = []
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            a, b = digits[i], digits[j]
            doubles.append("".join(sorted(a + a + b)))
            doubles.append("".join(sorted(a + b + b)))

    singles: List[str] = []
    if len(digits) >= 3:
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                for k in range(j + 1, len(digits)):
                    singles.append(digits[i] + digits[j] + digits[k])

    return _DrCandidateSets(tuple(sorted(set(singles))), tuple(sorted(set(doubles))), ())


def _load_dr_step_rows(*, steps_csv: Path, section: str) -> List[_DrStepRow]:
    rows: List[_DrStepRow] = []
    with steps_csv.open("r", encoding="utf-8", errors="replace", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            if (row.get("section") or "").strip() != section:
                continue
            val = "".join(ch for ch in (row.get("value") or "") if ch.isdigit())
            if not val:
                continue
            digits = tuple(sorted(set(val)))
            try:
                step = int((row.get("step") or "0").strip() or 0)
            except Exception:
                step = 0
            try:
                unique_digits = int((row.get("unique_digits") or "0").strip() or 0)
            except Exception:
                unique_digits = 0
            if unique_digits <= 0:
                unique_digits = len(digits)
            rows.append(_DrStepRow(step=step, unique_digits=unique_digits, digits=digits))
    return rows


def _rank_dr_envelope_candidates(
    *,
    rows: Sequence[_DrStepRow],
    candidate_cache: Dict[Tuple[str, ...], _DrCandidateSets],
    max_unique_digits: int,
    step_power: float,
    unique_power: float,
    double_weight: float,
    split_weight: bool,
) -> List[Tuple[str, float]]:
    scores: Dict[str, float] = {}
    for r in rows:
        if r.unique_digits <= 0 or r.unique_digits > max_unique_digits:
            continue
        step_w = 1.0 / ((1 + r.step) ** step_power) if step_power else 1.0
        uniq_w = 1.0 / (r.unique_digits**unique_power) if unique_power else 1.0
        base = step_w * uniq_w

        sets = candidate_cache.get(r.digits)
        if sets is None:
            sets = _dr_candidate_sets_for_digits(r.digits)
            candidate_cache[r.digits] = sets

        if sets.singles:
            w = base / len(sets.singles) if split_weight else base
            for c in sets.singles:
                scores[c] = scores.get(c, 0.0) + w

        if double_weight > 0 and sets.doubles:
            w = (base * double_weight) / len(sets.doubles) if split_weight else (base * double_weight)
            for c in sets.doubles:
                scores[c] = scores.get(c, 0.0) + w

        if sets.triples:
            w = base / len(sets.triples) if split_weight else base
            for c in sets.triples:
                scores[c] = scores.get(c, 0.0) + w

    return sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))


def _parse_dr_envelope_steps(
    *,
    state_dir: Path,
    state_key: str,
    boxed_canonicals: int,
    max_unique_digits: int = 7,
    step_power: float = 2.0,
    unique_power: float = 1.0,
    double_weight: float = 0.25,
    split_weight: bool = True,
) -> Tuple[List[dict], List[Path]]:
    """
    Optional Digit Reduction envelope pack (v0.3 prework).

    Reads only sharepack-local DR trace evidence:
      digit_reduction/<STATE>/training/<STATE>_digit_reduction_steps.csv

    Emits bounded BOX packs per section (Combined/Midday/Evening) by ranking canonicals derived
    from digit pools (early steps + smaller pools weighted higher).
    """
    if boxed_canonicals <= 0:
        return [], []

    steps_csv = (
        state_dir
        / "digit_reduction"
        / state_key
        / "training"
        / f"{state_key}_digit_reduction_steps.csv"
    )
    if not steps_csv.exists():
        return [], []

    packs: List[dict] = []
    candidate_cache: Dict[Tuple[str, ...], _DrCandidateSets] = {}
    for section in ("Combined", "Midday", "Evening"):
        step_rows = _load_dr_step_rows(steps_csv=steps_csv, section=section)
        if not step_rows:
            continue
        ranked = _rank_dr_envelope_candidates(
            rows=step_rows,
            candidate_cache=candidate_cache,
            max_unique_digits=max_unique_digits,
            step_power=step_power,
            unique_power=unique_power,
            double_weight=double_weight,
            split_weight=split_weight,
        )
        picked = [_canon(c) for c, _ in ranked if _canon(c)][: int(boxed_canonicals)]
        picked = [c for c in picked if c]
        if not picked:
            continue
        combos: set[str] = set()
        for canon in picked:
            combos.update(_unique_perms(canon))
        combos_list = sorted(combos)
        if not combos_list:
            continue
        packs.append(
            {
                "pack_id": f"digit_reduction_envelope:{section}:top{int(boxed_canonicals)}",
                "method_id": "digit_reduction_envelope_steps",
                "variant": section,
                "play_mode": "BOX",
                "canonicals": sorted(set(picked)),
                "combos": combos_list,
                "combos_count": len(combos_list),
                "cost_units": len(combos_list),
                "why_tags": [
                    "digit_reduction",
                    "envelope",
                    "steps_csv",
                    f"boxed_canonicals:{int(boxed_canonicals)}",
                    f"max_unique_digits:{int(max_unique_digits)}",
                    f"step_power:{step_power:g}",
                    f"unique_power:{unique_power:g}",
                    f"double_weight:{double_weight:g}",
                    "split_weight" if split_weight else "no_split_weight",
                ],
                "transform_chain": [
                    f"dr_steps_csv:{section}",
                    f"dr_envelope_rank:u{int(max_unique_digits)}_sp{step_power:g}_up{unique_power:g}_dw{double_weight:g}{'_split' if split_weight else ''}",
                    f"seed_top{int(boxed_canonicals)}",
                    "box_expand_unique_perms",
                ],
                "evidence_paths": [_safe_rel(steps_csv)],
            }
        )

    packs.sort(key=lambda p: p.get("pack_id", ""))
    return packs, [steps_csv]


def _find_sharepack_draws_csv(*, state_dir: Path, state_key: str) -> Optional[Path]:
    draws_dir = state_dir / "aux" / "draws"
    if not draws_dir.exists():
        return None
    candidates = sorted(draws_dir.glob("*_draws.csv"))
    if not candidates:
        return None
    # Prefer matching the state name (e.g., Florida4 -> Florida_draws.csv).
    wanted = re.sub(r"\d+$", "", (state_key or "").strip()).lower()
    if wanted:
        exact = f"{wanted}_draws.csv"
        for p in candidates:
            if p.name.lower() == exact:
                return p
    for p in candidates:
        if wanted and wanted in p.name.lower():
            return p
    return candidates[0]


def _find_sharepack_draws_csv_for_variant(*, state_dir: Path, state_key: str, variant: str) -> Optional[Path]:
    draws_dir = state_dir / "aux" / "draws"
    if not draws_dir.exists():
        return None
    candidates = sorted(draws_dir.glob("*_draws.csv"))
    if not candidates:
        return None
    v = (variant or "").strip().lower()
    if v in {"combined", "c"}:
        # Prefer matching state name and excluding Midday/Evening files.
        wanted = re.sub(r"\d+$", "", (state_key or "").strip()).lower()
        for p in candidates:
            name = p.name.lower()
            if "_midday_" in name or "_evening_" in name:
                continue
            if wanted and name == f"{wanted}_draws.csv":
                return p
        for p in candidates:
            name = p.name.lower()
            if "_midday_" in name or "_evening_" in name:
                continue
            if wanted and wanted in name:
                return p
        for p in candidates:
            name = p.name.lower()
            if "_midday_" not in name and "_evening_" not in name:
                return p
        return candidates[0]
    if v in {"midday", "m"}:
        for p in candidates:
            if "_midday_" in p.name.lower():
                return p
        return None
    if v in {"evening", "e"}:
        for p in candidates:
            if "_evening_" in p.name.lower():
                return p
        return None
    return None


def _read_draws_list(*, draws_csv: Path, max_n: int = 1000) -> List[str]:
    if not draws_csv.exists():
        return []
    out: List[str] = []
    with draws_csv.open("r", encoding="utf-8", errors="replace", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            draw = _normalize_pick3_literal(row.get("Draw") or row.get("draw") or "")
            if draw:
                out.append(draw)
            if len(out) >= max_n:
                break
    return out


def _load_recent_draw_digits(*, draws_csv: Path, recent_draws: int) -> set[str]:
    if recent_draws <= 0 or not draws_csv.exists():
        return set()
    digits: set[str] = set()
    with draws_csv.open("r", encoding="utf-8", errors="replace", newline="") as f:
        r = csv.DictReader(f)
        for i, row in enumerate(r):
            if i >= recent_draws:
                break
            draw = _normalize_pick3_literal(row.get("Draw") or row.get("draw") or "")
            if not draw:
                continue
            digits.update(draw)
    return digits


def _parse_dr004_steps(
    *,
    state_dir: Path,
    state_key: str,
    boxed_canonicals: int,
    index_boxed_canonicals: int,
    recent_draws: int,
    max_cost_units: int,
    min_unique_digits: int = 1,
    max_unique_digits: int = 3,
    signals_out: Optional[Dict[str, Any]] = None,
    signals_top_pools: int = 12,
    signals_top_canonicals: int = 25,
    signals_top_indices: int = 12,
) -> Tuple[List[dict], List[Path]]:
    """
    Optional Digit Reduction DR-004 packs (selection-layer transform; default-off).

    Reads only:
      - digit_reduction/<STATE>/training/<STATE>_digit_reduction_steps.csv
      - aux/draws/*_draws.csv (optional; recency penalty)

    Emits bounded BOX packs per section (Combined/Midday/Evening) using:
      - early-arrival (step) + persistence (segment span)
      - breadth (repeat across lanes/locations)
      - cross-variant convergence (Midday+Evening boost; Combined mild boost)
      - optional recent-digit overlap penalty (negative filter)
    """
    creating_packs = boxed_canonicals > 0 or index_boxed_canonicals > 0
    if not creating_packs and signals_out is None:
        return [], []
    if int(min_unique_digits) < 1:
        min_unique_digits = 1
    if int(max_unique_digits) < int(min_unique_digits):
        max_unique_digits = int(min_unique_digits)

    steps_csv = (
        state_dir
        / "digit_reduction"
        / state_key
        / "training"
        / f"{state_key}_digit_reduction_steps.csv"
    )
    if not steps_csv.exists():
        return [], []

    draws_csv = _find_sharepack_draws_csv(state_dir=state_dir, state_key=state_key)
    recent_digits = _load_recent_draw_digits(draws_csv=draws_csv, recent_draws=int(recent_draws)) if draws_csv else set()

    # Tunables (kept internal for v1; expose later only if evidence-gated).
    step_power = 2.0
    unique_power = 1.0
    persistence_power = 1.0
    breadth_bonus = 0.10
    breadth_cap = 5
    cross_me_bonus = 0.15  # Midday+Evening convergence
    cross_combined_bonus = 0.05  # Combined present (mild)
    recency_penalty = 0.08  # per overlapping digit (0..3)
    split_weight = True
    singles_weight = 1.0
    doubles_weight = 0.35
    triples_weight = 0.50

    lanes_by_section: Dict[str, Dict[str, List[Tuple[int, Tuple[str, ...]]]]] = {
        "Combined": {},
        "Midday": {},
        "Evening": {},
    }

    with steps_csv.open("r", encoding="utf-8", errors="replace", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            section = (row.get("section") or "").strip()
            if section not in lanes_by_section:
                continue
            val = "".join(ch for ch in (row.get("value") or "") if ch.isdigit())
            if not val:
                continue
            digits = tuple(sorted(set(val)))
            if not digits:
                continue
            try:
                step = int((row.get("step") or "0").strip() or 0)
            except Exception:
                step = 0
            area = (row.get("area") or "").strip()
            location = (row.get("location") or "").strip()
            method = (row.get("method") or "").strip()
            mode = (row.get("mode") or "").strip()
            lane_key = "|".join(x for x in (area, location, method, mode) if x)
            if not lane_key:
                lane_key = f"lane:{section}"
            lanes_by_section[section].setdefault(lane_key, []).append((step, digits))

    pools_by_section: Dict[str, Dict[Tuple[str, ...], _Dr004PoolAgg]] = {}
    presence: Dict[Tuple[str, ...], set[str]] = {}

    for section, lanes in lanes_by_section.items():
        sec_pools: Dict[Tuple[str, ...], _Dr004PoolAgg] = {}
        for lane_key, entries in lanes.items():
            entries.sort(key=lambda t: t[0])
            dedup: List[Tuple[int, Tuple[str, ...]]] = []
            seen_steps: set[int] = set()
            for step, digits in entries:
                if step in seen_steps:
                    continue
                seen_steps.add(step)
                dedup.append((step, digits))
            if not dedup:
                continue

            prev_digits: Optional[Tuple[str, ...]] = None
            seg_start_step = 0
            seg_len = 0

            def flush() -> None:
                nonlocal prev_digits, seg_start_step, seg_len
                if not prev_digits or seg_len <= 0:
                    return
                if len(prev_digits) < int(min_unique_digits) or len(prev_digits) > int(max_unique_digits):
                    return
                step_w = 1.0 / ((1 + seg_start_step) ** step_power) if step_power else 1.0
                uniq_w = 1.0 / ((len(prev_digits) ** unique_power) if unique_power else 1.0)
                persist_w = (seg_len**persistence_power) if persistence_power else 1.0
                base = step_w * uniq_w * persist_w
                agg = sec_pools.setdefault(prev_digits, _Dr004PoolAgg())
                agg.score_raw += base
                agg.lanes.add(lane_key)
                if agg.earliest_step is None or seg_start_step < agg.earliest_step:
                    agg.earliest_step = seg_start_step
                agg.span_sum += int(seg_len)
                agg.span_max = max(agg.span_max, int(seg_len))
                agg.segments += 1

            for step, digits in dedup:
                if prev_digits is None:
                    prev_digits = digits
                    seg_start_step = step
                    seg_len = 1
                    continue
                if digits == prev_digits:
                    seg_len += 1
                    continue
                flush()
                prev_digits = digits
                seg_start_step = step
                seg_len = 1
            flush()

        pools_by_section[section] = sec_pools
        for digits, agg in sec_pools.items():
            if agg.score_raw > 0:
                presence.setdefault(digits, set()).add(section)

    def cross_bonus(sections_present: set[str]) -> float:
        b = 1.0
        if "Midday" in sections_present and "Evening" in sections_present:
            b *= 1.0 + cross_me_bonus
        if "Combined" in sections_present:
            b *= 1.0 + cross_combined_bonus
        return b

    candidate_cache: Dict[Tuple[str, ...], _DrCandidateSets] = {}
    packs: List[dict] = []

    # Only count DR-004 inputs as Candidate Universe inputs if DR-004 packs are actually emitted.
    signals_inputs: List[Path] = [steps_csv]
    if draws_csv:
        signals_inputs.append(draws_csv)
    inputs: List[Path] = list(signals_inputs) if creating_packs else []

    canon_scores_by_section: Dict[str, Dict[str, float]] = {}
    pool_signals_by_section: Dict[str, List[Dict[str, Any]]] = {}
    selected_boxed_by_section: Dict[str, List[str]] = {}
    selected_index_boxed_by_section: Dict[str, List[str]] = {}

    for section, pools in pools_by_section.items():
        canon_scores: Dict[str, float] = {}
        pool_rows: List[Dict[str, Any]] = []
        for digits, agg in pools.items():
            sections_present = presence.get(digits, set())
            cross_mult = cross_bonus(sections_present)
            score = agg.score_raw * cross_mult
            lane_count = len(agg.lanes)
            breadth_mult = 1.0
            if lane_count > 1:
                breadth_mult = 1.0 + (breadth_bonus * min(lane_count - 1, breadth_cap))
                score *= breadth_mult
            overlap = 0
            recency_mult = 1.0
            if recent_digits:
                overlap = len(set(digits) & recent_digits)
                if overlap > 0:
                    recency_mult = max(0.05, 1.0 - (recency_penalty * overlap))
                    score *= recency_mult

            if signals_out is not None:
                pool_rows.append(
                    {
                        "digits": "".join(digits),
                        "unique_digits": len(digits),
                        "score_raw": round(float(agg.score_raw), 8),
                        "score": round(float(score), 8),
                        "sections_present": sorted(sections_present),
                        "cross_mult": round(float(cross_mult), 6),
                        "lane_count": lane_count,
                        "lanes_sample": sorted(agg.lanes)[:6],
                        "earliest_step": agg.earliest_step,
                        "segments": int(agg.segments),
                        "span_max": int(agg.span_max),
                        "span_sum": int(agg.span_sum),
                        "breadth_mult": round(float(breadth_mult), 6),
                        "recent_digits_n": len(recent_digits),
                        "recent_overlap": int(overlap),
                        "recency_mult": round(float(recency_mult), 6),
                    }
                )

            sets = candidate_cache.get(digits)
            if sets is None:
                sets = _dr_candidate_sets_for_digits(digits)
                candidate_cache[digits] = sets

            if sets.singles:
                w = (score * singles_weight) / len(sets.singles) if split_weight else (score * singles_weight)
                for c in sets.singles:
                    canon = _canon(c)
                    if canon:
                        canon_scores[canon] = canon_scores.get(canon, 0.0) + w
            if sets.doubles:
                w = (score * doubles_weight) / len(sets.doubles) if split_weight else (score * doubles_weight)
                for c in sets.doubles:
                    canon = _canon(c)
                    if canon:
                        canon_scores[canon] = canon_scores.get(canon, 0.0) + w
            if sets.triples:
                w = (score * triples_weight) / len(sets.triples) if split_weight else (score * triples_weight)
                for c in sets.triples:
                    canon = _canon(c)
                    if canon:
                        canon_scores[canon] = canon_scores.get(canon, 0.0) + w

        canon_scores_by_section[section] = canon_scores
        if signals_out is not None:
            pool_rows.sort(key=lambda r: (-float(r["score"]), str(r["digits"])))
            pool_signals_by_section[section] = pool_rows[: max(0, int(signals_top_pools))]

        ranked = sorted(canon_scores.items(), key=lambda kv: (-kv[1], kv[0]))
        if boxed_canonicals > 0 and ranked:
            picked: List[str] = []
            combos: set[str] = set()
            cost = 0
            for canon, _ in ranked:
                if len(picked) >= int(boxed_canonicals):
                    break
                cu = _boxed_cost_units(canon)
                if cu <= 0:
                    continue
                if max_cost_units > 0 and (cost + cu) > int(max_cost_units):
                    continue
                picked.append(canon)
                cost += cu
                combos.update(_unique_perms(canon))

            combos_list = sorted(combos)
            if picked and combos_list:
                selected_boxed_by_section[section] = list(sorted(set(picked)))
                packs.append(
                    {
                        "pack_id": f"digit_reduction_dr004:{section}:top{int(boxed_canonicals)}",
                        "method_id": "digit_reduction_dr004",
                        "variant": section,
                        "play_mode": "BOX",
                        "canonicals": sorted(set(picked)),
                        "combos": combos_list,
                        "combos_count": len(combos_list),
                        "cost_units": len(combos_list),
                        "why_tags": [
                            "digit_reduction",
                            "dr004",
                            "steps_csv",
                            f"boxed_canonicals:{int(boxed_canonicals)}",
                            f"max_cost_units:{int(max_cost_units)}" if max_cost_units else "max_cost_units:off",
                            f"recent_draws:{int(recent_draws)}" if recent_draws else "recent_draws:off",
                            "cross_variant_bonus",
                            "breadth_bonus",
                        ],
                        "transform_chain": [
                            f"dr_steps_csv:{section}",
                            "segment_pools:u<=3",
                            "score:early_arrival+persistence+breadth+cross_variant",
                            "expand:canonicals_from_pools",
                            f"seed_top{int(boxed_canonicals)}",
                            "box_expand_unique_perms",
                        ],
                        "evidence_paths": sorted({_safe_rel(steps_csv), *([_safe_rel(draws_csv)] if draws_csv else [])}),
                    }
                )

    # Optional index-gateway packs: choose at most one canonical per index (bounded).
    if index_boxed_canonicals > 0 and _vtrac_get_index is not None:
        for section, canon_scores in canon_scores_by_section.items():
            if not canon_scores:
                continue
            by_idx: Dict[int, List[Tuple[str, float]]] = {}
            idx_scores: Dict[int, float] = {}
            for canon, s in canon_scores.items():
                idx = _vtrac_get_index(canon)
                if not isinstance(idx, int):
                    continue
                by_idx.setdefault(idx, []).append((canon, s))
                idx_scores[idx] = idx_scores.get(idx, 0.0) + float(s)

            ranked_indices = sorted(idx_scores.items(), key=lambda kv: (-kv[1], kv[0]))
            picked: List[str] = []
            combos: set[str] = set()
            cost = 0
            for idx, _ in ranked_indices:
                if len(picked) >= int(index_boxed_canonicals):
                    break
                members = sorted(by_idx.get(idx, []), key=lambda kv: (-kv[1], kv[0]))
                if not members:
                    continue
                canon = members[0][0]
                cu = _boxed_cost_units(canon)
                if cu <= 0:
                    continue
                if max_cost_units > 0 and (cost + cu) > int(max_cost_units):
                    continue
                picked.append(canon)
                cost += cu
                combos.update(_unique_perms(canon))

            combos_list = sorted(combos)
            if picked and combos_list:
                selected_index_boxed_by_section[section] = list(sorted(set(picked)))
                packs.append(
                    {
                        "pack_id": f"digit_reduction_dr004_index:{section}:top{int(index_boxed_canonicals)}",
                        "method_id": "digit_reduction_dr004_index",
                        "variant": section,
                        "play_mode": "BOX",
                        "canonicals": sorted(set(picked)),
                        "combos": combos_list,
                        "combos_count": len(combos_list),
                        "cost_units": len(combos_list),
                        "why_tags": [
                            "digit_reduction",
                            "dr004",
                            "index_gateway",
                            f"boxed_canonicals:{int(index_boxed_canonicals)}",
                            f"max_cost_units:{int(max_cost_units)}" if max_cost_units else "max_cost_units:off",
                        ],
                        "transform_chain": [
                            f"dr004_scores:{section}",
                            "group_by:vtrac_index",
                            "pick_top_index_members:1_each",
                            "box_expand_unique_perms",
                        ],
                        "evidence_paths": sorted({_safe_rel(steps_csv), *([_safe_rel(draws_csv)] if draws_csv else [])}),
                    }
                )

    if signals_out is not None:
        canon_signals_by_section: Dict[str, List[Dict[str, Any]]] = {}
        index_signals_by_section: Dict[str, List[Dict[str, Any]]] = {}

        top_n_canon = max(0, int(signals_top_canonicals))
        top_n_idx = max(0, int(signals_top_indices))

        for section, canon_scores in canon_scores_by_section.items():
            ranked_canon = sorted(canon_scores.items(), key=lambda kv: (-kv[1], kv[0]))[:top_n_canon]
            canon_signals_by_section[section] = [
                {
                    "canonical": canon,
                    "score": round(float(score), 8),
                    "cost_units": _boxed_cost_units(canon),
                    "vtrac_index": (_vtrac_get_index(canon) if _vtrac_get_index is not None else None),
                }
                for canon, score in ranked_canon
            ]

            if _vtrac_get_index is None or top_n_idx <= 0:
                continue
            by_idx: Dict[int, List[Tuple[str, float]]] = {}
            idx_scores: Dict[int, float] = {}
            for canon, s in canon_scores.items():
                idx = _vtrac_get_index(canon)
                if not isinstance(idx, int):
                    continue
                by_idx.setdefault(idx, []).append((canon, float(s)))
                idx_scores[idx] = idx_scores.get(idx, 0.0) + float(s)

            ranked_indices = sorted(idx_scores.items(), key=lambda kv: (-kv[1], kv[0]))[:top_n_idx]
            idx_rows: List[Dict[str, Any]] = []
            for idx, score in ranked_indices:
                members = sorted(by_idx.get(idx, []), key=lambda kv: (-kv[1], kv[0]))[:5]
                idx_rows.append(
                    {
                        "vtrac_index": int(idx),
                        "score": round(float(score), 8),
                        "top_canonicals": [c for c, _ in members],
                    }
                )
            index_signals_by_section[section] = idx_rows

        signals_out.clear()
        signals_out.update(
            {
                "schema": "dr004_signals_v1",
                "method_id": "digit_reduction_dr004",
                "state_key": state_key,
                "inputs": {
                    "steps_csv": _safe_rel(steps_csv),
                    "draws_csv": _safe_rel(draws_csv) if draws_csv else "",
                    "recent_draws": int(recent_draws),
                    "recent_digits": sorted(recent_digits),
                },
                "config": {
                    "boxed_canonicals": int(boxed_canonicals),
                    "index_boxed_canonicals": int(index_boxed_canonicals),
                    "max_cost_units": int(max_cost_units),
                    "min_unique_digits": int(min_unique_digits),
                    "max_unique_digits": int(max_unique_digits),
                    "signals_top_pools": int(signals_top_pools),
                    "signals_top_canonicals": int(signals_top_canonicals),
                    "signals_top_indices": int(signals_top_indices),
                },
                "sections": {
                    section: {
                        "top_pools": pool_signals_by_section.get(section, []),
                        "top_canonicals": canon_signals_by_section.get(section, []),
                        "top_indices": index_signals_by_section.get(section, []),
                        "selected_boxed_canonicals": selected_boxed_by_section.get(section, []),
                        "selected_index_boxed_canonicals": selected_index_boxed_by_section.get(section, []),
                    }
                    for section in ("Combined", "Midday", "Evening")
                },
            }
        )

    packs.sort(key=lambda p: p.get("pack_id", ""))
    return packs, inputs


def _parse_vtrac_top(*, state_dir: Path, state_key: str, top_n: int = 8) -> Tuple[List[dict], List[Path]]:
    vtrac_dir = state_dir / "vtrac" / state_key
    if not vtrac_dir.exists():
        return [], []
    # Find the single enhanced JSON bundle (timestamped).
    candidates = sorted(vtrac_dir.glob(f"{state_key}_vtrac_enhanced_*.json"))
    if not candidates:
        return [], []
    path = candidates[-1]
    raw = _read_json(path)
    if not isinstance(raw, dict):
        return [], [path]
    ranked = raw.get("straights_ranked")
    if not isinstance(ranked, list):
        return [], [path]

    combos: List[str] = []
    why_tags: List[str] = []
    for entry in ranked:
        if len(combos) >= top_n:
            break
        if not isinstance(entry, dict):
            continue
        s = _normalize_pick3_literal(entry.get("straight") or "")
        if not s:
            continue
        combos.append(s)
        reasons = entry.get("reasons")
        if isinstance(reasons, list):
            why_tags.extend([str(x) for x in reasons if x])

    combos = sorted(set(combos))
    if not combos:
        return [], [path]
    pack = {
        "pack_id": "vtrac_top_straights",
        "method_id": "vtrac_enhanced_top",
        "variant": "Unknown",
        "play_mode": "STRAIGHT",
        "canonicals": sorted({_canon(c) for c in combos if _canon(c)}),
        "combos": combos,
        "combos_count": len(combos),
        "cost_units": len(combos),
        "why_tags": ["vtrac", f"top_n:{top_n}", *sorted(set(why_tags))],
        "transform_chain": [f"vtrac_enhanced:straights_ranked:top{top_n}"],
        "evidence_paths": [_safe_rel(path)],
    }
    return [pack], [path]


def _parse_hot_zones_top(*, state_dir: Path, state_key: str, date: str, top_n: int = 8) -> Tuple[List[dict], List[Path]]:
    hz_dir = state_dir / "hot_zones" / state_key
    if not hz_dir.exists():
        return [], []

    # Prefer winner_map.json (compact triad list), fall back to top lanes CSV.
    wm = hz_dir / f"{date}_hot_zones_winner_map.json"
    inputs: List[Path] = []
    combos: List[str] = []
    why_tags: List[str] = []
    if wm.exists():
        inputs.append(wm)
        raw = _read_json(wm)
        if isinstance(raw, list):
            # Sort by score_mean desc, then triad.
            def key_fn(r: Any) -> Tuple[float, str]:
                if not isinstance(r, dict):
                    return (float("-inf"), "")
                triad = _normalize_pick3_literal(r.get("triad") or "")
                try:
                    score = float(r.get("score_mean") or 0.0)
                except Exception:
                    score = 0.0
                return (score, triad)

            ordered = sorted(raw, key=key_fn, reverse=True)
            for r in ordered:
                if len(combos) >= top_n:
                    break
                if not isinstance(r, dict):
                    continue
                triad = _normalize_pick3_literal(r.get("triad") or "")
                if not triad:
                    continue
                combos.append(triad)
                tags = (r.get("evidence_tags") or "").strip()
                if tags:
                    why_tags.extend([t for t in tags.split(",") if t])
    else:
        top_csv = hz_dir / f"{state_key}_hot_zones_top_lanes.csv"
        if top_csv.exists():
            inputs.append(top_csv)
            rows = _load_csv_dict_rows(top_csv)
            # columns vary; try to find triad key
            for r in rows:
                if len(combos) >= top_n:
                    break
                triad = _normalize_pick3_literal(r.get("triad") or r.get("Triad") or "")
                if not triad:
                    continue
                combos.append(triad)

    combos = sorted(set(combos))
    if not combos:
        return [], inputs

    pack = {
        "pack_id": "hot_zones_top_triads",
        "method_id": "hot_zones_top",
        "variant": "Unknown",
        "play_mode": "STRAIGHT",
        "canonicals": sorted({_canon(c) for c in combos if _canon(c)}),
        "combos": combos,
        "combos_count": len(combos),
        "cost_units": len(combos),
        "why_tags": ["hot_zones", f"top_n:{top_n}", *sorted(set(why_tags))],
        "transform_chain": [f"hot_zones:top_triads:top{top_n}"],
        "evidence_paths": [_safe_rel(p) for p in inputs],
    }
    return [pack], inputs


def _parse_hot_zones_index_closure(
    *,
    state_dir: Path,
    state_key: str,
    date: str,
    seed_top_n: int,
    top_box_canonicals: int,
) -> Tuple[List[dict], List[Path]]:
    """
    Optional Hot Zones "index-hit → box-hit" conversion helper.

    Idea:
    - Hot Zones often has a meaningful VTRAC index signal even when it misses the exact winner canonical.
    - Under tight budgets, closing an entire index is too expensive (often 24–48 straight lines).
    - This pack instead:
        1) votes a *dominant* VTRAC index from the top Hot Zones triads
        2) box-expands a small number of seed canonicals within that index (bounded).

    This is intentionally:
    - additive (does not remove/replace Hot Zones top triads),
    - bounded (default ~12 lines),
    - selection-layer (derived from tool evidence; no analyzer changes).
    """
    if seed_top_n <= 0 or top_box_canonicals <= 0:
        return [], []
    if not _vtrac_get_index:
        return [], []

    hz_dir = state_dir / "hot_zones" / state_key
    if not hz_dir.exists():
        return [], []

    inputs: List[Path] = []
    ordered: List[Tuple[str, float]] = []

    # Prefer winner_map.json (compact triad list + evidence tags), fall back to top lanes CSV.
    wm = hz_dir / f"{date}_hot_zones_winner_map.json"
    if wm.exists():
        inputs.append(wm)
        raw = _read_json(wm)
        if isinstance(raw, list):
            for r in raw:
                if not isinstance(r, dict):
                    continue
                triad = _normalize_pick3_literal(r.get("triad") or "")
                if not triad:
                    continue
                try:
                    score = float(r.get("score_mean") or 0.0)
                except Exception:
                    score = 0.0
                ordered.append((triad, score))
            ordered.sort(key=lambda t: (-t[1], t[0]))
    else:
        top_csv = hz_dir / f"{state_key}_hot_zones_top_lanes.csv"
        if top_csv.exists():
            inputs.append(top_csv)
            rows = _load_csv_dict_rows(top_csv)
            for r in rows:
                triad = _normalize_pick3_literal(r.get("triad") or r.get("Triad") or "")
                if not triad:
                    continue
                # tolerate different column names
                score_val = r.get("score_mean") or r.get("score_max") or r.get("ScoreMean") or r.get("ScoreMax") or 0.0
                try:
                    score = float(score_val or 0.0)
                except Exception:
                    score = 0.0
                ordered.append((triad, score))
            ordered.sort(key=lambda t: (-t[1], t[0]))

    seed = ordered[:seed_top_n]
    if not seed:
        return [], inputs

    # Vote a dominant index from the seed triads (count first, then score sum).
    idx_count: Dict[int, int] = {}
    idx_score: Dict[int, float] = {}
    for triad, score in seed:
        idx = _vtrac_get_index(triad)
        if idx is None:
            continue
        idx_count[idx] = idx_count.get(idx, 0) + 1
        idx_score[idx] = idx_score.get(idx, 0.0) + float(score or 0.0)
    if not idx_count:
        return [], inputs

    best_idx = sorted(idx_count.keys(), key=lambda i: (-idx_count[i], -idx_score.get(i, 0.0), i))[0]

    # Choose a small number of seed canonicals within that index, then BOX-expand.
    canonicals: List[str] = []
    for triad, _ in seed:
        idx = _vtrac_get_index(triad)
        if idx != best_idx:
            continue
        canon = _canon(triad)
        if not canon or canon in canonicals:
            continue
        canonicals.append(canon)
        if len(canonicals) >= top_box_canonicals:
            break
    if not canonicals:
        return [], inputs

    combos: List[str] = []
    for canon in canonicals:
        combos.extend(_unique_perms(canon))
    combos = sorted(set(combos))
    if not combos:
        return [], inputs

    pack = {
        "pack_id": f"hot_zones_index_closure:idx={best_idx}:top_box={len(canonicals)}:seed_top={seed_top_n}",
        "method_id": "hot_zones_index_closure",
        "variant": "Unknown",
        "play_mode": "STRAIGHT",
        "canonicals": sorted(set(canonicals)),
        "combos": combos,
        "combos_count": len(combos),
        "cost_units": len(combos),
        "why_tags": [
            "hot_zones",
            "index_closure",
            f"idx:{best_idx}",
            f"seed_top_n:{seed_top_n}",
            f"top_box_canonicals:{len(canonicals)}",
        ],
        "transform_chain": [
            f"hot_zones:top_triads:top{seed_top_n}",
            f"vtrac_index_vote:idx={best_idx}",
            f"box_expand:top{len(canonicals)}",
        ],
        "evidence_paths": [_safe_rel(p) for p in inputs],
    }
    return [pack], inputs


def _parse_aux_top(*, state_dir: Path, state_key: str, top_n: int = 10) -> Tuple[List[dict], List[Path]]:
    aux_path = state_dir / "aux" / state_key / "summary.json"
    if not aux_path.exists():
        return [], []
    raw = _read_json(aux_path)
    if not isinstance(raw, dict):
        return [], [aux_path]
    positional = raw.get("positional") or {}
    if not isinstance(positional, dict):
        return [], [aux_path]
    shortlist = positional.get("shortlist_report") or {}
    if not isinstance(shortlist, dict):
        return [], [aux_path]
    candidates = shortlist.get("candidates") or []
    if not isinstance(candidates, list):
        return [], [aux_path]

    combos: List[str] = []
    why: List[str] = []
    for entry in candidates[:top_n]:
        if not isinstance(entry, dict):
            continue
        combo = _normalize_pick3_literal(entry.get("combo") or "")
        if not combo:
            continue
        combos.append(combo)
        tags = entry.get("tags")
        if isinstance(tags, list):
            why.extend([str(t) for t in tags if t])

    combos = sorted(set(combos))
    if not combos:
        return [], [aux_path]
    pack = {
        "pack_id": "aux_positional_shortlist",
        "method_id": "aux_positional",
        "variant": "Unknown",
        "play_mode": "STRAIGHT",
        "canonicals": sorted({_canon(c) for c in combos if _canon(c)}),
        "combos": combos,
        "combos_count": len(combos),
        "cost_units": len(combos),
        "why_tags": ["aux", f"top_n:{top_n}", *sorted(set(why))],
        "transform_chain": [f"aux_positional_shortlist:top{top_n}"],
        "evidence_paths": [_safe_rel(aux_path)],
    }
    return [pack], [aux_path]


def _parse_aux_vtrac_indices(*, state_dir: Path, state_key: str, top_n: int = 2) -> Tuple[List[dict], List[Path]]:
    """
    Parse Aux VTRAC overdue overlays into explicit index-closure packs.

    This answers the common “index-level” Aux question:
    - Which boxed VTRAC indices are most overdue (per variant)?
    - What is the full index closure universe (48 combos) for each?

    Output packs are STRAIGHT lists (explicit combos) so cost is measurable.
    """
    if top_n <= 0:
        return [], []
    if not _vtrac_get_index_set:
        return [], []

    aux_path = state_dir / "aux" / state_key / "summary.json"
    if not aux_path.exists():
        return [], []
    raw = _read_json(aux_path)
    if not isinstance(raw, dict):
        return [], [aux_path]
    vtrac = raw.get("vtrac") or {}
    if not isinstance(vtrac, dict):
        return [], [aux_path]
    overlay_top = vtrac.get("overlay_top") or {}
    if not isinstance(overlay_top, dict):
        return [], [aux_path]

    packs: List[dict] = []
    for variant, rows in overlay_top.items():
        if not isinstance(rows, list):
            continue
        picked = rows[: int(top_n)]
        for r in picked:
            if not isinstance(r, dict):
                continue
            try:
                idx = int(r.get("index"))  # type: ignore[arg-type]
            except Exception:
                continue
            try:
                ds = int(r.get("draws_since") or 0)
            except Exception:
                ds = 0
            try:
                combos = sorted({_normalize_pick3_literal(x) for x in _vtrac_get_index_set(idx) if _normalize_pick3_literal(x)})
            except Exception:
                combos = []
            if not combos:
                continue
            canonicals = sorted({_canon(c) for c in combos if _canon(c)})
            packs.append(
                {
                    "pack_id": f"aux_vtrac_index_overdue:{_variant_title(variant)}:idx={idx}",
                    "method_id": "aux_vtrac_index_overdue",
                    "variant": _variant_title(variant),
                    "play_mode": "STRAIGHT",
                    "canonicals": canonicals,
                    "combos": combos,
                    "combos_count": len(combos),
                    "cost_units": len(combos),
                    "why_tags": ["aux", "vtrac_overlay", "overdue_index", f"idx:{idx}", f"ds:{ds}", f"top_n:{int(top_n)}"],
                    "transform_chain": [
                        f"aux_summary:vtrac_overlay_top:{_variant_title(variant)}:top{int(top_n)}",
                        f"vtrac_index_set:{idx}",
                    ],
                    "evidence_paths": [_safe_rel(aux_path)],
                }
            )

    packs.sort(key=lambda p: p.get("pack_id", ""))
    return packs, [aux_path]


def _parse_blackapple_alert_packs(
    *,
    state_dir: Path,
    state_key: str,
    top_n: int,
    min_score: int,
) -> Tuple[List[dict], List[Path]]:
    """
    Parse Blackapple candidates from Aux `summary.json` into bounded STRAIGHT packs.

    Design:
    - Default-off (controlled by CLI flags).
    - ALERT-only by default (`min_score=3`), to avoid widening Candidate Universe on OFF/WATCH days.
    - Uses sharepack-local Aux summary (draws-only; predictive-safe).
    """
    if int(top_n) <= 0:
        return [], []
    aux_path = state_dir / "aux" / state_key / "summary.json"
    if not aux_path.exists():
        return [], []
    raw = _read_json(aux_path)
    if not isinstance(raw, dict):
        return [], [aux_path]
    ba = raw.get("blackapple") or {}
    if not isinstance(ba, dict):
        return [], [aux_path]
    by_variant = ba.get("by_variant") or {}
    if not isinstance(by_variant, dict):
        return [], [aux_path]

    packs: List[dict] = []
    for variant_key, analysis in by_variant.items():
        if not isinstance(analysis, dict):
            continue
        try:
            score = int(analysis.get("score") or 0)
        except Exception:
            score = 0
        if score < int(min_score):
            continue
        candidates = analysis.get("candidates") or []
        if not isinstance(candidates, list):
            continue
        combos: List[str] = []
        why: List[str] = []
        triggers = analysis.get("triggers") or {}
        if isinstance(triggers, dict):
            # Keep this intentionally shallow (avoid exploding tag space).
            if triggers.get("mirror"):
                why.append("mirror")
            if triggers.get("root_due"):
                why.append("root_due")
            if triggers.get("floating"):
                why.append("floating")
            if triggers.get("pattern"):
                why.append("pattern")
            if triggers.get("pairs"):
                why.append("pairs")

        for entry in candidates[: int(top_n)]:
            if not isinstance(entry, dict):
                continue
            combo = _normalize_pick3_literal(entry.get("combo") or "")
            if combo:
                combos.append(combo)
        combos = sorted(set(combos))
        if not combos:
            continue

        variant_title = _variant_title(str(variant_key))
        packs.append(
            {
                "pack_id": f"blackapple:{variant_title}:score>={int(min_score)}:top{int(top_n)}",
                "method_id": "blackapple",
                "variant": variant_title,
                "play_mode": "STRAIGHT",
                "canonicals": sorted({_canon(c) for c in combos if _canon(c)}),
                "combos": combos,
                "combos_count": len(combos),
                "cost_units": len(combos),
                "why_tags": ["blackapple", f"score:{score}", f"min_score:{int(min_score)}", f"top_n:{int(top_n)}", *sorted(set(why))],
                "transform_chain": [f"blackapple:{variant_title}:score>={int(min_score)}:top{int(top_n)}"],
                "evidence_paths": [_safe_rel(aux_path)],
            }
        )

    packs.sort(key=lambda p: p.get("pack_id", ""))
    return packs, [aux_path]


def _extract_stable_signals(*, state_dir: Path, state_key: str, top_n: int) -> Tuple[Dict[str, Any], List[Path]]:
    if top_n <= 0:
        return {"available": False, "sections": {}}, []
    stable_scores = state_dir / "stable" / state_key / f"{state_key}_stable_patterns_scores.csv"
    if not stable_scores.exists():
        return {"available": False, "sections": {}}, []

    rows = _load_csv_dict_rows(stable_scores)
    if not rows:
        return {"available": False, "sections": {}}, [stable_scores]

    best: Dict[Tuple[str, str], Tuple[float, str]] = {}
    for r in rows:
        section = (r.get("section") or "").strip() or "Unknown"
        canon = _normalize_pick3_literal(r.get("Canonical") or "")
        if canon:
            canon = canon.zfill(3)
        else:
            canon = _normalize_pick3_literal(str(r.get("Canonical") or ""))
        if not canon:
            continue
        score_raw = (r.get("score") or "").strip()
        try:
            score = float(score_raw)
        except Exception:
            continue
        why = (r.get("why") or "").strip()
        key = (section, canon)
        prev = best.get(key)
        if prev is None or score > prev[0]:
            best[key] = (score, why)

    sections: Dict[str, List[Dict[str, Any]]] = {}
    for section in sorted({s for s, _ in best.keys()}):
        ranked: List[Tuple[str, float, str]] = []
        for (sec, canon), (score, why) in best.items():
            if sec != section:
                continue
            ranked.append((canon, float(score), str(why or "")))
        ranked.sort(key=lambda t: (-t[1], t[0]))
        sections[section] = [
            {
                "canonical": canon,
                "vtrac_index": (_vtrac_get_index(canon) if _vtrac_get_index is not None else None),
                "score": score,
                "why": why,
            }
            for canon, score, why in ranked[:top_n]
        ]

    return {"available": True, "evidence_paths": [_safe_rel(stable_scores)], "sections": sections}, [stable_scores]


def _extract_hot_zones_signals(
    *,
    state_dir: Path,
    state_key: str,
    date: str,
    top_n: int,
) -> Tuple[Dict[str, Any], List[Path]]:
    if top_n <= 0:
        return {"available": False, "triads": []}, []
    hz_dir = state_dir / "hot_zones" / state_key
    if not hz_dir.exists():
        return {"available": False, "triads": []}, []

    wm = hz_dir / f"{date}_hot_zones_winner_map.json"
    inputs: List[Path] = []
    triads: List[Dict[str, Any]] = []

    if wm.exists():
        inputs.append(wm)
        raw = _read_json(wm)
        if isinstance(raw, list):
            ordered: List[Dict[str, Any]] = []
            for r in raw:
                if not isinstance(r, dict):
                    continue
                triad = _normalize_pick3_literal(r.get("triad") or "")
                if not triad:
                    continue
                try:
                    score_mean = float(r.get("score_mean") or 0.0)
                except Exception:
                    score_mean = 0.0
                ordered.append({"triad": triad, "row": r, "score_mean": score_mean})
            ordered.sort(key=lambda x: (-x["score_mean"], x["triad"]))
            for it in ordered[:top_n]:
                r = it["row"]
                triad = it["triad"]
                canon = _canon(triad)
                score_max_val = None
                score_max_raw = str(r.get("score_max") or "").strip()
                if score_max_raw:
                    try:
                        score_max_val = float(score_max_raw)
                    except Exception:
                        score_max_val = None
                support_count_val = None
                support_count_raw = str(r.get("support_count") or "").strip()
                if support_count_raw:
                    try:
                        support_count_val = int(float(support_count_raw))
                    except Exception:
                        support_count_val = None
                triads.append(
                    {
                        "triad": triad,
                        "canonical": canon,
                        "vtrac_index": (_vtrac_get_index(triad) if _vtrac_get_index is not None else None),
                        "vt_triad": (str(r.get("vt_triad") or "").strip() or None),
                        "score_mean": float(it["score_mean"]),
                        "score_max": score_max_val,
                        "evidence_tags": (str(r.get("evidence_tags") or "").strip() or None),
                        "support_count": support_count_val,
                    }
                )
    else:
        top_csv = hz_dir / f"{state_key}_hot_zones_top_lanes.csv"
        if top_csv.exists():
            inputs.append(top_csv)
            rows = _load_csv_dict_rows(top_csv)
            for r in rows:
                if len(triads) >= top_n:
                    break
                triad = _normalize_pick3_literal(r.get("triad") or r.get("Triad") or "")
                if not triad:
                    continue
                score_val = r.get("score_mean") or r.get("score_max") or r.get("ScoreMean") or r.get("ScoreMax") or 0.0
                try:
                    score_mean = float(score_val or 0.0)
                except Exception:
                    score_mean = 0.0
                canon = _canon(triad)
                triads.append(
                    {
                        "triad": triad,
                        "canonical": canon,
                        "vtrac_index": (_vtrac_get_index(triad) if _vtrac_get_index is not None else None),
                        "vt_triad": (str(r.get("vt_triad") or "").strip() or None),
                        "score_mean": score_mean,
                        "score_max": None,
                        "evidence_tags": None,
                        "support_count": None,
                    }
                )

    triads.sort(key=lambda t: (-(t.get("score_mean") or 0.0), str(t.get("triad") or "")))
    return (
        {"available": bool(triads), "evidence_paths": [_safe_rel(p) for p in inputs], "triads": triads[:top_n]},
        inputs,
    )


def _extract_vtrac_enhanced_signals(
    *,
    state_dir: Path,
    state_key: str,
    top_indices: int,
    top_straights: int,
) -> Tuple[Dict[str, Any], List[Path]]:
    vtrac_dir = state_dir / "vtrac" / state_key
    if not vtrac_dir.exists():
        return {"available": False, "top_indices": [], "top_straights": []}, []
    candidates = sorted(vtrac_dir.glob(f"{state_key}_vtrac_enhanced_*.json"))
    if not candidates:
        return {"available": False, "top_indices": [], "top_straights": []}, []
    path = candidates[-1]
    raw = _read_json(path)
    if not isinstance(raw, dict):
        return {"available": False, "top_indices": [], "top_straights": []}, [path]

    indices: List[Dict[str, Any]] = []
    if top_indices > 0:
        ranked = raw.get("indices_ranked")
        if isinstance(ranked, list):
            for r in ranked:
                if len(indices) >= int(top_indices):
                    break
                if not isinstance(r, dict):
                    continue
                try:
                    idx = int(r.get("index"))
                except Exception:
                    continue
                try:
                    score = float(r.get("score") or 0.0)
                except Exception:
                    score = 0.0
                indices.append({"index": idx, "score": score})
            indices.sort(key=lambda x: (-float(x.get("score") or 0.0), int(x.get("index") or 0)))

    straights: List[Dict[str, Any]] = []
    if top_straights > 0:
        ranked = raw.get("straights_ranked")
        if isinstance(ranked, list):
            for r in ranked:
                if len(straights) >= int(top_straights):
                    break
                if not isinstance(r, dict):
                    continue
                straight = _normalize_pick3_literal(r.get("straight") or "")
                if not straight:
                    continue
                try:
                    score = float(r.get("score") or 0.0)
                except Exception:
                    score = 0.0
                reasons = r.get("reasons")
                straights.append(
                    {
                        "straight": straight,
                        "canonical": _canon(straight),
                        "index": (int(r.get("index")) if str(r.get("index") or "").strip() else None),
                        "score": score,
                        "reasons": ([str(x) for x in reasons if x] if isinstance(reasons, list) else []),
                    }
                )
            straights.sort(key=lambda x: (-float(x.get("score") or 0.0), str(x.get("straight") or "")))

    return (
        {
            "available": bool(indices or straights),
            "evidence_paths": [_safe_rel(path)],
            "top_indices": indices[: int(top_indices)] if top_indices > 0 else [],
            "top_straights": straights[: int(top_straights)] if top_straights > 0 else [],
        },
        [path],
    )


def _extract_aux_signals(*, state_dir: Path, state_key: str, top_shortlist: int, top_overdue: int) -> Tuple[Dict[str, Any], List[Path]]:
    aux_path = state_dir / "aux" / state_key / "summary.json"
    if not aux_path.exists():
        return {"available": False, "positional_shortlist": [], "vtrac_overlay_top": {}}, []
    raw = _read_json(aux_path)
    if not isinstance(raw, dict):
        return {"available": False, "positional_shortlist": [], "vtrac_overlay_top": {}}, [aux_path]

    positional_shortlist: List[Dict[str, Any]] = []
    if top_shortlist > 0:
        candidates = (((raw.get("positional") or {}).get("shortlist_report") or {}).get("candidates") or [])
        if isinstance(candidates, list):
            ordered: List[Dict[str, Any]] = []
            for r in candidates:
                if not isinstance(r, dict):
                    continue
                combo = _normalize_pick3_literal(r.get("combo") or "")
                if not combo:
                    continue
                try:
                    score = float(r.get("score") or 0.0)
                except Exception:
                    score = 0.0
                ordered.append({"combo": combo, "score": score, "tags": r.get("tags"), "source": r.get("source")})
            ordered.sort(key=lambda x: (-float(x.get("score") or 0.0), str(x.get("combo") or "")))
            for r in ordered[: int(top_shortlist)]:
                tags = r.get("tags")
                positional_shortlist.append(
                    {
                        "combo": r.get("combo"),
                        "canonical": _canon(str(r.get("combo") or "")),
                        "vtrac_index": (_vtrac_get_index(str(r.get("combo") or "")) if _vtrac_get_index is not None else None),
                        "score": float(r.get("score") or 0.0),
                        "tags": ([str(t) for t in tags if t] if isinstance(tags, list) else []),
                        "source": (str(r.get("source") or "").strip() or None),
                    }
                )

    overlay_top = ((raw.get("vtrac") or {}).get("overlay_top") or {})
    vtrac_overlay_top: Dict[str, List[Dict[str, Any]]] = {}
    if top_overdue > 0 and isinstance(overlay_top, dict):
        for variant, rows in overlay_top.items():
            if not isinstance(rows, list):
                continue
            picked: List[Dict[str, Any]] = []
            for r in rows[: int(top_overdue)]:
                if not isinstance(r, dict):
                    continue
                try:
                    idx = int(r.get("index"))
                except Exception:
                    continue
                try:
                    ds = int(r.get("draws_since") or 0)
                except Exception:
                    ds = 0
                picked.append({"index": idx, "draws_since": ds})
            if picked:
                picked.sort(key=lambda x: (-int(x.get("draws_since") or 0), int(x.get("index") or 0)))
                vtrac_overlay_top[str(variant)] = picked

    return (
        {
            "available": bool(positional_shortlist or vtrac_overlay_top),
            "evidence_paths": [_safe_rel(aux_path)],
            "positional_shortlist": positional_shortlist,
            "vtrac_overlay_top": vtrac_overlay_top,
        },
        [aux_path],
    )


def _extract_aux_badge_pressure_signals(
    *,
    state_dir: Path,
    state_key: str,
    top_k: int = 5,
) -> Tuple[Dict[str, Any], List[Path]]:
    """
    Predictive-safe signals export: derive a compact "index pressure" surface from Aux draw snapshots.

    This mirrors the intent of the RUNS badge-matrix export, but produces only the top-K indices per variant
    (and the Midday∩Evening intersection) so the signal can be consumed without exploding artifacts.
    """
    if top_k <= 0:
        return {"available": False, "by_variant": {}, "midday_evening_intersection": []}, []
    draws_dir = state_dir / "aux" / "draws"
    if not draws_dir.exists():
        return {"available": False, "by_variant": {}, "midday_evening_intersection": []}, []

    try:
        from modules.analyze_pairs import get_vtrac_statuses  # type: ignore
        from modules.vtrac_reference import VTRAC_DISPLAY  # type: ignore
    except Exception:
        return {"available": False, "by_variant": {}, "midday_evening_intersection": []}, []

    def _color_weight(color: str) -> int:
        c = (color or "").strip().lower()
        if c == "red":
            return 3
        if c == "blue":
            return 2
        if c == "purple":
            return 1
        return 0

    def _shape_weight(status: dict) -> int:
        if status.get("shape_red_circle"):
            return 2
        if status.get("shape_blue_square"):
            return 1
        return 0

    by_variant: Dict[str, Any] = {}
    inputs: List[Path] = []

    for variant in ("combined", "midday", "evening"):
        p = _find_sharepack_draws_csv_for_variant(state_dir=state_dir, state_key=state_key, variant=variant)
        if not p:
            continue
        draws = _read_draws_list(draws_csv=p, max_n=1000)
        if not draws:
            continue
        inputs.append(p)
        with redirect_stdout(StringIO()):
            vstat = get_vtrac_statuses(draws[:100], draws[:1000])
        if not isinstance(vstat, dict):
            continue

        ranked: List[Tuple[int, float, int]] = []
        for entry in VTRAC_DISPLAY:
            try:
                idx = int(entry.get("Index"))
            except Exception:
                continue
            payload = vstat.get(idx, {})
            if not isinstance(payload, dict):
                continue
            singles_status = payload.get("singles_status") if isinstance(payload.get("singles_status"), dict) else {}
            doubles_status = payload.get("doubles_status") if isinstance(payload.get("doubles_status"), dict) else {}
            singles = str(entry.get("Singles") or "").split()
            doubles = str(entry.get("Doubles") or "").split()
            canon_count = len(singles) + len(doubles)
            raw_score = 0
            for combo in singles:
                st = singles_status.get(combo, {}) if isinstance(singles_status, dict) else {}
                if not isinstance(st, dict):
                    continue
                raw_score += _color_weight(str(st.get("color") or "")) + _shape_weight(st)
            for combo in doubles:
                st = doubles_status.get(combo, {}) if isinstance(doubles_status, dict) else {}
                if not isinstance(st, dict):
                    continue
                raw_score += _color_weight(str(st.get("color") or "")) + _shape_weight(st)
            density = (raw_score / canon_count) if canon_count else 0.0
            ranked.append((idx, density, raw_score))

        ranked.sort(key=lambda t: (t[1], t[2], -t[0]), reverse=True)
        top = [{"index": idx, "pressure_density": round(dens, 6), "pressure_raw": raw} for idx, dens, raw in ranked[: int(top_k)]]
        by_variant[variant] = {
            "top_k": int(top_k),
            "rank_by": "pressure_density",
            "weights": {"color": {"red": 3, "blue": 2, "purple": 1}, "shape": {"RC": 2, "BS": 1}},
            "top_indices": top,
        }

    midday = {int(r.get("index")) for r in (by_variant.get("midday") or {}).get("top_indices", []) if isinstance(r, dict) and str(r.get("index", "")).isdigit()}
    evening = {int(r.get("index")) for r in (by_variant.get("evening") or {}).get("top_indices", []) if isinstance(r, dict) and str(r.get("index", "")).isdigit()}
    intersection = sorted(midday.intersection(evening))

    return (
        {
            "available": bool(by_variant),
            "evidence_paths": [_safe_rel(p) for p in inputs],
            "by_variant": by_variant,
            "midday_evening_intersection": intersection,
        },
        inputs,
    )


def _build_fusion_gate_dr004_packs(
    *,
    state_key: str,
    dr004_signals: Dict[str, Any],
    stable_signals: Dict[str, Any],
    hot_zones_signals: Dict[str, Any],
    vtrac_signals: Dict[str, Any],
    aux_signals: Dict[str, Any],
    boxed_canonicals: int,
    min_sources: int,
) -> List[dict]:
    """
    Build small BOX packs when DR-004 index signals converge with other tool signals.

    This is a selection-layer helper only (default-off):
    - It does NOT replace DR-004 signals export.
    - It does NOT widen the universe aggressively (small N canonicals per section).
    - It prefers cross-tool overlap at the VTRAC index level.
    """
    if boxed_canonicals <= 0 or min_sources <= 1:
        return []
    if not _vtrac_get_index:
        return []

    sections = dr004_signals.get("sections") if isinstance(dr004_signals, dict) else None
    if not isinstance(sections, dict):
        return []

    # Normalize inputs (safe_rel strings only).
    evidence_paths: List[str] = []
    for key in ("inputs", "evidence_paths"):
        items = dr004_signals.get(key) if isinstance(dr004_signals, dict) else None
        if isinstance(items, list):
            evidence_paths.extend([str(x) for x in items if str(x)])
    for sig in (stable_signals, hot_zones_signals, vtrac_signals, aux_signals):
        items = sig.get("evidence_paths") if isinstance(sig, dict) else None
        if isinstance(items, list):
            evidence_paths.extend([str(x) for x in items if str(x)])
    evidence_paths = sorted(set(evidence_paths))

    stable_sections = stable_signals.get("sections") if isinstance(stable_signals, dict) else {}
    hot_triads = hot_zones_signals.get("triads") if isinstance(hot_zones_signals, dict) else []
    vt_top_indices = vtrac_signals.get("top_indices") if isinstance(vtrac_signals, dict) else []
    vt_top_straights = vtrac_signals.get("top_straights") if isinstance(vtrac_signals, dict) else []
    aux_overlay = aux_signals.get("vtrac_overlay_top") if isinstance(aux_signals, dict) else {}

    vtrac_index_scores: Dict[int, float] = {}
    if isinstance(vt_top_indices, list):
        for r in vt_top_indices:
            if not isinstance(r, dict):
                continue
            try:
                idx = int(r.get("index"))
            except Exception:
                continue
            try:
                score = float(r.get("score") or 0.0)
            except Exception:
                score = 0.0
            vtrac_index_scores[idx] = max(vtrac_index_scores.get(idx, float("-inf")), score)

    packs: List[dict] = []
    for section in ("Combined", "Midday", "Evening"):
        sec = sections.get(section)
        if not isinstance(sec, dict):
            continue

        dr_top_indices = sec.get("top_indices") or []
        if not isinstance(dr_top_indices, list) or not dr_top_indices:
            continue

        dr_index_scores: Dict[int, float] = {}
        for r in dr_top_indices:
            if not isinstance(r, dict):
                continue
            try:
                idx = int(r.get("vtrac_index"))
            except Exception:
                continue
            try:
                score = float(r.get("score") or 0.0)
            except Exception:
                score = 0.0
            dr_index_scores[idx] = max(dr_index_scores.get(idx, float("-inf")), score)

        sources_by_index: Dict[int, set[str]] = {}

        def add_source(idx: Optional[int], source: str) -> None:
            if idx is None:
                return
            try:
                idx_int = int(idx)
            except Exception:
                return
            sources_by_index.setdefault(idx_int, set()).add(source)

        for idx in dr_index_scores:
            add_source(idx, "dr004")

        # Stable section votes (canonical -> index).
        if isinstance(stable_sections, dict):
            for r in stable_sections.get(section, []) if isinstance(stable_sections.get(section), list) else []:
                if not isinstance(r, dict):
                    continue
                try:
                    idx = int(r.get("vtrac_index")) if r.get("vtrac_index") is not None else None
                except Exception:
                    idx = None
                add_source(idx, "stable")

        # Hot Zones votes (variant-agnostic).
        if isinstance(hot_triads, list):
            for r in hot_triads:
                if not isinstance(r, dict):
                    continue
                try:
                    idx = int(r.get("vtrac_index")) if r.get("vtrac_index") is not None else None
                except Exception:
                    idx = None
                add_source(idx, "hot_zones")

        # VTRAC enhanced votes.
        if isinstance(vt_top_indices, list):
            for r in vt_top_indices:
                if not isinstance(r, dict):
                    continue
                try:
                    idx = int(r.get("index"))
                except Exception:
                    continue
                add_source(idx, "vtrac_enhanced")
        if isinstance(vt_top_straights, list):
            for r in vt_top_straights:
                if not isinstance(r, dict):
                    continue
                idx = r.get("index")
                add_source(idx if idx is not None else None, "vtrac_enhanced")

        # Aux overdue overlay votes (variant-matched).
        aux_variant = section.lower()
        if aux_variant == "combined":
            aux_variant = "combined"
        if isinstance(aux_overlay, dict) and isinstance(aux_overlay.get(aux_variant), list):
            for r in aux_overlay.get(aux_variant)[:]:
                if not isinstance(r, dict):
                    continue
                try:
                    idx = int(r.get("index"))
                except Exception:
                    continue
                add_source(idx, "aux_overdue")

        # Find convergent indices (must include DR-004).
        fused: List[Tuple[int, set[str]]] = []
        for idx, srcs in sources_by_index.items():
            if "dr004" not in srcs:
                continue
            if len(srcs) < int(min_sources):
                continue
            fused.append((idx, srcs))
        if not fused:
            continue

        fused.sort(
            key=lambda t: (
                -len(t[1]),
                -float(dr_index_scores.get(t[0], 0.0) or 0.0),
                -float(vtrac_index_scores.get(t[0], 0.0) or 0.0),
                t[0],
            )
        )
        best_idx, best_srcs = fused[0]

        # Collect canonical votes within the best index.
        dr_top_canon_rows = sec.get("top_canonicals") or []
        dr_canon_score: Dict[str, float] = {}
        dr_canon_set: set[str] = set()
        if isinstance(dr_top_canon_rows, list):
            for r in dr_top_canon_rows:
                if not isinstance(r, dict):
                    continue
                canon = _canon(r.get("canonical") or "")
                if not canon:
                    continue
                dr_canon_set.add(canon)
                try:
                    dr_canon_score[canon] = float(r.get("score") or 0.0)
                except Exception:
                    dr_canon_score[canon] = 0.0

        stable_canon_set: set[str] = set()
        if isinstance(stable_sections, dict) and isinstance(stable_sections.get(section), list):
            for r in stable_sections.get(section, []):
                if not isinstance(r, dict):
                    continue
                canon = _canon(r.get("canonical") or "")
                if canon:
                    stable_canon_set.add(canon)

        hot_canon_set: set[str] = set()
        if isinstance(hot_triads, list):
            for r in hot_triads:
                if not isinstance(r, dict):
                    continue
                canon = _canon(r.get("canonical") or r.get("triad") or "")
                if canon:
                    hot_canon_set.add(canon)

        vt_canon_set: set[str] = set()
        if isinstance(vt_top_straights, list):
            for r in vt_top_straights:
                if not isinstance(r, dict):
                    continue
                canon = _canon(r.get("canonical") or r.get("straight") or "")
                if canon:
                    vt_canon_set.add(canon)

        aux_canon_set: set[str] = set()
        aux_shortlist = aux_signals.get("positional_shortlist") if isinstance(aux_signals, dict) else []
        if isinstance(aux_shortlist, list):
            for r in aux_shortlist:
                if not isinstance(r, dict):
                    continue
                canon = _canon(r.get("canonical") or r.get("combo") or "")
                if canon:
                    aux_canon_set.add(canon)

        union_canons = sorted(set().union(dr_canon_set, stable_canon_set, hot_canon_set, vt_canon_set, aux_canon_set))
        scored: List[Tuple[int, float, int, str]] = []
        for canon in union_canons:
            idx = _vtrac_get_index(canon)
            if idx != best_idx:
                continue
            votes = 0
            votes += 1 if canon in dr_canon_set else 0
            votes += 1 if canon in stable_canon_set else 0
            votes += 1 if canon in hot_canon_set else 0
            votes += 1 if canon in vt_canon_set else 0
            votes += 1 if canon in aux_canon_set else 0
            scored.append((votes, float(dr_canon_score.get(canon, 0.0) or 0.0), _boxed_cost_units(canon), canon))

        picked_canons: List[str] = []
        if scored:
            scored.sort(key=lambda t: (-t[0], -t[1], t[2], t[3]))
            picked_canons = [canon for _, _, _, canon in scored[: int(boxed_canonicals)]]

        if not picked_canons:
            # Fallback to DR-004's best canonicals within the chosen index.
            for r in dr_top_indices:
                if not isinstance(r, dict):
                    continue
                try:
                    idx = int(r.get("vtrac_index"))
                except Exception:
                    continue
                if idx != best_idx:
                    continue
                tops = r.get("top_canonicals") or []
                if isinstance(tops, list):
                    for c in tops:
                        canon = _canon(str(c))
                        if not canon or canon in picked_canons:
                            continue
                        picked_canons.append(canon)
                        if len(picked_canons) >= int(boxed_canonicals):
                            break
                break

        picked_canons = [c for c in picked_canons if c][: int(boxed_canonicals)]
        if not picked_canons:
            continue

        combos: set[str] = set()
        for canon in picked_canons:
            combos.update(_unique_perms(canon))
        combos_sorted = sorted(combos)
        if not combos_sorted:
            continue

        packs.append(
            {
                "pack_id": f"fusion_gate_dr004:{section}:idx={best_idx}:box{len(picked_canons)}",
                "method_id": "fusion_gate_dr004",
                "variant": section,
                "play_mode": "BOX",
                "canonicals": sorted(set(picked_canons)),
                "combos": combos_sorted,
                "combos_count": len(combos_sorted),
                "cost_units": len(combos_sorted),
                "why_tags": [
                    "fusion_gate",
                    "dr004",
                    f"idx:{best_idx}",
                    f"min_sources:{int(min_sources)}",
                    f"sources:{','.join(sorted(best_srcs))}",
                    f"state:{state_key}",
                ],
                "transform_chain": [
                    "fusion_gate:dr004_index_convergence",
                    f"vtrac_index:{best_idx}",
                    f"box_expand_unique_perms:top{len(picked_canons)}",
                ],
                "evidence_paths": evidence_paths,
            }
        )

    packs.sort(key=lambda p: p.get("pack_id", ""))
    return packs


def _rank_aux_aggregated_digits(*, state_dir: Path, state_key: str) -> Tuple[List[str], List[Path]]:
    """
    Return digits ranked by Aux aggregated digit evidence (cross-position).

    We treat this as a discovery-safe signal:
    - Base score comes from Aux `aggregated_digits` weights.
    - We add explicit bonuses when tags include XVAR consensus and/or double-pressure.
    """
    aux_path = state_dir / "aux" / state_key / "summary.json"
    if not aux_path.exists():
        return [], []
    raw = _read_json(aux_path)
    if not isinstance(raw, dict):
        return [], [aux_path]
    positional = raw.get("positional") or {}
    if not isinstance(positional, dict):
        return [], [aux_path]
    shortlist = positional.get("shortlist_report") or {}
    if not isinstance(shortlist, dict):
        return [], [aux_path]
    aggregated = shortlist.get("aggregated_digits") or {}
    if not isinstance(aggregated, dict):
        return [], [aux_path]

    # digit -> best weighted score (max across positions)
    scores: Dict[str, float] = {}
    for _, items in aggregated.items():
        if not isinstance(items, list):
            continue
        for it in items:
            if not isinstance(it, dict):
                continue
            d = str(it.get("digit") if it.get("digit") is not None else "").strip()
            if d and d.isdigit():
                d = d[0]
            if d not in MIRROR_MAP:
                continue
            try:
                score = float(it.get("score") or 0.0)
            except Exception:
                score = 0.0
            tags = it.get("tags") if isinstance(it.get("tags"), list) else []
            tags_str = " ".join(str(t) for t in tags)
            if "XVAR-Cons" in tags_str:
                score += 100.0
            if "Double-Pressure" in tags_str:
                score += 50.0
            if score > scores.get(d, float("-inf")):
                scores[d] = score

    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    return [d for d, _ in ranked], [aux_path]


def _rank_due_doubles_mirror_pairs(*, day_dir: Path, state_key: str) -> Tuple[List[str], List[Path]]:
    """
    Return mirror-pair keys ranked by Control Center Due Doubles families.

    This is a *pair-selection* signal only. It does NOT imply the winner is a double.
    It is useful for mirror-double conversion because Due Doubles families are defined
    over the same VTRAC mirror-pair taxonomy (0/5, 1/6, 2/7, 3/8, 4/9).

    Input: sharepacks/<root>/<D>/control_center/due_doubles.csv
    Output: list of pair keys like ["1/6","3/8",...]
    """
    path = day_dir / "control_center" / "due_doubles.csv"
    rows = _load_csv_dict_rows(path)
    if not rows:
        return [], []

    inputs = [path]
    scores: Dict[str, float] = {}
    for r in rows:
        if (r.get("StateKey") or "").strip() != state_key:
            continue
        for i in range(1, 6):
            cell = (r.get(f"Family {i}") or "").strip()
            if not cell or cell == "-":
                continue
            family_label = cell.split(":", 1)[0].strip() if ":" in cell else ""
            if not family_label:
                continue
            # Family 1 is most important, Family 5 least.
            weight = float(6 - i)
            for token in (t.strip() for t in family_label.split("-") if t.strip()):
                if "/" not in token:
                    continue
                a, b = (x.strip() for x in token.split("/", 1))
                if not a or not b or a not in MIRROR_MAP or b not in MIRROR_MAP:
                    continue
                # Only accept true mirror pairs (vtrac_pair mapping).
                if _mirror_digit(a) != b and _mirror_digit(b) != a:
                    continue
                pair_key = f"{min(a, b)}/{max(a, b)}"
                scores[pair_key] = scores.get(pair_key, 0.0) + weight

    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    return [k for k, _ in ranked], inputs


def _build_mirror_pair_closure_packs_from_pairs(
    *,
    pair_keys: List[str],
    state_dir: Path,
    state_key: str,
    envelope: dict,
    top_pairs: int,
    top_thirds: int,
    method_id: str,
    pack_prefix: str,
    why_tag_src: str,
    evidence_paths: List[str],
) -> List[dict]:
    if top_pairs <= 0 or top_thirds <= 0:
        return []
    if not pair_keys:
        return []

    ranked_digits, _ = _rank_aux_aggregated_digits(state_dir=state_dir, state_key=state_key)
    has_aux_rank = bool(ranked_digits)
    ranked_pool = [d for d in ranked_digits if d in MIRROR_MAP]

    env_digits = envelope.get("digits") if isinstance(envelope, dict) else []
    if not isinstance(env_digits, list):
        env_digits = []
    env_digits = [str(d) for d in env_digits if str(d) in MIRROR_MAP]
    fallback_pool = env_digits + [str(d) for d in range(10)]

    selected: List[Tuple[str, str]] = []
    for pk in pair_keys:
        if "/" not in pk:
            continue
        a, b = (x.strip() for x in pk.split("/", 1))
        if a in MIRROR_MAP and b in MIRROR_MAP and (_mirror_digit(a) == b or _mirror_digit(b) == a):
            selected.append((min(a, b), max(a, b)))
        if len(selected) >= top_pairs:
            break
    if not selected:
        return []

    packs: List[dict] = []
    for a, b in selected:
        thirds: List[str] = []
        used_fallback = False
        for d in ranked_pool:
            if d in {a, b} or d in thirds:
                continue
            thirds.append(d)
            if len(thirds) >= top_thirds:
                break
        if len(thirds) < top_thirds:
            for d in fallback_pool:
                if d not in MIRROR_MAP or d in {a, b} or d in thirds:
                    continue
                thirds.append(d)
                used_fallback = True
                if len(thirds) >= top_thirds:
                    break

        canonicals: List[str] = []
        combos: set[str] = set()
        for t in thirds:
            if t in {a, b}:
                continue
            canon = "".join(sorted([a, b, t]))
            if not canon or len(set(canon)) != 3:
                continue
            canonicals.append(canon)
            combos.update(_unique_perms(canon))

        canonicals = sorted(set(canonicals))
        combos_list = sorted(combos)
        if not combos_list:
            continue

        pair_key = f"{a}/{b}"
        why_tags = [
            pack_prefix,
            f"pair:{pair_key}",
            f"top_pairs:{int(top_pairs)}",
            f"top_thirds:{int(top_thirds)}",
            f"thirds:{''.join(thirds)}",
            why_tag_src,
        ]
        if has_aux_rank:
            why_tags.append("thirds_src:aux_aggregated_digits")
        else:
            why_tags.append("thirds_src:digit_envelope")
        if used_fallback:
            why_tags.append("thirds_fallback:envelope_or_0_9")

        packs.append(
            {
                "pack_id": f"{pack_prefix}:pair={pair_key}",
                "method_id": method_id,
                "variant": "Unknown",
                "play_mode": "BOX",
                "canonicals": canonicals,
                "combos": combos_list,
                "combos_count": len(combos_list),
                "cost_units": len(combos_list),
                "why_tags": why_tags,
                "transform_chain": [
                    "aux_summary:positional_shortlist_report:aggregated_digits",
                    f"{pack_prefix}:{pair_key}:thirds_top{int(top_thirds)}(vtrac_pair)",
                    "box_expand_unique_perms",
                ],
                "evidence_paths": evidence_paths,
            }
        )

    packs.sort(key=lambda p: p.get("pack_id", ""))
    return packs


def _build_mirror_pair_closure_packs(
    *,
    state_dir: Path,
    state_key: str,
    envelope: dict,
    top_pairs: int = 2,
    top_thirds: int = 3,
) -> Tuple[List[dict], List[Path]]:
    """
    Build bounded mirror-pair closure packs for mirror-double conversion.

    Target failure mode: Candidate Universe hits the correct vtrac_index lane but misses the exact box.
    This pack adds a small BOX closure set of the form:
      { sort(d, mirror(d), t) for top t } * perms

    - d is selected from Aux aggregated digit evidence (fallback: digit envelope).
    - Third digits t are selected from Aux evidence (fallback: digit envelope / 0–9).
    """
    if top_pairs <= 0 or top_thirds <= 0:
        return [], []

    ranked_digits, inputs = _rank_aux_aggregated_digits(state_dir=state_dir, state_key=state_key)
    has_aux_rank = bool(ranked_digits)

    env_digits = envelope.get("digits") if isinstance(envelope, dict) else []
    if not isinstance(env_digits, list):
        env_digits = []
    env_digits = [str(d) for d in env_digits if str(d) in MIRROR_MAP]

    # Choose unique mirror pairs (unordered) from ranked digits (fallback: envelope digits).
    selected_pairs: List[Tuple[str, str]] = []
    seen_pairs: set[str] = set()
    for d in list(ranked_digits) + env_digits:
        if d not in MIRROR_MAP:
            continue
        m = _mirror_digit(d)
        a, b = (min(d, m), max(d, m))
        pair_key = f"{a}/{b}"
        if pair_key in seen_pairs:
            continue
        seen_pairs.add(pair_key)
        selected_pairs.append((a, b))
        if len(selected_pairs) >= top_pairs:
            break

    if not selected_pairs:
        return [], inputs

    ranked_pool = [d for d in ranked_digits if d in MIRROR_MAP]
    fallback_pool = env_digits + [str(d) for d in range(10)]

    packs: List[dict] = []
    evidence_paths = [_safe_rel(p) for p in inputs] if inputs else []

    packs = _build_mirror_pair_closure_packs_from_pairs(
        pair_keys=[f"{a}/{b}" for a, b in selected_pairs],
        state_dir=state_dir,
        state_key=state_key,
        envelope=envelope,
        top_pairs=top_pairs,
        top_thirds=top_thirds,
        method_id="mirror_pair_closure",
        pack_prefix="mirror_pair_closure",
        why_tag_src="src:aux_aggregated_digits" if has_aux_rank else "src:digit_envelope",
        evidence_paths=evidence_paths,
    )

    packs.sort(key=lambda p: p.get("pack_id", ""))
    return packs, inputs


def _build_mirror_pair_closure_due_doubles_packs(
    *,
    day_dir: Path,
    state_dir: Path,
    state_key: str,
    envelope: dict,
    top_pairs: int = 2,
    top_thirds: int = 2,
) -> Tuple[List[dict], List[Path]]:
    """
    Mirror-pair closure packs seeded from Control Center Due Doubles families.

    This is designed to address the dominant mirror-double miss mode:
    the correct mirror pair is often not selected by Aux digit ranking alone.
    """
    if top_pairs <= 0 or top_thirds <= 0:
        return [], []

    pair_keys, dd_inputs = _rank_due_doubles_mirror_pairs(day_dir=day_dir, state_key=state_key)
    if not pair_keys:
        return [], dd_inputs

    evidence_paths: List[str] = []
    for p in dd_inputs:
        evidence_paths.append(_safe_rel(p))
    aux_path = state_dir / "aux" / state_key / "summary.json"
    if aux_path.exists():
        evidence_paths.append(_safe_rel(aux_path))
    evidence_paths = sorted(set(evidence_paths))

    packs = _build_mirror_pair_closure_packs_from_pairs(
        pair_keys=pair_keys,
        state_dir=state_dir,
        state_key=state_key,
        envelope=envelope,
        top_pairs=top_pairs,
        top_thirds=top_thirds,
        method_id="mirror_pair_closure_due_doubles",
        pack_prefix="mirror_pair_closure_due_doubles",
        why_tag_src="src:due_doubles_families",
        evidence_paths=evidence_paths,
    )
    # IMPORTANT: do not return dd_inputs here; due_doubles.csv is already hashed by the main due_doubles parser.
    return packs, []


def _consensus_double_9(*, consensus_digit: str, key_digits: List[str], stable_additions: Optional[List[str]] = None) -> List[str]:
    """
    COMBINATION_FORMING3 primitive: CONSENSUS9 (9 core combos + optional stable additions).

    - consensus_digit: a single digit, or a “double digit” string like "66"; the last digit is used.
    - key_digits: up to 3 supporting digits (each produces a 3-perm double triad).
    """
    if not consensus_digit:
        return []
    trigger = str(consensus_digit)[-1]
    if trigger not in MIRROR_MAP:
        return []

    keys = [str(d)[0] for d in key_digits if str(d) and str(d)[0] in MIRROR_MAP][:3]
    out: set[str] = set()
    for kd in keys:
        out.update(
            {
                f"{trigger}{trigger}{kd}",
                f"{trigger}{kd}{trigger}",
                f"{kd}{trigger}{trigger}",
            }
        )

    if stable_additions:
        for s in stable_additions:
            triad = _normalize_pick3_literal(s)
            if triad:
                out.add(triad)

    return sorted({_normalize_pick3_literal(x) for x in out if _normalize_pick3_literal(x)})


def _repeated_digit(triad: str) -> str:
    triad = _normalize_pick3_literal(triad)
    if not triad or len(set(triad)) != 2:
        return ""
    for d in triad:
        if triad.count(d) == 2:
            return d
    return ""


def _build_consensus_double_pack(
    *,
    state_dir: Path,
    state_key: str,
    packs: Sequence[dict],
    envelope: dict,
    stable_additions_n: int = 0,
) -> Tuple[Optional[dict], List[Path]]:
    """
    Build a bounded CONSENSUS9 pack using sharepack-local evidence:
    - Prefer Aux aggregated digits with XVAR-Cons / Double-Pressure tags as the trigger digit.
    - Fallback: seed from Due Doubles top canonical (repeated digit).
    - Key digits: digit envelope top4 (excluding trigger), up to 3.
    """
    inputs: List[Path] = []
    evidence_paths: set[str] = set()

    trigger_digit = ""
    trigger_src = ""

    aux_path = state_dir / "aux" / state_key / "summary.json"
    if aux_path.exists():
        raw = _read_json(aux_path)
        if isinstance(raw, dict):
            positional = raw.get("positional") or {}
            shortlist = positional.get("shortlist_report") if isinstance(positional, dict) else {}
            aggregated = shortlist.get("aggregated_digits") if isinstance(shortlist, dict) else {}
            if isinstance(aggregated, dict):
                best_score = float("-inf")
                best_digit = ""
                for _, items in aggregated.items():
                    if not isinstance(items, list):
                        continue
                    for it in items:
                        if not isinstance(it, dict):
                            continue
                        d = str(it.get("digit") if it.get("digit") is not None else "").strip()
                        if d and d.isdigit():
                            d = d[0]
                        if d not in MIRROR_MAP:
                            continue
                        try:
                            score = float(it.get("score") or 0.0)
                        except Exception:
                            score = 0.0
                        tags = it.get("tags") if isinstance(it.get("tags"), list) else []
                        tags_str = " ".join(str(t) for t in tags)
                        if "XVAR-Cons" in tags_str:
                            score += 100.0
                        if "Double-Pressure" in tags_str:
                            score += 50.0
                        if score > best_score or (score == best_score and d < best_digit):
                            best_score = score
                            best_digit = d
                if best_digit:
                    trigger_digit = best_digit
                    trigger_src = "aux_aggregated_digits"
                    inputs.append(aux_path)
                    evidence_paths.add(_safe_rel(aux_path))

    if not trigger_digit:
        # Fallback: due doubles top canonical repeated digit.
        for p in packs:
            if str(p.get("method_id") or "") != "due_doubles":
                continue
            canonicals = p.get("canonicals") or []
            if isinstance(canonicals, list) and canonicals:
                seed = _canon(str(canonicals[0]))
                rep = _repeated_digit(seed)
                if rep:
                    trigger_digit = rep
                    trigger_src = "due_doubles_seed"
                    for ep in p.get("evidence_paths") or []:
                        if str(ep):
                            evidence_paths.add(str(ep))
                    break

    if not trigger_digit:
        # Last fallback: pooled digit envelope.
        digits = envelope.get("digits") if isinstance(envelope, dict) else []
        if isinstance(digits, list) and digits:
            d = str(digits[0])
            if d in MIRROR_MAP:
                trigger_digit = d
                trigger_src = "digit_envelope"

    if not trigger_digit:
        return None, inputs

    digits = envelope.get("digits") if isinstance(envelope, dict) else []
    key_digits = [str(d) for d in digits if str(d) in MIRROR_MAP and str(d) != trigger_digit][:3]
    if not key_digits:
        return None, inputs

    stable_additions: List[str] = []
    if stable_additions_n > 0:
        for p in packs:
            if str(p.get("method_id") or "") != "stable_top":
                continue
            for c in p.get("canonicals") or []:
                triad = _canon(str(c))
                if triad:
                    stable_additions.append(triad)
            for ep in p.get("evidence_paths") or []:
                if str(ep):
                    evidence_paths.add(str(ep))
            if len(stable_additions) >= stable_additions_n:
                break
        stable_additions = stable_additions[:stable_additions_n]

    combos = _consensus_double_9(consensus_digit=trigger_digit * 2, key_digits=key_digits, stable_additions=stable_additions)
    if not combos:
        return None, inputs

    why_tags = ["consensus_double", f"trigger:{trigger_digit}", f"trigger_src:{trigger_src}", f"keys:{''.join(key_digits)}"]
    if stable_additions:
        why_tags.append(f"stable_additions:{len(stable_additions)}")

    pack = {
        "pack_id": f"combo_pack:consensus_double_9:trigger={trigger_digit}:keys={''.join(key_digits)}",
        "method_id": "consensus_double_9",
        "variant": "Unknown",
        "play_mode": "MIXED",
        "canonicals": sorted({_canon(c) for c in combos if _canon(c)}),
        "combos": combos,
        "combos_count": len(combos),
        "cost_units": len(combos),
        "why_tags": why_tags,
        "transform_chain": [
            f"consensus_trigger:{trigger_digit}({trigger_src})",
            "key_digits:digit_envelope_top4",
            "consensus_double_9",
        ],
        "evidence_paths": sorted(evidence_paths),
    }
    return pack, inputs


def _build_digit_envelope(*, packs: Sequence[dict]) -> dict:
    # Gather digit evidence from pack canonicals and combos.
    digits: List[str] = []
    sources: List[str] = []
    for p in packs:
        # Keep the pooled digit envelope stable across optional v0.3 research packs.
        # Those packs should be additive, not perturb the derived combo packs unless
        # explicitly promoted into defaults later.
        if (p.get("method_id") or "") in {
            "digit_reduction_envelope_steps",
            "digit_reduction_dr004",
            "digit_reduction_dr004_index",
            "fusion_gate_dr004",
        }:
            continue
        pack_id = p.get("pack_id", "?")
        for c in p.get("canonicals", []) or []:
            c = _canon(c)
            if c:
                digits.extend(list(c))
                sources.append(f"{pack_id}:canonical")
        for s in p.get("combos", []) or []:
            s = _normalize_pick3_literal(s)
            if s:
                digits.extend(list(s))
                sources.append(f"{pack_id}:combo")

    top4 = _top_digits(digits, top_k=4)
    triads = _derive_triads_from_envelope(top4)
    return {
        "digits": top4,
        "sources": sorted(set(sources)),
        "derived_triads": triads,
        "notes": ["pooled_top4_from_packs"],
    }


def _build_combo_packs_from_envelope(*, envelope: dict) -> List[dict]:
    triads = envelope.get("derived_triads") or []
    if not isinstance(triads, list):
        return []
    triads = [t for t in (_normalize_pick3_literal(x) for x in triads) if t]
    if not triads:
        return []

    packs: List[dict] = []

    # R-perm-4 across derived triads (bounded closure).
    combos_r4: set[str] = set()
    for t in triads:
        combos_r4.update(_r_perm_4(t))
    packs.append(
        {
            "pack_id": "combo_pack:R-perm-4:envelope",
            "method_id": "R-perm-4",
            "variant": "Unknown",
            "play_mode": "STRAIGHT",
            "canonicals": sorted({_canon(c) for c in combos_r4 if _canon(c)}),
            "combos": sorted(combos_r4),
            "combos_count": len(combos_r4),
            "cost_units": len(combos_r4),
            "why_tags": ["combo_pack", "envelope_top4"],
            "transform_chain": ["digit_envelope:top4", "derived_triads:choose3", "r_perm_4"],
            "evidence_paths": [],
        }
    )

    seed = triads[0]
    vt8 = _vt8_expand_ordered(seed)
    packs.append(
        {
            "pack_id": f"combo_pack:PackA_vt8:seed={seed}",
            "method_id": "PackA_vt8",
            "variant": "Unknown",
            "play_mode": "STRAIGHT",
            "canonicals": sorted({_canon(c) for c in vt8 if _canon(c)}),
            "combos": vt8,
            "combos_count": len(vt8),
            "cost_units": len(vt8),
            "why_tags": ["combo_pack", "vt8_expand_ordered"],
            "transform_chain": [f"seed_triad:{seed}", "vt8_expand_ordered(vtrac_pair)"],
            "evidence_paths": [],
        }
    )

    m12 = _method1_pair_mirror_12(seed)
    packs.append(
        {
            "pack_id": f"combo_pack:PackB_mirror3rd:seed={seed}",
            "method_id": "PackB_mirror3rd",
            "variant": "Unknown",
            "play_mode": "STRAIGHT",
            "canonicals": sorted({_canon(c) for c in m12 if _canon(c)}),
            "combos": m12,
            "combos_count": len(m12),
            "cost_units": len(m12),
            "why_tags": ["combo_pack", "keep_pair_mirror_third"],
            "transform_chain": [f"seed_triad:{seed}", "keep_pair_mirror_third(vtrac_pair)", "r_perm_4"],
            "evidence_paths": [],
        }
    )

    # Double packs if the seed itself is a double.
    if _is_double(seed):
        d6a = _double_pack_mirror_single_6(seed)
        packs.append(
            {
                "pack_id": f"combo_pack:doubles_mirror_single:seed={seed}",
                "method_id": "doubles_mirror_single",
                "variant": "Unknown",
                "play_mode": "STRAIGHT",
                "canonicals": sorted({_canon(c) for c in d6a if _canon(c)}),
                "combos": d6a,
                "combos_count": len(d6a),
                "cost_units": len(d6a),
                "why_tags": ["combo_pack", "double_seed"],
                "transform_chain": [f"seed_triad:{seed}", "double_pack_mirror_single_6(vtrac_pair)"],
                "evidence_paths": [],
            }
        )
        d6b = _double_pack_mirror_double_6(seed)
        packs.append(
            {
                "pack_id": f"combo_pack:doubles_mirror_double:seed={seed}",
                "method_id": "doubles_mirror_double",
                "variant": "Unknown",
                "play_mode": "STRAIGHT",
                "canonicals": sorted({_canon(c) for c in d6b if _canon(c)}),
                "combos": d6b,
                "combos_count": len(d6b),
                "cost_units": len(d6b),
                "why_tags": ["combo_pack", "double_seed"],
                "transform_chain": [f"seed_triad:{seed}", "double_pack_mirror_double_6(vtrac_pair)"],
                "evidence_paths": [],
            }
        )

    return packs


def _collect_union(packs: Sequence[dict]) -> Tuple[List[str], int]:
    union: set[str] = set()
    for p in packs:
        for c in p.get("combos", []) or []:
            c = _normalize_pick3_literal(c)
            if c:
                union.add(c)
    out = sorted(union)
    return out, len(out)


def _write_candidate_universe_md(*, out_path: Path, payload: Dict[str, Any]) -> None:
    def short_list(items: Sequence[str], limit: int = 8) -> str:
        xs = [str(x) for x in items if str(x)]
        if len(xs) <= limit:
            return ", ".join(xs)
        return ", ".join(xs[:limit]) + f", …(+{len(xs) - limit})"

    state_key = str(payload.get("state_key") or "?")
    results_date = str(payload.get("results_date") or "?")
    history_date = str(payload.get("history_date") or "-")
    generated_at = str(payload.get("generated_at") or "-")
    inputs_hash = str(payload.get("inputs_hash") or "-")
    packs = payload.get("packs") or []
    union_count = int(payload.get("union_combos_count") or 0)
    leakage = bool(payload.get("contains_winners_artifacts"))
    leakage_issues = payload.get("leakage_issues") or []

    lines: List[str] = []
    lines.append(f"# Candidate Universe — {state_key} — D={results_date}")
    lines.append("")
    lines.append("This is a **pre-results** playset artifact (gradeable later).")
    lines.append("")
    lines.append("## Meta")
    lines.append("")
    lines.append(f"- generated_at: `{generated_at}`")
    lines.append(f"- history_date (H): `{history_date}`")
    lines.append(f"- results_date (D): `{results_date}`")
    lines.append(f"- inputs_hash: `{inputs_hash}`")
    lines.append(f"- packs: `{len(packs) if isinstance(packs, list) else 0}`")
    lines.append(f"- union_combos_count: `{union_count}`")
    lines.append("")
    lines.append("## Leakage")
    lines.append("")
    lines.append(f"- contains_winners_artifacts: `{str(leakage).lower()}`")
    if leakage_issues:
        for issue in leakage_issues:
            lines.append(f"- issue: `{issue}`")
    else:
        lines.append("- issues: none")
    lines.append("")
    lines.append("## Packs")
    lines.append("")

    if isinstance(packs, list):
        for p in packs:
            if not isinstance(p, dict):
                continue
            pack_id = str(p.get("pack_id") or "?")
            method_id = str(p.get("method_id") or "?")
            variant = str(p.get("variant") or "Unknown")
            play_mode = str(p.get("play_mode") or "Unknown")
            combos = p.get("combos") or []
            canonicals = p.get("canonicals") or []
            why_tags = p.get("why_tags") or []
            evidence_paths = p.get("evidence_paths") or []
            lines.append(f"### `{pack_id}`")
            lines.append("")
            lines.append(f"- method_id: `{method_id}`")
            lines.append(f"- variant: `{variant}`")
            lines.append(f"- play_mode: `{play_mode}`")
            lines.append(f"- combos_count: `{int(p.get('combos_count') or 0)}`")
            lines.append(f"- cost_units: `{int(p.get('cost_units') or 0)}`")
            if canonicals:
                lines.append(f"- canonicals: {short_list([str(c) for c in canonicals], limit=12)}")
            if why_tags:
                lines.append(f"- why_tags: {short_list([str(t) for t in why_tags], limit=12)}")
            if evidence_paths:
                lines.append(f"- evidence_paths: {short_list([str(e) for e in evidence_paths], limit=8)}")
            if combos:
                lines.append(f"- combos(sample): {short_list([str(c) for c in combos], limit=18)}")
            lines.append("")

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _pack_source_class(method_id: str) -> str:
    """
    Classify packs for "evidence-only" exports.

    This is intentionally coarse: it's meant to disambiguate
    (a) direct tool evidence, (b) Control Center boards, and
    (c) derived/transform packs.
    """
    m = (method_id or "").strip()
    if m in {
        "stable_top",
        "stable_compound_top",
        "stable_family_vote",
        "stable_family_vote_v2",
        "stable_last_remaining",
        "digit_reduction_analyzer_v2",
        "vtrac_enhanced_top",
        "hot_zones_top",
        "aux_positional",
        "aux_vtrac_index_overdue",
    }:
        return "tool"
    if m in {"due_doubles", "profit_alerts"}:
        return "control_center"
    if m == "blackapple":
        return "control_center"
    if m in {
        "due_doubles_mirror_single",
        "due_doubles_mirror_double",
        "hot_zones_index_closure",
        "consensus_double_9",
        "R-perm-4",
        "PackA_vt8",
        "PackB_mirror3rd",
        "doubles_mirror_single",
        "doubles_mirror_double",
    }:
        return "derived"
    return "other"


def _write_candidate_universe_evidence_csv(*, out_path: Path, payload: Dict[str, Any]) -> None:
    """
    Write an evidence-focused CSV that makes CU provenance explicit.

    It is NOT a "pick list" and does not apply budgets.
    It is a view over CU packs so you can see exactly what came from:
      - direct tool outputs
      - Control Center boards
      - derived/transform packs
    """
    packs = payload.get("packs") or []
    if not isinstance(packs, list):
        packs = []

    rows: List[Dict[str, str]] = []
    for p in packs:
        if not isinstance(p, dict):
            continue
        pack_id = str(p.get("pack_id") or "")
        method_id = str(p.get("method_id") or "")
        variant = str(p.get("variant") or "Unknown")
        play_mode = str(p.get("play_mode") or "Unknown")
        combos_count = str(int(p.get("combos_count") or 0))
        cost_units = str(int(p.get("cost_units") or 0))
        why_tags = "|".join(sorted({str(x) for x in (p.get("why_tags") or []) if str(x)}))
        evidence_paths = "|".join(sorted({str(x) for x in (p.get("evidence_paths") or []) if str(x)}))
        transform_chain = "|".join([str(x) for x in (p.get("transform_chain") or []) if str(x)])

        canonicals = p.get("canonicals") or []
        if not isinstance(canonicals, list):
            canonicals = []
        canonicals_norm = sorted({_canon(str(c)) for c in canonicals if _canon(str(c))})
        for canonical in canonicals_norm:
            rows.append(
                {
                    "results_date": str(payload.get("results_date") or ""),
                    "history_date": str(payload.get("history_date") or ""),
                    "profile": str(payload.get("profile") or ""),
                    "state_key": str(payload.get("state_key") or ""),
                    "canonical": canonical,
                    "source_class": _pack_source_class(method_id),
                    "method_id": method_id,
                    "variant": variant,
                    "play_mode": play_mode,
                    "pack_id": pack_id,
                    "combos_count": combos_count,
                    "cost_units": cost_units,
                    "why_tags": why_tags,
                    "evidence_paths": evidence_paths,
                    "transform_chain": transform_chain,
                }
            )

    # Stable ordering for diffs and reproducibility.
    rows.sort(
        key=lambda r: (
            r.get("state_key", ""),
            r.get("canonical", ""),
            r.get("source_class", ""),
            r.get("method_id", ""),
            r.get("variant", ""),
            r.get("pack_id", ""),
        )
    )

    fieldnames = [
        "results_date",
        "history_date",
        "profile",
        "state_key",
        "canonical",
        "source_class",
        "method_id",
        "variant",
        "play_mode",
        "pack_id",
        "combos_count",
        "cost_units",
        "why_tags",
        "evidence_paths",
        "transform_chain",
    ]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: (r.get(k) or "") for k in fieldnames})


def _write_candidate_universe_evidence_md(*, out_path: Path, payload: Dict[str, Any]) -> None:
    packs = payload.get("packs") or []
    if not isinstance(packs, list):
        packs = []

    # Aggregate by canonical across all packs.
    agg: Dict[str, Dict[str, Any]] = {}
    for p in packs:
        if not isinstance(p, dict):
            continue
        pack_id = str(p.get("pack_id") or "")
        method_id = str(p.get("method_id") or "")
        variant = str(p.get("variant") or "Unknown")
        source_class = _pack_source_class(method_id)
        canonicals = p.get("canonicals") or []
        if not isinstance(canonicals, list):
            continue
        for c in canonicals:
            canon = _canon(str(c))
            if not canon:
                continue
            entry = agg.setdefault(
                canon,
                {
                    "tool_methods": set(),
                    "cc_methods": set(),
                    "derived_methods": set(),
                    "other_methods": set(),
                    "variants": set(),
                    "packs": [],
                },
            )
            entry["variants"].add(variant)
            entry["packs"].append(f"{source_class}:{method_id}:{pack_id}")
            if source_class == "tool":
                entry["tool_methods"].add(method_id)
            elif source_class == "control_center":
                entry["cc_methods"].add(method_id)
            elif source_class == "derived":
                entry["derived_methods"].add(method_id)
            else:
                entry["other_methods"].add(method_id)

    # Summaries to reduce anxiety: what's truly "direct evidence" vs "derived only".
    canonicals = sorted(agg.keys())
    direct = [c for c in canonicals if agg[c]["tool_methods"] or agg[c]["cc_methods"]]
    derived_only = [c for c in canonicals if c not in direct]

    lines: List[str] = []
    state_key = str(payload.get("state_key") or "?")
    results_date = str(payload.get("results_date") or "?")
    profile = str(payload.get("profile") or "?")
    inputs_hash = str(payload.get("inputs_hash") or "-")
    lines.append(f"# Candidate Universe — Evidence View — {state_key} — D={results_date} ({profile})")
    lines.append("")
    lines.append("Purpose: make Candidate Universe provenance explicit (what came from tools/boards vs what is derived).")
    lines.append("This file is additive: it does not change CU packs, budgets, or grading.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- inputs_hash: `{inputs_hash}`")
    lines.append(f"- unique_canonicals_total: `{len(canonicals)}`")
    lines.append(f"- canonicals_with_direct_evidence (tool or Control Center): `{len(direct)}`")
    lines.append(f"- canonicals_derived_only: `{len(derived_only)}`")
    lines.append("")
    lines.append("Legend:")
    lines.append("- source_class `tool` = Stable/DR/VTRAC/HZ/Aux outputs")
    lines.append("- source_class `control_center` = boards like Due Doubles / Profit Alerts")
    lines.append("- source_class `derived` = combo/closure packs produced from the digit envelope / seeds")
    lines.append("")
    lines.append("## Canonical Evidence (top by support)")
    lines.append("")
    lines.append("| Canonical | Tool methods | CC methods | Derived methods | Variants | Packs |")
    lines.append("|---:|---:|---:|---:|---:|---|")

    def support_key(c: str) -> Tuple[int, int, int, int, str]:
        e = agg[c]
        return (
            -len(e["tool_methods"]),
            -len(e["cc_methods"]),
            -len(e["derived_methods"]),
            -len(e["packs"]),
            c,
        )

    for canon in sorted(canonicals, key=support_key)[:60]:
        e = agg[canon]
        variants = ",".join(sorted(e["variants"]))
        packs = ", ".join(sorted(e["packs"])[:6])
        if len(e["packs"]) > 6:
            packs += f", …(+{len(e['packs']) - 6})"
        lines.append(
            "| "
            + " | ".join(
                [
                    canon,
                    str(len(e["tool_methods"])),
                    str(len(e["cc_methods"])),
                    str(len(e["derived_methods"])),
                    variants or "-",
                    packs or "-",
                ]
            )
            + " |"
        )

    if len(canonicals) > 60:
        lines.append("")
        lines.append(f"(Top 60 shown; total canonicals = {len(canonicals)}.)")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Create per-state candidate_universe.json inside a frozen sharepack day.")
    ap.add_argument("--date", required=True, help="Sharepack day date D (YYYY-MM-DD)")
    ap.add_argument(
        "--sharepacks-root",
        default="sharepacks/_predictive",
        help="Sharepacks root directory (default: sharepacks/_predictive)",
    )
    ap.add_argument(
        "--profile",
        choices=["mixed", "tool_only", "profit_only"],
        default="tool_only",
        help="Ablation profile for pack sources (default: tool_only). tool_only = skip profit_alerts packs; profit_only = profit_alerts packs only.",
    )
    ap.add_argument(
        "--experiment-tag",
        default="",
        help=textwrap.dedent(
            """\
            Optional experiment tag appended to output filenames (default: none).
            Example: --experiment-tag dr004_v1 writes candidate_universe__tool_only__dr004_v1.json.
            """
        ).strip(),
    )
    ap.add_argument("--states", nargs="*", help="Optional subset of state keys (default: auto-discover from day dir)")
    ap.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing candidate_universe*.json (default: refuse).",
    )
    ap.add_argument(
        "--allow-winners-artifacts",
        action="store_true",
        help="Allow running even if winners-dependent artifacts are detected (NOT recommended for predictive packs).",
    )
    ap.add_argument("--top-n-stable", type=int, default=3, help="Top N stable canonicals per section (default: 3)")
    ap.add_argument(
        "--top-n-stable-compound",
        type=int,
        default=0,
        help="Optional Stable compound packs: top N direct 3-digit compound canonicals per section (default: 0 disables).",
    )
    ap.add_argument(
        "--top-n-stable-families",
        type=int,
        default=0,
        help="Optional Stable family-vote packs: top N family/lane closure packs per section (default: 0 disables).",
    )
    ap.add_argument(
        "--top-n-stable-families-v2",
        type=int,
        default=0,
        help="Optional Stable family-vote v2 packs: top N extra bounded family/lane closure packs per section using richer arena evidence (default: 0 disables).",
    )
    ap.add_argument(
        "--top-n-stable-last-remaining",
        type=int,
        default=0,
        help="Optional Stable survivor packs: top N last-remaining family/lane packs per section (default: 0 disables).",
    )
    ap.add_argument(
        "--stable-lane-closure-max-cost-units",
        type=int,
        default=12,
        help="Stable family/lane closure hard cap in boxed cost units (default: 12).",
    )
    ap.add_argument("--top-n-dr", type=int, default=0, help="Top N DR analyzer patterns per variant (default: 0)")
    ap.add_argument(
        "--dr-envelope-boxed-canonicals",
        type=int,
        default=0,
        help="Optional DR envelope packs: BOX-expand top N envelope-derived canonicals per section from DR steps CSV (default: 0 disables).",
    )
    ap.add_argument(
        "--dr004-boxed-canonicals",
        type=int,
        default=0,
        help="Optional DR-004 packs: BOX-expand top N DR-004 canonicals per section from DR steps CSV (default: 0 disables).",
    )
    ap.add_argument(
        "--dr004-index-boxed-canonicals",
        type=int,
        default=0,
        help="Optional DR-004 index-gateway packs: pick up to N boxed canonicals (1 per index) per section (default: 0 disables).",
    )
    ap.add_argument(
        "--dr004-recent-draws",
        type=int,
        default=0,
        help="Optional DR-004 recency penalty: count digits from N most recent draws (sharepack-local aux/draws) (default: 0 disables).",
    )
    ap.add_argument(
        "--dr004-max-cost-units",
        type=int,
        default=0,
        help="Optional DR-004 hard cap on boxed cost units per pack (default: 0 = no cap).",
    )
    ap.add_argument(
        "--dr004-min-unique-digits",
        type=int,
        default=1,
        help="DR-004 pool filter: minimum unique digits per segment (default: 1).",
    )
    ap.add_argument(
        "--dr004-max-unique-digits",
        type=int,
        default=3,
        help="DR-004 pool filter: maximum unique digits per segment (default: 3; set to 4 to enable envelope4).",
    )
    ap.add_argument(
        "--dr004-write-signals",
        action="store_true",
        help="Write dr004_signals*.json next to candidate_universe.json (predictive-safe; default: off).",
    )
    ap.add_argument(
        "--dr004-signals-top-pools",
        type=int,
        default=12,
        help="When writing DR-004 signals, record this many top digit pools per section (default: 12).",
    )
    ap.add_argument(
        "--dr004-signals-top-canonicals",
        type=int,
        default=25,
        help="When writing DR-004 signals, record this many top canonicals per section (default: 25).",
    )
    ap.add_argument(
        "--dr004-signals-top-indices",
        type=int,
        default=12,
        help="When writing DR-004 signals, record this many top VTRAC indices per section (default: 12).",
    )
    ap.add_argument(
        "--write-signals-bundle",
        action="store_true",
        help="Write signals_bundle*.json next to candidate_universe.json (predictive-safe; default: off).",
    )
    ap.add_argument(
        "--fusion-gate-boxed-canonicals",
        type=int,
        default=0,
        help="Optional fusion-gate packs: BOX-expand up to N canonicals per section when DR-004 converges with other tool signals (default: 0 disables).",
    )
    ap.add_argument(
        "--fusion-gate-min-sources",
        type=int,
        default=2,
        help="Fusion-gate threshold: require this many supporting signal sources including DR-004 (default: 2).",
    )
    ap.add_argument("--top-n-vtrac", type=int, default=8, help="Top N VTRAC straights (default: 8)")
    ap.add_argument("--top-n-vtrac-indices", type=int, default=12, help="Top N VTRAC indices (signals bundle; default: 12)")
    ap.add_argument("--top-n-hot", type=int, default=8, help="Top N Hot Zones triads (default: 8)")
    ap.add_argument(
        "--hot-zones-index-closure",
        action="store_true",
        help="Add an optional Hot Zones VTRAC-index closure pack (bounded box-expansion from dominant index; default: off).",
    )
    ap.add_argument(
        "--hot-zones-index-closure-boxed-canonicals",
        type=int,
        default=2,
        help="BOX-expand this many Hot Zones seed canonicals from the dominant index (default: 2 => ~12 lines).",
    )
    ap.add_argument("--top-n-aux", type=int, default=10, help="Top N Aux positional shortlist combos (default: 10)")
    ap.add_argument(
        "--top-n-aux-vtrac-indices",
        type=int,
        default=2,
        help="Top N Aux overdue VTRAC indices per variant to include as index-closure packs (default: 2; 0 disables).",
    )
    ap.add_argument(
        "--top-n-blackapple",
        type=int,
        default=0,
        help="Top N Blackapple candidates per ALERT variant to include as STRAIGHT packs (default: 0 disables).",
    )
    ap.add_argument(
        "--blackapple-min-score",
        type=int,
        default=3,
        help="Minimum Blackapple score to include a pack (default: 3 => ALERT).",
    )
    ap.add_argument(
        "--top-n-due-doubles",
        type=int,
        default=4,
        help="Top N due-doubles canonicals per variant row (BOX-expanded; default: 4 => ~12 combos).",
    )
    ap.add_argument(
        "--due-doubles-mirror-seeds",
        type=int,
        default=1,
        help="Seed count (per due-doubles variant row) to expand into mirror-double packs (default: 1; 0 disables).",
    )
    ap.add_argument(
        "--mirror-pair-closure-pairs",
        type=int,
        default=2,
        help="Top N mirror pairs to close using Aux aggregated digits (default: 2; 0 disables).",
    )
    ap.add_argument(
        "--top-n-mirror-pair-closure",
        type=int,
        default=3,
        help="Top N third digits per mirror-pair closure pack (default: 3; 0 disables).",
    )
    ap.add_argument(
        "--mirror-pair-closure-due-doubles-pairs",
        type=int,
        default=0,
        help="Top N mirror pairs to close using Due Doubles families (default: 0 disables; recommended starting point: 2).",
    )
    ap.add_argument(
        "--top-n-mirror-pair-closure-due-doubles",
        type=int,
        default=2,
        help="Top N third digits per due-doubles mirror-pair closure pack (default: 2; 0 disables).",
    )
    ap.add_argument(
        "--skip-combo-packs",
        action="store_true",
        help="Skip generating combination-forming packs from the pooled digit envelope.",
    )
    ap.add_argument(
        "--skip-consensus-double-pack",
        action="store_true",
        help="Skip generating the COMBINATION_FORMING3 consensus double-trigger pack (CONSENSUS9).",
    )
    ap.add_argument(
        "--consensus-stable-additions",
        type=int,
        default=0,
        help="Optional stable additions to include in CONSENSUS9 (default: 0).",
    )
    ap.add_argument(
        "--write-md",
        action="store_true",
        help="Also write candidate_universe.md next to candidate_universe.json (default: off).",
    )
    ap.add_argument(
        "--write-evidence",
        action="store_true",
        help="Also write candidate_universe_evidence.csv/.md next to candidate_universe.json (default: off).",
    )
    ap.add_argument(
        "--write-dr-arena",
        action="store_true",
        help="Also write analysis/dr_arena*.json/.md from the frozen Digit Reduction bundle (default: off).",
    )
    ap.add_argument(
        "--dr-arena-top-trace",
        type=int,
        default=10,
        help="Top N DR trace-strength family rows per variant to keep in the arena (default: 10).",
    )
    ap.add_argument(
        "--dr-arena-top-lane",
        type=int,
        default=10,
        help="Top N DR lane-only confidence family rows per variant to keep in the arena (default: 10).",
    )
    ap.add_argument(
        "--dr-arena-top-competing",
        type=int,
        default=10,
        help="Top N DR competing-literal pressure rows per variant to keep in the arena (default: 10).",
    )
    ap.add_argument(
        "--dr-arena-top-double",
        type=int,
        default=10,
        help="Top N DR double-pressure rows per variant to keep in the arena (default: 10).",
    )
    ap.add_argument(
        "--dr-arena-top-row-repeat",
        type=int,
        default=10,
        help="Top N DR row-repeat / final-survival entries per variant to keep in the arena (default: 10).",
    )
    ap.add_argument(
        "--dr-arena-top-preclusters",
        type=int,
        default=12,
        help="Top N DR pre-reduction cluster entries per variant to keep in the arena (default: 12).",
    )
    ap.add_argument(
        "--dr-arena-top-reveals",
        type=int,
        default=12,
        help="Top N DR reduction-reveal entries per variant to keep in the arena (default: 12).",
    )
    ap.add_argument(
        "--dr-arena-top-fourth",
        type=int,
        default=10,
        help="Top N DR fourth-variable candidates per variant to keep in the arena (default: 10).",
    )
    ap.add_argument(
        "--write-stable-arena",
        action="store_true",
        help="Also write analysis/stable_arena*.json/.md from the frozen Stable bundle (default: off).",
    )
    ap.add_argument(
        "--write-aux-cc-arena",
        action="store_true",
        help="Also write analysis/aux_control_center_arena*.json/.md from frozen Aux summary + Control Center artifacts (default: off).",
    )
    ap.add_argument(
        "--aux-cc-arena-top-items",
        type=int,
        default=8,
        help="Top N rows/items per Aux / Control Center arena object to keep (default: 8).",
    )
    ap.add_argument(
        "--stable-arena-top-rows",
        type=int,
        default=25,
        help="Top N Stable row patterns per variant to keep in the arena (default: 25).",
    )
    ap.add_argument(
        "--stable-arena-top-pattern-ledgers",
        type=int,
        default=25,
        help="Top N Stable variant-level pattern ledgers per variant to keep in the arena (default: 25).",
    )
    ap.add_argument(
        "--stable-arena-top-compound",
        type=int,
        default=25,
        help="Top N Stable compound rows per variant to keep in the arena (default: 25).",
    )
    ap.add_argument(
        "--stable-arena-top-families",
        type=int,
        default=10,
        help="Top N Stable family/lane rollups per variant to keep in the arena (default: 10).",
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

    states = list(args.states) if args.states else sorted(
        p.name for p in day_dir.iterdir() if p.is_dir() and p.name != "control_center"
    )
    if not states:
        raise SystemExit(f"No states found under: {_safe_rel(day_dir)}")

    strict_predictive = _is_predictive_root(sharepacks_root) and not args.allow_winners_artifacts

    cc_meta = _load_control_center_meta(day_dir)

    profile = str(args.profile or "mixed").strip()
    out_suffix = "" if profile == "mixed" else f"__{profile}"
    exp_tag = _normalize_experiment_tag(args.experiment_tag)
    tag_suffix = f"__{exp_tag}" if exp_tag else ""
    include_profit_alerts = profile in {"mixed", "profit_only"}
    include_non_profit = profile in {"mixed", "tool_only"}

    for state_key in states:
        state_dir = day_dir / state_key
        if not state_dir.exists():
            raise SystemExit(f"Missing state dir: {_safe_rel(state_dir)}")

        out_path = state_dir / f"candidate_universe{out_suffix}{tag_suffix}.json"
        if out_path.exists() and not args.force:
            raise SystemExit(
                f"Refusing to overwrite existing candidate universe: {_safe_rel(out_path)} (use --force)"
            )
        arena_path = state_dir / "analysis" / f"stable_arena{out_suffix}{tag_suffix}.json"
        if args.write_stable_arena and arena_path.exists() and not args.force:
            raise SystemExit(
                f"Refusing to overwrite existing stable arena: {_safe_rel(arena_path)} (use --force)"
            )
        dr_arena_path = state_dir / "analysis" / f"dr_arena{out_suffix}{tag_suffix}.json"
        if args.write_dr_arena and dr_arena_path.exists() and not args.force:
            raise SystemExit(
                f"Refusing to overwrite existing DR arena: {_safe_rel(dr_arena_path)} (use --force)"
            )
        aux_cc_arena_path = state_dir / "analysis" / f"aux_control_center_arena{out_suffix}{tag_suffix}.json"
        if args.write_aux_cc_arena and aux_cc_arena_path.exists() and not args.force:
            raise SystemExit(
                f"Refusing to overwrite existing Aux/CC arena: {_safe_rel(aux_cc_arena_path)} (use --force)"
            )

        leakage = _detect_winners_artifacts(day_dir=day_dir, state_dir=state_dir)
        if leakage and strict_predictive:
            joined = "\n  - " + "\n  - ".join(leakage)
            raise SystemExit(
                "Winners-dependent artifacts detected inside predictive sharepack; aborting.\n"
                f"date={args.date} state={state_key} root={_safe_rel(sharepacks_root)}\n"
                f"Issues:{joined}\n"
                "If you *intentionally* want to run anyway, pass --allow-winners-artifacts."
            )

        packs: List[dict] = []
        inputs: List[Path] = []
        stable_arena_payload: Optional[Dict[str, Any]] = None
        dr_arena_payload: Optional[Dict[str, Any]] = None
        aux_cc_arena_payload: Optional[Dict[str, Any]] = None
        aux_badge_sig_cached: Optional[Dict[str, Any]] = None
        aux_cc_sig_cached: Optional[Dict[str, Any]] = None
        if include_non_profit and (int(args.top_n_stable_families_v2) > 0 or args.write_stable_arena):
            stable_arena_payload = build_stable_arena_payload(
                state_dir=state_dir,
                state_key=state_key,
                results_date=args.date,
                history_date=cc_meta.history_date,
                profile=profile,
                experiment_tag=exp_tag,
                sharepacks_root=sharepacks_root,
                contains_winners_artifacts=bool(leakage),
                repo_root=REPO_ROOT,
                top_rows=max(1, int(args.stable_arena_top_rows)),
                top_pattern_ledgers=max(1, int(args.stable_arena_top_pattern_ledgers)),
                top_compound=max(1, int(args.stable_arena_top_compound)),
                top_families=max(
                    1,
                    int(args.stable_arena_top_families),
                    int(args.top_n_stable_families) + int(args.top_n_stable_families_v2) + 6,
                ),
            )
        if include_non_profit and args.write_dr_arena:
            dr_arena_payload = build_dr_arena_payload(
                state_dir=state_dir,
                state_key=state_key,
                results_date=args.date,
                history_date=cc_meta.history_date,
                profile=profile,
                experiment_tag=exp_tag,
                sharepacks_root=sharepacks_root,
                contains_winners_artifacts=bool(leakage),
                repo_root=REPO_ROOT,
                top_trace=max(1, int(args.dr_arena_top_trace)),
                top_lane=max(1, int(args.dr_arena_top_lane)),
                top_competing=max(1, int(args.dr_arena_top_competing)),
                top_double=max(1, int(args.dr_arena_top_double)),
                top_row_repeat=max(1, int(args.dr_arena_top_row_repeat)),
                top_preclusters=max(1, int(args.dr_arena_top_preclusters)),
                top_reveals=max(1, int(args.dr_arena_top_reveals)),
                top_fourth=max(1, int(args.dr_arena_top_fourth)),
            )
        if args.write_aux_cc_arena or (args.write_signals_bundle and include_non_profit):
            aux_badge_sig_cached, _ = _extract_aux_badge_pressure_signals(
                state_dir=state_dir,
                state_key=state_key,
                top_k=max(5, int(args.aux_cc_arena_top_items)),
            )
            aux_cc_arena_payload = build_aux_control_center_arena_payload(
                day_dir=day_dir,
                state_dir=state_dir,
                state_key=state_key,
                results_date=args.date,
                history_date=cc_meta.history_date,
                profile=profile,
                experiment_tag=exp_tag,
                sharepacks_root=sharepacks_root,
                contains_winners_artifacts=bool(leakage),
                repo_root=REPO_ROOT,
                badge_pressure=aux_badge_sig_cached,
                top_items=max(1, int(args.aux_cc_arena_top_items)),
            )
            aux_cc_sig_cached = build_aux_control_center_signals(aux_cc_arena_payload)

        # 1) Profit Alerts (Control Center)
        if include_profit_alerts:
            pa_packs, pa_inputs = _parse_profit_alerts(day_dir=day_dir, state_key=state_key)
            packs.extend(pa_packs)
            inputs.extend(pa_inputs)

        # 1b+) Non-profit packs (Brain-1 + Aux + bounded combo packs)
        if include_non_profit:
            # 1b) Due Doubles (Control Center) (bounded BOX packs)
            dd_packs, dd_inputs = _parse_due_doubles(
                day_dir=day_dir, state_key=state_key, top_n=int(args.top_n_due_doubles)
            )
            packs.extend(dd_packs)
            inputs.extend(dd_inputs)

            # 1c) Due Doubles mirror packs (bounded)
            dd_mirror = _derive_due_doubles_mirror_packs(
                due_packs=dd_packs, seed_top_n=int(args.due_doubles_mirror_seeds)
            )
            packs.extend(dd_mirror)

            # 2) Stable (top canonicals per section, BOX-expanded)
            st_packs, st_inputs = _parse_stable_top(
                state_dir=state_dir, state_key=state_key, top_n=int(args.top_n_stable)
            )
            packs.extend(st_packs)
            inputs.extend(st_inputs)

            # 2b) Stable compound direct packs (optional; default-off)
            st_compound_packs, st_compound_inputs = _parse_stable_compound_top(
                state_dir=state_dir,
                state_key=state_key,
                top_n=int(args.top_n_stable_compound),
            )
            packs.extend(st_compound_packs)
            inputs.extend(st_compound_inputs)

            # 2c) Stable family/lane vote packs (optional; default-off)
            st_family_packs, st_family_inputs = _parse_stable_family_vote(
                state_dir=state_dir,
                state_key=state_key,
                top_n=int(args.top_n_stable_families),
                max_cost_units=int(args.stable_lane_closure_max_cost_units),
            )
            packs.extend(st_family_packs)
            inputs.extend(st_family_inputs)

            # 2d) Stable family/lane vote packs v2 (optional; default-off)
            st_family_v2_packs, st_family_v2_inputs = _parse_stable_family_vote_v2(
                state_dir=state_dir,
                state_key=state_key,
                top_n=int(args.top_n_stable_families_v2),
                legacy_top_n=int(args.top_n_stable_families),
                max_cost_units=int(args.stable_lane_closure_max_cost_units),
                arena_payload=stable_arena_payload,
            )
            packs.extend(st_family_v2_packs)
            inputs.extend(st_family_v2_inputs)

            # 2e) Stable last-remaining survivor packs (optional; default-off)
            st_survivor_packs, st_survivor_inputs = _parse_stable_last_remaining(
                state_dir=state_dir,
                state_key=state_key,
                top_n=int(args.top_n_stable_last_remaining),
                max_cost_units=int(args.stable_lane_closure_max_cost_units),
            )
            packs.extend(st_survivor_packs)
            inputs.extend(st_survivor_inputs)

            # 3) Digit Reduction analyzer v2 (top patterns per variant)
            dr_packs, dr_inputs = _parse_dr_top(
                state_dir=state_dir, state_key=state_key, top_n=int(args.top_n_dr)
            )
            packs.extend(dr_packs)
            inputs.extend(dr_inputs)

            # 3b) Digit Reduction envelope packs (optional; v0.3 prework)
            dr_env_packs, dr_env_inputs = _parse_dr_envelope_steps(
                state_dir=state_dir,
                state_key=state_key,
                boxed_canonicals=int(args.dr_envelope_boxed_canonicals),
            )
            packs.extend(dr_env_packs)
            inputs.extend(dr_env_inputs)

            # 3c) Digit Reduction DR-004 packs (optional; default-off)
            want_dr004_signals = bool(
                args.dr004_write_signals or args.write_signals_bundle or int(args.fusion_gate_boxed_canonicals) > 0
            )
            dr004_signals: Optional[Dict[str, Any]] = {} if want_dr004_signals else None
            dr004_packs, dr004_inputs = _parse_dr004_steps(
                state_dir=state_dir,
                state_key=state_key,
                boxed_canonicals=int(args.dr004_boxed_canonicals),
                index_boxed_canonicals=int(args.dr004_index_boxed_canonicals),
                recent_draws=int(args.dr004_recent_draws),
                max_cost_units=int(args.dr004_max_cost_units),
                min_unique_digits=int(args.dr004_min_unique_digits),
                max_unique_digits=int(args.dr004_max_unique_digits),
                signals_out=dr004_signals,
                signals_top_pools=int(args.dr004_signals_top_pools),
                signals_top_canonicals=int(args.dr004_signals_top_canonicals),
                signals_top_indices=int(args.dr004_signals_top_indices),
            )
            packs.extend(dr004_packs)
            inputs.extend(dr004_inputs)
            if args.dr004_write_signals and dr004_signals:
                sig_path = state_dir / f"dr004_signals{out_suffix}{tag_suffix}.json"
                sig_payload: Dict[str, Any] = {
                    **dr004_signals,
                    "results_date": args.date,
                    "history_date": cc_meta.history_date,
                    "profile": profile,
                    "experiment_tag": exp_tag,
                    "sharepacks_root": _safe_rel(sharepacks_root),
                    "sharepack_state_dir": _safe_rel(state_dir),
                    "contains_winners_artifacts": bool(leakage),
                }
                _write_json(sig_path, sig_payload)
                print(f"Wrote: {_safe_rel(sig_path)}")

            # 4) VTRAC enhanced (top straights)
            vt_packs, vt_inputs = _parse_vtrac_top(
                state_dir=state_dir, state_key=state_key, top_n=int(args.top_n_vtrac)
            )
            packs.extend(vt_packs)
            inputs.extend(vt_inputs)

            # 5) Hot Zones (top triads)
            hz_packs, hz_inputs = _parse_hot_zones_top(
                state_dir=state_dir, state_key=state_key, date=args.date, top_n=int(args.top_n_hot)
            )
            packs.extend(hz_packs)
            inputs.extend(hz_inputs)

            # 5b) Hot Zones (optional index-closure conversion pack; bounded)
            if args.hot_zones_index_closure:
                hzic_packs, hzic_inputs = _parse_hot_zones_index_closure(
                    state_dir=state_dir,
                    state_key=state_key,
                    date=args.date,
                    seed_top_n=int(args.top_n_hot),
                    top_box_canonicals=int(args.hot_zones_index_closure_boxed_canonicals),
                )
                packs.extend(hzic_packs)
                inputs.extend(hzic_inputs)

            # 6) Aux (positional shortlist)
            aux_packs, aux_inputs = _parse_aux_top(
                state_dir=state_dir, state_key=state_key, top_n=int(args.top_n_aux)
            )
            packs.extend(aux_packs)
            inputs.extend(aux_inputs)

            # 6b) Aux (overdue VTRAC indices; index-closure packs)
            aux_vt_packs, aux_vt_inputs = _parse_aux_vtrac_indices(
                state_dir=state_dir, state_key=state_key, top_n=int(args.top_n_aux_vtrac_indices)
            )
            packs.extend(aux_vt_packs)
            inputs.extend(aux_vt_inputs)

            # 6c) Blackapple (ALERT-only; optional; bounded STRAIGHT packs)
            ba_packs, ba_inputs = _parse_blackapple_alert_packs(
                state_dir=state_dir,
                state_key=state_key,
                top_n=int(args.top_n_blackapple),
                min_score=int(args.blackapple_min_score),
            )
            packs.extend(ba_packs)
            inputs.extend(ba_inputs)

            # 6d) Fusion gate (optional; bounded; derived from tool signals + DR-004)
            if int(args.fusion_gate_boxed_canonicals) > 0:
                st_sig, _ = _extract_stable_signals(
                    state_dir=state_dir, state_key=state_key, top_n=int(args.top_n_stable)
                )
                hz_sig, _ = _extract_hot_zones_signals(
                    state_dir=state_dir, state_key=state_key, date=args.date, top_n=int(args.top_n_hot)
                )
                vt_sig, _ = _extract_vtrac_enhanced_signals(
                    state_dir=state_dir,
                    state_key=state_key,
                    top_indices=int(args.top_n_vtrac_indices),
                    top_straights=int(args.top_n_vtrac),
                )
                aux_sig, _ = _extract_aux_signals(
                    state_dir=state_dir,
                    state_key=state_key,
                    top_shortlist=int(args.top_n_aux),
                    top_overdue=int(args.top_n_aux_vtrac_indices),
                )
                fg_packs = _build_fusion_gate_dr004_packs(
                    state_key=state_key,
                    dr004_signals=dr004_signals or {},
                    stable_signals=st_sig,
                    hot_zones_signals=hz_sig,
                    vtrac_signals=vt_sig,
                    aux_signals=aux_sig,
                    boxed_canonicals=int(args.fusion_gate_boxed_canonicals),
                    min_sources=int(args.fusion_gate_min_sources),
                )
                packs.extend(fg_packs)

        # 7) Digit envelope (always recorded; derived packs only for non-profit_only profiles)
        digit_envelopes: List[dict] = []
        envelope = _build_digit_envelope(packs=packs)
        digit_envelopes.append(envelope)

        if profile != "profit_only":
            # 7b) COMBINATION_FORMING3 consensus double-trigger pack (CONSENSUS9)
            if not args.skip_consensus_double_pack:
                consensus_pack, consensus_inputs = _build_consensus_double_pack(
                    state_dir=state_dir,
                    state_key=state_key,
                    packs=packs,
                    envelope=envelope,
                    stable_additions_n=int(args.consensus_stable_additions),
                )
                if consensus_pack:
                    packs.append(consensus_pack)
                inputs.extend(consensus_inputs)

            # 7c) Mirror-pair closure packs (bounded; mirror-double conversion helper)
            mp_packs, mp_inputs = _build_mirror_pair_closure_packs(
                state_dir=state_dir,
                state_key=state_key,
                envelope=envelope,
                top_pairs=int(args.mirror_pair_closure_pairs),
                top_thirds=int(args.top_n_mirror_pair_closure),
            )
            packs.extend(mp_packs)
            inputs.extend(mp_inputs)

            # 7d) Mirror-pair closure packs seeded from Control Center Due Doubles families (optional; additive)
            mpdd_packs, mpdd_inputs = _build_mirror_pair_closure_due_doubles_packs(
                day_dir=day_dir,
                state_dir=state_dir,
                state_key=state_key,
                envelope=envelope,
                top_pairs=int(args.mirror_pair_closure_due_doubles_pairs),
                top_thirds=int(args.top_n_mirror_pair_closure_due_doubles),
            )
            packs.extend(mpdd_packs)
            inputs.extend(mpdd_inputs)

            if not args.skip_combo_packs:
                combo_packs = _build_combo_packs_from_envelope(envelope=envelope)
                packs.extend(combo_packs)

        # Stabilize ordering and fill missing evidence_paths for combo packs.
        for p in packs:
            p.setdefault("evidence_paths", [])
            p["evidence_paths"] = sorted(set(p["evidence_paths"]))
            p["why_tags"] = [str(x) for x in p.get("why_tags", []) if str(x)]

        packs.sort(key=lambda p: p.get("pack_id", ""))

        union_combos, union_count = _collect_union(packs)
        inputs_rel = sorted(set(_safe_rel(p) for p in inputs))
        inputs_hash = _hash_inputs(inputs)

        payload = {
            "schema_version": SCHEMA_VERSION,
            "generated_at": _now_iso(),
            "results_date": args.date,
            "history_date": cc_meta.history_date,
            "profile": profile,
            "experiment_tag": exp_tag,
            "state_key": state_key,
            "sharepack_root": _safe_rel(sharepacks_root),
            "sharepack_state_dir": _safe_rel(state_dir),
            "mirror_scheme": MIRROR_SCHEME,
            "contains_winners_artifacts": bool(leakage),
            "leakage_checks": [
                "state:winners_dir",
                "state:vtrac/validation_report.*",
                "day:vtrac_compact_report.* and vtrac payload zips",
                "day:control_center/profit_alerts_eval.*",
            ],
            "leakage_issues": leakage,
            "inputs": inputs_rel,
            "inputs_hash": inputs_hash,
            "digit_envelopes": digit_envelopes,
            "packs": packs,
            "union_combos": union_combos,
            "union_combos_count": union_count,
            "control_center_meta": {
                "history_excel_path": cc_meta.history_excel_path,
                "results_file": cc_meta.results_file,
            },
        }

        if args.write_signals_bundle and include_non_profit:
            bundle_path = state_dir / f"signals_bundle{out_suffix}{tag_suffix}.json"
            if bundle_path.exists() and not args.force:
                raise SystemExit(
                    f"Refusing to overwrite existing signals bundle: {_safe_rel(bundle_path)} (use --force)"
                )
            st_sig, _ = _extract_stable_signals(
                state_dir=state_dir, state_key=state_key, top_n=int(args.top_n_stable)
            )
            hz_sig, _ = _extract_hot_zones_signals(
                state_dir=state_dir, state_key=state_key, date=args.date, top_n=int(args.top_n_hot)
            )
            vt_sig, _ = _extract_vtrac_enhanced_signals(
                state_dir=state_dir,
                state_key=state_key,
                top_indices=int(args.top_n_vtrac_indices),
                top_straights=int(args.top_n_vtrac),
            )
            aux_sig, _ = _extract_aux_signals(
                state_dir=state_dir,
                state_key=state_key,
                top_shortlist=int(args.top_n_aux),
                top_overdue=int(args.top_n_aux_vtrac_indices),
            )
            aux_badge_sig = aux_badge_sig_cached
            if aux_badge_sig is None:
                aux_badge_sig, _ = _extract_aux_badge_pressure_signals(
                    state_dir=state_dir, state_key=state_key, top_k=max(5, int(args.aux_cc_arena_top_items))
                )
            aux_cc_sig = aux_cc_sig_cached or {"available": False, "evidence_paths": [], "arena_objects": {}}
            bundle_payload: Dict[str, Any] = {
                "schema": "signals_bundle_v1",
                "generated_at": _now_iso(),
                "results_date": args.date,
                "history_date": cc_meta.history_date,
                "profile": profile,
                "experiment_tag": exp_tag,
                "state_key": state_key,
                "sharepack_root": _safe_rel(sharepacks_root),
                "sharepack_state_dir": _safe_rel(state_dir),
                "contains_winners_artifacts": bool(leakage),
                "candidate_universe_path": _safe_rel(out_path),
                "candidate_universe_inputs_hash": inputs_hash,
                "tools": {
                    "digit_reduction_dr004": dr004_signals or {"available": False},
                    "stable": st_sig,
                    "hot_zones": hz_sig,
                    "vtrac_enhanced": vt_sig,
                    "aux": aux_sig,
                    "aux_badge_pressure": aux_badge_sig,
                    "aux_control_center_context": aux_cc_sig,
                },
            }
            _write_json(bundle_path, bundle_payload)
            print(f"Wrote: {_safe_rel(bundle_path)}")

        _write_json(out_path, payload)
        if args.write_md:
            md_path = state_dir / f"candidate_universe{out_suffix}{tag_suffix}.md"
            _write_candidate_universe_md(out_path=md_path, payload=payload)
            print(f"Wrote: {_safe_rel(md_path)}")
        if args.write_evidence:
            ev_csv = state_dir / f"candidate_universe_evidence{out_suffix}{tag_suffix}.csv"
            ev_md = state_dir / f"candidate_universe_evidence{out_suffix}{tag_suffix}.md"
            _write_candidate_universe_evidence_csv(out_path=ev_csv, payload=payload)
            _write_candidate_universe_evidence_md(out_path=ev_md, payload=payload)
            print(f"Wrote: {_safe_rel(ev_csv)}")
            print(f"Wrote: {_safe_rel(ev_md)}")
        if args.write_stable_arena:
            if stable_arena_payload is None:
                print(f"Skipped stable arena: missing Stable bundle for {_safe_rel(state_dir)}")
            else:
                arena_json, arena_md = write_stable_arena_files(
                    out_json_path=arena_path,
                    payload=stable_arena_payload,
                    write_md=True,
                )
                print(f"Wrote: {_safe_rel(arena_json)}")
                if arena_md is not None:
                    print(f"Wrote: {_safe_rel(arena_md)}")
        if args.write_dr_arena:
            if dr_arena_payload is None:
                print(f"Skipped DR arena: missing Digit Reduction bundle for {_safe_rel(state_dir)}")
            else:
                arena_json, arena_md = write_dr_arena_files(
                    out_json_path=dr_arena_path,
                    payload=dr_arena_payload,
                    write_md=True,
                )
                print(f"Wrote: {_safe_rel(arena_json)}")
                if arena_md is not None:
                    print(f"Wrote: {_safe_rel(arena_md)}")
        if args.write_aux_cc_arena:
            if aux_cc_arena_payload is None:
                print(f"Skipped Aux/CC arena: missing Aux / Control Center artifacts for {_safe_rel(state_dir)}")
            else:
                arena_json, arena_md = write_aux_control_center_files(
                    out_json_path=aux_cc_arena_path,
                    payload=aux_cc_arena_payload,
                    write_md=True,
                )
                print(f"Wrote: {_safe_rel(arena_json)}")
                if arena_md is not None:
                    print(f"Wrote: {_safe_rel(arena_md)}")
        print(f"Wrote: {_safe_rel(out_path)} (packs={len(packs)} union={union_count})")


if __name__ == "__main__":
    main()
