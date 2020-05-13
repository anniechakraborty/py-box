# A List is a collection which is ordered and changeable. Allows duplicate members.

# Creating a list -

# (i) Through static initialisation
numbers = [1, 2, 3, 4, 5]

# (ii) Using Constructor
numbers2 = list((1, 2, 3, 3, 4, 5, 6))

print(numbers, numbers2)

fruits = ['Apples', 'Mangoes', 'Bananas', 'Oranges', 'Grapes', 'Pears']

print('The fruits array : ' + str(fruits))
print('The fourth element of the above array is : ' + fruits[3])
print('Length of the fruits array is = {len}'.format(len=len(fruits)))

# Appending to a list

print('Appending to the grapes list : ')
fruits.append('Tomatoes')
print('The fruits array : ' + str(fruits))

# Removing elements from the list (using their value)

print('Removing from the grapes list : ')
fruits.remove('Grapes')
print('The fruits array : ' + str(fruits))

# Inserting elements in any given position

print('Inserting \'Strawberries\' in the third position of the list : ')
fruits.insert(2, 'Strawberries')
print('The fruits array : ' + str(fruits))

# Removing elements from the list (using their position)

print('Removing the second element from the grapes list : ')
fruits.pop(1)
print('The fruits array : ' + str(fruits))

# Reverse the list

print('Reversing the fruits array : ')
fruits.reverse()
print('The fruits array : ' + str(fruits))

# Sort the list

print('Sorting the fruits array : ')
fruits.sort()
print('The fruits array : ' + str(fruits))

# Reverse sort the list

print('Sorting the fruits array in reverse order : ')
fruits.sort(reverse=True)
print('The fruits array : ' + str(fruits))

# If we want to change the value in any given position then we simply reassign it -
# list_name[position_storing_the_new_value] = new_value
