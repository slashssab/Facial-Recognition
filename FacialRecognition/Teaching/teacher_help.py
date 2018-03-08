"""Import modules"""
import cv2
import time
from CameraManagement.camera_manager import get_image

def setup_face_database(frame, cap, file,imagOrd):   
    """Saves captured images to the specified folder"""
    # Take a photo of your face, and save in the images folder
    cv2.imshow('PrtScr', frame)  
    camera_capture = get_image(cap)
    cv2.imwrite(file + str(imagOrd) + ".jpg", camera_capture)
    
