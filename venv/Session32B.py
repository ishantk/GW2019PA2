from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

irisData = load_iris()
FEATURES = irisData.data

print(FEATURES)

model = KMeans(n_clusters=3)
model.fit(FEATURES)

# predictedClasses = model.predict(FEATURES)
# print(predictedClasses)

sampleInput = [6.2, 3.4, 5.4, 2.3]
predictedClasses = model.predict([sampleInput])
print(predictedClasses)
