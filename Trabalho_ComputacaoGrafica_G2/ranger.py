import cv2
import numpy as np
cap = cv2.VideoCapture(0)
def nothing(x):
    pass
cv2.namedWindow('result')

# Creating track bar
cv2.createTrackbar('h', 'result', 0, 179, nothing)
cv2.createTrackbar('s', 'result', 0, 255, nothing)
cv2.createTrackbar('v', 'result', 0, 255, nothing)
while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h = cv2.getTrackbarPos('h', 'result')
    s = cv2.getTrackbarPos('s', 'result')
    v = cv2.getTrackbarPos('v', 'result')
    lower = np.array([h, s, v])
    upper = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('result', result)
    k = cv2.waitKey(60)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()