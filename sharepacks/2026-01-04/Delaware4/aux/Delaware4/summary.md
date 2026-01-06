# Aux Summary — Delaware4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/Delaware4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Delaware
- combined: live=`data/cleaned/draws/Delaware_draws.csv` snap=`sharepacks/2026-01-04/Delaware4/aux/draws/Delaware_draws.csv` n=1000 head=797, 422, 076, 126, 937
- midday: live=`data/cleaned/draws/Delaware_Midday_draws.csv` snap=`sharepacks/2026-01-04/Delaware4/aux/draws/Delaware_Midday_draws.csv` n=1000 head=422, 126, 149, 082, 706
- evening: live=`data/cleaned/draws/Delaware_Evening_draws.csv` snap=`sharepacks/2026-01-04/Delaware4/aux/draws/Delaware_Evening_draws.csv` n=1000 head=797, 076, 937, 337, 563

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=2 max=3 last_repeat_gap=1 last_repeat_index=28

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:2 (gap=21), P2:1 (gap=17), P3:1 (gap=42)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 251: score=42.13762857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 211: score=41.040642857142856 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 254: score=40.988192857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 214: score=39.89120714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 851: score=36.829814285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 231: score=36.39734285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 271: score=36.101757142857146 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 811: score=35.73282857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 854: score=35.68037857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 201: score=35.28834285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 557: ds=971 sev=B
- 447: ds=963 sev=B
- 033: ds=896 sev=B
- 288: ds=836 sev=B
- 579: ds=813 sev=B
- 088: ds=799 sev=B
- 155: ds=770 sev=B
- 079: ds=767 sev=B
- 269: ds=748 sev=B
- 555: ds=730 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 44: ds=62 sev=purple
  - 11: ds=54 sev=purple
  - 88: ds=36 sev=purple
  - 00: ds=33 sev=purple
  - 55: ds=15 sev=-
  - 99: ds=13 sev=-
  - 66: ds=12 sev=-
  - 33: ds=6 sev=-
  - 22: ds=1 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 48: ds=63 sev=red
  - 13: ds=55 sev=blue
  - 47: ds=47 sev=blue
  - 78: ds=41 sev=blue
  - 17: ds=35 sev=purple
  - 27: ds=35 sev=purple
  - 01: ds=34 sev=purple
  - 18: ds=34 sev=purple
  - 69: ds=29 sev=purple
  - 23: ds=28 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:234, 2:163, 32:128, 19:94, 1:93, 31:89, 16:68, 26:66, 22:60, 24:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=234 fs=5 fl=2 hz=0.010767160161507403, 2:ds=163 fs=13 fl=3 hz=0.01932367149758454, 32:ds=128 fs=2 fl=4 hz=0.008073817762399077, 19:ds=94 fs=30 fl=2 hz=0.03535911602209945, 1:ds=93 fs=1 fl=2 hz=0.008746355685131196, 31:ds=89 fs=16 fl=4 hz=0.022321428571428572, 16:ds=68 fs=2 fl=6 hz=0.009876543209876543, 26:ds=66 fs=8 fl=4 hz=0.014888337468982629, 22:ds=60 fs=46 fl=0 hz=0.0500544069640914, 24:ds=45 fs=46 fl=0 hz=0.04847207586933614

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S27: ds=100 flags=purple
- S22: ds=87 flags=purple
- S5: ds=56 flags=blue+purple
- S11: ds=55 flags=purple
- S2: ds=52 flags=blue+purple
- S3: ds=42 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['5', '8'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 018: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 028: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 038: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 048: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=1 max=2 last_repeat_gap=43 last_repeat_index=14

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=20), P2:3 (gap=26), P3:0 (gap=29)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 251: score=42.13762857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 211: score=41.040642857142856 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 254: score=40.988192857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 214: score=39.89120714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 851: score=36.829814285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 231: score=36.39734285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 271: score=36.101757142857146 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 811: score=35.73282857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 854: score=35.68037857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 201: score=35.28834285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 122: ds=954 sev=B
- 778: ds=950 sev=B
- 118: ds=888 sev=B
- 066: ds=800 sev=B
- 155: ds=787 sev=B
- 033: ds=786 sev=B
- 444: ds=758 sev=B
- 269: ds=700 sev=B
- 005: ds=693 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=74 sev=blue
  - 33: ds=70 sev=purple
  - 44: ds=56 sev=purple
  - 66: ds=48 sev=purple
  - 11: ds=28 sev=purple
  - 00: ds=16 sev=-
  - 77: ds=15 sev=-
  - 55: ds=7 sev=-
  - 99: ds=6 sev=-
  - 22: ds=0 sev=-
