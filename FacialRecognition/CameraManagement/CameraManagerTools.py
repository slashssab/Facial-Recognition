import cv2
import ctypes

def get_image(cap):
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = cap.read()
 return im

def DetectFace(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces

def CameraInitSize(ret, cap):
    user32 = ctypes.windll.user32
    ret = cap.set(3, user32.GetSystemMetrics(0))
    ret = cap.set(4, user32.GetSystemMetrics(1))