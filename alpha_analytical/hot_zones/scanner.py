from __future__ import annotations

import itertools
import itertools
from collections import defaultdict
from dataclasses import dataclass, asdict
from typing import DefaultDict, Dict, Iterable, List, Sequence, Set, Tuple

from .models import (
    TableEnv,
    HotScanConfig,
    SectionEntry,
    SetEntry,
    DrawEntry,
)
from .vtrac import (
    canonical_vtriad_from_string,
    has_vt_straight_lane,
    map_digits_to_v,
    MIRROR_MAP,
)

# --- helper dataclasses ---

@dataclass
class BoxRef:
    section: str
    set_name: str
    draw_name: str
    row_name: str
    column_index: int  # 1 == newest column
    is_starred: bool
    star_count: int
    is_set1: bool

@dataclass
class BoxData:
    ref: BoxRef
    draw_data: List[str]
    col_value: str | None
    s_raw: str
    vt_code: str
    s_mirror: str
    is_superhot_slot: bool
    hot_zone_count: int

@dataclass
class Evidence:
    triad: str
    vt_triad: str
    section: str
    set_name: str
    draw_name: str
    column_index: int
    row_hits: Dict[str, bool]
    has_straight: bool
    has_vt_straight: bool
    vt_only_lane: bool
    col1_arrival: bool
    precol1_funnel: bool
    ls_col_42: bool
    ls2_lane: bool
    is_starred: bool
    star_count: int
    is_superhot_slot: bool
    is_set1: bool
    is_literal_draw: bool
    guard_injected: bool

@dataclass
class PerItemRow:
    section: str
    set_name: str
    draw_name: str
    column_index: int
    triad: str
    vt_triad: str
    vertical_support: int
    horizontal_span: int
    set_span: int
    variant_echo: int
    has_straight: int
    has_vt_straight: int
    vt_only_lane: int
    col1_arrival: int
    precol1_funnel: int
    ls_col_42: int
    ls2_lane: int
    is_starred: int
    star_count: int
    is_superhot_slot: int
    is_set1: int
    guard_injected: int
    score: float
    reasons: str

@dataclass
class TopCandidateRow:
    triad: str
    vt_triad: str
    support_count: int
    hot_hits: int
    superhot_hits: int
    vertical_hits: int
    set1_hits: int
    col1_hits: int
    precol1_hits: int
    vt_straight_hits: int
    vt_only_lane_hits: int
    guard_hits: int
    literal_hits: int
    variant_span: int
    set_span: int
    column_span: int
    score_mean: float
    score_max: float
    evidence_tags: str

@dataclass
class HotZoneWeights:
    w_hot_star: float = 1.0
    w_superhot_set1: float = 2.25
    w_vertical_support: float = 0.6
    w_horizontal_span: float = 0.9
    w_set_span: float = 0.75
    w_variant_echo: float = 1.2
    w_vt_straight: float = 1.35
    w_exact_straight_lane: float = 1.1
    w_vt_only_lane_bonus: float = 0.8
    w_precol1_funnel: float = 2.1
    w_col1_arrival: float = 2.4
    w_ls_col_42: float = 0.5
    w_ls2_lane: float = 0.7
    w_set1_bias: float = 1.25
    w_literal_hit: float = 4.0
    w_guard_bonus: float = 3.0

# --- utilities ---

def _list_columns(row_values: Sequence[str]) -> List[Tuple[int, str]]:
    cols: List[Tuple[int, str]] = []
    for idx, value in enumerate(reversed(row_values), start=1):
        digits = "".join(ch for ch in value if ch.isdigit())
        cols.append((idx, digits))
    return cols

def _mirror_digit(ch: str) -> str:
    return MIRROR_MAP.get(ch, ch)

def _mirror_string(s: str) -> str:
    return "".join(_mirror_digit(ch) for ch in s if ch.isdigit())

