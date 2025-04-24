from .. import bot
from telethon import events
import asyncio


@bot.on(events.NewMessage(incoming = True, pattern ="/start"))
async def start(event):
  await event.reply("👋 Hello! I'm your assistant bot.\n\n"
        "Use /help to see what I can do.")

@bot.on(events.NewMessage(incoming = True, pattern ="/help"))
async def start(event):
  await event.reply("**🛠 Bot Commands Help**\n\n"
        "/start - Welcome message\n"
        "/help - Show this help menu\n"
        "/ask <your question> - Get a response from ChatGPT\n"
        "/download a <YouTube URL> - Download audio from YouTube\n"
        "/download v <YouTube URL> - Download video from YouTube\n"
        "/wiki <yuor topic> - Get information on the topic from Wikipedia\n"
        "\n✨ More features coming soon!")
