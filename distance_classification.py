## import cv2
## import numpy
## import matplotlib pyplot
## import KMeans cluster from sklearn
## import distance from scipy.spatial

import cv2

img = cv2.imread("Plaksha_Faculty.jpg")
template_img = "Dr_Shashi_Tharoor.jpg"
template_img = cv2.imread(template_img)