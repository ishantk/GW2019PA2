# Dimensionality Reduction
# Drop/Reduce Dimensions of your dataset
# In a way of dropping features/attributes

from sklearn.feature_selection import VarianceThreshold

X = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
        [0, 1, 1],
        [0, 1, 0],
        [0, 1, 1]
    ]

print("===X Before===")
print(X)

reduction = VarianceThreshold(0.8 * (1 - 0.8))
X = reduction.fit_transform(X)
print("===X After===")
print(X)

# https://scikit-learn.org/stable/modules/feature_selection.html#feature-selection

