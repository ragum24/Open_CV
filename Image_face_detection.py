import cv2
haar=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face1=cv2.imread("face1.jpg")
face2=cv2.imread("face2.png")
resizee_face1=cv2.resize(face1,(460,460))

#converting into grayscale becasue haarcascade needs images in grayscale :P
gray_ppl=cv2.cvtColor(face2,cv2.COLOR_BGR2GRAY)

#detecting faces: face data will go in a list 
face_data=haar.detectMultiScale(gray_ppl)
print(face_data)
for (x,y,w,h) in face_data:
    cv2.rectangle(face2,(x,y),(x+w,y+h),(83,28,56),5)

cv2.imshow("faces",resizee_face1)
cv2.imshow("faced",face2)
cv2.waitKey(0)   
cv2.destroyAllWindows()