# 03/13/2021
# If statements:
# if expression:
#     code here when expression is true
# else:
#     code here when expression is false

# else expression is optional

num1 = 2
num2 = 3
if num1 < num2:
    print("expression is true")
    print("you can do something here")
else:
    print("expression is false")
print("if statement completed here")
print("----------------------------------")
num1 = 20
num2 = 3
if num1 < num2:
    print("expression is true")
    print("you can do something here")
else:
    print("expression is false")
print("if statement completed here")
print("----------------------------------")
num1 = 20
num2 = 3  # one equal sign ('=') assigns a value
if num1 == num2:  # comparing 2 values using'=='
    print("expression is true")
    print("you can do something here")
else:
    print("expression is false")
print("if statement completed here")

# if I would want a user to pass the input
# num1_str = input("enter the num1:")
# num1 = int(num1_str)
# lines 36-37 equivalent to line 40
# num1 = int(input("enter the num1:"))
# num2 = 3  # one equal sign ('=') assigns a value
# if num1 == num2:  # comparing 2 values using'=='
#     print("expression is true")
#     print("you can do something here")
# else:
#     print("expression is false")
# print("if statement completed here")

# input() functions recognizes an input as a string; need to convert it into integer if comparing numbers

print("---------------second---------------")
msg = True
if msg:
    print("expression is true")
    print("you can do something here")
else:
    print("expression is false")

print("---------------third---------------")
# msg = 0  # this will be considered as False expression
msg = 5  # this will be considered as True expression
if msg:
    print("expression is true")
    print("you can do something here")
else:
    print("expression is false")

print("---------------fourth---------------")
num = 5  # this will be considered as True expression
if num in range(6):
    print("expression is true, and num is within range")
    print("you can do something here")
else:
    print("expression is false")

num = 5  # this will be considered as True expression
if num in range(3, 6, 2):
    print("expression is true, and num is within range")
    print("you can do something here")
else:
    print("expression is false")

print("------------------------------")
num = 0  # this will be considered as True expression
if num not in range(5):
    print("expression is true, and num is outside range")
    print("you can do something here")
else:
    print("expression is false")

num = 0  # this will be considered as True expression
if num != 0:
    print("expression is true, and num is outside range")
    print("you can do something here")
else:
    print("expression is false")
# expressions can be comparison, true/false statements

print("-------------sixth-----------------")
msg = input("enter the message: ")
if msg.strip() != '':
    print(f"this message was entered: \n'{msg}'")
else:
    print("whitespace was entered")

# msg = input("enter the message: ")
if msg.strip() == '':
    print("whitespace was entered")
else:
    print(f"this message was entered: \n'{msg}'")

print("--------Comparing the string values ---------")
name = input('Please, enter your name: ')
if name.strip().lower() == 'john doe':
    print(f"We have missed you {name.title()}.")
else:
    print(f"Welcome {name.title()}!")

print("----------if statement with lists----------")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
if 'tesla' in cars:
    print("Yes, we have tesla in stock.")
else:
    print("Sorry, we don't have this car.")

print("---------if statement with strings-------")
if 'sat' in "today is saturday":  # we could check for a  whole word or a part of a string the same way
    print("Yes, it is a part of the string.")
else:
    print("No, it is not a part of the string..")

print("-------if statement with lists and looping------")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars:
    if car == 'tesla':
        print(f"This is {car.upper()}")
    else:
        print(f"Current car is {car.title()}")

print("------if statement with lists and looping------")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars:
    if car == 'tesla':
        print(f"This is {car.upper()}")
        break  # stop the looping
    else:
        print(f"Current car is {car.title()}")

print("exercise: ------------------------")
# print values but when you find 5, print it and print 'completed'
nums = [45, 4, 5, 6, 3, 10]
for num in nums:
    if num == 5:
        print(num, " completed")
        break
    else:
        print(num, "is not 5")


print("-----------------incrementing -----------------")
nums = [45, 4, 5, 6, 3, 10, 5, 123, 346, 4, 5, 666, 5]
count = 0  # it should be declared before and outside of for-loop
for num in nums:
    if num == 5:
        count = count + 1 # count + = 1 incrementing count by 1 every time (decrementing: count - = 1)
print(count)
# count + = 1 means increment the new value of count by 1 each time
# need extra variable to count how many 5s
# + increment # - decrement

# H/w count how many 5s you have in the list
# hint: use additional variable to save the counts and keep incrementing it every time you encounter the 5 in the list
