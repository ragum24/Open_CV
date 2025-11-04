import cv2
import numpy as np

image=cv2.imread(r"c:\Users\ragur\OneDrive\Desktop\Open_CV\Cirlce and blob detection\b1.jpg",0)
if image is None:
    print("Error")

params=cv2.SimpleBlobDetector_Params()
#Set area filtering
params.filterByArea=True
params.minArea=100
params.filterByCircularity=True
params.minCircularity=0.9
params.filterByConvexity=True
params.minConvexity=0.2
params.filterByInertia=True #how long something (a blob) is
params.minInertiaRatio=0.01

dectector=cv2.SimpleBlobDetector_create(params)

keypoints=dectector.detect(image)
blank=np.zeros((1,1))
blobs=cv2.drawKeypoints(image,keypoints,blank,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)#(DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)matching all the keypoints until matching blob is found
num_blobs=len(keypoints)
text="Number of Circular Blobs: "+str(num_blobs)
cv2.putText(blobs,text,(20,550),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0),5)

cv2.imshow("blob",blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()