import requests
import os
from dotenv import load_dotenv
from decimal import Decimal


# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("COVALENT_API_KEY")
CHAIN_ID = os.getenv("COVALENT_CHAIN_ID", "43114")
BASE_URL = "https://api.covalenthq.com/v1"

def get_avax_balance(address):
    url = f"{BASE_URL}/{CHAIN_ID}/address/{address}/balances_v2/?key={API_KEY}"
    resp = requests.get(url)
    data = resp.json()
    for item in data.get("data", {}).get("items", []):
        if item.get("contract_ticker_symbol", "").upper() == "AVAX" or item.get("contract_address", "native") == "native":
            return {"balance": str(Decimal(item["balance"]) / Decimal(10 ** item["contract_decimals"]))}
    return {"balance": "0.00"}

def get_avax_tokens(address):
    url = f"{BASE_URL}/{CHAIN_ID}/address/{address}/balances_v2/?key={API_KEY}"
    resp = requests.get(url)
    data = resp.json()
    tokens = []
    for item in data.get("data", {}).get("items", []):
        symbol = item.get("contract_ticker_symbol")
        if (symbol or "").upper() != "AVAX":
            tokens.append({
                "name": item.get("contract_name"),
                "symbol": symbol or "",
                "balance": str(Decimal(item["balance"]) / Decimal(10 ** item["contract_decimals"])),
                "contract_address": item.get("contract_address"),
                "decimals": item.get("contract_decimals"),
            })
    return tokens


def get_avax_transactions(address, page=0, size=50):
    url = f"{BASE_URL}/{CHAIN_ID}/address/{address}/transactions_v3/?key={API_KEY}&page-number={page+1}&page-size={size}"
    resp = requests.get(url)
    data = resp.json()
    return data.get("data", {}).get("items", [])
