from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")

        title_lbl=Label(self.root,text="HELP DESK", font=("Times New Roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"F:\Project\Face_Recognition_System\Images\help.jpg")
        img_top=img_top.resize((1530,730),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=730)

        dev_lbl = Label(f_lbl, text="Please Contact - \n Email: adit.ya.paul0499@gmail.com",font=("times new roman",40,"bold"),bg="white",fg="black")
        dev_lbl.place(x=300, y=450)


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()