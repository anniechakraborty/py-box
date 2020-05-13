# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create a function


def say_hello(name) :
    print('Hello {name}'.format(name=name))


say_hello('Jane Doe')


# Creating a function whose parameter has a default value -


def say_helloy(name='Sally') :
    print('Hello {name}'.format(name=name))


say_helloy()


# Return values


def getSum(num1, num2) :
    total = num1 + num2
    return total


print(getSum(299, 67))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getDiff = lambda num1, num2 : num1 - num2

print(getDiff(16, 3))
