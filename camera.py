import cv2
import time

# 웹캠 화면 크기 설정 (640X480)
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3,wCam) # 가로
cap.set(4,hCam) # 세로
pTime = 0

while True:
    success, img = cap.read()

    # 좌우 반전
    img = cv2.flip(img, 1)

    cTime = time.time()
    fps = 1/((cTime + 0.01)-pTime)
    pTime = cTime

    cv2.putText(img,f'FPS:{int(fps)}',(480,50), cv2.FONT_ITALIC,1,(255,0,0),2)
    cv2.imshow('Hand LiveFeed',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break