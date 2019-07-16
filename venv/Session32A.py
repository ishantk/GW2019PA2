from sklearn.cluster import KMeans

#1. Prepare Your Data | Un-Supervised Learning
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

TARGET_NAMES = ["Car", "Bike"]

# Creating the Model
clusters = 2
model = KMeans(n_clusters=clusters)

# Train the Model
model.fit(FEATURES)

# predictedClasses = model.predict(FEATURES)
# print(predictedClasses)

sampleInput = [1313, 1295]
predictedClass = model.predict([sampleInput])
print(predictedClass)