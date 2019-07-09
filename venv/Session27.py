from sklearn.datasets import load_iris
from sklearn import tree

# 1. Lets Create our DataSet
irisData = load_iris()
print(">>>> IRIS DATA SET >>>>")
print(irisData)
print()

print(">>>> IRIS DATA SET FEATURES >>>>")
print(irisData.data)
print()

print(">>>> IRIS DATA SET LABELS >>>>")
print(irisData.target)
print()

print(">>>> IRIS DATA SET LABEL NAMES >>>>")
print(irisData.target_names)

# 2. Lets Create our Decision Tree ML Model
model = tree.DecisionTreeClassifier()

# 3. Train the Model | Supervised Learning ML
model.fit(irisData.data, irisData.target)

# 4. Test the model for any input data !!
inputSample = [5.5,2.5,4.0,1.3] # -> Versicolor -> 1

predicatedClass = model.predict([inputSample])

print("Type of Flower Predicted is:",predicatedClass)
print("Type of Flower Predicted is:",predicatedClass[0])
print("Type of Flower Predicted is:",irisData.target_names[predicatedClass[0]])

# Create a DataSet of Flu and train your DecisionTreeClassifier with it
# Capture Image of blood report and use pytesseract to extract data and than use it as unputSample

import graphviz # Explore it a bit more !! :)

data = tree.export_graphviz(model, out_file=None)
graph = graphviz.Source(data)
graph.render("IRIS DATA SET DECISION TREE")
graph.view()
