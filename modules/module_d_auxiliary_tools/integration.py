"""
Glue layer for the new in-app Auxiliary Tools module.

This module provides the high-level API for integrating auxiliary tools
functionality into the main AAT9 application.
"""

import pandas as pd
from typing import Dict, Any, List, Optional
import logging
from pathlib import Path

from .refactored.extractor import extract_draw_list, validate_draw_data
from .refactored.boxed_vtrac import generate_boxed_vtrac_table
from .refactored.indicators import (
    get_overdue_pairs_analysis, 
    get_doubles_tracker_analysis,
    get_compound_scoring_placeholder
)

logger = logging.getLogger(__name__)


def run_aux_tools(state: str, data_dir: Optional[Path] = None) -> Dict[str, pd.DataFrame]:
    """
    Main API function to run auxiliary tools analysis for a state.
    
    Args:
        state: State name (e.g., "Connecticut4")
        data_dir: Optional directory containing draw data
        
    Returns:
        Dictionary with analysis results:
        {
            "boxed_vtrac": pd.DataFrame,
            "overdue_pairs": pd.DataFrame, 
            "doubles_tracker": pd.DataFrame,
            "compound_indicators": pd.DataFrame (placeholder)
        }
    """
    try:
        # Extract draw data for the state
        logger.info(f"Running auxiliary tools analysis for {state}")
        draws = extract_draw_list(state, data_dir)
        
        # DEBUG: Print draw extraction results
        print(f"[DEBUG] {state}: loaded {len(draws)} draws — first5={draws[:5] if draws else []}")
        if draws:
            print(f"[DEBUG] Last5 draws: {draws[-5:]}")
        else:
            print(f"[DEBUG] NO DRAWS LOADED FOR {state}!")
        
        if not draws:
            logger.warning(f"No draw data found for {state}")
            return _empty_results()
        
        # Validate draw data
        validated_draws = validate_draw_data(draws)
        logger.info(f"Processing {len(validated_draws)} validated draws for {state}")
        
        # Generate boxed V-TRAC table
        boxed_vtrac = generate_boxed_vtrac_table(validated_draws)
        
        # Generate overdue pairs analysis
        overdue_pairs = get_overdue_pairs_analysis(validated_draws, top_n=15)
        
        # Generate doubles tracker analysis
        doubles_tracker = get_doubles_tracker_analysis(validated_draws)
        
        # Generate compound indicators (placeholder for now)
        compound_indicators = get_compound_scoring_placeholder(validated_draws)
        
        logger.info(f"Successfully completed auxiliary tools analysis for {state}")
        
        return {
            "boxed_vtrac": boxed_vtrac,
            "overdue_pairs": overdue_pairs,
            "doubles_tracker": doubles_tracker,
            "compound_indicators": compound_indicators
        }
        
    except Exception as e:
        logger.error(f"Error running auxiliary tools for {state}: {e}")
        return _empty_results()


def _empty_results() -> Dict[str, pd.DataFrame]:
    """
    Return empty results structure when analysis fails.
    
    Returns:
        Dictionary with empty DataFrames
    """
    return {
        "boxed_vtrac": pd.DataFrame(columns=['Index', 'Singles', 'Doubles']),
        "overdue_pairs": pd.DataFrame(columns=['Pair', 'Draws_Overdue', 'Color', 'Type']),
        "doubles_tracker": pd.DataFrame(columns=['Double', 'Last_Seen', 'Frequency', 'Draws_Since']),
        "compound_indicators": pd.DataFrame(columns=['Indicator', 'Value', 'Status', 'Description'])
    }


def get_available_states(data_dir: Optional[Path] = None) -> List[str]:
    """
    Get list of available states for auxiliary tools analysis.
    
    Args:
        data_dir: Optional directory containing draw data
        
    Returns:
        List of available state names
    """
    if data_dir is None:
        data_dir = Path("data/cleaned")
    
    if not data_dir.exists():
        return []
    
    # Look for cleaned Excel files
    states = []
    for file_path in data_dir.glob("*_cleaned.xlsx"):
        state_name = file_path.stem.replace("_cleaned", "")
        states.append(state_name)
    
    return sorted(states)


def validate_state_data(state: str, data_dir: Optional[Path] = None) -> Dict[str, Any]:
    """
    Validate that a state has the required data for analysis.
    
    Args:
        state: State name
        data_dir: Optional directory containing draw data
        
    Returns:
        Dictionary with validation results
    """
    try:
        draws = extract_draw_list(state, data_dir)
        validated_draws = validate_draw_data(draws)
        
        return {
            "valid": True,
            "total_draws": len(draws),
            "validated_draws": len(validated_draws),
            "data_quality": len(validated_draws) / len(draws) if draws else 0,
            "message": f"State {state} has {len(validated_draws)} valid draws available"
        }
        
    except Exception as e:
        return {
            "valid": False,
            "total_draws": 0,
            "validated_draws": 0,
            "data_quality": 0,
            "message": f"State {state} validation failed: {str(e)}"
        } 