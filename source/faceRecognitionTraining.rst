faceRecognitionTraining
==================================================

NO PARAMS NEEDED FOR THIS FUNCTION
------------------------------------------------

Training the model
------------------------------------------------

This function is used for the model to be trained, with OpenCV and Numpy, the function "train" can be executed with the values needed, which are:

* facesData: All the photos taken from the face of the user. (Array)
* labels: These labels are the identifiers for every photo, so the "np.array" can append them. (Array)

.. code-block:: py

    def trainModel():

        dataPath = './faces'#data route
        peopleList = os.listdir(dataPath)

        print('People list: ', peopleList)

        labels = []
        facesData = []
        label = 0

        for nameDir in peopleList:
            personPath = dataPath + '/' + nameDir
            print('Reading images')

            for fileName in os.listdir(personPath):
                print('Faces: ', nameDir + '/' + fileName)
                labels.append(label)
                facesData.append(cv2.imread(personPath+'/'+fileName,0))

            label = label + 1

        # LBPH Training model
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()

        print("Training...")
        face_recognizer.train(facesData, np.array(labels))

        # Save model on xml file
        face_recognizer.write('LBPHFaceModel.xml')
        print("Model ready!")
        return True

Once all the faces are in the Arrays, the model is trained and is written on a xml file called "LBPHFaceModel.xml", which is the algorithm being used for the training.
