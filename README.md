# Qiskit Quantum Workflow Starter

A small, reproducible Qiskit workflow starter for local quantum circuit simulation, validation, and reporting.

## Project positioning

This is an educational Qiskit workflow starter focused on reproducible local simulation, validation, and reporting. Version
0.1 focuses on readable engineering practices around small local simulations:
deterministic configuration, probability-tolerant validation, tests, command
line usage, and public-safe JSON and Markdown outputs.

This project does not demonstrate quantum advantage. It is not a
production-ready quantum workload, and it does not make claims about useful
hardware performance.

## Why this project exists

Small quantum examples are easy to run once and surprisingly easy to make hard
to reproduce. This repository packages three familiar circuits into a compact
workflow that can be rerun, tested, inspected, and shared without private
cloud credentials.

## What this project demonstrates

- Modern Qiskit 2.x-compatible circuit construction
- Local simulation with `qiskit-aer`
- Bell, GHZ, and two-qubit Grover toy workflows
- Seeded, shot-based runs and probability-tolerant validation
- JSON and Markdown report generation
- CLI and script entry points
- Pytest coverage and public-safe sample artifacts

## What this project does not claim

- No quantum advantage is claimed.
- No production quantum workload is implemented.
- No industrial optimization problem is solved.
- No hardware accuracy or performance is promised.

## Tech stack

- Python 3.10+
- Qiskit 2.x
- Qiskit Aer
- Matplotlib
- pytest and Ruff

## Quickstart

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pip install -e .
pytest
python scripts/run_all_demos.py
python scripts/generate_report.py
python scripts/export_circuit_images.py
```

Version 0.1 uses local simulation only. No IBM token or credential should be
committed, and none is required to run the project.

### Tested environment

Local validation was completed with Python 3.12, Qiskit 2.4.2, and Qiskit Aer
0.17.2. Dependency requirements remain flexible at `qiskit>=2.0,<3` and
`qiskit-aer>=0.17`.

## Demo workflows

```powershell
python -m qiskit_quantum_workflow_starter.cli --demo bell
python -m qiskit_quantum_workflow_starter.cli --demo ghz
python -m qiskit_quantum_workflow_starter.cli --demo grover
python -m qiskit_quantum_workflow_starter.cli --demo all
python scripts/run_all_demos.py
```

The Grover toy uses Qiskit's displayed count-key convention. For a two-qubit
key such as `01`, the left character corresponds to `q1` and the right
character corresponds to `q0`.

## Sample outputs

Generate reproducible artifacts with:

```powershell
python scripts/generate_report.py
```

The `sample_outputs/` directory contains per-demo count files, a machine-readable
summary, and a Markdown report.

## Validation strategy

Validation checks probability ranges rather than exact counts:

- Bell: at least 90% combined probability on `00` and `11`, with their
  probabilities within 0.20.
- GHZ: at least 90% combined probability on the all-zero and all-one states,
  with their probabilities within 0.20.
- Grover toy: at least 40% probability on the marked state, which must also be
  the highest-count state.

See [docs/validation_strategy.md](docs/validation_strategy.md) for details.

## Screenshots

Circuit images can be generated with:

```powershell
python scripts/export_circuit_images.py
```

Terminal, test, and report-preview screenshots must be captured manually. See
[screenshots/README.md](screenshots/README.md) for the public-safety checklist.

## Limitations

Version 0.1 contains small educational circuits, an ideal local simulator, no
noise model, no error mitigation, and no hardware execution. See
[docs/limitations.md](docs/limitations.md).

## Roadmap

- **v0.1:** local simulation, validation, reporting, tests, and documentation
- **Future, optional:** IBM Quantum backend execution with explicit credential
  handling
- **Future, optional:** noise-aware experiments and richer result comparison

IBM Quantum backend execution is optional future work and is deliberately not
implemented in v0.1.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE) and
[NOTICE.md](NOTICE.md).
