'''
HOG: The idea is to extract features into a vector , and feed it
into a classification algorithm like a Support Vector Machine for
example that will assess whether a face(or any object you train it to
recognize actually) is present in a region or not
'''
##############################################
# Input -> Gray -> HAAR Cascade -> Face Count
##############################################
import imutils
import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
number = 0
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Hollow Purple.mp4')
while True:
    try:
        ret, img = cap.read()
        img = imutils.resize(img, width=480,inter=cv2.INTER_AREA)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray)
        #print(f'FACES: {faces}')
        if len(faces) == 0:
            print("No faces found")
            cv2.rectangle(img, (0, img.shape[0] -25), (270, img.shape[0]), (255,255,255),-1)
            cv2.rectangle(gray, (0, img.shape[0] -25), (270, img.shape[0]), (255,255,255),-1)
            cv2.putText(img, f'Number of faces detected: 0', (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
            cv2.putText(gray, f'Number of faces detected: 0', (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
        else:
            print(f"Number of faces detected: {faces.shape[0]}")
            number = faces.shape[0]
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
                cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 1)
            cv2.rectangle(img, (0, img.shape[0] -25), (270, img.shape[0]), (255,255,255),-1)
            cv2.rectangle(gray, (0, img.shape[0] -25), (270, img.shape[0]), (255,255,255),-1)
            cv2.putText(img, f'Number of faces detected: {faces.shape[0]}', (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
            cv2.putText(gray, f'Number of faces detected: {faces.shape[0]}', (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
        cv2.imshow('IMG', img)
        cv2.imshow('Gray', gray)
        cv2.waitKey(1)
    except KeyboardInterrupt():
        cv2.destroyAllWindows()

        
