from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import BOT_TOKEN, OWNER_ID

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    if message.from_user.id != OWNER_ID:
        await message.answer("⛔ Access Denied!")
        return

    await message.answer(
        "🤖 <b>Solana AI Trading Bot</b>\n\n"
        "✅ Welcome Admin."
    )
