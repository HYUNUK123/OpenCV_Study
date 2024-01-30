import cv2

cap = cv2.VideoCapture('scene.mp4')

if cap.isOpened() == False:
    print("Error")
    exit()
while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        edge = cv2.Canny(frame, 50, 150)

        inversed = ~frame

        cv2.imshow('Frame', frame)
        cv2.imshow('inversed', inversed)
        cv2.imshow('edge', edge)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()