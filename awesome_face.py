import cv2
import numpy as np

cap = cv2.VideoCapture(0)

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 7)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for(x,y,w,h) in faces:
        roi_gray_blur = gray_blur[y:y+h, x:x+w]
        edge = cv2.adaptiveThreshold(roi_gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        edge[np.where(edge == [0])] = [100]
        
        frame[y:y+h, x:x+w] = cv2.bitwise_and(cv2.cvtColor(edge, cv2.COLOR_GRAY2RGB), frame[y:y+h, x:x+w])
                    
        
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    # wait for ESC key to exit
    if k == 27:
        cv2.destroyAllWindows()
        cap.release()
        break
