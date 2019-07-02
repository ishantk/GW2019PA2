import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

table = pd.read_csv("soccerdata.csv")
"""
print(table)
print()
print(table.head(5))
print()
print(table.tail(5))
print()
"""
# print(table["Name"])
# print(table.Name)

"""
print(table.Age)

sns.countplot(x="Age", data=table)
plt.show()
"""

# Use Case:
# Find the GoalKeeper who can stop the shots in best possible ways

# Weight or Bias
w1 = 1
w2 = 2
w3 = 3
w4 = 4

table["Best_GoalKeepers"] = (w1 * table.GK_Positioning + w2*table.GK_Diving + w3*table.GK_Handling + w4*table.GK_Reflexes)
print(table["Best_GoalKeepers"])

sortedData = table.sort_values("Best_GoalKeepers")
# print(sortedData)

print(sortedData.tail(5))