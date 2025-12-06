"""Shared window definitions for the long-string digit reduction module."""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Iterable, Literal, Tuple, List

TableKind = Literal["midday", "evening", "combined"]

@dataclass(frozen=True)
class LongStringBox:
    """Descriptor for a window within the stacked tables."""

    table: TableKind
    sets: Tuple[str, ...]
    draws: Tuple[str, ...]
    row_types: Tuple[str, ...]
    columns: Tuple[int, ...]


_COMMON_WINDOWS: List[Tuple[Tuple[str, ...], Tuple[str, ...], Tuple[str, ...], Tuple[int, ...]]] = [
    (("Set3", "Set2", "Set1"), ("Draw1",), ("R2",), (7, 6, 5)),
    (("Set1",), ("Draw4",), ("R2",), (3,)),
    (("Set1",), ("Draw6",), ("R2",), (1,)),
]

_EXTENDED_SET1_WINDOWS: List[Tuple[Tuple[str, ...], Tuple[str, ...], Tuple[str, ...], Tuple[int, ...]]] = [
    (("Set1",), ("Draw2",), ("R2",), (6, 5, 4)),
    (("Set1",), ("Draw3",), ("R2",), (6, 5, 4, 3, 2)),
    (("Set1",), ("Draw4",), ("R2",), (4, 2)),
    (("Set1",), ("Draw5",), ("R2",), (3, 2, 1)),
    (("Set1",), ("Draw6",), ("R2",), (2,)),
    (("Set1",), ("Draw7",), ("R2",), (1,)),
]

_EXTENDED_SET2_WINDOWS: List[Tuple[Tuple[str, ...], Tuple[str, ...], Tuple[str, ...], Tuple[int, ...]]] = [
    (("Set2",), ("Draw1",), ("R2",), (3,)),
]

_VALID_TABLES: Tuple[TableKind, ...] = ("midday", "evening", "combined")


def _extended_enabled() -> bool:
    return str(os.getenv("AAT9_DR_EXTENDED_SET1", "1")).lower() in {"1", "true", "yes", "on"}


def get_long_string_boxes(table: str) -> List[LongStringBox]:
    """Return the long-string windows for a given stacked table."""

    table_key = str(table).lower()
    if table_key not in _VALID_TABLES:
        return []
    key = table_key  # narrow type for the dataclass field
    windows = list(_COMMON_WINDOWS)
    if _extended_enabled():
        windows += _EXTENDED_SET1_WINDOWS
        windows += _EXTENDED_SET2_WINDOWS
    return [
        LongStringBox(
            table=key,  # type: ignore[assignment]
            sets=entry[0],
            draws=entry[1],
            row_types=entry[2],
            columns=entry[3],
        )
        for entry in windows
    ]


__all__ = ["LongStringBox", "TableKind", "get_long_string_boxes"]
