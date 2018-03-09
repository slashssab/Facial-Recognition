# Facial-Recognition
Team Project

This project is based on the articles and the repos shown below.

This project gives user a few tools associated directly with FaceID. The main problem is to recognize a face from the current image and classify It. There are some criteria of classification:
- Emotions
- Gender
- Glasses

One of the most interesting problem associated with this program is Machine-Learning. This area of science is used in the program to learn the face form the set of an images. When the program knows the face, and can classify It, we should do something with this fact. We can store data about emotions of the person in a database, we can check if the person wear glases or guess Its gender.In a specified cases the program sends information by the SMS or FB, or display an appropriate statement. 

Mandatory tools:
- numpy
- opencv-python
- opencv-contrib-python
- ctypes
- HaarCascades

>How It works?
1. Check the face form the captured view and save It.
2. The Algotithm learns the face from set of the saved images.
3. The Program indentify the face shown in the current image per declared period (eg. one second).
4. If the face from the captured image is recognized by the program It shows a special statement, and when It's not recognized It sends an information to the administrator by SMS/FaceBook 
>Capturing an image form your camera

There are few lines of code with our own function prepeared for this project. Let's take a look at the code and check how the program works  

```python
from CameraManagement.camera_manager import *
from CameraManagement.frame_config import *
from Teaching.teacher_help import setup_face_database

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
file = "./images/test_image"
imagOrd = 1

#Setup the camera configuration
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
#Set a size of the capuring images 
camera_init_size(ret, cap)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    faces = detect_face(frame, face_cascade)

    # Display the resulting frame
    display_frame(faces, frame, "tekst z bazy"+str(imagOrd))
    
    # Take a photo of your face, and save in the images folder
    if cv2.waitKey(1) & 0xff == ord('k'):
        setup_face_database(frame, cap, file, imagOrd)
        imagOrd = imagOrd + 1
    if cv2.waitKey(1) & 0xff == ord('q'):
        cv2.destroyWindow('PrtScr')
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

```


>Save the images of your face, and force the program to learn It

Based on

- [opencv-face-recognition-python](https://github.com/informramiz/opencv-face-recognition-python) by
[informramiz](https://github.com/informramiz) 
- [HaarCascades](https://github.com/sightmachine/SimpleCV/tree/master/SimpleCV/Features/HaarCascades)
