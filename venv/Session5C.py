# Built-Ins on Strings

# Strings are IMMUTABLE : They cannot be changed
name = "Fionna Flynn"
newName = name.upper() # Modification Operation creates a new String in memory
print(name)
print(newName)

quote = "be exceptional"

print("Before:",hex(id(quote)))

quote = quote.capitalize()

print("After:",hex(id(quote)))

print(quote)

names = "John, Jennie, Jim, Jack, Joe"
# idx = names.index("o")
idx = names.index("Jennie")
print(idx)

newNames = names.replace("J","K")
idx = newNames.index("K")
print(newNames)
print(idx)

num = names.count("n", 0, len(names))
print(num)

print()

data = names.split(",")
print(data, type(data))

for n in data:
    print(n.strip())

quote = "Work Hard and get Luckier"
data = quote.split(" ")
print(data, len(data))

# HW: in a string find a word with maximum occurrence

salutation = "Mr."
fname = "George"

name = salutation + fname # Concatenation
print(name)

number = input("Enter a Number: ")

if number.isdigit():
    num = int(number)
    print("You Entered:",num)

songName = "Hello.doc"
if songName.endswith(".mp3"): # startswith
    print("Play audio file")
else:
    print("Invalid file format to be played")

# Explore Other Built ins in String Use . to explore other built ins