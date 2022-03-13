##############################################################
# Input -> Gray Conversion -> Edge 
# Detection -> Morphology -> Contours -> Shape Recognition
##############################################################
import numpy as np
import imutils
import cv2
import time
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Hinokami Dance.mp4')
pTime = 0

while True:
    ret, img = cap.read()
    if not ret:
        break
    img = imutils.resize(img, width=480,inter=cv2.INTER_AREA)
    
    # FPS Calculation
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    canny_edge = cv2.Canny(blur, 150, 200)
    #canny_edge = cv2.Canny(blur, 100, 200)
    #canny_edge = cv2.Canny(blur, 10, 250)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    closed = cv2.morphologyEx(canny_edge, cv2.MORPH_CLOSE, kernel)

    #corners = cv2.cornerHarris(np.float32(blur), 2, 3, 0.04)
    corners = cv2.cornerHarris(np.float32(blur), 2, 3, 0.15)
    dst = cv2. dilate(corners, None)

    cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    triangles=0
    #for t in cnts:
        # approximate the contour
        #perit = cv2.arcLength(t, True)
        #approxt = cv2.approxPolyDP(t, 0.02 * perit, True)
        # if the approximated contour has three points, then the object is triangular.
        #if len(approxt) == 3:
            #cv2.drawContours(img, [approxt], -1, (0, 255, 0), 4)
            #triangles += 1
    # display the output
    #if triangles==0:
        #print ("\nThere isn't any triangular object\n")
    #elif triangles==1:
        #print ("There is "+str(triangles)+" triangular object\n")
    #else:
        #print ("There are "+str(triangles)+" triangular objects\n")
    rectangles = 0
    for r in cnts:
        # approximate the contour
        perir = cv2.arcLength(r, True)
        approxr = cv2.approxPolyDP(r, 0.02 * perir, True)
        # if the approximated contour has four points, then the object is rectangular.
        if len(approxr) == 4:
            cv2.drawContours(img, [approxr], -1, (0, 0, 255), 4)
            rectangles += 1
    # display the output
    if rectangles==0:
        print ("There isn't any rectangular object\n")

    else:
        print ("There are "+str(rectangles)+" rectangular objects\n")
    polygons = 0
##    for p in cnts:
##        # approximate the contour
##        perip = cv2.arcLength(p, True)
##        approxp = cv2.approxPolyDP(p, 0.02 * perip, True)
##        # if the approximated contour has more than four points, then the object is a polygon.
##        if len(approxp) > 4:
##            cv2.drawContours(image, [approxp], -1, (255, 0, 0), 4)
##            polygons += 1
##    # display the output
##    if polygons==0:
##        print ("There isn't any object with more than four in the image.\n")
##    else:
##        print ("There are "+str(polygons)+" object four edges polygon.\n")
    #Calculate the total number of objects
    total = triangles + rectangles +polygons
    #Return the number of objects found:
    if total == 0:
        print ("no object in this image.\n")
    elif total == 1:
        print ("TOTAL OBJECTS:: "+str(total)+"\n")
    else:
        print ("TOTAL OBJECTS::"+str(total)+"\n")
    
    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,0,0), 2)
    cv2.imshow('Original', img)
    cv2.imshow('Gray', gray)
    #cv2.imshow('Blur', blur)
    cv2.imshow('Canny Edge', canny_edge)
    cv2.imshow('closed', closed)
    cv2.imshow('corners', corners)
    cv2.imshow('dst', dst)

    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()