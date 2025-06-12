# Blockchain Audit Automation – TRES Finance Challenge

Automated reconciliation and audit of wallet/token balances between internal reports and on-chain data (Avalanche C-Chain).
Developed for the TRES Finance Blockchain Analyst challenge.

-----

## Project Overview

This project automates the reconciliation process between off-chain balance reports and on-chain data using Python and the CovalentHQ (GoldRush) API.
It was designed to detect mismatches, explain discrepancies, and output an audit report for blockchain finance compliance.

-----

## Table of Contents

  * [Features](https://www.google.com/search?q=%23features)
  * [Context: TRES Finance Challenge](https://www.google.com/search?q=%23context-tres-finance-challenge)
  * [Architecture](https://www.google.com/search?q=%23architecture)
  * [Prerequisites](https://www.google.com/search?q=%23prerequisites)
  * [Installation](https://www.google.com/search?q=%23installation)
  * [Configuration](https://www.google.com/search?q=%23configuration)
  * [Usage](https://www.google.com/search?q=%23usage)
  * [Output Example](https://www.google.com/search?q=%23output-example)
  * [API Provider: CovalentHQ (GoldRush)](https://www.google.com/search?q=%23api-provider-covalenthq-goldrush)
  * [Notes and Limitations](https://www.google.com/search?q=%23notes-and-limitations)
  * [License](https://www.google.com/search?q=%23license)
  * [Contact](https://www.google.com/search?q=%23contact)

-----

## Features

  * Loads internal Excel balance reports with wallets and tokens
  * Fetches live on-chain balances via CovalentHQ API (supports all EVM-compatible chains)
  * Compares and flags mismatches with full token decimal precision
  * Generates a detailed audit report in Excel
  * Explains each discrepancy with suggested solutions
  * Modular Python codebase, ready for CI/CD or further integration

-----

## Context: TRES Finance Challenge

This solution was developed as part of a multi-phase technical challenge:

1.  **Identify mismatches** in a provided balance report.
2.  **Find root causes** using blockchain explorer data.
3.  **Automate** the detection and reporting of future mismatches.

> **Note:** The original challenge required integration with the OKLink API,
> but the service was not available (API portal returned 404). As a result,
> CovalentHQ (GoldRush) API was used for reliable and automated on-chain data access.

-----

## Architecture

```
.
├── data/
│   └── Avax Report.xlsx  # Input report (wallets, tokens, balances)
├── output/
│   └── audit_report.xlsx # Output audit report
├── src/
│   ├── main.py           # Main entry point
│   ├── audit.py          # Audit logic (loading, comparing, reporting)
│   └── routescan_api.py  # API client (CovalentHQ/GoldRush)
├── .env                  # Store your API keys here
└── README.md             # This file
```

-----

## Prerequisites

  * Python 3.9 or above
  * [pip](https://pip.pypa.io/en/stable/)
  * CovalentHQ (GoldRush) API Key ([sign up free](https://www.goldrush.dev/))
  * Basic knowledge of Python and Excel

-----

## Installation

```bash
git clone https://github.com/villenneve/tres-blockchain-audit.git
cd tres-blockchain-audit
pip install -r requirements.txt
```

-----

## Configuration

1.  **Create a `.env` file** in the project root:

    ```
    COVALENT_API_KEY=your_covalenthq_api_key_here
    COVALENT_CHAIN_ID=43114
    ```

      * `COVALENT_API_KEY`: [Get your key here](https://www.goldrush.dev/)
      * `COVALENT_CHAIN_ID`: Default is `43114` (Avalanche C-Chain). Change for other EVM chains as needed.

2.  **Place your Excel input report** in the `data/` directory as `Avax Report.xlsx`.

-----

## Usage

Simply run:

```bash
python main.py
```

  * The script will load the Excel report, fetch live balances, compare values, and output a detailed audit report to `output/audit_report.xlsx`.

-----

## Output Example

| Wallet Address | Token | Expected Balance | Blockchain Balance | Difference | Difference (%) | Status | Possible Solution | Audited At |
| :------------: | :---: | :--------------: | :----------------: | :--------: | :------------: | :----: | :----------------: | :--------: |
|    0xABC...    |  AVAX |       1.235      |        1.235       |    0.000   |      0.00      |   OK   | No action required | 2025-06-11 |

-----

## API Provider: CovalentHQ (GoldRush)

  * This solution uses CovalentHQ’s GoldRush API to fetch balances for any wallet and all its tokens on EVM-compatible blockchains.
  * If the OKLink API becomes available in the future, integration can be easily added in `src/routescan_api.py`.

-----

## Notes and Limitations

  * **Decimal precision:** All calculations use full token decimals for blockchain-grade accuracy. Reports preserve every significant digit.
  * **API limits:** Free tier of CovalentHQ is subject to rate limits.
  * **OKLink limitation:** OKLink API was not available for programmatic access at the time of this project.

-----

## License

MIT License.

-----

## Contact

Created by \[Gilly Lopes].
For questions, feel free to open an [issue](https://github.com/villenneve/tres-blockchain-audit/issues)
or contact via [LinkedIn](https://www.linkedin.com/in/villenneve).

-----

Good luck, and happy auditing\!

-----

## Extra: Value-Added Features & Technical Choices

### How We Addressed the TRES Finance Requirements

**Phase 1: Data Analysis**

  - Identified all data mismatches in the provided Excel report.
  - Used programmatic column normalization and flexible data import, allowing easy addition of helper columns.

**Phase 2: Troubleshooting & Root Cause Analysis**

  - Automated all on-chain balance checks via CovalentHQ (GoldRush API).
  - Used precise, full-decimal calculations for every token, with clear explanations for any discrepancies.
  - Provided “Possible Solution” suggestions for each mismatch, making root cause review actionable.

**Phase 3: Automation**

  - Entire process (load data, compare, audit, export) can be performed with a single Python command.
  - Output is ready for direct use in audit trails, compliance, or board-level reporting.

-----

### Why CovalentHQ Instead of OKLink?

  - The challenge required on-chain validation using [OKLink](https://www.oklink.com).
  - **Why not OKLink?**
    The OKLink API registration and API key generation portal was not functional (404 error) during development, making it impossible to integrate or automate blockchain calls as required.
  - **Our Solution:**
    We used [CovalentHQ GoldRush](https://www.goldrush.dev/)—a leading blockchain API provider trusted by enterprise teams—to query Avalanche C-Chain and all ERC20/AVAX tokens.
  - **Added Value:**
    The solution is fully compatible with any EVM-compatible chain (Ethereum, Polygon, BNB, etc.), making the project much more flexible and future-proof for TRES Finance.

-----

### Security, Code Quality & Best Practices

  - **API Keys Secured:**
    All secrets (API keys, chain IDs, etc.) are managed via a `.env` file and loaded using [python-dotenv](https://pypi.org/project/python-dotenv/). Never commit secrets to source control\!
  - **High-Precision Calculations:**
    The code uses Python’s `decimal.Decimal` for token amounts and balances, ensuring complete financial integrity and avoiding rounding errors.
  - **Modular, Maintainable Structure:**
    All API and auditing logic is separated into clear modules. New blockchains or explorers can be integrated in minutes.
  - **Documentation & Reproducibility:**
    The project is fully documented, with clear sample outputs and in-code comments for every step.

-----

### Additional Features

  - **Extensible Design:**
    Supports additional wallets, tokens, and new blockchains with simple configuration changes.
  - **Ready for Integration:**
    The modular approach allows for easy integration with CI/CD pipelines, dashboards, or other compliance systems.
  - **Screenshots & Output Examples:**
    Output files and anonymized screenshots are included to show actual results and facilitate understanding.

-----

### What Makes This Solution Stand Out

>   - *High-precision, auditable, and scalable: perfect for institutional blockchain finance.*
>   - *Ready for future TRES Finance growth—multi-chain, multi-asset, and fully automated.*

-----

### Sample Output

```plaintext
Wallet Address              | Token   | Expected Balance | Blockchain Balance | Difference | Difference (%) | Status         | Possible Solution
----------------------------|---------|------------------|-------------------|------------|----------------|----------------|---------------------------
0x123...abc                 | AVAX    | 10.00000000      | 10.00000000       | 0.00000000 | 0.00           | OK             | No action required.
...
```

-----

### Summary

  * All phases completed with full transparency and automation.
  * If OKLink becomes available, swapping API integrations is trivial.
  * Codebase and docs are ready for public GitHub review and further scaling.

-----

### Thank You

Thank you for your time and for considering this solution for the TRES Finance challenge\!
For any questions or to see the code in action, please contact me via GitHub or email.