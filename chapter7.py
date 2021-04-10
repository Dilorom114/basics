# Chapter 7
# The input() function pauses your program and waits for the user to enter some text. 
# Sometimes you’ll want to write a prompt that’s longer than one line. 
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name.title() + "!")
# The first line stores the first part of the message in the variable prompt. In the second line, the operator += takes the string that was stored in prompt and adds the new string onto the end.
# When you use the input() function, Python interprets everything the user enters as a string. 
# When you try to use the input to do a numerical comparison, Python produces an error because it can’t compare a string to an integer.
# We can resolve this issue by using the int() function, which tells Python to treat the input as a numerical value.
height = int(input("How tall are you, in inches? "))
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# The Modulo Operator
# A useful tool for working with numerical information is the modulo operator (%), which divides one number by another number and returns the remainder.
# The modulo operator doesn’t tell you how many times one number fits into another; it just tells you what the remainder is.
number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# Exercise 7-1
msg71 = input("What kind of a rental car you would like? ")
if msg71.lower().strip() == 'subaru':
    print("Let me see if I can find you a Subaru.")
else:
    print("A great choice!")

# Exercise 7-2
num = int(input("How many people are in your dinner group? "))
if num > 8:
    print("Sorry, you will have to wait for a table.")
else:
    print("Your table is ready.")

# Exercise 7-3
number = int(input("Enter a number: "))
if number % 10 == 0:
    print("The number is a multiple of 10")
else:
    print("The number is not a multiple of 10")

# While loops
# The for loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the while loop runs as long as, or while, a certain condition is true.

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# The while loop is then set to keep running as long as the value of current_number is less than or equal to 5. 
# Programs wouldn’t be fun to use if they stopped running before we told them to or kept running even after we wanted to quit, so while loops are quite useful.

# Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# This program works well, except that it prints the word 'quit' as if it were an actual message. A simple if test fixes this:  when quit is entered  does not print that message, but just quits running.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Using a Flag
# For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False. As a result, our overall while statement needs to check only one condition: whether or not the flag is currently True.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to Exit a Loop
# The break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren’t, so the program only executes code that you want it to, when you want it to.
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# Using continue in a Loop
# Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop based on the result of a conditional test.
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
# The continue statement tells Python to ignore the rest of the loop and return to the beginning.
# If the current number is not divisible by 2, the rest of the loop is executed and Python prints the current number.

x = 1
while x <= 5:
    print(x)
    x += 1

# if you accidentally omit the line x += 1, the loop will run forever: the value of x will start at 1 but never change. As a result, the conditional test x <= 5 will always evaluate to True and the while loop will run forever, printing a series of 1s.

# Exercise 7-4
while True:
    topping = input("Enter a topping for your pizza: ")
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping}!")

# Exercise 7-5
age = int(input("Enter your age: "))
if age < 3:
    price = 0
elif age < 13:
    price = 10
else:
    price = 15
print(f"The cost of your movie ticket is ${price}")

# Exercise 7-6
active = True
while active:
    age = int(input("Enter your age: "))
    if age < 3:
        price = 0
    elif age < 13:
        price = 10
    else:
        price = 15
    print(f"The cost of their movie ticket is ${price}")
    repeat = input("Would you like to continue? (yes/no) ")
    if repeat == "no":
        active = False
    elif repeat == "yes":
        active = True
    else:
        print("Please, type 'yes' to continue or 'no' to quit.")

# Exercise 7-7
# Write a loop that never ends, and run it
# topping = input("Enter a topping for your pizza: ")
# while True:
#     if topping == 'quit':
#         break
#     else:
#         print(f"Adding {topping}!")

# Using a while loop with Lists and Dictionaries
# 1. Moving Items from One List to Another
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 2. Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 3. Filling a Dictionary with User Input
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Store the response in the dictionary:
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")

# Exercise 7-8
sandwich_orders = ['tuna sandwich', 'bacon sandwich', 'cheese sandwich', 'beef sandwich', 'chicken sandwich']
finished_sandwiches = []
while sandwich_orders:
    in_process = sandwich_orders.pop()
    finished_sandwiches.append(in_process)
    print(f"I made your {in_process.title()}.")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} is ready to pick up.")

# Exercise 7-9
sandwich_orders = ['pastrami sandwich', 'tuna sandwich', 'bacon sandwich', 'pastrami sandwich', 'cheese sandwich',
                   'beef sandwich', 'chicken sandwich', 'pastrami sandwich']
finished_sandwiches = []
print("The deli has run out of pastrami.")
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
while sandwich_orders:
    in_process = sandwich_orders.pop()
    finished_sandwiches.append(in_process)
    print(f"I made your {in_process.title()}.")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} is ready to pick up.")

# Exercise 7-10
poll = {}
poll_active = True
while poll_active:
    name = input("What is your name? ")
    question = input("If you could visit one place in the world, where would you go? ")
    poll[name] = question
    exit = input("Would you like to let another person respond? (yes/no) ")
    if exit == 'no':
        poll_active = False
for name, question in poll.items():
    print(name.title() + " would like to go to " + question.title() + ".")


