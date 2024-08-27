import discord
from discord import Intents, Message, app_commands
from discord.ext import commands
from typing import Final
from responses import get_response
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
count = 0

@bot.event
async def on_ready() -> None:
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="people")
async def people(interaction: discord.Interaction):
	await interaction.response.send_message(f"There are {count} people in the Robotics room.", ephemeral=True)


@bot.tree.command(name="who")
async def people(interaction: discord.Interaction):
	await interaction.response.send_message(f"There's no one in the Robotics room.", ephemeral=True)

bot.run(TOKEN)