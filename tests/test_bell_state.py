from qiskit_quantum_workflow_starter.circuits import create_bell_circuit
from qiskit_quantum_workflow_starter.simulators import run_local_simulation
from qiskit_quantum_workflow_starter.validation import validate_bell_counts


def test_bell_circuit_creation():
    circuit = create_bell_circuit()
    assert circuit.num_qubits == 2
    assert circuit.num_clbits == 2
    assert circuit.count_ops()["h"] == 1
    assert circuit.count_ops()["cx"] == 1
    assert circuit.count_ops()["measure"] == 2


def test_bell_simulation_and_validation():
    counts = run_local_simulation(create_bell_circuit(), shots=512)
    assert sum(counts.values()) == 512
    assert validate_bell_counts(counts)["valid"] is True


def test_bell_probability_tolerance():
    assert validate_bell_counts({"00": 490, "11": 510})["valid"] is True
    assert validate_bell_counts({"00": 800, "11": 200})["valid"] is False
