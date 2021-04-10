# 03/28/2021 Object-oriented Programming Concepts: Class and Object
# What is class and object?
# Class - blueprint or template; consists of functions (action/behavioral), parameters (state)
# Object - instance of class: create a variable and set to a class.
# Class - theory, while object - practice, execution of that theory
# Class is also created the way function is created, but starts with 'class' instead of 'def'
# Class has behavior and state; attributes are state
# Constructer is init method which is hidded/incapsulated

# All class names should be with upper case.
class Car:
    """This class describes model of the car."""
    def __init__(self, brand, model, color):
        self.brandofthecar = brand  # assigning the local brand variable to a global variable (self.brandofthecar)
        self.colorofthecar = color
        self.modelofthecar = model
        self.__odo_reader = 0  # incapsulation

    def set_odometer_reader(self, miles):
        """Function to update the value of the __odo_reader global variable."""
        if miles > self.__odo_reader:
            self.__odo_reader = miles
        else:
            print("miles cannot be less than odometer")

    def drive(self):
        """driving action"""
        if self.brandofthecar.lower() == "bmw":
            print(f"You are driving FAST car even without DL! isn't it awesome ? ")
        else:
            print(f"You are driving the car even without DL! isn't it awesome ? ")

    def do_something(self):
        print("I want to do something .......")
        print("let me drive this car ;) ")
        self.drive()
        # motor = Motorcycle()
        # motor.drive()

    def get_description(self):
        """ """
        # print(f"Brand of the car : )
        print(f"Model of the car: {self.modelofthecar}")
        print(f"Color of the car: {self.colorofthecar}")
        print(f"Model of the car: {self.brandofthecar}")
        print(f"You have {self.__odo_reader} miles on your car.")

# 04/03/2021

class ElectricCar(Car):
    """This is the child class for Car. ElectricCar class inherits from Car class."""
    def __init__(self, brand, model, color, battery_size = 60):
        super().__init__(brand, model, color)
        self.battery_size = battery_size
    #
    # def __init__(self, brand, model, color):
    #     super().__init__(brand, model, color)
    #     self.battery_size = 60

    def get_battery_info(self):
        print(f"This car has a {self.battery_size}--kw battery.")

    def get_description(self):
        super().get_description()
        print(f"Battery size of the car: {self.battery_size}")

    def drive(self):
        print(f"You are driving an EV! It is a way awesome than just a car, maybe")




