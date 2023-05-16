# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:50:30 2019

@author: yingl
"""

import tensorflow as tf

from tensorflow.keras import datasets, layers, models
import numpy as np
from keras.layers import Dropout

(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1)) # pixel values: 0, 1, 2, ..., 255

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

# Display a gray-scale image
import matplotlib.pyplot as plt
plt.imshow(test_images[19,:,:], cmap='gray', vmin=0, vmax=1)
plt.show()

model = models.Sequential()
# 32: number of filters
# (3,3): filter size
model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1))) 
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.summary()

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=3,batch_size=64) # batch size: default: 32

test_loss, test_acc = model.evaluate(test_images, test_labels)

print(test_acc)

predicted_probability = model.predict(test_images)
y_test_hat = np.argmax(predicted_probability, axis=1)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(test_labels, y_test_hat, labels=range(10))

