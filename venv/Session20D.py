import pandas as pd

table = pd.read_csv("CityTemps.csv")
print(table)

print("======")

print(table["Ludhiana"])

print("===3===")

print(table.iloc[3])

print("===3:9===")

print(table.iloc[3:9])

print("===Head 5===")
print(table.head(5))

print("===Tail 5===")
print(table.tail(5))