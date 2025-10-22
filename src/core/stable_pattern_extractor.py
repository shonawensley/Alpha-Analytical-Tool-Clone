from importlib import import_module
from pathlib import Path
from datetime import datetime
import pandas as pd

from alpha_analytical.stable.metrics import build_metrics, write_metrics
from alpha_analytical.stable.post_pass_families import build_family_summary
from alpha_analytical.stable.winner_family_spotlight import build_winner_spotlight
from alpha_analytical.stable.training_bundle import write_training_bundle
_ex = import_module("alpha_analytical.stable")


# NOTE: out_path now optional – if not provided we save to the canonical
# data/outputs/analysis/patterns/<STATE>/ folder.

def run_stable_pattern_extraction(
    state: str,
    tables_path: Path,
    out_path: Path | str | None = None,
    min_occ: int = 3,
    winners: list[str] | None = None,
    bundle_stamp: str | None = None,
    write_bundle: bool = False,
):
    """Convenience wrapper around the canonical Stable-Pattern Extractor.

    Parameters
    ----------
    state : str
        State identifier (e.g. "Connecticut4"). Only used for naming outputs.
    tables_path : Path | str
        Directory containing the combined-table CSV files produced by the upstream
        table-generator pipeline.
    out_path : Path | str | None, default=None
        Destination directory where the HTML report and CSV score file will be
        written. The directory is created if it does not already exist. If None,
        the canonical patterns folder is used.
    min_occ : int, default=3
        Minimum number of occurrences a pattern must have before being returned.
    bundle_stamp : str | None, default=None
        Optional identifier used when writing a training bundle.
    write_bundle : bool, default=False
        When True, copies the generated artefacts into a versioned training bundle directory.

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
    # ------------------------------------------------------------------
    # Resolve paths
    # ------------------------------------------------------------------
    tables_path = Path(tables_path)

    # Decide where to store artefacts. If the caller did not supply a path
    # we default to the canonical patterns folder – one sub-dir per state.
    if out_path is None:
        out_path = Path("data/outputs/analysis/patterns") / state
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
    csv_path = out_path / f"{state}_stable_patterns_scores.csv"

    # Write outputs
    with open(html_path, "w", encoding="utf-8") as fh:
        fh.write("<html><head><meta charset='utf-8'></head><body>" + "\n".join(html_sections) + "</body></html>")

    # ------------------------------------------------------------------
    # Persist CSV if we have results
    # ------------------------------------------------------------------

    families_df = pd.DataFrame()
    families_path = ""
    spotlight_raw_path = ""
    spotlight_family_path = ""

    cfg = getattr(_ex, "CFG", {})
    if not df_scores.empty:
        families_df = build_family_summary(df_scores, cfg)
        if not families_df.empty:
            families_path_obj = out_path / f"{state}_stable_patterns_families.csv"
            families_df.to_csv(families_path_obj, index=False)
            families_path = str(families_path_obj)

    winners = [w.strip() for w in (winners or []) if str(w).strip()]
    if winners and not df_scores.empty:
        raw_df, fam_df = build_winner_spotlight(df_scores, families_df, winners)
        if not raw_df.empty:
            spotlight_raw_obj = out_path / f"{state}_winner_family_spotlight_raw.csv"
            raw_df.to_csv(spotlight_raw_obj, index=False)
            spotlight_raw_path = str(spotlight_raw_obj)
        if not fam_df.empty:
            spotlight_family_obj = out_path / f"{state}_winner_family_spotlight_families.csv"
            fam_df.to_csv(spotlight_family_obj, index=False)
            spotlight_family_path = str(spotlight_family_obj)

    df_scores.attrs["families_path"] = families_path
    df_scores.attrs["families_df"] = families_df.head(20) if isinstance(families_df, pd.DataFrame) else None
    df_scores.attrs["spotlight_raw_path"] = spotlight_raw_path
    df_scores.attrs["spotlight_family_path"] = spotlight_family_path

    metrics_data = build_metrics(
        state=state,
        df_scores=df_scores,
        families_df=families_df,
        winners=winners,
    )
    metrics_path_obj = write_metrics(out_path, state, metrics_data)
    metrics_path = str(metrics_path_obj)
    df_scores.attrs["metrics"] = metrics_data
    df_scores.attrs["metrics_path"] = metrics_path

    if not df_scores.empty:
        df_scores.to_csv(csv_path, index=False)
        csv_path_str = str(csv_path)
    else:
        # If nothing to write, fall back to empty string so callers can test truthiness
        csv_path_str = ""

    html_path_str = str(html_path)

    bundle_info = None
    if write_bundle and csv_path_str:
        stamp = bundle_stamp or datetime.now().strftime("%Y%m%d_%H%M%S")
        analysis_root = out_path.parent
        bundle_info = write_training_bundle(
            state=state,
            stamp=stamp,
            analysis_root=analysis_root,
            scores_path=csv_path_str,
            html_path=html_path_str,
            families_path=families_path or None,
            spotlight_raw_path=spotlight_raw_path or None,
            spotlight_family_path=spotlight_family_path or None,
            metrics_path=metrics_path or None,
            winners=winners,
        )

    df_scores.attrs["training_bundle"] = bundle_info

    return df_scores, html_path_str, csv_path_str


# Optional convenience re-exports (if they exist in the underlying module)
build_html_report = getattr(_ex, "build_html", None)
flatten_results = getattr(_ex, "flatten_results", None)

__all__ = [
    "run_stable_pattern_extraction",
    "build_html_report",
    "flatten_results",
] 
