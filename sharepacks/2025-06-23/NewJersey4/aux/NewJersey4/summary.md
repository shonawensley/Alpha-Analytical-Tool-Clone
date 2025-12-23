# Aux Summary — NewJersey4 — 2025-06-23

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2025-06-23/NewJersey4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025-06-22.xlsm` | aux_state_label: New Jersey
- combined: live=`data/cleaned/draws/New_Jersey_draws.csv` snap=`sharepacks/2025-06-23/NewJersey4/aux/draws/New_Jersey_draws.csv` n=1000 head=887, 985, 554, 182, 445
- midday: live=`data/cleaned/draws/New_Jersey_Midday_draws.csv` snap=`sharepacks/2025-06-23/NewJersey4/aux/draws/New_Jersey_Midday_draws.csv` n=1000 head=985, 182, 399, 034, 234
- evening: live=`data/cleaned/draws/New_Jersey_Evening_draws.csv` snap=`sharepacks/2025-06-23/NewJersey4/aux/draws/New_Jersey_Evening_draws.csv` n=1000 head=887, 554, 445, 740, 351

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=29 streak=1 max=2 last_repeat_gap=96 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=23), P2:6 (gap=22), P3:3 (gap=14)
- consensus_notes: P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 666: score=39.10503214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 668: score=38.66884285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 663: score=37.6424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 068: score=35.721221428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 063: score=34.69477857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 066: score=33.948992857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 868: score=33.790132857142865 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 662: score=33.24332857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 667: score=32.57154285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 606: score=32.04531071428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 223: ds=992 sev=B
- 444: ds=917 sev=B
- 499: ds=853 sev=B
- 336: ds=828 sev=B
- 339: ds=811 sev=B
- 556: ds=791 sev=B
- 666: ds=786 sev=B
- 255: ds=758 sev=B
- 777: ds=754 sev=B
- 377: ds=729 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 00: ds=148 sev=red
  - 22: ds=117 sev=red
  - 33: ds=79 sev=blue
  - 66: ds=72 sev=blue
  - 77: ds=54 sev=purple
  - 11: ds=18 sev=-
  - 99: ds=5 sev=-
  - 44: ds=4 sev=-
  - 55: ds=2 sev=-
  - 88: ds=0 sev=-
- non_repeating:
  - 56: ds=111 sev=red
  - 05: ds=60 sev=red
  - 38: ds=49 sev=blue
  - 16: ds=47 sev=blue
  - 48: ds=46 sev=blue
  - 67: ds=38 sev=blue
  - 79: ds=32 sev=purple
  - 08: ds=30 sev=purple
  - 68: ds=30 sev=purple
  - 27: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:418, 35:237, 27:147, 13:127, 1:116, 2:82, 32:79, 19:73, 16:72, 20:70

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=418 fs=2 fl=1 hz=0.013452914798206279, 35:ds=237 fs=3 fl=1 hz=0.007936507936507936, 27:ds=147 fs=11 fl=2 hz=0.016568047337278107, 13:ds=127 fs=9 fl=3 hz=0.01568627450980392, 1:ds=116 fs=1 fl=3 hz=0.007398273736128237, 2:ds=82 fs=18 fl=2 hz=0.022753128555176336, 32:ds=79 fs=3 fl=2 hz=0.007202881152460984, 19:ds=73 fs=28 fl=1 hz=0.03341013824884793, 16:ds=72 fs=1 fl=3 hz=0.0064516129032258064, 20:ds=70 fs=16 fl=0 hz=0.018973214285714288

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S6: ds=82 flags=red+purple
- S24: ds=81 flags=blue+purple
- S12: ds=49 flags=red+purple
- S18: ds=44 flags=purple
- S2: ds=43 flags=purple
- S19: ds=37 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['0', '3', '6'], 'pairs': {'remaining_count': 1}}
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

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=14 streak=1 max=3 last_repeat_gap=18 last_repeat_index=30

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=33), P2:6 (gap=23), P3:6 (gap=20)
- consensus_notes: P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 666: score=39.10503214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 668: score=38.66884285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 663: score=37.6424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 068: score=35.721221428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 063: score=34.69477857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 066: score=33.948992857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 868: score=33.790132857142865 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 662: score=33.24332857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 667: score=32.57154285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 606: score=32.04531071428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 448: ds=986 sev=B
- 555: ds=954 sev=B
- 588: ds=943 sev=B
- 889: ds=911 sev=B
- 336: ds=867 sev=B
- 577: ds=859 sev=B
- 168: ds=799 sev=B
- 668: ds=783 sev=B
- 778: ds=779 sev=B
- 069: ds=755 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 77: ds=205 sev=red
  - 66: ds=112 sev=red
  - 44: ds=86 sev=blue
  - 00: ds=82 sev=blue
  - 22: ds=58 sev=purple
  - 33: ds=39 sev=purple
  - 88: ds=34 sev=purple
  - 11: ds=19 sev=-
  - 55: ds=15 sev=-
  - 99: ds=2 sev=-
- non_repeating:
  - 26: ds=61 sev=red
  - 56: ds=55 sev=blue
  - 15: ds=45 sev=blue
  - 68: ds=43 sev=blue
  - 08: ds=38 sev=blue
  - 09: ds=38 sev=blue
  - 48: ds=34 sev=purple
  - 05: ds=31 sev=purple
  - 67: ds=29 sev=purple
  - 19: ds=26 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:252, 1:174, 16:173, 31:135, 18:126, 4:120, 35:118, 15:95, 2:82, 27:73

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=252 fs=1 fl=0 hz=0.007246376811594203, 1:ds=174 fs=4 fl=0 hz=0.009554140127388535, 16:ds=173 fs=6 fl=2 hz=0.013138686131386862, 31:ds=135 fs=23 fl=0 hz=0.029449423815620997, 18:ds=126 fs=17 fl=3 hz=0.023781212841854936, 4:ds=120 fs=28 fl=1 hz=0.03341013824884793, 35:ds=118 fs=3 fl=0 hz=0.006720430107526881, 15:ds=95 fs=21 fl=1 hz=0.02502844141069397, 2:ds=82 fs=26 fl=0 hz=0.030338389731621937, 27:ds=73 fs=13 fl=4 hz=0.018805309734513272

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S3: ds=94 flags=purple
- S6: ds=82 flags=red+purple
- S23: ds=64 flags=purple
- S24: ds=40 flags=purple
- S18: ds=33 flags=red+purple
- S10: ds=32 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['6', '7'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 036: score=1 tags=FLT
  - 037: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=29 streak=1 max=3 last_repeat_gap=18 last_repeat_index=7

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:6 (gap=63), P2:7 (gap=16), P3:2 (gap=33)
- consensus_notes: P1 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 6 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 0 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 3 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 6 aligns across Combined, Midday (XVAR-Cons(CM)), P1 mirror cluster around digit 1 (Mirror-Echo(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CE)), P2 mirror cluster around digit 1 (Mirror-Echo(CEM)), P2 mirror cluster around digit 5 (Mirror-Echo(CE)), P3 mirror cluster around digit 8 (Mirror-Echo(CM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), P3 mirror cluster around digit 1 (Mirror-Echo(CM)), Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:6 (ds=63)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 666: score=39.10503214285714 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 668: score=38.66884285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 663: score=37.6424 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 068: score=35.721221428571425 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 063: score=34.69477857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 066: score=33.948992857142855 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 868: score=33.790132857142865 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=repeat_endcap
- 662: score=33.24332857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 667: score=32.57154285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 606: score=32.04531071428571 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CM),R1 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 155: ds=988 sev=B
- 668: ds=943 sev=B
- 225: ds=932 sev=B
- 024: ds=896 sev=B
- 035: ds=760 sev=B
- 499: ds=751 sev=B
- 339: ds=737 sev=B
- 002: ds=705 sev=B
- 556: ds=669 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 22: ds=223 sev=red
  - 00: ds=74 sev=blue
  - 99: ds=62 sev=purple
  - 33: ds=44 sev=purple
  - 66: ds=36 sev=purple
  - 77: ds=27 sev=purple
  - 11: ds=9 sev=-
  - 44: ds=2 sev=-
  - 55: ds=1 sev=-
  - 88: ds=0 sev=-
- non_repeating:
  - 56: ds=126 sev=red
  - 28: ds=97 sev=red
  - 36: ds=53 sev=blue
  - 37: ds=48 sev=blue
  - 89: ds=46 sev=blue
  - 38: ds=44 sev=blue
  - 16: ds=36 sev=purple
  - 27: ds=33 sev=purple
  - 24: ds=31 sev=purple
  - 05: ds=30 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:231, 26:209, 3:167, 13:155, 27:89, 17:68, 23:67, 33:61, 1:58, 19:55

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=231 fs=5 fl=1 hz=0.009510869565217392, 26:ds=209 fs=3 fl=0 hz=0.00753012048192771, 3:ds=167 fs=23 fl=1 hz=0.028915662650602407, 13:ds=155 fs=13 fl=2 hz=0.01968503937007874, 27:ds=89 fs=10 fl=2 hz=0.014412416851441241, 17:ds=68 fs=12 fl=3 hz=0.016233766233766232, 23:ds=67 fs=22 fl=2 hz=0.02631578947368421, 33:ds=61 fs=19 fl=2 hz=0.02661596958174905, 1:ds=58 fs=1 fl=1 hz=0.008450704225352114, 19:ds=55 fs=19 fl=2 hz=0.022975929978118162

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=89 flags=purple
- S5: ds=88 flags=purple
- S2: ds=59 flags=purple
- S24: ds=46 flags=blue+purple
- S6: ds=41 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['2', '6', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 023: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 026: score=1 tags=FLT
  - 027: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 223 -> combined:992(B); midday:677(B)
- 336 -> combined:828(B); midday:867(B)
- 339 -> combined:811(B); evening:737(B)
- 499 -> combined:853(B); evening:751(B)
- 556 -> combined:791(B); evening:669(B)
- 668 -> evening:943(B); midday:783(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:148(red); evening:74(blue); midday:82(blue)
- 05 -> combined:60(red); evening:30(purple); midday:31(purple)
- 08 -> combined:30(purple); midday:38(blue)
- 16 -> combined:47(blue); evening:36(purple)
- 19 -> combined:28(purple); midday:26(purple)
- 22 -> combined:117(red); evening:223(red); midday:58(purple)
- 27 -> combined:29(purple); evening:33(purple)
- 33 -> combined:79(blue); evening:44(purple); midday:39(purple)
- 37 -> combined:25(purple); evening:48(blue)
- 38 -> combined:49(blue); evening:44(blue)
- 48 -> combined:46(blue); midday:34(purple)
- 56 -> combined:111(red); evening:126(red); midday:55(blue)
- 66 -> combined:72(blue); evening:36(purple); midday:112(red)
- 67 -> combined:38(blue); midday:29(purple)
- 68 -> combined:30(purple); midday:43(blue)
- 77 -> combined:54(purple); evening:27(purple); midday:205(red)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 6(4.5228214285714285)[R1,XVAR-Cons(CE)], 0(2.5752)[R3,XVAR-Cons(CE)], 8(1.5852857142857142)[R1,Double-Pressure], 2(0.8979999999999999)[R2,Double-Pressure], 1(0.6959214285714286)[R3,Mirror-Echo]
- P2: 6(7.035221428571429)[R1,Mirror-Echo], 0(3.4755000000000003)[R2,XVAR-Cons(CE)], 7(1.1777142857142857)[R1,Double-Pressure], 2(1.1598)[R2,Double-Pressure], 1(0.6547142857142857)[R3,Mirror-Echo]
- P3: 8(3.6108)[R2,Mirror-Echo], 6(2.8385714285714285)[R3,XVAR-Cons(CM)], 3(2.584357142857143)[R1,Mirror-Echo], 2(1.6852857142857143)[R1,Double-Pressure], 7(1.0135)[R2,Double-Pressure]