def _extract_boxes(env: TableEnv, cfg: HotScanConfig) -> List[BoxData]:
    boxes: List[BoxData] = []
    for section in env.sections:
        if section.name not in cfg.consider_sections:
            continue
        for set_entry in section.sets:
            for draw in set_entry.draws:
                draw_values = list(draw.draw_data or [])
                for row_name, values in [
                    ("R2", draw.patterns.R2),
                    ("R4", draw.patterns.R4),
                    ("R6", draw.patterns.R6),
                    ("R8", draw.patterns.R8),
                ]:
                    for col_idx, digits in _list_columns(values):
                        if not digits:
                            continue
                        col_value = None
                        if draw_values and col_idx <= len(draw_values):
                            col_value = draw_values[-col_idx]
                        ref = BoxRef(
                            section=section.name,
                            set_name=set_entry.set_id,
                            draw_name=draw.draw_id,
                            row_name=row_name,
                            column_index=col_idx,
                            is_starred=draw.is_hot_zone,
                            star_count=draw.hot_zone_count,
                            is_set1=set_entry.set_id == "Set1",
                        )
                        vt_code = "".join(str(v) for v in map_digits_to_v(digits))
                        boxes.append(
                            BoxData(
                                ref=ref,
                                draw_data=list(draw.draw_data),
                                col_value=col_value,
                                s_raw=digits,
                                vt_code=vt_code,
                                s_mirror=_mirror_string(digits),
                                is_superhot_slot=ref.is_set1 and col_idx in (1, 2),
                                hot_zone_count=draw.hot_zone_count,
                            )
                        )
    return boxes

def _extract_candidate_triads(s: str) -> Set[str]:
    out: Set[str] = set()
    for i in range(0, max(0, len(s) - 2)):
        tri = s[i:i+3]
        if len(tri) == 3 and tri.isdigit():
            out.add("".join(sorted(tri)))
    # allow gap-1 subsequences
    for i in range(len(s)):
        a = s[i]
        if not a.isdigit():
            continue
        for j in (i + 1, i + 2):
            if j >= len(s):
                continue
            b = s[j]
            if not b.isdigit():
                continue
            for k in (j + 1, j + 2):
                if k >= len(s):
                    continue
                c = s[k]
                if not c.isdigit():
                    continue
                out.add("".join(sorted(a + b + c)))
    return out

def _detect_triad(triad: str, box: BoxData) -> Tuple[bool, bool]:
    perms = {"".join(p) for p in itertools.permutations(triad, 3)}
    literal_hit = any(p in box.s_raw for p in perms)
    vt, _ = canonical_vtriad_from_string(box.s_raw)
    vt_hit = has_vt_straight_lane(box.s_raw, vt) if vt else False
    return literal_hit, vt_hit

def _generate_guard_triads(row_boxes: List[BoxData]) -> Set[str]:
    if not row_boxes:
        return set()
    sample = row_boxes[0]
    if sample.ref.section != "Combined" or sample.ref.set_name != "Set1":
        return set()
    if sample.ref.column_index not in (1, 2):
        return set()
    if max((b.hot_zone_count for b in row_boxes), default=0) < 20:
        return set()
    digits: List[str] = []
    for b in row_boxes:
        digits.extend(ch for ch in b.s_raw if ch.isdigit())
    if len(digits) < 3:
        return set()
    guard: Set[str] = set()
    from itertools import combinations, product
    n = len(digits)
    indices = range(n)
    for idx_combo in combinations(indices, 3):
        substitution_choices = []
        for idx in idx_combo:
            d = digits[idx]
            mirrored = _mirror_digit(d)
            if mirrored == d:
                substitution_choices.append([d])
            else:
                substitution_choices.append([d, mirrored])
        for picks in product(*substitution_choices):
            guard.add("".join(sorted(picks)))
    return guard

