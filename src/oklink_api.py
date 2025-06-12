import requests
from config.settings import OKLINK_API_KEY, BASE_URL

def get_wallet_transactions(address, chain="avalanche", page=1):
    """
    Fetches the list of transactions for a given wallet address using Oklink API.
    Returns the API response as a JSON object.
    """
    url = f"{BASE_URL}/transaction-list"
    headers = {"Ok-Access-Key": OKLINK_API_KEY}
    params = {
        "address": address,
        "chainShortName": chain,
        "page": page,
        "limit": 20
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()
