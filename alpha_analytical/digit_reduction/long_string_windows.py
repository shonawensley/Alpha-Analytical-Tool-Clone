"""Shared window definitions for the long-string digit reduction module."""
from __future__ import annotations

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

_VALID_TABLES: Tuple[TableKind, ...] = ("midday", "evening", "combined")


def get_long_string_boxes(table: str) -> List[LongStringBox]:
    """Return the long-string windows for a given stacked table."""

    table_key = str(table).lower()
    if table_key not in _VALID_TABLES:
        return []
    key = table_key  # narrow type for the dataclass field
    return [
        LongStringBox(
            table=key,  # type: ignore[assignment]
            sets=entry[0],
            draws=entry[1],
            row_types=entry[2],
            columns=entry[3],
        )
        for entry in _COMMON_WINDOWS
    ]


__all__ = ["LongStringBox", "TableKind", "get_long_string_boxes"]
