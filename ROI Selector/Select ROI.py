import cv2
import imutils

img = cv2.imread('Tomioka & Shinobu.png')
#img = imutils.resize(img, width=400,inter=cv2.INTER_AREA)

i = cv2.selectROI(img)
print(i)
crop = img[int(i[1]) : int(i[1] + i[3]),
            int(i[0]) : int(i[0]) + i[2]]    

#cv2.imshow('Original',img)
cv2.imshow('Region Of Intereset',crop)

cv2.waitKey(0)
cv2.destroyAllWindows() 
