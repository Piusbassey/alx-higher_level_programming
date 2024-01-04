#!/usr/bin/python3
def uppercase(str):
    for char in str;

    uppercase_char = chr(ord('a') - 32) if 97 <= ord('z') <= 122 else char
    print(uppercase_char, end="")
    print()

uppercase("best")
uppercase("Best School 98 Battery street")
