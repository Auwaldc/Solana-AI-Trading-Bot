import asyncio

from bot import bot, dp


async def main():
    print("🚀 Solana AI Trading Bot Started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
