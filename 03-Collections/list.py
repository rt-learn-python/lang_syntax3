#!/usr/bin/env python3.5

# 1. Initialize an empty list
lst1 = []
print(lst1)


# 2. Initiale a list with values
lst2 = [1, 2, 3]
print(lst2)


# 3. Check if list contains an element
lst3 = [1, 2, 3, 4]
print(3 in lst3)  # True


# 4. Convert an iterable into a list
range


# Get length of a list
print("Length of list: {}".format(len([1, 2, 3, 4])))


# Iterate 2 lists
lst1 = [1, 3, 5, 7, 9]
lst2 = [2, 4, 6, 8, 10]
for i, j in zip(lst1, lst2):
    print('{} {}'.format(i, j))


# 1. Sort a collection
sorted1 = sorted([1, 3, 10, 7, 9])
print(sorted1)


# 2. Sort a collection
sorted2 = [1, 3, 10, 7, 9]
sorted2.sort()
print(sorted2)


list3 = [1, 2, 3]
list3.append(4)
print('3. Add element to list: {}'.format(list3))

list4 = [1, 2, 3]
# Will throw error when item is not found.
print('4. Find elements in a list: {}'.format(
    [x for x in list4 if x == 2]))


# Find element, considering case where element don't exist.
list5 = [1, 2, 3]
try:
    found = list5.index(5)
except ValueError:
    found = False
print('5. Find elements in a list: {}'.format(found))
