# data = [1, 2, 3, 4, 5, "John", "Jennie"] # max and min will not work here
data = [1, 2, 3, 5, 4]
# length = len(data)
# print(length)

print("Length",len(data))
print("Max",max(data))
print("Min",min(data))

names = ["John", "Annie", "Bob", "Krish", "George", "Kia"]
print(max(names)) # Krish
print(min(names)) # Annie

print("=======")

for i in range(0,len(names), 2):
    print(names[i])

print("=======")
# Enhanced/ For-Each Loop | Read-Only Loop
for name in names:
    print(name)

print("=======")