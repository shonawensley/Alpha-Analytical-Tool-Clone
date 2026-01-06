# Aux Summary — Pennsylvania4 — 2026-01-04

Evidence dump for Master Validation **Part 3** (Aux).
All facts are labeled by source for provenance.

## Config (source: core/aux_config.py)
- windows: pairs=360 positional=360 vtrac_index=1000 sums_used=100
- thresholds: doubles_late=667 doubles_very_late=1000 pair_pending=25

## Draw sources (source: modules.aux_loaders.load_state_draws)
- snapshot_dir: `sharepacks/2026-01-04/Pennsylvania4/aux/draws`
- snapshot_mode: generated_from_excel
- excel: `data/history/Pick3StatsC4_2026-01-03.xlsm` | aux_state_label: Pennsylvania
- combined: live=`data/cleaned/draws/Pennsylvania_draws.csv` snap=`sharepacks/2026-01-04/Pennsylvania4/aux/draws/Pennsylvania_draws.csv` n=1000 head=909, 744, 360, 871, 328
- midday: live=`data/cleaned/draws/Pennsylvania_Midday_draws.csv` snap=`sharepacks/2026-01-04/Pennsylvania4/aux/draws/Pennsylvania_Midday_draws.csv` n=1000 head=744, 871, 322, 684, 186
- evening: live=`data/cleaned/draws/Pennsylvania_Evening_draws.csv` snap=`sharepacks/2026-01-04/Pennsylvania4/aux/draws/Pennsylvania_Evening_draws.csv` n=1000 head=909, 360, 328, 221, 173

## Combined (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=3 last_repeat_gap=27 last_repeat_index=4

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:0 (gap=14), P2:5 (gap=25), P3:7 (gap=19)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=35.26034285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 455: score=35.2097 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 015: score=34.92782857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 055: score=34.877185714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 417: score=34.69262857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 457: score=34.64198571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 017: score=34.36011428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 057: score=34.30947142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 416: score=34.18077142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 456: score=34.13012857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 666: ds=998 sev=B
- 159: ds=886 sev=B
- 007: ds=883 sev=B
- 088: ds=847 sev=B
- 008: ds=825 sev=B
- 444: ds=801 sev=B
- 039: ds=776 sev=B
- 355: ds=766 sev=B
- 344: ds=695 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 33: ds=143 sev=red
  - 77: ds=82 sev=blue
  - 88: ds=81 sev=blue
  - 66: ds=69 sev=purple
  - 55: ds=46 sev=purple
  - 11: ds=31 sev=purple
  - 00: ds=29 sev=purple
  - 22: ds=5 sev=-
  - 44: ds=1 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 07: ds=49 sev=blue
  - 35: ds=42 sev=blue
  - 69: ds=40 sev=blue
  - 34: ds=35 sev=purple
  - 19: ds=33 sev=purple
  - 15: ds=25 sev=purple
  - 45: ds=22 sev=-
  - 08: ds=21 sev=-
  - 57: ds=20 sev=-
  - 79: ds=20 sev=-

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:285, 26:242, 16:100, 7:68, 6:63, 13:61, 19:57, 10:52, 1:46, 11:43

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=285 fs=2 fl=1 hz=0.007380073800738007, 26:ds=242 fs=0 fl=1 hz=0.003898635477582846, 16:ds=100 fs=3 fl=2 hz=0.007371007371007371, 7:ds=68 fs=35 fl=1 hz=0.04, 6:ds=63 fs=21 fl=1 hz=0.025611175785797437, 13:ds=61 fs=21 fl=1 hz=0.024553571428571428, 19:ds=57 fs=21 fl=3 hz=0.025695931477516063, 10:ds=52 fs=23 fl=2 hz=0.02676659528907923, 1:ds=46 fs=1 fl=2 hz=0.0044742729306487695, 11:ds=43 fs=48 fl=0 hz=0.05128205128205128

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S23: ds=100 flags=red+purple
- S24: ds=100 flags=red+purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S3: ds=94 flags=purple
- S20: ds=81 flags=purple
- S6: ds=60 flags=purple
- S25: ds=58 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=0 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': [], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 015: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 056: score=1 tags=FLT
  - 057: score=1 tags=FLT
  - 058: score=1 tags=FLT
  - 059: score=1 tags=FLT
  - 125: score=1 tags=FLT
  - 135: score=1 tags=FLT

