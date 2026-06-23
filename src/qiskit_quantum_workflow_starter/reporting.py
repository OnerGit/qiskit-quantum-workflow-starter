"""JSON and Markdown reporting helpers."""

import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any

COUNT_FILENAMES = {
    "bell": "bell_counts.json",
    "ghz": "ghz_counts.json",
    "grover": "grover_counts.json",
}


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def export_counts_json(
    results: Mapping[str, Any],
    output_dir: str | Path = "sample_outputs",
) -> dict[str, str]:
    """Write per-demo counts and a complete workflow summary."""
    output_path = Path(output_dir)
    written: dict[str, str] = {}

    for demo_name, filename in COUNT_FILENAMES.items():
        path = output_path / filename
        _write_json(path, results["demos"][demo_name]["counts"])
        written[demo_name] = path.as_posix()

    summary_path = output_path / "quantum_workflow_summary.json"
    summary = dict(results)
    summary["counts_file_path"] = {
        demo_name: (Path(output_path.name) / filename).as_posix()
        for demo_name, filename in COUNT_FILENAMES.items()
    }
    _write_json(summary_path, summary)
    written["summary"] = summary_path.as_posix()
    return written


def _format_counts(counts: Mapping[str, int]) -> str:
    return ", ".join(f"`{state}`: {count}" for state, count in sorted(counts.items()))


def generate_markdown_report(
    results: Mapping[str, Any],
    output_path: str | Path | None = None,
) -> str:
    """Create a human-readable report and optionally write it to disk."""
    demos = results["demos"]
    lines = [
        "# Quantum Workflow Report",
        "",
        "## Project overview",
        "",
        f"- Project: `{results['project']}`",
        f"- Version: `{results['version']}`",
        f"- Backend: `{results['backend']}`",
        f"- Shots per demo: `{results['shots']}`",
        f"- Simulator seed: `{results['seed_simulator']}`",
        f"- Generated at: `{results['timestamp']}`",
        "",
        "Version 0.1 uses local simulation only and makes no quantum advantage claim.",
        "",
    ]

    sections = [
        ("bell", "Bell state result"),
        ("ghz", "GHZ state result"),
        ("grover", "Grover toy result"),
    ]
    for demo_name, heading in sections:
        demo = demos[demo_name]
        validation = demo["validation"]
        lines.extend(
            [
                f"## {heading}",
                "",
                demo["description"] + ".",
                "",
                f"- Counts: {_format_counts(demo['counts'])}",
                f"- Validation: **{'PASS' if validation['valid'] else 'FAIL'}**",
                f"- Rule: {validation['rule']}",
                "",
            ]
        )
        if demo_name == "grover":
            lines.insert(
                len(lines) - 1,
                (
                    f"- Marked state: `{demo['marked_state']}` "
                    f"(count-key order `{demo['bitstring_order']}`)"
                ),
            )

    lines.extend(
        [
            "## Validation summary",
            "",
            f"Overall status: **{results['validation_status'].upper()}**.",
            "",
            "Validation is probability-tolerant because shot-based simulation is "
            "statistical; exact count equality is not expected.",
            "",
            "## Limitations",
            "",
            results["limitations_summary"],
            "",
            "## Reproducibility notes",
            "",
            "- All demos use the local Aer simulator.",
            f"- Each demo uses `{results['shots']}` shots.",
            f"- The simulator and transpiler seed is `{results['seed_simulator']}`.",
            "- No hardware backend was used.",
            "- No IBM token is required.",
            "",
        ]
    )
    report = "\n".join(lines)
    if output_path is not None:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report, encoding="utf-8")
    return report
