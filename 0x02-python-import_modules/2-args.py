#!/usr/bin/python3
import sys

arguments = sys.argv

num_arguments = len(arguments) - 1

if num_arguments == 0:
    print("0 arguments.")
else:
    print(f"{num_arguments} argument{'s' if num_arguments != 1 else ''}:")
    argument_number = 1
    for argument in arguments[1:]:
        print(f"{argument_number}: {argument:}")
        argument_number += 1
