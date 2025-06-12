from src.audit import audit_wallets_and_generate_report

INPUT_FILE = "data/Avax Report.xlsx"
OUTPUT_FILE = "output/audit_report.xlsx"

if __name__ == "__main__":
    audit_wallets_and_generate_report(INPUT_FILE, OUTPUT_FILE)
