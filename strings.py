# 03/04/2021

# Strings (str)

fullname = "john doe"
msg = "we are looking at string functions in python."

# Functions available for strings
print(fullname)
print(fullname.upper())
print(fullname.title())
print(msg.replace('.', '!!!!!!'))
print(msg.replace('.', '!!!!!!').title())
print(msg.replace('python', 'java'))
# Boolean values
print(f"fullname.isdigit() >> {fullname.isdigit()}")
print(f"fullname.islower() >> {fullname.islower()}")
print(f"fullname.isupper() >> {fullname.isupper()}")
print(f"FULLNAME.isupper() >> {'FULLNAME'.isupper()}")
print(f"467.isdigit() >> {'467'.isdigit()}")

# Concatenation
msg1 = fullname.title() + ", " + msg
print(msg1)
print(fullname.upper() + ", " + msg)

# working with white spaces in string: \t, \n, etc
print(fullname.upper() + "\n\t\t\t, " + msg)
msg2 = fullname.title() + "\n\t\t\t, " + msg
print(msg2)
print(msg2.replace('\t', ''))
msg3 = "\n\t\t\t" + fullname.title() + ", " + msg
print(msg3)
print(msg3.strip())
print(msg2, msg3)
# strip() used with strings, removes leading and preceding white space.
print(msg3 + '!!!')
print(msg3.strip() + '!!!')

# fstring
msg3 = "\n\t\t\t" + fullname.title() + ", " + msg
msg4 = f"\n\t\t\t {fullname.title()}, {msg}"
# msg3 and msg4 are equivalent
print("fstring")
print(msg3.lstrip())
print(msg4.strip() + '!!!!')

msg = "we are looking at string functions in python."
msg5 = f"{fullname.title()}, {msg}"
print(msg5)

print("Integers:**********")
num = 456
num2 = 600
# print(num..strip()) - strip() is only used for string data type

print(num + num2)
print(num - num2)
print(num * num2)
print(num / num2)
print(f"num + num2 = {num + num2}")
print(f"num - num2 = {num - num2}")
print(f"num * num2 = {num * num2}")
print(f"num / num2 = {num / num2}")

# print("Value of num is : " + num)
# TypeError: can only concatenate str (not "int") to str
# need to use function to convert num to string
print("Value of num is : " + str(num))
# string (expression) - this will convert the data type to str
print("num + num2 = " + str(num+num2))

num3 = "753"  # it is a string(str) not integer (int)
print(f"num + num3 = {num + int(num3)}")
# ctrl + click - will take you where the specific variable is defined

print(f"3**2 = {3**2}")  # 3**2 means 3*3, or square of 3, '**' - exponent

num4 = "45.55"
print(f"num + num4 = {num+float(num4)}")

print(int(45.4988))

# Exercise 2-5:
print("# Exercise 2-5: ")
quote = '\t\t\tAlert Einstein once said, "A person who never made a \n\t\t\tmistake never tried anything new."'
print(quote)

author = "Alert Einstein"
quote1 = f'\t\t\t{author} once said, "A person who never made a \n\t\t\tmistake never tried anything new."'
print(quote1)

# H/w all in chapter 2

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
# Exercise 2-8:
print(5+3)
print(10-2)
print(4*2)
print(int(16/2))
# Exercise 2-9:
number = 18
msg29 = "My favourite number is " + str(number) + " because it is my son's birthday."
print(msg29)
# Exercise 2-10:
# Dilorom Akhmedjanova 03-05-2021
# str() function tells Python to represent non-string values as strings:
print("My favourite number is " + str(number) + " because it is my son's birthday.")


# Pycharm shortcuts:
# Autoformatting: ctrl + command + L

# https://www.integralist.co.uk/posts/data-types-and-data-structures/
# https://towardsdatascience.com/8-common-data-structures-every-programmer-must-know-171acf6a1a42
# Array is a list
