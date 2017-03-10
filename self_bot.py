import discord
from discord.ext import commands
from modules.math.solve import iterate
from modules.emoji.to_reg import emojify
from modules.math.format.mathf import mformat
from lxml import html
import modules.symbols as symbols
import requests
import shutil
import os
import sys
import json
import asyncio
import time
import random

description = 'A bot to do things that are useful'
prefix = '.'
bot = commands.Bot(command_prefix=[prefix], description=description, self_bot=True)

def camel(string):
    return string[0].upper() + string[1:].lower()

###################
## Startup Stuff ##
###################

@bot.event
async def on_ready():
    print('---------------------------')
    print('          SelfBot          ')
    print('---------------------------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------------------')
    bot.load_extension('modules.moderation')


@bot.event
async def send(channel, message):
    await bot.send_message(channel, message)

######################
###    Commands    ###
######################

@bot.command(pass_context=True)
async def hi(ctx):
    time.sleep(0.4)
    await bot.delete_message(ctx.message)
    await bot.say('hi')


@bot.command(pass_context=True, hidden=True)
async def ping(ctx):
    await bot.delete_message(ctx.message)
    tmp = await bot.say('pong')
    time.sleep(5)
    await bot.delete_message(tmp)


@bot.command(pass_context=True, hidden=True)
async def sd(ctx, t: int, *, message: str):
    i = t
    while i > 0:
        await bot.edit_message(ctx.message, '`' + str(i) + 's` | ' + message)
        time.sleep(1)
        i -= 1
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True, hidden=True)
async def _(ctx, n=1000000):
    count = -1
    async for log in bot.logs_from(ctx.message.channel, limit=1000000):
        if log.author == ctx.message.author and count < n:
            count += 1
            await bot.delete_message(log)


@bot.command(pass_context=True)
async def count(ctx):
    counter = 0
    async for log in bot.logs_from(ctx.message.channel, limit=1000000):
        counter += 1
    await bot.say('Counted `{}` messages'.format(counter))


@bot.command(pass_context=True, hidden=True)
async def e(ctx, *, message):
    await bot.delete_message(ctx.message)
    await bot.say(emojify(message))


@bot.command(pass_context=True, hidden=True)
async def n(ctx, a: int, b: int, s: int, *, message: str):
    msg = message.split('$n')
    for i in range(a, b+1)[::s]:
        await bot.edit_message(ctx.message, str(i).join(msg))
        time.sleep(1)


@bot.command(pass_context=True, hidden=True)
async def rect(ctx, x: int, y: int, outer = ':black_large_square:', inner = ':white_large_square:'):
    bs = outer
    ws = inner
    top = ''.join([bs]*x)
    mid = ''.join([bs] + (x-2)*[ws] + [bs])
    bottom = top
    rect = '\n'.join([top] + [mid]*(y-2) + [bottom])
    await bot.delete_message(ctx.message)
    await bot.say(rect)


@bot.command(pass_context=True, hidden=True)
async def hug(ctx, *names: str):
    await bot.delete_message(ctx.message)
    for name in names:
        await bot.say('*hugs {}*'.format(name))


@bot.command(pass_context=True, hidden=True)
async def heart(ctx, H = ':heart:', r = ':gay_pride_flag:'):
    heart =[[r,r,r,r,r,r,r,r,r,r,r],
            [r,r,H,H,H,r,H,H,H,r,r],
            [r,H,H,H,H,H,H,H,H,H,r],
            [r,H,H,H,H,H,H,H,H,H,r],
            [r,r,H,H,H,H,H,H,H,r,r],
            [r,r,r,H,H,H,H,H,r,r,r],
            [r,r,r,r,H,H,H,r,r,r,r],
            [r,r,r,r,r,H,r,r,r,r,r],
            [r,r,r,r,r,r,r,r,r,r,r]]
    heart_c = []
    for line in heart:
        heart_c += [''.join(line)]
    msg = '\n'.join(heart_c)
    await bot.delete_message(ctx.message)
    await bot.say(msg)


@bot.command(pass_context=True)
async def re(ctx, n: int, caps = True):
    await bot.delete_message(ctx.message)
    if caps:
        await bot.say('R' + 'E'*n)
    else:
        await bot.say('r' + 'e'*n)


@bot.command(pass_context=True)
async def all(ctx, *, message: str):
    await bot.delete_message(ctx.message)
    await bot.say('***__{}__***'.format(message))


