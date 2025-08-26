import cv2

pikachoop=cv2.imread("Pika.png")

import numpy as np

'''kernel=np.ones((5,5),np.uint8)

erode=cv2.erode(pikachoop,kernel

cv2.imshow("Pikaahh",erode)'''

#blur effect :P

#gaussian blur :O

#gaussian=cv2.GaussianBlur(pikachoop,(7,7),0)

girl=cv2.imread("graineh_lady.png")

median=cv2.medianBlur(girl,10)

cv2.imshow("MB",median)

cv2.waitKey(0)

cv2.destroyAllWindows()