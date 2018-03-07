import cv2

def DisplayFrame(faces, frame):
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x + w,y + h),(255,0,0),2)
    cv2.imshow('Camera', frame)