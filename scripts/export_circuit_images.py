"""Render the three v0.1 circuits as PNG images."""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLBACKEND", "Agg")
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".matplotlib"))
sys.path.insert(0, str(ROOT / "src"))

import matplotlib.pyplot as plt  # noqa: E402

from qiskit_quantum_workflow_starter.circuits import (  # noqa: E402
    create_bell_circuit,
    create_ghz_circuit,
    create_grover_toy_circuit,
)


def main() -> int:
    output_dir = ROOT / "screenshots"
    output_dir.mkdir(parents=True, exist_ok=True)
    circuits = {
        "bell_circuit.png": create_bell_circuit(),
        "ghz_circuit.png": create_ghz_circuit(),
        "grover_circuit.png": create_grover_toy_circuit(),
    }
    for filename, circuit in circuits.items():
        figure = circuit.draw(output="mpl", fold=-1, idle_wires=False)
        path = output_dir / filename
        figure.savefig(path, bbox_inches="tight", dpi=160)
        plt.close(figure)
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
