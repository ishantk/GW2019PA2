import pandas as pd
import numpy as np

# arr = np.arange(1, 51, 2)
arr = list(range(1, 51))
print(arr)

series = pd.Series(arr)
print("-------Series--------")
print(series)
print("-------Axes--------")
print(series.axes)
print("-------Values--------")
data = series.values
print(data)
print(type(data))
print("-------head(5)--------")
print(series.head(5))
print("-------tail(5)--------")
print(series.tail(5))