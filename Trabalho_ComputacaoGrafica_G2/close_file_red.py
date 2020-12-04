import cv2 as cv
import numpy as np 

camera = cv.VideoCapture(0)


def DetectCloseWindow():
    lower_green = np.array([161, 155, 84], np.uint8)
    upper_green = np.array([179, 255, 255], np.uint8)
    green_mask = cv.inRange(hsv_frame, lower_green, upper_green)
    result = cv.bitwise_and(frame, frame, mask=green_mask)
    frame_gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)


    _, thresh = cv.threshold(frame_gray, 3, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(
        thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)
        area = cv.contourArea(contour)
        if area > 1000:
            cv.putText(frame, "Green detected", (10, 80),
                        cv.FONT_HERSHEY_SIMPLEX, 1, 1)
            cv.destroyAllWindows()
            camera.release()

while True:
    _, frame = camera.read()
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    DetectCloseWindow()
    cv.imshow("Camera", frame)
    key = cv.waitKey(60)
    if key == 27:
        break

cv.destroyAllWindows()
camera.release()

