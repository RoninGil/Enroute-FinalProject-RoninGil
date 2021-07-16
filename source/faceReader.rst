faceReader
==================================================

Params
--------------------------------------

*name: This value is provided by the user inside the "Username" field on the GUI. (str)

Read Face
--------------------------------------

With this function, the algorithm takes a total of 100 photos of the person on camera.

.. code-block:: py

    def generateFace(name):
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
        ...

With this function, a uses name is provided from the GUI and create a folder with that name (where the photos will be stored).
With OpenCV the Haar Cascade Classifier will be used to classify the faces from the photos taken.

.. code-block:: py

    ...
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

With this loop, the function is creating a frame for the photos to be taken, everytime a photo is taken, the 'count' variable is increased by 1.
With values x, y, w, h certain coordinate points are created in order to take the photos where the face is being recognized.
If you press "Esc" key or the counter reaches 100, the process will be terminated.