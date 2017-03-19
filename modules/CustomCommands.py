# -*- coding: utf-8 -*-
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
    
    global cmds
    with open('res/commands.json', 'r+', encoding='utf-8') as file:
        cmds = json.load(file)

    for k, v in cmds.items():
        exec('''
@commands.command(pass_context=True)
async def {cmd}(self, ctx, *, message: str = ''):
    await self.bot.delete_message(ctx.message)
    await self.bot.say(message + " {value}")
'''.format(cmd=k, value=v))


    @commands.command()
    async def command(self, action: str, key: str = None, value: str = None):
        file = open('res/commands.json', 'r+', encoding='utf-8')
        cmds = json.load(file)

        if action in ['new', '+', 'add', 'plus'] and not value == None:
            cmds.update({ key : value })
            file.seek(0)
            json.dump(cmds, file, indent=4)
            file.truncate()
            self.bot.load_extension('modules.CustomCommands')
            await self.bot.say('Command `{}` added with value `{}`'.format(key, value))

        elif action in ['del', '-', 'remove', 'delete', 'rem']:
            del cmds[key]
            file.seek(0)
            json.dump(cmds, file, indent=4)
            file.truncate()
            self.bot.load_extension('modules.CustomCommands')
            await self.bot.say('Command `{}` removed.'.format(key))

        elif action in ['list', 'ls', 'enum', 'enumerate', 'lsit']:
            msg = '__**Avaliable Commands:**__\n'
            for k, v in cmds.items():
                msg += '{} ` -> ` {}\n'.format(k, v)
            await self.bot.say(msg)

        else:
            await self.bot.say('Command not found. Type `{}help command` for more.'.format(prefix))

        file.close()



def setup(bot):
    bot.add_cog(CustomCommands(bot))
