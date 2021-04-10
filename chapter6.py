# Chapter 6
# A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary.
alien_0 = {'color': 'green', 'points': 5}  # a dictionary is wrapped in braces, {}

# A key-value pair is a set of values associated with each other. Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.

# Accessing Values in a Dictionary
# When you provide a key, Python returns the value associated with that key.
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding New Key-Value Pairs
# Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time.
print(alien_0)  # {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)  # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
# Python doesn’t care about the order in which you store each key-value pair; it cares only about the connection between each key and its value.

# Starting with an Empty Dictionary
# Typically, you’ll use empty dictionaries when storing user-supplied data in a dictionary or when you write code that generates a large number of key-value pairs automatically.
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# Removing Key-Value Pairs
# When you no longer need a piece of information that’s stored in a diction- ary, you can use the del statement to completely remove a key-value pair.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
# The deleted key-value pair is removed permanently.

# A Dictionary of Similar Objects
# You can also use a dictionary to store one kind of information about many objects.
favorite_languages = {  # a way to format long dictionaries
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")

# Exercise 6-1
print("Exercise 6-1---------------------------")
amigo = {'first_name': 'Vitaly', 'last_name': 'Didkivsky', 'age': 19, 'city': 'Florence'}
print(f"my friend's first name is : {amigo['first_name']}")
print(f"my friend's last name is : {amigo['last_name']}")
print(f"my friend is : {amigo['age']} years old")
print(f"my friend lives in : {amigo['city']}")

# Exercise 6-2
fnumbers = {'jane': 5, 'tom': 11, 'john': 25, 'sarah': 5, 'jack': 44}
print(fnumbers['jane'])
print(fnumbers['john'])
print(fnumbers['sarah'])

# Exercise 6-3
glossary = {
    'list': 'a collection of items in a particular order',
    'loop': 'a process of iterating, going through the elements',
    'tuple': 'a data structure similar to a list but which cannot be modified',
    'immutable': 'unchangeable, unmodifiable',
    'slice': 'a specific group of items in a list'
}
print(f"List \n\t{glossary['list']}\n")
print(f"Loop \n\t{glossary['loop']}\n")
print(f"Tuple \n\t{glossary['tuple']}\n")
print(f"Immutable \n\t{glossary['immutable']}\n")
print(f"Slice \n\t{glossary['slice']}\n")

# Looping through a dictionary
# Looping Through All Key-Value Pairs
print("----------Looping Through All Key-Value Pairs----------")
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi', }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
# To write a for loop for a dictionary, you create names for the two variables that will hold the key and value in each key-value pair. You can choose any names you want for these two variables.
# items() method returns a list of key-value pairs
# Python doesn’t care about the order in which key-value pairs are stored; it tracks only the connections between individual keys and their values.
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping Through All the Keys in a Dictionary
print("------Looping Through All the Keys in a Dictionary------")
# keys() method is useful when you don’t need to work with all of the values in a dictionary. The keys() method isn’t just for looping: It actually returns a list of all the keys. You can omit key() bcz it is default behavior of looping through the dictionary
for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(
        name.title())  # Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(f"Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping Through a Dictionary’s Keys in Order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
# sorted(favorite_languages.keys()) tells Python to list all keys in the dictionary and sort that list before looping through it.

# Looping Through All Values in a Dictionary
# values() method returns a list of values without any keys.
print("------Looping Through All Values in a Dictionary------")
for language in favorite_languages.values():
    print(language.title())

# When you wrap set() around a list that contains duplicate items, Python identifies the unique items in the list and builds a set from those items. We use set() to pull out the unique, nonrepetitive values.
for language in set(favorite_languages.values()):
    print(language.title())

print("-------------------Exercises------------------")
# Exercise 6-4
glossary = {
    'list': 'a collection of items in a particular order',
    'loop': 'a process of iterating, going through the elements',
    'tuple': 'a data structure similar to a list but which cannot be modified',
    'immutable': 'unchangeable, unmodifiable',
    'slice': 'a specific group of items in a list'
}

glossary['dictionary'] = 'a collection of key-value pairs'
glossary['key-value pair'] = 'a set of values associated with each other where each key is connected to a certain value'
glossary['boolean value'] = 'is either True or False'
glossary['list comprehension'] = 'allows to generate the same list in just one line of code'
glossary['indentation error'] = 'an error that occurs when there extra or lack of indents on blocks of code'
print(glossary)

for key, value in sorted(glossary.items()):
    print(key.title())
    print("\t\t" + value + "\n")

# Exercise 6-5
rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for river in rivers:
    print(river.title())
for country in rivers.values():
    print(country.title())

# Exercise 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
poll = ['sarah', 'jack', 'jen', 'tom']
for name in sorted(poll):
    if name in favorite_languages:
        print(f"{name.title()}, thank you for responding.")
    else:
        print(f"{name.title()}, you should definitely take the poll!")

print("--------------------nesting------------------------")
# Nesting
# is storing set of dictionaries in a list or a list of items as a value in a dictionary, or even a dictionary inside another dictionary.

# A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# In the following example we use range() to create a fleet of 30 aliens:
aliens = []  # Make an empty list for storing aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# to change the first three aliens to yellow, medium-speed aliens worth 10 points each:
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien[
        'color'] == 'yellow':  # You could expand this loop by adding an elif block that turns yellow aliens into red, fast-moving ones worth 15 points each.
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:  # Show the first 5 aliens
    print(alien)
print("Total number of aliens: " + str(len(aliens)))  # Show how many aliens have been created

print("-------------------------------------")
# A List in a Dictionary
# You can nest a list inside a dictionary any time you want more than one value to be associated with a single key in a dictionary.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}""-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

# A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

print("--------------------------------------")
# Exercise 6-7
amigo1 = {'first_name': 'Victor', 'last_name': 'Krum', 'age': 25, 'city': 'Chicago'}
amigo2 = {'first_name': 'Linda', 'last_name': 'Brian', 'age': 50, 'city': 'New York'}
amigo3 = {'first_name': 'Nicole', 'last_name': 'Johnson', 'age': 30, 'city': 'Pittsburgh'}

people = [amigo1, amigo2, amigo3]
for amigo in people:
    print(amigo['first_name'], end=' || ')
    print(amigo['last_name'], end=' || ')
    print(amigo['age'], end=' || ')
    print(amigo['city'])

people = [amigo1, amigo2, amigo3]
for amigo in people:
    for key, value in amigo.items():
        print(f"{key}: {value}")

# Exercise 6-8
bob = {'animal': 'dog', 'owner': 'linda'}
stacy = {'animal': 'cat', 'owner': 'victor'}
ebony = {'animal': 'snake', 'owner': 'nicole'}
fluffy = {'animal': 'hamster', 'owner': 'john'}
pets = [bob, stacy, ebony, fluffy]

for pet in pets:
    for animal, owner in pet.items():
        print(f"{animal}: {owner}")

pets = {
    'bob': {'animal': 'dog', 'owner': 'linda'},
    'stacy': {'animal': 'cat', 'owner': 'victor'},
    'ebony': {'animal': 'snake', 'owner': 'nicole'},
    'fluffy': {'animal': 'hamster', 'owner': 'john'}
}

for pet, details in pets.items():
    print(pet.title())
    for key, value in details.items():
        print(f"{key}: {value}")

# Exercise 6-9
favorite_places = {
    'victor': ['moscow', 'miami', 'paris'],
    'linda': ['tokyo', 'new york', 'oranjestad'],
    'nicole': ['sarasota', 'paris', 'barcelona']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(place.title(), end=' | ')

# Exercise 6-10
favorite_numbers = {
    'jane': [5, 10, 99],
    'tom': [11, 14, 54],
    'john': [25, 10, 1],
    'sarah': [5, 50, 100],
    'jack': [44, 2, 18]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers:")
    for num in numbers:
        print(num, end="\t\t")

# Exercise 6-11
cities = {
    'tashkent': {'country': 'uzbekistan', 'population': '2.5 mln', 'fact': 'largest city in Central Asia'},
    'new york': {'country': 'usa', 'population': '8.5 mln', 'fact': 'more than 800 languages are spoken'},
    'tokyo': {'country': 'japan', 'population': '37 mln', 'fact': 'the most populated city in the world'}
}

for city, details in cities.items():
    print("\n" + city.upper() + ":")
    for key, value in details.items():
        print(f"\t{key.title()}:", end='\t')
        print("\t" + value.title())

# Exercise 6-12
cities = {
    'tashkent': {'country': 'uzbekistan', 'population': '2.5 mln', 'established': '2200 years ago',
                 'fact': 'largest city in Central Asia'},
    'new york': {'country': 'usa', 'population': '8.5 mln', 'established': '1624 year',
                 'fact': 'more than 800 languages are spoken'},
    'tokyo': {'country': 'japan', 'population': '37 mln', 'established': '1603 year',
              'fact': 'the most populated city in the world'}
}
for city, details in cities.items():
    print("\n" + city.upper() + ":")
    for key, value in details.items():
        print(f"\t{key.title()}:", end='\t')
        print(value.title())
