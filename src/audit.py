import pandas as pd
from datetime import datetime
from decimal import Decimal, getcontext
from src.routescan_api import get_avax_balance, get_avax_tokens

# Define máxima precisão para cálculos decimais
getcontext().prec = 50

def load_balance_sheet(file_path):
    df = pd.read_excel(file_path)
    # Remove whitespace e aspas dos nomes das colunas
    df.columns = [str(c).strip().replace("'", "").replace('"', '') for c in df.columns]
    print("COLUMNS:", [repr(c) for c in df.columns])
    return df

def get_token_onchain_balance(wallet, token_symbol):
    if token_symbol.upper() == 'AVAX':
        balance = get_avax_balance(wallet).get('balance', 0)
        return Decimal(str(balance))
    else:
        tokens_data = get_avax_tokens(wallet)
        for t in tokens_data:
            if t.get('symbol', '').upper() == token_symbol.upper():
                return Decimal(str(t.get('balance', 0)))
        return Decimal('0')

def suggest_solution(diff, pct_diff, token_symbol):
    # Ajuste para precisão de tokens (até 18 casas)
    if abs(diff) < Decimal("1e-12"):
        return "No action required."
    elif abs(pct_diff) < Decimal("0.1"):
        return "Check for rounding/formatting errors in reporting."
    elif abs(diff) < Decimal("1"):
        return "Verify minor transaction fees, possible small missing transaction."
    else:
        return f"Audit all transactions for {token_symbol}, check for missing or duplicate transactions on-chain and in internal records."

def audit_wallets_and_generate_report(balance_sheet_path, output_path):
    df = load_balance_sheet(balance_sheet_path)
    df.columns = [c.strip().lower() for c in df.columns]
    print("COLUMNS AT AUDIT:", [repr(c) for c in df.columns])

    WALLET_COL = "wallet address"
    TOKEN_COL = "asset symbol"
    EXPECTED_COL = "close historical balance (t)"

    audit_rows = []
    for idx, row in df.iterrows():
        wallet = row[WALLET_COL]
        token = row[TOKEN_COL]
        expected = Decimal(str(row[EXPECTED_COL]))
        actual = Decimal(str(get_token_onchain_balance(wallet, token)))
        diff = actual - expected
        pct_diff = (diff / expected * 100) if expected != 0 else Decimal("0")

        if abs(diff) < Decimal("1e-12"):
            status = "OK"
        elif abs(diff) < Decimal("0.01"):
            status = "Minor difference"
        else:
            status = "Discrepancy"

        solution = suggest_solution(diff, pct_diff, token)

        audit_rows.append({
            "Wallet Address": wallet,
            "Token": token,
            "Expected Balance": str(expected),         # Full decimal!
            "Blockchain Balance": str(actual),         # Full decimal!
            "Difference": str(diff),                   # Full decimal!
            "Difference (%)": str(pct_diff),           # Full decimal!
            "Status": status,
            "Possible Solution": solution,
            "Audited At": datetime.now().strftime("%Y-%m-%d %H:%M"),
        })

    audit_df = pd.DataFrame(audit_rows)
    audit_df.to_excel(output_path, index=False)
    print(f"✅ Audit report saved to: {output_path}")

