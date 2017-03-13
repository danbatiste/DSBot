import discord
from discord.ext import commands
import modules.symbols as symbols
from modules.math.format.mathf import mformat
from modules.color.embedding import embed, embeds
from modules.color.color import colors
from modules.emoji.to_reg import emojify
from modules.text.format import *
import time
import datetime



class Text():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def quote(self, ctx, message_id: str, channel_id: str = None):
        await self.bot.delete_message(ctx.message)
        if channel_id == None: channel_id = ctx.message.channel.id
        channel = self.bot.get_channel(channel_id)
        async for m in self.bot.logs_from(channel, 10000):
            if str(m.id) == message_id:
                t = m.timestamp
                td = datetime.date.today()

                if (t.day - 1, t.month, t.year) == (td.day, td.month, td.year):
                    day = 'Today'
                else:
                    day = '{}/{}/{}'.format(t.year, t.month, t.day - 1)

                hour, minute = (t.hour + 17)%24, ('0' + str(t.minute))[~1:]
                merid = 'PM'
                if hour < 12:
                    merid = 'AM'
                hour = hour%12
                date = '{day} at {hour}:{minute} {merid}'.format(day=day, hour=hour, minute=minute, merid=merid)
                footer = 'In {} - {}'.format(m.channel, date)
                try:
                    colour = m.author.colour
                except:
                    colour = colors['white']
                embed = discord.Embed(inline=False, colour=colour, description=m.clean_content)
                embed.set_footer(text=footer)
                embed.set_author(name=m.author.display_name, icon_url='{0.avatar_url}'.format(m.author))
                await self.bot.say(embed=embed)
                return 0


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
    async def ssd(self, ctx, t: float, *, message: str):
        await self.bot.edit_message(ctx.message, message)
        time.sleep(t)
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
    async def lenny(self, ctx, *, message = ''):
        await self.bot.delete_message(ctx.message)
        await self.bot.say(message + ' ( ͡° ͜ʖ ͡°)')


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
