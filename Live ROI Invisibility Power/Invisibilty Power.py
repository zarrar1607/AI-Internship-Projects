from typing import final
import cv2
import numpy as np
import time
import imutils

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
pTime = 0

#-----For Collecting 60 frames initially/Pre-processing-----
print('Pre-processing......')
time.sleep(1)
count = 0
background = 0
for i in range(60):
    ret, background = cap.read()
    if not ret:
        continue
background = np.flip(background, axis= 1)
print('Done!!!')

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    img = imutils.resize(img, width=480,inter=cv2.INTER_AREA)
    background = imutils.resize(background, width=480,inter=cv2.INTER_AREA)
    # FPS Calculation
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime


    count = count + 1
    img = np.flip(img, axis = 1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #--------------------------------------------
    #lower_red = np.array([100, 40, 40])
    #upper_red = np.array([100, 255, 255])
    #mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_blue = np.array([89,81,0])
    upper_blue = np.array([100, 255,113])
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)

    #lower_red = np.array([155,  40, 40])
    #upper_red = np.array([180, 255, 255])
    #mask2 = cv2.inRange(hsv, lower_red, upper_red)
    lower_blue = np.array([100, 81,0])
    upper_blue = np.array([153,255,113])
    mask2 = cv2.inRange(hsv, lower_blue, upper_blue)
    #--------------------------------------------
    
    mask1 = mask1 + mask2
    kernel = np.ones((3,3), dtype= np.uint8)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel, iterations= 1)
    mask1 = cv2.dilate(mask1, kernel, iterations= 1)
    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask= mask1)
    res2 = cv2.bitwise_and(img, img, mask= mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    #cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,0,0), 2)
    cv2.imshow('Original', img)
    cv2.imshow('Background', background)
    #cv2.imshow('HSV', hsv)
    cv2.imshow('Mask 1', mask1)
    cv2.imshow('Mask 2', mask2)
    cv2.imshow('Invisible', final_output)

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()