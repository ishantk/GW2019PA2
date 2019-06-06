"""
Sequence in Python : Multi Value Container
    List
    Tuple
    Set
    String
    Dictionary

    Operations on Sequence
    1. Concatenation
    2. Repetition
    3. Membership Testing
    4. Slicing
    5. Indexing

"""

students = ["John", "Jennie", "Jim", "Jack", "Joe"]

# students = ("John", "Jennie", "Jim", "Jack", "Joe") -> Tuple
# students = {"John", "Jennie", "Jim", "Jack", "Joe"} -> Set

print(students, type(students))

# 1. Concatenation
print(students + ["Fionna", "George"])
print(students)

print()

#  2. Repetition
print(students * 2)
print(students)

# 3. Membership Testing
print("Fionna" in students)
print("Fionna" not in students)

# 4. Slicing
print(students[1:4]) # 1 included, 4 excluded | begin from 1 less than 4 i.e. 3

# 5. Indexing
print(students[2])

# PS: Sets supports only Membership Testing where List and Tuple supports all operations