import  cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
window="draw"
cv2.namedWindow(window)

def on_double_click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,255,0),-1)


cv2.setMouseCallback(window,on_double_click)


while(True):
    cv2.imshow(window,img)
    if cv2.waitKey(20)==27:
        break
cv2.destroyWindow(window)