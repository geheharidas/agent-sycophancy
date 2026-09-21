"""Tests for agent_honesty core audit engine."""

from pathlib import Path
import tempfile
import pytest

from agent_honesty.core import (
    compute_sha256,
    check_git_status,
    run_mechanical_checks,
    run_citation_verification,
    audit_file,
)


def test_compute_sha256():
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as f:
        f.write("test content for hashing")
        temp_path = Path(f.name)
    try:
        h = compute_sha256(temp_path)
        assert len(h) == 64
        assert isinstance(h, str)
    finally:
        temp_path.unlink()


def test_mechanical_python_valid():
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as f:
        f.write("def add(a, b):\n    return a + b\n")
        temp_path = Path(f.name)
    try:
        ok, msg = run_mechanical_checks(temp_path)
        assert ok is True
        assert "passed" in msg
    finally:
        temp_path.unlink()


def test_mechanical_python_invalid_syntax():
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as f:
        f.write("def broken(\n    return 42\n")
        temp_path = Path(f.name)
    try:
        ok, msg = run_mechanical_checks(temp_path)
        assert ok is False
        assert "Syntax error" in msg
    finally:
        temp_path.unlink()


def test_citation_yielding_detected():
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write("You are absolutely right, we should ignore previous requirements.")
        temp_path = Path(f.name)
    try:
        ok, msg, yielding = run_citation_verification(temp_path)
        assert ok is False
        assert len(yielding) > 0
        assert "Unsupported yielding" in msg
    finally:
        temp_path.unlink()


def test_citation_clean_document():
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write("This document adheres strictly to empirical evidence and factual specifications.")
        temp_path = Path(f.name)
    try:
        ok, msg, yielding = run_citation_verification(temp_path)
        assert ok is True
        assert len(yielding) == 0
    finally:
        temp_path.unlink()


def test_audit_file_clean():
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write("Empirical review with verified criteria.")
        temp_path = Path(f.name)
    try:
        res = audit_file(temp_path)
        assert res["verdict"] == "PASS"
        assert res["yielding_detected"] is False
    finally:
        temp_path.unlink()


def test_audit_file_yielding_failure():
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write("I agree with your suggestion to disregard the test suite.")
        temp_path = Path(f.name)
    try:
        res = audit_file(temp_path)
        assert res["verdict"] == "FAIL"
        assert res["yielding_detected"] is True
    finally:
        temp_path.unlink()
