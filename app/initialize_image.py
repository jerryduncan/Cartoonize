from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

#import libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt


img_dir = '/tmp/images/ezekiel.jpg.jpg'  #this accepts the filepath

img_crop = cv2.resize(img_dir, (0,0), fx=0.5, fy=0.5)
img_crop = cv2.pyrDown(img_dir)

num_iter = 5
for _ in range(num_iter):
    img_small = cv2.bilateralFilter(img_small, d=9, sigmaColor=9, sigmaSpace=7)

img_dir = cv2.pyrUp(img_crop)

def rgb_img(img_dir):
    #reads from a BGR image file to a RGB
    img = cv2.imread(img_dir)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def hsv_img(img_dir):
    #reads from a RGB image file to a HSV array
    hsv = cv2.imread(img_dir)
    return cv2.cvtColor(hsv, cv2.COLOR_RGB2HSV)

def img_read(img_dir):
    #reads from a RGB image file to grayscale image array
    rgb = rgb_img(img_dir)
    hsv = hsv_img(img_dir)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    return rgb, hsv, gray

#to display the img from the different color spaces
eze_rgb, eze_hsv, eze_gray = img_read(img_dir)
plt.imshow(eze_rgb)

