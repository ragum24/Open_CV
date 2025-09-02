import cv2

pikachoop=cv2.imread("Pika.png")

border=cv2.copyMakeBorder(pikachoop,1000,1000,1000,1000,cv2.BORDER_REFLECT,value=1)

cv2.imshow("guinea pig",border)

cv2.waitKey(0)

cv2.destroyAllWindows()