import cv2

#initiating video capture object
camera=cv2.VideoCapture()#either you can give the location of the video file or you can write "0" to take the video using camera

#checking if the camera is working
if not camera.isOpened():
    print("CAMERA NOT WORKING HELP-")
    exit()

while True:
    #reading each frame at a time
    status,frame=camera.read()#status = true or false, frame = image------no frame, status false
    if not status:
        print("NO FRAME TO SHOW :(")
        break
    cv2.imshow()