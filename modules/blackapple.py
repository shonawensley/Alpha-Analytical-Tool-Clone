from __future__ import annotations
from typing import Dict, List, Tuple, Set

# -------------------- Config --------------------
WINDOW_RECENT = 100
WINDOW_FLOATING = 5

THRESH_ROOT_DUE = 25           # longest-out root-sum gap
THRESH_PATTERN_EXTREME = 25    # SSS/TTT gap
THRESH_PATTERN_MIXED = 12      # SST/STS/TSS gap

REMAINING_PAIRS_MIN = 27
REMAINING_PAIRS_MAX = 29

TOP_N_CANDIDATES = 12
USE_FOUNDATION_AS_HARD_BASE = False

WEIGHTS = {"MIR": 1, "RS": 2, "PAT": 1, "FLT": 1, "PAIR": 2}

# -------------------- Utilities --------------------
MIRROR_MAP = {"0": "5", "5": "0", "1": "6", "6": "1", "2": "7", "7": "2", "3": "8", "8": "3", "4": "9", "9": "4"}


def _is_draw(s: str) -> bool:
    return isinstance(s, str) and len(s) == 3 and s.isdigit()


def _sum_digits(s: str) -> int:
    return sum(int(c) for c in s) if _is_draw(s) else 0


def _digital_root(n: int) -> int:
    return 0 if n <= 0 else 1 + ((n - 1) % 9)


def _root_sum_of_draw(s: str) -> int:
    return _digital_root(_sum_digits(s))


def _st_pattern(s: str) -> str:
    # S for 0-4, T for 5-9
    return "".join("S" if c < "5" else "T" for c in s) if _is_draw(s) else ""


def _pairs_from_draw(s: str) -> List[str]:
    if not _is_draw(s):
        return []
    a, b, c = s[0], s[1], s[2]
    return ["".join(sorted(a + b)), "".join(sorted(b + c)), "".join(sorted(a + c))]


def _remaining_nonrep_pairs(draws: List[str], window: int) -> Set[str]:
    seen: Set[str] = set()
    for d in draws[:window]:
        if not _is_draw(d):
            continue
        for p in _pairs_from_draw(d):
            if p[0] != p[1]:
                seen.add(p)
    universe: Set[str] = set()
    for i in range(10):
        for j in range(i + 1, 10):
            universe.add(f"{i}{j}")
    return universe - seen


def _has_mirror_pair(s: str) -> bool:
    if not _is_draw(s):
        return False
    a, b, c = s
    for x, y in ((a, b), (b, c), (a, c)):
        if MIRROR_MAP.get(x) == y or MIRROR_MAP.get(y) == x:
            return True
    return False


def _floating_digits(draws: List[str], window: int) -> List[str]:
    present: Set[str] = set()
    for d in draws[:window]:
        if not _is_draw(d):
            continue
        present.update(d)
    return [str(i) for i in range(10) if str(i) not in present]


def _longest_out_root_sums(draws: List[str], window: int) -> Tuple[int, List[int]]:
    # Root sums are normally 1..9, but allow 0 to avoid crashes if a draw
    # stream contains "000" placeholders (e.g., from missing values).
    last_seen = {r: None for r in range(0, 10)}
    for idx, d in enumerate(draws[:window]):
        if not _is_draw(d):
            continue
        r = _root_sum_of_draw(d)
        if last_seen[r] is None:
            last_seen[r] = idx
    gaps = {r: (window if last_seen[r] is None else last_seen[r]) for r in range(1, 10)}
    max_gap = max(gaps.values()) if gaps else 0
    roots = [r for r, g in gaps.items() if g == max_gap]
    return max_gap, roots


def _pattern_due_flags(draws: List[str], window: int) -> Dict[str, bool]:
    last_sss = None
    last_ttt = None
    last_mixed = None
    for idx, d in enumerate(draws[:window]):
        pat = _st_pattern(d)
        if pat == "":
            continue
        if pat == "SSS" and last_sss is None:
            last_sss = idx
        elif pat == "TTT" and last_ttt is None:
            last_ttt = idx
        elif pat in ("SST", "STS", "TSS") and last_mixed is None:
            last_mixed = idx
        if last_sss is not None and last_ttt is not None and last_mixed is not None:
            break
    gap_sss = WINDOW_RECENT if last_sss is None else last_sss
    gap_ttt = WINDOW_RECENT if last_ttt is None else last_ttt
    gap_mixed = WINDOW_RECENT if last_mixed is None else last_mixed
    return {
        "extreme_due": (gap_sss >= THRESH_PATTERN_EXTREME) or (gap_ttt >= THRESH_PATTERN_EXTREME),
        "mixed_due": gap_mixed >= THRESH_PATTERN_MIXED,
    }


