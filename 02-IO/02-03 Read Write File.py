#!/usr/bin/env python3.5


# 1. Read file contents
print('Case 1 ----------------------')
with open('file1.txt', 'r') as file1:
    for line in file1:
        print(line.rstrip())


# 2. Read file contents
print('Case 2 ----------------------')
file2 = open('file2.txt', 'r')
for line in file2:
    print(line.rstrip())
file2.close()


# 3. Open two files simultaneously.
print('\nCase 3 =====================')
with open('file1.txt', 'r') as file3a, \
        open('file2.txt', 'r') as file3b:
    print('File 1 ----------------------')
    for line in file3a:
        print(line.rstrip())
    print('File 2 ----------------------')
    for line in file3b:
        print(line.rstrip())


# 4. Read file contents as a string.  Note that big files consume a lot of
# memory.
print('\nCase 4 ----------------------')
with open('file2.txt', 'r') as f:
    print(f.read())


# 5. Read file contents as a string.  Note that big files consume a lot of
# memory.
print('\nCase 5 ----------------------')
with open('file2.txt', 'r') as f:
    print(f.readlines())


# 6. Read file contents line by line.
print('\nCase 6 ----------------------')
with open('file2.txt', 'r') as f:
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline().strip())
    print(f.readline().strip())  # Reads empty string
    print(f.readline().strip())  # Reads empty string


print('7. Read file contents to a list')
with open('file2.txt', 'r') as f:
    lines = [line.strip() for line in f]
    print(lines)


print('8. Append to file')
with open("test.txt", "a") as myfile:
    myfile.write("appended text")
