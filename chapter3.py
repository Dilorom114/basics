# Chapter 3
# A list is a collection of items in a particular order.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
# Lists are ordered collections, so you can access any element in a list by telling Python the position,
# or index, of the item desired.
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

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

# Modifying Elements in a List (resetting)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding Elements to a List
motorcycles.append('honda')
print(motorcycles)

motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2)

motorcycles2.insert(0, 'ducati')
print(motorcycles2)

# Removing an Item Using the del Statement
del motorcycles2[0]
print(motorcycles2)
del motorcycles2[1]
print(motorcycles2)
# You can no longer access the value that was removed from the list after the del statement is used.

# Removing an Item Using the pop() Method
# Sometimes you’ll want to use the value of an item after you remove it from a list.
# For example, in a web application, you might want to remove a user from a list of active members
# and then add that user to a list of inactive members.

print(motorcycles2)  # We start by defining and printing the list motorcycles
popped_motorcycle = motorcycles2.pop()  # we pop a value from the list and store that value in the variable popped_motorcycle
print(motorcycles2)  # We print the list to show that a value has been removed from the list.
print(popped_motorcycle)  # We print the popped value to prove that we still have access to the value that was removed.

# The output shows that the value 'suzuki' was removed from the end of the list
# and is now stored in the variable popped_motorcycle

# Imagine that the bicycles in the list are stored in chronological order according to when we owned them.
# We can use the pop() method to print a statement about the last motorcycle we bought:
print(bicycles)
last_owned = bicycles.pop()
print("The last bicycle I owned was a " + last_owned.title() + ".")
print(bicycles)
bicycles.append('hybrid')
print(bicycles)
last_owned = bicycles.pop()
print("The last bicycle I owned was a " + last_owned.title() + ".")
print(bicycles)
# You can actually use pop() to remove an item in a list at any position by including the index of the item you want to remove in parentheses.
first_owned = bicycles.pop(0)
print("The first bicycle I owned was a " + first_owned.title() + ".")
print(bicycles)
# Remember that each time you use pop(), the item you work with is no longer stored in the list.
# When you want to delete an item from a list and not use that item in any way, use the del statement;
# if you want to use an item as you remove it, use the pop() method.

# Removing an Item by Value
# If you only know the value of the item you want to remove, you can use the remove() method.
print(motorcycles)
motorcycles.remove('ducati')  # The code tells Python to figure out where 'ducati' appears in the list and remove it.
print(motorcycles)
# You can also use the remove() method to work with a value that’s being removed from a list.
too_expensive = 'honda'  # we store the value 'ducati' in a variable called too_expensive
motorcycles.remove(too_expensive)  # we use this variable to tell which value to remove from the list
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for mee.")  # the value 'ducati' has been removed from the list
# but is still stored in the variable too_expensive, allowing us to print a statement about why we removed 'ducati' from the list of motorcycles

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
names = []  # creates an empty list
print(names)

# Organizing a list
# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# The sort() method changes the order of the list permanently. The cars are now in alphabetical order, and we can never revert to the original order.

cars.sort(reverse=True)  # Again, the order of the list is permanently changed
print(cars)

# Sorting a List Temporarily with the sorted() Function
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")

# Printing a List in Reverse Order
print(cars)
cars.reverse()
print(cars)

# Finding the Length of a List
print(len(cars))

# Exercise 3-8
places = ['makkah', 'paris', 'barcelona', 'khiva', 'tokyo']
print(f"original list: {places}")
print(f"sorted() list: {sorted(places)}")  # sort asc A-Z temporarily
print(f"no change after sorted(): {places}")
print(f"sorted() list in reverse: {sorted(places, reverse=True)}")  # sort desc Z-A temporarily
print(f"no change after sorted() in reverse: {places}")
places.reverse()  # flips the list
print(f"reverse(), list changed: {places}")
places.reverse()  # flips the list back
print(f"reverse(), list changed back: {places}")
places.sort()  # sort asc A-Z permanently
print(f"sort(), list changed: {places}")
places.sort(reverse=True)  # sort desc Z-A permanently
print(f"sort() in reverse, list changed : {places}")

# Exercise 3-9
names = ['jane', 'nicole', 'sophia', 'rachel', 'maria']
print(names)
print(len(names))

# Exercise 3-10

# Exercise 3-11
places = ['makkah', 'paris', 'barcelona', 'khiva', 'tokyo']
# print(places[5]) - IndexError: list index out of range
print(places[4])

print(len(places))
list_size = len(places)
print(f"places_list_size: {list_size}")
