import cv2
import numpy as np

KNOWN_WIDTH = 14.0  # cm (example: width of object)
FOCAL_LENGTH = 615  # determined by calibration

def distance_to_camera(knownWidth, focalLength, perWidth):
    return (knownWidth * focalLength) / perWidth

cap = cv2.VideoCapture(0)
object_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects = object_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in objects:
        distance = distance_to_camera(KNOWN_WIDTH, FOCAL_LENGTH, w)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"{distance:.2f} cm", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Camera Distance Detection", frame)
    if cv2.waitKey(1) == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
