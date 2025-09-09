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
