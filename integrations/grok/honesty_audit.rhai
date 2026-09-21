let meta = #{
    name: "honesty-audit",
    description: "Deterministic epistemic sycophancy gate for autonomous agent deliverables"
};

let target = if args == () || args.target == () {
    "deliverable.md"
} else {
    args.target
};

// Execute agent-honesty out-of-band to prevent in-context sycophantic overrides
let output = sh(`agent-honesty audit ${target}`);

complete(output);