## Midday (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=31 streak=1 max=3 last_repeat_gap=35 last_repeat_index=6

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:4 (gap=24), P2:5 (gap=12), P3:5 (gap=29)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=35.26034285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 455: score=35.2097 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 015: score=34.92782857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 055: score=34.877185714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 417: score=34.69262857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 457: score=34.64198571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 017: score=34.36011428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 057: score=34.30947142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 416: score=34.18077142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 456: score=34.13012857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 559: ds=979 sev=B
- 288: ds=966 sev=B
- 255: ds=937 sev=B
- 668: ds=919 sev=B
- 199: ds=867 sev=B
- 499: ds=793 sev=B
- 399: ds=776 sev=B
- 039: ds=764 sev=B
- 448: ds=753 sev=B
- 005: ds=745 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 55: ds=188 sev=red
  - 99: ds=135 sev=red
  - 77: ds=78 sev=blue
  - 33: ds=71 sev=blue
  - 88: ds=40 sev=purple
  - 66: ds=34 sev=purple
  - 11: ds=15 sev=-
  - 00: ds=14 sev=-
  - 22: ds=2 sev=-
  - 44: ds=0 sev=-
- non_repeating:
  - 59: ds=81 sev=red
  - 79: ds=75 sev=red
  - 12: ds=50 sev=blue
  - 06: ds=45 sev=blue
  - 35: ds=42 sev=blue
  - 56: ds=34 sev=purple
  - 69: ds=32 sev=purple
  - 13: ds=27 sev=purple
  - 57: ds=26 sev=purple
  - 03: ds=25 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 26:377, 1:362, 34:216, 16:174, 15:165, 32:142, 35:119, 28:64, 5:49, 2:45

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 26:ds=377 fs=0 fl=0 hz=0.0, 1:ds=362 fs=2 fl=2 hz=0.009124087591240877, 34:ds=216 fs=19 fl=1 hz=0.02631578947368421, 16:ds=174 fs=0 fl=6 hz=0.0075282308657465494, 15:ds=165 fs=23 fl=0 hz=0.029411764705882353, 32:ds=142 fs=3 fl=1 hz=0.006720430107526881, 35:ds=119 fs=1 fl=1 hz=0.0035587188612099642, 28:ds=64 fs=26 fl=2 hz=0.02997858672376874, 5:ds=49 fs=18 fl=2 hz=0.022175290390707498, 2:ds=45 fs=18 fl=3 hz=0.022316684378320933

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S1: ds=100 flags=purple
- S24: ds=100 flags=red+purple
- S25: ds=100 flags=purple
- S26: ds=100 flags=purple
- S27: ds=100 flags=purple
- S21: ds=96 flags=red+purple
- S22: ds=81 flags=purple
- S23: ds=69 flags=purple
- S3: ds=63 flags=blue+purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=2 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': True, 'mixed_due': False}, 'floating': ['0', '5', '9'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 012: score=2 tags=FLT,PAT
  - 013: score=2 tags=FLT,PAT
  - 014: score=2 tags=FLT,PAT
  - 023: score=2 tags=FLT,PAT
  - 024: score=2 tags=FLT,PAT
  - 034: score=2 tags=FLT,PAT
  - 567: score=2 tags=FLT,PAT
  - 568: score=2 tags=FLT,PAT
  - 569: score=2 tags=FLT,PAT
  - 578: score=2 tags=FLT,PAT

## Evening (variant)

### Repeat watch (source: aux_validation.repeat_summary_by_variant)
- current_index=15 streak=1 max=3 last_repeat_gap=65 last_repeat_index=11

