import matplotlib.pyplot as plt
import numpy as np

X = np.arange(1, 201)
Y1 = np.sin(X)
Y2 = np.tan(X)

plt.plot(X, Y1)
# plt.plot(X, Y2)
plt.show()