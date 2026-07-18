import asyncio

from telegram import bot, dp
from telegram import start


async def main():
    print("🚀 Solana AI Trading Bot Started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
