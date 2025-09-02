import cv2

some_random_picture=cv2.imread("open_cv.png")

uhh=cv2.medianBlur(some_random_picture,11)

cv2.imshow("idk",uhh)

cv2.waitKey(0)

cv2.destroyAllWindows()