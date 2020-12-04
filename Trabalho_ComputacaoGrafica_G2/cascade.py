import cv2
camera = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_alt.xml")

while True:
    _, frame = camera.read()
    frame = cv2.flip(frame, 1)
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #                                         (Imagem Gray, escala, qt. vizinhos)
    detect = cascade.detectMultiScale(frameGray, 1.1, 5)
    for (x, y, w, h) in detect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("Camera", frame)
    k = cv2.waitKey(60)
    if k == 27:
        break
cv2.destroyAllWindows()
camera.release()
