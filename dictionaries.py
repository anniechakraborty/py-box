# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# A dictionary uses a    key : value    pair format

# Creating a dictionary
person = {
    'first_name' : 'Annie',
    'last_name' : 'Chakraborty',
    'age' : 20,
    'alive' : True
}
print(person, type(person))

# Creating a dictionary using a constructor
human = dict(first_name='John', last_name='Doe', age=300, alive=False)
print(human, type(human))

# Accessing any element in a dictionary
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone_number'] = '222-777-4444'
print(person)

# Get all the dictionary keys
print(person.keys())

# Get all the dictionary items
print(human.items())

# Copying all the elements in a dictionary to another dictionary
copy_person = person.copy()
copy_person['city'] = 'Vancouver'

print('Person : \t', person, '\nCopy of person :\t', copy_person)
# Hence here the copy of person has all the details of person and the city of Vancouver.

# Remove an item from a dictionary
del (copy_person['city'])
# Removes the city key-value pair from  the copy_person dictionary

print('Copy_person : ', copy_person)

# Alternatively, to remove an item, we can use the pop()
copy_person.pop('age')
print('Copy_person : ', copy_person)

# To clear the entire dictionary without deleting it's existence,.i.e, to get an empty dictionary
copy_person.clear()

# To get the length of the dictionary
print(len(person))

# List of dict
people = [
    {
        'name' : 'Annie Chakraborty',
        'age' : 20,
    },
    {
        'name' : 'Fitzwilliam Darcy',
        'age' : 35,
    },
    {
        'name' : 'Elizabeth Bennett',
        'age' : 28,
    },
    {
        'name' : 'Jane Austen',
        'age' : 45,
    }
]
print('Displaying a list of dictionaries : ', people)

# To access any element such as 'Elizabeth Bennett' from the above list of dict, we do -
print(people[2]['name'])

