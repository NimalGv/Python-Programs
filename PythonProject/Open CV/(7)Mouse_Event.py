import  cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
window="draw"
cv2.namedWindow(window)

'''def on_double_click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,255,0),-1)
    if event==cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img, (x, y), 20, (0, 255, 0), -1)


cv2.setMouseCallback(window,on_double_click)'''

draw=False
mode=True
(sx,sy)=(-1,-1)

def draw_shape(event,x,y,flag,param):
    global draw,mode,sx,sy
    if event==cv2.EVENT_LBUTTONDOWN:
        draw=True
        (sx,sy)=x,y
    elif event==cv2.EVENT_MOUSEMOVE:
        if draw:
            if mode:
                cv2.rectangle(img,(sx,sy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),10,(255,0,0),-1)
    elif event==cv2.EVENT_LBUTTONUP:
        draw=False

cv2.setMouseCallback(window,draw_shape)

while(True):
    cv2.imshow(window,img)
    k= cv2.waitKey(1)
    if k==ord('m') or k==ord('M'):
        mode=not mode
    elif k==27:
        break
cv2.destroyWindow(window)