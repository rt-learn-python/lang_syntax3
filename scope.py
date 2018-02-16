#!/usr/bin/env python3.5


def five():
    global num  # declare to be able to use the global scoped num.
    num += 5


def four():
    num = 0
    num += 5
    print(num)


def main():
    global num  # declare to be able to use the global scoped num.
    num = 1
    four()
    five()
    print(num)


num = 0  # this is globally scoped
main()
print(num)
print("Hello")
