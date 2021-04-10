# 03/06/2021 # Lists (Array)
# creating a list: (empty list)
nums = list()
evens = []


num = 11
odds = [1, 3, 5, 7, 9]   # it is better to create a list with plural names
# index:           0  1  2  3  4
# negative index: -5 -4 -3 -2 -1
# 5 element, size of 'odds' list is 5
# What is the element on index 2? it is 5, because indexing starts with 0
friends = ['jackson', 'said', 'lenur', 'tyson']
print(friends[0])

# Access
first_friend = friends[0]
print(f"friends: {friends}")
print(f"first_friend: {first_friend}")
print(f"friends[0]: {friends[0]}")
print(f"friends[1]: {friends[1]}")
print(f"friends[2]: {friends[2]}")
print(f"friends[3]: {friends[3]}")
# print(f"friends[4]: {friends[4]}")  # IndexError: List index out of range
print(f"friends[-1]: {friends[-1]}")  # look at the right side of your list, negative indexes starting from the last element
print(f"friends[-3]: {friends[-3]}")
print(f"odds[3]: {odds[3]}")

# Adding elements:
# list.append (new_element)- this adds a new element to the end of the list
# list.insert(index, new_element) - this adds a new element on the indicated index, and shifts all elements to right
# add a friend : Obama to a friends list
friends.append('obama')  # this will not be printed bcz it is an operation done behind the scene
print(f"new friends list: {friends}")
friends.insert(0, 'messi')
friends.insert(1, 'ronaldo')
print(f"new friends list after insert: {friends}")
# shift + command + up/down

# resetting the existing element, only existing index should be used (replacing an element)
friends[2] = 'mark'
print(f"new friends list after reset: {friends}")
# friends[7] = 'elon' #  IndexError: list assignment index out of range
# while resetting, need to work with only existing indexes
# print(f"new friends list after adding new: {friends}")
# to comment do >> ctrl(or command) +/

# Remove the elements: by value
friends.remove('mark')
# removed_one1 = friends.remove('mark') - this is not valid statement, since remove() does not return anything
# print(removed_one1)
print(f"new friends list after removing mark: {friends}")

# Remove the elements: by index
friends.pop(4)
print(f"new friends list after removing index 4: {friends}")

removed_friends = []
removed_one = friends.pop(4)  # pop() function returns (informs) what it is removing
print(removed_one)
print(f"new friends list after popping index 4: {friends}")

del friends[-1]
print(f"new friends list after del index -1: {friends}")

friends = []
print(f"new friends list after redefining: {friends}")

# Exercise 3-3
cars = ['bugatti', 'ferrari', 'tesla', 'bmw']
print('************Exercise 3-3*****************')
print(f"I would like to own a {cars[0].title()} car.")
print(f"I would like to own a {cars[1].title()} car.")
print(f"I would like to own a {cars[2].title()} car.")
print(f"I would like to own a {cars[3].title()} car.")

# Exercise 3-4
print('************Exercise 3-4*****************')
friends = ['jackson', 'said', 'lenur', 'tyson']
print(f"Hi {friends[0].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {friends[2].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {friends[1].title()}, I would like to invite you to family dinner tomorrow.")
print(f"Hi {friends[3].title()}, I would like to invite you to family dinner tomorrow.")

# HW : Exercises till 3-7, till page 47

# Exercise 3-1
names = ['jane', 'nicole', 'sophia', 'rachel', 'maria']
print(names[-1].title())
print(names[0].upper())
print(names[2].title())
print(names[-4].upper())
print(names[-2].title())

# Exercise 3-2
print(f"Hi {names[0].title()}! How are you?")
msg = "Hi " + names[0].title() + "!" + " How are you?"
print(msg)
print(f"Hi {names[1].title()}! How are you?")
print(f"Hi {names[2].title()}! How are you?")
print(f"Hi {names[3].title()}! How are you?")
print(f"Hi {names[4].title()}! How are you?")

# Exercise 3-3
cars = ['mercedes', 'lamborghini', 'ferrari', 'tesla', 'maserati', 'jaguar']
print(f"I would like to own a {cars[0].title()} car.")
print(f"I would like to own a {cars[1].title()} car.")
print(f"I would like to own a {cars[2].title()} car.")
print(f"I would like to own a {cars[3].title()} car.")
print(f"I would like to own a {cars[4].title()} car.")
print(f"I would like to own a {cars[5].title()} car.")

