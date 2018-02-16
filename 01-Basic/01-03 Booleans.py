#!/usr/bin/env python3.5

# 1. To convert an expression to boolean, use the bool function.
print(bool(123))  # True


# 2. Truthy values.

# 2.1 non-zero is true
print(bool(1), bool(0))


# 2.2 non empty string is true
print(bool(' '), bool(''))


# 2.3 True literal is true
print(bool(True), bool(False))


# 2.4 non-empty collection is True
print(bool([1, 2]), bool([]))
