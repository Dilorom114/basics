# Chapter 8
# Functions are named blocks of code that are designed to do one specific job. When you want to perform a particular task that you’ve defined in a function, you call the name of the function responsible for it.
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()

# def - function definition - tells Python the name of the function and, if applicable, what kind of information the function needs to do its job.
# Any indented lines after the def line make up the body of the function.
# Docstring is enclosed in triple quotes, and describes what the function does.
# A function call tells Python to execute the code in the function. To call a function, you write the name of the function, followed by any necessary information in parentheses.

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
# By adding username here you allow the function to accept any value of username you specify. The function now expects you to provide a value for username each time you call it.

# Arguments and Parameters
# The variable username in the function definition is an example of a parameter, a piece of information the function needs to do its job.
# An argument is a piece of information that is passed from a function call to a function. The value 'jesse' is an example of an argument.

# Exercise 8-1
def display_message():
    print("In Chapter 8 I will be learning Functions.")

display_message()

# Exercise 8-2
def favorite_book(title):
    print(f"One of my favorite book is {title.title()}")

favorite_book('alice in wonderland')

# Positional Arguments
# When you call a function, Python must match each argument in the function call with a parameter in the function definition which is called positional arguments.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
# You can call a function as many times as needed.

# Keyword Arguments
# A keyword argument is a name-value pair that you pass to a function. Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
# The order of keyword arguments doesn’t matter because Python knows where each value should go.

# Default Values
# When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
# Note that the order of the parameters in the function definition had to be changed because Python still interprets this as a positional argument.
# When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly.
# If you specify a default value for a parameter, no spaces should be used on either side of the equal sign.

# Equivalent Function Calls
# Because positional arguments, keyword arguments, and default values can all be used together, often you’ll have several equivalent ways to call a function.
describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
# Each of these function calls would have the same output as the previous examples

# Unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work.

# Exercise 8-3
def make_shirt(size, message):
    print(f"\nThe size of the shirt is {size}.")
    print(f"The message on the shirt is: {message.upper()}")

make_shirt('M', 'i love ny')  # positional arguments call
make_shirt(message='i love ny', size='M')  # keyword arguments

# Exercise 8-4
def make_shirt(message='I love Python', size='L'):
    print(f"\nThe size of the shirt is {size}.")
    print(f"The message on the shirt is: {message.upper()}")

make_shirt()
make_shirt(size='M')
make_shirt('Just Do It', 'S')

# Exercise 8-5
def describe_city(city, country='USA'):
    print(f"\n{city.title()} is in {country}.")

describe_city('new york')
describe_city('tashkent', 'Uzbekistan')
describe_city(country='England', city='london')

# Return Values
# A function doesn’t always have to display its output directly. Instead, it can process some data and then return a value or set of values. The value the function returns is called a return value.
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an Argument Optional
# You can use default values to make an argument optional.
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
# (Since previous code makes the middle name mandatory) To make middle name optional an empty string is set as its default value:

