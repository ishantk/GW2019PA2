import os # Built In Module

print("CWD:",os.getcwd())
print("Login:",os.getlogin())
print("Process ID:",os.getppid())

print("***************")
pathToDir = "/Users/ishantkumar/Downloads"
pathToFile = "/Users/ishantkumar/Downloads/orders.csv"
print("Is Downloads Existing in the System:",os.path.exists(pathToDir))
print("Is orders.csv Existing in the System:",os.path.exists(pathToFile))


path = "/Users/ishantkumar/Downloads"
# os.mkdir(path)
# print(">> Directory Created")

# os.rmdir(path)
# print(">> Directory Removed")

# Fetch all the files and directories in the mentioned path
files = os.walk(path)
print(type(files))

allFiles = list(files)
for file in allFiles:
    print(file)

# Assignment: Create a File Explorer
#             List all the files as in Documents/Images/Videos

# Assignment : Find all those files which are created more than 1 year ago

