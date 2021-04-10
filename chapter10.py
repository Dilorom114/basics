# Chapter 10
# Reading from a file
# 1. Reading an Entire File
with open('ch10/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# To do any work with a file, even just printing its contents, you first need to open the file to access it. The open() function needs one argument: the name of the file you want to open. Python looks for this file in the directory where the program that’s currently being executed is stored.
# The keyword 'with' closes the file once access to it is no longer needed.
# The read() method is used to read the entire contents of the file and store it as one long string in a variable 'contents'.
# Extra blank line appears at the end of the output  because read() returns an empty string when it reaches the end of the file; this empty string shows up as a blank line. If you want to remove the extra blank line, you can use rstrip():
with open('/Users/Dilorom/dev/basics/ch10/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# File Paths
#  To get Python to open files from a directory other than the one where your program file is stored, you need to provide a file path, which tells Python to look in a specific location on your system.
# Because .txt file is inside the python project, you could use a relative file path to open the file.
with open('data/students.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
# with open('data\students.txt') as file_object:  - On Windows systems backslash (\) is used

# You can also tell Python exactly where the file is on your computer using an absolute file path.
file_path = '/Users/Dilorom/dev/basics/ch10/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
# Using absolute paths, you can read files from any location on your system.

# 2. Reading Line by Line
filename = 'ch10/pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

filename = 'data/students.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# 3. Making a List of Lines from a File
filename = 'ch10/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
# The readlines() method takes each line from the file and stores it in a list. This list is then stored in lines, which we can continue to work with after the with block ends.

# Working with a File’s Contents
# After you’ve read a file into memory, you can do whatever you want with that data:
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# Large Files: One Million Digits
# The code in these examples would work just as well on much larger files.

print(pi_string[:40] + "...")
print(len(pi_string))
# We can print just the first 40 decimal places.

# filename = 'ch10/pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")

# Exercise 10-1
print("---------------Reading an Entire File----------------")
with open('ch10/learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

print("------------------Reading Line by Line----------------")
file_name = 'ch10/learning_python.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())

print("-----------Making a List of Lines from a File---------")
with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())

# # Exercise 10-2
# You can use the replace() method to replace any word in a string with a different word.

# file_name = 'ch10/learning_python.txt'
# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.replace('python', 'C').strip())

# Writing to a File
# Writing to an Empty File
# To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file.
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file ('r+').
# If you omit the mode argument, Python opens the file in read-only mode by default.
# The open() function automatically creates the file you’re writing to if it doesn’t already exist.
# However, be careful opening a file in write mode ('w') because if the file does exist, Python will erase the file before returning the file object.
# Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.

# Writing Multiple Lines
# The write() function doesn’t add any newlines to the text you write. Including newlines in your write() statements makes each string appear on its own line:
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Appending to a File
# If you want to add content to a file instead of writing over existing content, you can open the file in append mode.
# Any lines you write to the file will be added at the end of the file. If the file doesn’t exist yet, Python will create an empty file for you.
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# Exercise 10-3
name = input("Enter your name: ")
filename = 'guest.txt'
with open(filename, 'a') as file_object:
    file_object.write('\n' + name)

# Exercise 10-4
while True:
    name = input("Enter your name\n"
                 "(Type 'quit' to end.): ")
    if name == 'quit':
        break
    else:
        print("Hello, " + name.title() + "!")
        filename = 'guest_book.txt'
        with open(filename, 'a') as file_object:
            file_object.write('\n' + name)

# Exercise 10-5
while True:
    name = input("Enter your name\n"
                 "(Type 'quit' to end at any time.): ")
    response = input("Why do you like programming, " + name.title() + "? ")
    if name == 'quit' or response == 'quit':
        break
    else:
        filename = 'guest_book.txt'
        with open(filename, 'a') as file_object:
            file_object.write('\n' + name + '\n' + response)

# Exceptions
# Python uses special objects called exceptions to manage errors that arise during a program’s execution.
# If you write code that handles the exception, the program will continue running.
# If you don’t handle the exception, the program will halt and show a traceback, which includes a report of the exception that was raised.
# For example, ZeroDivisionError is an exception object. Python creates this kind of object in response to a situation where it can’t do what we ask it to.
# Exceptions are handled with try-except blocks.
# If the code in a try block works, Python skips over the except block. If the code in the try block causes an error, Python runs the code in an except block.
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Using Exceptions to Prevent Crashes
# Handling errors correctly is especially important when the program has more work to do after the error occurs.
# The try-except-else block. Python attempts to run the code in the try statement. Sometimes you’ll have additional code that should run only if the try block was successful; this code goes in the else block. The except block tells Python what to do in case a certain exception arises when it tries to run the code in the try statement.
# Any code that depends on the try block executing successfully goes in the else block:
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# By anticipating likely sources of errors, you can write robust programs that continue to run even when they encounter invalid data and missing resources. Your code will be resistant to innocent user mistakes and malicious attacks.

# Handling the FileNotFoundError Exception
# FileNotFoundError is the exception Python creates when it can’t find the file it’s trying to open.
# The file you’re looking for might be in a different location, the filename may be misspelled, or the file may not exist at all.
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

# Analyzing Text
# The split() method separates a string into parts wherever it finds a space and stores all the parts of the string in a list.
filename = 'ch10/alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    #  Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

# Working with Multiple Files
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        #  Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = "ch10/alice.txt"
count_words(filename)

filenames = ['ch10/alice.txt', 'ch10/learning_python.txt', 'data/students.txt', 'siddhartha.txt', 'guest_book.txt']
for filename in filenames:
    count_words(filename)
# The missing siddhartha.txt file has no effect on the rest of the program’s execution since it was taken care of in the function.

# Failing Silently
# To make a program fail silently when an exception occurs and continue on as if nothing happened, you write a try block as usual, but you explicitly tell Python to do nothing in the except block. Python has a pass statement that tells it to do nothing in a block:
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        #  Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = "ch10/alice.txt"
count_words(filename)

filenames = ['ch10/alice.txt', 'ch10/learning_python.txt', 'data/students.txt', 'siddhartha.txt', 'guest_book.txt']
for filename in filenames:
    count_words(filename)
# Now when a FileNotFoundError is raised, the code in the except block runs, but nothing happens.
# The pass statement also acts as a placeholder. It’s a reminder that you’re choosing to do nothing at a specific point in your program’s execution and that you might want to do something there later.

# Exercise 10-6&7
print("Enter two numbers to find their sum.")
print(f"(Type 'q' to quit)")
while True:
    num1 = input("Enter the first number: ")
    if num1 == 'q':
        break
    num2 = input("Enter the second number: ")
    if num2 == 'q':
        break
    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print("Please, enter a number!")
    else:
        print(f"Sum of this two numbers is: {sum}")

# Exercise 10-8
def open_file(filepath):
    """To read a file"""
    try:
        with open(filepath) as object:
            for item in object:
                print(item.strip())
    except FileNotFoundError:
        print(f"Sorry, the file {filepath} does not exist.")

open_file('ch10/cats.txt')
files = ['ch10/cats.txt', 'birds.txt', 'ch10/dogs.txt', 'ch10/rats.txt']
for file in files:
    open_file(file)

# Exercise 10-9
def open_file(filepath):
    """To read a file"""
    try:
        with open(filepath) as object:
            for item in object:
                print(item.strip())
    except FileNotFoundError:
        pass

files = ['ch10/cats.txt', 'birds.txt', 'ch10/dogs.txt', 'ch10/rats.txt']
for file in files:
    open_file(file)

# Exercise 10-10
# You can use the count() method to find out how many times a word or phrase appears in a string.
filename = "ch10/butterflies.txt"
try:
    with open(filename) as object:
        content = object.read()
except FileNotFoundError:
    print(f"There is no such a file. Check the file name or the file path.")
else:
    number = content.lower().count('the')
    print(f"The word 'the' appears {number} times inside the text.")


