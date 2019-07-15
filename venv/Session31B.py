from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import svm

# flowers = datasets.load_iris()
digits = datasets.load_digits()
print(digits)

print()

print("==Inputs==")
print(digits.images) # print(digits['images'])
print(">> Length of Inputs:",len(digits.images))

print("==Check 1st Image==")
print(digits.images[0])
print(digits.images[0].shape)

print("==Check last Image==")
print(digits.images[-1])
print(digits.images[-1].shape)


"""
plt.subplot(2, 4, 1)
plt.imshow(digits.images[0], cmap=plt.cm.gray_r)

plt.subplot(2, 4, 2)
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r)
"""

"""
for i in range(1, 5):
    plt.subplot(2, 4, i)
    plt.imshow(digits.images[i], cmap=plt.cm.gray_r)

plt.show()
"""

print("===Labels===") # Classes
print(digits.target)
print(">> Length of Inputs:",len(digits.target))

print("==Target Names==")
print(digits.target_names)

# Model Creation
model = svm.SVC(gamma='scale')

# Model Training
model.fit(digits.data, digits.target)

inputSample = digits.data[-1]
predictedClass = model.predict([inputSample])
print(">> Predicted Class:",predictedClass)
plt.subplot(2, 4, 1)
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r)
plt.show()

# Explore Image Classification DataSet :)
# https://gogul09.github.io/software/image-classification-python

# Explore Mathematics Behind SVM
# http://cs229.stanford.edu/notes/cs229-notes3.pdf
# https://www.svm-tutorial.com/2014/11/svm-understanding-math-part-2/#hyperplane-equation