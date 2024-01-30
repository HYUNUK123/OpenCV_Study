import cv2
import numpy as np

img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

#If pixel value >127, 255  value<127, 0
#If pixel value>threshold_value  value, pixel value<threshold_value  0
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#If pixel value > 127  0, or 255
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#If pixel value > 127  127, or pixel value
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
#If pixel value > 127  pixel value, or 0
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
#If pixel value > 127  0, or pixel value
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('ㄱㅣㅈㅗㄴ', img)
cv2.imshow('Binary', th1)
cv2.imshow('Binary_INV', th2)
cv2.imshow('TRUNC', th3)
cv2.imshow('TOZERO', th4)
cv2.imshow('TOZERO_INV', th5)

cv2.waitKey()
cv2.destroyAllWindow()