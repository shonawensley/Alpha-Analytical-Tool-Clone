# Bonus-Ball Results Sidecar

Place the structured lottery results export here using the same date naming as the core results folder:

- `data/results_bonus/YYYY-MM-DD.txt`

Rules:

- Paste the full structured list; do not trim non-active states manually.
- Core Pick 3 truth remains authoritative in `data/results/YYYY-MM-DD.txt`.
- The bonus-ball sidecar is parsed only for the supported active bonus-ball states.
- Bonus digits are accepted only when the sidecar Pick 3 draw parity-matches the core results draw for the same state and slot.

Current v1 supported active bonus-ball states:

- `Connecticut4`
- `Florida4`
- `Indiana4`
- `NewJersey4`
- `NorthCarolina4`
- `Pennsylvania4`
- `PuertoRico4`
- `SouthCarolina4`
- `Virginia4`

Generate normalized daily truth artifacts with:

```bash
python3 scripts/tools/create_bonus_ball_truth_report.py --date YYYY-MM-DD --force
```

This writes:

- `reports/stable/bonus_ball_by_date/YYYY-MM-DD/bonus_ball_truth.json`
- `reports/stable/bonus_ball_by_date/YYYY-MM-DD/bonus_ball_truth.csv`
- `reports/stable/bonus_ball_by_date/YYYY-MM-DD/bonus_ball_parity_audit.md`
