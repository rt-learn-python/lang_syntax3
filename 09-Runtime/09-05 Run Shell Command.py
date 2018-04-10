#!/usr/bin/env python3

import subprocess
subprocess.call(["ls", "-l"])


# Capturing output
result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)

print(result.stdout)
# b'total 0\n-rw-r--r--  1 memyself  staff  0 Mar 14 11:04 files\n'

# The return value is a bytes object, so if you want a proper string, you'll
# need to decode it.  Assuming the called process returns a UTF-8-encoded
# string:

result.stdout.decode('utf-8')
