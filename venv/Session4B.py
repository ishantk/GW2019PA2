technologies = ["AI", "Android", "Hadoop", "JEE"]
technologies[1] = "Mobile Applications" # Update Index #1
print(technologies)

print()

del technologies[1]

print(technologies)
print(technologies[1])

print(technologies[-1]) # from the end

print()

data = [1, 2, 3, 4, 5, "John", "Jennie", "Jim", "Jack", "Joe"]
data.pop(3)     # removing index
print(data)

data.remove(3)  # removing element
print(data)

names = ["John", "Jennie", "Jim", "Jack", "Joe", "John", "Sia"]
names.remove("John")
print(names)
names.remove("John")
print(names)
