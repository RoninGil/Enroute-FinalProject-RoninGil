from tkinter import *
from faceReader import *
from faceRecognition import *
from faceRecognitionTraining import *
from CRUD import *
import os
from dotenv import load_dotenv
from mysql.connector import connect, Error

load_dotenv()

userName=os.getenv('MYSQL_USER')
pswd=os.getenv('MYSQL_PASSWORD')
hostName=os.getenv('MYSQL_HOST')
portSel= os.getenv('MYSQL_PORT')
databaseName='users'
#The testing in this function involves using the webcam, so it will not be deployed on Travis
def executeGUI():#pragma: no cover
    """
    This file executes the basic GUI to perform the Register and Login, as well as the
    face recognition complete algorithm.
    
    """
    values=[]
    root = Tk()
    f1=Frame(root)
    f2=Frame(root)
    f3=Frame(root)
    f4=Frame(root)
    for frame in (f1,f2,f3, f4):
        frame.grid(row=0,column=0,sticky="nsew")

    def show_frame(frames):
        """This function is executed to show different frames of Tkinter on the GUI.

        :param frames: Host name of DataBase.
        :type frames: Frame

        """
        frames.tkraise()

    def write_data(userFace):
        """This function is executed to write user's info according to the match of the face and the trained model.

        :param userFace: User's name after attempting to login and being recognized by the model.
        :type userFace: string

        """
        userData=select_user(hostName, userName, pswd, databaseName, portSel, userFace)
        text1='ID:',userData[0]
        text2='Name:',userData[1]
        text3='Address:',userData[2]
        text4='Tel. Number:',userData[3]
        text5='Email:',userData[4]
        lID.config(text=text1)
        luser2.config(text=text2)
        laddress2.config(text=text3)
        ltel2.config(text=text4)
        lemail2.config(text=text5)


    def read_train_face():
        """This function is executed to Get the values from the register GUI, it also runs the 'generateFace' and 'trainModel' scripts to read and train the model with a new face.
        After the face is read and stored on the respective folder, it executes the DB scripts to create db and table (if not exists) and insert the user's data written on the GUI.
        Finally, it shows the next frame of the Tkinter GUI.

        """
        values=[e1.get(), e2.get(), e3.get(), e4.get()]
        print(values)
        generateFace(e1.get())
        trainModel()
        # create_db(hostName, userName, pswd, databaseName, portSel)
        create_table(hostName, userName, pswd, portSel)
        insert_user(hostName, userName, pswd, databaseName, portSel, values)
        show_frame(f3)

    def faceRecogn():
        """This function is executed to execute the 'recognizeFace' script and get the person's name.
        After this is done, the name retrieved is used to ask for the user's data from the DataBase.


        """
        userFace=recognizeFace()
        write_data(userFace)
        show_frame(f4)

    show_frame(f1)
    root.title("Login")
    root.geometry("300x300")
    root.resizable(width=False, height=False)
    ######FRAME1
    welcome = Label(f1, text="Face Recognition App")
    welcome.grid(row=2)
    b1f1 = Button (f1, text="Register", command=lambda:show_frame(f2))
    b1f1.grid(row=3, column=0)
    b2f1 = Button(f1, text="Log In", command=faceRecogn)
    b2f1.grid(row=3, column=1)
    ######FRAME2
    welcome2 = Label(f2, text="Register User")
    welcome2.grid(row=2)
    luser = Label(f2, text="Username: ")
    luser.grid(row=3, column=0)
    e1 = Entry(f2, width=50)
    e1.grid(row=3, column=1)
    laddress = Label(f2, text="Address: ")
    laddress.grid(row=4, column=0)
    e2 = Entry(f2, width=50)
    e2.grid(row=4, column=1)
    ltel = Label(f2, text="Tel. number: ")
    ltel.grid(row=5, column=0)
    e3 = Entry(f2, width=50)
    e3.grid(row=5, column=1)
    lemail = Label(f2, text="Email: ")
    lemail.grid(row=6, column=0)
    e4 = Entry(f2, width=50)
    e4.grid(row=6, column=1)
    b2f2 = Button(f2, text="Biometry registry", command=read_train_face)
    b2f2.grid(row=8, column=0)
    ######FRAME 3
    welcome2 = Label(f3, text="Log In")
    welcome2.grid(row=2, column=0)
    b1f3 = Button(f3, text="Face Recognition", command=faceRecogn)
    b1f3.grid(row=3, column=1)
    ######FRAME4
    welcome4 = Label(f4, text="WELCOME!")
    welcome4.grid(row=2, column=0)
    lID = Label(f4, text="ID: ",)
    lID.grid(row=3, column=0)
    luser2 = Label(f4, text="Username: ")
    luser2.grid(row=3, column=0)
    laddress2 = Label(f4, text="Address: ")
    laddress2.grid(row=4, column=0)
    ltel2 = Label(f4, text="Tel. number: ")
    ltel2.grid(row=5, column=0)
    lemail2 = Label(f4, text="Email: ")
    lemail2.grid(row=6, column=0)

    root.mainloop()
executeGUI() #pragma: no cover