import cv2

cap = cv2.VideoCapture(1) #1 : usb camera

if not cap.isOpened():
    print('Error')
    exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

forc = cv2.VideoWriter_fourcc(*'DIVX')
delay = round(1000/fps)
out = cv2.VideoWriter('output1.avi',forc, fps, (w,h))

if not out.isOpened():
    print('File open failed')
    cap.release()
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    inversed = ~frame
    edge = cv2.Canny(frame, 50, 150)
    edge_color = cv2.cvtColor(edge,cv2.COLOR_GRAY2BGR)
    out.write(frame)

    cv2.imshow('frame',frame)
    cv2.imshow('inversed',inversed)
    cv2.imshow('edge',edge)
    
    if cv2.waitKey(delay) == ord('q'):
        break    
cap.release()
out.release()
cv2.destroyAllWindows()