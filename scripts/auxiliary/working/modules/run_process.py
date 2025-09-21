"""
Main script to run the entire data processing and analysis pipeline.
"""

import os
import sys
import time
from datetime import datetime
from typing import Dict, List, Optional

from .parse_excel import process_excel_file
from .analyze_pairs import (
    calculate_overdue_pairs,
    get_top_overdue_repeating_pairs,
    get_vtrac_statuses,
    get_doubles_history
)

def ensure_dirs():
    """Creates necessary directories if they don't exist."""
    dirs = ["data", "data/original", "data/cleaned", "data/outputs"]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Ensured directory exists: {d}")

def run_process(excel_path: Optional[str] = None, max_draws: int = 1000, analysis_draws: int = 100) -> Dict:
    """
    Runs the complete data processing pipeline.
    
    Args:
        excel_path: Path to the Excel file, or None to use default
        max_draws: Max rows to read from row 20 downward
        analysis_draws: Window for pair calculations (e.g., 100)
        
    Returns:
        Dict with all analysis results
    """
    # Initialize results dictionary
    results = {
        "combined": {
            "doubles_history": {}
        }
    }

    # Ensure directories exist
    ensure_dirs()

    # Set default Excel path if none provided
    if excel_path is None:
        excel_path = input("Enter path to Excel file (default: data/original/Pick3StatsC4.xlsm): ")
        if not excel_path:
            excel_path = "data/original/Pick3StatsC4.xlsm"

    # Normalize path
    excel_path = os.path.normpath(excel_path)
    output_dir = os.path.normpath("data/cleaned")

    # Process the Excel file
    print(f"\nProcessing Excel file: {excel_path}")
    start_time = time.time()
    state_draws = process_excel_file(excel_path, output_dir, max_draws=max_draws)

    if not state_draws:
        print("Error processing Excel file. Exiting.")
        return results

    print(f"Excel processing completed in {time.time() - start_time:.2f} seconds")

    # Run analysis for each state
    print("\nAnalyzing draw data for each state...")

    for state, draws in state_draws.items():
        print(f"Analyzing {state}...")

        if not draws:
            print(f"No draws found for {state}. Skipping.")
            continue

        # Windows
        draws_100 = draws[:analysis_draws] if len(draws) >= analysis_draws else draws
        draws_1000 = draws[:1000] if len(draws) >= 1000 else draws

        # Pair overdue
        non_repeating_overdue, repeating_overdue, pair_status = calculate_overdue_pairs(draws_100)

        # Top repeating pairs
        top_overdue_pairs = get_top_overdue_repeating_pairs(draws_100, 5)

        # VTRAC statuses (and top due singles tagging)
        vtrac_statuses = get_vtrac_statuses(draws_100, draws_1000)

        results[state] = {
            "draws": draws,
            "non_repeating_overdue": non_repeating_overdue,
            "repeating_overdue": repeating_overdue,
            "pair_status": pair_status,
            "top_overdue_pairs": top_overdue_pairs,
            "vtrac_statuses": vtrac_statuses
        }

        print(f"Analysis completed for {state}")

    # Combined doubles ranking
    doubles_history = get_doubles_history(state_draws)
    results["combined"]["doubles_history"] = doubles_history

    print(f"\nTotal processing completed in {time.time() - start_time:.2f} seconds")

    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outputs_dir = os.path.normpath("data/outputs")
    os.makedirs(outputs_dir, exist_ok=True)
    output_file = os.path.join(outputs_dir, f"analysis_results_{timestamp}.json")

    import json
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Results saved to {output_file}")

    return results

if __name__ == "__main__":
    if len(sys.argv) > 1:
        excel_path = sys.argv[1]
    else:
        excel_path = None

    run_process(excel_path) 