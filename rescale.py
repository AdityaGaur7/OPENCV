import cv2 as cv

# Reading Images
img = cv.imread('Photos/1.png')
cv.imshow('1', img)

#images , videos , live videos
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Only works for live videos
    capture.set(3, width)
    capture.set(4, height)
    
# Reading Videos
capture = cv.VideoCapture('Videos/download.mp4')
while True:
    isTrue, frame = capture.read()
    
    # Break the loop if the video ends or frame is empty
    if not isTrue:
        break
    
    frame_resized = rescaleFrame(frame, scale=0.1)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    # Break the loop if 'q' is pressed
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
capture.release()
cv.destroyAllWindows()