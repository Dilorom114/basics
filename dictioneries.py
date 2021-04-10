# 03/18/2021 Dictionary - java (HashMap, HashTable)

# key/value pair data structure, since each element comes as (key: value)
# Create, access, modify (add/remove/update elements)
# Looping this data structure
# Some mostly used built-in functions

my_friend = {}
my_house = dict()
my_car = {"brand": "Ford", "model": "Mustang", "year": 1964, 1: 'value of 1'}

print(my_car['brand'])
print(f"the value of ket 'brand' is: {my_car['brand']}.")
print(my_car[1])  # this is not an index, my_car has key = 1

# updating an element
my_car['price'] = 125000.00
print("price is added-------------")
print(my_car)

# updating the value in dictionary
print("price is updated-------------")
my_car['price'] = 120000.00
print(my_car)

# removing the values from dictionary
print("element with ley 1 is being removed-------")
del my_car[1]
print(my_car)

# Exercise 6-1
print("Exercise 6-1---------------------------")
amigo = {'first_name': 'Vitaly', 'last_name': 'Didkivsky', 'age': 19, 'city': 'Florence'}
print(f"my friend's first name is : {amigo['first_name']}")
print(f"my friend's last name is : {amigo['last_name']}")
print(f"my friend is : {amigo['age']} years old")
print(f"my friend lives in : {amigo['city']}")

# H/W: Exercise 6-2, and 6-3

