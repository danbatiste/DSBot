import discord
from discord.ext import commands
import time



class Time():
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(pass_context=True)
    async def timer(self, ctx, t: int = -1):
        if t == -1:
            await self.bot.delete_message(ctx.message)
            return 0
        await self.bot.edit_message(ctx.message, 'Timer set to {} seconds...'.format(t))
        time.sleep(t)
        await self.bot.say('{} seconds are up!'.format(t))
        


def setup(bot):
    bot.add_cog(Time(bot))
