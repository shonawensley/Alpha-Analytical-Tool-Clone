from __future__ import annotations

import pandas as pd


def read_csv_strsafe(path: str):
    """Read a CSV preserving strings exactly (no NA coercion, no numeric inference)."""
    return pd.read_csv(path, dtype=str, keep_default_na=False, na_filter=False)

