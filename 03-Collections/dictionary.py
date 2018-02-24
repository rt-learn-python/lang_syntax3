#!/usr/bin/env python3.5


map1 = {}
print('1. Initialize Empty hash: {}'.format(map1))

map2 = {1: 'a', 2: 'b'}
print('2. Initialize Map with values: {}'.format(map2))


print('3. Print values of a map')
for k, v in {1: 'a', 2: 'b'}.items():
    print('{} = {}'.format(k, v))


# 3. Clear contents
hsh3 = {'1': 1}
hsh3.clear()
print('3. Clearing hash contents: {}'.format(hsh3))

# 4. Retrieving map contents:
hsh4 = {'1': 1}
print('4. Retrieving existing content: {}'.format(hsh4['1']))

# 5. Retrieving map contents:
hsh5 = {'1': 1}
print('5. Retrieving non-existing content: {}'.format(hsh4['2']))

