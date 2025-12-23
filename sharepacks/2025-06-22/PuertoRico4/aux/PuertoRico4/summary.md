# Aux Summary — PuertoRico4 — 2025-06-22

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-22/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-21.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2025-06-22/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=551, 910, 383, 795, 656
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2025-06-22/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=910, 795, 681, 469, 708
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2025-06-22/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=551, 383, 656, 321, 913

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=3 last_repeat_gap=23 last_repeat_index=10

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=36), P2:3 (gap=24), P3:4 (gap=33)
- consensus_notes: P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 234: score=33.92050714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 244: score=33.91753571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 274: score=33.672892857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 734: score=31.839121428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 744: score=31.83615 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 774: score=31.591507142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 232: score=29.808839285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 242: score=29.805867857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),R2,R3 src=cartesian
- 294: score=29.748735714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 272: score=29.561225 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 358: ds=987 sev=B
- 334: ds=968 sev=B
- 233: ds=960 sev=B
- 034: ds=914 sev=B
- 389: ds=858 sev=B
- 225: ds=840 sev=B
- 077: ds=838 sev=B
- 344: ds=808 sev=B
- 112: ds=788 sev=B
- 229: ds=771 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=165 sev=red
  - 00: ds=70 sev=purple
  - 22: ds=47 sev=purple
  - 11: ds=35 sev=purple
  - 44: ds=33 sev=purple
  - 77: ds=29 sev=purple
  - 99: ds=18 sev=-
  - 66: ds=4 sev=-
  - 33: ds=2 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 26: ds=81 sev=red
  - 58: ds=69 sev=red
  - 05: ds=63 sev=red
  - 14: ds=54 sev=blue
  - 04: ds=52 sev=blue
  - 48: ds=50 sev=blue
  - 45: ds=46 sev=blue
  - 29: ds=44 sev=blue
  - 47: ds=39 sev=blue
  - 17: ds=35 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 33:346, 4:110, 26:109, 3:97, 29:95, 23:84, 20:75, 1:72, 35:71, 14:69

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 33:ds=346 fs=4 fl=1 hz=0.009554140127388535, 4:ds=110 fs=24 fl=2 hz=0.02931228861330327, 26:ds=109 fs=3 fl=2 hz=0.014925373134328358, 3:ds=97 fs=27 fl=1 hz=0.03398058252427184, 29:ds=95 fs=22 fl=1 hz=0.026589595375722544, 23:ds=84 fs=28 fl=2 hz=0.03389830508474576, 20:ds=75 fs=26 fl=2 hz=0.03056768558951965, 1:ds=72 fs=2 fl=2 hz=0.006521739130434782, 35:ds=71 fs=4 fl=2 hz=0.00853658536585366, 14:ds=69 fs=47 fl=0 hz=0.050865800865800864

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S7: ds=97 flags=red+purple
- S12: ds=91 flags=red+purple
- S20: ds=90 flags=red+purple
- S2: ds=60 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 034: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=9 streak=1 max=3 last_repeat_gap=78 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=47), P2:3 (gap=12), P3:6 (gap=19)
- consensus_notes: P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:3 (ds=47)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 234: score=33.92050714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 244: score=33.91753571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 274: score=33.672892857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 734: score=31.839121428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 744: score=31.83615 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 774: score=31.591507142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 232: score=29.808839285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 242: score=29.805867857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),R2,R3 src=cartesian
- 294: score=29.748735714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 272: score=29.561225 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=953 sev=B
- 233: ds=917 sev=B
- 112: ds=872 sev=B
- 389: ds=846 sev=B
- 111: ds=797 sev=B
- 299: ds=788 sev=B
- 344: ds=783 sev=B
- 003: ds=779 sev=B
- 077: ds=765 sev=B
- 333: ds=714 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=188 sev=red
  - 33: ds=133 sev=red
  - 88: ds=82 sev=blue
  - 00: ds=48 sev=purple
  - 22: ds=23 sev=-
  - 99: ds=21 sev=-
  - 11: ds=17 sev=-
  - 44: ds=16 sev=-
  - 77: ds=14 sev=-
  - 55: ds=6 sev=-
