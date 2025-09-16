from telethon import TelegramClient
from dotenv import load_dotenv
import os
from pathlib import Path

# Load credentials from .env
load_dotenv(dotenv_path=Path('./.env'))

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")
bot_name = os.getenv("BOT_USERNAME")

# Initialize the bot client
bot = TelegramClient(bot_name, api_id, api_hash)
print("Bot Session Started !!")