@bot.command(pass_context=True)
async def rel(ctx):
    await bot.delete_message(ctx.message)
    os.system('cls')
    os.system(sys.argv[0])
    sys.exit()


@bot.command(pass_context=True)
async def py(ctx, *, message: str):
    await bot.delete_message(ctx.message)
    await bot.say(str(eval(message)))


@bot.command(pass_context=True)
async def status(ctx, *, message: str):
    game = discord.Game(name=message)
    await bot.delete_message(ctx.message)
    await bot.change_presence(game=game)


@bot.command(pass_context=True)
async def _solve(ctx, x0: int, iterations, *, y: str):
    ys = y
    await bot.delete_message(ctx.message)
    await bot.say('Q: `x = {}`'.format(ys))
    x_ = iterate(ys, iterations, x0)
    await bot.say('=> `x = {}`'.format(str(x_)))


@bot.command(pass_context=True)
async def mathf(ctx, *, message: str):
    await bot.delete_message(ctx.message)
    await bot.say(mformat(message))


@bot.command(pass_context=True)
async def shrug(ctx, *, message: str):
    await bot.delete_message(ctx.message)
    await bot.say(message + ' ¯\\_(ツ)_/¯')


@bot.command(pass_context=True)
async def solve(ctx, *, y: str):
    y = ''.join(y.split(' '))
    if y[:2] == 'x=':
        y = y[2:]
    x0 = 2
    iterations = 100000
    ys = y
    await bot.say('`Q:` `x = {}`'.format(ys))
    x_ = iterate(ys, iterations, x0)
    await bot.say('`=>` `x = {}`'.format(str(x_)))


@bot.command(pass_context=True)
async def avatar(ctx, member: discord.Member):
    await bot.delete_message(ctx.message)
    await bot.say('{0.avatar_url}'.format(member))


@bot.command(pass_context=True)
async def bb(ctx, *, message: str):
    await bot.delete_message(ctx.message)
    msg = ''
    for char in message:
        if 'bb_{}'.format(char) in symbols.blackboard:
            msg += symbols.blackboard['bb_{}'.format(char)]
            continue
        msg += char
    await bot.say(msg)


@bot.command(pass_context=True)
async def say(ctx, *, message: str):
    await bot.delete_message(ctx.message)
    await bot.say(message)


@bot.command(pass_context=True)
async def aes(ctx, *, message: str):
    await bot.delete_message(ctx.message)
    msg = ''
    for char in message:
        if 'aes_{}'.format(char) in symbols.aesthetic:
            msg += symbols.aesthetic['aes_{}'.format(char)]
            continue
        msg += char
    await bot.say(msg)


@bot.command(pass_context=True)
async def xkcd(ctx, *, q = ''):
    if not q.isdigit() and not q == '':
        search = requests.get('http://derp.co.uk/xkcd/page?q={}'.format(q))
        searchtree = html.fromstring(search.content)
        try:
            n = searchtree.xpath("//tr/td/a[@target='_blank']/@href")[0].split('/')[~1]
        except:
            await bot.say(embed=embed(name='No results.', **embeds['xkcd']['error']))
            return 0
    else:
        n = q

    page = requests.get('https://xkcd.com/{}'.format(n))
    tree = html.fromstring(page.content)

    try:
        #url = 'https:' + tree.xpath("//div[@id='comic']/img/@src")[0]      --Outdated
        url = str(tree.xpath("//div[@id='middleContainer']/text()")[6].split(' ')[~0])[:~0]
    except:
        await bot.say(embed=embed(name='No image found.', **embeds['xkcd']['error']))
        return 0
    
    if not url.split('.')[~0] in ['png','jpg','jpeg']:
        await bot.say(embed=embed(name='No image found.', **embeds['xkcd']['error']))
        return 0

    mouseover = '\u034f'
    try:
        mouseover = tree.xpath("//div[@id='comic']/a/img/@title")[0]
    except:
        mouseover = tree.xpath("//div[@id='comic']/img/@title")[0]

    title = '__**{}**__'.format(tree.xpath("//div[@id='ctitle']/text()")[0])
    comicnum = tree.xpath("//div[@id='middleContainer']/text()")[5].split('/')[~1]
    comic = 'xkcd #{}'.format(comicnum)

    file = requests.get(url, stream=True)
    fdump = file.raw
    with open('temp/xkcd.png', 'wb') as path:
        shutil.copyfileobj(fdump, path)
    
    await bot.send_file(ctx.message.channel, 'temp/xkcd.png')
    #await bot.say('**{}**'.format(title))
    await bot.say(embed=embed(name=title, value='***{}***'.format(mouseover), description=comic, **embeds['xkcd']['info']))


