#!/usr/bin/env python3.5


# This must be run in the commandline


def get_valid_letter():
    while True:
        letter = input('Please enter a letter: ')
        if letter.isdigit():
            print('That is a number!')
        elif len(str(letter)) > 1:
            print("Sorry, you have to enter exactly ONE letter")
        else:
            return letter


get_valid_letter()
