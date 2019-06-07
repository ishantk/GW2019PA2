name = "John Watson"
print(name, type(name))
print(len(name))

print(name[0])
print(name[len(name)-1])
print(name[5:9]) # Wats

print("W" in name)

email = "john@example.com"

if ("@" in email) and ("." in email):
    print("Valid Email")
else:
    print("Invalid Email")

name = "JohnWatson"
print("Max:",max(name))
print("Min:",min(name))

# Create a Program to test a member in a sequence
# Your program should work on List, Tuple and String