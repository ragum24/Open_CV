import cv2

num1=629

num2=497

shoop=cv2.imread("moon.png")

line=cv2.line(shoop,(0,0),(629,497),(233,24,255),5)

rect=cv2.rectangle(shoop,(50,10),(580,480),(90,20,34),5)

circle=cv2.circle(shoop,(num1//2,num2//2),233,(255),5)

text=cv2.putText(shoop,"DA MOOOOONNNN",(45,100),cv2.FONT_HERSHEY_TRIPLEX,2,(21, 120, 1))

cv2.imshow("moon_in_half",rect)

#cv2.imshow("moon",line)

cv2.waitKey(0)

cv2.destroyAllWindows()