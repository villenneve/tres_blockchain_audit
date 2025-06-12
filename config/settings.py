import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OKLINK_API_KEY = os.getenv("OKLINK_API_KEY")
BASE_URL = "https://www.oklink.com/api/v5/explorer"
