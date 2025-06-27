from importlib import import_module
from pathlib import Path
import pandas as pd

_ex = import_module("alpha_analytical.stable")


def run_stable_pattern_extraction(state: str, tables_path: Path, out_path: Path, min_occ: int = 3):
    """Convenience wrapper around the canonical Stable-Pattern Extractor.

    Parameters
    ----------
    state : str
        State identifier (e.g. "Connecticut4"). Only used for naming outputs.
    tables_path : Path | str
        Directory containing the combined-table CSV files produced by the upstream
        table-generator pipeline.
    out_path : Path | str
        Destination directory where the HTML report and CSV score file will be
        written. The directory is created if it does not already exist.
    min_occ : int, default=3
        Minimum number of occurrences a pattern must have before being returned.

    Returns
    -------
    df_scores : pandas.DataFrame
        DataFrame containing all extracted pattern rows (sorted by score).
    html_path : str
        Absolute path to the generated HTML report (or empty string if nothing
        was generated).
    csv_path : str
        Absolute path to the generated CSV file (or empty string if nothing was
        generated).
    """
    # Ensure we are working with pathlib.Path objects
    tables_path = Path(tables_path)
    out_path = Path(out_path)
    out_path.mkdir(parents=True, exist_ok=True)

    # Glob for *_Combined*.csv files inside the tables folder
    csv_files = sorted(tables_path.glob("*Combined*.csv"))
    if not csv_files:
        # Nothing to process
        return pd.DataFrame(), "", ""

    html_sections = []
    all_rows: list[dict] = []

    for csv_file in csv_files:
        try:
            df_table = pd.read_csv(csv_file, dtype=str).fillna("")
        except Exception:
            # Skip malformed CSVs silently; could be expanded to logging
            continue

        # Derive section name from filename
        fname = csv_file.name.lower()
        if "_evening_" in fname:
            section = "Evening"
        elif "_midday_" in fname:
            section = "Midday"
        else:
            section = "Combined"

        mask_map, results = _ex.analyse(df_table, section)
        html_sections.append(_ex.build_html(df_table, mask_map, section, results))
        all_rows.extend(results)

    if not all_rows:
        return pd.DataFrame(), "", ""

    # Aggregate & sort
    all_rows.sort(key=lambda r: r.get("score", 0), reverse=True)
    df_scores = pd.DataFrame(all_rows)

    # Apply min_occ filter
    if min_occ > 1 and not df_scores.empty:
        pattern_counts = df_scores["Canonical"].value_counts()
        keepers = pattern_counts[pattern_counts >= min_occ].index
        df_scores = df_scores[df_scores["Canonical"].isin(keepers)].reset_index(drop=True)

    html_path = out_path / f"{state}_stable_patterns_report.html"
    csv_path = ""  # neutralise legacy path

    # Write outputs
    with open(html_path, "w", encoding="utf-8") as fh:
        fh.write("<html><head><meta charset='utf-8'></head><body>" + "\n".join(html_sections) + "</body></html>")

    return df_scores, str(html_path), csv_path


# Optional convenience re-exports (if they exist in the underlying module)
build_html_report = getattr(_ex, "build_html", None)
flatten_results = getattr(_ex, "flatten_results", None)

__all__ = [
    "run_stable_pattern_extraction",
    "build_html_report",
    "flatten_results",
] 