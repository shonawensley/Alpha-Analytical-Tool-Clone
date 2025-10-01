"""Central configuration for Auxiliary module windows and thresholds.

These constants keep overdue-pair, positional, sums, and V-TRAC analysis
aligned across the app so captions and guardrails reflect the same numbers.
"""

from __future__ import annotations

# Analysis windows (number of draws inspected)
PAIRS_WINDOW = 360                 # Combined + variant overdue-pair baseline
POSITIONAL_WINDOW = 360            # Positional tracker window per variant
SUMS_WINDOW = 360                  # Draws scanned when computing sums stats
VTRAC_INDEX_WINDOW = 1000          # Depth for V-TRAC index overlay scans
COMBINATION_WINDOW = 1000          # Draws used when ranking box combinations

# Pair overdue thresholds (draws since last seen)
REPEATING_LATE = 71                # Repeating pair enters late band ("blue")
REPEATING_VERY_LATE = 107          # Repeating pair enters very-late band ("red")
NONREPEATING_LATE = 37             # Non-repeating pair late band ("blue")
NONREPEATING_VERY_LATE = 56        # Non-repeating pair very-late band ("red")
PAIR_PENDING = 25                  # Shared "pending" floor for purple items

# Combination draw-since thresholds (box analysis)
COMBO_SINGLE_LATE = 334
COMBO_SINGLE_VERY_LATE = 501
COMBO_DOUBLE_LATE = 667
COMBO_DOUBLE_VERY_LATE = 1000

WINDOW_CAPTIONS = {
    "pairs": PAIRS_WINDOW,
    "positional": POSITIONAL_WINDOW,
    "sums": SUMS_WINDOW,
    "vtrac_index": VTRAC_INDEX_WINDOW,
    "combinations": COMBINATION_WINDOW,
}
