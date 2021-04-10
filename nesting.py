# 1. A List of lists
# 2. List of Dictionaries
# 3. A List in a Dictionary
# 4. A Dictionary in a Dictionary

# Nested list
countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies = ['level up', 'abc company', 'ola company']
# we can save all of these values in one list

customers = [companies, cities, countries]
print(customers)
print(customers[0])
print(customers[0][0])
print(f"printing barcelona: {customers[1][2]}")
# Concept of multidimensional arrays (as an idea of a matrix)

multi_dim_nums = [
    [3, 9, 0],
    [2, 7, 1],
    [0, 1, 0]
]
print(f"printing the middle value {multi_dim_nums[1][1]}")

print("----Looping through a multidimensional list(array)--")
# nested for looping
for column in customers:
    print(column)
#     # ['level up', 'abc company', 'ola company']
    for value in column:
        print(value.upper())
#
for city in customers[1]:
    print(city, end='\t')
#
for city in customers[1][0]:
    print(city, end='\t')
# iterates New York only letter by letter

print("************* list of dictionaries **************")
user_0 = {'name': 'john', 'age': 25, 'city': 'brooklyn'}
user_1 = {'name': 'jane', 'age': 20, 'city': 'paris'}
user_2 = {'name': 'mark', 'age': 35, 'city': 'tokyo'}

users = [user_1, user_0, user_2]
print(users[0])  # returns dictionary
print(users[0]['name'])  # accesses the value of the dictionary with a key
print(users[0]['age'])
print(users[0]['city'])
print(users[2]['name'])
print(users[2]['age'])
print(users[2]['city'])

print("-----------looping------------")
# This would not be possible if we had different keys in each dictionary, it would give a key error. When we want to iterate then need to be consistent in key names of dictionaries.
for user in users:
    print(user['name'], end=' || ')
    print(user['age'], end=' || ')
    print(user['city'])

for user in users:
    for key, value in user.items():
        print(f"{key}: {value}")

# Exercise 6-8 is a good example
print("***************** List in a Dictionary ***************")

countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies = ['level up', 'abc company', 'ola company']

customers = {
    'countries': ['usa', 'russia', 'spain'],
    'cities': ['new york', 'moscow', 'barcelona'],
    'companies': ['level up', 'abc company', 'ola company']
}

print(customers['cities'])
print(customers['cities'][1])  # second element from cities
print('======================================')
for keys, details in customers.items():
    print('\n' + keys + ':')
    for detail in details:
        print(detail)

# Exercise 6-9 is a good example

print("************ Dictionary in a Dictionary ************")
user_0 = {'name': 'john', 'age': 25, 'city': 'brooklyn'}
user_1 = {'name': 'jane', 'age': 20, 'city': 'paris'}
user_2 = {'name': 'mark', 'age': 35, 'city': 'tokyo'}

users = {
    'user_0': {'name': 'john', 'age': 25, 'city': 'brooklyn'},
    'user_1': {'name': 'jane', 'age': 20, 'city': 'paris'},
    'user_2': {'name': 'mark', 'age': 35, 'city': 'tokyo'}
}

print(users)
print(users['user_0'])
print(users['user_0']['name'])
print(users['user_2']['city'])

# for user in users.keys():
#     print(user)
#     print(users[user])

for username, details in users.items():
    print(username)
    # print(details['name'])
    for key in details:
        print(key)

for username, details in users.items():
    print(username)
    for key, value in details.items():
        print(f"details key is : {key}")
        print(f"details value is : {value}")

# Exercise 6-11 a good example for a dictionary in a dictionary

# H/w print multiplication table
# Exercises 6-7 to 6-12

for num in range(1, 11):
    print(num, end='\t')
    print(num*2, end='\t')
    print(num*3, end='\t')
    print(num*4, end='\t')
    print(num*5, end='\t')
    print(num*6, end='\t')
    print(num*7, end='\t')
    print(num*8, end='\t')
    print(num*9, end='\t')
    print(num*10)










