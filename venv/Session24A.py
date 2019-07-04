import numpy as np
import matplotlib.pyplot as plt
from scipy import  stats

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

"""
    =================
    EQUATION OF LINE
    =================
    Y = 2.2 + (0.6)X
    =================
"""

data = stats.linregress(X, Y)
print("Slope of Line:",data[0])
print("Interceptor of Line:",data[1])


# We are creating some unseen data points for x
max = np.max(X) + 10
min = np.min(X) - 10

x = np.linspace(min, max, 100)
y = data[1] + data[0] * x

print(x)
print("======")
print(y)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.plot(x, y, color="g", label="Regression Line")
plt.scatter(X, Y, color="r", label="Data Points")
plt.legend()
plt.show()


