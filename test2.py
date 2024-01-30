import cv2

img1 = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed')
    exit()

print('type(img1)', type(img1))
print('img.shape:', img1.shape)
print('img2.shape', img2.shape)
print('img1.dtype', img1.dtype)

h,w = img2.shape[:2]
print('img2 size : {} x {}'.format(w,h))

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.moveWindow('img2', 400,200)
cv2.waitKey()
