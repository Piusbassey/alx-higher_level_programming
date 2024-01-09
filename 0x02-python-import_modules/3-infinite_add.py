#!/usr/bin/python3
import sys

arguments = sys.argv[1:]

total = sum(int(arg) for arg in arguments)

print(total)

if __import__ == "__main__":
    arguments = sys.argv[1:]
    add_arguments(*arguments)
