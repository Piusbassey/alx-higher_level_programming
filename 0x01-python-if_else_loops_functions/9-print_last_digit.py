#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10
    print(last_digit)

    print_last_digit(98)
    print_last_digit(0)
    print_last_digit(-1024)

    def get_last_digit(number):
        return number % 10
