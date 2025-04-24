import glob
import logging
import asyncio
from pathlib import Path
from telethon import TelegramClient
import os, sys
from amit.utils import load_plug
from amit import bot, bot_token


# Set up logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# Load all plugins
plugin_path = "amit/plugins/*.py"
files = glob.glob(plugin_path)
for name in files:
    with open(name) as f:
        pxt = Path(f.name)
        plug = pxt.stem
        load_plug(plug.replace(".py", ""))

print("ALL PLUGINS Loaded !!")

# Start the bot 
async def main():

    await bot.start(bot_token=bot_token)
    print("Bot started successfully!")

    from sys import argv
    if len(argv) not in (1, 3, 4):
        await bot.disconnect()
    else:
        await bot.run_until_disconnected()

if __name__ == "__main__":
    try:
        asyncio.run(main())

    except Exception as e:
        print(f" Error: {e}")

    finally:
        print("Bot shutting down cleanly.")












































"""import glob
from pathlib import Path
from amit.utils import load_plug
from amit import bot, bot_token
import logging
from sys import argv
import asyncio


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
path = "amit/plugins/*.py"
files = glob.glob(path)
for name in files:
  with open(name) as a:
    pxt = Path(a.name)
    plugs = pxt.stem
    load_plug(plugs.replace(".py", ""))

print ("AMIT BOT HAS STARTED & LOADED ALL PLUGINS ")

async def main():
    # Close the session and reopen it
    bot.session.close()
    bot.session = None  # Set session to None so it will reopen a new one
    # Start the bot asynchronously
    await bot.start(bot_token=bot_token)

    # This will now print after the bot has started
    print("Bot started successfully!")

    if len(argv) not in (1, 3, 4):
      bot.disconnect()
    else:
    # Keep the bot running until disconnected
      await bot.run_until_disconnected()

if __name__ == "__main__":
  try:
    # await bot.run_until_disconnected()
    asyncio.run(main())
  finally:
    print("Bot shutting down cleanly.")
"""
