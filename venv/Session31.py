from sklearn import svm

# Input Data
X = [[0,0], [1,1]]

# Labels i.e. Classes
Y = [0, 1]

# Model Creation
model = svm.SVC(gamma='scale')

# Model Training
model.fit(X, Y)
# description = model.fit(X, Y)
# print(description)

inputSample = [2, 2]
predictedClass = model.predict([inputSample])
print(predictedClass)