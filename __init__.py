from telethon import TelegramClient
from dotenv import load_dotenv
import os
from pathlib import Path

# Load credentials from .env
load_dotenv(dotenv_path=Path('/home/jangi/projects/tel_bot/amit_bot/amit/.env'))

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")

# Initialize the bot client
bot = TelegramClient("MDL_YT_Bot", api_id, api_hash)
print("Bot Session Started !!")
