import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
sys.path.insert(1, str(root / "src"))

from modules.winner_report_full import write_winner_full_report

STATE = "Connecticut4"
WINNER = "059"

try:
    out_path = Path(write_winner_full_report(STATE, WINNER))
except Exception as exc:
    print(f"FAIL: write_winner_full_report raised {exc!r}")
    sys.exit(1)

if not out_path.exists():
    print(f"FAIL: expected report at {out_path} but file not found")
    sys.exit(1)

content = out_path.read_text(encoding="utf-8")
required = ["legend", "hit-winner", "hit-winner-gap", "hit-vt-straight", "hit-vt-straight-gap", "hit-family", "Long-string (DR) box"]
missing = [token for token in required if token not in content]
if missing:
    print(f"FAIL: report missing markers: {missing}")
    sys.exit(1)

print(f"OK: winners logger smoke passed ({out_path})")

