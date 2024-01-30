import cv2
import numpy as np

def bluring():
    img = cv2.imread('cat.jpg')

    #ㅍㅣㄱㅅㅔㄹㅇㅡㄹ ㅈㅜㅇㅅㅣㅁㅇㅡㄹㅗ 5x5ㅇㅕㅇㅇㅕㄱㅇㅡㄹ ㅁㅏㄴㄷㅡㄹㄱㅗ
    #ㅇㅣ ㅇㅕㅇㅇㅕㄱㅇㅡㅣ ㅁㅗㄷㅡㄴ ㅍㅣㄱㅅㅔㄹㄱㅏㅂㅅㅇㅡㄹ ㄷㅓㅎㅏㄱㅗ
    #ㄷㅓㅎㅏㄴ ㄱㅏㅂㅅㅇㅡㄹ 25ㄹㅗ ㄴㅏㄴㅜㄱㅗ ㅇㅣ ㄱㅏㅂㅅㅇㅡㄹ ㅈㅜㅇㅅㅣㅁㅍㅣㄱㅅㅔㄹ ㄱㅏㅂㅅㅇㅡㄹㅗ
    imgblu = np.ones((5,5), np.float32)/25
    blur = cv2.filter2D(img, -1, imgblu)

    cv2.imshow('original', img)
    cv2.imshow('blur', blur)

    cv2.waitKey()
    cv2.destroyAllWindow()
bluring()