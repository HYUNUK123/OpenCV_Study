import cv2
import numpy as np
import matplotlib.pyplot as plt

def grad():
    img = cv2.imread('keyboard.jpg', cv2.IMREAD_GRAYSCALE)

    lap = cv2.Laplacian(img, cv2.CV_64F,ksize=13)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1,0,ksize=7)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0,1,ksize=7)

    plt.subplot(2,2,1), plt.imshow(img, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(2,2,2), plt.imshow(lap, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

    plt.subplot(2,2,3), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

    plt.subplot(2,2,4), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])



    plt.show()

grad()