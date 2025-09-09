import cv2

shoop=cv2.imread("moon.png")

line=cv2.line(shoop,(0,0),(629,497),(233,24,255),5)

cv2.imshow("moon_in_half",line)

cv2.waitKey(0)

cv2.destroyAllWindows()