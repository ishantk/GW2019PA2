from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# -> Explore this API from sklearn.model_selection import train_test_split

# DataSet
trainingData = [
              [100, 110],
              [120, 150],
              [150, 200],
              [180, 220],
              [1000, 800],
              [1200, 1200],
              [1500, 1400],
              [2000, 1800]
           ]

trainingLabels = [0, 0, 0, 0, 1, 1, 1, 1]

testingData = [
              [1100, 810],          # 1
              [140, 157],           # 0
              [2000, 1800],         # 1
              [150, 200],           # 0
              [190, 230],           # 0
              [1300, 1255],         # 1
              [1500, 1400],         # 1
              [100, 110]            # 0
           ]



# Model Creation
# model = KNeighborsClassifier(n_neighbors=3)
model = DecisionTreeClassifier()
# Model Training
model.fit(trainingData, trainingLabels)

# Model Prediction
# sampleInput = [147, 215]
# predictedClass = model.predict([sampleInput])
# print(">> Predicted Class: ", predictedClass)

predictedLabels = model.predict(testingData)
print(predictedLabels)

accuracy = metrics.accuracy_score(trainingLabels, predictedLabels)
print(">> Accuracy is:",accuracy)