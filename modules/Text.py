import discord
from discord.ext import commands
import modules.symbols as symbols
from modules.math.format.mathf import mformat
from modules.emoji.to_reg import emojify
from modules.text.format import *
import time



class Text():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def say(self, ctx, *, message: str):
        await self.bot.delete_message(ctx.message)
        await self.bot.say(message)


    @commands.command(pass_context=True)
    async def sd(self, ctx, t: int, *, message: str):
        i = t
        while i > 0:
            await self.bot.edit_message(ctx.message, '`' + str(i) + 's` | ' + message)
            time.sleep(1)
            i -= 1
        await self.bot.delete_message(ctx.message)


    @commands.command(pass_context=True)
    async def n(self, ctx, a: int, b: int, s: int, *, message: str):
        msg = message.split('$n')
        for i in range(a, b+1)[::s]:
            await self.bot.edit_message(ctx.message, str(i).join(msg))
            time.sleep(1)


    @commands.command(pass_context=True)
    async def hug(self, ctx, *names: str):
        await self.bot.delete_message(ctx.message)
        for name in names:
            await self.bot.say('*hugs {}*'.format(name))


    @commands.command(pass_context=True)
    async def re(self, ctx, n: int, caps = True):
        await self.bot.delete_message(ctx.message)
        if caps:
            await self.bot.say('R' + 'E'*n)
        else:
            await self.bot.say('r' + 'e'*n)


    @commands.command(pass_context=True)
    async def all(self, ctx, *, message: str):
        await self.bot.delete_message(ctx.message)
        await self.bot.say('***__{}__***'.format(message))


    @commands.command(pass_context=True)
    async def py(self, ctx, *, message: str):
        await self.bot.delete_message(ctx.message)
        await self.bot.say(str(eval(message)))


    @commands.command(pass_context=True)
    async def mathf(self, ctx, *, message: str):
        await self.bot.delete_message(ctx.message)
        await self.bot.say(mformat(message))


    @commands.command(pass_context=True)
    async def shrug(self, ctx, *, message = ''):
        await self.bot.delete_message(ctx.message)
        await self.bot.say(message + ' ¯\\_(ツ)_/¯')


    @commands.command(pass_context=True)
    async def read(self, ctx, path):
        await self.bot.delete_message(ctx.message)
        tmp = []

        with open('temp/' + path, 'rb') as file:
            for line in file:
                tmp += [line.decode('utf-8')]
        message = '\n'.join(tmp)
        
        if len(message) > 2000:
            msgs = chunk(message, 2000)
            for msg in msgs:
                await self.bot.say(msg)
        else:
            await self.bot.say(message)


    @commands.command(pass_context=True)
    async def aes(self, ctx, *, message: str):
        await self.bot.delete_message(ctx.message)
        msg = ''
        for char in message:
            if 'aes_{}'.format(char) in symbols.aesthetic:
                msg += symbols.aesthetic['aes_{}'.format(char)]
                continue
            msg += char
        await self.bot.say(msg)


    @commands.command(pass_context=True)
    async def e(self, ctx, *, message):
        await self.bot.delete_message(ctx.message)
        await self.bot.say(emojify(message))


    @commands.command(pass_context=True)
    async def bb(self, ctx, *, message: str):
        await self.bot.delete_message(ctx.message)
        msg = ''
        for char in message:
            if 'bb_{}'.format(char) in symbols.blackboard:
                msg += symbols.blackboard['bb_{}'.format(char)]
                continue
            msg += char
        await self.bot.say(msg)



def setup(bot):
    bot.add_cog(Text(bot))
