# Aux Summary — Connecticut4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/Connecticut4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: Connecticut
- combined: live=`data/cleaned/draws/Connecticut_draws.csv` snap=`sharepacks/2025-06-21/Connecticut4/aux/draws/Connecticut_draws.csv` n=1000 head=763, 913, 201, 620, 070
- midday: live=`data/cleaned/draws/Connecticut_Midday_draws.csv` snap=`sharepacks/2025-06-21/Connecticut4/aux/draws/Connecticut_Midday_draws.csv` n=1000 head=913, 620, 221, 894, 438
- evening: live=`data/cleaned/draws/Connecticut_Evening_draws.csv` snap=`sharepacks/2025-06-21/Connecticut4/aux/draws/Connecticut_Evening_draws.csv` n=1000 head=763, 201, 070, 059, 778

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=2 last_repeat_gap=3 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=14), P2:4 (gap=17), P3:7 (gap=22)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 135: score=37.69568821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 185: score=37.661385357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 137: score=37.158654642857144 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 535: score=36.87892357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=repeat_endcap
- 585: score=36.849095 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 335: score=35.51746428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 385: score=35.487635714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 545: score=35.171845000000005 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 187: score=35.086392857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 337: score=35.05047857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 999: ds=936 sev=B
- 111: ds=920 sev=B
- 145: ds=895 sev=B
- 448: ds=837 sev=B
- 004: ds=828 sev=B
- 223: ds=809 sev=B
- 099: ds=800 sev=B
- 001: ds=783 sev=B
- 127: ds=782 sev=B
- 466: ds=735 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=163 sev=red
  - 88: ds=29 sev=purple
  - 44: ds=28 sev=purple
  - 55: ds=23 sev=-
  - 99: ds=21 sev=-
  - 11: ds=14 sev=-
  - 66: ds=11 sev=-
  - 77: ds=8 sev=-
  - 22: ds=5 sev=-
  - 00: ds=4 sev=-
- non_repeating:
  - 14: ds=85 sev=red
  - 03: ds=43 sev=blue
  - 56: ds=39 sev=blue
  - 04: ds=38 sev=blue
  - 15: ds=37 sev=blue
  - 47: ds=35 sev=purple
  - 68: ds=27 sev=purple
  - 27: ds=26 sev=purple
  - 57: ds=25 sev=purple
  - 17: ds=22 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 13:168, 2:131, 4:81, 23:72, 8:66, 14:61, 10:45, 15:41, 6:39, 9:38

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 13:ds=168 fs=16 fl=2 hz=0.022140221402214024, 2:ds=131 fs=17 fl=2 hz=0.02261904761904762, 4:ds=81 fs=25 fl=2 hz=0.029900332225913623, 23:ds=72 fs=17 fl=2 hz=0.021372328458942633, 8:ds=66 fs=43 fl=0 hz=0.04658721560130011, 14:ds=61 fs=31 fl=0 hz=0.033879781420765025, 10:ds=45 fs=17 fl=1 hz=0.022641509433962266, 15:ds=41 fs=17 fl=3 hz=0.02107481559536354, 6:ds=39 fs=31 fl=0 hz=0.03311965811965812, 9:ds=38 fs=35 fl=1 hz=0.03761755485893417

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S9: ds=86 flags=red+purple
- S4: ds=66 flags=purple
- S12: ds=57 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [9], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 018: score=3 tags=FLT,RS
  - 045: score=3 tags=FLT,RS
  - 135: score=3 tags=FLT,RS
  - 189: score=3 tags=FLT,RS
  - 234: score=3 tags=FLT,RS
  - 378: score=3 tags=FLT,RS
  - 459: score=3 tags=FLT,RS
  - 468: score=3 tags=FLT,RS
  - 567: score=3 tags=FLT,RS
  - 027: score=2 tags=RS

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=24 streak=1 max=3 last_repeat_gap=31 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=25), P2:0 (gap=25), P3:7 (gap=12)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 135: score=37.69568821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 185: score=37.661385357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 137: score=37.158654642857144 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 535: score=36.87892357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=repeat_endcap
- 585: score=36.849095 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 335: score=35.51746428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 385: score=35.487635714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 545: score=35.171845000000005 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 187: score=35.086392857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 337: score=35.05047857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 333: ds=891 sev=B
- 337: ds=854 sev=B
- 889: ds=824 sev=B
- 234: ds=775 sev=B
- 225: ds=751 sev=B
- 077: ds=732 sev=B
- 009: ds=725 sev=B
- 279: ds=698 sev=B
- 117: ds=684 sev=B
- 128: ds=682 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=81 sev=blue
  - 11: ds=72 sev=blue
  - 00: ds=40 sev=purple
  - 44: ds=37 sev=purple
  - 77: ds=23 sev=-
  - 88: ds=14 sev=-
  - 55: ds=11 sev=-
  - 99: ds=10 sev=-
  - 66: ds=5 sev=-
  - 22: ds=2 sev=-
