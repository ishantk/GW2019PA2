# Explore TensorFlow
# https://www.tensorflow.org/tutorials

import tensorflow as tf
from tensorflow import keras

# Helper Libraries
import numpy as np
import matplotlib.pyplot as plt

print(">> TensorFlow Version:",tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


print("===Training DataSet===")
print(len(train_images))
print(type(train_images))
print("----")
print(len(train_labels))
print(type(train_labels))


print("===Testing DataSet===")
print(len(test_images))
print(type(test_images))
print("----")
print(len(test_labels))
print(type(test_labels))


print("=== Training Image and Label at 0 index ===")
print(train_images[0])
print(train_labels[0])

print()

print("=== Testing Image and Label at 3 index ===")
print(test_images[3])
print(test_labels[3])

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# plt.subplot(2, 4, 1)
# plt.imshow(train_images[0], cmap=plt.cm.gray_r)
# plt.title(class_names[train_labels[0]]) # 9
#
# plt.subplot(2, 4, 2)
# plt.imshow(test_images[3], cmap=plt.cm.gray_r)
# plt.title(class_names[test_labels[3]])  # 1

# plt.show()

# Create Model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(32, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

# Compile Model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

train_images = train_images / 255.0
test_images = test_images / 255.0

# Train Your Model
model.fit(train_images, train_labels, epochs=5)

# Accuracy on Testing DataSet
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

# Predict The Model
predictions = model.predict(test_images)
print(len(predictions)) # 10,000

print(predictions[7])
idx = np.argmax(predictions[7])
print(idx, class_names[idx])

plt.subplot(2, 4, 1)
plt.imshow(test_images[7], cmap=plt.cm.gray_r)
plt.title(class_names[idx])  # 1
plt.show()
