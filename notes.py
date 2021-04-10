# Dictionary - java (HashMap, HashTable)

# A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary.
 # a dictionary is wrapped in braces, {}

# A key-value pair is a set of values associated with each other. Every key is connected to its value by a colon, and individual key-value pairs are separated by commas (key: value)

# Creating an Empty Dictionary
# Typically, you’ll use empty dictionaries when storing user-supplied data in a dictionary or when you write code that generates a large number of key-value pairs automatically.
my_friend = {}
my_house = dict()

# Accessing Values in a Dictionary
# When you provide a key, Python returns the value associated with that key.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Adding New Key-Value Pairs
# Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time.
print(alien_0)  # {'color': 'green', 'points': 5}
alien_0['speed'] = 'medium'
print(alien_0)  # {'color': 'green', 'points': 5, 'speed': 'medium'}

# Modifying Values in a Dictionary
alien_0 = {'color': 'green', 'points': 5, 'speed': 'medium'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Removing Key-Value Pairs
# When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement to completely remove a key-value pair.
alien_0 = {'color': 'yellow', 'points': 5, 'speed': 'medium'}
del alien_0['points']
print(alien_0)
# The deleted key-value pair is removed permanently.

# Looping through a dictionary ---------------------------
# 1. Looping Through All Key-Value Pairs
# To write a for loop for a dictionary, you create names for the two variables that will hold the key and value in each key-value pair. You can choose any names you want for these two variables.
# items() function returns a list of key-value pairs
# Python doesn’t care about the order in which key-value pairs are stored; it tracks only the connections between individual keys and their values.
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# 2. Looping Through All the Keys in a Dictionary
# keys() function is useful when you don’t need to work with all of the values in a dictionary. The keys() method isn’t just for looping: It actually returns a list of all the keys. You can omit key() bcz it is default behavior of looping through the dictionary.
for name in favorite_languages.keys():
    print(name.title())
# This code would have exactly the same output as the previous
for name in favorite_languages:
    print(name.title())

# 3. Looping Through All Values in a Dictionary
# values() function returns a list of values without any keys.
for language in favorite_languages.values():
    print(language.title())

# When you wrap set() around a list that contains duplicate items, Python identifies the unique items in the list and builds a set from those items. We use set() to pull out the unique, nonrepetitive values.
for language in set(favorite_languages.values()):
    print(language.title())

# Looping Through a Dictionary’s Keys or Value in Order
for name, language in sorted(favorite_languages.items()):
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in sorted(favorite_languages.keys()):  # sorts the key before looping
    print(f"{name.title()}, thank you for taking the poll.")
for language in sorted(favorite_languages.values()): # sorts the value before looping
    print(f"{language.title()} is very interesting!")