import requests
from aiogram import Bot, Dispatcher, types
import asyncio

# 👉 Вставь сюда свои данные:
TELEGRAM_TOKEN = "8071120961:AAHaCU8rIXZ1Zueb76ica40tFfhgjj80ThY"  # ← сюда токен бота от BotFather
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1440715797096960051/z5YaeijRYSHseKgcHWlxlr9KxGFOKOBz5we0s3LRpJAzNBCx-s9d0WGeiI1QtD76vKD3"  # ← сюда URL вебхука Discord

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


def send_to_discord(text):
    """Отправка текста в Discord через webhook"""
    data = {"content": text}
    requests.post(DISCORD_WEBHOOK, json=data)


@dp.message()
async def forward_message(message: types.Message):
    username = message.from_user.full_name

    # 1️⃣ Текст
    if message.text:
        send_to_discord(f"**{username}:** {message.text}")

    # 2️⃣ Фото
    elif message.photo:
        file_id = message.photo[-1].file_id
        file = await bot.get_file(file_id)
        url = f"https://api.telegram.org/file/bot{TELEGRAM_TOKEN}/{file.file_path}"
        send_to_discord(f"📸 {username} отправил фото:\n{url}")

    # 3️⃣ Документы
    elif message.document:
        file = await bot.get_file(message.document.file_id)
        url = f"https://api.telegram.org/file/bot{TELEGRAM_TOKEN}/{file.file_path}"
        send_to_discord(f"📎 {username} отправил файл:\n{url}")

    # 4️⃣ Видео
    elif message.video:
        file = await bot.get_file(message.video.file_id)
        url = f"https://api.telegram.org/file/bot{TELEGRAM_TOKEN}/{file.file_path}"
        send_to_discord(f"🎥 {username} отправил видео:\n{url}")


async def main():
    print("Бот запущен. Слушаю сообщения...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
