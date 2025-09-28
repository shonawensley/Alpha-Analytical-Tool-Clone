from dataclasses import dataclass
from typing import Dict, List, Optional, Any

@dataclass(frozen=True)
class Key:
    state: str
    area: str            # LS1 | LS2
    section: str         # Midday | Evening | Combined
    set: str             # Set1 | Set2 | Set3
    draw: str            # Draw1..Draw7
    col: int             # 7/6/5 (LS1) or 3/1 (LS2)
    method: str          # A..E,T
    mode: str            # own | combined

@dataclass
class Step:
    step: int
    value: str
    length: int
    unique_digits: int
    is_3value: bool

@dataclass
class Item:
    key: Key
    grid_position: Dict[str, int]
    sequence_meta: Dict[str, Any]
    steps: List[Step]
    final: Dict[str, Any]

    @property
    def orig(self) -> Step:
        return self.steps[0] if self.steps else Step(0, "", 0, 0, False)
