from __future__ import annotations

import json
from dataclasses import dataclass, field
from itertools import permutations
from statistics import mean
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

from .clustering import (
    Cluster,
    contiguous_runs,
    drop_variants,
    extract_clusters,
    iter_trigrams,
)
from .types import Item, Step, Key
from .vtrac_index import VtracIndex, vtrac_set


DetectionKind = str

DETECTION_KINDS: Tuple[DetectionKind, ...] = (
    "exact",
    "vtrac",
    "drop_exact",
    "drop_vtrac",
    "family_exact",
    "family_vtrac",
)


def _digits(value: str) -> List[str]:
    return [ch for ch in value if ch.isdigit()]


def _sanitize(value: str) -> str:
    return "".join(_digits(value))


def _first_step_with_len(steps: Sequence[Step], minimum: int) -> Optional[Step]:
    for step in steps:
        digits = _digits(step.value)
        if len(digits) >= minimum:
            return step
    return None


def _distinct_triplet(step: Optional[Step]) -> Tuple[str, List[str]]:
    if step is None:
        return "", []
    digits = _digits(step.value)
    if len(digits) < 3:
        return "", digits
    triplet = "".join(digits[:3])
    return triplet, digits


def _unique_sorted_with_dupes(digits: Sequence[str]) -> str:
    return "".join(sorted(digits))


def _permutation_set(triplet: str) -> Set[str]:
    if len(triplet) != 3:
        return set()
    return {"".join(p) for p in permutations(triplet, 3)}


def _is_three_value_family(cluster: Cluster, family_digits: Sequence[str]) -> bool:
    if not family_digits:
        return False
    family_set = set(family_digits)
    return set(cluster.text) <= family_set


@dataclass
class DetectionStats:
    steps: List[int] = field(default_factory=list)
    earliest: Optional[int] = None
    final_match: bool = False
    drop_records: List[Tuple[str, int]] = field(default_factory=list)

    def register(self, step_number: int, is_final: bool, drop_digit: Optional[str] = None, drop_len: Optional[int] = None) -> None:
        if self.earliest is None or step_number < self.earliest:
            self.earliest = step_number
        if step_number not in self.steps:
            self.steps.append(step_number)
        if is_final:
            self.final_match = True
        if drop_digit is not None:
            self.drop_records.append((drop_digit, drop_len or 0))

    @property
    def persistence(self) -> int:
        return len(self.steps)

    def serialize(self) -> Dict[str, Any]:
        return {
            "steps": self.steps,
            "earliest": self.earliest if self.earliest is not None else -1,
            "final_match": self.final_match,
            "drop_records": self.drop_records,
        }


@dataclass
class ItemFeature:
    row: Dict[str, Any]
    detail: Dict[str, Any]


