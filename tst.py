import cv2
import numpy as np


img = cv2.imread('5.png')

a = np.mean(np.mean(img[:, 5:20, :], axis=1), axis=-1)

bb = np.mean(img, axis=-1)

for i, num in enumerate(a):
    print(i, num)