def mine_evidence(boxes: List[BoxData], cfg: HotScanConfig) -> Dict[str, List[Evidence]]:
    grid: Dict[Tuple[str, str, str, int], List[BoxData]] = defaultdict(list)
    for b in boxes:
        key = (b.ref.section, b.ref.set_name, b.ref.draw_name, b.ref.column_index)
        grid[key].append(b)

    triad_to_evidence: Dict[str, List[Evidence]] = defaultdict(list)
    for (section, set_name, draw_name, col_idx), row_boxes in grid.items():
        if cfg.use_metadata_hot_flags and not any(b.ref.is_starred for b in row_boxes):
            continue

        triads: Set[str] = set()
        literal_tri = None
        if row_boxes:
            literal_value = row_boxes[0].col_value
            if literal_value and literal_value.isdigit() and len(literal_value) == 3:
                literal_tri = "".join(sorted(literal_value))
                triads.add(literal_tri)
        for b in row_boxes:
            triads |= _extract_candidate_triads(b.s_raw)
            if b.s_mirror:
                triads |= _extract_candidate_triads(b.s_mirror)
        guard_triads = _generate_guard_triads(row_boxes)
        triads |= guard_triads

        for triad in sorted(triads):
            vt_tri = "".join(str(x) for x in canonical_vtriad_from_string(triad)[0])
            row_hits: Dict[str, bool] = {}
            literal = False
            vt_lane = False
            literal_flag = literal_tri == triad if literal_tri else False
            if literal_flag:
                row_hits["DRAW"] = True
                literal = True
                vt_lane = True
            for box in row_boxes:
                lit_hit, vt_hit = _detect_triad(triad, box)
                row_hits[box.ref.row_name] = lit_hit or vt_hit
                literal = literal or lit_hit
                vt_lane = vt_lane or vt_hit

            is_set1 = any(b.ref.is_set1 for b in row_boxes)
            star_count = max((b.ref.star_count for b in row_boxes), default=0)
            is_starred = any(b.ref.is_starred for b in row_boxes)
            is_superhot_slot = any(b.is_superhot_slot for b in row_boxes)
            guard_flag = triad in guard_triads

            evidence = Evidence(
                triad=triad,
                vt_triad=vt_tri,
                section=section,
                set_name=set_name,
                draw_name=draw_name,
                column_index=col_idx,
                row_hits=row_hits,
                has_straight=literal,
                has_vt_straight=vt_lane,
                vt_only_lane=vt_lane and not literal,
                col1_arrival=(col_idx == 1 and (literal or vt_lane)),
                precol1_funnel=(col_idx in (2, 3) and (literal or vt_lane)),
                ls_col_42=(col_idx in (4, 2) and (literal or vt_lane)),
                ls2_lane=(is_set1 and col_idx in (3, 1) and (literal or vt_lane)),
                is_starred=is_starred,
                star_count=star_count,
                is_superhot_slot=is_superhot_slot,
                is_set1=is_set1,
                is_literal_draw=literal_flag,
                 guard_injected=guard_flag,
            )
            triad_to_evidence[triad].append(evidence)
    return triad_to_evidence

def _score_evidence(e: Evidence, weights: HotZoneWeights) -> Tuple[float, List[str]]:
    score = 0.0
    reasons: List[str] = []
    if e.is_starred:
        score += weights.w_hot_star * max(1, e.star_count)
        reasons.append(f"hot{e.star_count}")
    if e.is_superhot_slot:
        score += weights.w_superhot_set1
        reasons.append("superhot_set1")
    if e.is_literal_draw:
        score += weights.w_literal_hit
        reasons.append("literal_draw")
    if e.guard_injected:
        score += weights.w_guard_bonus
        reasons.append("guard_set1")
    vert = sum(1 for v in e.row_hits.values() if v)
    if vert:
        score += weights.w_vertical_support * vert
        reasons.append(f"vertical{vert}")
    if e.precol1_funnel:
        score += weights.w_precol1_funnel
        reasons.append("funnel_precol1")
    if e.col1_arrival:
        score += weights.w_col1_arrival
        reasons.append("col1")
    if e.ls_col_42:
        score += weights.w_ls_col_42
        reasons.append("ls_col_42")
    if e.ls2_lane:
        score += weights.w_ls2_lane
        reasons.append("ls2_lane")
    if e.has_vt_straight:
        score += weights.w_vt_straight
        reasons.append("vt_straight")
    if e.has_straight:
        score += weights.w_exact_straight_lane
        reasons.append("straight_lane")
    if e.vt_only_lane:
        score += weights.w_vt_only_lane_bonus
        reasons.append("vt_only_lane")
    if e.is_set1:
        score += weights.w_set1_bias
        reasons.append("set1_bonus")
    return score, reasons

