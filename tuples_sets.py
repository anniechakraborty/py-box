# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create a tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

fruits3 = ('Apples')
print(fruits3, type(fruits3))
# If a tuple has only one element we need to add a trailing comma after it otherwise it's not considered a tuple.
fruits3 = ('Apples',)
print(fruits3, type(fruits3))

# To get a value from a tuple we write -    tuple_name[index_of_the_value]      just like we do in lists

print(fruits[1])

# Since tuple values are unchangeable, we cannot reassign them like we did in lists
# ( tuple_name[index] = new_value    is not supported)

# Completely deleting a tuple
del fruits3

# To get the length of a tuple -
print(len(fruits))

# A Set is a collection which is unordered and un-indexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mangoes'}

# Check if in set
print('Apples' in fruits_set)

# Add an element to set (appends)
fruits_set.add('Grapes')

# Remove an element from set
fruits_set.remove('Grapes')

# Adding a duplicate element
fruits_set.add('Apples')
print(fruits_set)

# Clear the entire set (means we are left with an empty set, clear() only clears all the elements of the set)
fruits_set.clear()

# Deleting the set (totally removing the set from definition)
del fruits_set
