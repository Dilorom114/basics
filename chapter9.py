# Chapter 9
# Object-oriented programming is one of the most effective approaches to writing software.
# In object-oriented programming you write classes that represent real-world things and situations, and you create objects based on these classes.
# When you write a class, you define the general behavior that a whole category of objects can have.
# When you create individual objects from the class, each object is automatically equipped with the general behavior; you can then give each object whatever unique traits you desire.
# Making an object from a class is called instantiation, and you work with instances of a class.

# Creating and using a Class
# Creating the Dog Class
# Each instance created from the Dog class will store a name and an age, and we’ll give each dog the ability to sit() and roll_over():
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

# Making an Instance from a Class
# The class Dog is a set of instructions that tells Python how to make individual instances representing specific dogs.
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
# We store that instance in the variable my_dog.

# Accessing attributes
# To access the attributes of an instance, you use dot notation. We access the value of my_dog’s attribute name by writing:
# my_dog.name

# Calling Methods
# After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog.
my_dog.sit()
my_dog.roll_over()
# To call a method, give the name of the instance (in this case, my_dog) and the method you want to call, separated by a dot.

# Creating Multiple Instances
# You can create as many instances from a class as you need, as long as you give each instance a unique variable name or it occupies a unique spot in a list or dictionary.
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

# Exercise 9-1
class Restaurant():
    """A class to describe a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name, cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Give information about a restaurant name and its cuisine type"""
        print(f"This restaurant is called '{self.restaurant_name.title()}' "
              f"and it is the {self.cuisine_type.title()} kitchen.")
    def open_restaurant(self):
        """Announce whether the restaurant is open"""
        print(f"{self.restaurant_name.title()} is open!")

restaurant_uzbek = Restaurant('karavan', 'uzbek')
print(restaurant_uzbek.restaurant_name.upper())
print(restaurant_uzbek.cuisine_type.upper())
restaurant_uzbek.describe_restaurant()
restaurant_uzbek.open_restaurant()

# Exercise 9-2
restaurant_russian = Restaurant('u teshi', 'russian')
restaurant_italian = Restaurant('delizioso', 'italian')
restaurant_japanese = Restaurant('meshiagare', 'japanese')
restaurant_russian.describe_restaurant()
restaurant_russian.open_restaurant()
restaurant_italian.describe_restaurant()
restaurant_italian.open_restaurant()
restaurant_japanese.describe_restaurant()
restaurant_japanese.open_restaurant()

# Exercise 9-3
class User():
    """A class to store a user information"""
    def __init__(self, first_name, last_name, age, location, field):
        """Initialize a user's first name, last name, age, location, field"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.field = field
    def describe_user(self):
        """Provide information about a user attributes"""
        print(f"User name: {self.first_name.title()}, {self.last_name.title()}\n"
              f"Age: {self.age}\nLocation: {self.location.title()}\nField: {self.field.title()}")
    def greet_user(self):
        """Display a greeting to a user"""
        print(f"Hello {self.first_name.title() + ' ' + self.last_name.title()}! How are you doing?\n")

user1 = User('jane', 'johnson', 45, 'chicago', 'accounting')
user2 = User('michael', 'smith', 35, 'columbus', 'transportation')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()


# Working with Classes and Instances
# You can modify the attributes of an instance directly or write methods that update attributes in specific ways.
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# To make the class more interesting, let’s add an attribute that changes over time.
# We’ll add an attribute that stores the car’s overall mileage.

# Setting a Default Value for an Attribute
# If you set a default value for an attribute, you don’t have to include a parameter for that attribute.
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying Attribute Values
# You can change an attribute’s value in three ways: you can change the value directly through an instance, set the value through a method, or increment the value (add a certain amount to it) through a method.
# 1. Modifying an attribute’s Value Directly
# The simplest way to modify the value of an attribute is to access the attribute directly through an instance.
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 2. Modifying an attribute’s Value through a Method/Function
# Instead of accessing the attribute directly, you pass the new value to a method that handles the updating internally.
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

print("-------------------------------------------")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# We can extend the method update_odometer() to do additional work every time the odometer reading is modified.
# Let’s add a little logic to make sure no one tries to roll back the odometer reading:
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

print("-------------------------------------------")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(24)
my_new_car.read_odometer()

# 3. Incrementing an attribute’s Value through a Method
# Sometimes you’ll want to increment an attribute’s value by a certain amount rather than set an entirely new value.
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

print("-------------------------------------------")
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# Exercise 9-4
class Restaurant():
    """A class to describe a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name, cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Give information about a restaurant name and its cuisine type"""
        print(f"This restaurant is called '{self.restaurant_name.title()}' "
              f"and it is the {self.cuisine_type.title()} kitchen.")
    def open_restaurant(self):
        """Announce whether the restaurant is open"""
        print(f"{self.restaurant_name.title()} is open!")
        print(f"{self.number_served} customers have been served today.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

print("=================================================")
restaurant_uzbek = Restaurant('karavan', 'uzbek')
restaurant_uzbek.open_restaurant()
restaurant_uzbek.set_number_served(16)
restaurant_uzbek.open_restaurant()
restaurant_uzbek.increment_number_served(10)
restaurant_uzbek.open_restaurant()
restaurant_italian = Restaurant('delizioso', 'italian')
restaurant_italian.open_restaurant()
restaurant_italian.set_number_served(23)
restaurant_italian.open_restaurant()
restaurant_italian.increment_number_served(7)
restaurant_italian.open_restaurant()

# Exercise 9-5
class User():
    """A class to store a user information"""
    def __init__(self, first_name, last_name, age, location, field):
        """Initialize a user's first name, last name, age, location, field"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.field = field
        self.login_attempts = 0

    def describe_user(self):
        """Provide information about a user attributes"""
        print(f"User name: {self.first_name.title()}, {self.last_name.title()}\n"
              f"Age: {self.age}\nLocation: {self.location.title()}\nField: {self.field.title()}")

    def greet_user(self):
        """Display a greeting to a user"""
        print(f"\nHello {self.first_name.title() + ' ' + self.last_name.title()}! How are you doing?")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"The number of login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

