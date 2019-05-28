#!/usr/bin/env python3

# 1. Open a file with exception handling

try:
    open('non-existent.txt', 'r')
except FileNotFoundError as error:  # ignore anaconda lint warning here.
    print('This is printed')
