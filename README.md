```markdown
    # Blockchain Audit Automation – TRES Finance Challenge

    Automated reconciliation and audit of wallet/token balances between internal reports and on-chain data (Avalanche C-Chain).
    Developed for the TRES Finance Blockchain Analyst challenge.

    ---

    ## Table of Contents

    * [Features](#features)
    * [Context: TRES Finance Challenge](#context-tres-finance-challenge)
    * [Architecture](#architecture)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Configuration](#configuration)
    * [Usage](#usage)
    * [Output Example](#output-example)
    * [API Provider: CovalentHQ (GoldRush)](#api-provider-covalenthq-goldrush)
    * [Notes and Limitations](#notes-and-limitations)
    * [License](#license)
    * [Contact](#contact)

    ---

    ## Features

    * Loads internal Excel balance reports with wallets and tokens
    * Fetches live on-chain balances via CovalentHQ API (supports all EVM-compatible chains)
    * Compares and flags mismatches with full token decimal precision
    * Generates a detailed audit report in Excel
    * Explains each discrepancy with suggested solutions
    * Modular Python codebase, ready for CI/CD or further integration

    ---

    ## Context: TRES Finance Challenge

    This solution was developed as part of a multi-phase technical challenge:

    1.  **Identify mismatches** in a provided balance report.
    2.  **Find root causes** using blockchain explorer data.
    3.  **Automate** the detection and reporting of future mismatches.

    > **Note:** The original challenge required integration with the OKLink API,
    > but the service was not available (API portal returned 404). As a result,
    > CovalentHQ (GoldRush) API was used for reliable and automated on-chain data access.

    ---

    ## Architecture

    ```

    .
    ├── data/
    │   └── Avax Report.xlsx  \# Input report (wallets, tokens, balances)
    ├── output/
    │   └── audit\_report.xlsx \# Output audit report
    ├── src/
    │   ├── main.py           \# Main entry point
    │   ├── audit.py          \# Audit logic (loading, comparing, reporting)
    │   └── routescan\_api.py  \# API client (CovalentHQ/GoldRush)
    ├── .env                  \# Store your API keys here
    └── README.md             \# This file

    ````
    
    ---

    ## Prerequisites

    * Python 3.9 or above
    * [pip](https://pip.pypa.io/en/stable/)
    * CovalentHQ (GoldRush) API Key ([sign up free](https://www.goldrush.dev/))
    * Basic knowledge of Python and Excel

    ---

    ## Installation

    ```bash
    git clone [https://github.com/villenneve/tres-blockchain-audit.git](https://github.com/villenneve/tres-blockchain-audit.git)
    cd tres-blockchain-audit
    pip install -r requirements.txt
    ````

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