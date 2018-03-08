import cv2
import time
from CameraManagement.camera_manager_tools import get_image

def setup_face_database(frame, cap, file,imagOrd):   
    # Take a photo of your face, and save in the images folder
    cv2.imshow('PrtScr', frame)  
    camera_capture = get_image(cap)
    cv2.imwrite(file + str(imagOrd) + ".jpg", camera_capture)
    
