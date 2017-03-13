import discord
from discord.ext import commands
from modules.emoji.to_reg import emojify
from modules.text.format import *
import random as rand



class Emoji():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def upvote(self, ctx, message_id = None):
        await self.bot.delete_message(ctx.message)
        if message_id == None:
            log = []
            async for m in self.bot.logs_from(ctx.message.channel, 20):
                log += [m]

            message_id = log[0].id

        async for m in self.bot.logs_from(ctx.message.channel, 30):
            if str(m.id) == message_id:
                message = m
                break
        
        if ctx.message.server.id == '136542963336478720':
            await self.bot.add_reaction(message, 'upvote:243900148894138369')
        else:
            await self.bot.add_reaction(message, '\N{THUMBS UP SIGN}')


    @commands.command(pass_context=True)
    async def downvote(self, ctx, message_id = None):
        await self.bot.delete_message(ctx.message)
        if message_id == None:
            log = []
            async for m in self.bot.logs_from(ctx.message.channel, 20):
                log += [m]

            message_id = log[0].id

        async for m in self.bot.logs_from(ctx.message.channel, 30):
            if str(m.id) == message_id:
                message = m
                break
        
        if ctx.message.server.id == '136542963336478720':
            await self.bot.add_reaction(message, 'downvote:243900165583273984')
        else:
            await self.bot.add_reaction(message, '\N{THUMBS DOWN SIGN}')



    @commands.command(pass_context=True)
    async def deepfry(self, ctx, *, message: str):
        await self.bot.delete_message(ctx.message)
        cs = 'bcdfgjklmnpqrstvwxz'
        tdf = []
        fry = lambda c: (c.lower() in tdf) or (rand.randint(0,100) < 19 and c.lower() in cs)
        msg = ''.join(['\🅱️' if fry(c) else c for c in message])
        await self.bot.say(msg)


    @commands.command(pass_context=True)
    async def deeepfry(self, ctx, *, message: str):
        await self.bot.delete_message(ctx.message)
        cs = 'bcdfgjklmnpqrstvwxz'
        fry = lambda c: c.lower() in cs
        msg = ''.join(['\🅱️' if fry(c) else c for c in message])
        await self.bot.say(msg)


    @commands.command(pass_context=True)
    async def midge(self, ctx, n = 0):
        await self.bot.delete_message(ctx.message)
        if not n:
            await self.bot.send_file(ctx.message.channel, 'res/midge.png')
        elif n > 0 and ctx.message.server.id == '136542963336478720':
            msg = ['<:midge:286338835435225090>' for midge in range(n)]
            await self.bot.say(''.join(msg))
        elif ctx.message.server.id == '136542963336478720':
            self.bot.say('<:midge:286338835435225090>')


    @commands.command(pass_context=True)
    async def rect(self, ctx, x: int, y: int, outer = ':black_large_square:', inner = ':white_large_square:'):
        bs = outer
        ws = inner
        top = ''.join([bs]*x)
        mid = ''.join([bs] + (x-2)*[ws] + [bs])
        bottom = top
        rect = '\n'.join([top] + [mid]*(y-2) + [bottom])
        await self.bot.delete_message(ctx.message)
        await self.bot.say(rect)


    @commands.command(pass_context=True)
    async def heart(self, ctx, H = ':heart:', r = ':gay_pride_flag:'):
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
        await self.bot.delete_message(ctx.message)
        await self.bot.say(msg)



def setup(bot):
    bot.add_cog(Emoji(bot))
