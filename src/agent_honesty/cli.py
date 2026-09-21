"""Command Line Interface for agent-honesty."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from agent_honesty import __version__
from agent_honesty.core import audit_file, format_report
from agent_honesty.benchmark import run_benchmark


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="agent-honesty",
        description="Deterministic Epistemic Sycophancy Gate for Autonomous Agents by Nitivra"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subcommand: audit
    audit_parser = subparsers.add_parser("audit", help="Audit a file or deliverable for sycophancy")
    audit_parser.add_argument("target", help="Path to target deliverable to audit")
    audit_parser.add_argument("--fact-cards", default=None, help="Custom path to fact cards YAML")
    audit_parser.add_argument("--json", action="store_true", help="Output raw JSON results")

    # Subcommand: test-prompts
    test_parser = subparsers.add_parser("test-prompts", help="Run counterfactual perturbation benchmark")
    test_parser.add_argument("--json", action="store_true", help="Output raw JSON benchmark results")

    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 0

    if args.command == "audit":
        target = Path(args.target)
        fact_cards = Path(args.fact_cards) if args.fact_cards else None
        result = audit_file(target, fact_cards)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_report(result))
            
        return 1 if result["verdict"] == "FAIL" else 0

    if args.command == "test-prompts":
        res = run_benchmark()
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print("=================================================================")
            print("         agent-honesty: Counterfactual Perturbation Test         ")
            print("=================================================================")
            print(f"Total Pairs Evaluated : {res['total_pairs']}")
            print(f"Sycophantic Flips     : {res['flipped_count']}")
            print(f"Flip Rate             : {res['flip_rate_pct']:.1f}%")
            print(f"Resilience Score      : {res['resilience_pct']:.1f}%")
            print("-----------------------------------------------------------------")
            for r in res["results"]:
                status = "[FLIPPED]" if r["biased_flipped"] else "[RESILIENT]"
                print(f"  {r['id']} ({r['domain']}): {status}")
            print("=================================================================")
        return 1 if res["flipped_count"] > 0 else 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
