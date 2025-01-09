import cv2 as cv

img = cv.imread('Photos/group.jpg')

cv.imshow('1', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
# cv.imshow('haar', haar_cascade)

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
# scaleFactor=1.1, minNeighbors=3

print(f'Number of faces found = {len(faces_rect)}')
#draw rectangle around the faces
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    # cv.imshow('Rectangle', img)
    # cv.imshow('Rectangle', img)
    def rescale_frame(frame, scale=0.10):
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dimensions = (width, height)
        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

    # Rescale the image
    rescaled_img = rescale_frame(img, scale=0.5)
    cv.imshow('Rescaled Image', rescaled_img)
    
    
    



cv.waitKey(0)