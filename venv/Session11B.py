# file = open("Session11.py", "r") # r -> read mode
file = open("/Users/ishantkumar/Downloads/Session8.py", "r")
fileContent = file.read()
print(fileContent)

print("Re-Read the file !!")
fileContent = file.read()
print(fileContent)

# PS: We cannot re-read the file
#     If you wish to re-read the file close it and re-open it :)

# Close the File Explicitly
file.close()
print("Is file Closed?",file.closed)

file = open("/Users/ishantkumar/Downloads/Session8.py", "r")
fileContent = file.read()
print(fileContent)