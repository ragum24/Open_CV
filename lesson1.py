import cv2

#pika=cv2.imread("Pika.png")

#pika=cv2.imread("Pika.png",0)


#pika=cv2.imread("Pika.png",cv2.IMREAD_COLOR)

pika=cv2.imread("Pika.png",cv2.IMREAD_GRAYSCALE)

cv2.imshow("Pikachu",pika)

cv2.waitKey(0)

cv2.destroyAllWindows()

