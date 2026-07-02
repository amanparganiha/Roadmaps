# Tools

Python scripts for deterministic execution — API calls, data transformations, file operations, database queries.

Conventions:

- One script per task, named after what it does, e.g. `scrape_single_site.py`
- Read credentials and API keys from `.env` (use `python-dotenv`), never hardcode them
- Write intermediate files to `.tmp/`
- Accept inputs via command-line arguments so scripts are reusable and testable
- Print clear errors so failures are diagnosable
