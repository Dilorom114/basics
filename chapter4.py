# Chapter 4
# Looping allows you to take the same action, or set of actions, with every item in a list. As a result, you’ll be able to work efficiently with lists of any length, including those with thousands or even millions of items.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:  # This line tells Python to pull a name from the list magicians, and store it in the variable magician.
    print(magician)  # we tell Python to print the name that was just stored in magician for each name in the list

# “For every magician in the list of magicians, print the magician’s name.”

for magician in magicians:
    print(magician.title() + ", that was a great trick!")

# Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list.

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + "\n")

print("Thank you, everyone. That was a great magic show!")

# Any lines of code after the for loop that are not indented are executed once without repetition.

# for magician in magicians:
# print(magician) - IndentationError: expected an indented block

# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
# print("I can't wait to see your next trick, " + magician.title() + "\n")

# Exercise 4-1
pizzas = ['pepperoni', 'broccoli', 'chicken']
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("I really love pizza!")

# Exercise 4-2
wcats = ['lion', 'tiger', 'leopard', 'panther']
for cat in wcats:
    print("A " + cat.title() + " belongs to the Felidae family which are referred as cats.")
print("Any of these animals are carnivorous mammals of the cat family.")

# Making numerical lists
# You’ll almost always work with sets of numbers, such as temperatures, distances, population sizes, or latitude and longitude values, among other types of numerical sets.

# Using the range() Function
# range() function makes it easy to generate a series of numbers.
for value in range(1, 5):
    print(value)

# The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide. This is a result of the off-by-one behavior in programming languages.
for value in range(1, 6):
    print(value)

for num in range(4):
    print(f"number: {num}")
# Using range() to Make a List of Numbers
# You can convert the results of range() directly into a list using the list() function. When you wrap list() around a call to the range() function, the output will be a list of numbers.
numbers = list(range(1, 6))
print(numbers)

# We can also use the range() function to tell Python to skip numbers in a given range.
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# The range() function starts with the value 2 and then adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end value, 11.

# How you might make a list of the first 10 square numbers?
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# Simple Statistics with a List of Numbers
# You can easily find the minimum, maximum, and sum of a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print(f"final list: {squares}")
print(f"min(squares): {min(squares)}")
print(f"max(squares): {max(squares)}")
print(f"sum(squares): {sum(squares)}")

print("********************guests*********************")
names = ['jane', 'nicole', 'lauren', 'sophia', 'maria']  # original list
removed_guests = []  # we create an empty list to store the popped elements of a list

for num in range(2):
    removed_guests.append(names.pop())
    print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")

print(f"remaining guests list: {names}")
print(f"removed guests list: {removed_guests}")

# List Comprehensions
# The approach described earlier for generating the list squares consisted of using three or four lines of code. A list comprehension allows you to generate this same list in just one line of code.
squares = [value**2 for value in range(1, 11)]
print(squares)

# Exercise 4-3
for num in range(1, 21):
    print(num)

# Exercise 4-4
million = []
for value in range(1, 1000001):
    million.append(value)
    # print(million)
# If the output is taking too long, stop it by pressing
# ctrl-C - for windows
# Command + fn + F2 - for mac

# Exercise 4-5
print(min(million))
print(max(million))
print(sum(million))

# Exercise 4-6
odd_num = []
for num in range(1, 21, 2):
    odd_num.append(num)
print(odd_num)
# List Comprehension
odd_num2 = [num for num in range(1, 21, 2)]
print(odd_num2)

# Exercise 4-7
multi3 = []
for value in range(3, 31, 3):
    multi3.append(value)
print(multi3)
# List Comprehension
multi33 = [value for value in range(3, 31, 3)]
print(multi33)

# Exercise 4-8
cube = []
for value in range(1, 11):
    cube.append(value**3)
print(cube)

# Exercise 4-9
# List Comprehension
cube2 = [num**3 for num in range(1, 11)]
print(cube2)

# Working with Part of a list
# Slicing a List
# To make a slice, you specify the index of the first and last elements you want to work with. As with the range() function, Python stops one item before the second index you specify.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:
print(players[:4])
# A similar syntax works if you want a slice that includes the end of a list.
print(players[2:])
# For example, if we want to output the last three players on the roster, we can use the slice players[-3:]:
print(players[-3:])

# Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a List
# To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]). This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# To prove that we actually have two separate lists, we’ll add a new food to each list
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# If we had simply set friend_foods equal to my_foods, we would not produce two separate lists. For example, here’s what happens when you try to copy a list without using a slice:
# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# This syntax actually tells Python to connect the new variable friend_foods to the list that is already contained in my_foods, so now both variables point to the same list.

# Exercise 4-10
wcats = ['lion', 'tiger', 'leopard', 'panther']
print("The first three items in the list are:")
for cat in wcats[0:3]:
    print(cat.title())
print("Three items from the middle of the list are:")
for cat in wcats[1:]:
    print(cat.title())
print("The last three items in the list are:")
for cat in wcats[-3:]:
    print(cat.title())

# Exercise 4-11
pizzas = ['pepperoni', 'broccoli', 'chicken']
friend_pizzas = pizzas[:]
pizzas.append('mushroom')
friend_pizzas.append('spinach')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
print("My friend’s favorite pizzas are:")
for fpizza in friend_pizzas:
    print(fpizza.title())

# Exercise 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for mfood in my_foods:
    print(mfood.title())
print("\nMy friend's favorite foods are:")
for ffood in friend_foods:
    print(ffood.title())

# Tuples
# Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
# A tuple looks just like a list except you use parentheses instead of square brackets.
# you can access individual elements by using each item’s index, just as you would for a list.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 - TypeError: 'tuple' object does not support item assignment

# Looping Through All Values in a Tuple
for dimension in dimensions:
    print(dimension)

# If we wanted to change an element in dimensions, we could redefine the entire tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Exercise 4-13
dishes = ('applebees', 'lobster', 'pizza', 'steakhouse', 'chipotle')
for dish in dishes:
    print(dish.title())
# dishes[1] = 'taco' - TypeError: 'tuple' object does not support item assignment
dishes = ('taco', 'grill', 'pizza', 'steakhouse', 'chipotle')
for dish in dishes:
    print(dish.title())

# Styling your Code
# When someone wants to make a change to the Python language, they write a Python Enhancement Proposal (PEP). One of the oldest PEPs is PEP 8, which instructs Python programmers on how to style their code.

# Appendix B shows you how to configure your text editor so it always inserts four spaces each time you press the tab key and shows a vertical guideline to help you follow the 79-character limit.
