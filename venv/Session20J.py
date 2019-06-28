import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]

# List Comprehension
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]


# plt.plot(X, Y1, "b")
# plt.plot(X, Y2, "m")
# plt.plot(X, Y3, "g")

X = [1, 2, 3, 4, 5]

# for n in X:
#     print(n)

# List Comprehension
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

print(X)
print(Y1)
print(Y2)
print(Y3)

# plt.plot(X, Y1)
# plt.plot(X, Y2)
# plt.plot(X, Y3)

# plt.plot(X, Y1, "o")
# plt.plot(X, Y2, "^")
# plt.plot(X, Y3, "D")

plt.plot(X, Y1, ".")
plt.plot(X, Y2, "-.")
plt.plot(X, Y3, ":")


plt.show()