user1 = User('jane', 'johnson', 45, 'chicago', 'accounting')
user2 = User('michael', 'smith', 35, 'columbus', 'transportation')
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"The login attempt has been reset: {user1.reset_login_attempts()}")

user2.greet_user()
user2.increment_login_attempts()

# Inheritance
# If the class you’re writing is a specialized version of another class you wrote, you can use inheritance.
# When one class inherits from another, it automatically takes on all the attributes and methods of the first class.
# The original class is called the parent class, and the new class is the child class.
# The child class inherits every attribute and method from its parent class but is also free to define new attributes and methods of its own.

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# The super() function is a special function that helps Python make connections between the parent and child class.

# Defining Attributes and Methods for the Child Class
# You can add any new attributes and methods necessary to differentiate the child class from the parent class.
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.describe_battery()

# Overriding Methods from the Parent Class
# You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class.
# Say the class Car had a method called fill_gas_tank(). This method is meaningless for an all-electric vehicle, so you might want to override this method:
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

# Now if someone tries to call fill_gas_tank() with an electric car, Python will ignore the method fill_gas_tank() in Car and run this code instead.

# Instances as Attributes
# When modeling something from the real world in code, you may find that you’re adding more and more detail to a class. You can break your large class into smaller classes that work together.
# We might be adding many attributes and methods specific to the electric car’s battery. When we see this happening, we can stop and move those attributes and methods to a separate class called Battery.
class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        range = 0
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar2(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar2('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
print("-------------range---------------------")
my_tesla.battery.get_range()


# Exercise 9-6
class Restaurant():
    """A class to describe a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name, cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Give information about a restaurant name and its cuisine type"""
        print(f"This restaurant is called '{self.restaurant_name.title()}' "
              f"and it is the {self.cuisine_type.title()} kitchen.")
    def open_restaurant(self):
        """Announce whether the restaurant is open"""
        print(f"{self.restaurant_name.title()} is open!")
        print(f"{self.number_served} customers have been served today.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    """Represent a specific type a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'pistachio']

    def describe_flavors(self):
        print(f"This ice cream stand offers following flavors: ")
        for flavor in self.flavors:
            print("\t - " + flavor, end ='\n')

ice_cream_stand = IceCreamStand('delizioso gelato', 'italian')
ice_cream_stand.describe_flavors()
ice_cream_stand.set_number_served(56)
ice_cream_stand.open_restaurant()

# Exercise 9-7
class Admin(User):
    """A class to describe a special kind of user"""
    def __init__(self, first_name, last_name, age, location, field):
        super().__init__(first_name, last_name, age, location, field)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges of the admin user:")
        for privilege in self.privileges:
            print("* " + privilege)

admin1 = Admin('sarah', 'connor', 35, 'miami', 'it')
admin1.show_privileges()
admin1.greet_user()

# Exercise 9-8
class Privileges():
    """Describes privileges of an admin user"""
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Print a statement showing the privileges"""
        print("Privileges of the admin user:")
        for privilege in self.privileges:
            print("* " + privilege)

class Admin2(User):
    """A class to describe a special kind of user"""
    def __init__(self, first_name, last_name, age, location, field):
        super().__init__(first_name, last_name, age, location, field)
        self.privileges = Privileges()

admin2 = Admin2('george', 'martin', 35, 'miami', 'accounting')
admin2.greet_user()
admin2.privileges.show_privileges()

# Exercise 9-9
class Battery2():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        range = 0
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85

class ElectricCar3(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery2()

my_tesla2 = ElectricCar3('tesla', 'model y', 2021)
print(my_tesla2.get_descriptive_name())
my_tesla2.battery.describe_battery()
my_tesla2.battery.get_range()
my_tesla2.battery.upgrade_battery()
my_tesla2.battery.get_range()

# Importing Classes
# Python lets you store classes in modules and then import the classes you need into your main program.
## from file_name import ClassName
# You can store as many classes as you need in a single module, although each class in a module should be related somehow.
# You import multiple classes from a module by separating each class with a comma. Once you’ve imported the necessary classes, you’re free to make as many instances of each class as you need.
## from file_name import ClassName1, ClassName2

# Importing an Entire Module
# You can also import an entire module and then access the classes you need using dot notation.
## import file_name
# We then access the classes we need through the file_name.ClassName syntax.

# Importing All Classes from a Module
## from file_name import *
# With this approach it’s unclear which classes you’re using from the module. If you accidentally import a class with the same name as something else in your program file, you can create errors that are hard to diagnose.

# Importing a Module into a Module
# Sometimes you’ll want to spread out your classes over several modules to keep any one file from growing too large and avoid storing unrelated classes in the same module.
# For example, you can store the Car class in one module and and the ElectricCar and Battery classes in a separate module.
# The class ElectricCar needs access to its parent class Car, so we import Car directly into the module:
# from file_name import Car
# After we we can import from each module separately and create whatever kind of car we need:
# from file_name import Car
# from file_name2 import ElectricCar
# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())

