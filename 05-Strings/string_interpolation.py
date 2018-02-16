print('1. Basic interpolation.')
print("You got {} points".format(99))


# Print the number 1 with guaranteed 4 spaces.
print("Padded number [{:4d}]".format(1))


# Print 'abc' with guaranteed 5 spaces.
print('Padded string [{:5s}]'.format('abc'))


# Print abc with guaranteed 5 spaces, right aligned.
print('Padded string, right aligned [{:>5s}]'.format('abc'))

# Print the number 1 with guaranteed 4 spaces, left aligned.
print("Padded number, left aligned [{:<4d}]".format(1))

print('Number: {:d}'.format(1))
print('Number: {:.2f}'.format(1))
print('Number: {}'.format(1))


print('\nIndexed interpolation')
print('{0} {1}'.format('Hello', 'World'))


# substring
input = 'abcdef'
print(input[1:len(input) - 1])


# ends_with
input = 'abcdef'
print(input[-3:])
