import discord
from configparser import SafeConfigParser
import os


config = SafeConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname( __file__ )), '..', '..', 'config.ini'))


colors = {
    'default'   : eval('0x{}'.format(config.get('main', 'default_color'))),
    'red'       : discord.Colour.red(),
    'green'     : discord.Colour.green(),
    'yellow'    : 0xFFFF00,
    'light_grey': discord.Colour.light_grey(),
    'lighter_grey'  : discord.Colour.lighter_grey(),
    'magenta'   : discord.Colour.magenta(),
    'orange'    : discord.Colour.orange(),
    'purple'    : discord.Colour.purple(),
    'teal'      : discord.Colour.teal(),
    'gold'      : discord.Colour.gold(),
    'darker_grey'   : discord.Colour.darker_grey(),
    'dark_teal' : discord.Colour.dark_teal(),
    'dark_red'  : discord.Colour.dark_red(),
    'dark_purple'   : discord.Colour.dark_purple(),
    'dark_orange'   : discord.Colour.dark_orange(),
    'dark_magenta'  : discord.Colour.dark_magenta(),
    'dark_grey' : discord.Colour.dark_grey(),
    'dark_green': discord.Colour.dark_green(),
    'dark_gold' : discord.Colour.dark_gold(),
    'dark_blue' : discord.Colour.dark_blue(),
    'blue'      : discord.Colour.blue(),
    'black'     : 0x000000,
    'white'     : 0xFFFFFF,
    'brown'     : 0x795548,
    'sus_green' : 0x1f8b4c,
}

for color, code in config.items('custom_colors'):
    colors.update({color : code})