"""
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

from sklearn.naive_bayes import GaussianNB
# from sklearn.metrics import -> If you wish to check accuracy !!

# 1. Prepare Your Data | Supervised Learning
FEATURES = [
              [100, 110],
              [120, 150],
              [150, 200],
              [180, 220],
              [1000, 800],
              [1200, 1200],
              [1500, 1400],
              [2000, 1800]
           ]

LABELS = [0, 0, 0, 0, 1, 1, 1, 1]
TARGET_NAMES = ["Bike", "Car"]

# 2. Create ML Model
model = GaussianNB() # Object Construction Statement

# 3. Train the Model with DataSet
#    it will also optimize data for us !!
model.fit(FEATURES, LABELS)

# Check Your Model for Prediction !!
sampleInput = [1970, 1818]
predictedClass = model.predict([sampleInput])
print(">> Predicted Vehicle is:",predictedClass)
print(">> Predicted Vehicle is:",predictedClass[0])
print(">> Predicted Vehicle is:",TARGET_NAMES[predictedClass[0]])