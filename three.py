import os
import cv2
import matplotlib.pyplot as plt
import numpy as np




def read_files(relative_path):
    images = []
    for filename in os.listdir(relative_path):
        img = cv2.GaussianBlur(cv2.cvtColor(cv2.imread(os.path.join(relative_path, filename)), cv2.COLOR_BGR2GRAY),
                               (5, 5), 0)
        if img is not None:
            images.append(img)
    return images


image = read_files("frames")[0]
result1 = np.zeros((image.shape[0], image.shape[1]))
result2 = np.zeros((image.shape[0], image.shape[1]))
result3 = np.zeros((image.shape[0], image.shape[1]))
result4 = np.zeros((image.shape[0], image.shape[1]))
result5 = np.zeros((image.shape[0], image.shape[1]))
result6 = np.zeros((image.shape[0], image.shape[1]))

for i in range(0, image.shape[0]):
    for j in range(1, image.shape[1]-1):
        result1[i][j] = (image[i][j-1] + image[i][j+1]) / 2

plt.imshow(result1)
plt.show()

for i in range(0, image.shape[0]):
    for j in range(2, image.shape[1]-2):
        result2[i][j] = (8*image[i][j+1] - 8 * image[i][j-1] - image[i][j+2] + image[i][j-2]) / 12

plt.imshow(result2)
plt.show()

for i in range(0, image.shape[0]):
    for j in range(1, image.shape[1]-1):
        result3[i][j] = (image[i][j+1] - 2 * image[i][j] + image[i][j-1]) / 2

plt.imshow(result3)
plt.show()

for i in range(0, image.shape[0]):
    for j in range(2, image.shape[1]-2):
        result4[i][j] = (16*image[i][j+1] - 30*image[i][j] + 16 * image[i][j-1] - image[i][j+2] - image[i][j-2]) / 12

plt.imshow(result4)
plt.show()

for i in range(0, image.shape[0]):
    for j in range(2, image.shape[1]-2):
        result5[i][j] = image[i][j+2] + image[i][j-2]+6*image[i][j]-4*image[i][j+1]-image[i][j-1]

plt.imshow(result5)
plt.show()

for i in range(0, image.shape[0]):
    for j in range(3, image.shape[1]-3):
        result6[i][j] = 2*image[i][j+2] + 2 * image[i][j-2] - 1/6 * image[i][j+3] - 1/6 * image[i][j-3] - 13/2 * image[i][j+1] - 13/2*image[i][j-1] + 28/3 * image[i][j]
plt.imshow(result6)
plt.show()
