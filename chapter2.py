# Chapter 2
# Changing Case in a String with Methods

name = "ada lovelace"
print(name.title())
# In this example, the lowercase string "ada lovelace" is stored in the variable name.
# The method title() appears after the variable in the print() statement.
# A method is an action that Python can perform on a piece of data.
# The dot (.) after name in name.title() tells Python to make the title() method act on the variable name.
# Every method is followed by a set of parentheses, because methods often need additional information to do their work.
# That information is provided inside the parentheses.

# title() displays each word in title case, where each word begins with a capital letter.
name = "ada lovelace"
print(name.upper())
print(name.lower())

# The lower() method is particularly useful for storing data.
# Many times you won’t want to trust the capitalization that your users provide, so you’ll convert strings to lowercase before storing them.
# Then when you want to display the information, you’ll use the case that makes the most sense for each string.

# Combining or Concatenating Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)

# Adding Whitespace to Strings with Tabs or Newlines
# In programming, whitespace refers to any non printing character, such as spaces, tabs, and end-of-line symbols.
print("\tPython")
print("Language:\nPython\nC\nJavaScript")
print("Language:\n\tPython\n\tC\n\tJavaScript")
# Stripping Whitespace
favourite_language = 'python '
print(favourite_language.rstrip())
favourite_language = ' python'
print(favourite_language.lstrip())
favourite_language = ' python '
print(favourite_language.strip())
# In the real world, these stripping functions are used most often to clean up user input before it’s stored in a program.

# If you use an apostrophe within single quotes, you’ll produce an error.
print('I told my friend, "Python is my favorite language!"')
print("The language 'Python' is named after Monty Python, not the snake.")
print("One of Python's strengths is its diverse and supportive community.")

# Exercise 2-3:
vname = "Eric"
msg23 = f"Hello {vname}, would you like to learn some Python today?"
print(msg23)
# Exercise 2-4:
print(vname.lower())
print(vname.upper())
print(vname.title())
# Exercise 2-5:
print('\t\t\tAlbert Einstein once said, "A person who never made a \n\t\t\tmistake never tried anything new."')
# Exercise 2-6:
famous_person = "Albert Einstein"
msg26 = '\t\t\tAlbert Einstein once said, "A person who never made a \n\t\t\tmistake never tried anything new."'
print(msg26)
# Exercise 2-7:
famous_person2 = "\n\t\t\t\tAlbert Einstein\n\n\n\t\t"
print(famous_person2)
print(famous_person2.strip())
print(famous_person2.rstrip())
print(famous_person2.lstrip())

print(3**3)
print(2+3*4)
print((2+3)*4)

# Python calls any number with a decimal point a float.
print(2*0.2)

# Avoiding Type Errors with the str() Function
age = 23
# msg24 = "Happy " + age + "rd Birthday!"
# print(msg24) - This command gives a type error.
# It means Python can’t recognize the kind of information you’re using.
# When you use integers within strings like this,
# you need to specify explicitly that you want Python to use the integer as a string of characters.
# You can do this by wrapping the variable in the str() function,
# which tells Python to represent non-string values as strings:

msg25 = "Happy " + str(age) + "rd Birthday!"
print(msg25)

# Exercise 2-8:
print(5+3)
print(10-2)
print(4*2)
print(16/2)
# Exercise 2-9:
number = 18
msg29 = "My favourite number is " + str(number) + " because it is my son's birthday."
print(msg29)

# In Python, the hash mark (#) indicates a comment.
# Anything following a hash mark in your code is ignored by the Python interpreter (is not executed).

# Exercise 2-10:
# Dilorom Akhmedjanova 03-05-2021
# str() function tells Python to represent non-string values as strings:
print("My favourite number is " + str(number) + " because it is my son's birthday.")

# The Zen of Python
# The Python community’s philosophy is contained in “The Zen of Python” by Tim Peters.
# Experienced Python programmers will encourage you to avoid complexity and aim for simplicity whenever possible.
# import this - You can access this brief set of principles for writing good Python code by entering import this into your interpreter.s
