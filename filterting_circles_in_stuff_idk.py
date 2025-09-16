import cv2

imaehg=cv2.imread("Pika.png")

gray_imaehg=cv2.cvtColor(imaehg,cv2.COLOR_BGR2GRAY)

blarred_imaehg=cv2.blur(gray_imaehg,(3,3))

dect_circles=cv2.HoughCircles(blarred_imaehg,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=40)

print(dect_circles)

