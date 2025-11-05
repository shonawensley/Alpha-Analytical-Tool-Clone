from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pandas as pd


def write_stacked_html(
    out_dir: Path,
    state: str,
    per_item_rows: List[Dict[str, any]],
    variant: str,
    top_rows: List[Dict[str, any]],
) -> None:
    df = pd.DataFrame(per_item_rows)
    variant_df = df[df["section"] == variant]
    if variant_df.empty:
        return

    cols = ["Set1", "Set2", "Set3"]
    draws = ["Draw1", "Draw2", "Draw3", "Draw4", "Draw5", "Draw6", "Draw7"]
    methods = ["A", "B", "C", "D", "E", "T"]
    modes = ["own", "combined"]

    tables = []
    for method in methods:
        method_df = variant_df[variant_df["method"] == method]
        if method_df.empty:
            continue
        mode_tables = []
        for mode in modes:
            mode_df = method_df[method_df["mode"] == mode]
            if mode_df.empty:
                continue
            pivot = (
                mode_df.pivot_table(
                    index=["set", "draw"],
                    columns="col",
                    values="final_value",
                    aggfunc="first",
                )
                .reindex(pd.MultiIndex.from_product([cols, draws], names=["set", "draw"]))
                .sort_index(level="set", ascending=False)
            )
            html = pivot.to_html(border=0, na_rep="", justify="center")
            mode_tables.append(f"<div class='mode-block'><h4>{mode}</h4>{html}</div>")
        if mode_tables:
            tables.append(f"<section><h3>Method {method}</h3>{''.join(mode_tables)}</section>")

    top_df = pd.DataFrame(top_rows)
    top_variant = top_df[top_df["variant"] == variant]
    top_html = top_variant.to_html(index=False, justify="center") if not top_variant.empty else "<p>No candidates.</p>"

    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            table {{ border-collapse: collapse; margin-bottom: 16px; }}
            td, th {{ border: 1px solid #999; padding: 4px 6px; text-align: center; }}
            .mode-block {{ margin-bottom: 12px; }}
        </style>
    </head>
    <body>
        <h2>{state} — {variant} Stacked View</h2>
        <section>
            <h3>Top Candidates</h3>
            {top_html}
        </section>
        {''.join(tables)}
    </body>
    </html>
    """
    out = out_dir / f"{state}_stacked_{variant.lower()}.html"
    out.write_text(html, encoding="utf-8")
