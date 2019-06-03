import cv2

for i in range(2):
    img=cv2.imread("F:\\5.Python\\Tutorial\\standard_test_images\\4.1.01.tiff",i)
    outpath="F:\\5.Python\\Tutorial\\Output\\"+str(i)+".jpg"
    cv2.imwrite(outpath,img)
