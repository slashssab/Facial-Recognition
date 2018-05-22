import numpy as np
import cv2, os
import pickle
import sqlite3
from PIL import Image
from socialMedia import socialPost
# the function loadUserInformationFromDataBase return all information from database about user

def loadUserInformationFromDataBase(ID):

    # connect with database    

    connectWithDataBase = sqlite3.connect("Face.db");

    # this command select all columns where ID is equals the ID find from picture

    commandSQL = "Select *  From Person Where ID = " + str( ID )

    # this line execute our sql commands

    cursor = connectWithDataBase.execute( commandSQL )

    profile = None

    # in for loop we load every single information

    for row in cursor : 

        profile = row
    
    # for the end we close connection with database and return information about user

    connectWithDataBase.close()

    return profile

detectFace = cv2.CascadeClassifier( 'haarcascade_frontalface_default.xml' )
detectGlasses = cv2.CascadeClassifier('haarcascade_glasses.xml')

cameraVideo = cv2.VideoCapture( 0 )

faceRecognize = cv2.face.LBPHFaceRecognizer_create(); 
verify = "";
faceRecognize.read( "recognizer\\trainningData.yml" )

# we chose a font to display information

font = cv2.FONT_HERSHEY_SIMPLEX

# this loop will be last until you pressed letter 'e'
color = (0, 255, 0)
while( True ):
    
    retval, Picture = cameraVideo.read()

    # we load the picture and we change to other color space ( in our case is a Gray )
   
    grayColor = cv2.cvtColor( Picture, cv2.COLOR_BGR2GRAY )
    
    faces = detectFace.detectMultiScale( grayColor, 1.3, 5 )

    for ( x, y, w, h ) in faces:

        roi_gray = grayColor[y:y+h, x:x+w]
        roi_color = Picture[y:y+h, x:x+w]
        # drow red rectangle

        cv2.rectangle( Picture, ( x, y ), ( x + w, y + h ), color , 2 )
        glasses = detectGlasses.detectMultiScale(roi_gray)

        #for (ex,ey,ew,eh) in glasses:
        #    cv2.putText( Picture,'Glasses: Ok!', ( x, y + h + 150), font, 0.55, ( 0, 255, 0 ), 1 )        

        id, conf = faceRecognize.predict( grayColor[ y: y + h, x: x + w ] )
        
        profile = loadUserInformationFromDataBase( id )

        if (conf>60):
            color = (0, 0, 255)
        else :
            color = (0, 255, 0)

        if( profile != None ) : 
                if cv2.waitKey( 1 ) & 0xFF == ord( 'v' ):  
                        if (conf>60) :
                            verify = "Wasted "                            
                            cv2.imwrite("Intruder.jpg", grayColor[ y: y + h, x: x + w ] )
                            socialPost(open("Intruder.jpg", "rb"))
   
                        else:
                            verify = "Passed "
                            
                cv2.putText( Picture, str( profile[ 1 ] ), ( x, y + h + 30), font, 0.55, ( 0, 255, 0 ), 1 )

                cv2.putText( Picture, str( profile[ 2 ] ), ( x, y + h + 60), font, 0.55, ( 0, 255, 0 ), 1 )

                cv2.putText( Picture, str( profile[ 3 ] ), ( x, y + h + 90), font, 0.55, ( 0, 255, 0 ), 1 )

                cv2.putText( Picture, verify, ( x, y + h + 120), font, 0.55, ( 0, 255, 0 ), 1 )


    cv2.imshow( 'Frame', Picture )

    if cv2.waitKey( 1 ) & 0xFF == ord( 'e' ): 
        break
   

        
cap.release()

cv2.destroyAllWindows()
