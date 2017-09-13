import numpy as np 
import cv2
import sys

def code_check(colorcodes):
    for code in colorcodes:
        if code < 0 or code > 255:
            return False
    return True

def input_parse():
    if len(sys.argv) <= 3:
        print('Did not receive enough color commands')
        quit()
    output = []
    for element in sys.argv[2::]:
        color_values = [int(x) for x in element.split(',')]
        output += color_values
    if code_check(output):
        return output
    else:
        print('Color codes not entered correctly')


img = cv2.imread(sys.argv[1])
if img is None:
        print('Could not read in the provided image')
        quit()
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
box_colors = input_parse()
face_color= box_colors[:3:]
eye_color = box_colors[3::]

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for(x,y,w,h) in faces:
	img=cv2.rectangle(img, 
                      (x,y), 
                      (x+w, y+h), 
                      (face_color[0], face_color[1], face_color[2]),
                      2
                     )
	roi_gray= gray[y:y+h, x:x+w]
	roi_color= img[y:y+h, x:x+w]
	eyes= eye_cascade.detectMultiScale(roi_gray)
	for(ex, ey, ew, eh) in eyes:
		cv2.rectangle(roi_color,
                      (ex, ey),
                      (ex+ew, ey+eh),
                      (eye_color[0], eye_color[1], eye_color[2]),
                      2
                     )

cv2.imshow('img', img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