# Exercise 3-4
names = ['jane', 'nicole', 'sophia', 'rachel', 'maria']
print(f"{names[0].title()}, can you come to my place for dinner this Sunday?")
print(f"{names[1].title()}, can you come to my place for dinner this Sunday?")
print(f"{names[2].title()}, can you come to my place for dinner this Sunday?")
print(f"{names[3].title()}, can you come to my place for dinner this Sunday?")
print(f"{names[4].title()}, can you come to my place for dinner this Sunday?")

# Exercise 3-5
print(names[1].title() + " cannot come.")
names[1] = "diana"
print(names)
print(f"{names[1].title()}, can you come to my place for dinner this Sunday?")

# Exercise 3-6
print(names)
names.insert(0, 'sara')
names.insert(3, 'lauren')
names.append('liza')
print(names)
print(f"{names[0].title()}, can you come to my place for dinner this Sunday?")
print(f"{names[3].title()}, can you come to my place for dinner this Sunday?")
print(f"{names[7].title()}, can you come to my place for dinner this Sunday?")

# Exercise 3-7
no_guest = names.pop()
print(no_guest.title() + ", I am sorry that I can’t invite you to dinner.")
no_guest2 = names.pop(0)
print(no_guest2.title() + ", I am sorry that I can’t invite you to dinner.")
no_guest3 = names.pop(2)
print(no_guest3.title() + ", I am sorry that I can’t invite you to dinner.")
no_guest4 = names.pop(-1)
print(no_guest4.title() + ", I am sorry that I can’t invite you to dinner.")
no_guest5 = names.pop(0)
print(no_guest5.title() + ", I am sorry that I can’t invite you to dinner.")
no_guest6 = names.pop(1)
print(no_guest6.title() + ", I am sorry that I can’t invite you to dinner.")

names = []  # removes the whole list and creates an empty one
print(names)

# 03/07/2021
# H/W: exercise 3-7
names = ['sophia', 'nicole', 'rachel', 'maria', 'jane']
removed_guests = []

removed_guests.append(names.pop())
print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")
print(removed_guests)

removed_guests.append(names.pop(0))
print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")
print(removed_guests)
print(names)

# Organizing the lists
# Sorting the list permanently
names = ['sophia', 'nicole', 'jennifer', 'rachel', 'maria', 'jane']
print(names)
names.sort()  # changing the list by sorting in descending order
print(names)
names.sort(reverse=True)  # changing the list by sorting in ascending order
print(names)
# sort() affects the original list

# Sorting the list temporarily and returning the copy of sorted list
cars = ['bmw', 'audi', 'toyota', 'subaru']
sorted_cars_asc = sorted(cars)  # copy of the list sorted in asc order
print(f"cars: {cars}")  # copy of the list sorted in desc order
print(f"sorted_cars_asc: {sorted_cars_asc}")
sorted_cars_desc = sorted(cars, reverse=True)
print(f"sorted_cars_desc: {sorted_cars_desc}")

cars.reverse()  # it is just reverses/flips the original list, does not do any type of sorting
print(f"cars reversed: {cars}")
sorted_cars_asc2 = sorted(cars)
sorted_cars_asc2.reverse()
print(sorted_cars_asc2)

# Abstract thinking is tested on solving some coding problems
print("------------list length-------")
list_size = len(cars)
print(f"cars_list_size: {list_size}")

print(f"len('toyota'): {len('toyota')}")
print(f"len('toyota      '): {len('toyota      ')}")  # space also a character that will be counted

print('Exercise 3-8')
places = ['makkah', 'paris', 'barcelona', 'khiva', 'madina']
print(f"original list: {places}")
print(f"sorted() list: {sorted(places)}")
print(f"no change after sorted(): {places}")
print(f"sorted() list in reverse: {sorted(places, reverse=True)}")
print(f"no change after sorted() in reverse: {places}")
places.reverse()
print(f"reverse(), list changed: {places}")
places.reverse()
print(f"reverse(), list changed back: {places}")
places.sort()
print(f"sort(), list changed: {places}")
places.sort(reverse=True)
print(f"sort() in reverse, list changed : {places}")

places = ['makkah', 'paris', 'barcelona', 'khiva', 'madina']
len(places)
# None = null in sql
# object : everything is an object in the python (character, file, string, variable, list, function())
# iterable : something that can be iterate (loop) most data structures, string, not a number, not boolean
# return statement: some functions return an object so we can use in print to bring up to the STDOUT (console), but some functions do not return anything (None) so the result of the print (object) will be None
