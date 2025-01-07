import cv2 as cv 

# Reading Images
# img = cv.imread('Photos/1.png')

# cv.imshow('1', img)

# cv.waitKey(0)


# Reading Videos
capture = cv.VideoCapture('Videos/download.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
