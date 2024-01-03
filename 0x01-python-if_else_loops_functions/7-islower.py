#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')

char_input = 'a'
result = islower(char_input)
print(result)
