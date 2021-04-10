# 03/21/2021 While loop, Functions
print("***Incrementing the variable to reach the upper boundary***")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1
print("***Decrementing the variable to reach the lower boundary***")
current_number = 10
while current_number >= 5:
    print(current_number)
    current_number -= 1

print("*********** Game Started **********")
# enter colors, green - 15 points, yellow - 10, red - 5
# other colors or something else you loose
# q or quit is to end the game

# color = None
# while color != 'quit':
#     color = input("Enter your color (green/yellow/red): ")
#     color = color.lower().strip()
#     points = 0
#     if color == 'green':
#         points = 15
#     elif color == 'yellow':
#         points = 10
#     elif color == 'red':
#         points = 5
#     elif color != 'quit':
#         print("Sorry, that's not right color. You lost ;)")
#     print(f"You have {points} points.")
# print("closing the game....")

color = None
while color != 'quit' or color != 'q':
    color = input("Enter your color (green/yellow/red): ")
    color = color.lower().strip()
    points = 0
    if color == 'quit' or color != 'q':
        break
    elif color == 'green':
        points = 15
    elif color == 'yellow':
        points = 10
    elif color == 'red':
        points = 5
    else:
        print("Sorry, that's not right color. You lost ;)")
    print(f"You have {points} points.")
print("closing the game....")

# Using a flag
# 'hello guys'
count = 0
for letter in 'hello guys':
    if letter == 'l':
        count += 1
print(f"number of l's is : {count}")

'''
H/w exercises: 
1. How to swap 2 variable values. Ex. a=45 b=78 >> a=78 b=45 - hint to use flag
2. Count the vowels (aeuoi) in any phrase/sentence/word.
user enters any phrase, you return:
print(f"numer of {vowels}'s is : {count}")
3. Count each letter in any phrase
4. Find the first mostly used letter in a phrase.
    (max(), dictionary, add to dictionary, if the key is in the dictionary, increment)
5. Exercises from the book
'''


