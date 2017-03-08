import discord
from discord.ext import commands

class Moderation():
    def __init__(self, bot):
        self.bot = bot

    ##############################
    ## Misc moderation commands ##
    ##############################

    # Changes the bot's game
    @commands.command(pass_conext=True)
    async def changegame(self, *, game: str):
        """Updates the Bot's game"""
        # Update the bots game
        await self.bot.change_status(discord.Game(name=game))
        await self.bot.say("Game updated.")
        print("Updated Bot's Game")

    ##################################
    ## Banning and Kicking commands ##
    ##################################

    # Bans a member
    @commands.command()
    async def ban(self, member: discord.Member = None):
        """Bans a member"""
        # Are they trying to ban nobody? Are they stupid?
        # Why do they have mod powers if they're this much of an idiot?
        if member is None:
            return
        # Is the person being banned me? No we don't allow that
        elif member.id == '95953002774413312':
            await self.bot.say("http://i.imgur.com/BSbBniw.png")
            return
        # Bans the user
        await self.bot.ban(member, delete_message_days=1)
        # Prints to console
        print("{0.name} has been banned".format(member))

    # Kicks a member
    @commands.command()
    async def kick(self, member: discord.Member = None):
        """Kicks a member"""
        # Are they trying to kick nobody? Are they stupid?
        # Why do they have mod powers if they're this much of an idiot?
        if member is None:
            return
        # Is the person being banned me? No we don't allow that
        elif member.id == '95953002774413312':
            await self.bot.say("http://i.imgur.com/BSbBniw.png")
            return
        # Bans the user
        await self.bot.kick(member)
        # Prints to console
        print("{0.name} has been kicked".format(member))

    #################################
    ## Information commands        ##
    ## Server info and member info ##
    #################################

    # Gives the user some basic info on a user
    @commands.command(pass_context=True)
    async def info(self, ctx, member : discord.Member = None):
        """Gives basic info and shows profile image of a user."""
        if member == None:
            member = ctx.message.author
        await self.bot.say(
            "```xl\n" +
            "Name: {0.name}\n".format(member) +
            "Joined server: {0.joined_at}\n".format(member) +
            "ID: {0.id}\n".format(member) +
            "Has existed since: {0.created_at}\n".format(member) +
            "Bot?: {0.bot}\n".format(member) +
            "```" +
            "\n{0.avatar_url}".format(member))
        print("Run: info on {0.name}".format(member))

    # Server Info
    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        """Basic info on the server."""
        server = ctx.message.server
        afk = server.afk_timeout / 60
        await self.bot.say(
            "```xl\n" +
            "Name: {0.name}\n".format(server) +
            "Server ID: {0.id}\n".format(server) +
            "Region: {0.region}\n".format(server) +
            "Existed since: {0.created_at}\n".format(server) +
            "Owner: {0.owner}\n".format(server) +
            "AFK Timeout and Channel: {0} minutes in '{1.afk_channel}'\n".format(afk, server) +
            "Member Count: {0.member_count}\n".format(server) +
            "```")
        print("Run: Server Info")

def setup(bot):
    bot.add_cog(Moderation(bot))
