# Influencer RFP Helper

Internal CLI tool for turning raw influencer marketing RFP text into a standardized, structured brief.

This project is an early-stage prototype focused on:
- Reducing manual RFP review time
- Standardizing how key information is extracted
- Laying the groundwork for AI-assisted parsing, reporting, and automation

Version 1 (current) runs locally from the command line and uses stubbed parsing logic. Future versions will integrate AI-powered extraction and validation.

---

## What This Tool Does (v1)

Given an RFP as a plain text file, the tool:

1. Reads the raw RFP text
2. Seeds a predefined JSON schema used for influencer campaign planning
3. Generates:
   - A structured JSON output (machine-readable)
   - A Markdown summary (human-readable)
4. Flags missing or incomplete information placeholders for follow-up

Outputs are written to the `outputs/rfp_summaries/` directory.

---

## Folder Structure

.
├── agents/
│ ├── init.py
│ └── schema.py
│ # Shared logic and schema definitions for parsing RFPs
│
├── workflows/
│ ├── init.py
│ └── rfp_parser.py
│ # CLI entrypoint and orchestration logic
│
├── data_sources/
│ └── sample_rfps/
│ # Place incoming or test RFP .txt files here
│
├── outputs/
│ └── rfp_summaries/
│ # Generated JSON and Markdown summaries
│
├── requirements.txt
└── README.md

## How to Run (v1 – CLI)

### Prerequisites
- Python 3.10+
- pip

(Optional but recommended)
- A virtual environment

---

### Setup

```bash
pip install -r requirements.txt
Add an RFP file
Create or place a .txt file inside:

data_sources/sample_rfps/
Example:

data_sources/sample_rfps/doom_rfp.txt
Run the parser
From the project root:

python -m workflows.rfp_parser data_sources/sample_rfps/doom_rfp.txt
Output
After running, you should see:

outputs/rfp_summaries/
├── doom_rfp.json
└── doom_rfp.md
.json → structured data aligned to the internal campaign schema

.md → lightweight brief suitable for review, planning, or pitch prep

The terminal will also print confirmation messages when files are saved.

Current Limitations (Intentional)
Parsing logic is stubbed (placeholders only)

No AI extraction yet

No validation against real campaign requirements

Local-only execution

This is by design — v1 is about structure, workflow, and correctness before adding intelligence.

Planned Next Steps
Integrate AI-assisted parsing to populate schema fields

Automatically detect missing or ambiguous RFP information

Generate follow-up questions for clients

Expand schema to support budgeting, platform splits, and talent logic

Enable batch processing of multiple RFPs

Why This Exists
Influencer RFPs are inconsistent, vague, and time-consuming to process.
This tool turns that chaos into a repeatable, auditable workflow that can scale across teams and campaigns.

The long-term goal is not just faster RFP review — it’s building internal tooling that captures institutional knowledge and compounds over time.
