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
    Extract the raw draw list for a state. 
    First tries to read from CSV cache, then creates it from master Excel if needed.
    
    Args:
        state: State name (e.g., "Connecticut4")
        data_dir: Directory containing the data (defaults to data/cleaned)
        
    Returns:
        List of 3-digit draw strings, most recent first
        
    Raises:
        FileNotFoundError: If neither CSV nor master Excel file is found
        ValueError: If the data format is invalid
    """
    if data_dir is None:
        # Try legacy CSV location first, fallback to cleaned dir
        csv_dir = Path("data/processed/draws")
        if csv_dir.exists():
            data_dir = csv_dir
        else:
            data_dir = Path("data/cleaned")
    
    # First, try to read from cached CSV file (legacy format)
    state_csv = data_dir / f"{state.replace('4', '')}_draws.csv"  # Remove "4" suffix for legacy compatibility
    
    if state_csv.exists():
        try:
            df = pd.read_csv(state_csv)
            if 'Draw' in df.columns:
                draws = df['Draw'].astype(str).str.zfill(3).tolist()
                return draws[:1000]  # Most recent first, limit to 1000
        except Exception as e:
            logger.warning(f"Failed to read CSV {state_csv}: {e}")
    
    # If CSV doesn't exist, create it from master Excel using legacy approach
    logger.info(f"CSV not found for {state}, extracting from master Excel")
    return _extract_from_master_excel(state)


def _extract_from_master_excel(state: str) -> List[str]:
    """
    Extract draws directly from the master Pick3StatsC4.xlsm file using legacy column mapping.
    This replicates the exact logic from scripts/auxiliary/draw_extractor.py
    """
    # State mapping from legacy draw_extractor.py
    STATE_MAPPING = {
        4: ('Connecticut4', 'N'),
        5: ('Delaware4', 'O'), 
        6: ('Florida4', 'P'),
        7: ('Georgia4', 'Q'),
        10: ('Indiana4', 'T'),
        15: ('Michigan4', 'Y'),
        18: ('NewJersey4', 'AB'),
        20: ('NewYork4', 'AD'),
        21: ('NorthCarolina4', 'AE'),
        22: ('Ohio4', 'AF'),
        23: ('OntarioCanada4', 'AG'),
        24: ('Pennsylvania4', 'AH'),
        25: ('PuertoRico4', 'AI'),
        26: ('SouthCarolina4', 'AJ'),
        28: ('Texas4', 'AL'),
        29: ('TriState4', 'AM'),
        30: ('Virginia4', 'AN'),
        74: ('WestVirginia4', 'CF')
    }
    
    def excel_col_to_index(col_str):
        """Convert Excel column letter to 0-based index"""
        idx = 0
        for char in col_str:
            idx = idx * 26 + (ord(char.upper()) - ord('A') + 1)
        return idx - 1
    
    # Find state column
    state_column = None
    for state_id, (state_name, col) in STATE_MAPPING.items():
        if state_name == state:
            state_column = col
            break
    
    if not state_column:
        raise ValueError(f"State '{state}' not found in STATE_MAPPING")
    
    # Read master Excel file
    master_file = Path("data/original/Pick3StatsC4.xlsm")
    if not master_file.exists():
        raise FileNotFoundError(f"Master data file not found at {master_file}")
    
    try:
        # Load P3Draws sheet with no headers (like legacy)
        df = pd.read_excel(master_file, sheet_name="P3Draws", header=None)
        
        # Extract using legacy logic
        col_idx = excel_col_to_index(state_column)
        start_row = 19  # Data starts from row 20 (0-indexed: 19)
        max_draws = 1000
        
        draws = []
        max_row = min(start_row + max_draws * 2, len(df))
        
        for i in range(start_row, max_row):
            if i >= len(df) or col_idx >= len(df.columns):
                break
                
            draw_val = df.iloc[i, col_idx]
            
            if pd.isna(draw_val):
                continue
            
            try:
                draw_str = str(int(draw_val)).zfill(3)
                draws.append(draw_str)
                
                if len(draws) >= max_draws:
                    break
            except (ValueError, TypeError):
                continue
        
        if not draws:
            raise ValueError(f"No valid draws found for {state}")
        
        # Return newest first (legacy reverses the order)
        draws.reverse()
        return draws
        
    except Exception as e:
        logger.error(f"Error extracting from master Excel for {state}: {e}")
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