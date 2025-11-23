from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

@dataclass
class PatternBox:
    R2: List[str] = field(default_factory=list)
    R4: List[str] = field(default_factory=list)
    R6: List[str] = field(default_factory=list)
    R8: List[str] = field(default_factory=list)

@dataclass
class DrawEntry:
    draw_id: str
    draw_data: List[str]
    patterns: PatternBox
    is_hot_zone: bool = False
    hot_zone_count: int = 0

@dataclass
class SetEntry:
    set_id: str
    draws: List[DrawEntry]

@dataclass
class SectionEntry:
    name: str
    sets: List[SetEntry]

@dataclass
class TableEnv:
    state_name: str
    sections: List[SectionEntry]
    analysis_guide: Dict = field(default_factory=dict)

@dataclass
class HotScanConfig:
    use_metadata_hot_flags: bool = True
    superhot_draw_ids: tuple[str, ...] = ("Draw1", "Draw2")
    hot_draw_ids: tuple[str, ...] = ("Draw3", "Draw4", "Draw5")
    consider_sections: tuple[str, ...] = ("Midday", "Evening", "Combined")
    min_boxes_for_candidate: int = 2

def _patterns_from_obj(obj: Dict) -> PatternBox:
    pv = obj.get("pattern_variations", {})
    return PatternBox(
        R2=list(pv.get("R2", [])),
        R4=list(pv.get("R4", [])),
        R6=list(pv.get("R6", [])),
        R8=list(pv.get("R8", [])),
    )

def _draw_from_obj(draw_id: str, obj: Dict) -> DrawEntry:
    meta = obj.get("metadata", {})
    return DrawEntry(
        draw_id=draw_id,
        draw_data=list(obj.get("draw_data", [])),
        patterns=_patterns_from_obj(obj),
        is_hot_zone=bool(meta.get("is_hot_zone", False)),
        hot_zone_count=int(meta.get("hot_zone_count", 0) or 0),
    )

def _set_from_obj(set_id: str, obj: Dict) -> SetEntry:
    draws_node = obj.get("draws")
    if draws_node is None:
        draws_node = obj  # support flattened {"Draw1": {...}}
    ordered: List[DrawEntry] = []
    for k in sorted(draws_node.keys(), key=lambda x: int(x.replace("Draw", ""))):
        ordered.append(_draw_from_obj(k, draws_node[k]))
    return SetEntry(set_id=set_id, draws=ordered)

def _section_from_obj(name: str, obj: Dict) -> SectionEntry:
    sets_node = obj.get("sets", {})
    ordered: List[SetEntry] = []
    for set_name in ["Set1", "Set2", "Set3"]:
        if set_name in sets_node:
            ordered.append(_set_from_obj(set_name, sets_node[set_name]))
    return SectionEntry(name=name, sets=ordered)

def load_table_env_from_json(path: str | Path) -> TableEnv:
    p = Path(path)
    data = json.loads(p.read_text(encoding="utf-8"))
    sections_node = data.get("sections", {})
    sections: List[SectionEntry] = []
    for sec_name in ["Midday", "Evening", "Combined"]:
        if sec_name in sections_node:
            sections.append(_section_from_obj(sec_name, sections_node[sec_name]))
    return TableEnv(
        state_name=data.get("state_name", "UNKNOWN"),
        sections=sections,
        analysis_guide=data.get("analysis_guide", {}),
    )
