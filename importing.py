# 03/27/2021 Importing the modules

# import time
from time import *
import sys
from functions.functions_return import *

# import functions.functions_return
# import functions.functions_return as ft   # giving alias name to a function

# time.sleep(5)  # use this is when you 'import time'
sleep(5)  # use this when you 'from time import'
print(sys.platform)

# from functions_return import print_formatted_name - import only this particular function while * imports all the functions from that file


print_formatted_name('dilorom', 'akhmed')
# ft.print_formatted_name('dilorom', 'akhmed')  # when alias name used for an imported function

full_name = get_formatted_name('john', 'doe')
print(full_name)
print(get_formatted_name('jane', 'doe'))

print_formatted_name('ali', 'tehrani')
student = print_formatted_name('baur', 'eskara')
print(f"value of student is: {student}")
print(f"value of student is: {print_formatted_name('baur', 'eskara')}")

print(get_list_of_even_numbers(20))

print_username(['kevin', 'ronaldo', 'roger'])

# Package - specific purpose folder