- non_repeating:
  - 09: ds=64 sev=red
  - 25: ds=63 sev=red
  - 79: ds=59 sev=red
  - 23: ds=53 sev=blue
  - 29: ds=44 sev=blue
  - 58: ds=43 sev=blue
  - 59: ds=43 sev=blue
  - 18: ds=36 sev=purple
  - 05: ds=35 sev=purple
  - 48: ds=31 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 35:268, 32:203, 3:178, 15:125, 12:120, 26:112, 16:88, 2:81, 29:76, 13:74

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 35:ds=268 fs=2 fl=1 hz=0.013636363636363637, 32:ds=203 fs=3 fl=1 hz=0.008077544426494346, 3:ds=178 fs=18 fl=0 hz=0.023899371069182388, 15:ds=125 fs=14 fl=3 hz=0.019744483159117306, 12:ds=120 fs=43 fl=0 hz=0.048919226393629126, 26:ds=112 fs=6 fl=0 hz=0.012750455373406192, 16:ds=88 fs=1 fl=1 hz=0.0053475935828877, 2:ds=81 fs=17 fl=3 hz=0.022123893805309734, 29:ds=76 fs=21 fl=2 hz=0.02519167579408543, 13:ds=74 fs=14 fl=1 hz=0.017837235228539576

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S2: ds=100 flags=purple
- S3: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S6: ds=81 flags=red+purple
- S25: ds=69 flags=purple
- S20: ds=59 flags=purple
- S22: ds=43 flags=purple
- S5: ds=28 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [2], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['3', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 038: score=3 tags=FLT,RS
  - 056: score=3 tags=FLT,RS
  - 137: score=3 tags=FLT,RS
  - 236: score=3 tags=FLT,RS
  - 245: score=3 tags=FLT,RS
  - 389: score=3 tags=FLT,RS
  - 569: score=3 tags=FLT,RS
  - 578: score=3 tags=FLT,RS
  - 029: score=2 tags=RS
  - 047: score=2 tags=RS

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=28 streak=1 max=3 last_repeat_gap=70 last_repeat_index=24

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:1 (gap=24), P2:5 (gap=23), P3:4 (gap=28)
- consensus_notes: P1 digit 2 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P1 digit 8 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 1 aligns across Combined, Evening (XVAR-Cons(CE)), P2 digit 5 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 4 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P3 digit 8 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 7 (Mirror-Echo(CEM)), P1 mirror cluster around digit 3 (Mirror-Echo(CM)), P2 mirror cluster around digit 6 (Mirror-Echo(CE)), P2 mirror cluster around digit 0 (Mirror-Echo(CE)), P3 mirror cluster around digit 6 (Mirror-Echo(CEM)), P3 mirror cluster around digit 9 (Mirror-Echo(CEM)), P3 mirror cluster around digit 3 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening, midday (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across combined, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across combined, evening (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 251: score=42.13762857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 211: score=41.040642857142856 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 254: score=40.988192857142856 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),R1 src=cartesian
- 214: score=39.89120714285714 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),R1,R2 src=cartesian
- 851: score=36.829814285714285 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 231: score=36.39734285714286 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 271: score=36.101757142857146 tags=Double-Pressure,Mirror-Echo(CEM),R1,R2,R3 src=cartesian
- 811: score=35.73282857142857 tags=Double-Pressure,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 854: score=35.68037857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 201: score=35.28834285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),R1,R2 src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 229: ds=951 sev=B
- 055: ds=919 sev=B
- 000: ds=875 sev=B
- 279: ds=832 sev=B
- 222: ds=820 sev=B
- 006: ds=774 sev=B
- 778: ds=753 sev=B
- 189: ds=718 sev=B
- 255: ds=716 sev=B
- 004: ds=706 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=157 sev=red
  - 99: ds=62 sev=purple
  - 44: ds=31 sev=purple
  - 11: ds=27 sev=purple
  - 00: ds=26 sev=purple
  - 88: ds=18 sev=-
  - 22: ds=7 sev=-
  - 66: ds=6 sev=-
  - 33: ds=3 sev=-
  - 77: ds=0 sev=-
