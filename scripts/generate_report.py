"""Generate all JSON outputs and the Markdown workflow report."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qiskit_quantum_workflow_starter.reporting import (  # noqa: E402
    export_counts_json,
    generate_markdown_report,
)
from qiskit_quantum_workflow_starter.workflows import run_all_workflows  # noqa: E402


def main() -> int:
    results = run_all_workflows()
    output_dir = ROOT / "sample_outputs"
    written = export_counts_json(results, output_dir)
    report_path = output_dir / "quantum_workflow_report.md"
    generate_markdown_report(results, report_path)

    for name, path in written.items():
        print(f"{name}: {path}")
    print(f"report: {report_path}")
    return 0 if results["validation_status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
