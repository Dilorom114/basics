# 04/30/2021
# This file

# Execution
# drive() - we will not have an access to this function yet
# mycar = Car()  # Car is the class, mycar is an object, in this line we are creating an instance of the (instantation)
from classes.cars import Car, ElectricCar

mycar = Car("BMW", "530XI", "black")
yourcar = Car("Lexus", "Lexus IS", "silver")

mycar.get_description()
mycar.drive()
mycar.set_odometer_reader(50)
mycar.set_odometer_reader(25)
mycar.__odo_reader = 20 # this is the direct access to the instance variable
mycar.colorofthecar = "RED" # this is the direct access to the instance variable
mycar.get_description()
# yourcar.do_something()
print("====================================")
yourcar.get_description()
yourcar.drive()
yourcar.set_odometer_reader(30)
yourcar.get_description()






class Car:

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.__odo_reader = 0

    def set_odometer_reader(self, miles):
        if miles > self.__odo_reader:
            self.__odo_reader = miles
        else:
            print("miles cannot be less than odometer has.")

    def drive(self):
        if self.brand.lower() == 'bmw':
            print(f"You are driving FAST car even without DL! isn't it awesome!")
        else:
            print(f"You are driving the car even without DL! isn't it awesome!")

    def do_something(self):
        print(f"I will do something useful.")
        print(f"Let me drive this car")
        self.drive()

    def get_description(self):
        print(f"Model of the car: {self.model}")
        print(f"Color of the car: {self.color}")
        print(f"Brand of the car: {self.brand}")
        print(f"You have {self.__odo_reader} miles on your car")


mycar = Car('BMW', '530xi', 'black')
yourcar = Car('Lexus', 'IS', 'silver')

mycar.get_description()
mycar.drive()
mycar.set_odometer_reader(50)
mycar.get_description()
mycar.set_odometer_reader(25)
mycar.set_odometer_reader(60)
mycar.__odo_reader = 20
mycar.get_description()
mycar.color = 'RED'
mycar.get_description()
print("===================================")
yourcar.get_description()
yourcar.drive()
yourcar.set_odometer_reader(30)
yourcar.get_description()
# yourcar.do_something()

# 04/03/2021
print("-------Electric car instances----------")
# my_ev = ElectricCar('tesla', 'model x', 'blue')
my_ev = ElectricCar('tesla', 'model x', 'blue', 100)
my_ev.drive()
my_ev.get_description()
print('battery size: ', my_ev.battery_size)
# mycar.battery_size  # only child has battery_size attribute, parent does not see that attribute
# Car (state, behaviour) -> ElectricCar(state, behaviour)

# we can create new methods(functions, available to child only
my_ev.get_battery_info()

# we can override the method that parent had (OOPs - Method Overriding)
my_ev.get_description()
mycar.drive()
my_ev.drive()

