import cv2
import numpy
import sys

def code_check(colorcodes):
    for code in colorcodes:
        if code < 0 or code > 255:
            return False
    return True

def input_parse():
    if len(sys.argv) <= 2:
        print('Did not receive enough color commands')
        quit()
    output = []
    for element in sys.argv[1::]:
        color_values = [int(x) for x in element.split(',')]
        output += color_values
    if code_check(output):
        return output
    else: 
        print('Color codes not entered correctly')
        quit()

cap = cv2.VideoCapture(0)

eye_cascade= cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
box_colors = input_parse()
face_color = box_colors[:3:]
eye_color = box_colors[3::]

while(1):
	ret, frame= cap.read()

	gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces= face_cascade.detectMultiScale(gray, 1.3, 5)
	for(x,y,w,h) in faces:
		cv2.rectangle(frame, 
                      (x,y), 
                      (x+w, y+h), 
                      (face_color[0], face_color[1], face_color[2]), 
                      5
                     )
		roi_gray= gray[y:y+h , x:x+w]
		roi_color= frame[y:y+h , x:x+w]
		eyes= eye_cascade.detectMultiScale(roi_gray)
		for(ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, 
                          (ex, ey), 
                          (ex+ew, ey+eh), 
                          (eye_color[0], face_color[1], face_color[2]),
                          2
                         )

	cv2.imshow('frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
