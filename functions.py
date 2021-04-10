# 03/21/2021 Functions
# Functions
# Functions increase reusability.
# Functions need to be defines first and then executed (called).
# When all functions put in one file, it is called modules.
# After the function definition there is a doc string - in 3 consecutive double or single quotes, or just quotes.
# docstring is optional
# Function name always start with lower case, camel case between words in the name
# arguments or parameter interchangeable block

def greet_user():
    """this is a docstring, something that describe the function."""
    print("Hello!!!")

def greet_user_by_name(name):
    """
    It will say hello and use the name entered.
    name is a required, user has to pass to a function
    """
    print(f"Hello, {name.title()}!")

def sum_numbers(num1, num2):
    print(f"sum of {num1} and {num2} is {num2 + num1}")
    print(f"square of the {num2} on is : {num2**2}")

# def describe_pet(pet='dog', pet_name): cannot be - always put required parameter first
def describe_pet(pet_name, pet='dog'):
    """
    :param pet_name:
    :param pet: it is pet type : dog, cat etc, optional param, default is dog
    :return:
    """
    print(f"I have a {pet}, and we call it {pet_name.title()}")


# ***********************************************************
# All executions of the function (Calling the functions)
greet_user()  # this is how you CALL function
greet_user_by_name('ali')  # 'ali' is a parameter, it is a required parameter
# greet_user_by_name()  # expected TypeError bcz no required parameter is entered.
sum_numbers(45, 78)
sum_numbers(-46, 34)
sum_numbers(num2=-46, num1=34)

describe_pet('lazy', 'cat')
describe_pet('Fluffy', 'dog')
describe_pet('Fluffy',)
describe_pet(pet='cat', pet_name='Pretty',)
# describe_pet(pet='snake')  # TypeError: required parameter is missing

# H/w 8-3 -- 8-5

# To define a datatype for a functions parameters:
def multi_num(a: int, b: int):
    c = a * b
    print(f"product of {a} and {b} is {c}.")

def favorite_book(book_title: str):
    print(f"One of my favorite books is '{book_title.upper()}'....")

# Python has four primitive variable types:
# Integers.
# Float.
# Strings.
# Boolean.



