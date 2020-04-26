# KNN Algorithm
# K - Nearest Neighbor
# Unsupervised Learning

import cv2
import numpy as np
from matplotlib import pyplot as plt

# The location of the each data: 25 X 2 and 0 ~ 100 each.
trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
# Each data is 0 or 1
response = np.random.randint(0, 2, (25, 1)).astype(np.float32)

# The value of the red dots is 0.
red = trainData[response.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')

# The value of the red dots is 0.
blue = trainData[response.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')

# (0 ~ 100, 0 ~ 100) Creating one data and up it in this range.
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, response)
ret, results, neighbours, dist = knn.findNearest(newcomer, 3)

# Let if find the three nearest dots and decide its correct position.
print("result : ", results)
print("neighbours :", neighbours)
print("distance: ", dist)

plt.show()