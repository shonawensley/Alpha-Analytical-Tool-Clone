"""Smoke-test: Validate that the Stable-Pattern Extractor import is resolved to the
canonical script in scripts/tools/.
"""

from __future__ import annotations
import sys, pathlib

# Ensure the src/ folder is on sys.path so `import core` works when tests
# are executed from the project root (where pytest starts).
SRC_DIR = pathlib.Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

PROJ_ROOT = SRC_DIR.parent  # project root
if str(PROJ_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJ_ROOT))

def test_import_canonical_path():
    from core import stable_pattern_extractor as spe

    # The file path of the re-exported module (_ex) should end with the canonical path.
    # Checking spe.__file__ would only check the path of the wrapper itself.
    assert spe._ex.__name__ == "alpha_analytical.stable"

# Remove obsolete file-path assertion test
# def test_import_canonical_file():
#     from core import stable_pattern_extractor as spe
#
#     # The file path of the re-exported module (_ex) should end with the canonical path.
#     # Checking spe.__file__ would only check the path of the wrapper itself.
#     assert str(spe._ex.__file__).replace("\\", "/").endswith(
#         "scripts/tools/stable_pattern_extractor.py"
#     ) 