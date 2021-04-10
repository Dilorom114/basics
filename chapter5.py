# Chapter 5
print("------------if condition---------------")
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
else:
    print(requested_topping)

print("What is the answer for 6 x 7 ?")
answer = int(input("Enter the answer:  "))
if answer != 42:
    print("That is not the correct answer. Please try again!")
else:
    print("That is right! The answer is 42.")


banned_users = ['andrew', 'carolina', 'david']
user = input("Enter your user name: ")
if user.lower() not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
else:
    print("Sorry, " + user.title() + ", you cannot make a post.")

banned_users = ['andrew', 'carolina', 'david']
user = input("Enter your user name: ")
if user.lower() in banned_users:
    print("Sorry, " + user.title() + ", you cannot make a post.")
else:
    print(user.title() + ", you can post a response if you wish.")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

age = int(input("Enter your age:  "))
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet? ")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# The if-elif-else chain is powerful, but it’s only appropriate to use when you just need one test to pass. As soon as Python finds one test that passes, it skips the rest of the tests.

print("------------1st admission---------------")
age2 = int(input("Enter your age:  "))
if age2 < 4:
    print("Your admission cost is $0.")
elif age2 < 18:
    print("Your admission cost is $5.")
elif age2 < 65:
    print("Your admission cost is $10.")
else:
    print("Your admission cost is $5.")
print("------------2nd admission---------------")
if age2 < 4:
    price = 0
elif age2 < 18:
    price = 5
elif age2 < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

print("------------omitting else---------------")
# Python does not require an else block at the end of an if-elif chain.
if age2 < 4:
    price = 0
elif age2 < 18:
    price = 5
elif age2 < 65:
    price = 10
elif age2 >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

# Testing Multiple Conditions
# To check whether two conditions are both True simultaneously, use the keyword and to combine the two conditional tests
# Exercise 5-3
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points.")

alien_color2 = 'red'
if alien_color2 == 'green':
    print("You just earned 5 points.")

# Exercise 5-4
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points.")
else:
    print("You just earned 10 points.")

alien_color2 = 'red'
if alien_color2 == 'green':
    print("You just earned 5 points.")
else:
    print("You just earned 10 points.")

# Exercise 5-5
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points.")
elif alien_color == 'yellow':
    print("You just earned 10 points.")
elif alien_color == 'red':
    print("You just earned 15 points.")

alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points.")
elif alien_color == 'yellow':
    print("You just earned 10 points.")
elif alien_color == 'red':
    print("You just earned 15 points.")

alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points.")
elif alien_color == 'yellow':
    print("You just earned 10 points.")
elif alien_color == 'red':
    print("You just earned 15 points.")

# Exercise 5-6
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

# Exercise 5-7
favorite_fruits = ['apple', 'blueberry', 'peach', 'cherry']
if 'apple' in favorite_fruits:
    print("Apple is my favorite fruit.")
else:
    print("This is not my favorite fruit.")

if 'orange' not in favorite_fruits:
    print("This is not my favorite fruit.")
else:
    print("This is my favorite fruit.")

# Using if statements with lists
print('------------------pizza toppings-----------------------')
# Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!\n")

# Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!\n")
else:
    print("Are you sure you want a plain pizza?")

# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!\n")

print("----------------multiple lists and checking for availability---------------")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese', 'green peppers']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    elif requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!\n")

print("----------------------Exercises---------------------")
# Exercise 5-8
usernames = ['anna', 'john', 'jane', 'nick', 'admin']
for user in usernames:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

# Exercise 5-9
usernames = []
if usernames:
    for user in usernames:
        print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# Exercise 5-10
print("-----need to check with 03/19/2021 recording------")
current_users = ['anna', 'john', 'jane', 'nick', 'peter']
new_users = ['ANNA', 'julie', 'John', 'liza', 'tom']

for user in new_users:
    if user.lower() in current_users:
        print(f"{user.title()}, you will need to enter a new user name.")
    else:
        print(f"{user.title()}, the username is available.")

# Exercise 5-11
ordinal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in ordinal:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
