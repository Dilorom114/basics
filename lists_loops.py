# 03/07/2021
# Loops - process of iterating, going through the elements
# Flow control
# syntax in python language (for loop):

# for temp_variable in iterable:
#    some code to execute repetitively
#    some code to execute repetitively
#    some code to execute repetitively
#    some code to execute repetitively
#    some code to execute repetitively
#    some code to execute repetitively

# some code to execute outside of for loop

# in Pycharm there are 4 spaces to start the for loop, Tab does not give that 4 spaces in windows; Pycharm takes care of that tab = 4 spaces

cars = ['bugatti', 'ferrari', 'tesla', 'bmw']
print('************Exercise 3-3*****************')
for car in cars:
    print(f"I would like to own a {car.title()} car.")

print("This dreaming help me to motivate and work harder.")  # print statement outside the loop

# scope of your variable - life of your variable
# variable car in previous loop example does not exist outside loop. It needs to be defined to be used outside
# print(car) - out of scope

# java example that is not sensitive to spaces but requires {}
# for car in cars {
# print(f"I would like to own a {car.title()} car.")
# }

# java or C++ use {} to show the loop, space does not matter

print('**************Exercises**************')
# Exercise 1
names = ['jane', 'nicole', 'sophia', 'rachel', 'maria']
for name in names:
    print(name.title())
    print(f"Hi {name.title()}! How are you?")
    print(f"{name.title()}, can you come to my place for dinner this Sunday?")

# Exercise 2
cars = ['mercedes', 'lamborghini', 'ferrari', 'tesla', 'maserati', 'jaguar']
for car in cars:
    print(f"I would like to own a {car.title()} car.")

# Exercise 3
names = ['jane', 'nicole', 'sophia', 'rachel', 'maria']
names.insert(0, 'sara')
names.insert(3, 'lauren')
names.insert(4, 'liza')
print(names)
print(f"{names[0].title()}, can you come to my place for dinner this Sunday?")
print(f"{names[3].title()}, can you come to my place for dinner this Sunday?")
print(f"{names[7].title()}, can you come to my place for dinner this Sunday?")

# Exercise 4
names = ['sara', 'jane', 'nicole', 'lauren', 'liza', 'sophia', 'rachel', 'maria']
print(f"original guest list: {names}")
removed_guests = []  # we create an empty list to store the popped elements of a list

removed_guests.append(names.pop())
print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")
removed_guests.append(names.pop())
print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")
removed_guests.append(names.pop())
print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")
removed_guests.append(names.pop())
print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")
removed_guests.append(names.pop())
print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")
removed_guests.append(names.pop())
print(removed_guests[-1].title() + ", I am sorry that I can’t invite you to dinner.")

print(f"remaining guests list: {names}")
print(f"removed guests list: {removed_guests}")
