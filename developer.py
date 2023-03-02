from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

mydata=[]

class Developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")

        title_lbl=Label(self.root,text="DEVELOPER", font=("Times New Roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"F:\Project\Face_Recognition_System\Images\dev.jpg")
        img_top=img_top.resize((1530,730),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=730)

        #Frame
        main_frame=Frame(f_lbl,bd=2, bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        img_top1=Image.open(r"F:\Project\Face_Recognition_System\Images\Aditya.jpg")
        img_top1=img_top1.resize((180,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=180,height=200)

        #Developer Info
        dev_lbl = Label(main_frame, text="Hi, My name is Aditya",font=("times new roman",12,"bold"),bg="white",fg="black")
        dev_lbl.place(x=0, y=5)

        dev_lbl = Label(main_frame, text="Contact me for any queries\nrelated to this project.",font=("times new roman",12,"bold"),bg="white",fg="black")
        dev_lbl.place(x=0, y=40)

        #Image
        img3=Image.open(r"F:\Project\Face_Recognition_System\Images\dev1.jpg")
        img3=img3.resize((500,390),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(main_frame,image=self.photoimg3)
        f_lbl.place(x=0,y=210,width=500,height=390)





if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()


    