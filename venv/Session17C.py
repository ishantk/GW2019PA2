# JSON : Java Script Object Notation
# Its a Dictionary in the form of text i.e. String

# import json
import json as js

student = {"roll":101, "name":"John", "age":20}
print(student)
print(type(student))

print()

# Convert Dictionary to JSON
jsonData = js.dumps(student)
print(jsonData)
print(type(jsonData))

print()

# Convert JSON to Dictionary
dictionaryData = js.loads(jsonData)
print(dictionaryData)
print(type(dictionaryData))