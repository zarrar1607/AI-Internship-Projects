####################################
# Using Cascade Classifier Dataset
####################################
import numpy as np
import os 
import sys
import time
import imutils
import cv2
#datasets = 'Detected'
#path = os.path.join(datasets)
#(width, height) = (130,100)
fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
pTime = 0

while True:
    # Read
    ret, img = cap.read()
    if not ret:
        break
    img = imutils.resize(img, width=480,inter=cv2.INTER_AREA)
    
    # FPS Calculation
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    # Blurring or Smoothing
    # keep this kernel above a pixel, 
    # add all the 25 pixels below this kernel, 
    # take the average, 
    # and replace the central pixel with the new average value.
    # Basically as the denominator decreases images becomes brighter on a blurred image
    kernel = np.ones((7,7), np.float32)/25
    filter_img = cv2.filter2D(img, -1, kernel)

    # cv.bilateralFilter() is highly effective in noise removal while keeping edges sharp. 
    # But the operation is slower compared to other filters.
    bi_filter_img = cv2.bilateralFilter(filter_img, 9, 75, 75)

    # Gray
    gray = cv2.cvtColor(bi_filter_img, cv2.COLOR_BGR2GRAY)
    
    # Fire Cascade
    # If Fire is found, it returns the positions of detected fire as Rect(x,y,w,h)
    #fire = fire_cascade.detectMultiScale(gray, 1.2, 5)
    fire = fire_cascade.detectMultiScale(gray, 2, 5)
    #roi = str(fire)
    
    for (x, y, w, h) in fire:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        cv2.rectangle(filter_img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        cv2.rectangle(gray, (x,y), (x+w, y+h), (255, 0, 0), 2)
        cv2.rectangle(bi_filter_img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]

        #if roi >= '302 322 61 61':
        #    count = 1
        #    while count < 60:
        #        img_resize = cv2.resize(roi_color, (width, height))
        #        cv2.imwrite('%s/%s.jpg' % (path,count), img_resize)
        #        count += 1
        #    print ('Fire is detected..!')
        #    cv2.imwrite("first.jpg",img)
        cv2.putText(img, 'Fire is detected....!', (150,50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,255), 2)
        print('Fire is detected....!')
        #time.sleep(0.2)
        #    
    # Displays
    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,0,0), 2)
    cv2.imshow('Blurred', filter_img)
    cv2.imshow('Gray', gray)
    cv2.imshow('Bilateral Filtered', bi_filter_img)
    cv2.imshow('Output', img)
    
    # Exit
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

# Clean
cap.release()
cv2.destroyAllWindows()