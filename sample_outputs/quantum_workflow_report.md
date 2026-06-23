# Quantum Workflow Report

## Project overview

- Project: `qiskit-quantum-workflow-starter`
- Version: `0.1.0`
- Backend: `AerSimulator (local)`
- Shots per demo: `1024`
- Simulator seed: `42`
- Generated at: `2026-06-23T07:16:09.846478+00:00`

Version 0.1 uses local simulation only and makes no quantum advantage claim.

## Bell state result

Two-qubit Bell-state correlation demo.

- Counts: `00`: 521, `11`: 503
- Validation: **PASS**
- Rule: P(00)+P(11)>=0.90 and abs(P(00)-P(11))<=0.20

## GHZ state result

Three-qubit GHZ correlation demo.

- Counts: `000`: 490, `111`: 534
- Validation: **PASS**
- Rule: P(000)+P(111)>=0.90 and abs(P(000)-P(111))<=0.20

## Grover toy result

Two-qubit educational Grover search toy.

- Counts: `11`: 1024
- Validation: **PASS**
- Rule: P(marked_state)>=0.40 and marked_state is the highest-count state
- Marked state: `11` (count-key order `q1q0`)

## Validation summary

Overall status: **PASSED**.

Validation is probability-tolerant because shot-based simulation is statistical; exact count equality is not expected.

## Limitations

Small educational circuits on an ideal local simulator; no hardware, noise model, error mitigation, or quantum advantage claim.

## Reproducibility notes

- All demos use the local Aer simulator.
- Each demo uses `1024` shots.
- The simulator and transpiler seed is `42`.
- No hardware backend was used.
- No IBM token is required.
