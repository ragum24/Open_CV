import cv2
haar=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face1=cv2.imread("face1.jpg")
face2=cv2.imread("face2.png")
resizee_face1=cv2.resize(face1,(460,460))

#converting into grayscale becasue haarcascade needs images in grayscale :P
gray_ppl=cv2.cvtColor(face2,cv2.COLOR_BGR2GRAY)
gray_yay=cv2.cvtColor(resizee_face1,cv2.COLOR_BGR2GRAY)

#detecting faces: face data will go in a list 
face_data1=haar.detectMultiScale(gray_ppl)
print(face_data1)
for (x,y,w,h) in face_data1:
    cv2.rectangle(face2,(x,y),(x+w,y+h),(224,224,224),5)

face_data2=haar.detectMultiScale(gray_yay) #detectMultiScale = detects objects based on haarcascade classifiers e.g.frontalface
print(face_data2)
for (x,y,w,h) in face_data2:
    cv2.rectangle(resizee_face1,(x,y),(x+w,y+h),(255,255,8),5)

cv2.imshow("faces",resizee_face1) 
cv2.imshow("faced",face2)
cv2.waitKey(0)   
cv2.destroyAllWindows()