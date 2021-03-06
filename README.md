# EC601 Homework 1

## Objective:
Utilize Github in conjunction with Trello and Slack to effectively complete Homework Assignment 1, in which we explore the various features of OpenCV.

The code in this repo requires the Python version of OpenCV, which can be installed with pip install opencv-python

## Members:
* Shruthi Sivasubramanian (ShruthiSiva) - Repository Creator
* Kevin Chow (CaptainGinyu)
* Michael Graziano (GrazianoMJ)

## filters.py Command Line Format:
python filters.py

Select the desired filter.
This piece of code adds the corresponding filter to a real time video after face detection.
 
## FaceDetect.py Command Line Format:
python FaceDetect.py <*Image_File_Name*> <*Face_Detect_Color*> <*Eye_Detect_Color*>

The italicized fields are outlined below:
* Image_File_Name: Specify the name of the image file you would like to utilize. This image file should be saved within the same directory where FaceDetect.py is stored.
* Face_Detect_Color, Eye_Detect_Color: Specify the Blue, Green, Red (BGR) Code you wish to use for the drawn identification boxes. The BGR Code should be written as three integers between 0 and 255 separated by commas with no spaces (e.g.-255,255,255 would be the BGR code for a white box).

## FaceDetectVideo.py Command Line Format:
python FaceDetectVideo.py <*Face_Detect_Color*> <*Eye_Detect_Color*>

The italicized fields are outlined below:
* Face_Detect_Color, Eye_Dectect_Color: Specify the Blue, Green, Red (BGR) Code you wish to use for the drawn identification boxes. the BGR Code should be written as three integers between 0 and 255 separted by commas with no space (e.g.-255, 255, 255 would be the BGR code for a white box.).

## face_makeover.py Command Line Format:
python face_makeover.py

No additional arguments are needed.  Upon detection of a face, an image of Nicolas Cage will be overlayed onto that face.

## awesome_face.py Command Line Format:
python awesome_face.py

No additional arguments are needed.  Upon detection of a face, that face will be outlined in a cool-looking color.
