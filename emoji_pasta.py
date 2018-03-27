#!/usr/local/bin/python3
from random import randrange

emoji = ['😂', '👌', '🍕', '🎉', '🎈', '💯', '🔥']
emoji_n = len(emoji)

text = input()
words = text.split(' ')

out = str()
for x in words:
    index = randrange(emoji_n)
    out = out + x + ' ' + emoji[index] + ' '

print(out)
