"""
Draw list extractor and common helpers for auxiliary tools.

This module provides functionality to extract and process raw draw data
from CSV files produced from the P3Draws sheet.
"""

import pandas as pd
from pathlib import Path
from typing import List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


def extract_draw_list(state: str, data_dir: Optional[Path] = None) -> List[str]:
    """
    Extract the raw draw list for a state from CSV files.
    
    Args:
        state: State name (e.g., "Connecticut4")
        data_dir: Directory containing the draw data (defaults to data/cleaned)
        
    Returns:
        List of 3-digit draw strings, most recent first
        
    Raises:
        FileNotFoundError: If the state data file is not found
        ValueError: If the data format is invalid
    """
    if data_dir is None:
        data_dir = Path("data/cleaned")
    
    # Look for the state's cleaned Excel file
    state_file = data_dir / f"{state}_cleaned.xlsx"
    
    if not state_file.exists():
        raise FileNotFoundError(f"No cleaned data file found for {state} at {state_file}")
    
    try:
        # Read the P3Draws sheet (this is where the raw draw data is stored)
        df = pd.read_excel(state_file, sheet_name="P3Draws")
        
        # Look for draw columns - typically named like "Draw", "Midday", "Evening" or similar
        draw_columns = [col for col in df.columns if any(keyword in col.lower() 
                       for keyword in ['draw', 'midday', 'evening', 'number'])]
        
        if not draw_columns:
            # Fallback: look for numeric columns that could contain draws
            draw_columns = [col for col in df.columns if df[col].dtype == 'object' or 
                          (pd.api.types.is_numeric_dtype(df[col]) and df[col].max() <= 999)]
        
        if not draw_columns:
            raise ValueError(f"No draw columns found in {state} data")
        
        # Extract all draws from all draw columns
        draws = []
        for col in draw_columns:
            # Filter out null values and convert to string
            col_draws = df[col].dropna().astype(str)
            
            # Filter for valid 3-digit draws
            valid_draws = [draw.zfill(3) for draw in col_draws 
                          if draw.isdigit() and len(draw.zfill(3)) == 3]
            
            draws.extend(valid_draws)
        
        if not draws:
            raise ValueError(f"No valid draws found in {state} data")
        
        # Return most recent first (reverse chronological order)
        return list(reversed(draws))[-1000:]  # Limit to last 1000 draws for performance
        
    except Exception as e:
        logger.error(f"Error extracting draws for {state}: {e}")
        raise


def get_state_info(state: str) -> Dict[str, Any]:
    """
    Get basic information about a state.
    
    Args:
        state: State name
        
    Returns:
        Dictionary with state information
    """
    # State mapping from legacy code
    state_mapping = {
        "Connecticut4": {"id": 4, "draws_per_day": 2},
        "Delaware4": {"id": 5, "draws_per_day": 2},
        "Florida4": {"id": 6, "draws_per_day": 2},
        "Georgia4": {"id": 7, "draws_per_day": 3},
        "Indiana4": {"id": 10, "draws_per_day": 2},
        "Michigan4": {"id": 15, "draws_per_day": 2},
        "NewJersey4": {"id": 18, "draws_per_day": 2},
        "NewYork4": {"id": 20, "draws_per_day": 2},
        "NorthCarolina4": {"id": 21, "draws_per_day": 2},
        "Ohio4": {"id": 22, "draws_per_day": 2},
        "Ontario4": {"id": 23, "draws_per_day": 2},
        "Pennsylvania4": {"id": 24, "draws_per_day": 2},
        "Texas4": {"id": 28, "draws_per_day": 4},
        "Virginia4": {"id": 30, "draws_per_day": 2},
        "WestVirginia4": {"id": 74, "draws_per_day": 1},
    }
    
    return state_mapping.get(state, {"id": 0, "draws_per_day": 2})


def validate_draw_data(draws: List[str]) -> List[str]:
    """
    Validate and clean draw data.
    
    Args:
        draws: List of draw strings
        
    Returns:
        List of validated 3-digit draw strings
    """
    validated = []
    
    for draw in draws:
        # Convert to string and pad with zeros if necessary
        draw_str = str(draw).zfill(3)
        
        # Validate it's exactly 3 digits
        if len(draw_str) == 3 and draw_str.isdigit():
            validated.append(draw_str)
        else:
            logger.warning(f"Invalid draw skipped: {draw}")
    
    return validated