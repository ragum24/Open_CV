import cv2,os
from PIL import Image #pillow library is an image prossesing library

os.chdir("c:\\Users\\ragur\\OneDrive\\Desktop\\Open_CV\\Picture Collage\\collage pics")
path="c:\\Users\\ragur\\OneDrive\\Desktop\\Open_CV\\Picture Collage\\collage pics"
num=len(os.listdir("."))
print(num)
mean_h=0
mean_w=0
for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        img=Image.open(os.path.join(path,file))
        width,height=img.size
        print(width,height)