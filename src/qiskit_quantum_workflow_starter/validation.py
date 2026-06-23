"""Probability-tolerant validation for shot-based simulation results."""

from collections.abc import Mapping
from typing import Any


def _probabilities(counts: Mapping[str, int]) -> tuple[int, dict[str, float]]:
    total = sum(counts.values())
    if total <= 0:
        return 0, {}
    return total, {state: count / total for state, count in counts.items()}


def validate_bell_counts(counts: Mapping[str, int]) -> dict[str, Any]:
    """Validate Bell-state counts without requiring exact shot totals."""
    shots, probabilities = _probabilities(counts)
    p00 = probabilities.get("00", 0.0)
    p11 = probabilities.get("11", 0.0)
    dominant_probability = p00 + p11
    balance_difference = abs(p00 - p11)
    valid = shots > 0 and dominant_probability >= 0.90 and balance_difference <= 0.20
    return {
        "valid": valid,
        "shots": shots,
        "dominant_probability": dominant_probability,
        "balance_difference": balance_difference,
        "rule": "P(00)+P(11)>=0.90 and abs(P(00)-P(11))<=0.20",
    }


def validate_ghz_counts(counts: Mapping[str, int]) -> dict[str, Any]:
    """Validate counts for an n-qubit GHZ state."""
    shots, probabilities = _probabilities(counts)
    if not counts:
        return {
            "valid": False,
            "shots": 0,
            "dominant_probability": 0.0,
            "balance_difference": 0.0,
            "rule": "all-zero/all-one probability >=0.90 and balance <=0.20",
        }

    widths = {len(state.replace(" ", "")) for state in counts}
    if len(widths) != 1:
        raise ValueError("all GHZ count keys must have the same width")
    width = widths.pop()
    zero_state = "0" * width
    one_state = "1" * width
    p_zero = probabilities.get(zero_state, 0.0)
    p_one = probabilities.get(one_state, 0.0)
    dominant_probability = p_zero + p_one
    balance_difference = abs(p_zero - p_one)
    valid = shots > 0 and dominant_probability >= 0.90 and balance_difference <= 0.20
    return {
        "valid": valid,
        "shots": shots,
        "states": [zero_state, one_state],
        "dominant_probability": dominant_probability,
        "balance_difference": balance_difference,
        "rule": (
            f"P({zero_state})+P({one_state})>=0.90 and "
            f"abs(P({zero_state})-P({one_state}))<=0.20"
        ),
    }


def validate_grover_counts(
    counts: Mapping[str, int],
    marked_state: str,
) -> dict[str, Any]:
    """Validate a two-qubit Grover result using displayed count-key order."""
    if len(marked_state) != 2 or set(marked_state) - {"0", "1"}:
        raise ValueError("marked_state must be a two-character binary string")

    shots, probabilities = _probabilities(counts)
    marked_probability = probabilities.get(marked_state, 0.0)
    highest_count_state = max(counts, key=counts.get) if counts else None
    valid = (
        shots > 0 and marked_probability >= 0.40 and highest_count_state == marked_state
    )
    return {
        "valid": valid,
        "shots": shots,
        "marked_state": marked_state,
        "marked_probability": marked_probability,
        "highest_count_state": highest_count_state,
        "rule": "P(marked_state)>=0.40 and marked_state is the highest-count state",
    }
