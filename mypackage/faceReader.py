import cv2
import os
import imutils

#The testing in this function involves using the webcam, so it will not be deployed on Travis
def generateFace(name):
    """This function reads the person's face and take 100 photos, so the model can be trained with them.

    :param name: Name of the person registered.
    :type name: string

    """
    personName = name
    dataPath = './faces'#Ruta de imagenes
    personPath = dataPath + '/' + personName
    if not os.path.exists(personPath):
        print('Folder created: ',personPath)
        os.makedirs(personPath)
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    # cap = cv2.VideoCapture('Video.mp4')
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') #obtained directly from opencv
    count = 0
    while True:
        
        ret, frame = cap.read()
        if ret == False: break
        frame =  imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converts frame to gray color
        auxFrame = frame.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces: #Creates a frame to take the 100 photos 
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            showFace = auxFrame[y:y+h,x:x+w]
            showFace = cv2.resize(showFace,(150,150),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),showFace)
            count = count + 1 #count of photos
        cv2.imshow('frame',frame)
        k =  cv2.waitKey(1)
        if k == 27 or count >= 100: #Key: Esc
            break
    cap.release()
    cv2.destroyAllWindows()
    return True