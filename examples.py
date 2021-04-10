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


print('--------------Looping with index------------------')
pizzas = ['pepperoni', 'broccoli', 'chicken']

print("looping the list using index**********")
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

print("------------if conditions---------------")
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in  cars:
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

print("What is the answer for 6 x 7 ?")
answer = int(input("Enter the answer:  "))
if answer != 42:
    print("That is not the correct answer. Please try again!")
    answer2 = int(input("Enter the answer:  "))
    if answer2 != 42:
        print("That is not the correct answer. Please try again!")
        answer3 = int(input("Enter the answer:  "))
        if answer3 != 42:
            print("That is not the correct answer. Game over!")
        else:
            print("That is right! The answer is 42.")
    else:
        print("That is right! The answer is 42.")
else:
    print("Great Job! The answer is 42.")

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
    
age2 = int(input("Enter your age:  "))
if age2 < 4:
    print("Your admission cost is $0.")
elif age2 < 18:
    print("Your admission cost is $5.")    
else:
    print("Your admission cost is $10.")
    
if age < 4:
    price = 0 
elif age < 18:
    price = 5 
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

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

# A list in a dictionary
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskel'],
    }
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n {name.title()}'s favorite languages are:")
    else:
        print(f"\n {name.title()}'s favorite language is:")
    for language in languages:
        print(f"\t {language.title()}")

