import numpy as np
from CameraManagement.CameraManagerTools import *
from CameraManagement.FrameConfigTools import *

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
file = "./images/test_image"
imagOrd = 1

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
CameraInitSize(ret, cap)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    faces = DetectFace(frame, face_cascade)


    
        
    DisplayFrame(faces, frame, "tekst z bazy" + str(imagOrd))
    
    # Display the resulting frame

    
    if cv2.waitKey(1) & 0xff == ord('k'):
        cv2.imshow('PrtScr', frame)
        imagOrd = imagOrd + 1
        camera_capture = get_image(cap)
        cv2.imwrite(file + str(imagOrd) + ".jpg", camera_capture)
    if cv2.waitKey(1) & 0xff == ord('q'):
        cv2.destroyWindow('PrtScr')
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

