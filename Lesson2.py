import cv2
import numpy as np

umbrella=cv2.imread("Colourful_umbrellas.png")

#Split the image into 3 channels

b,g,r=cv2.split(umbrella)

cv2.imshow("Umbrella blue",b)

cv2.waitKey(0)

cv2.imshow("Umbrella red",r)

cv2.waitKey(0)

cv2.imshow("Umbrella green",g)

cv2.waitKey(0)

cv2.destroyAllWindows()