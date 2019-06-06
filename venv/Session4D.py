# List -> MUTABLE (We can change data)
names = ["John", "Annie", "Bob", "Krish", "George", "Kia"]
names[0] = "John Watson"
print(names)

# Tuple -> IMMUTABLE (We cannot change data)
moreNames = ("John", "Annie", "Bob", "Krish", "George", "Kia")
# moreNames[0] = "John Watson" # error
# moreNames.append("Sia")
# moreNames.remove("Bob")
print(moreNames)