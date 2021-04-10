from ch9_exercises import Restaurant, User
from ch9_exercises import *

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

