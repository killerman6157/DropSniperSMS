from aiogram import Bot, Dispatcher, types, executor
from db import assign_number_to_user, get_user_status, receive_otp
from rest_api import fetch_number
import json

API_TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    user_id = str(message.from_user.id)
    country_code = "NG"  # default
    number = fetch_number(country_code)
    if number:
        assign_number_to_user(user_id, number)
        await message.reply(f"✅ An baka wannan number: `{number}`\nYi amfani da ita don karɓar OTP.", parse_mode='Markdown')
    else:
        await message.reply("❌ An kasa samo number daga REST API.")

@dp.message_handler(commands=['status'])
async def status_cmd(message: types.Message):
    user_id = str(message.from_user.id)
    number, otps = get_user_status(user_id)
    if number:
        otp_text = "\n".join(otps) if otps else "🕓 Babu OTP tukuna."
        await message.reply(f"📱 Number: `{number}`\n📨 OTPs:\n{otp_text}", parse_mode='Markdown')
    else:
        await message.reply("❗ Ba ka da number tukuna. Yi amfani da /start")

@dp.message_handler(commands=['send_otp'])
async def mock_otp_cmd(message: types.Message):
    args = message.text.split()
    if len(args) != 3:
        return await message.reply("⚠️ Format: /send_otp <number> <otp>")

    number = args[1]
    otp = args[2]
    user_id = receive_otp(number, otp)
    if user_id:
        await bot.send_message(user_id, f"🔐 Sabon OTP da aka karɓa: `{otp}`", parse_mode='Markdown')
        await message.reply("✅ OTP an aika wa user.")
    else:
        await message.reply("❌ Ba a sami mai wannan number ba.")

if __name__ == '__main__':
    executor.start_polling(dp)