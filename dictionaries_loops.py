# 03/20/2021 Looping Through the Dictionary

my_car = {"brand": "Ford", "model": "Mustang", "year": 1964}

for key in my_car:
    print("------------------------------------")
    print(f"key in this iteration is: {key}")
    print(f"value of this key is: {my_car[key]}")

print("---------------- second -------------------")
for key in my_car.keys():
    print("----------------2-------------------")
    print(f"key in this iteration is: {key}")
    print(f"value of this key is: {my_car[key]}")

# do I have a model in the key?
# if 'model' in my_car.keys():
if 'model' in my_car:  # line 17 and 18 equivalent
    print(f"Yes my_car dect contains model information")


print("---------------- third: using values()-------------------")
for value in my_car.values():
    print("----------------2-------------------")
    print(f"value in this iteration is: {value}")
    # print(f"value of this key is: {my_car[value]}")

print("---------------- fourth: using items()----------------")
for key, value in my_car.items():
    print("----------------2-------------------")
    print(f"key in this iteration is: {key}")
    print(f"value of this key is: {value}")

if 1964 in my_car.values():
    print(f"Yes my_car dect contains 1964 information")

print("example with list sort(), sorted(list)*************")
friends = ['john', 'jane']
print(friends)
sorted_friends = sorted(friends)
friends.sort()
print(sorted_friends)
print(friends)

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python',}
print("**************sorted list*************")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}'s favorite language is {favorite_languages[name]}")

print(" ************* Exercise 6-5 **********")
rivers = {'nile': 'egypt', 'tigris': 'iraq', 'amazon': 'brazil', 'mississippi': 'usa'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# H/w 6-6
