import matplotlib.pyplot as plt

"""
A = [1, 2, 3, 4, 5]
B = [10, 20, 30, 40, 50]

plt.bar(A, B)
plt.show()
"""

scores = {"virat":82, "rohit":140, "rahul":102, "dhoni":56, "pandya":48}
"""
plt.bar(0, scores["virat"])
plt.bar(1, scores["rohit"])
plt.bar(2, scores["rahul"])
plt.bar(3, scores["dhoni"])
plt.bar(4, scores["pandya"])
"""

for i, key in enumerate(scores):
    # plt.bar(i, scores[key])
    plt.bar(key, scores[key])

plt.xlabel("BatsMen")
plt.ylabel("Scores")
plt.title("WC2019 - India")

plt.show()
