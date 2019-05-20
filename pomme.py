import discord
from discord.ext import commands
import os
import random

bot = commands.Bot(commands.when_mentioned_or('='))
bot.remove_command(name="help")


@bot.event
async def on_ready(ctx):
    await bot.change_presence(activity=discord.Game(name="V1.4 | =help"))



bot.run(os.getenv('TOKEN'))
