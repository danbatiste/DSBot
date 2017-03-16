import discord
from discord.ext import commands
from configparser import SafeConfigParser
from pprint import pprint
import os
import json


config = SafeConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname( __file__ )), '..', 'config.ini'))
prefix = config.get('main', 'prefix')


class CustomCommands():
    def __init__(self, bot):
        self.bot = bot
    with open('res/commands.json') as file:
        cmds = json.load(file)


    @commands.command()
    async def command(action: str, key: str, value: str = None):
        global cmds
        if action in ['new', '+', 'add'] and not value == None:
            cmds.update({ key : value })
        elif action in ['del', '-', 'remove', 'delete']:
            del cmd[key]
        else:
            await self.bot.say('Command not found. Type `{}halp command` for more.'.format(prefix))

    for cmd in list(cmds):
        for k, v in cmd.items():
            exec('''
@commands.command(pass_context=True)
async def {cmd}(self, ctx):
    await self.bot.delete_message(ctx.message)
    await self.bot.say("{value}")
'''.format(cmd=k, value=v))


def setup(bot):
    bot.add_cog(CustomCommands(bot))