class ItemFeatureBuilder:
    def __init__(self, item: Item, config: Dict[str, Any]):
        self.item = item
        self.config = config or {}
        cluster_cfg = self.config.get("features", {}).get("cluster_scan", {})
        self.cluster_min = int(cluster_cfg.get("min_len", 3))
        self.cluster_max = int(cluster_cfg.get("max_len", 12))
        self.steps = item.steps or []
        self.final_step = self.steps[-1] if self.steps else None
        self.triplet_step = _first_step_with_len(self.steps, 3)
        triplet, final_digits = _distinct_triplet(self.triplet_step)
        self.triplet = triplet
        self.final_digits = final_digits
        self.permutations = _permutation_set(self.triplet)
        self.family_sorted = _unique_sorted_with_dupes(list(self.triplet))
        self.family_unique = "".join(sorted(set(self.triplet)))
        self.vtrac_key = vtrac_set(self.triplet)
        self.v_index = VtracIndex.from_winner_permutations(self.permutations, self.permutations)
        self.final_step_digits = _digits(self.final_step.value) if self.final_step else []

        self.detections: Dict[DetectionKind, DetectionStats] = {
            kind: DetectionStats() for kind in DETECTION_KINDS
        }
        self.family_mass_values: List[float] = []
        self.family_run_lengths: List[int] = []
        self.drop_records_all: List[Tuple[str, int, int]] = []
        self.cluster_lengths: List[int] = []
        self.extended_cluster = False
        # Progression (extended Set1 ladder proximity)
        self.progress_score = self._ladder_proximity(self.item.key)

    def build(self) -> ItemFeature:
        row = self._base_row()
        if not self.steps or not self.triplet:
            row["features_json"] = json.dumps({}, sort_keys=True)
            return ItemFeature(row=row, detail={})

        self._scan_steps()
        self._populate_row(row)
        detail = {
            "detections": {kind: stats.serialize() for kind, stats in self.detections.items()},
            "family_mass": self.family_mass_values,
            "family_runs": self.family_run_lengths,
            "drop_records": self.drop_records_all,
            "cluster_lengths": self.cluster_lengths,
        }
        row["features_json"] = json.dumps(detail, sort_keys=True)
        return ItemFeature(row=row, detail=detail)

    def _base_row(self) -> Dict[str, Any]:
        key = self.item.key
        grid = self.item.grid_position or {}
        box_id = _sanitize(self.steps[0].value) if self.steps else ""
        row = {
            "state": key.state,
            "area": key.area,
            "section": key.section,
            "set": key.set,
            "draw": key.draw,
            "col": key.col,
            "method": key.method,
            "mode": key.mode,
            "variant": key.section,
            "box_id": box_id,
            "area_rank": grid.get("area_rank"),
            "section_rank": grid.get("section_rank"),
            "set_rank": grid.get("set_rank"),
            "draw_rank": grid.get("draw_rank"),
            "col_rank": grid.get("col_rank"),
            "pattern": self.triplet,
            "family_id": self.family_sorted,
            "family_unique": self.family_unique,
            "vtrac_key": self.vtrac_key,
            "final_value": _sanitize(self.final_step.value) if self.final_step else "",
            "is_extended_cluster": False,
            # Extended ladder proximity (add-only, weight-gated)
            "ls2_progress": self.progress_score,
        }
        return row

    def _ladder_proximity(self, key: Key) -> float:
        """
        Heuristic proximity score for extended Set1 ladder boxes (Draw2–Draw7 cols 6→1).
        Nearer to current (lower draw index / lower col) gets a slightly higher value.
        Returns 0.0 for non-Set1 or non-extended ladder boxes.
        """
        if key.set != "Set1":
            return 0.0
        try:
            draw_num = int(str(key.draw).replace("Draw", ""))
            col_num = int(key.col)
        except Exception:
            return 0.0
        if draw_num < 2 or draw_num > 7 or col_num < 1 or col_num > 6:
            return 0.0
        draw_term = max(0, 7 - draw_num) / 5.0   # Draw2→1.0, Draw7→0
        col_term = max(0, 6 - col_num) / 5.0     # col1→1.0, col6→0
        return round(0.5 * draw_term + 0.5 * col_term, 4)

    def _scan_steps(self) -> None:
        family_set = set(self.triplet)
        for step in self.steps:
            digits = _sanitize(step.value)
            if not digits:
                continue
            clusters = extract_clusters(digits, self.cluster_min, self.cluster_max)
            self.cluster_lengths.extend(cluster.length for cluster in clusters)
            self._record_family_mass(digits, family_set)
            self._record_family_runs(digits, family_set)
            self._register_detection(step, digits, clusters)
        if self.final_step:
            final_clusters = extract_clusters(_sanitize(self.final_step.value), self.cluster_min, self.cluster_max)
            if any(cluster.length > 3 for cluster in final_clusters):
                self.extended_cluster = True
        if len(self.final_step_digits) > 3:
            self.extended_cluster = True

    def _record_family_mass(self, digits: str, family_set: Set[str]) -> None:
        if not digits:
            return
        total = len(digits)
        inside = sum(1 for ch in digits if ch in family_set)
        self.family_mass_values.append(inside / total if total else 0.0)

    def _record_family_runs(self, digits: str, family_set: Set[str]) -> None:
        runs = [
            run_len for _, run_len, digit in ((start, end - start, d) for start, end, d in contiguous_runs(digits))
            if digit in family_set
        ]
        if runs:
            self.family_run_lengths.append(max(runs))

    def _register_detection(self, step: Step, digits: str, clusters: List[Cluster]) -> None:
        step_number = step.step + 1
        is_final = self.final_step is not None and step_number == self.final_step.step
        trigram_hits = list(iter_trigrams(digits))

        if self.permutations and any(tri in self.permutations for tri in trigram_hits):
            self.detections["exact"].register(step_number, is_final)
        if any(self.v_index.is_vtrac(tri) for tri in trigram_hits):
            self.detections["vtrac"].register(step_number, is_final)

        unique_trip = "".join(dict.fromkeys(digits))
        if len(unique_trip) >= 3:
            unique_tris = [unique_trip[idx : idx + 3] for idx in range(len(unique_trip) - 2)]
            if self.permutations and any(tri in self.permutations for tri in unique_tris):
                self.detections["exact"].register(step_number, is_final)
            if any(self.v_index.is_vtrac(tri) for tri in unique_tris):
                self.detections["vtrac"].register(step_number, is_final)

        for collapsed, digit, run_len in drop_variants(digits):
            if not collapsed:
                continue
            collapsed_trigrams = list(iter_trigrams(collapsed))
            drop_registered = False
            if self.permutations and any(tri in self.permutations for tri in collapsed_trigrams):
                self.detections["drop_exact"].register(step_number, is_final, digit, run_len)
                drop_registered = True
            if any(self.v_index.is_vtrac(tri) for tri in collapsed_trigrams):
                self.detections["drop_vtrac"].register(step_number, is_final, digit, run_len)
                drop_registered = True
            self.drop_records_all.append((digit, run_len, step_number))
            if drop_registered:
                self.drop_records_all[-1] = (digit, run_len, step_number)

        family_digits = list(self.triplet)
        family_vkey = self.vtrac_key
        for cluster in clusters:
            if not cluster.text:
                continue
            if _is_three_value_family(cluster, family_digits):
                self.detections["family_exact"].register(step_number, is_final)
            if family_vkey and vtrac_set(cluster.text) == family_vkey:
                self.detections["family_vtrac"].register(step_number, is_final)

    def _populate_row(self, row: Dict[str, Any]) -> None:
        def get_stat(name: DetectionKind) -> DetectionStats:
            return self.detections.get(name, DetectionStats())

        for kind in DETECTION_KINDS:
            stats = get_stat(kind)
            row[f"earliest_{kind}_step"] = stats.earliest if stats.earliest is not None else -1
            row[f"persistence_{kind}"] = stats.persistence
            row[f"final_{kind}_match"] = int(stats.final_match)

        density = max(self.family_mass_values) if self.family_mass_values else 0.0
        row["box_family_density"] = float(density)
        max_run = max(self.family_run_lengths) if self.family_run_lengths else 0
        row["dup_bonus_raw"] = max_run
        row["dup_bonus"] = float(max(0, max_run - 1))
        row["residual_purity"] = self._residual_purity()

        drop_digit, drop_len, drop_mode, drop_mode_strength = self._drop_metadata()
        row["drop_digit"] = drop_digit or ""
        row["drop_run_len"] = drop_len
        row["drop_digit_mode"] = drop_mode or ""
        row["drop_digit_mode_stability"] = drop_mode_strength

        row.setdefault("cols_hit", 0)
        row.setdefault("variants_hit", 0)
        row.setdefault("method_consensus", 0)
        row.setdefault("cluster_echo_count", 0)
        row.setdefault("variant_echo_count", 0)
        row.setdefault("set_echo_count", 0)
        row.setdefault("recency_carryover", 0)
        row.setdefault("box_pair_agree", 0)
        row["is_extended_cluster"] = bool(self.extended_cluster)

    def _residual_purity(self) -> int:
        if not self.final_step:
            return 0
        digits = set(_digits(self.final_step.value))
        family_set = set(self.triplet)
        residual = digits - family_set
        return len(residual)

    def _drop_metadata(self) -> Tuple[Optional[str], int, Optional[str], int]:
        def _mode_with_len(records: Sequence[Tuple[str, int]]) -> Tuple[Optional[str], int, int]:
            if not records:
                return None, 0, 0
            stats: Dict[str, Tuple[int, int]] = {}
            for digit, run_len in records:
                freq, best_len = stats.get(digit, (0, 0))
                freq += 1
                best_len = max(best_len, run_len or 0)
                stats[digit] = (freq, best_len)

            def _priority(item: Tuple[str, Tuple[int, int]]) -> Tuple[int, int, int]:
                digit, (freq, best_len) = item
                # Prefer higher freq, longer runs, and deterministic digit ordering.
                return (freq, best_len, -ord(digit[0]) if digit else 0)

            digit_mode, (freq, best_len) = max(stats.items(), key=_priority)
            return digit_mode, best_len, freq

        def _scarce_digit(records: Sequence[Tuple[str, int, int]]) -> Tuple[Optional[str], int]:
            if not records:
                return None, 0
            stats: Dict[str, Tuple[int, int, int]] = {}
            for digit, run_len, step_number in records:
                freq, best_len, earliest = stats.get(digit, (0, 0, step_number))
                freq += 1
                best_len = max(best_len, run_len or 0)
                earliest = min(earliest, step_number)
                stats[digit] = (freq, best_len, earliest)

            def _priority(item: Tuple[str, Tuple[int, int, int]]) -> Tuple[int, int, int, int]:
                digit, (freq, best_len, earliest) = item
                # Prefer digits that disappear quickly (lower freq), surfaced earlier, then longer runs.
                return (freq, earliest, -best_len, ord(digit[0]) if digit else 0)

            digit_choice, (_, best_len, _) = min(stats.items(), key=_priority)
            return digit_choice, best_len

        drop_stats = (
            self.detections["drop_exact"].drop_records
            + self.detections["drop_vtrac"].drop_records
        )
        collapsed_all = [(digit, run_len) for digit, run_len, _ in self.drop_records_all]

        preferred_digit: Optional[str]
        preferred_len: int
        if self.drop_records_all:
            preferred_digit, preferred_len = _scarce_digit(self.drop_records_all)
        elif collapsed_all:
            preferred_digit, preferred_len, _ = _mode_with_len(collapsed_all)
        elif drop_stats:
            preferred_digit, preferred_len, _ = _mode_with_len(drop_stats)
        else:
            return None, 0, None, 0

        if preferred_digit is None:
            return None, 0, None, 0

        if drop_stats:
            mode_digit, _, mode_strength = _mode_with_len(drop_stats)
        else:
            mode_digit = preferred_digit
            mode_strength = 1
        return preferred_digit, preferred_len, mode_digit, mode_strength

def build_item_feature(item: Item, config: Dict[str, Any]) -> ItemFeature:
    builder = ItemFeatureBuilder(item, config)
    return builder.build()


def build_features(items: Iterable[Item], config: Dict[str, Any]) -> List[ItemFeature]:
    return [build_item_feature(item, config) for item in items]
