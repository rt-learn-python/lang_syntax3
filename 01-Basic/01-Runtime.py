#!/usr/bin/env python3.5

# 1. print script version engine
import sys
print(sys.version)

# 2. Reading environment variables.
import os
print(os.environ['RUBY_VERSION'])
print(os.environ.get('HOME'))

# 99. Terminate a script
import sys
sys.exit()
print('This is not executed')
