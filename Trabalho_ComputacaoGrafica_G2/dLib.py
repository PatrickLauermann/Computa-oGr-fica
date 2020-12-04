# Dlib - pip install dlib
# Imutils - pip intall imutils
# Scipy - pip install scipy

import cv2
import dlib
import numpy as np
from imutils import face_utils

camera = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(
    'models/shape_predictor_68_face_landmarks.dat')

while True:
    _, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 1)

    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        # face_utils.rect_to_bb() é a mesma função do cv2.BoundingRect()
        (x, y, w, h) = face_utils.rect_to_bb(face)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        for (x, y) in shape:
            cv2.circle(frame, (x, y), 1, (0, 255, 0),3)

    cv2.imshow("Camera", frame)
    k = cv2.waitKey(60)
    if k == 27:
        break

cv2.destroyAllWindows()
camera.release()
