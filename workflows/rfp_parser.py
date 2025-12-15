"""CLI workflow to stub parse RFP text into JSON schema and Markdown summary."""

from __future__ import annotations

import argparse
import copy
import json
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from agents.schema import SCHEMA_TEMPLATE

console = Console()


def load_rfp_text(rfp_path: Path) -> str:
    """Read the raw RFP text from a file."""
    return rfp_path.read_text(encoding="utf-8")


def build_stubbed_payload(rfp_path: Path, rfp_text: str) -> dict:
    """
    Create a starter payload based on the schema template.

    This implementation is intentionally minimal for v1 and should be replaced by
    real parsing logic and AI-assisted extraction later.
    """

    payload = copy.deepcopy(SCHEMA_TEMPLATE)
    payload["meta"].update(
        {
            "rfp_title": rfp_path.stem,
            "rfp_source": str(rfp_path),
            "date_received": datetime.today().strftime("%Y-%m-%d"),
        }
    )

    payload["missing_or_unclear"]["fields_missing"].append(
        "Automated parsing not yet implemented; please fill fields manually for now."
    )
    payload["missing_or_unclear"]["fields_partial"].append(
        "Raw RFP text captured for reference, but structured extraction is pending."
    )
    payload["campaign_overview"]["campaign_name"] = rfp_path.stem

    # Store the raw RFP content for reference in the payload under an auxiliary key.
    payload["raw_rfp_text"] = rfp_text
    return payload


def build_markdown_summary(payload: dict) -> str:
    """Generate a lightweight Markdown summary based on the stubbed payload."""
    lines = [
        f"# RFP Summary: {payload['meta']['rfp_title']}",
        "",
        "> Parsing logic is a stub for v1. Update fields manually or connect AI parsing in a future iteration.",
        "",
        "## Campaign Overview",
        f"- Campaign Name: {payload['campaign_overview']['campaign_name']}",
        f"- Primary Objective: {payload['campaign_overview']['primary_objective'] or 'TBD'}",
        "",
        "## Missing or Unclear",
        *[f"- {item}" for item in payload["missing_or_unclear"]["fields_missing"]],
        *[f"- {item}" for item in payload["missing_or_unclear"]["fields_partial"]],
    ]
    return "\n".join(lines)


def write_outputs(base_name: str, payload: dict, markdown: str) -> None:
    """Write JSON and Markdown outputs to the outputs/rfp_summaries directory."""
    output_dir = Path("outputs/rfp_summaries")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / f"{base_name}.json"
    md_path = output_dir / f"{base_name}.md"

    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    md_path.write_text(markdown, encoding="utf-8")

    console.print(Panel.fit(f"Saved JSON to [bold]{json_path}[/]"))
    console.print(Panel.fit(f"Saved Markdown to [bold]{md_path}[/]"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Stub parser for Influencer RFPs. Reads a text file and generates "
            "starter JSON + Markdown files in outputs/rfp_summaries."
        )
    )
    parser.add_argument("rfp_path", type=Path, help="Path to the RFP .txt file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.rfp_path.exists():
        console.print(Panel.fit(f"RFP file not found: {args.rfp_path}", style="red"))
        return

    console.print(Panel.fit(f"Loading RFP from {args.rfp_path}", style="cyan"))
    rfp_text = load_rfp_text(args.rfp_path)

    payload = build_stubbed_payload(args.rfp_path, rfp_text)
    markdown = build_markdown_summary(payload)

    write_outputs(args.rfp_path.stem, payload, markdown)
    console.print(Panel.fit("Done. Review and update the outputs manually as needed.", style="green"))


if __name__ == "__main__":
    main()
