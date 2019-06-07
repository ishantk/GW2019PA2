A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# C = A | B  # Union
# D = A & B  # Intersection
# E = A - B  # Difference

C = A.union(B)
D = A.intersection(B)
E = A.difference(B)

print(C)
print(D)
print(E)

print(1 in A)


S1 = {1, 2, 3, 'a', 'b', 'c'}
S2 = {1, 3, 'b'}
print(S2.issubset(S1))
print(S1.issubset(S2))
print(S1.issuperset(S2))