- non_repeating:
  - 69: ds=47 sev=blue
  - 03: ds=45 sev=blue
  - 24: ds=43 sev=blue
  - 48: ds=43 sev=blue
  - 89: ds=42 sev=blue
  - 13: ds=40 sev=blue
  - 19: ds=39 sev=blue
  - 16: ds=34 sev=purple
  - 47: ds=30 sev=purple
  - 34: ds=29 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 5:177, 1:130, 35:117, 17:107, 31:89, 2:86, 32:64, 21:52, 11:50, 19:47

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 5:ds=177 fs=11 fl=2 hz=0.01643489254108723, 1:ds=130 fs=3 fl=1 hz=0.0063371356147021544, 35:ds=117 fs=3 fl=1 hz=0.007042253521126761, 17:ds=107 fs=20 fl=2 hz=0.02466367713004484, 31:ds=89 fs=20 fl=2 hz=0.025669642857142856, 2:ds=86 fs=15 fl=3 hz=0.02238805970149254, 32:ds=64 fs=2 fl=3 hz=0.007308160779537149, 21:ds=52 fs=49 fl=0 hz=0.05190677966101695, 11:ds=50 fs=54 fl=0 hz=0.05953693495038588, 19:ds=47 fs=25 fl=1 hz=0.027689030883919063

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S6: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=78 flags=blue+purple
- S22: ds=66 flags=purple
- S18: ds=54 flags=red+purple
- S7: ds=53 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['1', '2', '4', '8'], 'pairs': {'remaining_count': 0}}
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
- 033 -> combined:896(B); midday:786(B)
- 155 -> combined:770(B); midday:787(B)
- 269 -> combined:748(B); midday:700(B)
- 778 -> evening:753(B); midday:950(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 00 -> combined:33(purple); evening:26(purple)
- 11 -> combined:54(purple); evening:27(purple); midday:28(purple)
- 13 -> combined:55(blue); evening:40(blue); midday:27(purple)
- 18 -> combined:34(purple); midday:36(purple)
- 23 -> combined:28(purple); midday:53(blue)
- 44 -> combined:62(purple); evening:31(purple); midday:56(purple)
- 46 -> combined:26(purple); midday:29(purple)
- 47 -> combined:47(blue); evening:30(purple)
- 48 -> combined:63(red); evening:43(blue); midday:31(purple)
- 69 -> combined:29(purple); evening:47(blue)
- 88 -> combined:36(purple); midday:74(blue)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 2(6.326957142857142)[R1,XVAR-Cons(CEM)], 8(3.519142857142857)[R2,XVAR-Cons(CM)], 1(1.4165714285714284)[R1,Double-Pressure], 5(0.9508)[R2,Double-Pressure], 6(0.23971428571428574)[R3,Swap]
- P2: 5(3.6865714285714284)[R2,Mirror-Echo], 1(3.5895857142857146)[R1,XVAR-Cons(CE)], 3(1.4462857142857144)[R1,Double-Pressure], 7(1.1506999999999998)[R2,Double-Pressure], 0(0.33728571428571424)[R3,Mirror-Echo]
- P3: 1(8.1241)[R1,XVAR-Cons(CEM)], 4(6.974664285714286)[R2,XVAR-Cons(CEM)], 8(1.965407142857143)[R3,XVAR-Cons(CE)], 0(1.5658571428571428)[R1,Double-Pressure]
