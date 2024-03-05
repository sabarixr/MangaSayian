import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from bot.commands import bot_commands

load_dotenv()
DISCORD_API = os.getenv("DISCORD_API")
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all(), help_command=None, link_command = None)

bot_commands(bot)

if __name__ == "__main__":
    bot.run(DISCORD_API)
