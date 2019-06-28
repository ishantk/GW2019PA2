import pandas as pd

numbers = [10, 20, 30, 40, 50]
ages = {"John":30, "Jennie":26, "Jim":12, "Jack":22, "Joe":33}

S1 = pd.Series(numbers)
S2 = pd.Series(ages)

print(S1)
print()
print(S2)

print("----------")

# Access Elements in Series by indexing
print(S1[1])
print(S2["John"])

# Slicing in Series
print(S1[1:])
print(S1[:3])
print(S1[2:4])

print("----------")

print(S2["Jennie":])
print(S2[:"Jim"])
print(S2["Jennie":"Joe"])