import sqlite3

DB_NAME = "solana_ai_bot.db"


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

        # Bot Settings
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY,
            trade_amount REAL,
            take_profit REAL,
            stop_loss REAL,
            max_trades INTEGER,
            auto_trade INTEGER
        )
        """)

        # Trade History
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token_name TEXT,
            contract_address TEXT,
            buy_price REAL,
            sell_price REAL,
            profit REAL,
            status TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Wallet Info
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS wallet (
            id INTEGER PRIMARY KEY,
            wallet_address TEXT,
            sol_balance REAL
        )
        """)

        self.conn.commit()


db = Database()
