import asyncio
from loguru import logger

from config import (
    BOT_NAME,
    VERSION,
)

async def startup():
    logger.info("=" * 50)
    logger.info(f"Starting {BOT_NAME}")
    logger.info(f"Version: {VERSION}")
    logger.info("=" * 50)

    # Future Modules
    logger.info("✓ Settings Loaded")
    logger.info("✓ Security Module")
    logger.info("✓ Database Module")
    logger.info("✓ Telegram Module")
    logger.info("✓ Trading Engine")
    logger.info("✓ Wallet Tracker")
    logger.info("✓ AI Scanner")

    logger.success("Bot Started Successfully!")

async def shutdown():
    logger.warning("Stopping Bot...")
    logger.success("Bot Stopped.")

async def main():
    try:
        await startup()

        # Main Loop
        while True:
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        await shutdown()

if __name__ == "__main__":
    asyncio.run(main())
