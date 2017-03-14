import discord
from .color import colors


def embed(description='\u034f', colour=colors['default'], url=None, title=None, name='\u034f', value=None, inline=True):
    data = discord.Embed(url=url, title=title, description=description, colour=colour)
    data.add_field(name=name, value=value)
    #data.set_author(name='Author', icon_url='Image URL to set as the thumbnail for the embed here')
    return data


embeds = {
    'help' : {
        'main' : {
            'description'   : 'Help menu',
            'colour'        : colors['default'],
            'name'          : 'Available Commands:',
            'inline'        : True,
        },

        'info' : {
            'description'   : 'Help menu',
            'colour'        : colors['default'],
            'name'          : 'Command Info',
            'inline'        : True,
        },

        'new' : {
            'description'   : 'Help menu',
            'colour'        : colors['default'],
            'name'          : 'New commands:',
            'inline'        : True,
        },
    },

    'xkcd' : {
        'error' : {
            'colour'        : colors['default'],
            'value'         : '\u034F',
            'inline'        : True,
        },

        'info' : {
            'colour'        : colors['default'],
            'inline'        : True,
        },
    },
}