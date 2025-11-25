import cv2,os #operating system
from PIL import Image #pillow library is an image prossesing library

path="c:\\Users\\ragur\\OneDrive\\Desktop\\Open_CV\\Picture Collage\\collage pics"
os.chdir(path) #chdir=change directory-----changing current folder

print(os.listdir(".")) # listdir = names of all the files in the current folder as a list 
num=len(os.listdir("."))#counts how much images there are----the dot is the current folder
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

for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): #running a loop to acsess every image
        img=Image.open(os.path.join(path,file))
        resized_image=img.resize((mean_w,mean_h),Image.LANCZOS)
        resized_image.save(file,"JPEG",quality=95) #replaces the previous image with the resized image
        print("File saved successfully!!! oh no...it got deleted :P")

def generate_vid():
    vedio_nama="Guinea_Pigs.avi"
    #os.chdir() = this is what we use to change the location of the video file somewhere else
    images=[]
    for file_name in os.listdir("."):
        if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith("png"): #running a loop to acsess every image
            images.append(file_name)
    
    vid=cv2.VideoWriter(vedio_nama,0,1,(mean_w,mean_h)) #vid=video file
    for image in images:
        vid.write(cv2.imread(os.path.join(".",image))) #running a loop to acsess every image
    print("VIDEO COLLAGE HAD BEEN CREATED.")
    cv2.destroyAllWindows()
    vid.release()
generate_vid()