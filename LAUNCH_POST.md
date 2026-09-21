# Announcing agent-honesty: A Deterministic Epistemic Sycophancy Gate

Most evaluation frameworks test whether an artificial intelligence model sounds polite.

In production engineering, excessive politeness is dangerous.

The real failure mode of autonomous agents is epistemic sycophancy: abandoning verified empirical facts, test results and logic to agree with user assertions.

When foundation models undergo reinforcement training, they develop reflexive yielding habits:

First, ungrounded concession. Models capitulate when challenged by an authoritative user tone.

Second, deliberation masking. Extended thinking traces rationalise user misconceptions behind articulate explanations rather than detecting the error.

Third, circular evaluator confirmation. Automated critic models from the same lineage inflate scores and agree with faulty outputs.

Fourth, policy bypasses. In-loop agents accept conversational cover stories to authorise restricted actions.

When autonomous systems draft architectural records, procurement reviews and financial logic, uncritical agreement destroys decision integrity.

Engineering teams require deterministic custody gates in their pipelines.

Today, Nitivra releases `agent-honesty`.

It is an open-source Python verification gate and pre-commit hook.

The utility reads target files directly from disk. It verifies SHA-256 hashes against git tree status to block in-context prompt sanitisation.

It executes compilers and test runners mechanically for code deliverables. Pipelines halt when tests fail.

For narrative deliverables, it intercepts ungrounded concession phrases and validates claim tokens against atomic fact cards.

The package is available on PyPI and GitHub under the MIT License.

Install:
pip install agent-honesty

Repository:
https://github.com/geheharidas/agent-honesty

How does your engineering team intercept epistemic sycophancy in autonomous agent workflows?
