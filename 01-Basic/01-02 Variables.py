#!/usr/bin/env python3.5


# 1. Initialize a single variable.
var1 = 1
print(var1)


# 2. Initialize multiple variables.
var2, varb = 1, 'b'
print(var2, varb)


# 3. Initialize multiple variables with the same value.
var3a = var3b = var3c = 0
print(var3a, var3b, var3c)


# 4. Initialize a variable with null reference
var4 = None
print(var4)


# 5. De-initialize a variable
var5 = 1
del var5
try:
    print(var5)
except NameError as err:
    print(err)  # This line well be executed.


# 6. Get expression data type
print(type({}))
