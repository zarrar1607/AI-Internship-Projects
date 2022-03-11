from collections import deque
import numpy as np
import imutils
import cv2

#====== HSV Ranges & Text Colors =======
lower = {'purple':(135,0,178), 'red':(169,164,0), 'blue':(97,117,10)}
upper = {'purple':(170,255,255), 'red':(179,255,255), 'blue':(127,225,255)}
colors = {'purple':(252 , 53 , 241 ), 'red':(0,0,255), 'blue':(255,0,0)}
#======================================
#========For Images========(Uncommented this)
'''
#img = cv2.imread('Blue-Red.png')
img = cv2.imread('Merge.png')
#img = cv2.imread('Hollow Purple.png')
cv2.imshow("Hollow Purple", img)

img = imutils.resize(img, width=400)
blurred = cv2.GaussianBlur(img, (11,11), 0)
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)
prev_mask = cv2.inRange(hsv, lower['purple'], upper['purple'])
for key, value in upper.items():
    kernel = np.ones((11,11), np.uint8)
    mask = cv2.inRange(hsv, lower[key], upper[key])
    prev_mask = prev_mask + mask
    cv2.imshow('mask',mask)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask - cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_NONE)[-2]
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if radius > 0.5:
            cv2.drawContours(img, cnts, -1, colors[key], 2)
            cv2.drawContours(blurred, cnts, -1, colors[key], 2)
            cv2.putText(img,key, (int(x),int(y)), cv2.FONT_HERSHEY_SIMPLEX,1,colors[key],2) 
            cv2.putText(blurred,key, (int(x),int(y)), cv2.FONT_HERSHEY_SIMPLEX,1,colors[key],2)    
cv2.imshow("prev_mask",prev_mask)
cv2.imshow("blurred", blurred)
cv2.imshow("Hollow Purple", img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
'''
#==========================
#=======For Video==========
cap= cv2.VideoCapture('Hollow Purple.mp4')

out= cv2.VideoWriter('Output.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (400, 224))
out_orginal= cv2.VideoWriter('Orginal.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (400, 224))
out_mask= cv2.VideoWriter('Mask.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (400, 224))
out_blurred= cv2.VideoWriter('Blurred.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (400, 224))
out_hsv= cv2.VideoWriter('HSV.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (400, 224))

while True:
    # grab the current frame
    # if we are viewing a video and we did not grab a frame,
    # then we have reached the end of the video
    grabbed, orginal = cap.read()
    if not grabbed:
        break
    #---------PRE-PROCESSING & HSV-----------
    orginal = imutils.resize(orginal, width=400)
    frame = orginal.copy()
    blurred = cv2.GaussianBlur(frame, (11,11), 0) #Ksize = (11,11)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    # HSV: Hue Staturation Value
    # Constructing a mask for EACH COLOR from dictionary
    prev_mask = cv2.inRange(hsv, lower['purple'], upper['purple'])
    for key, value in upper.items():
        kernel = np.ones((11,11), np.uint8) #Ksize = (11,11)
        mask = cv2.inRange(hsv, lower[key], upper[key])
        prev_mask = prev_mask + mask
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask - cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        #---------CONTOURS----------- Each Contour Color in Dictionary
        # find contours in the mask and initialize the current
        # (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_NONE)[-2]
        
        # If a contour is found then:
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            if radius > 0.5:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.drawContours(frame, cnts, -1, colors[key], 2)
                cv2.drawContours(blurred, cnts, -1, colors[key], 2)
                cv2.putText(frame,key, (int(x),int(y)), cv2.FONT_HERSHEY_SIMPLEX,1,colors[key],2) 
                cv2.putText(blurred,key, (int(x),int(y)), cv2.FONT_HERSHEY_SIMPLEX,1,colors[key],2)      

    #--------SHOW OR DISPLAY---------
    out.write(frame)
    out_orginal.write(orginal)
    out_mask.write(prev_mask)
    out_blurred.write(blurred)
    out_hsv.write(hsv)

    cv2.imshow("Original Video", orginal) 
    cv2.imshow("prev_mask",prev_mask)
    cv2.imshow("blurred", blurred)
    cv2.imshow("HSV", hsv)
    cv2.imshow("Output_Hollow Purple", frame) 

    #-----CLOSE WINDOW------
    key = cv2.waitKey(1) & 0xff
    if key == 27 or key == ord('q'): #ESC
        break

cap.release()
out.release()
out_hsv.release()
out_blurred.release()
out_mask.release()
out_orginal.release()
cv2.destroyAllWindows()
#=======================