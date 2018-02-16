#!/usr/bin/python3


# 1. Initialize a string variable
text1a = 'Single Quotes'
print(text1a)
text1b = "Double Quotes"
print(text1b)


# 2. Multiline
text2 = '''Multi
Line'''
print('Multiline: ' + text2)


# 3. Long Line
text3 = 'the quick brown fox jumps over the lazy dog. ' \
        'The end.'
print('Very long line: ' + text3)


# 4. String concatenation
text4a = 'String' + ' ' + 'Concat+'
print(text4a)
text4b = 'String ' 'Concat next to each other'
print(text4b)


# 5. Split string
text5 = 'Split String'
print(text5.split(' ')[0])  # => 'Split'


# 6. Replace
text6 = "Replace earth"
print(text6.replace('earth', 'world'))  # => 'Replace world'


# 7. Remove trailing spaces.
text7 = 'Hello   \n'.rstrip()
print('[' + text7 + ']')  # => '[Hello]'


# 8. Remove specific trailing characters
text8 = 'Hello   \n'.rstrip('\n')
print('[' + text8 + ']')  # => '[Hello   ]'


# 9. Get first character
text9a = 'ABCDE'[0]
print(text9a)
text9b = '1234'[:1]
print(text9b)


# 10. Get last character
text10a = 'ABCDE'[-1]
print(text10a)
text10b = '1234'[-1:]
print(text10b)


# 11. Substring
text11a = 'Hakuna Matata'
print('Hakuna' in text11a)  # True
print('Pumba' not in text11a)  # True

# 12. Lowercase
text12 = 'Hakuna Matata'
print(text12.lower())

print('13. String length: {}'.format(len('Hakuna Matata')))
