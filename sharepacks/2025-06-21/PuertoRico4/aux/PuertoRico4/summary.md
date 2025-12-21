# Aux Summary — PuertoRico4 — 2025-06-21

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-21/PuertoRico4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_06_20.xlsm` | aux_state_label: Puerto Rico
- combined: live=`data/cleaned/draws/Puerto_Rico_draws.csv` snap=`sharepacks/2025-06-21/PuertoRico4/aux/draws/Puerto_Rico_draws.csv` n=1000 head=383, 795, 656, 681, 321
- midday: live=`data/cleaned/draws/Puerto_Rico_Midday_draws.csv` snap=`sharepacks/2025-06-21/PuertoRico4/aux/draws/Puerto_Rico_Midday_draws.csv` n=1000 head=795, 681, 469, 708, 618
- evening: live=`data/cleaned/draws/Puerto_Rico_Evening_draws.csv` snap=`sharepacks/2025-06-21/PuertoRico4/aux/draws/Puerto_Rico_Evening_draws.csv` n=1000 head=383, 656, 321, 913, 655

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=32 streak=1 max=3 last_repeat_gap=21 last_repeat_index=10

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=34), P2:3 (gap=22), P3:0 (gap=47)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 530: score=37.58218214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 540: score=37.45841035714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 040: score=36.297292857142864 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 030: score=36.27448571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 070: score=36.06429285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 570: score=35.14387857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 090: score=32.16842142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=31.53105714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Repeat-Endcap src=cartesian
- 590: score=31.248007142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 500: score=30.610642857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 358: ds=985 sev=B
- 334: ds=966 sev=B
- 233: ds=958 sev=B
- 034: ds=912 sev=B
- 389: ds=856 sev=B
- 225: ds=838 sev=B
- 077: ds=836 sev=B
- 344: ds=806 sev=B
- 112: ds=786 sev=B
- 229: ds=769 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=163 sev=red
  - 00: ds=68 sev=purple
  - 22: ds=45 sev=purple
  - 11: ds=33 sev=purple
  - 44: ds=31 sev=purple
  - 77: ds=27 sev=purple
  - 99: ds=16 sev=-
  - 55: ds=8 sev=-
  - 66: ds=2 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 26: ds=79 sev=red
  - 58: ds=67 sev=red
  - 05: ds=61 sev=red
  - 14: ds=52 sev=blue
  - 04: ds=50 sev=blue
  - 01: ds=49 sev=blue
  - 48: ds=48 sev=blue
  - 45: ds=44 sev=blue
  - 29: ds=42 sev=blue
  - 47: ds=37 sev=blue

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 33:344, 4:108, 26:107, 3:95, 29:93, 23:82, 20:73, 1:70, 35:69, 14:67

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 33:ds=344 fs=4 fl=1 hz=0.009554140127388535, 4:ds=108 fs=24 fl=2 hz=0.02931228861330327, 26:ds=107 fs=3 fl=2 hz=0.014925373134328358, 3:ds=95 fs=27 fl=1 hz=0.03398058252427184, 29:ds=93 fs=22 fl=1 hz=0.026589595375722544, 23:ds=82 fs=29 fl=2 hz=0.03384279475982533, 20:ds=73 fs=26 fl=2 hz=0.03056768558951965, 1:ds=70 fs=2 fl=2 hz=0.006521739130434782, 35:ds=69 fs=4 fl=3 hz=0.008602150537634409, 14:ds=67 fs=47 fl=0 hz=0.050865800865800864

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S7: ds=95 flags=red+purple
- S12: ds=89 flags=red+purple
- S20: ds=88 flags=red+purple
- S2: ds=58 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=3 triggers={'mirror': True, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=4 tags=FLT,MIR,RS
  - 056: score=4 tags=FLT,MIR,RS
  - 146: score=4 tags=FLT,MIR,RS
  - 479: score=4 tags=FLT,MIR,RS
  - 029: score=3 tags=FLT,RS
  - 047: score=3 tags=FLT,RS
  - 245: score=3 tags=FLT,RS
  - 389: score=3 tags=MIR,RS
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=12 streak=1 max=3 last_repeat_gap=77 last_repeat_index=22

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:3 (gap=46), P2:3 (gap=11), P3:0 (gap=23)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:3 (ds=46)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 530: score=37.58218214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 540: score=37.45841035714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 040: score=36.297292857142864 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 030: score=36.27448571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 070: score=36.06429285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 570: score=35.14387857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 090: score=32.16842142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=31.53105714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Repeat-Endcap src=cartesian
- 590: score=31.248007142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 500: score=30.610642857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 558: ds=952 sev=B
- 233: ds=916 sev=B
- 112: ds=871 sev=B
- 389: ds=845 sev=B
- 111: ds=796 sev=B
- 299: ds=787 sev=B
- 344: ds=782 sev=B
- 003: ds=778 sev=B
- 077: ds=764 sev=B
- 333: ds=713 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 66: ds=187 sev=red
  - 33: ds=132 sev=red
  - 88: ds=81 sev=blue
  - 00: ds=47 sev=purple
  - 22: ds=22 sev=-
  - 99: ds=20 sev=-
  - 11: ds=16 sev=-
  - 44: ds=15 sev=-
  - 77: ds=13 sev=-
  - 55: ds=5 sev=-
- non_repeating:
  - 14: ds=63 sev=red
  - 19: ds=55 sev=blue
  - 35: ds=51 sev=blue
  - 89: ds=50 sev=blue
  - 15: ds=40 sev=blue
  - 26: ds=39 sev=blue
  - 12: ds=36 sev=purple
  - 58: ds=33 sev=purple
  - 29: ds=31 sev=purple
  - 04: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 1:291, 32:229, 16:187, 33:180, 6:114, 19:97, 23:81, 4:65, 9:55, 26:53

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 1:ds=291 fs=0 fl=2 hz=0.008264462809917356, 32:ds=229 fs=2 fl=1 hz=0.0067385444743935305, 16:ds=187 fs=3 fl=2 hz=0.008438818565400843, 33:ds=180 fs=6 fl=2 hz=0.011278195488721804, 6:ds=114 fs=21 fl=1 hz=0.02505694760820046, 19:ds=97 fs=14 fl=3 hz=0.01925254813137033, 23:ds=81 fs=31 fl=1 hz=0.0365296803652968, 4:ds=65 fs=22 fl=0 hz=0.024864864864864864, 9:ds=55 fs=42 fl=0 hz=0.0455531453362256, 26:ds=53 fs=7 fl=2 hz=0.010881392818280738

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=95 flags=red+purple
- S20: ds=67 flags=purple
- S26: ds=60 flags=blue+purple
- S10: ds=55 flags=purple

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
- current_index=32 streak=1 max=2 last_repeat_gap=34 last_repeat_index=2

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:7 (gap=42), P2:0 (gap=25), P3:0 (gap=29)
- consensus_notes: P1 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 0 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 0 (Mirror-Echo(CM)), P2 mirror cluster around digit 8 (Mirror-Echo(CM)), P2 mirror cluster around digit 9 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CM)), P3 mirror cluster around digit 5 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CE)), P3 mirror cluster around digit 7 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:7 (ds=42)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 530: score=37.58218214285714 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM) src=lane
- 540: score=37.45841035714286 tags=Double-Pressure,Lane-C,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM) src=lane
- 040: score=36.297292857142864 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 030: score=36.27448571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 070: score=36.06429285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 570: score=35.14387857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 090: score=32.16842142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=repeat_endcap
- 000: score=31.53105714285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,Repeat-Endcap src=cartesian
- 590: score=31.248007142857144 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 500: score=30.610642857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 358: ds=929 sev=B
- 047: ds=916 sev=B
- 444: ds=870 sev=B
- 229: ds=849 sev=B
- 299: ds=839 sev=B
- 448: ds=828 sev=B
- 122: ds=827 sev=B
- 579: ds=809 sev=B
- 114: ds=753 sev=B
- 277: ds=693 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=163 sev=red
  - 22: ds=71 sev=blue
  - 77: ds=42 sev=purple
  - 00: ds=34 sev=purple
  - 11: ds=29 sev=purple
  - 44: ds=26 sev=purple
  - 99: ds=8 sev=-
  - 55: ds=4 sev=-
  - 66: ds=1 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 58: ds=60 sev=red
  - 17: ds=52 sev=blue
  - 26: ds=46 sev=blue
  - 79: ds=44 sev=blue
  - 08: ds=38 sev=blue
  - 05: ds=33 sev=purple
  - 01: ds=29 sev=purple
  - 02: ds=28 sev=purple
  - 09: ds=28 sev=purple
  - 14: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:285, 26:221, 13:186, 33:172, 14:141, 20:106, 29:92, 22:91, 17:61, 5:56

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=285 fs=5 fl=1 hz=0.01662049861495845, 26:ds=221 fs=3 fl=2 hz=0.008415147265077139, 13:ds=186 fs=21 fl=2 hz=0.029754204398447608, 33:ds=172 fs=14 fl=1 hz=0.019393939393939394, 14:ds=141 fs=42 fl=0 hz=0.0498812351543943, 20:ds=106 fs=22 fl=4 hz=0.030162412993039445, 29:ds=92 fs=23 fl=1 hz=0.026460859977949284, 22:ds=91 fs=33 fl=1 hz=0.0379041248606466, 17:ds=61 fs=32 fl=0 hz=0.034261241970021415, 5:ds=56 fs=18 fl=2 hz=0.021321961620469083

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S23: ds=98 flags=purple
- S22: ds=79 flags=purple
- S7: ds=67 flags=purple
- S4: ds=56 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': True, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '4', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=2 tags=FLT,MIR
  - 016: score=2 tags=FLT,MIR
  - 025: score=2 tags=FLT,MIR
  - 027: score=2 tags=FLT,MIR
  - 035: score=2 tags=FLT,MIR
  - 038: score=2 tags=FLT,MIR
  - 045: score=2 tags=FLT,MIR
  - 049: score=2 tags=FLT,MIR
  - 056: score=2 tags=FLT,MIR
  - 057: score=2 tags=FLT,MIR

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 077 -> combined:836(B); midday:764(B)
- 112 -> combined:786(B); midday:871(B)
- 229 -> combined:769(B); evening:849(B)
- 233 -> combined:958(B); midday:916(B)
- 299 -> evening:839(B); midday:787(B)
- 344 -> combined:806(B); midday:782(B)
- 358 -> combined:985(B); evening:929(B)
- 389 -> combined:856(B); midday:845(B)
- 555 -> evening:692(B); midday:687(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:68(purple); evening:34(purple); midday:47(purple)
- 01 -> combined:49(blue); evening:29(purple)
- 04 -> combined:50(blue); evening:25(purple); midday:30(purple)
- 05 -> combined:61(red); evening:33(purple); midday:30(purple)
- 09 -> combined:35(purple); evening:28(purple)
- 11 -> combined:33(purple); evening:29(purple)
- 14 -> combined:52(blue); evening:26(purple); midday:63(red)
- 17 -> combined:33(purple); evening:52(blue)
- 22 -> combined:45(purple); evening:71(blue)
- 26 -> combined:79(red); evening:46(blue); midday:39(blue)
- 28 -> combined:30(purple); midday:26(purple)
- 29 -> combined:42(blue); midday:31(purple)
- 44 -> combined:31(purple); evening:26(purple)
- 45 -> combined:44(blue); midday:30(purple)
- 48 -> combined:48(blue); midday:26(purple)
- 58 -> combined:67(red); evening:60(red); midday:33(purple)
- 77 -> combined:27(purple); evening:42(purple)
- 88 -> combined:163(red); evening:163(red); midday:81(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 5(2.611642857142857)[R3,Mirror-Echo], 0(1.897142857142857)[R1,Mirror-Echo], 7(1.8549285714285713)[R1,Mirror-Echo], 3(1.7449999999999999)[R1,Double-Pressure], 1(1.3315)[R2,Double-Pressure]
- P2: 3(3.689857142857143)[R1,XVAR-Cons(CM)], 4(2.7126642857142858)[R2,XVAR-Cons(CE)], 7(2.4796642857142857)[R3,XVAR-Cons(CM)], 0(1.4464285714285714)[R1,Double-Pressure], 9(1.083792857142857)[R2,Mirror-Echo]
- P3: 0(8.55257142857143)[R1,XVAR-Cons(CEM)], 4(3.9045)[R2,XVAR-Cons(CE)], 2(1.9985357142857145)[R3,XVAR-Cons(CE)], 6(0.9761999999999998)[R2,Double-Pressure], 7(0.32840714285714284)[R3,Swap]
