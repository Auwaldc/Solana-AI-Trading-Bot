from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from config import BOT_TOKEN, OWNER_ID, BOT_PIN


bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

dp = Dispatcher()


class LoginState(StatesGroup):
    pin = State()


admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💰 Wallet"),
            KeyboardButton(text="📈 Trading"),
        ],
        [
            KeyboardButton(text="👀 Wallet Tracker"),
            KeyboardButton(text="🤖 AI Hunter"),
        ],
        [
            KeyboardButton(text="⚙️ Settings"),
            KeyboardButton(text="📊 Reports"),
        ],
        [
            KeyboardButton(text="🔔 Notifications"),
            KeyboardButton(text="🛑 Emergency Stop"),
        ],
    ],
    resize_keyboard=True,
)


@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):

    if message.from_user.id != OWNER_ID:
        await message.answer("⛔ Access Denied!")
        return

    await state.set_state(LoginState.pin)

    await message.answer(
        "🔒 <b>Admin Login</b>\n\n"
        "Please enter your 4-digit PIN."
    )


@dp.message(LoginState.pin)
async def check_pin(message: Message, state: FSMContext):

    if message.text != BOT_PIN:
        await message.answer("❌ Wrong PIN!")
        return

    await state.clear()

    await message.answer(
        "✅ <b>Login Successful!</b>\n\n"
        "🤖 <b>SOLANA AI TRADING BOT</b>\n\n"
        "Welcome, Admin.",
        reply_markup=admin_keyboard
    )
