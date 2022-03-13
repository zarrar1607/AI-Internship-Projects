############################################################
# Input -> Gray -> Threshold -> Contour -> Dot Count
############################################################
'''
Segmentation Techniques
1. Simple threshold: Where we manually supply parameters to segment the image.
2. Otsu threshold: Attempt to be more dynamic and automatically compute the optimal threshold value based on the input image.
3. Adaptive threshold: Instead of trying to threshold an image globally using a single value, 
                        breaks the image down into smaller pieces, and thresholds each of these pieces separately and individually.
'''
import cv2
img = cv2.imread('white dots.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
th, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
cnts = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
s1 = 2
s2 = 10
xcnts = []
for cnt in cnts:
    if s1 < cv2.contourArea(cnt) < s2:
        xcnts.append(cnt)
cv2.drawContours(img, cnts, -1, (0,255,0), 1)


print(f'White Dots: {len(xcnts)}')
cv2.putText(img, f'White Dots: {len(xcnts)}', (10,40), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,0,255), 2)
cv2.imshow('Thresh', thresh)
cv2.imshow('Gray', gray)
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows