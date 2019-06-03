import cv2
#default mode =1
cv2.imshow('window',cv2.imread('F:\\5.Python\\Tutorial\\standard_test_images\\4.1.01.tiff',1))
cv2.waitKey(0)
#Black and white mode =0
cv2.imshow('window',cv2.imread('F:\\5.Python\\Tutorial\\standard_test_images\\4.1.01.tiff',0))
cv2.waitKey(0)
#saves alpha transperancy mode =-1
cv2.imshow('window',cv2.imread('F:\\5.Python\\Tutorial\\standard_test_images\\4.1.01.tiff',-1))
cv2.waitKey(0)
cv2.destroyAllWindows()