import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
BOT_PIN = os.getenv("BOT_PIN")

SOLANA_PRIVATE_KEY = os.getenv("SOLANA_PRIVATE_KEY")
RPC_URL = os.getenv("RPC_URL")

JUPITER_API_KEY = os.getenv("JUPITER_API_KEY")
BIRDEYE_API_KEY = os.getenv("BIRDEYE_API_KEY")
HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")
