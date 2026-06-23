# Workflow overview

Each v0.1 workflow follows the same small pipeline:

1. Build a measured circuit.
2. Transpile it for a local Aer simulator.
3. Run a fixed number of shots with a fixed simulator seed.
4. Convert Qiskit counts to a plain JSON-compatible dictionary.
5. Apply a probability-tolerant validation rule.
6. Export machine-readable JSON and a human-readable Markdown report.

The shared structure keeps the examples easy to compare without introducing a
framework or unnecessary abstraction.

## Included demos

- **Bell state:** two-qubit correlation.
- **GHZ state:** configurable multi-qubit correlation, demonstrated with three
  qubits.
- **Grover toy:** a two-qubit educational oracle and diffuser example.

All execution is local in v0.1.
