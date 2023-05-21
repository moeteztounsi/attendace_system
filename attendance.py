import cv2
import numpy as np 
import face_recognition

import os 
from datetime import datetime

path = 'ImagesAttendance'
images = []
classNames = []

# this is to loead the images and store them in a list of images
myList = os.listdir(path)
for cls in myList:
    currentImage = cv2.imread(f'{path}/{cls}')
    images.append(currentImage)
    classNames.append(os.path.splitext(cls)[0])


# this is a function to find the encodings of the images 

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


# this is a function to take the attendance 

def markAttendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {dtString}')


def main():
    encodeListKnown = findEncodings(images)
    print('encoding completed -----------')



    cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()
        imgs = cv2.resize(img, (0,0), None,0.25,0.25)
        imgs = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

        faceCurrentFrame= face_recognition.face_locations(imgs)


        encodeCurrentFrame = face_recognition.face_encodings(imgs,faceCurrentFrame)

        for encodeFace, faceLoc in zip(encodeCurrentFrame,faceCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDist = face_recognition.face_distance(encodeListKnown,encodeFace)
            matchIndex = np.argmin(faceDist)


            if matches[matchIndex]:
                name = classNames[matchIndex].upper()  
                #print(name)
                y1,x2,y2,x1 = faceLoc
                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-30),(x2,y2),(0,255,0),cv2.FILLED)

                cv2.putText(img,name,(x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
                markAttendance(name)
        


        cv2.imshow("Webcam",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


