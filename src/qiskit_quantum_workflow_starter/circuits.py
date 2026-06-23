"""Circuit builders for the starter workflows."""

from qiskit import QuantumCircuit


def create_bell_circuit() -> QuantumCircuit:
    """Create a measured two-qubit Bell-state circuit."""
    circuit = QuantumCircuit(2, 2, name="bell")
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    return circuit


def create_ghz_circuit(num_qubits: int = 3) -> QuantumCircuit:
    """Create a measured GHZ circuit with a CNOT chain."""
    if num_qubits < 2:
        raise ValueError("num_qubits must be at least 2")

    circuit = QuantumCircuit(num_qubits, num_qubits, name=f"ghz_{num_qubits}")
    circuit.h(0)
    for control in range(num_qubits - 1):
        circuit.cx(control, control + 1)
    circuit.measure(range(num_qubits), range(num_qubits))
    return circuit


def create_grover_toy_circuit(marked_state: str = "11") -> QuantumCircuit:
    """Create a measured two-qubit Grover search circuit.

    ``marked_state`` follows Qiskit's displayed count-key order: the left
    character is q1 and the right character is q0.
    """
    if len(marked_state) != 2 or set(marked_state) - {"0", "1"}:
        raise ValueError("marked_state must be a two-character binary string")

    circuit = QuantumCircuit(2, 2, name=f"grover_{marked_state}")
    circuit.h([0, 1])

    # Phase oracle. Reverse the key so character positions map to q0, q1.
    zero_qubits = [
        qubit for qubit, bit in enumerate(reversed(marked_state)) if bit == "0"
    ]
    if zero_qubits:
        circuit.x(zero_qubits)
    circuit.cz(0, 1)
    if zero_qubits:
        circuit.x(zero_qubits)

    # Two-qubit diffuser.
    circuit.h([0, 1])
    circuit.x([0, 1])
    circuit.cz(0, 1)
    circuit.x([0, 1])
    circuit.h([0, 1])
    circuit.measure([0, 1], [0, 1])
    return circuit
