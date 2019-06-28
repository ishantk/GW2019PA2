import matplotlib.pyplot as plt
import numpy as np

X = np.random.randn(50)
print(X)

plt.hist(X, 20)
plt.show()