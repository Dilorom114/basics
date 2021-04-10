# 03/13/2021
# 1. Style the code
# PEP 8 - Styling Guide for Python Code
# PEP 8 does not recommend using to many blank line between codes, autoformatting removes extra blank lines
# autoformatting in pycharm - ctrl + alt + L

# Working with the part of the list
# slice of the list list_name[start:stop] - start is inclusive, stop is exclusive values
# values: list_name[start], list_name[start+1], ... , list_name[stop-1]
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']

for car in cars:
    print(f"the car is : {car}")

for car in cars[1:2]:  # slicing accessed with []
    print(f"the car by given range of index : {car}")

for car in cars[1:3]:  # slicing accessed with []
    print(f"the car by given given range of index : {car}")

print("-----------------second-----------------")
for car in cars[:3]:  # the same thin as [0:3]
    print(f"the car is : {car}")
# if you are starting from 0, don't have to put it in the range: [:3]

print("-----------------third-----------------")
# the same idea for the last element of the list
for car in cars[2:]:  # the same thin as [2:endofthelist]
    print(f"the car is : {car}")

for car in cars[2:-1]:  # is not the same as [2:]
    print(f"the car is : {car}")

print("-----------------fourth-----------------")
for car in cars[2:5]:  # no out of range index error
    print(f"the car is : {car}")

print("--------------copying and linking-----------------")
print("-----linking the 2 variables to the same value-----")
cars2 = cars
print(f"cars: {cars}")
print(f"cars2: {cars2}")
cars.append('bmw')
print(f"cars after update: {cars}")
print(f"cars2 after update: {cars2}")

print("---------------------copying--------------------")
cars3 = cars[:]
print(f"cars: {cars}")
print(f"cars3: {cars3}")
cars.append('toyota')
print(f"cars after update: {cars}")
print(f"cars3 after update: {cars3}")

print("Exercise 4-10: slicing")
print(f"The first three items in the list are: {cars[:3]}")
print(f"Three items from the middle of the list are: {cars[2:5]}")
print(f"The last three items in the list are: {cars[3:]}")

# Lists can be modified (mutable)
# Tuples - data structure similar to list but can not be modified (immutable)
cars_t = ('bugatti', 'ferrari', 'tesla', 'lexus')
print(f"first value is : {cars_t[0]}")
cars[0] = 'honda'  # this is possible since cars is the list data structure
# cars_t[0] = 'honda' # this is not possible since cars_t is the tuple data structure
print(f"cars_t tuple: {cars_t}")

# tuples could be redefined/redeclared
cars_t = ('honda', 'ferrari', 'tesla')
print(f"cars_t tuple after redeclared: {cars_t}")
print(f"size of the tuple: {len(cars_t)}")
# len() is the function that can accept an object (not only list)
# del is also universal function which accept multiple data structure - del cars[2]
