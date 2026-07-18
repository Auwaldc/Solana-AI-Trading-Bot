import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# =========================
# Telegram
# =========================
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
BOT_PIN = os.getenv("BOT_PIN")

# =========================
# Wallet
# =========================
SOLANA_PRIVATE_KEY = os.getenv("SOLANA_PRIVATE_KEY")

# =========================
# Solana RPC
# =========================
RPC_URL = os.getenv("RPC_URL")

# =========================
# APIs
# =========================
JUPITER_API_KEY = os.getenv("JUPITER_API_KEY")
BIRDEYE_API_KEY = os.getenv("BIRDEYE_API_KEY")
HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")

# =========================
# Bot Settings
# =========================
BOT_NAME = "Solana AI Trading Bot"
VERSION = "1.0.0"

DEFAULT_TRADE_AMOUNT = 1.0
MAX_OPEN_TRADES = 3

DEFAULT_TAKE_PROFIT = 25
DEFAULT_STOP_LOSS = 8

ENABLE_AUTO_HUNTER = False
ENABLE_WATCHLIST = False
ENABLE_WALLET_TRACKER = False

LOG_LEVEL = "INFO"
