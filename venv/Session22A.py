import pandas as pd
import numpy as np

n = int(input("How Many odds and evens you wish to see ?"))

oddNums = np.arange(1, n, 2)
evenNums = np.arange(0, n, 2)

data = {
         "odds":oddNums,
         "evens":evenNums
       }

frame = pd.DataFrame(data)
print("-----frame----")
print(frame)

print()

print("------sum------")
print(frame.sum())

print()

print("------std------")
print(frame.std())

print()

print("------max------")
print(frame.max())