"""
Converts text to discord emoji.
Output is sent to output.txt in the current working directory.

I made this instead of working on my college apps, less than 24 hours before the deadline. Lol.
"""

import random
import modules.emoji.emojis as emojis

def emojify(string: str):
    words = string.split(' ')
    output = str()
    for n in range(len(words)):
        
        # To-do: Implement pinging (@/#) that works with names that have spaces in them.
        # Initially had (words[n][0] == "$") predicate 
        if words[n] in emojis.phrase_list:
            if type(emojis.phrase_list[words[n]]) == type(lambda:0): 
                output += emojis.phrase_list[words[n]]()
            elif type(emojis.phrase_list[words[n]]) == type([]):
                output += random.choice(emojis.phrase_list[words[n]])
            else:
                output += emojis.phrase_list[words[n]]
            continue
        
        
        words[n] = list(words[n])
        
        for m in range(len(words[n])):
            char = words[n][m] #Yes, it's super ugly and confusing, but I needed to do it this way
        
            """ 
            Replaces special characters ('!', '?', etc.) with their respective emojis.
            If there is more than one emoji per character, it randomly chooses between the two.
            """
            
            if char in emojis.special_chars:
                if type(emojis.special_chars[char]) == type([]):
                    output += random.choice(emojis.special_chars[char])
                else:
                    output += emojis.special_chars[char]
            elif char.isdigit():
                output += "\u034F:{}:".format(emojis.numbers[str(char)])
            elif char.isalpha():
                output += "\u034F:regional_indicator_{}:".format(char.lower())
            else:
                output += "\u034F**{}**".format(char)
        
        #Adds spaces between words
        if not words[n] == words[~0]:
            output += emojis.special_chars[' ']
    
    return output