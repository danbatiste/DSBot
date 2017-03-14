import discord
from discord.ext import commands
from modules.color.embedding import embeds, embed
from lxml import html
import requests
import shutil
import os



class Xkcd():
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def xkcd(self, ctx, *, q = ''):
        if not q.isdigit() and not q == '':
            search = requests.get('http://derp.co.uk/xkcd/page?q={}'.format(q))
            searchtree = html.fromstring(search.content)
            try:
                n = searchtree.xpath("//tr/td/a[@target='_blank']/@href")[0].split('/')[~1]
            except:
                await self.bot.say(embed=embed(name='No results.', **embeds['xkcd']['error']))
                return 0
        else:
            n = q
        xkcd_page = 'https://xkcd.com/{}'.format(n)
        page = requests.get(xkcd_page)
        tree = html.fromstring(page.content)

        try:
            #url = 'https:' + tree.xpath("//div[@id='comic']/img/@src")[0]      --Outdated
            url = str(tree.xpath("//div[@id='middleContainer']/text()")[6].split(' ')[~0])[:~0]
        except:
            await self.bot.say(embed=embed(name='No image found.', **embeds['xkcd']['error']))
            return 0
        
        if not url.split('.')[~0] in ['png','jpg','jpeg']:
            await self.bot.say(embed=embed(name='No image found.', **embeds['xkcd']['error']))
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
        
        embed = discord.Embed(url=xkcd_page, title=comic, **embeds['xkcd']['info'])
        embed.add_field(name=title, value='***{}***'.format(mouseover))
        
        await self.bot.send_file(ctx.message.channel, 'temp/xkcd.png')
        await self.bot.say(embed=embed)

        os.remove('temp/xkcd.png')




def setup(bot):
    bot.add_cog(Xkcd(bot))
