from modules.symbols import symbols

def mformat(string):
    global symbols
    return string.format(**symbols)