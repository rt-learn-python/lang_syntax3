# Split string
text = 'Hello World'
print(text.split(' ')[0])  # => 'Hello'

# replace
print(text.replace('World', 'Earth'))  # => 'Hello'

# replace
print('Hello   \n'.rstrip())  # => 'Hello'

# remove ending newline only
print('Hello   \n'.rstrip('/n'))  # => 'Hello   '
