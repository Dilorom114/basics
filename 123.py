# # for nums in range(1,11):
# #     print(nums, end ='\n')
# #     for val in range(1,11,1):
# #         print(val, end ='\t')
#
# # count = 0
# # for num in range(1, 11):
# #     if num == 10:
# #         print(num * (count + 1))
# #     else:
# #         print(num * (count + 1), end='\t')
#
#
# # for num in range(1, 11):
# #     count = 0
# #     for value in range(1, 11, count+1):
# #         print(value, end='\t')
#
#
# print("What is the answer for 6 x 7 ?")
# answer = int(input("Enter the answer:  "))
# if answer != 42:
#     print("That is not the correct answer. Please try again!")
# else:
#     print("That is right! The answer is 42.")
#
# print("What is the answer for 6 x 7 ?")
# answer = int(input("Enter the answer:  "))
# if answer != 42:
#     print("That is not the correct answer. Please try again!")
#     answer2 = int(input("Enter the answer:  "))
#     if answer2 != 42:
#         print("That is not the correct answer. Please try again!")
#         answer3 = int(input("Enter the answer:  "))
#         if answer3 != 42:
#             print("That is not the correct answer. Game over!")
#         else:
#             print("That is right! The answer is 42.")
#     else:
#         print("That is right! The answer is 42.")
# else:
#     print("Great Job! The answer is 42.")

# active = True
# while active:
#     age = int(input("Enter your age: "))
#     if age < 3:
#         price = 0
#     elif age < 13:
#         price = 10
#     else:
#         price = 15
#     print(f"The cost of their movie ticket is ${price}")
#     repeat = input("Would you like to continue? (yes/no) ")
#     if repeat == "no":
#         active = False
#     elif repeat == "yes":
#         active = True
#     else:
#         print("Please, type 'yes' to continue or 'no' to quit.")


#
# magicians = ['alice', 'david', 'carolina']
# def make_great():
#     magicians2 = []
#     while magicians:
#         magician = magicians.pop()
#         magicians2. append('the Great'+ ' ' + magician.title())
#     print(magicians2)

# make_great()

# magicians = ['alice', 'david', 'carolina']
# def show_magicians():
#     for name in magicians:
#         print(name.title())
# show_magicians()
#
# def make_great():
#     for name in magicians:
#         print('the Great'+ ' ' +name.title())
# make_great()
#
# make_great(magicians[:])


# Exercise 8-7
# def make_album(artist, album, tracks_number =''):
# def make_album(artist, album, tracks_number =0):
#     songs={}
#     songs['artist']= artist
#     songs['album'] = album
#     if tracks_number >0:
#         songs['tracks'] = tracks_number
#     return songs
#
# print(make_album('linkin park', 'meteora', 15))
# print(make_album('tokio hotel', 'schrei'))
# print(make_album('sia', '1000 form of fear', 12))

# class Restaurant():
#     """A class to describe a restaurant"""
#     def __init__(self, restaurant_name, cuisine_type):
#         """Initialize restaurant name, cuisine type attributes"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         """Give information about a restaurant name and its cuisine type"""
#         print(f"This restaurant is called '{self.restaurant_name.title()}' "
#               f"and it is an {self.cuisine_type.title()} kitchen.")
#     def open_restaurant(self):
#         """Announce whether the restaurant is open"""
#         print(f"{self.restaurant_name.title()} is open!")
#
# restaurant_uzbek = Restaurant('karavan', 'uzbek')
# restaurant_russian = Restaurant('u teshi', 'russian')
# restaurant_italian = Restaurant('delizioso', 'italian')
# restaurant_japanese = Restaurant('meshiagare', 'japanese')
# restaurant_uzbek.describe_restaurant()
# restaurant_uzbek.open_restaurant()
# restaurant_russian.describe_restaurant()
# restaurant_russian.open_restaurant()
# restaurant_italian.describe_restaurant()
# restaurant_italian.open_restaurant()
# restaurant_japanese.describe_restaurant()
# restaurant_japanese.open_restaurant()

# Need a functions to give a value to a incupsulated parameter


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

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

print('--------------------------------')
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

# filename = 'ch10/cats.txt'
# with open(filename) as object:
#     for item in object:
#         print(item.strip())


