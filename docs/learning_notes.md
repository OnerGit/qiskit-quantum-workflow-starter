# Learning notes

## Measurement ordering

Qiskit count keys are displayed from the highest classical bit to the lowest.
For a circuit that measures qubit 0 into classical bit 0 and qubit 1 into
classical bit 1, the key `01` means `q1=0` and `q0=1`.

## Reproducibility

A fixed simulator seed makes portfolio examples and tests repeatable. Validation
still uses probability thresholds rather than exact counts so the intent of the
test remains clear.

## Separation of concerns

Circuit construction, simulation, validation, reporting, and CLI handling live
in separate modules. This is enough structure to keep the project maintainable
without turning three small demos into a large application.
