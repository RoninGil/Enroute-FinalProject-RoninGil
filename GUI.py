from tkinter import *
from faceReader import *
from faceRecognition import *
from faceRecognitionTraining import *

root = Tk()
f1=Frame(root)
f2=Frame(root)
f3=Frame(root)
for frame in (f1,f2,f3):
    frame.grid(row=0,column=0,sticky="nsew")
def show_frame(frames):
    frames.tkraise()

def read_train_face():
    generateFace(e1.get())
    trainModel()
    show_frame(f2)

def faceRecogn():
    recognizeFace()
    show_frame(f3)

show_frame(f1)
root.title("Login")
root.geometry("300x300")
root.resizable(width=False, height=False)
######FRAME1
welcome = Label(f1, text="Face Recognition App")
welcome.pack()
e1 = Entry(f1, width=50)
e1.pack()
b1f1 = Button (f1, text="Register", command=read_train_face)
b1f1.pack()
b2f1 = Button(f1, text="Log In", command=faceRecogn)
b2f1.pack()
######FRAME2
welcome2 = Label(f2, text="Training complete!")
welcome2.pack()
b2f2 = Button(f2, text="Log In", command=faceRecogn)
b2f2.pack()
######FRAME3
welcome3 = Label(f3, text="WELCOME!")
welcome3.pack()


root.mainloop()