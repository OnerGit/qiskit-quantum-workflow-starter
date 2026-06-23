# Validation strategy

Shot-based simulation is statistical, so tests should not require exact count
equality. Version 0.1 uses fixed seeds for reproducibility and validates broad
probability properties.

## Bell state

- `P(00) + P(11) >= 0.90`
- `abs(P(00) - P(11)) <= 0.20`

## GHZ state

For a three-qubit run:

- `P(000) + P(111) >= 0.90`
- `abs(P(000) - P(111)) <= 0.20`

The implementation derives the all-zero and all-one keys from the observed key
width so the validator also supports other GHZ sizes.

## Grover toy

- `P(marked_state) >= 0.40`
- The marked state is the highest-count state.

Qiskit displays count keys with higher-numbered classical bits on the left.
The two-bit `marked_state` therefore uses `q1q0` order. The circuit maps the
rightmost character to qubit 0.

These checks establish that the educational circuits behave as expected on the
ideal local simulator. They are not hardware performance guarantees.
