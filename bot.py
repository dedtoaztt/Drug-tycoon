import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

initial_extensions = ["commands.start", "commands.grow", "commands.harvest", "commands.sell"]

for ext in initial_extensions:
    bot.load_extension(ext)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name}")

bot.run(TOKEN)