import cv2
import os
import numpy as np

def trainModel():
    """This function trains the model with the photos taken from the 'faceReader' function.
       In this part, a xml file is created with the trained model, so it doesn't have to be run everytime the script is executed.

    """
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