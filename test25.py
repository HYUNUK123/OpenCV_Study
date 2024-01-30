import cv2

def contour():
    img = cv2.imread('111.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #ㅇㅣㅁㅣㅈㅣ ㅇㅣㅈㅣㄴㅎㅗㅏ
    ret, thimg = cv2.threshold(imgray, 127, 255, 0)
    #ㅇㅗㅣㄱㅗㅏㄱㅅㅓㄴ ㅊㅏㅈㄱㅣ
    contours, _ = cv2.findContours(thimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #ㅊㅏㅈㅇㅡㄴ ㅇㅗㅣㄱㅗㅏㄱㅅㅓㄴ ㄱㅡㄹㅣㄱㅣ
    cv2.drawContours(img, contours, -1, (0,0,255),1)

    cv2.imshow('ㅇㅣㅈㅣㄴㅎㅗㅏ',thimg)
    cv2.imshow('ㅇㅗㅣㄱㅗㅏㄱㅅㅓㄴ',img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour()