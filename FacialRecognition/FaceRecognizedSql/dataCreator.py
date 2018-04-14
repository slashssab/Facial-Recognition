import cv2
import sqlite3

connectWithDataBase = sqlite3.connect('Face.db')

cameraVideo = cv2.VideoCapture(0)

detectFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def CreateNewUser( ID, name, age, gender ):
   
   commandsSQL = connectWithDataBase.cursor()

   # we input a data to data base

   commandsSQL.execute("INSERT INTO Person VALUES ('" + str(ID) + "','" + str(name) + "','" + str(age) + "','" + str(gender) + "')")

   # the line below save the changes ( commit )

   connectWithDataBase.commit()

   # Ater our all changes in database we should close it

   connectWithDataBase.close()
   
        
Id = input("enter your ID: ")

name = input("enter your name: ")

age = input("Enter your age: ")

gender = input(" You're a Male or Female ? : ")

CreateNewUser( Id, name, age, gender )

sampleNumber = 0

# this loop will be last until you pressed letter 'e'

while(True):

    retval, picture = cameraVideo.read()
   
    # we load the picture and we change to other color space ( in our case is a Gray )

    grayColor = cv2.cvtColor( picture, cv2.COLOR_BGR2GRAY )
   
    faces = detectFace.detectMultiScale( grayColor, 1.3, 5 )
   
    for ( x, y, w, h) in faces:
   
        # draw red rectangle on picture 

        cv2.rectangle( picture, ( x, y ) , ( x + w, y + h ), ( 255, 0, 0 ), 2 )        
   
        # incrementing sample number 
   
        sampleNumber += 1
   
        # saving the captured face in the dataset folder
   
        cv2.imwrite("dataSet/User." + Id + '.' + str( sampleNumber ) + ".jpg", grayColor[ y: y + h, x: x + w ] )
   

    # show the video in Frame

    cv2.imshow( 'frame', picture )
   
    # wait for 2 second ( this time we can changed, the value is write in millisecond ! )
   
    if cv2.waitKey(2000) & 0xFF == ord( 'e' ):
   
        break
   
    # break if the sample number is morethan 18
   
    elif sampleNumber > 18 :
   
        break

cameraVideo.release()

cv2.destroyAllWindows()