- non_repeating:
  - 14: ds=64 sev=red
  - 35: ds=52 sev=blue
  - 89: ds=51 sev=blue
  - 15: ds=41 sev=blue
  - 26: ds=40 sev=blue
  - 12: ds=37 sev=blue
  - 58: ds=34 sev=purple
  - 29: ds=32 sev=purple
  - 04: ds=31 sev=purple
  - 05: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:292, 32:230, 16:188, 33:181, 6:115, 19:98, 23:82, 4:66, 26:54, 21:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=292 fs=0 fl=2 hz=0.008264462809917356, 32:ds=230 fs=2 fl=1 hz=0.0067385444743935305, 16:ds=188 fs=3 fl=2 hz=0.008438818565400843, 33:ds=181 fs=6 fl=2 hz=0.011278195488721804, 6:ds=115 fs=21 fl=1 hz=0.02505694760820046, 19:ds=98 fs=14 fl=3 hz=0.01925254813137033, 23:ds=82 fs=31 fl=1 hz=0.0365296803652968, 4:ds=66 fs=22 fl=0 hz=0.024864864864864864, 26:ds=54 fs=7 fl=2 hz=0.010881392818280738, 21:ds=53 fs=48 fl=0 hz=0.051391862955032126

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=96 flags=red+purple
- S20: ds=68 flags=purple
- S26: ds=61 flags=blue+purple
- S23: ds=51 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '3'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT
  - 034: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=2 streak=1 max=2 last_repeat_gap=35 last_repeat_index=2

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=43), P2:0 (gap=26), P3:0 (gap=30)
- consensus_notes: P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), P3 mirror cluster around digit 2 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:7 (ds=43)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 234: score=33.92050714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 244: score=33.91753571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 274: score=33.672892857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 734: score=31.839121428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 744: score=31.83615 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 774: score=31.591507142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 232: score=29.808839285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian
- 242: score=29.805867857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),R2,R3 src=cartesian
- 294: score=29.748735714285715 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 272: score=29.561225 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 358: ds=930 sev=B
- 047: ds=917 sev=B
- 444: ds=871 sev=B
- 229: ds=850 sev=B
- 299: ds=840 sev=B
- 448: ds=829 sev=B
- 122: ds=828 sev=B
- 579: ds=810 sev=B
- 114: ds=754 sev=B
- 277: ds=694 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=164 sev=red
  - 22: ds=72 sev=blue
  - 77: ds=43 sev=purple
  - 00: ds=35 sev=purple
  - 11: ds=30 sev=purple
  - 44: ds=27 sev=purple
  - 99: ds=9 sev=-
  - 66: ds=2 sev=-
  - 33: ds=1 sev=-
  - 55: ds=0 sev=-
- non_repeating:
  - 58: ds=61 sev=red
  - 17: ds=53 sev=blue
  - 26: ds=47 sev=blue
  - 79: ds=45 sev=blue
  - 08: ds=39 sev=blue
  - 05: ds=34 sev=purple
  - 01: ds=30 sev=purple
  - 02: ds=29 sev=purple
  - 09: ds=29 sev=purple
  - 14: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:286, 26:222, 13:187, 33:173, 14:142, 20:107, 29:93, 22:92, 17:62, 5:57

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=286 fs=5 fl=1 hz=0.01662049861495845, 26:ds=222 fs=3 fl=2 hz=0.008415147265077139, 13:ds=187 fs=21 fl=2 hz=0.029754204398447608, 33:ds=173 fs=14 fl=1 hz=0.019393939393939394, 14:ds=142 fs=42 fl=0 hz=0.0498812351543943, 20:ds=107 fs=22 fl=4 hz=0.030162412993039445, 29:ds=93 fs=22 fl=1 hz=0.027218934911242602, 22:ds=92 fs=33 fl=1 hz=0.0379041248606466, 17:ds=62 fs=32 fl=0 hz=0.034261241970021415, 5:ds=57 fs=18 fl=2 hz=0.021321961620469083

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=99 flags=purple
- S22: ds=80 flags=purple
- S7: ds=68 flags=purple
- S4: ds=57 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 077 -> combined:838(B); midday:765(B)
- 112 -> combined:788(B); midday:872(B)
- 229 -> combined:771(B); evening:850(B)
- 233 -> combined:960(B); midday:917(B)
- 299 -> evening:840(B); midday:788(B)
- 344 -> combined:808(B); midday:783(B)
- 358 -> combined:987(B); evening:930(B)
- 389 -> combined:858(B); midday:846(B)
- 555 -> evening:693(B); midday:688(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:70(purple); evening:35(purple); midday:48(purple)
- 04 -> combined:52(blue); evening:26(purple); midday:31(purple)
- 05 -> combined:63(red); evening:34(purple); midday:31(purple)
- 11 -> combined:35(purple); evening:30(purple)
- 14 -> combined:54(blue); evening:27(purple); midday:64(red)
- 17 -> combined:35(purple); evening:53(blue)
- 22 -> combined:47(purple); evening:72(blue)
- 26 -> combined:81(red); evening:47(blue); midday:40(blue)
- 28 -> combined:32(purple); midday:27(purple)
- 29 -> combined:44(blue); midday:32(purple)
- 44 -> combined:33(purple); evening:27(purple)
- 45 -> combined:46(blue); midday:31(purple)
- 47 -> combined:39(blue); evening:25(purple)
- 48 -> combined:50(blue); evening:25(purple); midday:27(purple)
- 58 -> combined:69(red); evening:61(red); midday:34(purple)
- 77 -> combined:29(purple); evening:43(purple)
- 88 -> combined:165(red); evening:164(red); midday:82(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(2.4424214285714285)[R3,XVAR-Cons(CE)], 7(1.8610357142857141)[R1,Mirror-Echo], 0(1.8)[R1,Double-Pressure], 3(1.7449999999999999)[R1,Double-Pressure], 8(1.3739999999999999)[R2,Double-Pressure]
- P2: 3(3.782571428571428)[R1,XVAR-Cons(CM)], 4(2.7796)[R2,XVAR-Cons(CE)], 7(2.534957142857143)[R3,XVAR-Cons(CM)], 0(1.4762857142857142)[R1,Double-Pressure], 9(1.1108)[R2,Mirror-Echo]
- P3: 4(7.195514285714286)[R1,XVAR-Cons(CEM)], 7(3.0173428571428573)[R3,Mirror-Echo], 2(2.9623999999999997)[R2,Mirror-Echo], 0(1.4957142857142856)[R1,Double-Pressure], 6(1.1672857142857143)[R1,Double-Pressure]
