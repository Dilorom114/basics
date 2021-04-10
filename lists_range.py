# 03/11/2021 - Lists (continue)

cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
# Making Numerical list with range() functions
# range([start], stop, [step]) - Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive)
for num in range(4):
    print(f"number: {num}")

# shift + fn + f6 - mac shortcut for Refactor>rename
# shift + f6 - windows shortcut for Refactor>rename (function key needs to be turned on first)
# ctrl + Y deletes the line in windows
# command + delete deletes the line in mac

nums = range  # this does not mean nums = [0, 1, 2, 3]
nums = range  # this does not mean nums = [0, 1, 2, 3]
print(nums)
nums2 = list(range(4))  # this creates list data structure from sequence of numbers
print(nums2)
for num in nums2:
    print(num)
print("range with start and stop-------")
for num in range(1, 4):
    print(num)

print("range with start, stop and step -------")
for num in range (1, 20, 3):
    print(num)

print("print all even numbers from 1 to 16 (16 should be included)")
for num in range(2,17,2):
    print(num)

evens = []
for num in range(2, 17, 2):
    print(num)
    evens.append(num)
    print(evens)

print(f"This is the final list: {evens}")

tens = []
for num in range(0, 60, 10):
    tens.append(num)
    print(tens)

print ("print the squares of numbers from 10 to 20")

for num in range(10, 21):
    print(num**2)

squares = list()
for num in range(10, 21):
    squares.append(num**2)

print(f"final list: {squares}")
print(f"min(squares): {min(squares)}")
print(f"max(squares): {max(squares)}")
print(f"sum(squares): {sum(squares)}")


print("looping the list---------------")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars:
    print(car)
    print(f"index of the {car} is {cars.index(car)}")
print("looping the list using index**********")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for ind in range(4):  # 4 bcz length of the list
    print(ind)
    print(f"index of the {cars[ind]} is {ind}")
print("for dynamic list---------------- ")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus', 'bmw']
cars_len = len(cars)
for ind in range(cars_len):  # makes the code to match the dynamic list
    print(ind)
    print(f"index of the {cars[ind]} is {ind}")
# instead of creating the variable cars_len, we can use len() with range() for a dynamic list
for ind in range(len(cars)):  # makes the code to match the dynamic list
    print(ind)
    print(f"index of the {cars[ind]} is {ind}")

# List comprehension:
print("******List comprehension:*******")
squares = list()
for num in range(10, 21):
    squares.append(num**2)
squares = [num**2 for num in range (10,21)]  # for read only now, use later
# line 77 is equivalent to lines 74-76


# print("Exercise 4-4: One Million: **************")
# nums = []
# for num in range(1, 1000001):
#     print(num)
#     nums.append(num)
# # print(nums)

print("Exercise 4-5: One Million: **************")

# print(f"smallest: {min(nums)}")
# print(f"biggest: {max(nums)}")
# print(f"total: {sum(nums)}")


