# Influencer RFP Helper

Internal CLI workflow to turn raw RFP text into a standardized brief for influencer campaigns. This v1 focuses on local usage from the command line and uses stubbed parsing logic that will be expanded with AI-assisted extraction later.

## Folder Structure
- `data_sources/sample_rfps/`: Place example or incoming RFP text files here for processing.
- `workflows/`: Entry-point scripts and orchestration for parsing and summarizing RFPs.
- `agents/`: Shared logic such as schema definitions or future parsing helpers.
- `outputs/rfp_summaries/`: Generated JSON and Markdown summaries from processed RFP files.

## How to Run (v1 CLI)
1. Install Python 3 if you do not already have it.
2. (Optional but recommended) Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add a test RFP text file to `data_sources/sample_rfps/` (e.g., `doom_rfp.txt`).
5. Run the parser:
   ```bash
   python workflows/rfp_parser.py data_sources/sample_rfps/doom_rfp.txt
   ```
6. Review the generated JSON and Markdown files in `outputs/rfp_summaries/`.

> Note: The current parsing logic is a stub and simply scaffolds the schema and summary. Future versions will add real extraction and AI integration.
