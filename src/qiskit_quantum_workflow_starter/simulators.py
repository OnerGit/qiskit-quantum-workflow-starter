"""Local simulator helpers."""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def run_local_simulation(
    circuit: QuantumCircuit,
    shots: int = 1024,
    seed_simulator: int = 42,
) -> dict[str, int]:
    """Run a circuit on a local Aer simulator and return plain counts."""
    if shots <= 0:
        raise ValueError("shots must be positive")

    backend = AerSimulator()
    compiled = transpile(circuit, backend, seed_transpiler=seed_simulator)
    result = backend.run(
        compiled,
        shots=shots,
        seed_simulator=seed_simulator,
    ).result()
    return {str(key): int(value) for key, value in result.get_counts(compiled).items()}
