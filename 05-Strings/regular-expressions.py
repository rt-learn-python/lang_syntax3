#!/usr/bin/python3
import re

print('1. Initialize')
regex = r'test'
print(regex)


print('2. Find String occurence')
text = 'productCodes.3900(), "tiny",'
matcher = re.search(r'\d+', text)
print(matcher.group())


# 3. Replace with dynamic string.
replaced = re.sub(r'\.\d+\(\)', text, '.{}()'.format('hug'))


print(replaced)
