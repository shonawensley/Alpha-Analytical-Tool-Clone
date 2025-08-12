"""
Re-export all symbols from the legacy `vtrac_reference` so that
`from modules.vtrac_reference import ...` works in this project.

We can't use a relative import here reliably because `legacy_modules_backup`
is not a package. Instead, temporarily insert the parent directory onto
`sys.path` and import the top-level `vtrac_reference` module directly.
"""

import os
import sys

_PARENT = os.path.dirname(os.path.dirname(__file__))
if _PARENT not in sys.path:
    sys.path.insert(0, _PARENT)

from vtrac_reference import *  # noqa: F401,F403



