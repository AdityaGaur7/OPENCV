import cv2 as cv 

img = cv.imread('Photos/1.png')
cv.imshow('1', img)

#gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edge cascade 
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow('Dilated', dilated)

#eroding
eroded = cv.erode(dilated, (7, 7), iterations=1)
cv.imshow('Eroded', eroded)

#resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)