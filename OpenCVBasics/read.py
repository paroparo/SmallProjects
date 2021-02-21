import cv2 as cv

# Rescale Frame
def rescaleFrame(frame, scale = 0.75):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Live Video
    capture.set(3, width)
    capture.set(4, height)


# Reading an image
img = cv.imread('DSC03328.JPG')
cv.imshow('CB', img)
cv.imshow("CB_resized", rescaleFrame(img))
cv.waitKey(0)


# Reading videos
capture = cv.VideoCapture('GX010186.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    # if the letter d is pressed, break out
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
