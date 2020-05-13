# If/ Else conditions are used to decide to do something based on something being true or false

x = 201
y = 205

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple IF

if x > y :
    print('{} is greater than {}'.format(x, y))

# If - else

if x > y :
    print('{} is greater than {}'.format(x, y))
else :
    print('{} is greater than {}'.format(y, x))

# elif

if x > y :
    print('{} is greater than {}'.format(x, y))
elif x == y :
    print('{} is equal to {}'.format(x, y))
else :
    print('{} is greater than {}'.format(y, x))

# We also have nested if-elif-else similar rto other programming languages

# Logical operators (and, or, not) - Used to combine conditional statements

if (x % 2 == 0) and x <= 20 :
    print('{} is even and greater or equal to 20'.format(x))
elif (x % 2 == 0) or x <= 10 :
    print(x ** 4)
elif not (x == y) :
    print('{} is not equal to {}'.format(x, y))
else :
    print(y / x)

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

x = 4

numbers = [1, 2, 3, 4, 5]
print('The numbers list : {}'.format(numbers))
print('x = {}'.format(x))
#  in
if x in numbers :
    print('x in numbers : ', x in numbers)

# not in
if x not in numbers :
    print('x not in numbers : ', x not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

x = 104
y = 100

print('x = {} and y = {}'.format(x, y))

# is
if x is y :
    print('x is y = ', x is y)

# is not
if x is not y :
    print('x is not y : ', x is y)
