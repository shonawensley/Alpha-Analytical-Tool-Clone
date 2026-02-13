# Cases — Crossroads Glass‑Box Pack (B36‑only)

Baseline posture: `tool_only` + `stable10`  
Baseline strategy: `v0_2_default_multi_pack_packheavy_spine4_index_tail` @ `B36`

How to review each case:
1) PRE: open the predictive run report (winners‑free evidence pointers)
2) DECISION: open the glass‑box trace (what we actually selected under B36)
3) POST: open MV + the specific winners HTML (forensics/spec only)

## Case index (deterministic)

### Case 1 — Ontario (HIT_INCLUSIVE; strict miss, lane retained)
- Header: `2026-01-15 OntarioCanada4 Midday` winner=`598` idx=`14`
- Predictive report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__OntarioCanada4__PREDICTIVE__tool_only.md`
- Glass‑box trace: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__GLASS_BOX_TRACE__OntarioCanada4__Midday__v0_2_default_multi_pack_packheavy_spine4_index_tail__B36__stable10.md`
- MV report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__OntarioCanada4.md`
- Winners HTML: `sharepacks/2026-01-15/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac14_winner_598_20260127_014847.html`

### Case 2 — Ontario (CU_MISS; lane missing even in CU)
- Header: `2026-01-15 OntarioCanada4 Evening` winner=`791` idx=`22`
- Predictive report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__OntarioCanada4__PREDICTIVE__tool_only.md`
- Glass‑box trace: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__GLASS_BOX_TRACE__OntarioCanada4__Evening__v0_2_default_multi_pack_packheavy_spine4_index_tail__B36__stable10.md`
- MV report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__OntarioCanada4.md`
- Winners HTML: `sharepacks/2026-01-15/OntarioCanada4/winners/OntarioCanada4/OntarioCanada4_vtrac22_winner_791_20260127_014849.html`

### Case 3 — NewYork (CU_LANE_BUT_PLAY_MISS; lane in CU, dropped by Play Card)
- Header: `2026-01-15 NewYork4 Midday` winner=`901` idx=`9`
- Predictive report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__NewYork4__PREDICTIVE__tool_only.md`
- Glass‑box trace: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__GLASS_BOX_TRACE__NewYork4__Midday__v0_2_default_multi_pack_packheavy_spine4_index_tail__B36__stable10.md`
- MV report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__NewYork4.md`
- Winners HTML: `sharepacks/2026-01-15/NewYork4/winners/NewYork4/NewYork4_vtrac9_winner_901_20260127_014837.html`

### Case 4 — Delaware (CU_EXACT_BUT_PLAY_MISS; exact present in CU, cut by Play Card)
- Header: `2026-01-16 Delaware4 Evening` winner=`107` idx=`7`
- Predictive report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__Delaware4__PREDICTIVE__tool_only.md`
- Glass‑box trace: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__GLASS_BOX_TRACE__Delaware4__Evening__v0_2_default_multi_pack_packheavy_spine4_index_tail__B36__stable10.md`
- MV report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-16__Delaware4.md`
- Winners HTML: `sharepacks/2026-01-16/Delaware4/winners/Delaware4/Delaware4_vtrac7_winner_107_20260127_015237.html`

### Case 5 — NorthCarolina (strict hit anatomy; “what good looks like”)
- Header: `2026-01-15 NorthCarolina4 Midday` winner=`045` idx=`5`
- Predictive report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__NorthCarolina4__PREDICTIVE__tool_only.md`
- Glass‑box trace: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__GLASS_BOX_TRACE__NorthCarolina4__Midday__v0_2_default_multi_pack_packheavy_spine4_index_tail__B36__stable10.md`
- MV report: `docs/AAT9_KIT/FINAL VALIDATION/RUNS/2026-01-15__NorthCarolina4.md`
- Winners HTML: `sharepacks/2026-01-15/NorthCarolina4/winners/NorthCarolina4/NorthCarolina4_vtrac5_winner_045_20260127_014841.html`
