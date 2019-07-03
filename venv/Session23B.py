"""

    ML Program:
    1. Representation
    2. Evaluation
    3. Optimization

    Pre-Requisite : We need Data !!
    .csv file
    web scrapping
    list/tuple/set/dictionary etc..

    Data Set: Vehicles
    Bike    0
    Car     1

    In ML we only process mathematical data

    weight      engine      Vehicle
    -------------------------------
    100 kgs     110cc       Bike (0)
    120 kgs     150cc       Bike (0)
    150 kgs     200cc       Bike (0)
    180 kgs     220cc       Bike (0)
    -------------------------------
    1000 kgs    800cc       Car (1)
    1200 kgs    1200cc      Car (1)
    1500 kgs    1500cc      Car (1)
    2000 kgs    1800cc      Car (1)
    -------------------------------
"""

# Classification Problem
# Supervised Learning

from sklearn import tree

# Model : is a proven combination of Representation + Evaluation + Optimization

data = [
          [100, 110],
          [120, 150],
          [150, 200],
          [180, 220],
          [1000, 800],
          [1200, 1200],
          [1500, 1400],
          [2000, 1800]
       ]

labels = [0, 0, 0, 0, 1, 1, 1, 1]

#DecisionTreeClassifier -> Model
# 1. Model Construct
clf = tree.DecisionTreeClassifier()

# 2. Model Train
clf.fit(data, labels)

# Test Data
input = [300, 350]
output = clf.predict([input])
# print(output) -> [0]

if output[0] == 0:
    print(">> Its a Bike")
else:
    print(">> Its a Car")