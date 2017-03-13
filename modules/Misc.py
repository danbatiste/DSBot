import discord
from discord.ext import commands
from modules.math.solve import iterate
from PIL import Image
from configparser import SafeConfigParser
from modules.color.color import colors
import io
import random
import time



config = SafeConfigParser()
config.read('config.ini')



class Misc():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def color(self, ctx, colour = 'default'):
        await self.bot.delete_message(ctx.message)
        try:
            color = colors[colour]
        except:
            color = colour

        if type(color) == type(discord.Colour.red()):
            color = color.to_tuple()
        else:
            color = '#' + format(color, 'x')

        image = Image.new("RGB", (100, 100), color)
        imgByteArr = io.BytesIO()
        image.save(imgByteArr, format='PNG')
        imgByteArr = imgByteArr.getvalue()


        await self.bot.edit_profile(config.get('main', 'password'), avatar=imgByteArr)

        

    @commands.command(pass_context=True)
    async def hi(self, ctx):
        time.sleep(0.4)
        await self.bot.delete_message(ctx.message)
        await self.bot.say('hi')


    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await self.bot.delete_message(ctx.message)
        tmp = await self.bot.say('pong')
        time.sleep(5)
        await self.bot.delete_message(tmp)


    @commands.command(pass_context=True)
    async def pingu(self, ctx):
        #await self.bot.delete_message(ctx.message)
        await self.bot.say(random.choice(['noot','pongu']))


    @commands.command(pass_context=True)
    async def _solve(self, ctx, x0: int, iterations, *, y: str):
        ys = y
        await self.bot.delete_message(ctx.message)
        await self.bot.say('Q: `x = {}`'.format(ys))
        x_ = iterate(ys, iterations, x0)
        await self.bot.say('=> `x = {}`'.format(str(x_)))


    @commands.command(pass_context=True)
    async def solve(self, ctx, *, y: str):
        y = ''.join(y.split(' '))
        if y[:2] == 'x=':
            y = y[2:]
        x0 = 2
        iterations = 100000
        ys = y
        await self.bot.say('`Q:` `x = {}`'.format(ys))
        x_ = iterate(ys, iterations, x0)
        await self.bot.say('`=>` `x = {}`'.format(str(x_)))


    @commands.command(pass_context=True)
    async def avatar(self, ctx, member: discord.Member):
        await self.bot.delete_message(ctx.message)
        await self.bot.say('{0.avatar_url}'.format(member))


def setup(bot):
    bot.add_cog(Misc(bot))
