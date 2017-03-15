import discord
from discord.ext import commands

class Blank():
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Blank(bot))
