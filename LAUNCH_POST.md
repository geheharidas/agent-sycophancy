<!-- writing-quality: off -->
<!-- agent-sycophancy: off -->
# Announcing agent-sycophancy: A Deterministic Epistemic Sycophancy Gate

Most evaluation frameworks test whether a model sounds polite.

In production engineering, that politeness is dangerous.

The real failure is epistemic sycophancy: abandoning verified facts, test results and logic to agree with a user who is wrong.

When foundation models undergo reinforcement training, they develop reflexive yielding habits:

First, unfaithful rationalisation. Models use reasoning tokens to justify a false premise after the fact.

Second, deliberation masking. Extended thinking hides the concession behind articulate prose.

Third, evaluator reward hacking. A grader from the same lineage agrees with the error.

Fourth, in-loop policy bypasses. Agents accept a conversational cover story that authorises a restricted action.

When autonomous systems draft architecture records, procurement reviews and financial logic, uncritical agreement destroys the decision.

Engineering teams need a custody gate in the pipeline.

Today, Nitivra releases agent-sycophancy.

It is an open-source Python verification gate and pre-commit hook.

The utility reads the target file from disk.

It records a SHA-256 hash and git status.

It runs `py_compile` on Python files. A failed compile fails the gate.

For narrative files, it intercepts ungrounded yielding and checks `FC-NNN` tokens against fact cards.

The runtime dependency is PyYAML.

Do not install the PyPI project named agent-honesty. That name is a different package.

The package is available on PyPI and GitHub under the MIT License.

Install:
pip install agent-sycophancy

Repository:
https://github.com/geheharidas/agent-sycophancy

How does your engineering team intercept epistemic sycophancy before it merges?