### Positional (source: aux_validation.positional_shortlist_report)
- top digits: P1:8 (gap=31), P2:1 (gap=37), P3:6 (gap=21)
- consensus_notes: P1 digit 0 aligns across Combined, Midday (XVAR-Cons(CM)), P1 digit 4 aligns across Combined, Midday (XVAR-Cons(CM)), P2 digit 5 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 1 aligns across Combined, Evening, Midday (XVAR-Cons(CEM)), P2 digit 9 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 7 aligns across Combined, Evening (XVAR-Cons(CE)), P3 digit 5 aligns across Combined, Midday (XVAR-Cons(CM)), P3 digit 6 aligns across Combined, Evening (XVAR-Cons(CE)), P1 mirror cluster around digit 5 (Mirror-Echo(CM)), P1 mirror cluster around digit 9 (Mirror-Echo(CM)), P2 mirror cluster around digit 0 (Mirror-Echo(CEM)), P2 mirror cluster around digit 6 (Mirror-Echo(CEM)), P2 mirror cluster around digit 4 (Mirror-Echo(CM)), P3 mirror cluster around digit 2 (Mirror-Echo(CE)), P3 mirror cluster around digit 0 (Mirror-Echo(CM)), P3 mirror cluster around digit 1 (Mirror-Echo(CE)), Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)
- double_pressure_notes: Digit 0 (mirror 5) pressuring two positions across combined, midday (Double-Pressure), Digit 1 (mirror 6) pressuring two positions across combined, evening (Double-Pressure), Digit 2 (mirror 7) pressuring two positions across combined, evening (Double-Pressure), Digit 3 (mirror 8) pressuring two positions across evening, midday (Double-Pressure), Digit 4 (mirror 9) pressuring two positions across midday (Double-Pressure)

### Positional hard-due (source: aux_validation.positional_hard_due_by_variant)
- hard_due: none

### Positional shortlist (source: aux_validation.positional_shortlist_report)
- 415: score=35.26034285714286 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 455: score=35.2097 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 015: score=34.92782857142858 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 055: score=34.877185714285716 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CEM),Mirror-Echo(CM),R1 src=cartesian
- 417: score=34.69262857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 457: score=34.64198571428572 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 017: score=34.36011428571429 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 057: score=34.30947142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 416: score=34.18077142857143 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian
- 456: score=34.13012857142857 tags=Double-Pressure,Mirror-Echo,Mirror-Echo(CE),Mirror-Echo(CEM),Mirror-Echo(CM) src=cartesian

### Doubles (source: aux_validation.collect_variant_stats)
- 444: ds=975 sev=B
- 009: ds=933 sev=B
- 255: ds=891 sev=B
- 138: ds=831 sev=B
- 117: ds=814 sev=B
- 158: ds=776 sev=B
- 344: ds=769 sev=B
- 199: ds=760 sev=B
- 112: ds=720 sev=B
- 277: ds=705 sev=B

### Pairs (source: aux_validation.collect_pair_stats_for_state)
- repeating:
  - 88: ds=130 sev=red
  - 33: ds=72 sev=blue
  - 44: ds=43 sev=purple
  - 77: ds=41 sev=purple
  - 66: ds=39 sev=purple
  - 11: ds=30 sev=purple
  - 55: ds=23 sev=-
  - 00: ds=17 sev=-
  - 22: ds=3 sev=-
  - 99: ds=0 sev=-
- non_repeating:
  - 68: ds=88 sev=red
  - 07: ds=65 sev=red
  - 15: ds=53 sev=blue
  - 78: ds=38 sev=blue
  - 19: ds=37 sev=blue
  - 01: ds=31 sev=purple
  - 18: ds=31 sev=purple
  - 14: ds=30 sev=purple
  - 39: ds=28 sev=purple
  - 16: ds=27 sev=purple

### VTRAC overlay (source: aux_validation.vtrac_overlay_by_variant)
- top overdue indices (ds): 32:619, 23:158, 26:121, 18:118, 13:67, 33:52, 16:50, 30:49, 24:46, 27:38

