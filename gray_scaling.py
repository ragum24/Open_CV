import cv2

pikachuuuuuuu=cv2.imread("Pika.png")

#gray_pika=cv2.cvtColor(pikachuuuuuuu,cv2.COLOR_BGR2GRAY)

print(pikachuuuuuuu.shape)

(row,column)=pikachuuuuuuu.shape[0:2]

for i in range(row):
    for j in range(column):
        pikachuuuuuuu[i,j]=sum(pikachuuuuuuu[i,j]*0.33)

cv2.imshow("pIKa",pikachuuuuuuu)

#cv2.imshow("pika",gray_pika)

cv2.waitKey(0)

cv2.destroyAllWindows()