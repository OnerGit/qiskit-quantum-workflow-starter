import json

import pytest

from qiskit_quantum_workflow_starter.cli import main


@pytest.mark.parametrize("demo", ["bell", "ghz", "grover", "all"])
def test_cli_basic_execution(demo, capsys):
    exit_code = main(["--demo", demo, "--shots", "128"])
    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    if demo == "all":
        assert payload["validation_status"] == "passed"
    else:
        assert payload["validation"]["valid"] is True
