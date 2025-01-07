import cv2 as cv
import numpy as np 

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# #1. Paint the image a certain color
# blank[100:200] = 0, 255, 0
# cv.imshow('Green', blank)

#2. Draw a Rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

#3. Draw a Circle
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle', blank)

#4. Draw a Line
cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

#5. Write Text
cv.putText(blank, 'Hello, my name is John', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

# Reading Images
# img = cv.imread('Photos/1.png')
# cv.imshow('1', img)

cv.waitKey(0)