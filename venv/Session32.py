"""

    Unsupervised Learning :)

    We have data but no labels (classes)
    eg: we have flowers but we dont have types :)

    Algo : k-means clustering | ML Model

    k denotes number of classes
    k means number of clusters

    Use Case: k = 2

    ----------
    P   X   Y
    ----------
    A   1   1
    B   1   0
    C   0   2
    D   2   4
    E   3   5
    ----------

    Step 1:
    -------
    Assume any 2 random points from dataset which can be centroids of clusters
    eg : A (1, 1) and C(0, 2) are 2 centroids

    Step 2:
    -------
    Calculate Distance of Each Point from these 2 Centroids
    Eucilidean Method : sqrt[ sq(x2-x1) + sq(y2-y1)]

    ----------------------------------------
    P   X   Y       C1(1, 1)     C2(0, 2)
    ----------------------------------------
    A   1   1       0            1.4
    B   1   0       1            2.2
    C   0   2       1.4          0
    D   2   4       3.2          2.8
    E   3   5       4.5          4.2
    ----------------------------------------

    Step 3:
    -------
    Arrange Points as per calculated Distance
    -------------
    P   Near To
    -------------
    A   C1
    B   C1
    C   C2
    D   C2
    E   C2

    Step 4:
    -------
    Calculate New Centroids for New Clusters which are now created
    Calculate Mean for points in the same cluster

    CM1 = (1+1)/2, (1+0)/2
    CM2 = (0+2+3)/3, (2+4+5)/3

    CM1 = (1, 0.5)
    CM2 = (1.7, 3.7)

    Step 5:
    ------
    Re-Calculate Distance of Points from new Centroids

    -------------------------------------
    P   X   Y   CM1(1, 0.5)  CM2(1.7, 3.7)
    -------------------------------------
    A   1   1   0.5         2.8
    B   1   0   0.5         3.8
    C   0   2   1.8         2.4
    D   2   4   3.6         0.4
    E   3   5   4.9         1.8
    -------------------------------------

    Step 6:
    -------
    Arrange Points as per calculated Distance w.r.t new centroids
    -------------
    P   Near To
    -------------
    A   CM1
    B   CM1
    C   CM1
    D   CM2
    E   CM2
    
    Re Compute the new mean and new distances to validate if cluster remains same or changes
    Result should not change 2 times and thereafter we can lock our result

"""

import matplotlib.pyplot as plt

X = [1, 1, 0, 2, 3]
Y = [1, 0, 2, 4, 5]

plt.scatter(X, Y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()