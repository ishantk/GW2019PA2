from sklearn import svm

#1. Prepare Your Data | Supervised Learning
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

# Model Creation
model = svm.SVC(gamma='scale')

# Model Training
model.fit(FEATURES, LABELS)

inputSample = [200, 210]
predictedClass = model.predict([inputSample])
print(predictedClass)