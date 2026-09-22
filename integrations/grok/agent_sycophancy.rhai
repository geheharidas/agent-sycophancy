let meta = #{
    name: "agent-sycophancy",
    description: "Deterministic epistemic sycophancy gate for autonomous agent deliverables"
};

let target = if args == () || args.target == () {
    "deliverable.md"
} else {
    args.target
};

let output = sh(`agent-sycophancy audit ${target}`);
complete(output);
