"""Command-line entry point for the starter demos."""

import argparse
import json
from collections.abc import Callable
from typing import Any

from .circuits import (
    create_bell_circuit,
    create_ghz_circuit,
    create_grover_toy_circuit,
)
from .simulators import run_local_simulation
from .validation import (
    validate_bell_counts,
    validate_ghz_counts,
    validate_grover_counts,
)
from .workflows import run_all_workflows


def _run_one(
    circuit_factory: Callable[[], Any],
    validator: Callable[[dict[str, int]], dict[str, Any]],
    shots: int,
    seed: int,
) -> dict[str, Any]:
    counts = run_local_simulation(circuit_factory(), shots=shots, seed_simulator=seed)
    return {"counts": counts, "validation": validator(counts)}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--demo",
        choices=("bell", "ghz", "grover", "all"),
        default="all",
        help="workflow to run",
    )
    parser.add_argument("--shots", type=int, default=1024)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--marked-state",
        default="11",
        help="two-bit Grover count key in q1q0 order",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.demo == "all":
        payload = run_all_workflows(
            shots=args.shots,
            seed_simulator=args.seed,
            marked_state=args.marked_state,
        )
    elif args.demo == "bell":
        payload = _run_one(
            create_bell_circuit, validate_bell_counts, args.shots, args.seed
        )
    elif args.demo == "ghz":
        payload = _run_one(
            create_ghz_circuit, validate_ghz_counts, args.shots, args.seed
        )
    else:
        payload = _run_one(
            lambda: create_grover_toy_circuit(args.marked_state),
            lambda counts: validate_grover_counts(counts, args.marked_state),
            args.shots,
            args.seed,
        )

    print(json.dumps(payload, indent=2, sort_keys=True))
    if args.demo == "all":
        return 0 if payload["validation_status"] == "passed" else 1
    return 0 if payload["validation"]["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
