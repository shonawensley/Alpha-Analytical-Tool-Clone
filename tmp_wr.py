import sys
from pathlib import Path
root = Path(__file__).resolve().parent
src = root / "src"
if str(src) not in sys.path:
    sys.path.insert(0, str(src))
if str(root) not in sys.path:
    sys.path.insert(0, str(root))
from modules.winner_report_full import write_winner_full_report
print(write_winner_full_report("Connecticut4", "059"))
