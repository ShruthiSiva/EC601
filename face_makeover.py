import cv2
import numpy as np

nicolas_cage = cv2.imread('nicolas-cage.jpg')
cap = cv2.VideoCapture(0)

eye_cascade= cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(1):
    ret, frame= cap.read()

    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces= face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        resized_nicolas_cage = cv2.resize(nicolas_cage, (w, h))
        frame[y:y+h, x:x+w] = resized_nicolas_cage
    
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    # wait for ESC key to exit
    if k == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
