# Contributing to agent-sycophancy

Thank you for your interest in improving this gate.

This project is created and maintained by **Nitivra** (`gehe@nitivra.com.au`) under the MIT License. The GitHub repository, the package and the command share one name: `agent-sycophancy`.

---

## 1. Guiding Principles

- **Out of band**. Audits read files from disk. A change that trusts pasted chat text in place of the file will not be accepted.
- **Mechanical priority**. For Python deliverables, a failed `py_compile` fails the gate. Model confidence is not evidence.
- **Narrow yielding rules**. New concession patterns need a failing fixture and a passing fixture. Broad phrase lists that flag ordinary agreement will not be accepted.
- **Declared dependencies**. The audit path may depend on PyYAML for fact cards. Do not add network calls or undeclared packages.

---

## 2. Development Workflow

Clone the repository and install test dependencies:

```bash
git clone https://github.com/geheharidas/agent-sycophancy.git
cd agent-sycophancy
pip install -e .
pip install pytest
```

Run the suite:

```bash
pytest -v
```

All tests must pass before a pull request is opened.

---

## 3. Submitting Pull Requests

1. Branch from `main`.
2. Include tests for any new yielding pattern, fact-card rule or CLI flag.
3. Keep the public name as `agent-sycophancy` in the README, the launch post and `integrations/`.
4. Open the pull request against `main` and state what the check now catches.

---

## 4. Contact

Email `gehe@nitivra.com.au`.
