import discord
from discord.ext import commands
from modules.color.embedding import embeds, embed
from modules.text.format import *
from configparser import SafeConfigParser
import os


config = SafeConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname( __file__ )), '..', 'config.ini'))
prefix = config.get('main', 'prefix')



class Help():
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def halp(self, cmd = '', attr = ''):
        global cmds
        global em
        if not cmd:
            cmdlist = [command for command in cmds]
            formatted = ['`{}`'.format(cmd) for cmd in cmdlist[:~1]]
            message = ''.join([
                '{} and {}.'.format(', '.join(formatted), '`{}`'.format(cmdlist[~0])),
                'Type `{}halp command` for more info about a specific commands.'.format(prefix),
                ])
            await self.bot.say(embed=embed(value=message, **embeds['halp']['main']))
            return 0

        if not cmd in cmds:
            message = 'Command `{}` not found.'
            await self.bot.say(embed=embed(value=message, **embeds['halp']['info']))
            return 0

        if attr and camel(attr) not in cmds[cmd]:
            message = '{} not an attribute of `{}`'.format(camel(attr), cmd)
            await self.bot.say(embed=embed(value=message, **embeds['halp']['info']))
            return 0

        if attr:
            message = '**__{}__**: {}'.format(camel(attr), cmds[cmd][camel(attr)])
            await self.bot.say(embed=embed(value=message, **embeds['halp']['info']))
            return 0

        usage = '**__Usage:__** {}'.format(cmds[cmd]['Usage'])
        info = '**__Info:__** {}'.format(cmds[cmd]['Info'])
        message = '\n'.join([usage, info])
        await self.bot.say(embed=embed(value=message, **embeds['halp']['info']))



def setup(bot):
    bot.add_cog(Help(bot))


cmds = {
    'halp' : {
        'Usage' : '`{}help [command]`'.format(prefix),
        'Info'  : 'Displays all commands, and displays information about specific commands',
        },

    'reload' : {
        'Usage' : '`{}reload`'.format(prefix),
        'Info'  : 'Reloads the bot.',
        },

    'say'   : {
        'Usage' : '`{}say message`'.format(prefix),
        'Info'  : 'Has the bot say a message.',
        },

    'solve' : {
        'Usage' : '`{}solve [x=]y`'.format(prefix),
        'Info'  : 'Solves an equation in the form of `x = y`, as long as the limit as x approaches infinity for `y` is less than that of `ln(x)`.'
        },

    'avatar': {
        'Usage' : '`{}avatar user`'.format(prefix),
        'Info'  : "Posts a link to a user's avatar.",
        },

    'ping'  : {
        'Usage' : '`{}ping`'.format(prefix),
        'Info'  : 'pong.',
        },

    'xkcd'  : {
        'Usage' : '`{}xkcd [comic # | search term]`'.format(prefix),
        'Info'  : 'Finds an xkcd comic by number or search term, and then displays it in chat. Can also invoke the command without arguments to display the most recent xkcd.',
        },

    'aes'   : {
        'Usage' : '`{}aes message`'.format(prefix),
        'Info'  : 'Makes a message aesthetic.',
        },

    'bb'   : {
        'Usage' : '`{}bb message`'.format(prefix),
        'Info'  : 'Makes a message Blackboard font.',
        },

    'e' : {
        'Usage' : '`{}e message'.format(prefix),
        'Info'  : 'Converts the message to emoji. `/r for a random emoji, `/heart` for a random heart, and `/face` for a random face.',
    },

    'shrug' : {
        'Usage' : '`{}shrug message`'.format(prefix),
        'Info'  : 'Appends the shrugging emoticon to the end of a message.',
    },

    'all' : {
        'Usage' : '`{}all message`'.format(prefix),
        'Info'  : 'Displays the message in italics, bold, and underlined.',
    },

    'purge' : {
        'Usage' : '`{}_ n`'.format(prefix),
        'Info'  : 'Deletes the last `n` messages.',
    },

    'em' : {
        'Usage' : '`{}em color message`'.format(prefix),
        'Info'  : 'Embeds a message with a given color.',
    },

    'de' : {
        'Usage' : '`{}de message`'.format(prefix),
        'Info'  : 'Embeds a message with the default color.',
    },

    'py' : {
        'Usage' : '`{}py code`'.format(prefix),
        'Info'  : 'Evaluates Python code and then sends a message containing the value returned.',
    },

    'status' : {
        'Usage' : '`{}status status`'.format(prefix),
        'Info'  : 'Changes the user\'s status.',
    },

    'rect' : {
        'Usage' : '`{}rect width height [outer_emoji] [inner_emoji]`'.format(prefix),
        'Info'  : 'Creates a rectangle of dimensions `width`x`height`. The outer_emoji and inner_emoji are :black_large_square: and :white_large_square: by default.',
    },

    're' : {
        'Usage' : '`{}re n [caps?]`'.format(prefix),
        'Info'  : 'REEEs with `n` number of \'E\'s. Caps is True by default.',
    },

    'hi' : {
        'Usage' : '`{}hi`'.format(prefix),
        'Info'  : 'Says hi',
    },

    'sd' : {
        'Usage' : '`{}sd t message`'.format(prefix),
        'Info'  : 'Puts out a message that self destructs in `t` seconds. `t` must be an integer.',
    },

    'hug' : {
        'Usage' : '`{}hug [user1] [user2] ...`'.format(prefix),
        'Info'  : 'Hugs each user.',
    },

    'mathf' : {
        'Usage' : '`{}mathf message`. Sample message: W = N{{dot}}m'.format(prefix),
        'Info'  : 'Formats a message with mathematical symbols. ',
    },

    'midge' : {
        'Usage' : '`{}midge n`'.format(prefix),
        'Info'  : '<:midge:286338835435225090>',
    },

    'read' : {
        'Usage' : '`{}read file`'.format(prefix),
        'Info'  : 'Reads a file in the temp folder. Breaks the file up into multiple messages if the file has over 2000 characters.',
    },

    'pingu' : {
        'Usage' : '`{}pingu`'.format(prefix),
        'Info'  : 'pongu',
    },
 
    'deepfry' : {
        'Usage' : '`{}deepfry message`'.format(prefix),
        'Info'  : 'Deep fries a message. Re\🅱laces consonants with \🅱.',
    },
   
    'deeepfry' : {
        'Usage' : '`{}deeepfry 🅱e🅱🅱a🅱e`'.format(prefix),
        'Info'  : '\🅱ee\🅱e\🅱 \🅱\🅱ie\🅱 a \🅱e\🅱\🅱a\🅱e. \🅱e\🅱\🅱a\🅱e\🅱 \🅱o\🅱\🅱o\🅱a\🅱\🅱\🅱 \🅱i\🅱h \🅱',
    },

    'ssd' : {
        'Usage' : '`{}ssd t message`'.format(prefix),
        'Info'  : 'Sends a message that silently self destructs in `t` seconds.',
    },

    'quote' : {
        'Usage' : '`{}quote message_id [server_id]`'.format(prefix),
        'Info'  : 'Quotes a message with id `message_id` in server `server_id`. By default, the server is the one the command is executed in.',
    },

    'upvote' : {
        'Usage' : '`{}upvote [message_id]`'.format(prefix),
        'Info'  : 'Upvotes the message `message_id`. Defaults to the most recent message.',
    },

    'downvote' : {
        'Usage' : '`{}downvote [message_id]`'.format(prefix),
        'Info'  : 'Upvotes the message `message_id`. Defaults to the most recent message.',
    },
}


blank = {
    '' : {
        'Usage' : '`{}`'.format(prefix),
        'Info'  : '',
    },
}
