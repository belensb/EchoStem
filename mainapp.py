import discord
from discord.ext import commands
from logging_config import logging_config
import os
from dotenv import load_dotenv

load_dotenv()

logging_config()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
TARGET_CHANNEL = int(os.getenv("TARGET_CHANNEL_ID"))

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
   print(f'Bot connected as {bot.user}')

@bot.event
async def on_voice_state_update(member, before, after):
   if before.channel is None and after.channel is not None:
      if after.channel.id == TARGET_CHANNEL:
         if bot.voice_clients == []:
            await after.channel.connect()

   elif before.channel is not None and after.channel is not None:
      if after.channel.id == TARGET_CHANNEL:
         if bot.voice_clients == []:
            await after.channel.connect()

bot.run(TOKEN)   