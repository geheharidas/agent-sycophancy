"""agent-honesty: Deterministic Epistemic Sycophancy Gate for Autonomous Agents.

Created and maintained by Nitivra.
"""
from __future__ import annotations

__version__ = "1.0.0"
__author__ = "Nitivra"

from agent_honesty.core import (
    audit_file,
    compute_sha256,
    check_git_status,
    format_report,
)
from agent_honesty.benchmark import run_benchmark

__all__ = [
    "audit_file",
    "compute_sha256",
    "check_git_status",
    "format_report",
    "run_benchmark",
    "__version__",
    "__author__",
]
