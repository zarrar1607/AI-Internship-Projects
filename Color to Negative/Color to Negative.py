'''
Input -> Gray Conversion -> Red Plane Separation -> Negative
'''
import cv2
import numpy as np
import imutils
import time

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Hinokami Dance.mp4')

'''
There was a change in cv2 library and now you have to specify the video source (for example cv2.CAP_DSHOW on Windows).
'''

pTime = 0

while(1):
    ret, img = cap.read()
    if not ret:
        break
    img = imutils.resize(img, width=480,inter=cv2.INTER_AREA)
    
    # FPS Calculation
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255,0,0), 3)
    
    # Gray Converstion
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Red plane seperation  
    Red_Plane = img[:,:,2] #IMG = BGR => R = img[:,:,2]
    rows, cols = Red_Plane.shape
    negative = np.zeros((rows,cols), dtype= np.uint8)
    minus_ones = np.full((rows,cols),-1)

    #Following 'for loop' is updating each index => decreasing the fps to 1
    #for i in range (0, rows-2):
    #    for j in range(0, cols-2):
    #        negative[i,j] = -1 * Red_Plane[i,j]
    
    #Following 'for loop' is updating each list => fps remains almost same
    for i in range (0, rows-2):
        negative[i] = minus_ones[i] * Red_Plane[i]
        
    # Display
    
    cv2.imshow('Original', img)
    cv2.imshow('Gray', gray)
    cv2.imshow('Red_Plane', Red_Plane)
    cv2.imshow('Negative', negative)
    

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

