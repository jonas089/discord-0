from constants import token
from constants import db as path
import discord
from discord.ext import commands
from other import next, incr, _format
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
    _event = Event(next(), owner, game, date, time)
    _export_event = _event.export()
    if _export_event == None:
        await ctx.send('[Error]: Invalid date or time.')
        return
    db = Database(path)
    db.store(_export_event)
    incr()
    await ctx.send('[Success]: Event added.')
@bot.command()
async def view(ctx):
    db = Database(path)
    _d = _format(db.read())
    await ctx.send('>>> {}'.format(_d))
@bot.command()
async def edit_game(ctx, id, game):
    user = ctx.message.author.mention
    db = Database(path)
    _event = db.read()
    _Event = (
        _event['id'],
        _event['owner'],
        _event['game'],
        _event['date'],
        _event['time']
        )
    _Event.edit_game(game)
    db.remove_id(user, _event['id'])
    db.store(_Event.export())
@bot.command()
async def edit_date(ctx, id, date):
    user = ctx.message.author.mention
    db = Database(path)
    _event = db.read()
    _Event = (
        _event['id'],
        _event['owner'],
        _event['game'],
        _event['date'],
        _event['time']
        )
    _Event.edit_date(date)
    db.remove_id(user, _event['id'])
    db.store(_Event.export())
@bot.command()
async def edit_time(ctx, id, date):
    user = ctx.message.author.mention
    db = Database(path)
    _event = db.read()
    _Event = (
        _event['id'],
        _event['owner'],
        _event['game'],
        _event['date'],
        _event['time']
        )
    _Event.edit_time(time)
    db.remove_id(user, _event['id'])
    db.store(_Event.export())
@bot.command()
async def delete(ctx, id):
    user = ctx.message.author.mention
    db = Database(path)
    if db.remove_id(user, id) == True:
        await ctx.send('>>> {}'.format('[Success]: Event deleted.'))
        return
    await ctx.send('[Error]: Failed to delete event.')
bot.run(token)
