bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[-1] = 'giant'
print(bicycles)
# bicycles[5] = 'merida'

bicycles.pop(2)
print(bicycles)

popped_bicycle = bicycles.pop()  # we pop a value from the list and store that value in the variable popped_motorcycle
print(bicycles)  # We print the list to show that a value has been removed from the list.
print(popped_bicycle)  # We print the popped value to prove that we still have access to the value that was removed.

# Imagine that the bicycles are stored in chronological by when owned, to see the last bicycle we bought:
print("The last bicycle I owned was a " + bicycles.pop().title() + ".")
print(bicycles)
# Remember that each time you use pop(), the item you work with is no longer stored in the list.

cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
too_expensive = 'ferrari'  # we store the value in a variable
cars.remove(too_expensive)  # we use this variable to tell what to remove
print("\nA " + too_expensive.title() + " is too expensive for me.")
print(cars)

print("\nA " + cars.pop().title() + " is too expensive for me.")  # with pop () only one line
print(cars)


print('--------------Looping the list using index------------------')
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars:
    print(f"index of the {car} is {cars.index(car)}")

for ind in range(len(cars)):
    print(f"index of the {cars[ind]} is {ind}")

print("********************guests*********************")
names = ['jane', 'nicole', 'lauren', 'sophia', 'maria']  # original list
removed_guests = []  # we create an empty list to store the popped elements of a list

for num in range(2):
    removed_guests.append(names.pop())
    print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")

print(f"remaining guests list: {names}")
print(f"removed guests list: {removed_guests}")

print("******List comprehension:*******")
# List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
# line 52 is equivalent to lines 54-56

print("------------------Copying------------------")
my_cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
friend_cars = my_cars[:]
print(my_cars)
print(friend_cars)
# To prove that we actually have two separate lists, we’ll add a new food to each list
my_cars.append('bmw')
friend_cars.append('toyota')
print(my_cars)
print(friend_cars)
print("--------------copying and linking-----------------")
my_cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
friend_cars = my_cars
my_cars.append('maserati')
friend_cars.append('honda')
print(my_cars)
print(friend_cars)

# Tuples
# Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
# A tuple looks just like a list except you use parentheses instead of square brackets.
# you can access individual elements by using each item’s index, just as you would for a list.
pizzas = ('chicken', 'broccoli', 'pepperoni')
print(pizzas[0])
print(pizzas[1])

# pizzas[1] = 'mushroom' - this is not possible since pizzas is the tuple data structure
# TypeError: 'tuple' object does not support item assignment

# If we wanted to change an element in pizzas, we could redefine/redeclare the entire tuple
print(pizzas)
pizzas = ('spinach', 'broccoli', 'pepperoni', 'mushroom',)
print(pizzas)

# Looping Through All Values in a Tuple
for pizza in pizzas:
    print(pizza.title())

# print("What is the answer for 6 x 7 ?")
# answer = int(input("Enter the answer:  "))
# if answer != 42:
#     print("That is not the correct answer. Please try again!")
#     answer2 = int(input("Enter the answer:  "))
#     if answer2 != 42:
#         print("That is not the correct answer. Please try again!")
#         answer3 = int(input("Enter the answer:  "))
#         if answer3 != 42:
#             print("That is not the correct answer. Game over!")
#         else:
#             print("That is right! The answer is 42.")
#     else:
#         print("That is right! The answer is 42.")
# else:
#     print("Great Job! The answer is 42.")

ages = int(input("Enter your age: "))
if ages < 2:
    print("You are a baby.")
elif ages < 4:
    print("You are a toddler.")
elif ages < 13:
    print("You are a kid.")
elif ages < 20:
    print("You are a teenager.")
elif ages < 65:
    print("You are an adult.")
else:
    print("You are an elder.")
