from telethon import events
from telegram_bot import bot
import openai
import os
from telegram_bot import openai_key


client = openai.OpenAI(api_key=openai_key)

@bot.on(events.NewMessage(incoming = True, pattern ="/ask (.+)"))
async def ask_openai(event):
    prompt = event.pattern_match.group(1)
    await event.reply("🤖 Thinking...")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        answer = response.choices[0].message.content.strip()
        await event.respond(answer)
    except Exception as e:
        await event.reply(str(e), parse_mode=None)
