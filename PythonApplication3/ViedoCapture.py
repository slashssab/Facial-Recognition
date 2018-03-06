
import numpy as np
import ctypes
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
#ret, frame = cap.read()
user32 = ctypes.windll.user32
ret = cap.set(3, user32.GetSystemMetrics(0))
ret = cap.set(4, user32.GetSystemMetrics(1))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x + w,y + h),(255,0,0),2)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xff == ord('k'):
        cv2.imshow('frame1qqq', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

