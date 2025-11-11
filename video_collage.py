import cv2,os
from PIL import Image #pillow library is an image prossesing library

os.chdir("c:\\Users\\ragur\\OneDrive\\Desktop\\Open_CV\\Picture Collage\\collage pics") #chdir=change directory
path="c:\\Users\\ragur\\OneDrive\\Desktop\\Open_CV\\Picture Collage\\collage pics"
num=len(os.listdir("."))#counts how much images there are
print(num)
mean_h=0
mean_w=0
for file in os.listdir("."):#running a loop to acsess every image
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        img=Image.open(os.path.join(path,file))
        width,height=img.size
        print(width,height)
        mean_w=mean_w+width
        mean_h=mean_h+height
#in the end of the for loop, we will get total of all the widths and heights of the images in mean_w and mean_h
mean_w=mean_w//num
mean_h=mean_h//num
print(mean_w)
print(mean_h)