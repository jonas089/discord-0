from constants import token
import discord
import random
import os
from discord.ext import commands
from storage import read, write, push, edit, delete, clear, id, signup, ownerof
from help import helpmessage, helpmessage_fmt
from catlist import cats
import time
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def _timestamp(m2, m3):
    try:
        timestr = m2 + ' ' + m3 + ':00'
        print(timestr)
        timestamp = time.mktime(time.strptime(timestr, "%d.%m.%Y %H:%M:%S"))
        print("timestamp: ", timestamp)
        return timestamp
    except Exception as timeError:
        print(timeError)
        return False

# FUN
@bot.command(
    help='Renders a cute cat image to the channel.',
    brief='Get cute cat'
)
async def cat(ctx):
    index = random.randint(0, len(cats) - 1)
    await ctx.send(cats[index])

# Gaming-Sessions
@bot.command(
    help=helpmessage,
    brief='Create and Join Gaming Sessions'
)
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    user = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    msg = str(message.content)
    print(f'Message {msg} by {user} on {channel}')
    # commands must have prefix.
    if not msg.startswith('!'):
        return


    # ADMIN
    if msg.startswith('!clean') and user == '$CSPR.R&D(Jonas)':
        clear()
        await message.channel.send(
        '''
        Admin command Executed.
        All data is lost.
        '''
        )

    # PROPOSE
    elif msg.startswith('!propose'):
        m = msg.split()
        _id = id()
        data = read()
        for d in data:
            if d['id'] == _id:
                _id += 1
        proposal = {
            'id':_id,
            'creator':user,
            'game':m[1],
            'date': m[2],
            'time': m[3],
            'participating': [user]
        }
        if _timestamp(m[2], m[3]) == False:
            await message.channel.send(
            '''
            Invalid Format: Make sure the date and time is formatted according to this pattern: d.m.Y h:m \n example: 12.02.2012 16:30
            '''
            )
            return
        # add proposal to db
        write(push(read(), proposal))
        await message.channel.send(
        '''
        Your Gaming Session was added to the list.\nWait for friends to join and use !view to list all sessions.
        ''')

    # VIEW
    elif msg.startswith('!view'):
        data = read()
        res = ''
        for p in data:
            print(p)
            print(p['id'])
            res += ':id: ' + str(p['id']) + '\n' + 'creator: ' + p['creator'] + '\n' + 'game: ' + p['game'] + '\n' + 'date: ' + p['date'] + '\n' + 'time: ' + p['time'] + '\n' + 'participating: ' + str(p['participating']) + '\n' + '-'*5 + '\n'
        if len(res) == 0:
            await message.channel.send("no outstanding gaming sessions.")
            return
        await message.channel.send(res)
    elif msg.startswith('!join'):
        m = msg.split()
        res = signup(int(m[1]), user)
        if res == True:
            await message.channel.send("Successfully joined session #" + m[1])
        else:
            await message.channel.send("Failed to join session #" + m[1])

    # EDIT
    elif msg.startswith('!edit'):
        m = msg.split()
        if ownerof(int(m[1])) == False:
            await message.channel.send("Failed to edit session #" + m[1])
            return
        elif ownerof(int(m[1])) != user:
            await message.channel.send("Failed to edit session #" + m[1])
            return
        proposal = {
            'id':int(m[1]),
            'creator':user,
            'game':m[2],
            'date': m[3],
            'time': m[4],
            'participating': [user]
        }
        res = edit(int(m[1]), proposal)
        if res == True:
            await message.channel.send("Successfully edited session #" + m[1])
        else:
            await message.channel.send("Failed to edit session #" + m[1])

    # DELETE
    elif msg.startswith('!delete'):
        m = msg.split()
        if ownerof(int(m[1])) == False:
            await message.channel.send("Failed to delete session #" + m[1])
            return
        elif ownerof(int(m[1])) != user:
            await message.channel.send("Failed to edit session #" + m[1])
            return

        res = delete(int(m[1]))
        if res == True:
            await message.channel.send("Successfully deleted session #" + m[1])
        else:
            await message.channel.send("Failed to delete session #" + m[1])

    # ME
    elif msg.startswith('!me'):
        res = f'{user} is participating in these sessions: \n'
        data = read()
        for p in data:
            if user in p['participating']:
                res += ':id: ' + str(p['id']) + '\n' + 'creator: ' + p['creator'] + '\n' + 'game: ' + p['game'] + '\n' + 'date: ' + p['date'] + '\n' + 'time: ' + p['time'] + '\n' + 'participating: ' + str(p['participating']) + '\n' + '-'*5 + '\n'
        if len(res) == 0:
            await message.channel.send("You are not participating in any sessions.")
            return
        await message.channel.send(res);

    elif msg.startswith('!autoclean'):
        cnt = 0
        data = read()
        now = time.time()
        day = 86400
        for d in data:
            if _timestamp(d['date'], d['time']) + day <= now:
                data.remove(d)
                cnt += 1
        write(data)
        await message.channel.send("Deleted " + str(cnt) + " old sessions.")


    # HELP
    elif msg.startswith('!help'):
        await message.channel.send(helpmessage_fmt)
bot.run(token)
