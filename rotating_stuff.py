import cv2
#rotation line 3-13
'''qwertyuio=cv2.imread("house.jpg")

qwertyuio=cv2.resize(qwertyuio,(500,500))

(row,column)=qwertyuio.shape[0:2]

matrix=cv2.getRotationMatrix2D((row//2,column//2),180,1)

result=cv2.warpAffine(qwertyuio,matrix,(column,row))

cv2.imshow("Resized rotataed image",result)'''

#edge detection line 16+

akip=cv2.imread("Simba_but_cat.png")

edges=cv2.Canny(akip,100,500)

cv2.imshow("PikA edged",edges)

cv2.waitKey(0)

cv2.destroyAllWindows()