import cv2
import random
import os
os.system('clear')
BC = cv2.CascadeClassifier('PRO-C106-ProjectSolution-main/haarcascade_fullbody.xml')
video = cv2.VideoCapture('PRO-C106-ProjectSolution-main/walking.avi')
while True:
    ret,image = video.read()
    grayS = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    bodys=BC.detectMultiScale(grayS,1.2,3)
    for (x,y,w,h) in bodys:
        cv2.rectangle(image,(x,y),(x+w,y+h),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),2)
        #cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,200),2)
        cv2.imshow('peoplw walk',image)
    if(cv2.waitKey(1)==32):
        break
video.release()
cv2.destroyAllWindows()
