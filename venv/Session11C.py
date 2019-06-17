file = open("/Users/ishantkumar/Downloads/Session8.py", "r")

"""
line = file.readline()
print(line)

line = file.readline()
print(line)

# readline reads line by line

"""

lines = file.readlines()
print(type(lines))
# print(lines[0])
# print(lines[len(lines)-1])

# print(lines)

for line in lines:
    print(line)

#  Source Code Analysis
# HW: 1. Read a python file and find number of classes in it
#     2. Find Objects for those classes
#     3. Create a Dictionary where keys will be classes and value will
#        be object count for them
#      {"Student":2, "Customer":0}
#     4. Consider the Comments