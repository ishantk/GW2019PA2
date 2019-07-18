import pandas as pd
import matplotlib.pyplot as plt
from skimage import io           # https://scikit-image.org/

table = pd.read_csv("faces/face_landmarks.csv")
print(table)

n = 7

imageName = table.iloc[n, 0]
print(">> Image Name is:",imageName)

landmarks = table.iloc[n, 1:].as_matrix()
print(">> LandMarks")
print(landmarks)


landmarks = landmarks.astype('float').reshape(-1, 2)
print(">> New Landmarks:")
print(landmarks)

path = "faces/{}".format(imageName)
image = io.imread(path)

print(path)
# print(image)
plt.imshow(image)
plt.title(imageName)
plt.scatter(landmarks[:, 0], landmarks[:, 1], s=20, marker=".", c='r')
plt.show()

# Explore further to rescale and random crop with transform module of pytrorch
# https://pytorch.org/tutorials/beginner/data_loading_tutorial.html
