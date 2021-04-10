# 03/14/2021
# Checking for multiple conditions
num = 2
if num >= 1:
    print(f"number is equal or greater than 1")
else:
    print(f"number is less than 1")

'''
expression AND/OR expression AND/OR expression AND/OR
OR:
expression OR expression = True OR False = True



num = 20
if num >= 1 and num <= 10:
    print(f"number is equal or greater than 1 and less than 10")
else:
    print(f"number is less than 1 or greater than 10")

age = int(input('enter the visitors age:  '))
if 0 <= age <= 4:
    print(f"Your admission cost is $0.")
elif 4 < age < 18:
    print(f"Your admission cost is $5.")
elif 18 <= age < 140:
    print(f"Your admission cost is $10.")
else:
    print("Invalid age was entered, bye!")
    
age = int(input('enter the visitors age:  '))
price = 0
if age < 4:
    price = 0
elif age < 18:
    price =5
elif age < 140:
    price = 10
else:
    print("Invalid age was entered, bye!")
print(f"Your admission cost is ${price}.")
'''
print("------------------- Exercise -------------------------")
# alien_color = input('enter the alien color (green/yellow/red): ')
alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points, whee!")
elif alien_color == 'red':
    print("You just earned 15 points, you are killing it, man!")
else:
    print("No points, sorry. Take a rest, meditate.")

print("========================================")
friends = []
if friends:
    print("Good for you, can I be a friend?")
else:
    print("Go out and make some friends, only good friends.")

print("***************** Using Multiple Lists ******************")
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['Mushrooms', 'french fries', '     extra Cheese']

for requested_topping in requested_toppings:
    if requested_topping.lower().strip() in available_toppings:
        print(f"I am adding {requested_topping.title().strip()}")
    else:
        print(f"Sorry, we don't have {requested_topping.upper().strip()}")

# Exercises:
# 1. FuzzBuzz, assume user enter then integer number>0
#   print Fuzz if the number is dividable by 3
#   print Buzz if the number is dividable by 5
#   print FuzzBuzz if the number is dividable by 3 and 5
# % - modulus - operator to return remainder in division
# // - floor division - division ignoring the remainder and considering only dividable num (for ex. 40 // 11 will give 3, meaning there are three 11s in 40
# num % 5 == 0 - calculates num%5 and returns a remainder, and that remainder is compared to 0, which means if remainder is 0 num is dividable by 5 without any remainder.

num = int(input("Enter a number > 0: "))
if num % 5 == 0 and num % 3 == 0:
    print("FuzzBuzz")
elif num % 3 == 0:
    print("Fuzz")
elif num % 5 == 0:
    print("Buzz")

# n % 10 <= 2 or (10 - n % 10) <= 2

# H/w:
# Implement sum() with for loop
# Double characters in a string (e.g. “abc” => “aabbcc”)
# for letter in "hello":
#     print(letter)
# Prove that a number is a prime
# Prove that a string is a palindrome (mom, dad, madam, kayak etc)

# Exercise 5-10
current_users = ['mary', 'stanley', 'joseph', 'jennifer', 'Admin']
new_users = ['sam', 'stanley', 'Mathew', 'mia', 'jennifer']
# current_users_lower =[user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")
