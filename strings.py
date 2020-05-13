# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Annie Chakraborty'
age = 20

# Concatenate
print('Hello, my name is ' + name + ' and I\'m ' + str(age) + ' years old.')
# We type casted the age variable into a string variable as we can concatenate only strings.

# String Formatting

# -  Arguments by position

print('Hello, my name is {name} and I\'m {age} years old.'.format(name=name, age=age))

# - Using F-Strings (available only on Python v3.6 onwards)

# print(f'Hello, my name is {name} and I\'m {age} years old.')
# Since this is v3.5 it doesn't support F Strings

# String Methods

s = "hello world"

# Capitalise
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())
# The split() splits all the words in the string and puts them in a list (like an array)

# Find position
print(s.find('r'))
# The find() looks for the first position of the given character in the string

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

# There are a lot of other methods as well, these are just some examples