def _boxed_singles_unordered() -> List[str]:
    combos: List[str] = []
    for a in range(10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                combos.append(f"{a}{b}{c}")
    return combos


def _score_combo(
    combo: str,
    triggers: Dict,
    foundation_pairs: Set[str],
    floating: Set[str],
    due_roots: Set[int],
    pat_flags: Dict[str, bool],
) -> Tuple[int, Set[str]]:
    score = 0
    tags: Set[str] = set()
    pairs = [
        "".join(sorted(combo[0] + combo[1])),
        "".join(sorted(combo[1] + combo[2])),
        "".join(sorted(combo[0] + combo[2])),
    ]
    if any(p in foundation_pairs for p in pairs):
        score += WEIGHTS["PAIR"]
        tags.add("PAIR")
    if any(d in floating for d in combo):
        score += WEIGHTS["FLT"]
        tags.add("FLT")
    rs = _digital_root(_sum_digits(combo))
    if rs in due_roots and triggers.get("root_due"):
        score += WEIGHTS["RS"]
        tags.add("RS")
    pat = _st_pattern(combo)
    if pat in ("SSS", "TTT") and pat_flags.get("extreme_due"):
        score += WEIGHTS["PAT"]
        tags.add("PAT")
    elif pat in ("SST", "STS", "TSS") and pat_flags.get("mixed_due"):
        score += WEIGHTS["PAT"]
        tags.add("PAT")
    if _has_mirror_pair(combo) and triggers.get("mirror"):
        score += WEIGHTS["MIR"]
        tags.add("MIR")
    return score, tags


def analyze_blackapple(draws: List[str]) -> Dict:
    if not isinstance(draws, list) or not draws:
        return {"score": 0, "triggers": {}, "candidates": []}
    norm = [d for d in draws if _is_draw(d)]
    if not norm:
        return {"score": 0, "triggers": {}, "candidates": []}

    latest = norm[0]
    trig_mirror = _has_mirror_pair(latest)

    max_gap, due_roots = _longest_out_root_sums(norm, WINDOW_RECENT)
    trig_root_due = max_gap >= THRESH_ROOT_DUE

    pat_flags = _pattern_due_flags(norm, WINDOW_RECENT)

    floating_list = _floating_digits(norm, WINDOW_FLOATING)
    trig_floating = len(floating_list) >= 2

    remaining_pairs = _remaining_nonrep_pairs(norm, WINDOW_RECENT)
    rp_count = len(remaining_pairs)
    trig_pairs = REMAINING_PAIRS_MIN <= rp_count <= REMAINING_PAIRS_MAX

    triggers = {
        "mirror": bool(trig_mirror),
        "root_due": list(sorted(due_roots)) if trig_root_due else [],
        "pattern": pat_flags,
        "floating": floating_list if trig_floating else [],
        "pairs": {"remaining_count": rp_count},
    }

    trigger_score = 0
    if trig_mirror:
        trigger_score += 1
    if trig_root_due:
        trigger_score += 1
    if pat_flags.get("extreme_due") or pat_flags.get("mixed_due"):
        trigger_score += 1
    if trig_floating:
        trigger_score += 1
    if trig_pairs:
        trigger_score += 1

    foundation_pairs = remaining_pairs if trig_pairs else set()
    floating_set = set(floating_list)
    due_roots_set = set(due_roots) if trig_root_due else set()

    candidates: List[Dict] = []
    for combo in _boxed_singles_unordered():
        if USE_FOUNDATION_AS_HARD_BASE and not any(
            p in foundation_pairs for p in _pairs_from_draw(combo)
        ):
            continue
        score, tags = _score_combo(
            combo, triggers, foundation_pairs, floating_set, due_roots_set, pat_flags
        )
        if score > 0:
            candidates.append({"combo": combo, "score": score, "tags": tags})

    candidates.sort(key=lambda x: (-x["score"], x["combo"]))
    return {"score": trigger_score, "triggers": triggers, "candidates": candidates[:TOP_N_CANDIDATES]}


def ba_status_label(score: int) -> str:
    if score >= 3:
        return "ALERT"
    if score == 2:
        return "WATCH"
    return "OFF"


def sum_tags(combo: str) -> Dict[str, int]:
    s = _sum_digits(combo)
    return {"Sigma": s, "sD": s % 10, "RS": _digital_root(s)}
