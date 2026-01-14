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
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

try:
    from modules.vtrac_reference import get_index_set as _vtrac_get_index_set  # type: ignore
except Exception:  # pragma: no cover - may fail in partial environments
    _vtrac_get_index_set = None  # type: ignore


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
        default="mixed",
        help="Ablation profile for pack sources (default: mixed). tool_only = skip profit_alerts packs; profit_only = profit_alerts packs only.",
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
    ap.add_argument("--top-n-dr", type=int, default=3, help="Top N DR analyzer patterns per variant (default: 3)")
    ap.add_argument("--top-n-vtrac", type=int, default=8, help="Top N VTRAC straights (default: 8)")
    ap.add_argument("--top-n-hot", type=int, default=8, help="Top N Hot Zones triads (default: 8)")
    ap.add_argument("--top-n-aux", type=int, default=10, help="Top N Aux positional shortlist combos (default: 10)")
    ap.add_argument(
        "--top-n-aux-vtrac-indices",
        type=int,
        default=2,
        help="Top N Aux overdue VTRAC indices per variant to include as index-closure packs (default: 2; 0 disables).",
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
    include_profit_alerts = profile in {"mixed", "profit_only"}
    include_non_profit = profile in {"mixed", "tool_only"}

    for state_key in states:
        state_dir = day_dir / state_key
        if not state_dir.exists():
            raise SystemExit(f"Missing state dir: {_safe_rel(state_dir)}")

        out_path = state_dir / f"candidate_universe{out_suffix}.json"
        if out_path.exists() and not args.force:
            raise SystemExit(
                f"Refusing to overwrite existing candidate universe: {_safe_rel(out_path)} (use --force)"
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

            # 3) Digit Reduction analyzer v2 (top patterns per variant)
            dr_packs, dr_inputs = _parse_dr_top(
                state_dir=state_dir, state_key=state_key, top_n=int(args.top_n_dr)
            )
            packs.extend(dr_packs)
            inputs.extend(dr_inputs)

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

        _write_json(out_path, payload)
        if args.write_md:
            md_path = state_dir / f"candidate_universe{out_suffix}.md"
            _write_candidate_universe_md(out_path=md_path, payload=payload)
            print(f"Wrote: {_safe_rel(md_path)}")
        print(f"Wrote: {_safe_rel(out_path)} (packs={len(packs)} union={union_count})")


if __name__ == "__main__":
    main()
