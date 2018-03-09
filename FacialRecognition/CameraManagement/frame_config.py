"""Import modules"""
import cv2

def draw_text(img, text, x, y):
    """Simply draw the text"""
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

def display_frame(faces, frame, text): 
    """Draws a frame with text around the face"""
    for (x, y, w, h) in faces: 
        cv2.rectangle(frame,(x, y),(x + w, y + h),(255, 0, 0), 2)
        draw_text(frame, text, x, y-5)
    cv2.imshow('Camera', frame)
   