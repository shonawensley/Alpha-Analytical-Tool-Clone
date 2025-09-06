"""
Forwarder shim for path handler (AAT9)

This legacy module re-exports all public symbols from the canonical
`utils.path_handler` so older code importing `src.utils.path_handler`
continues to work. Do not add new logic here; update utils/path_handler.py.
"""

from utils.path_handler import *  # noqa: F401,F403
from utils import path_handler as _ph

# Ensure __all__ reflects the canonical module
try:
    __all__ = [n for n in dir(_ph) if not n.startswith('_')]
except Exception:
    __all__ = []

def get_analysis_dir(kind: str, state: str) -> Path:
    """Return analysis subfolder path, creating it if needed.

    Args:
        kind: sub-folder under data/outputs/analysis (e.g. 'patterns', 'vtrac').
        state: state name, e.g. 'Connecticut4'.

    Returns:
        pathlib.Path pointing to the directory data/outputs/analysis/<kind>/<state>/
    """
    base = get_outputs_dir() / "analysis" / kind / state
    base.mkdir(parents=True, exist_ok=True)
    return base

if __name__ == "__main__":
    # Display path information when run directly
    print("Lottery Data Processing Path Information:")
    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Data Directory: {DATA_DIR}")
    print(f"Original Data: {ORIGINAL_DIR}")
    print(f"Cleaned Data: {DATA_DIR / 'cleaned'}")
    print(f"Outputs Directory: {DATA_DIR / 'outputs'}")
    print(f"Tables Output: {DATA_DIR / 'outputs' / 'tables'}")
    print(f"Winners Output (Today): {DATA_DIR / 'outputs' / 'winners' / get_current_date_str()}")
    print(f"Analysis Output: {DATA_DIR / 'outputs' / 'analysis'}")
    print(f"Excel File Path: {get_excel_path()}")
    
    # Create directories
    create_output_directories()
    print("\nAll required directories have been created.") 
