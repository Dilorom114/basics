# 04/04/2021 Reading a file

# filepath = "data/students.txt"  # relative path to project
filepath = "/Users/Dilorom/dev/basics/data/students.txt"

# # READING FROM FILE
# # Reading an entire file
# with open(filepath) as students:
#     contents = students.read()
#     print(contents)
#
# # Making a List of Lines from a File:
# with open(filepath) as students:
#     lines = students.readline()
#
# print(lines)
# print(lines[0])
# for line in lines:
#     print(line)

with open(filepath, 'a') as students:  # 'a' is for append, that appends the value to the file content, 'w' is for write, that truncate the file and adds new content
    print("writing to the file.. ")
    students.write("Sergey")

with open(filepath, 'r') as students:
    lines = students.readlines()
    print(lines)

print("Program is completed!!")
