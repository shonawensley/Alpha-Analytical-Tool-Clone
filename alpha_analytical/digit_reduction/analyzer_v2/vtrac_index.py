from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

import json
from collections import defaultdict

from .clustering import Cluster

# Canonical digit → V-family mapping used across AAT9 (0/5→1, 1/6→2, 2/7→3, 3/8→4, 4/9→5)
VTRAC_MAP = {
    "0": "1",
    "5": "1",
    "1": "2",
    "6": "2",
    "2": "3",
    "7": "3",
    "3": "4",
    "8": "4",
    "4": "5",
    "9": "5",
}

MIRROR = {
    "0": "5",
    "5": "0",
    "1": "6",
    "6": "1",
    "2": "7",
    "7": "2",
    "3": "8",
    "8": "3",
    "4": "9",
    "9": "4",
}


def _digits(value: str) -> List[str]:
    return [ch for ch in value if ch.isdigit()]


def _sanitize_trigram(value: str) -> str:
    digits = _digits(value)
    return "".join(digits[:3]) if len(digits) >= 3 else ""


def _family_key(value: str) -> str:
    return "".join(sorted(set(_digits(value))))


def _expand_family(trigram: str) -> Set[str]:
    tri = _sanitize_trigram(trigram)
    if len(tri) != 3:
        return set()
    a_options = {tri[0], MIRROR.get(tri[0], tri[0])}
    b_options = {tri[1], MIRROR.get(tri[1], tri[1])}
    c_options = {tri[2], MIRROR.get(tri[2], tri[2])}
    expansions: Set[str] = set()
    for a in a_options:
        for b in b_options:
            for c in c_options:
                expansions.add("".join((a, b, c)))
    return expansions


def to_vtrac_str(value: str) -> str:
    return "".join(VTRAC_MAP.get(ch, "") for ch in _digits(value))


def vtrac_set(value: str) -> str:
    families = set(to_vtrac_str(value))
    return "".join(sorted(families))


@dataclass(slots=True)
class VHotSpec:
    families: Set[str]
    source: str
    detail: Dict[str, float]


class VtracIndex:
    """
    Tracks exact permutations and their V-TRAC families so cluster membership
    can be evaluated quickly.
    """

    def __init__(self, exact: Iterable[str], family: Dict[str, Set[str]]):
        self._exact: Set[str] = { _sanitize_trigram(v) for v in exact if len(_sanitize_trigram(v)) == 3 }
        self._exact.discard("")
        self._family: Dict[str, Set[str]] = {k: set(v) for k, v in family.items()}

    @classmethod
    def from_winner_permutations(
        cls,
        permutations: Sequence[str],
        extra_family_seeds: Sequence[str] | None = None,
    ) -> "VtracIndex":
        exact: Set[str] = set()
        lookup: Dict[str, Set[str]] = defaultdict(set)

        def add_seed(seed: str) -> None:
            cleaned = _sanitize_trigram(seed)
            if len(cleaned) != 3:
                return
            exact.add(cleaned)
            key = _family_key(cleaned)
            if not key:
                return
            lookup[key].update(_expand_family(cleaned))

        for perm in permutations:
            add_seed(perm)
        if extra_family_seeds:
            for seed in extra_family_seeds:
                add_seed(seed)

        # Ensure all exact permutations are included in the family cache
        for perm in list(exact):
            key = _family_key(perm)
            if key:
                lookup[key].add(perm)

        return cls(exact=exact, family=lookup)

    def is_exact(self, trigram: str) -> bool:
        cleaned = _sanitize_trigram(trigram)
        return len(cleaned) == 3 and cleaned in self._exact

    def is_vtrac(self, trigram: str) -> bool:
        cleaned = _sanitize_trigram(trigram)
        if len(cleaned) != 3:
            return False
        key = _family_key(cleaned)
        if not key:
            return False
        family = self._family.get(key)
        return bool(family and cleaned in family)

    def cluster_membership(self, cluster: Cluster) -> Dict[str, bool]:
        exact_hit = False
        vtrac_hit = False
        for trigram in cluster.iter_trigrams():
            if not exact_hit and self.is_exact(trigram):
                exact_hit = True
            if not vtrac_hit and self.is_vtrac(trigram):
                vtrac_hit = True
            if exact_hit and vtrac_hit:
                break
        is_three_value = cluster.unique_count == 3
        return {
            "exact": exact_hit,
            "vtrac": vtrac_hit,
            "three_value_exact": exact_hit and is_three_value,
            "three_value_vtrac": vtrac_hit and is_three_value,
        }