@bot.command(pass_context=True)
async def g(ctx, *, message: str):
    await bot.delete_message(ctx.message)
    await bot.say(embed=discord.Embed(colour=colours['sus_green'], description=message))

@bot.command(pass_context=True)
async def em(ctx, colour: str, *, message: str):
    await bot.delete_message(ctx.message)
    await bot.say(embed=discord.Embed(colour=eval(colour), description=message))


################
## HELP STUFF ##
################

@bot.command()
async def halp(cmd = '', attr = ''):
    global cmds
    global em
    if not cmd:
        cmdlist = [command for command in cmds]
        formatted = ['`{}`'.format(cmd) for cmd in cmdlist[:~1]]
        message = ''.join([
            '{} and {}.'.format(', '.join(formatted), '`{}`'.format(cmdlist[~0])),
            'Type `{}halp command` for more info about a specific command.'.format(prefix),
            ])
        await bot.say(embed=embed(value=message, **embeds['halp']['main']))
        return 0

    if not cmd in cmds:
        message = 'Command `{}` not found.'
        await bot.say(embed=embed(value=message, **embeds['halp']['info']))
        return 0

    if attr and camel(attr) not in cmds[cmd]:
        message = '{} not an attribute of `{}`'.format(camel(attr), cmd)
        await bot.say(embed=embed(value=message, **embeds['halp']['info']))
        return 0

    if attr:
        message = '**__{}__**: {}'.format(camel(attr), cmds[cmd][camel(attr)])
        await bot.say(embed=embed(value=message, **embeds['halp']['info']))
        return 0

    usage = '**__Usage:__** {}'.format(cmds[cmd]['Usage'])
    info = '**__Info:__** {}'.format(cmds[cmd]['Info'])
    message = '\n'.join([usage, info])
    await bot.say(embed=embed(value=message, **embeds['halp']['info']))


colours = {
    'default'   : 0x1f8b4c,
    'brown'     : 0x795548,
    'sus_green' : 0x1f8b4c,
}

def embed(description='\u034f', colour=colours['default'], name='\u034f', value='\u034f', inline=True):
    data = discord.Embed(description=description, colour=colour)
    data.add_field(name=name, value=value)
    #data.set_author(name='Author', icon_url='Image URL to set as the thumbnail for the embed here')
    return data


embeds = {
    'halp' : {
        'main' : {
            'description'   : 'Halp menu',
            'colour'        : colours['default'],
            'name'          : 'Available Commands:',
            'inline'        : True,
        },

        'info' : {
            'description'   : 'Halp menu',
            'colour'        : colours['default'],
            'name'          : 'Command Info',
            'inline'        : True,
        },
    },

    'xkcd' : {
        'error' : {
            'colour'        : colours['default'],
            'inline'        : True,
        },

        'info' : {
            'colour'        : colours['default'],
            'inline'        : True,
        },
    },

}


cmds = {
    'halp' : {
        'Usage' : '1{}help [command]`'.format(prefix),
        'Info'  : 'Displays all commands, and displays information about specific commands',
        },

    'reload' : {
        'Usage' : '`{}reload`'.format(prefix),
        'Info'  : 'Reloads the bot.',
        },

    'say'   : {
        'Usage' : '`{}say message`'.format(prefix),
        'Info'  : 'Has the bot say a message.',
        },

    'solve' : {
        'Usage' : '`{}solve [x=]y`'.format(prefix),
        'Info'  : 'Solves an equation in the form of `x = y`, as long as the limit as x approaches infinity for `y` is less than that of `ln(x)`.'
        },

    'avatar': {
        'Usage' : '`{}avatar user`'.format(prefix),
        'Info'  : "Posts a link to a user's avatar.",
        },

    'ping'  : {
        'Usage' : '`{}ping`'.format(prefix),
        'Info'  : 'pong.',
        },

    'xkcd'  : {
        'Usage' : '`{}xkcd [comic # | search term]`'.format(prefix),
        'Info'  : 'Finds an xkcd comic by number or search term, and then displays it in chat. Can also invoke the command without arguments to display the most recent xkcd.',
        },
}


##############################
## FANCY TOKEN LOGIN STUFFS ##
##############################

with open('self_token.txt') as token:
    bot.run(token.read(), bot=False)

