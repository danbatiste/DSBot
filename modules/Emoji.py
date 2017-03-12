import discord
from discord.ext import commands
from modules.emoji.to_reg import emojify
from modules.text.format import *



class Emoji():
    def __init__(self, bot):
        self.bot = bot


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
