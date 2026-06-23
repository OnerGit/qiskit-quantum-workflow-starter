import pytest

from qiskit_quantum_workflow_starter.circuits import create_grover_toy_circuit
from qiskit_quantum_workflow_starter.simulators import run_local_simulation
from qiskit_quantum_workflow_starter.validation import validate_grover_counts


def test_grover_circuit_creation():
    circuit = create_grover_toy_circuit()
    assert circuit.num_qubits == 2
    assert circuit.num_clbits == 2
    assert circuit.count_ops()["measure"] == 2
    assert circuit.count_ops()["cz"] == 2


@pytest.mark.parametrize("marked_state", ["00", "01", "10", "11"])
def test_grover_bitstring_order_and_validation(marked_state):
    counts = run_local_simulation(
        create_grover_toy_circuit(marked_state),
        shots=256,
        seed_simulator=42,
    )
    assert max(counts, key=counts.get) == marked_state
    assert validate_grover_counts(counts, marked_state)["valid"] is True


def test_grover_rejects_invalid_marked_state():
    with pytest.raises(ValueError):
        create_grover_toy_circuit("2")


def test_grover_validation_rejects_wrong_winner():
    result = validate_grover_counts({"00": 700, "11": 300}, "11")
    assert result["valid"] is False
