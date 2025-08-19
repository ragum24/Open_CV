import cv2
import numpy as np

c1=np.array([240,110,207])

c2=np.array([179,199,139]) 

image1=np.full((300,300,3),c1,dtype=np.uint8)

image2=np.full((300,300,3),c2,dtype=np.uint8)

#addition=cv2.add(image1,image2)

#subtraction=cv2.subtract(image1,image2)

addition=image1+image2

subtraction=image1-image2

result=np.concatenate((image1,image2,addition,subtraction),axis=1)

print("Addition result is:",addition[0][0])

print("Subtraction result is:",subtraction[0][0])

cv2.imshow("MATHS_with_colours",result)

cv2.waitKey(0)

cv2.destroyAllWindows()