johnsAge = 30
print(johnsAge, hex(id(johnsAge)))

jenniesAge = 30
print(jenniesAge, hex(id(jenniesAge)))

del johnsAge

print(jenniesAge)
