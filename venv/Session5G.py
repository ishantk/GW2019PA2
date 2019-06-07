employee = {"eid":101, "name":"John", "salary":30000}
print(employee, type(employee))
# eid is key and 101 is value

print(len(employee))
print(max(employee))
print(min(employee))

# Remember, keys cannot be changed, values can be !!
employee["eid"] = 222 # updating value for key
print(employee["eid"])

print(list(employee.items()))
print(list(employee.keys()))
print(list(employee.values()))

keys = list(employee.keys())
print("Keys:",keys)

for key in keys:
    print(key, "=>",employee[key])

# Explore Dictionary of Dictionary
# Explore List of Dictionaries, Set of Lists etc...