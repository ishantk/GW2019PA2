file = open("/Users/ishantkumar/Downloads/Session8.py", "r")

chunkSize = 50

data = file.read(chunkSize)
print(data)

# From Here next 50 characters will be read
data = file.read(chunkSize)
print(data)