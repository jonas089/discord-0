from constants import token
import discord
from discord.ext import commands
import sys
sys.path.append('./components')
from event import Event
from storage import Database
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def create(ctx, game, date, time):
    owner = ctx.message.author.mention
    _event = Event()

bot.run(token)
