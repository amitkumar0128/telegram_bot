from .. import bot 
from telethon import events
import wikipediaapi

@bot.on(events.NewMessage(incoming=True, pattern="/wiki (.*)"))

async def search(event):
    topic = event.text[6:]
    gyf = await event.reply("Searching ...")
    wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='MDL_YT_Bot/1.0 (contact: aj3234@gmail.com)'
)
    page_py = wiki_wiki.page(topic)

    if page_py.exists():
        content = page_py.text[:4096]
    else:
        content = "Page not Found"

    await gyf.edit(content)
