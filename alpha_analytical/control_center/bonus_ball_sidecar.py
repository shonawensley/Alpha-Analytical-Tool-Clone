from __future__ import annotations

from dataclasses import asdict, dataclass
import re
import unicodedata
from typing import Dict, List, Optional, Tuple

from alpha_analytical.control_center.batch_runner import parse_winner_sheet


BONUS_LABEL_RE = re.compile(r"\b(Fireball|Wild Ball|Superball)\s*:\s*(\d)\b", flags=re.IGNORECASE)
DRAW_RE = re.compile(r"(\d)\D+(\d)\D+(\d)")


def _normalize_token(value: str) -> str:
    if not value:
        return ""
    text = unicodedata.normalize("NFKD", value)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "", text.lower())


@dataclass(frozen=True)
class BonusBallStateConfig:
    project_state: str
    slot_labels: Dict[str, str]


SUPPORTED_BONUS_STATES: Dict[str, BonusBallStateConfig] = {
    "Connecticut": BonusBallStateConfig(
        project_state="Connecticut4",
        slot_labels={
            _normalize_token("Play 3 Day"): "Midday",
            _normalize_token("Play 3 Night"): "Evening",
        },
    ),
    "Florida": BonusBallStateConfig(
        project_state="Florida4",
        slot_labels={
            _normalize_token("Pick 3 Midday"): "Midday",
            _normalize_token("Pick 3 Evening"): "Evening",
        },
    ),
    "Indiana": BonusBallStateConfig(
        project_state="Indiana4",
        slot_labels={
            _normalize_token("Daily 3 Midday"): "Midday",
            _normalize_token("Daily 3 Evening"): "Evening",
        },
    ),
    "New Jersey": BonusBallStateConfig(
        project_state="NewJersey4",
        slot_labels={
            _normalize_token("Pick 3 Midday"): "Midday",
            _normalize_token("Pick 3 Evening"): "Evening",
        },
    ),
    "North Carolina": BonusBallStateConfig(
        project_state="NorthCarolina4",
        slot_labels={
            _normalize_token("Pick 3 Daytime"): "Midday",
            _normalize_token("Pick 3 Evening"): "Evening",
        },
    ),
    "Pennsylvania": BonusBallStateConfig(
        project_state="Pennsylvania4",
        slot_labels={
            _normalize_token("Pick 3 Day"): "Midday",
            _normalize_token("Pick 3 Evening"): "Evening",
        },
    ),
    "Puerto Rico": BonusBallStateConfig(
        project_state="PuertoRico4",
        slot_labels={
            _normalize_token("Pega 3 Día"): "Midday",
            _normalize_token("Pega 3 Noche"): "Evening",
        },
    ),
    "South Carolina": BonusBallStateConfig(
        project_state="SouthCarolina4",
        slot_labels={
            _normalize_token("Pick 3 Midday"): "Midday",
            _normalize_token("Pick 3 Evening"): "Evening",
        },
    ),
    "Virginia": BonusBallStateConfig(
        project_state="Virginia4",
        slot_labels={
            _normalize_token("Pick 3 Day"): "Midday",
            _normalize_token("Pick 3 Night"): "Evening",
        },
    ),
}


SUPPORTED_BONUS_STATE_TOKENS: Dict[str, str] = {
    _normalize_token(canonical): canonical for canonical in SUPPORTED_BONUS_STATES
}


@dataclass(frozen=True)
class BonusBallSourceRow:
    state_label_raw: str
    canonical: str
    project_state: str
    game_label_raw: str
    draw_date_raw: str
    slot: Optional[str]
    sidecar_draw: Optional[str]
    bonus_label_raw: Optional[str]
    bonus_label_norm: Optional[str]
    bonus_digit: Optional[str]


@dataclass(frozen=True)
class BonusBallParityRow:
    results_date: str
    state_label_raw: str
    canonical: str
    project_state: str
    slot: Optional[str]
    game_label_raw: str
    draw_date_raw: str
    core_draw: Optional[str]
    sidecar_draw: Optional[str]
    bonus_label_raw: Optional[str]
    bonus_label_norm: Optional[str]
    bonus_digit: Optional[str]
    status: str
    reason: str
    accepted: bool


def parse_bonus_ball_source(text: str) -> List[BonusBallSourceRow]:
    rows: List[BonusBallSourceRow] = []
    current_state_label: Optional[str] = None
    current_canonical: Optional[str] = None
    current_config: Optional[BonusBallStateConfig] = None

    for raw in text.splitlines():
        line = raw.strip()
        if not line or line == ":":
            continue

        head_norm = _normalize_token(line)
        if head_norm in {"bothmiddayandeveningresults", "gamedrawdateresults"}:
            continue

        parts = [part.strip() for part in raw.split("\t")]
        if len(parts) == 1:
            current_state_label = parts[0].strip()
            current_canonical = SUPPORTED_BONUS_STATE_TOKENS.get(_normalize_token(current_state_label))
            current_config = SUPPORTED_BONUS_STATES.get(current_canonical) if current_canonical else None
            continue

        if not current_canonical or not current_config or not current_state_label:
            continue

        game_label_raw = parts[0] if parts else ""
        draw_date_raw = parts[1] if len(parts) >= 2 else ""
        results_field = parts[2] if len(parts) >= 3 else parts[-1]

        slot = current_config.slot_labels.get(_normalize_token(game_label_raw))
        draw_match = DRAW_RE.search(results_field)
        sidecar_draw = "".join(draw_match.groups()) if draw_match else None

        bonus_match = BONUS_LABEL_RE.search(results_field)
        bonus_label_raw = None
        bonus_label_norm = None
        bonus_digit = None
        if bonus_match:
            bonus_label_raw = bonus_match.group(1)
            bonus_label_norm = _normalize_token(bonus_label_raw)
            bonus_digit = bonus_match.group(2)

        rows.append(
            BonusBallSourceRow(
                state_label_raw=current_state_label,
                canonical=current_canonical,
                project_state=current_config.project_state,
                game_label_raw=game_label_raw,
                draw_date_raw=draw_date_raw,
                slot=slot,
                sidecar_draw=sidecar_draw,
                bonus_label_raw=bonus_label_raw,
                bonus_label_norm=bonus_label_norm,
                bonus_digit=bonus_digit,
            )
        )

    return rows


