# Nome: Alyson Matheus Maruyama Nacimento
# nUSP: 8532269

import numpy as np
import imageio
import matplotlib.pyplot as plt

fileName = str(input()).rstrip()

# reading image files
input_img = imageio.imread(fileName)
method = int(input())
save = int(input())

def t1(image):
  size = image.shape
  imgT = np.zeros(size, dtype=float)
  for x in range(size[0]):
    for y in range(size[1]):
      imgT[x,y] = 255 - float(image[x,y])

  return imgT

def t2(image, c, d):
  size = image.shape
  # imgT will store the transformed Image
  imgT = np.zeros(size, dtype=float)
  # Finding `a` and `b` values (lowest and highest image intensities)
  a = 999
  b = -999
  for x in range(size[0]):
    for y in range(size[1]):
      if image[x,y] > b: b = image[x,y] 
      if image[x,y] <= a: a = image[x,y]

  # Applying Transformation
  for x in range(size[0]):
    for y in range(size[1]):
      imgT[x,y] = (image[x,y] - a) * ((d - c) / (b - a)) + c

  return imgT

def t3(image):
  size = image.shape
  imgT = np.zeros(size, dtype=float)
  # Finding `R` value (highest intensity)
  R = -999
  for x in range(size[0]):
    for y in range(size[1]):
      if image[x,y] >= R: R = image[x,y]

  # Applying Transformation
  for x in range(size[0]):
    for y in range(size[1]):
      imgT[x,y] = 255 * (np.log2(1 + image[x,y]) / np.log2(1 + R))

  return imgT

def t4(image, W, lambd):
  size = image.shape
  imgT = np.zeros(size, dtype=float)
  for x in range(size[0]):
    for y in range(size[1]):
      imgT[x,y] = W * np.power(image[x,y], lambd)

  return imgT

def RSE(m, r):
  error = 0
  size = r.shape
  for i in range(size[0]):
    for j in range(size[1]):
      error += (m[i,j] - r[i,j]) ** 2
  return np.sqrt(error)

# This variable will store the final image
finalImage = None
if method == 1:
  finalImage = t1(input_img)

if method == 2:
  c = int(input())
  d = int(input())
  finalImage = t2(input_img, c, d)



if method == 3:
  finalImage = t3(input_img)


if method == 4:
  W = int(input())
  lambd = float(input())
  finalImage = t4(input_img, W, lambd)


if save == 1:
  imageio.imwrite('output_img.png', finalImage)

# Rounding to 4 decimals
print("%.4f" % RSE(finalImage, input_img))
