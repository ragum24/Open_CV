import cv2

house=cv2.imread("House.jpg")

planet=cv2.imread("Planet.jpg")

sum=cv2.addWeighted(house,0.7,planet,0.4,0)

cv2.imshow("Houseplanet",sum)

cv2.waitKey(0)

cv2.destroyAllWindows()