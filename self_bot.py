import discord
from discord.ext import commands
from modules.math.solve import iterate
from modules.emoji.to_reg import emojify
from modules.math.format.mathf import mformat
from modules.color.embedding import embed, embeds
from modules.color.color import colors
from lxml import html
from configparser import SafeConfigParser
import string
import modules.symbols as symbols
import requests
import shutil
import os
import sys
import asyncio
import time
import random



config = SafeConfigParser()
config.read('config.ini')


description = 'A selfbot for Discord by danb'
prefix = config.get('main', 'prefix')
bot = commands.Bot(command_prefix=[prefix], description=description, self_bot=True, help_attrs={'name':'0'*100})



@bot.event
async def on_ready():
    print('---------------------------')
    print('          SelfBot          ')
    print('---------------------------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------------------')
    bot.load_extension('modules.Xkcd')
    bot.load_extension('modules.Misc')
    bot.load_extension('modules.Text')
    bot.load_extension('modules.Emoji')
    bot.load_extension('modules.Help')
    #bot.load_extension('modules.CustomCommands')


@bot.event
async def send(channel, message):
    await bot.send_message(channel, message)


@bot.command(pass_context=True)
async def purge(ctx, n=100):
    count = -1
    async for log in bot.logs_from(ctx.message.channel, limit=1000000):
        if log.author == ctx.message.author and count < n:
            count += 1
            await bot.delete_message(log)


@bot.command(pass_context=True)
async def reload(ctx):
    await bot.delete_message(ctx.message)
    os.system('cls')
    os.system(sys.argv[0])
    os._exit(0)


@bot.command(pass_context=True)
async def status(ctx, *, message: str):
    game = discord.Game(name=message)
    await bot.delete_message(ctx.message)
    await bot.change_presence(game=game)


@bot.command(pass_context=True)
async def update():
    os.system('update.py')


@bot.command(pass_context=True)
async def de(ctx, *, message: str):
    await bot.delete_message(ctx.message)
    await bot.say(embed=discord.Embed(colour=colors['default'], description=message))


@bot.command(pass_context=True)
async def link(ctx):
    await bot.delete_message(ctx.message)
    url = 'https://github.com/danbatiste/DSBot'
    description = 'DSBot - A self bot for Discord, written in Python'
    title = 'danbatiste/DSBot'
    embed = discord.Embed(url=url, title=title, description=description, colour=colors['default'])
    embed.set_thumbnail(url='https://avatars0.githubusercontent.com/u/22204498?v=3&s=460')
    embed.set_author(name='GitHub', url=url)

    await bot.say(embed=embed)



@bot.command(pass_context=True)
async def em(ctx, color: str, *, message: str):
    await bot.delete_message(ctx.message)
    try:
        await bot.say(embed=discord.Embed(colour=colors[color], description=message))
    except:
        await bot.say(embed=discord.Embed(colour=eval(color), description=message))



bot.run(config.get('main', 'token'), bot=False)

