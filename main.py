import os
from dotenv import load_dotenv
import discord
import random
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    if message.author == client.user:
            return
    elif any(keyword in message.content.lower() for keyword in ["!v", "<@1402784150301184020>]", "@Venti", "hey venti", "hi venti", "hello venti", "venti,"):
	


keep_alive()
client.run(TOKEN)
