import cv2
import os

def recognizeFace():
    """This function executes a script to use the trained model and and actual footage of the person who wants to Log In.
       It compares the input and output from the trained model and gives the name (if found) of the person on camera and the trust value resulting.

    """
    dataPath = './faces' #Data route
    imagePaths = os.listdir(dataPath)
    print('imagePaths=',imagePaths)
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    face_recognizer.read('LBPHFaceModel.xml')    # read xml model file
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #webcam stream
    # cap = cv2.VideoCapture('Video.mp4') #video stream
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    faceChecked = 0
    while True:
        ret,frame = cap.read()
        if ret == False: break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            showFace = auxFrame[y:y+h,x:x+w]
            showFace = cv2.resize(showFace,(150,150),interpolation= cv2.INTER_CUBIC)
            result = face_recognizer.predict(showFace)
            cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            # LBPHFace
            if result[1] < 70:
                print('Person recognized: ', imagePaths[result[0]])
                print('Trust value: ',result[1])
                cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                faceChecked=faceChecked+1
            else:
                cv2.putText(frame,'Unknown',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
            
        cv2.imshow('frame',frame)
        k = cv2.waitKey(1)
        if faceChecked == 30:
            print("Welcome",imagePaths[result[0]], "!")
            break
        if k == 27:
            print("WHO ARE YOU?!?!?!?!")
            break
    cap.release()
    cv2.destroyAllWindows()
    return imagePaths[result[0]]