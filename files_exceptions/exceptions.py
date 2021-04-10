# Exception Handling - handle the situations where you expect certain type of errors

filepath = "/Users/Dilorom/dev/base/data/students.txt"

try:
    print('trying block started....')
    with open(filepath, 'a') as students:
        print("writing to the file...")
        students.write(f"\nSegey")

    with open(filepath, 'r') as students:
        lines = students.readlines()
        print(lines)
except FileNotFoundError as err:
    print(err)
    print("Check your file path and enter the correct one.")

# print(5/0)

# try:
#     print(5/0)

try:
    num = 5/int(input('enter the number to divide by: '))
except ZeroDivisionError as err:
    print('You can not divide by zero')
else:  # This is dependent on try block, if try block executed else block will be executed
    print('this is else block')
    print(f"Result of this division: {num}")
finally:
    print("I am a Finally block, I am always executed whatever happens with try, except or else block.")

print("Program is completed!!")

# 2:47 recording question


