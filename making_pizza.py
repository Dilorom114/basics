import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# The line import pizza tells Python to open the file pizza.py and copy all the functions from it into this program.

import functions.functions_return

print(functions.functions_return.get_list_of_even_numbers(20))

# from chapter8 import describe_city
#
# print(describe_city('khiva', 'uzbekistan'))

from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

from chapter8 import make_sandwich

make_sandwich('cheese')
