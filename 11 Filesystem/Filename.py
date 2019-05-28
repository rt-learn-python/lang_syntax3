#!/usr/bin/env python3

import os


# 1. Get base name
from os.path import basename

# now you can call it directly with basename
print(basename("/a/b/c.txt"))
print(os.path.dirname("/a/b/c.txt"))
