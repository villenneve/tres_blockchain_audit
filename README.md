# TRES Blockchain Audit Tool

Automated validator to detect mismatches between internal balance reports and actual blockchain data on Avalanche.

## Features
- Parses Excel reports with wallet balances and transaction logs.
- Verifies calculation of ending balances.
- Optionally fetches real blockchain data from Oklink API.
- Exports discrepancies to a structured Excel file.

## How to Run

```bash
pip install -r requirements.txt
python main.py
