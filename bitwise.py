import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
cv.imshow('Blank', blank)


reactangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('Rectangle', reactangle)
cv.imshow('Circle', circle)

#bitwise AND
bitwise_and = cv.bitwise_and(reactangle, circle)
cv.imshow('Bitwise AND', bitwise_and)
#bitwise OR
bitwise_or = cv.bitwise_or(reactangle, circle)
cv.imshow('Bitwise OR', bitwise_or)
#bitwise XOR
bitwise_xor = cv.bitwise_xor(reactangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)
#bitwise NOT
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT', bitwise_not)





img = cv.imread('Photos/1.png')






cv.waitKey(0)




