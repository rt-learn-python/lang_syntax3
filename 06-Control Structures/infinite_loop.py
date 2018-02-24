#!/usr/bin/env python3


import sys

# 1. Infinite loop
while True:
    # a = input('Enter "q" to exit this infinite loop: ')
    a = 'q'
    print('You typed [{}]'.format(a))
    if a == 'q':
        sys.exit()
