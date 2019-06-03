import cv2
import numpy as np

def empty():
    pass

img=np.zeros((512,512,3),np.uint8)
window="Image"
cv2.namedWindow(window)
cv2.createTrackbar("Blue",window,0,255,empty)
cv2.createTrackbar("Green",window,0,255,empty)
cv2.createTrackbar("Red",window,0,255,empty)
while(True):
    cv2.imshow(window, img)
    if cv2.waitKey(1)==27:
        break;
    Blue=cv2.getTrackbarPos("Blue",window)
    Green=cv2.getTrackbarPos("Green",window)
    Red=cv2.getTrackbarPos("Red",window)
    img[:]=[Blue,Green,Red]
    print(Blue,Green,Red)

cv2.destroyWindow(window)