def load_core_results_map(text: str) -> Dict[Tuple[str, str], str]:
    core: Dict[Tuple[str, str], str] = {}
    for entry in parse_winner_sheet(text):
        if entry.midday:
            core[(entry.canonical, "Midday")] = entry.midday
        if entry.evening:
            core[(entry.canonical, "Evening")] = entry.evening
    return core


def apply_bonus_ball_parity(
    *,
    results_date: str,
    core_results_text: str,
    bonus_results_text: str,
) -> List[BonusBallParityRow]:
    core_draws = load_core_results_map(core_results_text)
    out: List[BonusBallParityRow] = []

    for row in parse_bonus_ball_source(bonus_results_text):
        core_draw = core_draws.get((row.canonical, row.slot or ""))
        status = "accepted"
        reason = "parity_match"
        accepted = True

        if not row.slot:
            status = "rejected"
            reason = "unsupported_game_label"
            accepted = False
        elif not row.sidecar_draw:
            status = "rejected"
            reason = "missing_sidecar_draw"
            accepted = False
        elif not row.bonus_digit or not row.bonus_label_raw:
            status = "skipped"
            reason = "no_bonus_ball"
            accepted = False
        elif not core_draw:
            status = "rejected"
            reason = "core_draw_missing"
            accepted = False
        elif core_draw != row.sidecar_draw:
            status = "rejected"
            reason = "draw_mismatch"
            accepted = False

        out.append(
            BonusBallParityRow(
                results_date=results_date,
                state_label_raw=row.state_label_raw,
                canonical=row.canonical,
                project_state=row.project_state,
                slot=row.slot,
                game_label_raw=row.game_label_raw,
                draw_date_raw=row.draw_date_raw,
                core_draw=core_draw,
                sidecar_draw=row.sidecar_draw,
                bonus_label_raw=row.bonus_label_raw,
                bonus_label_norm=row.bonus_label_norm,
                bonus_digit=row.bonus_digit,
                status=status,
                reason=reason,
                accepted=accepted,
            )
        )

    return out


def summarize_bonus_ball_parity(rows: List[BonusBallParityRow]) -> Dict[str, object]:
    summary: Dict[str, object] = {
        "rows_total": len(rows),
        "accepted_rows": 0,
        "rejected_rows": 0,
        "skipped_rows": 0,
        "accepted_by_bonus_label": {},
        "rows_by_state": [],
    }
    accepted_by_label: Dict[str, int] = {}
    per_state: Dict[str, Dict[str, object]] = {}

    for row in rows:
        if row.status == "accepted":
            summary["accepted_rows"] = int(summary["accepted_rows"]) + 1
            if row.bonus_label_raw:
                accepted_by_label[row.bonus_label_raw] = accepted_by_label.get(row.bonus_label_raw, 0) + 1
        elif row.status == "rejected":
            summary["rejected_rows"] = int(summary["rejected_rows"]) + 1
        else:
            summary["skipped_rows"] = int(summary["skipped_rows"]) + 1

        state_bucket = per_state.setdefault(
            row.project_state,
            {
                "canonical": row.canonical,
                "project_state": row.project_state,
                "rows": 0,
                "accepted_rows": 0,
                "rejected_rows": 0,
                "skipped_rows": 0,
            },
        )
        state_bucket["rows"] = int(state_bucket["rows"]) + 1
        state_bucket[f"{row.status}_rows"] = int(state_bucket[f"{row.status}_rows"]) + 1

    summary["accepted_by_bonus_label"] = accepted_by_label
    summary["rows_by_state"] = list(per_state.values())
    return summary


def build_bonus_ball_truth_payload(
    *,
    results_date: str,
    core_results_text: str,
    bonus_results_text: str,
    core_results_path: Optional[str] = None,
    bonus_results_path: Optional[str] = None,
) -> Dict[str, object]:
    rows = apply_bonus_ball_parity(
        results_date=results_date,
        core_results_text=core_results_text,
        bonus_results_text=bonus_results_text,
    )
    return {
        "metadata": {
            "results_date": results_date,
            "core_results_path": core_results_path,
            "bonus_results_path": bonus_results_path,
            "supported_bonus_states": [
                {
                    "canonical": canonical,
                    "project_state": config.project_state,
                }
                for canonical, config in SUPPORTED_BONUS_STATES.items()
            ],
        },
        "summary": summarize_bonus_ball_parity(rows),
        "rows": [asdict(row) for row in rows],
    }