# ---------- Hot-family helpers (optional synergy) ----------

def _latest_prediction_json(pred_dir: Path, state: str) -> Optional[Path]:
    if not pred_dir.exists():
        return None
    candidates: List[Tuple[float, Path]] = []
    pattern = f"*{state}*"
    for path in pred_dir.glob(pattern):
        if path.suffix.lower() not in {".json"}:
            continue
        try:
            candidates.append((path.stat().st_mtime, path))
        except OSError:
            continue
    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][1]


def _extract_indices(payload: dict) -> List[int]:
    if not isinstance(payload, dict):
        return []
    if isinstance(payload.get("top_indices"), list):
        results = []
        for item in payload["top_indices"]:
            idx = item.get("index") or item.get("id") or item.get("idx")
            if isinstance(idx, int):
                results.append(idx)
        if results:
            return results
    if isinstance(payload.get("ranked"), list):
        results = []
        for item in payload["ranked"]:
            idx = item.get("index") or item.get("id") or item.get("idx")
            if isinstance(idx, int):
                results.append(idx)
        if results:
            return results
    if isinstance(payload.get("indices"), dict):
        results = []
        for key in payload["indices"].keys():
            try:
                results.append(int(key))
            except (TypeError, ValueError):
                continue
        return results
    return []


def _indices_to_families(indices: Iterable[int]) -> Set[str]:
    # Placeholder until a canonical mapping table is wired in.
    return set()


def try_load_hot_families_from_predictions(state: str, predictions_dir: Path) -> Optional[VHotSpec]:
    latest = _latest_prediction_json(predictions_dir, state)
    if not latest:
        return None
    try:
        payload = json.loads(latest.read_text(encoding="utf-8"))
    except Exception:
        return None
    indices = _extract_indices(payload)
    families = _indices_to_families(indices)
    if not families:
        return None
    return VHotSpec(families=families, source="predictions_json", detail={fam: 1.0 for fam in families})


def derive_hot_families_from_dr(
    rows: Iterable[Dict[str, any]],
    min_methods: int = 2,
    prefer_section: str = "Combined",
    top_k: int = 5,
) -> VHotSpec:
    bucket: Dict[str, Dict[str, int]] = defaultdict(lambda: {"count": 0, "methods": 0, "sections": 0, "cols": 0, "sets": 0, "pref": 0})
    seen: Set[Tuple[str, ...]] = set()
    for row in rows:
        sig = str(row.get("final_3canon") or "")
        if not sig:
            continue
        fam = vtrac_set(sig)
        if not fam:
            continue
        key = (
            str(row.get("area", "")),
            str(row.get("section", "")),
            str(row.get("set", "")),
            str(row.get("draw", "")),
            str(row.get("col", "")),
            str(row.get("mode", "")),
            str(row.get("method", "")),
            sig,
        )
        if key in seen:
            continue
        seen.add(key)
        metrics = bucket[fam]
        metrics["count"] += 1
        metrics["methods"] += 1
        metrics["sections"] += 1
        metrics["cols"] += 1
        metrics["sets"] += 1
        if str(row.get("section")) == prefer_section:
            metrics["pref"] += 1

    if not bucket:
        return VHotSpec(families=set(), source="none", detail={})

    scores: Dict[str, float] = {}
    for fam, metrics in bucket.items():
        scores[fam] = (
            1.0 * metrics["count"]
            + 0.5 * metrics["methods"]
            + 0.5 * metrics["cols"]
            + 0.5 * metrics["sets"]
            + 0.6 * metrics["pref"]
        )

    ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)[: max(1, top_k)]
    peak = max(score for _, score in ranked) or 1.0
    detail = {fam: score / peak for fam, score in ranked}
    return VHotSpec(families=set(detail.keys()), source="derived_from_DR", detail=detail)
