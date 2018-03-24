#!/usr/bin/env python3


# 1. for in dictionary

map = {'one': 1}

for k, v in map.items():
    print('{}={}'.format(k, v))


# Looping with index
for x in range(1, 3):
    print("We're on time %d" % (x))