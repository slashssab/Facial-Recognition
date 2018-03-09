# Facial-Recognition
Team Project

This project gives user a few tools associated directly with FaceID. The main problem is to recognize a face from the current image and classify It. There are some criteria of classification
- Emotions
- Gender
- Glasses
Mandatory tools
- numpy
- opencv-python
- opencv-contrib-python
- ctypes
- HaarCascades

>How It works?
1. Check the face form the captured view and save It.
2. The Algotithm learns the face from set of the saved images.
3. The Program indentify the face shown in the current image per declared period (eg. one second).
4. If the face from the captured image is recognized by the program It shows a special statement, and when It's not recognized It sends an information to the administrator by SMS/FaceBook 
>Capturing an image form your camera

>Save the images of your face, and force the program to learn It

Based on

- [opencv-face-recognition-python](https://github.com/informramiz/opencv-face-recognition-python) by
[informramiz](https://github.com/informramiz) 
- [HaarCascades](https://github.com/sightmachine/SimpleCV/tree/master/SimpleCV/Features/HaarCascades)
