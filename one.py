import cv2
import os

import numpy as np
from PIL import Image, ImageDraw

def read_files(relative_path):
    images = []
    files = os.listdir(relative_path)
    files.sort()
    for filename in files:
        img = cv2.GaussianBlur(cv2.cvtColor(cv2.imread(os.path.join(relative_path, filename)), cv2.COLOR_BGR2RGB),
                               (5, 5), 0)
        if img is not None:
            images.append(img)
    return images


def draw_circle():
    image = Image.new('RGB', (200, 200), (150, 150, 150))
    draw = ImageDraw.Draw(image)
    draw.ellipse((0, 0, 200, 200), fill='red', outline='red')
    draw.point((100, 100), 'red')
    draw.pieslice([0, 0, 200, 200], 0, 360, fill=255)
    image.save("circle.png")


def add_circle(image, n, column, dis, fig):
    temp = dis
    while n < image.shape[0]:
        m = column
        while m < image.shape[1]:
            r = image[n][m][0]
            g = image[n][m][1]
            b = image[n][m][0]
            if 170 < r and 170 < g and 170 < b:
                im = Image.fromarray(image)
                im.paste(fig, (m+temp, n))
                image = cv2.cvtColor(np.asarray(im), cv2.COLOR_BGR2RGB)
                temp += 30
                return [image, n + 30, temp]
            m += 1
        n += 1
    return [0, image, 0]


def add_circle_2(image, n, column, dis, fig):
    temp = dis
    while n > 0:
        m = column
        while m > image.shape[1] // 2:
            r = image[n][m][0]
            g = image[n][m][1]
            b = image[n][m][0]
            if 170 < r and 170 < g and 170 < b:
                im = Image.fromarray(image)
                im.paste(fig, (m+temp, n))
                image = cv2.cvtColor(np.asarray(im), cv2.COLOR_BGR2RGB)
                temp += 10
                return [image, n - 32, temp]
            m -= 1
        n -= 1
    return [0, image, 0]


draw_circle()
figure = Image.open('circle.png')
count = 100
row = 60
distance = 30
length = len(read_files("frames"))
figure = figure.resize((40, 40))
cwd = os.getcwd()

for i in range(0, length//2):
    file = read_files("frames")[i]
    img, row, distance = add_circle(file, row, 0, distance, figure)
    os.chdir("Shedegi1")
    cv2.imwrite("image{}.png".format(count), img)
    os.chdir(cwd)
    count += 1

size = read_files("frames")[0].shape
row = size[0] - 1
distance = -200
length = len(read_files("frames"))

for i in range(length//2, length):
    file = read_files("frames")[i]
    img, row, distance = add_circle_2(file, row, size[1] - 1, distance, figure)
    os.chdir("Shedegi1")
    cv2.imwrite("image{}.png".format(count), img)
    os.chdir(cwd)
    count += 1

count = 100
row = 60
distance = 30
length = len(read_files("Shedegi1"))
figure = figure.resize((40, 40))
cwd = os.getcwd()

file = read_files("Shedegi1")[0]
os.chdir("result_multiple")
cv2.imwrite("image{}.png".format(count), cv2.cvtColor(file, cv2.COLOR_BGR2RGB))
os.chdir(cwd)
count += 1

file = read_files("Shedegi1")[1]
os.chdir("result_multiple")
cv2.imwrite("image{}.png".format(count), cv2.cvtColor(file, cv2.COLOR_BGR2RGB))
os.chdir(cwd)
count += 1

for i in range(2, length//2 + 2):
    file = read_files("Shedegi1")[i]
    img, row, distance = add_circle(file, row, 0, distance, figure)
    os.chdir("result_multiple")
    cv2.imwrite("image{}.png".format(count), img)
    os.chdir(cwd)
    count += 1

size = read_files("Shedegi1")[0].shape
row = size[0] - 1
distance = -200
length = len(read_files("Shedegi1"))

for i in range(length//2+2, length):
    file = read_files("Shedegi1")[i]
    img, row, distance = add_circle_2(file, row, size[1] - 1, distance, figure)
    os.chdir("result_multiple")
    cv2.imwrite("image{}.png".format(count), img)
    os.chdir(cwd)
    count += 1
