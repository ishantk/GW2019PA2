import numpy as np

list1 = [10, 20, 30]
list2 = [
            [10, 20, 30, 40],
            [10, 20, 30, 40],
            [10, 20, 30, 40]
        ]
list3 = [
            [
                [10, 20, 30, 40],
                [10, 20, 30, 40],
                [10, 20, 30, 40]
            ],
            [
                [10, 20, 30, 40],
                [10, 20, 30, 40],
                [10, 20, 30, 40]
            ]
        ]

a1 = np.array(list1)
a2 = np.array(list2)
a3 = np.array(list3)

print(a1)
print(a1.shape)
print(a1.ndim)
print()

print(a2)
print(a2.shape)
print(a2.ndim)
print()

print(a3)
print(a3.shape)
print(a3.ndim)
print()

print(len(a1))
print(len(a2))
print(len(a3))

