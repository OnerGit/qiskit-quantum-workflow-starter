from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_no_real_env_file_exists():
    assert not (ROOT / ".env").exists()


def test_env_example_has_no_secret_value():
    text = (ROOT / ".env.example").read_text(encoding="utf-8")
    active_assignments = [
        line
        for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith("#") and "=" in line
    ]
    assert active_assignments == []