- non_repeating:
  - 18: ds=90 sev=red
  - 69: ds=67 sev=red
  - 14: ds=42 sev=blue
  - 04: ds=34 sev=purple
  - 45: ds=30 sev=purple
  - 58: ds=30 sev=purple
  - 67: ds=26 sev=purple
  - 01: ds=25 sev=purple
  - 09: ds=25 sev=purple
  - 28: ds=24 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:142, 13:123, 19:104, 23:90, 17:72, 2:65, 8:57, 27:49, 31:46, 5:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=142 fs=2 fl=0 hz=0.006006006006006006, 13:ds=123 fs=16 fl=1 hz=0.021013597033374538, 19:ds=104 fs=21 fl=1 hz=0.026284348864994027, 23:ds=90 fs=23 fl=1 hz=0.026402640264026403, 17:ds=72 fs=32 fl=2 hz=0.037158469945355196, 2:ds=65 fs=22 fl=1 hz=0.026713124274099886, 8:ds=57 fs=53 fl=0 hz=0.05644302449414271, 27:ds=49 fs=16 fl=3 hz=0.020452099031216364, 31:ds=46 fs=20 fl=3 hz=0.024390243902439025, 5:ds=43 fs=14 fl=2 hz=0.018046709129511677

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S24: ds=92 flags=purple
- S6: ds=65 flags=red+purple
- S9: ds=57 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [7], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 025: score=3 tags=FLT,RS
  - 079: score=3 tags=FLT,RS
  - 178: score=3 tags=FLT,RS
  - 259: score=3 tags=FLT,RS
  - 358: score=3 tags=FLT,RS
  - 367: score=3 tags=FLT,RS
  - 457: score=3 tags=FLT,RS
  - 016: score=2 tags=RS
  - 034: score=2 tags=RS
  - 124: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=21 streak=1 max=3 last_repeat_gap=23 last_repeat_index=31

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=17), P2:3 (gap=36), P3:5 (gap=31)
- consensus_notes: P1 digit 1 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CM)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P1 mirror cluster around digit 8 (Mirror-Echo(CE)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CEM)), P3 mirror cluster around digit 0 (Mirror-Echo(CEM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 135: score=37.69568821428571 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 185: score=37.661385357142855 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 137: score=37.158654642857144 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 535: score=36.87892357142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=repeat_endcap
- 585: score=36.849095 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 335: score=35.51746428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 385: score=35.487635714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 545: score=35.171845000000005 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=repeat_endcap
- 187: score=35.086392857142854 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 337: score=35.05047857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 255: ds=933 sev=B
- 034: ds=910 sev=B
- 228: ds=888 sev=B
- 088: ds=886 sev=B
- 223: ds=847 sev=B
- 666: ds=835 sev=B
- 225: ds=810 sev=B
- 678: ds=711 sev=B
- 668: ds=708 sev=B
- 399: ds=707 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=84 sev=blue
  - 88: ds=49 sev=purple
  - 55: ds=31 sev=purple
  - 99: ds=15 sev=-
  - 44: ds=14 sev=-
  - 66: ds=12 sev=-
  - 11: ds=7 sev=-
  - 22: ds=5 sev=-
  - 77: ds=4 sev=-
  - 00: ds=2 sev=-
- non_repeating:
  - 35: ds=88 sev=red
  - 14: ds=77 sev=red
  - 15: ds=72 sev=red
  - 56: ds=72 sev=red
  - 16: ds=43 sev=blue
  - 08: ds=35 sev=purple
  - 03: ds=33 sev=purple
  - 57: ds=31 sev=purple
  - 39: ds=30 sev=purple
  - 34: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 20:223, 2:171, 15:144, 32:130, 16:117, 34:93, 13:84, 4:55, 6:53, 33:49

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 20:ds=223 fs=18 fl=2 hz=0.0258732212160414, 2:ds=171 fs=19 fl=2 hz=0.02811244979919679, 15:ds=144 fs=14 fl=1 hz=0.01873536299765808, 32:ds=130 fs=2 fl=0 hz=0.004120879120879121, 16:ds=117 fs=2 fl=1 hz=0.005961251862891207, 34:ds=93 fs=20 fl=2 hz=0.025, 13:ds=84 fs=23 fl=3 hz=0.028540065861690448, 4:ds=55 fs=22 fl=1 hz=0.024918743228602384, 6:ds=53 fs=16 fl=1 hz=0.0196078431372549, 33:ds=49 fs=29 fl=0 hz=0.03176341730558598

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=93 flags=red+purple
- S8: ds=91 flags=red+purple
- S24: ds=70 flags=purple
- S20: ds=69 flags=purple
- S6: ds=57 flags=purple
- S2: ds=53 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 049: score=1 tags=FLT
  - 124: score=1 tags=FLT
  - 134: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 044 -> combined:695(B); evening:703(B)
- 145 -> combined:895(B); evening:672(B)
- 223 -> combined:809(B); evening:847(B)
- 225 -> evening:810(B); midday:751(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 03 -> combined:43(blue); evening:33(purple)
- 04 -> combined:38(blue); midday:34(purple)
- 14 -> combined:85(red); evening:77(red); midday:42(blue)
- 15 -> combined:37(blue); evening:72(red)
- 33 -> combined:163(red); evening:84(blue); midday:81(blue)
- 44 -> combined:28(purple); midday:37(purple)
- 47 -> combined:35(purple); evening:29(purple)
- 56 -> combined:39(blue); evening:72(red)
- 57 -> combined:25(purple); evening:31(purple)
- 88 -> combined:29(purple); evening:49(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(3.8864285714285716)[R1,XVAR-Cons(CM)], 3(2.8206857142857142)[R3,XVAR-Cons(CE)], 5(2.4252285714285717)[R2,XVAR-Cons(CM)], 8(1.3595714285714284)[R1,Mirror-Echo], 7(0.9552999999999999)[R2,Double-Pressure]
- P2: 3(3.4322857142857144)[R3,Mirror-Echo], 8(3.402457142857143)[R2,Mirror-Echo], 4(2.725207142857143)[R1,XVAR-Cons(CE)], 0(1.483607142857143)[R1,Mirror-Echo], 1(1.2433999999999998)[R2,Double-Pressure]
- P3: 5(6.764492857142857)[R2,XVAR-Cons(CEM)], 7(6.297507142857143)[R1,XVAR-Cons(CEM)], 6(2.3763714285714284)[R3,XVAR-Cons(CE)], 9(0.879)[R2,Double-Pressure]
