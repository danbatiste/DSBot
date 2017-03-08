import discord
import asyncio
import os
import sys
import requests
import shutil
from modules.math.solve import iterate
from discord.ext import commands
from lxml import html

description = 'BIRB'
prefix = '$'
p = prefix
bot = commands.Bot(command_prefix=[prefix], description=description, self_bot=False)

def camel(string):
    return string[0].upper() + string[1:].lower()


###################
## Startup Stuff ##
###################

@bot.event
async def on_ready():
    print('---------------------------')
    print('          BirdBot          ')
    print('---------------------------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------------------')


@bot.event
async def send(channel, message):
    await bot.send_message(channel, message)


######################
###    Commands    ###
######################

@bot.command()
async def about():
    await bot.say(description)


@bot.command()
async def say(*, msg):
    await bot.say(msg)


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
    await bot.say('{0.avatar_url}'.format(member))


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say('pong')


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
async def status(ctx, *, message: str):
    game = discord.Game(name=message)
    await bot.delete_message(ctx.message)
    await bot.change_presence(game=game)


@bot.command(pass_context=True)
async def reload(ctx):
    await bot.delete_message(ctx.message)
    os.system('cls')
    os.system(sys.argv[0])
    sys.exit()


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


def embed(description='\u034f', colour=discord.Colour.red(), name='\u034f', value='\u034f', inline=True):
    data = discord.Embed(description=description, colour=colour)
    data.add_field(name=name, value=value)
    #data.set_author(name='Author', icon_url='Image URL to set as the thumbnail for the embed here')
    return data


colors = {
    'brown' : 0x795548,
}


embeds = {
    'halp' : {
        'main' : {
            'description'   : 'Halp menu',
            'colour'        : colors['brown'],
            'name'          : 'Available Commands:',
            'inline'        : True,
        },

        'info' : {
            'description'   : 'Halp menu',
            'colour'        : colors['brown'],
            'name'          : 'Command Info',
            'inline'        : True,
        },
    },

    'xkcd' : {
        'error' : {
            'colour'        : colors['brown'],
            'inline'        : True,
        },

        'info' : {
            'colour'        : colors['brown'],
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

with open('bot_token.txt') as token:
    bot.run(token.read(), bot=True)