def aggregate(triad_to_evs: Dict[str, List[Evidence]], weights: HotZoneWeights) -> Tuple[List[PerItemRow], List[TopCandidateRow]]:
    per_items: List[PerItemRow] = []
    tops: List[TopCandidateRow] = []
    for triad, evs in triad_to_evs.items():
        sections = {e.section for e in evs}
        sets = {e.set_name for e in evs}
        columns = {e.column_index for e in evs}
        triad_rows: List[PerItemRow] = []
        for e in evs:
            vertical_support = sum(1 for val in e.row_hits.values() if val)
            horizontal_span = len({ev.column_index for ev in evs if ev.section == e.section and ev.set_name == e.set_name})
            set_span = len(sets)
            variant_echo = len(sections)
            s, reasons = _score_evidence(e, weights)
            triad_rows.append(
                PerItemRow(
                    section=e.section,
                    set_name=e.set_name,
                    draw_name=e.draw_name,
                    column_index=e.column_index,
                    triad=e.triad,
                    vt_triad=e.vt_triad,
                    vertical_support=vertical_support,
                    horizontal_span=horizontal_span,
                    set_span=set_span,
                    variant_echo=variant_echo,
                    has_straight=int(e.has_straight),
                    has_vt_straight=int(e.has_vt_straight),
                    vt_only_lane=int(e.vt_only_lane),
                    col1_arrival=int(e.col1_arrival),
                    precol1_funnel=int(e.precol1_funnel),
                    ls_col_42=int(e.ls_col_42),
                    ls2_lane=int(e.ls2_lane),
                    is_starred=int(e.is_starred),
                    star_count=int(e.star_count),
                    is_superhot_slot=int(e.is_superhot_slot),
                    is_set1=int(e.is_set1),
                    guard_injected=int(e.guard_injected),
                    score=round(s, 3),
                    reasons="|".join(reasons),
                )
            )
        per_items.extend(triad_rows)
        hot_hits = sum(1 for e in evs if e.is_starred)
        superhot_hits = sum(1 for e in evs if e.is_superhot_slot)
        vertical_hits = max(sum(1 for val in e.row_hits.values() if val) for e in evs)
        set1_hits = sum(1 for e in evs if e.is_set1)
        col1_hits = sum(1 for e in evs if e.col1_arrival)
        precol1_hits = sum(1 for e in evs if e.precol1_funnel)
        vt_hits = sum(1 for e in evs if e.has_vt_straight)
        vt_only_hits = sum(1 for e in evs if e.vt_only_lane)
        guard_hits = sum(1 for e in evs if e.guard_injected)
        literal_hits = sum(1 for e in evs if e.is_literal_draw)
        variant_span = len(sections)
        set_span = len(sets)
        column_span = len(columns)
        scores = [row.score for row in triad_rows]
        evidence_tags = ",".join(sorted({tag for row in triad_rows for tag in row.reasons.split("|") if tag}))
        tops.append(
            TopCandidateRow(
                triad=triad,
                vt_triad=evs[0].vt_triad,
                support_count=len(evs),
                hot_hits=hot_hits,
                superhot_hits=superhot_hits,
                vertical_hits=vertical_hits,
                set1_hits=set1_hits,
                col1_hits=col1_hits,
                precol1_hits=precol1_hits,
                vt_straight_hits=vt_hits,
                vt_only_lane_hits=vt_only_hits,
                guard_hits=guard_hits,
                literal_hits=literal_hits,
                variant_span=variant_span,
                set_span=set_span,
                column_span=column_span,
                score_mean=round(sum(scores) / len(scores), 3) if scores else 0.0,
                score_max=round(max(scores), 3) if scores else 0.0,
                evidence_tags=evidence_tags,
            )
        )
    per_items.sort(key=lambda r: (-r.score, -r.vertical_support, r.column_index))
    tops.sort(key=lambda r: (-r.score_max, -r.literal_hits, -r.guard_hits, -r.score_mean))
    return per_items, tops

class HotZoneScanner:
    def __init__(self, env: TableEnv, config: HotScanConfig | None = None, weights: HotZoneWeights | None = None):
        self.env = env
        self.cfg = config or HotScanConfig()
        self.weights = weights or HotZoneWeights()

    def scan(self) -> Tuple[List[PerItemRow], List[TopCandidateRow]]:
        boxes = _extract_boxes(self.env, self.cfg)
        triads = mine_evidence(boxes, self.cfg)
        return aggregate(triads, self.weights)
