faceRecognition
==================================================

NO PARAMS NEEDED FOR THIS FUNCTION
------------------------------------------------

Face Recognition
------------------------------------------------

With this function, you can read the trained algorithm (stored in the xml file from the training) and access to the camera or a video to start the face recognition algorithm.

.. code-block:: py

    def recognizeFace():
        dataPath = './faces' #Data route
        imagePaths = os.listdir(dataPath)
        print('imagePaths=',imagePaths)
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()

        face_recognizer.read('LBPHFaceModel.xml')    # read xml model file
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #webcam stream
        # cap = cv2.VideoCapture('Video.mp4') #video stream
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        faceChecked = 0
        ...

When the model is read, a loop will start, where it will do something similar to the "faceReader" section.
It will pop up the camera or the video (according to selected by the code) and start to read the face while matching the information with the trained model.
It will display the name of the person identified and the "trust" value of the accuracy that this algorithm has.
Finally, if the algorithm succesfully matches the user's face 30 times with any face in the folder of faces, it will grant access to the info from the DB and display the data in the GUI.

.. code-block:: py

        ...
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