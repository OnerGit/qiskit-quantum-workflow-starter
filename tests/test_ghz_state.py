import pytest

from qiskit_quantum_workflow_starter.circuits import create_ghz_circuit
from qiskit_quantum_workflow_starter.simulators import run_local_simulation
from qiskit_quantum_workflow_starter.validation import validate_ghz_counts


def test_ghz_circuit_creation():
    circuit = create_ghz_circuit()
    assert circuit.num_qubits == 3
    assert circuit.num_clbits == 3
    assert circuit.count_ops()["h"] == 1
    assert circuit.count_ops()["cx"] == 2
    assert circuit.count_ops()["measure"] == 3


def test_ghz_rejects_too_few_qubits():
    with pytest.raises(ValueError):
        create_ghz_circuit(1)


def test_ghz_simulation_and_validation():
    counts = run_local_simulation(create_ghz_circuit(), shots=512)
    assert sum(counts.values()) == 512
    assert validate_ghz_counts(counts)["valid"] is True


def test_ghz_probability_tolerance():
    assert validate_ghz_counts({"000": 500, "111": 500})["valid"] is True
    assert validate_ghz_counts({"000": 500, "001": 500})["valid"] is False
