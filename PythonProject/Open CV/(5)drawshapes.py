import cv2
import numpy as n

img=n.zeros((512,512,3),n.uint8)
cv2.circle(img,(256,256),120,(256,0,0),-1)
cv2.line(img,(200,300),(300,300),(0,256,0),3)
cv2.rectangle(img,(170,200),(200,210),(0,0,256),-1)
cv2.rectangle(img,(330,200),(300,210),(0,0,256),-1)
cv2.putText(img,"Hello There!",(170,270),cv2.FONT_HERSHEY_SIMPLEX,1,(256,124,60),3)
cv2.imshow("Image",img)
cv2.imwrite("F:\\5.Python\\Tutorial\\Output\\Drawing.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()