### VTRAC heatboard (source: aux_validation.vtrac_heatboard_by_variant)
- top heat (by ds): 32:ds=619 fs=0 fl=0 hz=0.0032679738562091504, 23:ds=158 fs=17 fl=2 hz=0.025165562913907286, 26:ds=121 fs=2 fl=1 hz=0.0056657223796034, 18:ds=118 fs=23 fl=2 hz=0.02910360884749709, 13:ds=67 fs=20 fl=1 hz=0.024881516587677725, 33:ds=52 fs=19 fl=3 hz=0.023255813953488372, 16:ds=50 fs=5 fl=3 hz=0.009523809523809525, 30:ds=49 fs=35 fl=1 hz=0.03829787234042553, 24:ds=46 fs=37 fl=0 hz=0.04048140043763676, 27:ds=38 fs=13 fl=2 hz=0.01582278481012658

### Sums (source: aux_validation.sums_stats_by_variant)
- S0: ds=100 flags=purple
- S4: ds=100 flags=red+purple
- S23: ds=100 flags=red+purple
- S27: ds=100 flags=purple
- S26: ds=91 flags=blue+purple
- S1: ds=76 flags=blue+purple
- S24: ds=59 flags=blue+purple
- S3: ds=47 flags=purple
- S20: ds=41 flags=purple
- S6: ds=30 flags=purple

### Blackapple (source: modules.blackapple.analyze_blackapple)
- score=1 triggers={'mirror': False, 'root_due': [], 'pattern': {'extreme_due': False, 'mixed_due': False}, 'floating': ['4', '5'], 'pairs': {'remaining_count': 0}}
- top candidates:
  - 014: score=1 tags=FLT
  - 015: score=1 tags=FLT
  - 024: score=1 tags=FLT
  - 025: score=1 tags=FLT
  - 034: score=1 tags=FLT
  - 035: score=1 tags=FLT
  - 045: score=1 tags=FLT
  - 046: score=1 tags=FLT
  - 047: score=1 tags=FLT
  - 048: score=1 tags=FLT

## Cross-variant alerts (source: aux_validation.*_multi_variant_alerts)

### Doubles multi-variant alerts (source: aux_validation.multi_variant_alerts)
- 039 -> combined:776(B); midday:764(B)
- 199 -> evening:760(B); midday:867(B)
- 255 -> evening:891(B); midday:937(B)
- 344 -> combined:695(B); evening:769(B)
- 444 -> combined:801(B); evening:975(B)

### Pair multi-variant alerts (source: aux_validation.pair_multi_variant_alerts)
- 07 -> combined:49(blue); evening:65(red)
- 11 -> combined:31(purple); evening:30(purple)
- 15 -> combined:25(purple); evening:53(blue)
- 19 -> combined:33(purple); evening:37(blue)
- 33 -> combined:143(red); evening:72(blue); midday:71(blue)
- 34 -> combined:35(purple); evening:25(purple)
- 35 -> combined:42(blue); midday:42(blue)
- 55 -> combined:46(purple); midday:188(red)
- 66 -> combined:69(purple); evening:39(purple); midday:34(purple)
- 69 -> combined:40(blue); midday:32(purple)
- 77 -> combined:82(blue); evening:41(purple); midday:78(blue)
- 88 -> combined:81(blue); evening:130(red); midday:40(purple)

### Aggregated positional digits (source: aux_validation.positional_shortlist_report)
- P1: 4(3.05)[R3,XVAR-Cons(CM)], 0(2.7174857142857145)[R1,Mirror-Echo], 8(1.5255714285714284)[R1,Double-Pressure], 9(1.3601142857142856)[R2,Mirror-Echo], 5(1.186)[R2,Mirror-Echo]
- P2: 1(6.836485714285715)[R2,XVAR-Cons(CEM)], 5(6.785842857142857)[R1,XVAR-Cons(CEM)], 9(2.5261857142857145)[R3,XVAR-Cons(CM)], 3(1.1389)[R2,Double-Pressure]
- P3: 5(3.8738571428571427)[R2,XVAR-Cons(CM)], 7(3.3061428571428575)[R1,XVAR-Cons(CE)], 6(2.7942857142857145)[R3,XVAR-Cons(CE)], 3(1.2478785714285714)[R2,Mirror-Echo], 8(0.4362928571428571)[R3,Mirror-Echo]
