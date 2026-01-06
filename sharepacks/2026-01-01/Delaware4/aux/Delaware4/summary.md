# Aux Summary — Delaware4 — 2026-01-01

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-01/Delaware4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2025_12_31.xlsm` | aux_state_label: Delaware
- combined: live=`data/cleaned/draws/Delaware_draws.csv` snap=`sharepacks/2026-01-01/Delaware4/aux/draws/Delaware_draws.csv` n=1000 head=337, 082, 563, 706, 386
- midday: live=`data/cleaned/draws/Delaware_Midday_draws.csv` snap=`sharepacks/2026-01-01/Delaware4/aux/draws/Delaware_Midday_draws.csv` n=1000 head=082, 706, 357, 989, 355
- evening: live=`data/cleaned/draws/Delaware_Evening_draws.csv` snap=`sharepacks/2026-01-01/Delaware4/aux/draws/Delaware_Evening_draws.csv` n=1000 head=337, 563, 386, 660, 022

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=29 streak=1 max=3 last_repeat_gap=13 last_repeat_index=8

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=21), P2:7 (gap=24), P3:1 (gap=36)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 171: score=49.432808571428566 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 141: score=47.35409428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 174: score=43.74491428571429 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 144: score=41.6662 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 131: score=41.49529428571428 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Repeat-Endcap src=cartesian
- 151: score=41.435722857142856 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Repeat-Endcap src=cartesian
- 111: score=41.13118 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Repeat-Endcap src=cartesian
- 191: score=40.693151428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 271: score=35.99286428571428 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 134: score=35.8074 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 557: ds=965 sev=B
- 447: ds=957 sev=B
- 033: ds=890 sev=B
- 288: ds=830 sev=B
- 579: ds=807 sev=B
- 088: ds=793 sev=B
- 155: ds=764 sev=B
- 079: ds=761 sev=B
- 269: ds=742 sev=B
- 555: ds=724 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=56 sev=purple
  - 11: ds=48 sev=purple
  - 88: ds=30 sev=purple
  - 00: ds=27 sev=purple
  - 77: ds=24 sev=-
  - 55: ds=9 sev=-
  - 22: ds=8 sev=-
  - 99: ds=7 sev=-
  - 66: ds=6 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 79: ds=110 sev=red
  - 24: ds=80 sev=red
  - 19: ds=72 sev=red
  - 48: ds=57 sev=red
  - 13: ds=49 sev=blue
  - 47: ds=41 sev=blue
  - 78: ds=35 sev=purple
  - 17: ds=29 sev=purple
  - 27: ds=29 sev=purple
  - 01: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:228, 2:157, 32:122, 28:114, 19:88, 1:87, 31:83, 16:62, 26:60, 22:54

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=228 fs=5 fl=2 hz=0.010767160161507403, 2:ds=157 fs=13 fl=3 hz=0.01932367149758454, 32:ds=122 fs=2 fl=4 hz=0.008073817762399077, 28:ds=114 fs=14 fl=4 hz=0.02112676056338028, 19:ds=88 fs=30 fl=2 hz=0.03535911602209945, 1:ds=87 fs=1 fl=2 hz=0.008746355685131196, 31:ds=83 fs=16 fl=4 hz=0.022321428571428572, 16:ds=62 fs=2 fl=6 hz=0.009876543209876543, 26:ds=60 fs=8 fl=4 hz=0.014888337468982629, 22:ds=54 fs=46 fl=0 hz=0.0500544069640914

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=81 flags=purple
- S5: ds=50 flags=blue+purple
- S11: ds=49 flags=purple
- S2: ds=46 flags=blue+purple
- S8: ds=42 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '9'], 'pairs': {'remaining_count': 1}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=11 streak=1 max=2 last_repeat_gap=40 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=17), P2:3 (gap=23), P3:0 (gap=26)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 171: score=49.432808571428566 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 141: score=47.35409428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 174: score=43.74491428571429 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 144: score=41.6662 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 131: score=41.49529428571428 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Repeat-Endcap src=cartesian
- 151: score=41.435722857142856 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Repeat-Endcap src=cartesian
- 111: score=41.13118 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Repeat-Endcap src=cartesian
- 191: score=40.693151428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 271: score=35.99286428571428 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 134: score=35.8074 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 122: ds=951 sev=B
- 778: ds=947 sev=B
- 118: ds=885 sev=B
- 066: ds=797 sev=B
- 155: ds=784 sev=B
- 033: ds=783 sev=B
- 444: ds=755 sev=B
- 269: ds=697 sev=B
- 005: ds=690 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=71 sev=blue
  - 33: ds=67 sev=purple
  - 44: ds=53 sev=purple
  - 66: ds=45 sev=purple
  - 11: ds=25 sev=purple
  - 00: ds=13 sev=-
  - 77: ds=12 sev=-
  - 22: ds=7 sev=-
  - 55: ds=4 sev=-
  - 99: ds=3 sev=-
- non_repeating:
  - 19: ds=74 sev=red
  - 09: ds=61 sev=red
  - 25: ds=60 sev=red
  - 79: ds=56 sev=red
  - 23: ds=50 sev=blue
  - 24: ds=41 sev=blue
  - 29: ds=41 sev=blue
  - 58: ds=40 sev=blue
  - 59: ds=40 sev=blue
  - 18: ds=33 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:265, 32:200, 3:175, 15:122, 12:117, 26:109, 16:85, 28:84, 2:78, 29:73

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=265 fs=2 fl=1 hz=0.013636363636363637, 32:ds=200 fs=3 fl=1 hz=0.008077544426494346, 3:ds=175 fs=18 fl=0 hz=0.023899371069182388, 15:ds=122 fs=14 fl=3 hz=0.019744483159117306, 12:ds=117 fs=43 fl=0 hz=0.048919226393629126, 26:ds=109 fs=6 fl=0 hz=0.012750455373406192, 16:ds=85 fs=1 fl=1 hz=0.0053475935828877, 28:ds=84 fs=21 fl=1 hz=0.024309392265193373, 2:ds=78 fs=17 fl=3 hz=0.022123893805309734, 29:ds=73 fs=21 fl=2 hz=0.02519167579408543

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=78 flags=red+purple
- S25: ds=66 flags=purple
- S20: ds=56 flags=purple
- S22: ds=40 flags=purple
- S8: ds=34 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 034: score=1 tags=FLT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=29 streak=1 max=3 last_repeat_gap=67 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:9 (gap=43), P2:5 (gap=20), P3:4 (gap=25)
- consensus_notes: P1 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 2 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 7 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 6 (Mirror-Echo(CEM)), P1 mirror cluster around digit 7 (Mirror-Echo(CE)), P2 mirror cluster around digit 2 (Mirror-Echo(CEM)), P2 mirror cluster around digit 9 (Mirror-Echo(CM)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening, midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: P1:9 (ds=43)

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 171: score=49.432808571428566 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 141: score=47.35409428571428 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 174: score=43.74491428571429 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 144: score=41.6662 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 131: score=41.49529428571428 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Repeat-Endcap src=cartesian
- 151: score=41.435722857142856 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Repeat-Endcap src=cartesian
- 111: score=41.13118 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,Repeat-Endcap src=cartesian
- 191: score=40.693151428571426 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian
- 271: score=35.99286428571428 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 134: score=35.8074 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 229: ds=948 sev=B
- 055: ds=916 sev=B
- 000: ds=872 sev=B
- 279: ds=829 sev=B
- 222: ds=817 sev=B
- 006: ds=771 sev=B
- 778: ds=750 sev=B
- 189: ds=715 sev=B
- 255: ds=713 sev=B
- 004: ds=703 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=154 sev=red
  - 99: ds=59 sev=purple
  - 44: ds=28 sev=purple
  - 11: ds=24 sev=-
  - 00: ds=23 sev=-
  - 88: ds=15 sev=-
  - 77: ds=12 sev=-
  - 22: ds=4 sev=-
  - 66: ds=3 sev=-
  - 33: ds=0 sev=-
- non_repeating:
  - 79: ds=55 sev=blue
  - 69: ds=44 sev=blue
  - 03: ds=42 sev=blue
  - 24: ds=40 sev=blue
  - 48: ds=40 sev=blue
  - 89: ds=39 sev=blue
  - 13: ds=37 sev=blue
  - 19: ds=36 sev=purple
  - 16: ds=31 sev=purple
  - 47: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 5:174, 1:127, 35:114, 17:104, 31:86, 2:83, 32:61, 28:57, 21:49, 11:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 5:ds=174 fs=11 fl=2 hz=0.01643489254108723, 1:ds=127 fs=3 fl=1 hz=0.0063371356147021544, 35:ds=114 fs=3 fl=1 hz=0.007042253521126761, 17:ds=104 fs=20 fl=2 hz=0.02466367713004484, 31:ds=86 fs=20 fl=2 hz=0.025669642857142856, 2:ds=83 fs=15 fl=3 hz=0.02238805970149254, 32:ds=61 fs=2 fl=3 hz=0.007308160779537149, 28:ds=57 fs=15 fl=3 hz=0.020202020202020204, 21:ds=49 fs=49 fl=0 hz=0.05190677966101695, 11:ds=47 fs=54 fl=0 hz=0.05953693495038588

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=75 flags=blue+purple
- S23: ds=65 flags=purple
- S22: ds=63 flags=purple
- S18: ds=51 flags=red+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '4', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=1 tags=FLT
  - 013: score=1 tags=FLT
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 016: score=1 tags=FLT
  - 017: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 019: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 029: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 033 -> combined:890(B); midday:783(B)
- 155 -> combined:764(B); midday:784(B)
- 269 -> combined:742(B); midday:697(B)
- 778 -> evening:750(B); midday:947(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 11 -> combined:48(purple); midday:25(purple)
- 13 -> combined:49(blue); evening:37(blue)
- 18 -> combined:28(purple); midday:33(purple)
- 19 -> combined:72(red); evening:36(purple); midday:74(red)
- 24 -> combined:80(red); evening:40(blue); midday:41(blue)
- 44 -> combined:56(purple); evening:28(purple); midday:53(purple)
- 47 -> combined:41(blue); evening:27(purple)
- 48 -> combined:57(red); evening:40(blue); midday:28(purple)
- 79 -> combined:110(red); evening:55(blue); midday:56(red)
- 88 -> combined:30(purple); midday:71(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 1(7.2079)[R1,XVAR-Cons(CEM)], 2(1.7999357142857142)[R3,XVAR-Cons(CE)], 9(1.7449999999999999)[R1,Double-Pressure], 8(1.1075714285714284)[R1,Double-Pressure], 4(1.0739999999999998)[R2,Double-Pressure]
- P2: 7(5.2942285714285715)[R1,XVAR-Cons(CEM)], 4(3.7155142857142858)[R2,Mirror-Echo], 3(1.3567142857142855)[R1,Double-Pressure], 5(1.2971428571428572)[R1,Double-Pressure], 1(0.9925999999999999)[R2,Double-Pressure]
- P3: 1(7.8987)[R1,XVAR-Cons(CEM)], 4(6.742785714285715)[R2,XVAR-Cons(CEM)], 8(1.840242857142857)[R3,XVAR-Cons(CE)], 0(1.4462857142857144)[R1,Double-Pressure]
