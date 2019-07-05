from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd

# Step1 : Prepare Data to train Model
#       : Supervised Learning
table = pd.read_csv("advertising.csv")

# file = open("advertising.csv", "r")
# data = file.readline()
# print(data)

X = table["Radio"].values
Y = table.Sales.values

print("==TV Data==")
print(X)

print("==Sales Data==")
print(Y)

print("==X and Y are 1-D Arrays==")
print(X.shape)
print(Y.shape)

# Change X and Y to 2-D Arrays
X = X.reshape(len(X), 1)
Y = Y.reshape(len(Y), 1)

# Our LinearRegression Model from sklearn will use 2-d array to get trained
print("==X and Y are 2-D Arrays==")
print(X.shape)
print(Y.shape)

# Step 2 : Create the Model
model = LinearRegression() # Python : Object Construction Statement

# Step 3 : Train the Model with Data | Supervised Learning
#          X and Y should be 2-d array :)
model.fit(X, Y)

# Step 4: Test the model by making predictions
# X is original Input and Y1 is Predicted Output
Y1 = model.predict(X)

# Step 5: Evaluate Errors
score = r2_score(Y, Y1)
print("R2 Score is:", score)

slope = model.coef_
interceptor = model.intercept_

print("Slope is:",slope)
print("Interceptor is:",interceptor)

# Y = 7.03259355 + 0.04753664 * X

# Assignment : Choose any batsman/bowler of your choice
#              Predict what will he score against the teams
#              espn-cric-info