def get_formatted_name(first_name, last_name,  middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# Returning a Dictionary
# A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries.
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('josh', 'groban')
print(musician)
# You can easily extend this function to accept optional values:
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Using a Function with a while Loop
# This is an infinite loop!
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

# Exercise 8-6
def city_country(city, country):
    print(f'"{city.title()}, {country.title()}"')

city_country('tashkent', 'uzbekistan')
city_country(country='russian', city='moscow')
city_country('tokyo', 'japan')

# Exercise 8-7
# Track number is an integer type data
def make_album(artist, album, tracks_number=0):
    songs = {}
    songs['artist'] = artist
    songs['album'] = album
    if tracks_number > 0:
        songs['tracks'] = tracks_number
    return songs
# Track number is a string type data
# def make_album(artist, album, tracks_number =''):
#     songs={}
#     songs['artist']= artist
#     songs['album'] = album
#     if tracks_number:
#         songs['tracks'] = tracks_number
#     return songs

print(make_album('linkin park', 'meteora'))
print(make_album('tokio hotel', 'schrei'))
print(make_album('sia', '1000 form of fear', 12))

# Exercise 8-8
while True:
    print("\n What is your favorite album? ")
    print("(Enter 'q' any time to quit)")

    artist_name = input("The name of the artist: ")
    if artist_name == 'q':
        break
    album_name = input("The name of the album: ")
    if album_name == 'q':
        break
    dictionary = make_album(artist_name, album_name)
    print(f"My favorite album: \n{dictionary}")
    print(f"My favorite album is {dictionary['album'].title()} by {dictionary['artist'].title()}.")

# Passing a list
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a Function
# When you pass a list to a function, the function can modify the list.
# The following code does this without using functions:
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# We can reorganize this code by writing two functions, each of which does one specific job.
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
# This program is easier to extend, maintain, and reuse (when more models need to be printed) than the version without functions.

# Preventing a Function from Modifying a List
# You can send a copy of a list to a function like this:
# function_name(list_name[:])
# So, the previous function definition will be like this:
# If we didn’t want to empty the list of unprinted_designs, we could call print_models() like this:
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# Exercise 8-9
def show_magicians(names):
    for name in names:
        print(name.title())

magicians = ['alice', 'david', 'carolina']
show_magicians(magicians)

# Exercise 8-10
def make_great(names):
    for name in names:
        print('the Great'+ ' ' +name.title())

make_great(magicians)

new_list = []
def make_great(names):
    while names:
        new_name = names.pop()
        new_list.append('the Great'+ ' ' + new_name.title())
    print(new_list)

print(magicians)
make_great(magicians)
print(magicians)
print(new_list)

# Exercise 8-11
print(magicians)
make_great(magicians[:])
show_magicians(magicians)
print(magicians)
print(new_list)

# Passing an arbitrary number of arguments
# Python allows a function to collect an arbitrary number of arguments from the calling statement - as many as needed
# The function in the following example has one parameter, *toppings, but this parameter collects as many arguments as the calling line provides:
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguments
# You can write functions that accept as many key-value pairs as the calling statement provides.
# In the following example the function always takes in a first and last name, but it accepts an arbitrary number of keyword arguments as well:
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location= 'princeton', field='physics')
print(user_profile)
# The double asterisks before the parameter **user_info cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary.
# You can mix positional, keyword, and arbitrary values in many different ways when writing your own functions.

# Exercise 8-12
def make_sandwich(*sandwich_items):
    print(f"\nMaking a sandwich with following:")
    for item in sandwich_items:
        print(f"\t* {item}")


make_sandwich('chicken')
make_sandwich('butter', 'cheese')
make_sandwich('cream cheese', 'tuna', 'lettuce')

# Exercise 8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile2 = build_profile('dilorom', 'akhmed', location= 'new york', filed='IT')
print(user_profile2)

# Exercise 8-14
def make_car(car_manufacturer, car_model, **car_info):
    """Build a dictionary about a car"""
    cars = {}
    cars['manufacturer'] = car_manufacturer
    cars['model'] = car_model
    for key, value in car_info.items():
        cars[key] = [value]
    return cars

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

# Storing Your Functions in Modules
# You can store your functions in a separate file called a module and then import that module into your main program.
# An import statement tells Python to make the code in a module available in the currently running program file.

# Importing an Entire Module
# If we save make_pizza function in file pizza.py and create another and import the function, we would be able to use the function in a new file as well:
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# The line import pizza tells Python to open the file pizza.py and copy all the functions from it into the current program (another file).
# To call a function from an imported module, enter the name of the module you imported, pizza, followed by the name of the function, make_pizza(), separated by a dot.
# This first approach to importing, in which you simply write import followed by the name of the module, makes every function from the module available in your program.
# Syntax: module_name.function_name()

# Importing Specific Functions
# You can also import a specific function from a module.
# Syntax: from module_name import function_name
# You can import as many functions as you want from a module by separating each function’s name with a comma:
# from module_name import function_0, function_1, function_2
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Function an Alias
# If the name of a function you’re importing might conflict with an existing name in your program or if the function name is long, you can use a short, unique alias—an alternate name similar to a nickname for the function.
# Syntax: from module_name import function_name as fn
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Module an Alias
# You can also provide an alias for a module name.
# Syntax: import module_name as mn
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module
# Because every function is imported, you can call each function by name without using the dot notation.
# Syntax: from module_name import *
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

