import matplotlib.pyplot as plt

scores = [26, 33, 100]
domains = ["java", "python", "c++"]

plt.pie(scores, labels=domains)
plt.legend()
plt.show()

# Explore : https://seaborn.pydata.org/