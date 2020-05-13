# A variable is a container for a value, which can be of various types

"""
This is a
multi-line comment
or docstring (used to define a functions purpose)
can be single or double quotes
"""

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x = 1               # int
# y = 2.5             # float
# name = 'John'       # string
# is_cool = True      # bool

# Multiple Assignment

x , y, name, is_cool = (1, 2.5, 'John', True)

# Displaying using print()

print('Hello')
print(x , y, name, is_cool)
print(2.55*78)

# Casting

print(type(x) , x)  # prints the original type of the variable x
x = str(x)          # converts the variable x to str type
print(type(x) , x)  # prints the current type of the variable x

print(type(y) , y)  # prints the original type of the variable y
y = int(y)          # converts the variable y to int type
print(type(y) , y)  # prints the current type of the variable y

print(type(y) , y)  # prints the original type of the variable y
y = float(y)        # converts the variable y to float type
print(type(y) , y)  # prints the current type of the variable y
