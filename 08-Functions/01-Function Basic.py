#!/usr/bin/env python3.5


# 1. Manipulating global variable.
glob = 0


def func1():
    global glob
    glob = 1
    print('inside 1: {}'.format(glob))


def func2():
    glob = 2
    print('inside 2: {}'.format(glob))


print(glob)
func1()
func2()
print(glob)


# 2. Computing experience points gained
def compute(your_level, target_level):
    return max(10 - (your_level - target_level), 1)


template = '2. Compute Level ({}, {}): {}'
your_level = 1
target_level = 1
print(
    template.format(
        your_level, target_level, compute(your_level, target_level)))

your_level = 1
target_level = 2
print(
    template.format(
        your_level, target_level, compute(your_level, target_level)))

your_level = 10
target_level = 1
print(
    template.format(
        your_level, target_level, compute(your_level, target_level)))

your_level = 15
target_level = 1
print(
    template.format(
        your_level, target_level, compute(your_level, target_level)))

your_level = 15
target_level = 4
print(
    template.format(
        your_level, target_level, compute(your_level, target_level)))

your_level = 15
target_level = 7
print(
    template.format(
        your_level, target_level, compute(your_level, target_level)))



