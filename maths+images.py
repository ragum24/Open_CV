import cv2

catttttt=cv2.imread("Simba_but_cat.png")

catttttt=cv2.resize(catttttt,(500,500))

da_moon=cv2.imread("moon.png")

da_moon=cv2.resize(da_moon,(500,500))

add=cv2.addWeighted(catttttt,0.7,da_moon,0.4,0)

subtracttt=cv2.subtract(catttttt,da_moon)

cv2.imshow("Yayayyayayaya",subtracttt)

cv2.waitKey(0)

cv2.imshow("SIMBA",add)

cv2.waitKey(0)

cv2.destroyAllWindows()