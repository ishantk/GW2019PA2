import os # Built In Module

print("CWD:",os.getcwd())
print("Login:",os.getlogin())
print("Process ID:",os.getppid())

print("***************")
pathToDir = "/Users/ishantkumar/Downloads"
pathToFile = "/Users/ishantkumar/Downloads/orders.csv"
print("Is Downloads Existing in the System:",os.path.exists(pathToDir))
print("Is orders.csv Existing in the System:",os.path.exists(pathToFile))


path = "/Users/ishantkumar/Downloads/MyPythonPrograms"
# os.mkdir(path)
# print(">> Directory Created")

# os.rmdir(path)
# print(">> Directory Removed")