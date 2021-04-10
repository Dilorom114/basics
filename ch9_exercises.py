# Exercise 9-1
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

    def set_number_served(self, number):  # Exercise 9-4
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

# Exercise 9-6
class IceCreamStand(Restaurant):
    """Represent a specific type a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'pistachio']

    def describe_flavors(self):
        print(f"This ice cream stand offers following flavors: ")
        for flavor in self.flavors:
            print("\t - " + flavor, end ='\n')
# Exercise 9-1
print("==================== 9-1 =========================")
restaurant_uzbek = Restaurant('karavan', 'uzbek')
print(restaurant_uzbek.restaurant_name.upper())
print(restaurant_uzbek.cuisine_type.upper())
restaurant_uzbek.describe_restaurant()
restaurant_uzbek.open_restaurant()
# Exercise 9-2
print("==================== 9-2 =========================")
restaurant_russian = Restaurant('u teshi', 'russian')
restaurant_italian = Restaurant('delizioso', 'italian')
restaurant_japanese = Restaurant('meshiagare', 'japanese')
restaurant_russian.describe_restaurant()
restaurant_russian.open_restaurant()
restaurant_italian.describe_restaurant()
restaurant_italian.open_restaurant()
restaurant_japanese.describe_restaurant()
restaurant_japanese.open_restaurant()
# Exercise 9-4
print("==================== 9-4 =========================")
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
# Exercise 9-6
print("==================== 9-6 =========================")
ice_cream_stand = IceCreamStand('delizioso gelato', 'italian')
ice_cream_stand.describe_flavors()
ice_cream_stand.set_number_served(56)
ice_cream_stand.open_restaurant()

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
        self.login_attempts = 0

    def describe_user(self):
        """Provide information about a user attributes"""
        print(f"User name: {self.first_name.title()}, {self.last_name.title()}\n"
              f"Age: {self.age}\nLocation: {self.location.title()}\nField: {self.field.title()}")
    def greet_user(self):
        """Display a greeting to a user"""
        print(f"Hello {self.first_name.title() + ' ' + self.last_name.title()}! How are you doing?\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"The number of login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

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


# Exercise 9-3
print("==================== 9-3 =========================")
user1 = User('jane', 'johnson', 45, 'chicago', 'accounting')
user2 = User('michael', 'smith', 35, 'columbus', 'transportation')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

# Exercise 9-5
print("==================== 9-5 =========================")
user1 = User('jane', 'johnson', 45, 'chicago', 'accounting')
user2 = User('michael', 'smith', 35, 'columbus', 'transportation')
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"The login attempt has been reset: {user1.reset_login_attempts()}")

user2.greet_user()
user2.increment_login_attempts()

# Exercise 9-7
print("==================== 9-7 =========================")
admin1 = Admin('sarah', 'connor', 35, 'miami', 'it')
admin1.show_privileges()
admin1.greet_user()
# Exercise 9-8
print("==================== 9-8 =========================")
admin2 = Admin2('george', 'martin', 35, 'miami', 'accounting')
admin2.greet_user()
admin2.privileges.show_privileges()

