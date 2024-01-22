#!/usr/bin/python3

def raise_exception():
    raise TypeError("Exception raised")

# Test in 5-main.py
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

