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
    
    # Take a photo of your face, and save It in the "images" folder
    if cv2.waitKey(1) & 0xff == ord('k'):
        setup_face_database(frame, cap, file, imagOrd)
        imagOrd = imagOrd + 1
    if cv2.waitKey(1) & 0xff == ord('q'):
        cv2.destroyWindow('PrtScr')
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
input()

