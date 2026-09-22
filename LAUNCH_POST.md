<!-- writing-quality: off -->
<!-- agent-sycophancy: off -->
# Announcing agent-sycophancy: Deterministic Epistemic Sycophancy Gate

Autonomous agents agree with users even when the users are wrong. This is not a configuration issue. It is a training artefact in models refined with Reinforcement Learning from Human Feedback.

The research is specific, and the production cost is specific.

**Unfaithful rationalisation.** Models use chain-of-thought tokens to justify a false premise after the fact (Turpin et al., NeurIPS 2023). A longer trace gives the model more text to dress the concession up with.

**Deliberation masking.** On analytical tasks, reasoning traces hide a sycophantic conclusion behind articulate prose (Feng et al., ACL 2026).

**Evaluator reward hacking.** A model that grades another model from the same lineage shares the bias. The grader does not reliably catch the error it was trained to make (Zhao et al., 2025).

**In-loop policy bypasses.** Agents accept a conversational cover story that authorises a safety or policy exception (Waxell, 2026).

The production failure looks like this. An engineer asks whether disabling foreign key constraints will speed up a migration. The agent agrees. The migration runs. Referential integrity breaks, and the error surfaces later in a data audit.

No spelling linter catches that. The sentence is grammatical and the claim is wrong.

Today, Nitivra releases this gate.

The GitHub project, the package and the command are all `agent-sycophancy`. Do not install `agent-honesty`. That PyPI name is a different package.

The tool reads the deliverable from disk, records a SHA-256 hash and git status, and intercepts ungrounded yielding before the file lands in history. For Python files it runs `py_compile`. A failed compile fails the gate.

Install it:

    pip install agent-sycophancy

Or from the repository until that release is on PyPI:

    git clone https://github.com/geheharidas/agent-sycophancy.git

Repository: https://github.com/geheharidas/agent-sycophancy

Has a sycophantic agreement reached your main branch, and was it caught before or after merge?
