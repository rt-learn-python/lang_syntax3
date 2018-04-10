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
text3 = 'productCodes.3900(), "tiny",'
replaced3 = re.sub(r'\.\d+\(\)', text3, '.{}()'.format('hug'))
print(replaced3)


# 4. Check match
pattern4 = re.compile("^([A-Z][0-9]+)+$")
pattern4.match('string')
