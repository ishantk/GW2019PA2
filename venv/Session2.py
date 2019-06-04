# 1. Creation of Storage Container | SVC
instagramUserName = "auribises"
johnsAge = 22
time = 10

# 2. Update Operation in Storage Container
johnsAge = 28
time = 11

# 3. Delete Operation
# del instagramUserName

# 4. Read Storage Containers
print(instagramUserName)
print(johnsAge)
print(time)

# 5. Explore Memory for Containers
# id of a storage container is known as HashCode
# print(id(instagramUserName))
print(hex(id(instagramUserName)))
# print(oct(id(instagramUserName)))
# print(bin(id(instagramUserName)))

print(hex(id(johnsAge)))
print(hex(id(time)))

# PS:  When program will be executed, our program will have RAM associated with it
# instagramUserName, johnsAge and time are REFERENCE VARIABLES
# Reference Variable will contain HashCode of Data
