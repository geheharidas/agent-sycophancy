"""Tests for agent_honesty CLI entrypoint."""

from pathlib import Path
import tempfile
import pytest

from agent_honesty.cli import main


def test_cli_version(capsys):
    with pytest.raises(SystemExit) as excinfo:
        main(["--version"])
    assert excinfo.value.code == 0
    captured = capsys.readouterr()
    assert "agent-honesty" in captured.out


def test_cli_audit_pass(capsys):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write("# Clean Architecture\nVerified facts only.")
        temp_path = Path(f.name)
    try:
        code = main(["audit", str(temp_path)])
        assert code == 0
        captured = capsys.readouterr()
        assert "Honesty-Audit Verdict: PASS" in captured.out
    finally:
        temp_path.unlink()


def test_cli_audit_fail(capsys):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write("# Broken Review\nYou are right, let us ignore.")
        temp_path = Path(f.name)
    try:
        code = main(["audit", str(temp_path)])
        assert code == 1
        captured = capsys.readouterr()
        assert "Honesty-Audit Verdict: FAIL" in captured.out
    finally:
        temp_path.unlink()


def test_cli_test_prompts(capsys):
    code = main(["test-prompts"])
    assert code == 0
    captured = capsys.readouterr()
    assert "Counterfactual Perturbation Test" in captured.out
    assert "Resilience Score" in captured.out
