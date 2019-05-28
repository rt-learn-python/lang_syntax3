#!/usr/bin/python3
import re

print('1. Initialize')
regex = r'test'
print(regex)


print('2. Find String occurence')
text = 'productCodes.3900()400, "tiny",'
matcher21 = re.search(r'(\d+)', text)
print(matcher21.group(1))


print('3. Replace')
text3 = 'productCodes.3900(), "tiny",'
p = re.compile(r'\.\d+\(\)')
replaced3 = p.sub('.hug()', text3)
print(replaced3)


# 4. Check match
pattern4 = re.compile("^([A-Z][0-9]+)+$")
pattern4.match('string')
