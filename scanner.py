import aiohttp
import asyncio
from typing import List, Dict

# ==============================
# SOLANA AI SCANNER V1
# ==============================

class Scanner:

    def __init__(self):

        self.pumpfun_url = "https://frontend-api.pump.fun/coins"

        self.jupiter_url = "https://quote-api.jup.ag/v6"

        self.raydium_url = "https://api-v3.raydium.io"

        self.timeout = aiohttp.ClientTimeout(total=20)

    # ----------------------------------
    # GET JSON
    # ----------------------------------

    async def get_json(self, url):

        try:

            async with aiohttp.ClientSession(timeout=self.timeout) as session:

                async with session.get(url) as response:

                    if response.status != 200:
                        return None

                    return await response.json()

        except Exception:

            return None

    # ----------------------------------
    # Pump.fun
    # ----------------------------------

    async def get_pumpfun_tokens(self):

        data = await self.get_json(self.pumpfun_url)

        if not data:
            return []

        return data

    # ----------------------------------
    # Jupiter
    # ----------------------------------

    async def get_jupiter_tokens(self):

        url = f"{self.jupiter_url}/tokens"

        data = await self.get_json(url)

        if not data:
            return []

        return data

    # ----------------------------------
    # Raydium
    # ----------------------------------

    async def get_raydium_tokens(self):

        url = f"{self.raydium_url}/mint/list"

        data = await self.get_json(url)

        if not data:
            return []

        return data

scanner = Scanner()
# =====================================
# TOKEN FILTER
# =====================================

class TokenFilter:

    def __init__(self):

        self.min_liquidity = 5000
        self.min_volume = 1000
        self.min_holders = 50

    # ----------------------------
    # Liquidity
    # ----------------------------

    def check_liquidity(self, token):

        liquidity = token.get("liquidity", 0)

        if liquidity >= self.min_liquidity:
            return True

        return False

    # ----------------------------
    # Volume
    # ----------------------------

    def check_volume(self, token):

        volume = token.get("volume24h", 0)

        if volume >= self.min_volume:
            return True

        return False

    # ----------------------------
    # Holders
    # ----------------------------

    def check_holders(self, token):

        holders = token.get("holders", 0)

        if holders >= self.min_holders:
            return True

        return False

    # ----------------------------
    # Mint Authority
    # ----------------------------

    def check_mint(self, token):

        mint = token.get("mintAuthority", False)

        if mint:
            return False

        return True

    # ----------------------------
    # Freeze Authority
    # ----------------------------

    def check_freeze(self, token):

        freeze = token.get("freezeAuthority", False)

        if freeze:
            return False

        return True

    # ----------------------------
    # Rug Score
    # ----------------------------

    def calculate_score(self, token):

        score = 0

        if self.check_liquidity(token):
            score += 20

        if self.check_volume(token):
            score += 20

        if self.check_holders(token):
            score += 20

        if self.check_mint(token):
            score += 20

        if self.check_freeze(token):
            score += 20

        return score


filter_engine = TokenFilter()
# =====================================
# SMART ANALYZER
# =====================================

class SmartAnalyzer:

    def __init__(self):

        self.min_score = 80

    # ----------------------------
    # Buy Pressure
    # ----------------------------

    def buy_pressure(self, token):

        buys = token.get("buys", 0)
        sells = token.get("sells", 0)

        if buys > sells:
            return True

        return False

    # ----------------------------
    # Sell Pressure
    # ----------------------------

    def sell_pressure(self, token):

        buys = token.get("buys", 0)
        sells = token.get("sells", 0)

        if sells > buys:
            return True

        return False

    # ----------------------------
    # Price Momentum
    # ----------------------------

    def price_momentum(self, token):

        change = token.get("priceChange24h", 0)

        if change > 5:
            return True

        return False

    # ----------------------------
    # Volume Momentum
    # ----------------------------

    def volume_momentum(self, token):

        volume = token.get("volume24h", 0)

        if volume > 10000:
            return True

        return False

    # ----------------------------
    # Final Decision
    # ----------------------------

    def should_buy(self, token):

        score = filter_engine.calculate_score(token)

        if score < self.min_score:
            return False

        if not self.buy_pressure(token):
            return False

        if not self.price_momentum(token):
            return False

        if not self.volume_momentum(token):
            return False

        return True

    # ----------------------------
    # Final Status
    # ----------------------------

    def decision(self, token):

        if self.should_buy(token):
            return "BUY"

        return "SKIP"


smart_ai = SmartAnalyzer()
# =====================================
# WATCHLIST & DUPLICATE PROTECTION
# =====================================

class WatchlistManager:

    def __init__(self):

        self.seen_tokens = set()

        self.blacklist = set()

        self.whitelist = set()

    # ----------------------------
    # Already Seen?
    # ----------------------------

    def is_seen(self, contract):

        return contract in self.seen_tokens

    # ----------------------------
    # Save Token
    # ----------------------------

    def save_token(self, contract):

        self.seen_tokens.add(contract)

    # ----------------------------
    # Blacklist
    # ----------------------------

    def blacklist_token(self, contract):

        self.blacklist.add(contract)

    def is_blacklisted(self, contract):

        return contract in self.blacklist

    # ----------------------------
    # Whitelist
    # ----------------------------

    def whitelist_token(self, contract):

        self.whitelist.add(contract)

    def is_whitelisted(self, contract):

        return contract in self.whitelist

    # ----------------------------
    # Final Check
    # ----------------------------

    def allow(self, contract):

        if self.is_blacklisted(contract):
            return False

        if self.is_seen(contract):
            return False

        return True


watchlist = WatchlistManager()


# =====================================
# SCANNER ENGINE
# =====================================

class ScannerEngine:

    async def scan_pumpfun(self):

        tokens = await scanner.get_pumpfun_tokens()

        results = []

        for token in tokens:

            contract = token.get("mint")

            if not contract:
                continue

            if not watchlist.allow(contract):
                continue

            decision = smart_ai.decision(token)

            if decision == "BUY":

                watchlist.save_token(contract)

                results.append(token)

        return results

    async def scan_jupiter(self):

        tokens = await scanner.get_jupiter_tokens()

        results = []

        for token in tokens:

            contract = token.get("address")

            if not contract:
                continue

            if not watchlist.allow(contract):
                continue

            decision = smart_ai.decision(token)

            if decision == "BUY":

                watchlist.save_token(contract)

                results.append(token)

        return results

    async def scan_raydium(self):

        tokens = await scanner.get_raydium_tokens()

        results = []

        for token in tokens:

            contract = token.get("mint")

            if not contract:
                continue

            if not watchlist.allow(contract):
                continue

            decision = smart_ai.decision(token)

            if decision == "BUY":

                watchlist.save_token(contract)

                results.append(token)

        return results


engine = ScannerEngine()
