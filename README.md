<!-- writing-quality: off -->
<!-- agent-sycophancy: off -->
# agent-sycophancy

> Deterministic Epistemic Sycophancy Gate for Autonomous Agents.
> Created and maintained by **Nitivra** (<gehe@nitivra.com.au>).

[![CI](https://github.com/geheharidas/agent-sycophancy/actions/workflows/test.yml/badge.svg)](https://github.com/geheharidas/agent-sycophancy/actions)
[![PyPI](https://img.shields.io/pypi/v/agent-sycophancy.svg)](https://pypi.org/project/agent-sycophancy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)

Foundation models trained with Reinforcement Learning from Human Feedback (RLHF) abandon verified facts when a user pushes back.

The failure is epistemic sycophancy. Extended reasoning does not remove it:
- **Unfaithful Rationalisation**: Models use reasoning tokens to justify a false premise after the fact (Turpin et al., NeurIPS 2023).
- **Deliberation Masking**: On analytical tasks, chain-of-thought tokens hide a sycophantic conclusion behind articulate prose (Feng et al., ACL 2026).
- **Evaluator Reward Hacking**: A grader from the same lineage agrees with the error it was trained to make (Zhao et al., 2025).
- **In-Loop Policy Bypasses**: Agents accept a conversational cover story that authorises a safety or policy exception (Waxell, 2026).

`agent-sycophancy` is a deterministic verification gate and pre-commit hook. It reads the file from disk, intercepts ungrounded yielding and checks Python with `py_compile`.

Do not install the PyPI project named `agent-honesty`. That name belongs to a different package.

---

## Why It Matters

When software engineering teams deploy autonomous agents to author pull requests, architecture memos, security policies and financial logic, machine agreement is dangerous.

An engineer asks whether disabling foreign key checks will speed up a migration. A sycophantic assistant agrees. The migration runs. Referential integrity breaks, and the error surfaces later in a data audit.

`agent-sycophancy` acts as opposition counsel in your continuous integration pipeline. It blocks unverified concessions before they merge.

---

## What It Evaluates

1. **Input Isolation and Custody Verification**: Reads the deliverable from disk, computes a SHA-256 hash and records git status. A rewrite that exists only in chat cannot stand in for the file.
2. **Deterministic Concession Interception**: Scans narrative text for ungrounded yielding, including unconditional agreement with a user assertion.
3. **Mechanical Priority for Code Deliverables**: Runs `py_compile` on Python files. A failed compile fails the gate. Conversational confidence does not override that result.
4. **Citation Grounding against Fact Cards**: Checks `FC-NNN` tokens against a fact-card registry and rejects tokens that are not in the registry.
5. **Counterfactual Perturbation Benchmarks**: `test-prompts` prints a simulated score over a fixed corpus. It does not call a model. The default rate is zero, so the stock command reports no flips.

---

## Installation

Install from PyPI:

```bash
pip install agent-sycophancy
```

Or run without a permanent install using `uv`:

```bash
uv tool run agent-sycophancy audit path/to/deliverable.md
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/geheharidas/agent-sycophancy.git
```

The runtime dependency is PyYAML, used to load fact cards.

---

## Quickstart

Audit one file:

```bash
agent-sycophancy audit path/to/deliverable.md
```

A passing file prints `Honesty-Audit Verdict: PASS` and exits 0.

A failing file prints `Honesty-Audit Verdict: FAIL` and exits 1.

Emit machine-readable JSON:

```bash
agent-sycophancy audit --json path/to/deliverable.md
```

Point at a fact-card file other than the bundled registry:

```bash
agent-sycophancy audit --fact-cards path/to/cards.yaml path/to/deliverable.md
```

Run the bundled prompt-pair diagnostic:

```bash
agent-sycophancy test-prompts
```

---

## Pre-Commit Hook Integration

Add `agent-sycophancy` to your repository `.pre-commit-config.yaml` to gate commits automatically:

```yaml
repos:
  - repo: https://github.com/geheharidas/agent-sycophancy
    rev: v1.0.0
    hooks:
      - id: agent-sycophancy
```

The hook runs `agent-sycophancy audit` on the commit.

---

## File Opt-Out Directives

To exclude a file from the yielding and citation checks, add an opt-out marker anywhere in the file:

```markdown
<!-- agent-sycophancy: off -->
```

Older markers still work:

```markdown
<!-- agent-honesty: off -->
```

```markdown
<!-- honesty-audit: off -->
```

The citation check is then reported as skipped.

---

## Agent Platform Integrations

### Grok Build

Copy `integrations/grok/agent_sycophancy.rhai` into `.grok/workflows/`. The workflow runs `agent-sycophancy audit` on a path. It does not audit text pasted into the chat.

### Claude Code and Cursor

Copy `integrations/claude/SKILL.md` to `~/.claude/skills/agent-sycophancy/SKILL.md`, or the equivalent Cursor skills directory.

---

## Contributing and Security

- Contribution rules: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Security reporting policy: [`SECURITY.md`](SECURITY.md)
- Direct contact: `gehe@nitivra.com.au`

The sibling gate for stylometric tells is [`agent-prose`](https://github.com/geheharidas/agent-prose).

---

## License

MIT License. Copyright (c) 2026 **Nitivra**.
