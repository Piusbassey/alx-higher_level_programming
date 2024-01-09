#!/usr/bin/python3
import sys

arguments = sys.argv

num_arguments = len(arguments)

if num_arguments == 0:
    print("0 arguments.")
else:
    print(f"{num_arguments} argument{'s' if num_arguments != 1 else ''}:")
    for argument in arguments[1:]:
        print(f"1: {argument}")
