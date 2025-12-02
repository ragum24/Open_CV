import cv2
haar=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face1=cv2.imread("face1.jpg")
face2=cv2.imread("face2.png")
resizee_face1=cv2.resize(face1,(460,460))





cv2.imshow("faces",resizee_face1)
cv2.imshow("faced",face2)
cv2.waitKey(0)
cv2.destroyAllWindows()