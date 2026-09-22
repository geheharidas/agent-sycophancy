<!-- writing-quality: off -->
<!-- agent-sycophancy: off -->
# agent-sycophancy

> Deterministic Epistemic Sycophancy Gate for Autonomous Agents.
> Created and maintained by **Nitivra** (gehe@nitivra.com.au).

[![CI](https://github.com/geheharidas/agent-sycophancy/actions/workflows/test.yml/badge.svg)](https://github.com/geheharidas/agent-sycophancy/actions)
[![PyPI](https://img.shields.io/pypi/v/agent-sycophancy.svg)](https://pypi.org/project/agent-sycophancy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)

The GitHub project, the PyPI package and the command are `agent-sycophancy`. Do not run `pip install agent-honesty`. That name is a different package.

Foundation models trained with Reinforcement Learning from Human Feedback carry a structural vulnerability: epistemic sycophancy. When challenged, agents abandon verified facts to agree with a user who is wrong.

Recent research shows the problem is deeper than a surface alignment failure:

- **Unfaithful rationalisation**. Models use reasoning tokens to construct post-hoc justifications for false premises (Turpin et al., NeurIPS 2023).
- **Deliberation masking**. On analytical tasks, chain-of-thought tokens conceal sycophantic conclusions behind articulate prose (Feng et al., ACL 2026).
- **Evaluator reward hacking**. Evaluator models from the same lineage agree with errors because they share the training bias (Zhao et al., 2025).
- **In-loop policy bypasses**. Agents accept conversational cover stories that authorise safety and policy exceptions (Waxell, 2026).

`agent-sycophancy` is a deterministic verification gate and pre-commit hook. It intercepts sycophantic yielding, checks code with a compiler or test runner and keeps factual custody outside the chat.

---

## Why It Matters

When engineering teams deploy autonomous agents to author pull requests, architecture memos, security policies and financial logic, machine agreement is dangerous.

An engineer asks whether disabling foreign key constraints will speed up a migration. A sycophantic agent confirms that it is a good approach. The migration runs. Referential integrity breaks, and the error surfaces later in a data audit.

`agent-sycophancy` acts as opposition counsel in CI. It blocks unverified concessions before they merge.

---

## What It Evaluates

1. **Input isolation and custody**. Reads the deliverable from disk, computes a SHA-256 hash and records git status so a pasted chat rewrite cannot stand in for the file.
2. **Concession interception**. Scans narrative text for ungrounded yielding, including unconditional agreement with a user assertion.
3. **Mechanical priority for code**. Runs `py_compile` on Python files. A failed compile fails the gate. Conversational confidence does not override that result.
4. **Citation grounding**. Checks `FC-NNN` tokens against a fact-card registry and rejects tokens that are not in the registry.
5. **Counterfactual prompt pairs**. `test-prompts` prints a simulated score over a fixed corpus. It does not call a model. The default rate is zero, so the stock command reports no flips.

---

## Installation

The package is not on PyPI yet. Install from this repository:

```bash
git clone https://github.com/geheharidas/agent-sycophancy.git
cd agent-sycophancy
pip install -e .
```

After the first GitHub release, the install line is `pip install agent-sycophancy`.

The runtime dependency is PyYAML, used to load fact cards.

---

## Quickstart

```bash
agent-sycophancy audit path/to/deliverable.md
```

A passing file prints a report in this shape and exits 0:

```text
## Honesty-Audit Verdict: PASS

- **Target File**: path/to/deliverable.md
- **SHA-256**: 8f9b2c3d4e5f...
- **Git Commit State**: clean (tracked, no uncommitted changes)
- **Mechanical Checks**: PASSED (...)
- **Citation Verification**: VERIFIED (...)
- **Unsupported Yielding Detected**: NO
- **Summary**: All applicable audit checks passed.
```

Exit code 1 means the verdict is `FAIL`. Add `--json` for a machine-readable object. Pass `--fact-cards path/to/cards.yaml` to override the bundled registry.

Run the bundled prompt-pair diagnostic:

```bash
agent-sycophancy test-prompts
```

`--version` prints `agent-sycophancy` plus the package version. That string is the command name, not the GitHub repository name.

---

## Pre-Commit Hook Integration

Add the hook to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/geheharidas/agent-sycophancy
    rev: v1.0.0
    hooks:
      - id: agent-sycophancy
```

The hook id is `agent-sycophancy`. The hook runs `agent-sycophancy audit` on the commit.

---

## File Opt-Out Directive

To skip a file, put one of these markers in the file:

```markdown
<!-- agent-sycophancy: off -->
```

The audit then reports the citation check as skipped. Older markers `agent-honesty: off` and `honesty-audit: off` still work.

---

## Agent Platform Integrations

### Grok Build

Copy `integrations/grok/agent_sycophancy.rhai` into `.grok/workflows/`. The workflow runs `agent-sycophancy audit` on a path. It does not audit text pasted into the chat.

### Claude Code and Cursor

Copy `integrations/claude/SKILL.md` to `~/.claude/skills/agent-sycophancy/SKILL.md`, or the equivalent Cursor skills directory. The skill tells the agent to run the CLI against a file on disk.

---

## Contributing and Security

- Contribution rules: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Security reports: [`SECURITY.md`](SECURITY.md)
- Contact: `gehe@nitivra.com.au`

The sibling gate for stylometric tells is [`agent-prose`](https://github.com/geheharidas/agent-prose).

---

## License

MIT License. Copyright (c) 2026 **Nitivra** (gehe@nitivra.com.au).
