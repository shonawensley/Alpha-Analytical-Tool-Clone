"""
Main script to run the entire data processing and analysis pipeline.
"""

import os
import sys
import time
from datetime import datetime
from typing import Dict, List, Optional

from modules.parse_excel import process_excel_file
from modules.analyze_pairs import (
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
        max_draws: Maximum number of draws to extract from Excel (default 1000)
        analysis_draws: Number of draws to use for overdue analysis (default 100)
        
    Returns:
        Dict with all analysis results
    """
    # Initialize results dictionary
    results = {
        "combined": {
            "doubles_history": {}  # Initialize with empty dict
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
    state_draws = process_excel_file(excel_path, output_dir, max_draws)
    
    # Debug check for state_draws
    if state_draws is None:
        print("ERROR: process_excel_file returned None. Exiting.")
        return results  # Return initialized results with empty doubles_history
    
    print(f"DEBUG: state_draws contains data for {len(state_draws)} states: {list(state_draws.keys())}")
    
    # Quick check on a state to see if we have any draws
    if state_draws and len(state_draws) > 0:
        first_state = next(iter(state_draws))
        draws = state_draws[first_state]
        if draws:
            print(f"DEBUG: First 5 draws for {first_state}: {draws[:5]}")
            # Check draw order - we expect newest first (based on the code comments)
            print(f"DEBUG: Order verification - these should be the newest draws")
            
    print(f"Excel processing completed in {time.time() - start_time:.2f} seconds")
    
    # Run analysis for each state
    print("\nAnalyzing draw data for each state...")
    
    for state, draws in state_draws.items():
        print(f"Analyzing {state}...")
        
        # Skip if no draws
        if not draws:
            print(f"No draws found for {state}. Skipping.")
            continue
        
        print(f"DEBUG: {state} has {len(draws)} draws.")
        
        # For each state, get the analysis draws and the 1000 draws (or all draws if less than needed)
        draws_analysis = draws[:analysis_draws] if len(draws) >= analysis_draws else draws
        draws_1000 = draws[:1000] if len(draws) >= 1000 else draws
        
        print(f"DEBUG: Using {len(draws_analysis)} draws for overdue analysis and {len(draws_1000)} for 1000-draw combo tracking")
        
        # Calculate overdue pairs (using the analysis draws)
        non_repeating_overdue, repeating_overdue, pair_status = calculate_overdue_pairs(draws_analysis)
        
        # Get top 5 most overdue repeating pairs
        top_overdue_pairs = get_top_overdue_repeating_pairs(draws_analysis, 5)
        
        # Get V-Trac statuses (using both analysis and 1000 draw histories)
        vtrac_statuses = get_vtrac_statuses(draws_analysis, draws_1000)
        
        # Check if any combos should be underlined
        combos_with_underline = 0
        for idx_data in vtrac_statuses.values():
            for combo_dict in idx_data.get("singles_status", {}).values():
                if combo_dict.get("underline", False):
                    combos_with_underline += 1
            for combo_dict in idx_data.get("doubles_status", {}).values():
                if combo_dict.get("underline", False):
                    combos_with_underline += 1
        
        print(f"DEBUG: Found {combos_with_underline} combos that should be underlined (never appeared in draws_1000)")
        
        # Store all analysis results
        results[state] = {
            "draws": draws,
            "non_repeating_overdue": non_repeating_overdue,
            "repeating_overdue": repeating_overdue,
            "pair_status": pair_status,
            "top_overdue_pairs": top_overdue_pairs,
            "vtrac_statuses": vtrac_statuses
        }
        
        print(f"Analysis completed for {state}")
    
    # Calculate doubles history for all states
    doubles_history = get_doubles_history(state_draws)
    
    # Update combined results
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
    # Run process with command line argument or default path
    if len(sys.argv) > 1:
        excel_path = sys.argv[1]
    else:
        excel_path = None
    
    run_process(excel_path) 