import ctypes
import cv2


def get_image(cap_):
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, got_im = cap_.read()
    del retval
    return got_im

def detect_face(frame_, face_cascade_):
    gray = cv2.cvtColor(frame_, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_.detectMultiScale(gray, 1.3, 5)
    return faces

def camera_initSize(ret, cap):
    user32 = ctypes.windll.user32
    ret = cap.set(3, user32.GetSystemMetrics(0))
    ret = cap.set(4, user32.GetSystemMetrics(1))