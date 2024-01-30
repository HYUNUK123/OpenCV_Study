import cv2
import numpy as np
from matplotlib import pyplot as plt

def tmpMatching():
    img1 = cv2.imread('car_all.jpg', cv2.IMREAD_GRAYSCALE)
    img2 = img1.copy()

    template = cv2.imread('car_number.jpg', cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    method_names = [
        'cv2.TM_CCOEFF_NORMED',
        'cv2.TM_CCORR',
        'cv2.TM_CCORR_NORMED',
        'cv2.TM_SQDIFF',
        'cv2.TM_SQDIFF_NORMED'
    ]

    for method_name in method_names:
        img1 = img2.copy()
        method = eval(method_name)

        try:
            res = cv2.matchTemplate(img1, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        except Exception as e:
            print('Error', method_name, e)
            continue

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img1, top_left, bottom_right, 255, 2)

        # 수정된 부분: 각 매칭 결과를 표시한 후 창을 닫음 
        plt.subplot(121), plt.imshow(res, cmap='gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img1, cmap='gray')
        plt.title('Detect Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(method_name)
        plt.show()
        
tmpMatching()
