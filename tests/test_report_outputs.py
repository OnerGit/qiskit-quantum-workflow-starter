import json

from qiskit_quantum_workflow_starter.reporting import (
    export_counts_json,
    generate_markdown_report,
)
from qiskit_quantum_workflow_starter.workflows import run_all_workflows


def test_report_and_summary_generation(tmp_path):
    results = run_all_workflows(shots=128)
    written = export_counts_json(results, tmp_path)
    report_path = tmp_path / "quantum_workflow_report.md"
    report = generate_markdown_report(results, report_path)

    assert report_path.read_text(encoding="utf-8") == report
    for heading in (
        "Project overview",
        "Bell state result",
        "GHZ state result",
        "Grover toy result",
        "Validation summary",
        "Limitations",
        "Reproducibility notes",
    ):
        assert heading in report

    summary = json.loads((tmp_path / "quantum_workflow_summary.json").read_text())
    assert summary["project"] == "qiskit-quantum-workflow-starter"
    assert summary["version"] == "0.1.0"
    assert summary["no_hardware_backend_used"] is True
    assert summary["ibm_token_required"] is False
    assert summary["validation_status"] == "passed"
    assert set(summary["counts_file_path"]) == {"bell", "ghz", "grover"}
    assert written["summary"].endswith("quantum_workflow_summary.json")
