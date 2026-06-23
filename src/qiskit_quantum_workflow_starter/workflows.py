"""Composition layer for circuit, simulation, and validation workflows."""

from datetime import datetime, timezone
from typing import Any

from .circuits import (
    create_bell_circuit,
    create_ghz_circuit,
    create_grover_toy_circuit,
)
from .simulators import run_local_simulation
from .validation import (
    validate_bell_counts,
    validate_ghz_counts,
    validate_grover_counts,
)

PROJECT_NAME = "qiskit-quantum-workflow-starter"
VERSION = "0.1.0"
BACKEND_NAME = "AerSimulator (local)"


def run_all_workflows(
    shots: int = 1024,
    seed_simulator: int = 42,
    marked_state: str = "11",
) -> dict[str, Any]:
    """Run all v0.1 workflows and return a report-ready result mapping."""
    bell_counts = run_local_simulation(
        create_bell_circuit(), shots=shots, seed_simulator=seed_simulator
    )
    ghz_counts = run_local_simulation(
        create_ghz_circuit(), shots=shots, seed_simulator=seed_simulator
    )
    grover_counts = run_local_simulation(
        create_grover_toy_circuit(marked_state),
        shots=shots,
        seed_simulator=seed_simulator,
    )

    demos = {
        "bell": {
            "description": "Two-qubit Bell-state correlation demo",
            "counts": bell_counts,
            "validation": validate_bell_counts(bell_counts),
        },
        "ghz": {
            "description": "Three-qubit GHZ correlation demo",
            "counts": ghz_counts,
            "validation": validate_ghz_counts(ghz_counts),
        },
        "grover": {
            "description": "Two-qubit educational Grover search toy",
            "marked_state": marked_state,
            "bitstring_order": "q1q0",
            "counts": grover_counts,
            "validation": validate_grover_counts(grover_counts, marked_state),
        },
    }
    all_valid = all(demo["validation"]["valid"] for demo in demos.values())
    return {
        "project": PROJECT_NAME,
        "version": VERSION,
        "backend": BACKEND_NAME,
        "shots": shots,
        "seed_simulator": seed_simulator,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "demos": demos,
        "validation_status": "passed" if all_valid else "failed",
        "limitations_summary": (
            "Small educational circuits on an ideal local simulator; no hardware, "
            "noise model, error mitigation, or quantum advantage claim."
        ),
        "no_hardware_backend_used": True,
        "ibm_token_required": False,
    }
