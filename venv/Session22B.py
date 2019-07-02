import pandas as pd
import numpy as np

# data = np.random.randn(5, 4)
data = np.random.rand(5, 4)
# np.random.randint()

print(data)

frame = pd.DataFrame(data, columns=["COL1", "COL2", "COL3", "COL4"])
print(frame)

# Iterate in DataFrame using function : iteritems
# Within Columns
for key, value in frame.iteritems():
    print("-----------")
    print(key)
    print("-----------")
    print(value)
    print(type(value))
    print("-----------")

# Conclusion : Series is a collection of numpy array
#              DataFrame is a collection of Series

print("@#@#@#@#@#@#@#@#@#@")

# Iterate in DataFrame using function : iterrows
# Within Rows
for key, value in frame.iterrows():
    print("-----------")
    print(key)
    print("-----------")
    print(value)
    print(type(value))
    print("-----------")

print("$%$%$%$%$%$%$%$%$%$%$%")

# Iterate in DataFrame using function : itertuples
# Returns tuples
for row in frame.itertuples():
    print(row)