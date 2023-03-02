from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter
from studentbtn import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        img1=Image.open(r"F:\Project\Face_Recognition_System\Images\loginbg.jpg")
        img1=img1.resize((1550,800),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=1550,height=800)

        frame = Frame(self.root, bg="white")
        frame.place(x=610, y=170, width=340, height=450)

        img2=Image.open(r"F:\Project\Face_Recognition_System\Images\loginicon.png")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2, bg="black",borderwidth=0)
        lblimg2.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=96,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times roman new",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)

        self.txtuser=Entry(frame,font=("times new roman",15,"bold"),bg="gray",fg="white")
        self.txtuser.place(x=40,y=180,width=270)


        password=lbl=Label(frame,text="Password",font=("times roman new",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)

        self.txtpass=Entry(frame,font=("times new roman",15,"bold"),bg="gray",fg="white")
        self.txtpass.place(x=40,y=250,width=270)

        #=================Icon Images================
        img3=Image.open(r"F:\Project\Face_Recognition_System\Images\loginicon.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimg3, bg="black",borderwidth=0)
        lblimg3.place(x=650,y=323,width=25,height=25)

        img4=Image.open(r"F:\Project\Face_Recognition_System\Images\passwordicon.png")
        img4=img4.resize((25,25),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg4=Label(image=self.photoimg4, bg="black",borderwidth=0)
        lblimg4.place(x=650,y=395,width=25,height=25)

        #LoginBtn
        login_btn=Button(frame,command=self.login, text="Login", font=("times new roman",15,"bold"),bd=3,relief=RIDGE, bg="red",fg="white",activeforeground="white",activebackground="red")
        login_btn.place(x=110,y=300,width=120, height=35)

        #RegisterBtn
        Register_btn=Button(frame, text="New User Register",command=self.register_window, font=("times new roman",10,"bold"),borderwidth=0, bg="white",fg="black",activeforeground="black",activebackground="white")
        Register_btn.place(x=15,y=350,width=120)

        #Forgetpassbtn
        forget_btn=Button(frame, text="Forget Password",command=self.forgot_password_window, font=("times new roman",10,"bold"),borderwidth=0, bg="white",fg="black",activeforeground="black",activebackground="white")
        forget_btn.place(x=10,y=370,width=120)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields required")
        elif self.txtuser.get()=="Admin" and self.txtpass.get()=="1234":
            messagebox.showinfo("Success", "Wellcome to Attendance System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@123",database="register")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("Yes No","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@123",database="register")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s") 
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query1=("update register set password=%s where email=%s")
                value1=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query1,value1)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has be reset, please login using the new password",parent=self.root2)
                self.root2.destroy()












    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset the password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@123",database="register")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times roman new",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Questions", font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2, font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","School Name","Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A= Label(self.root2, text="Security Answer", font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2, font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password= Label(self.root2, text="New Password", font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2, font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass, font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=130,y=290)

            

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

        #===============Variables=================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #BG IMAGE
        self.bg=ImageTk.PhotoImage(file=r"F:\Project\Face_Recognition_System\Images\loginbg.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file=r"F:\Project\Face_Recognition_System\Images\regpagebg.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        #Main Frame
        frame=Frame(self.root, bg="white")
        frame.place(x=520,y=100,width=960,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="red", bg="white")
        register_lbl.place(x=20,y=20)

        #LBL and BTNS
        fname=Label(frame,text="First Name", font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name", font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        contact=Label(frame,text="Contact No", font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email", font=("times new roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email, font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        security_Q = Label(frame, text="Select Security Questions", font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","School Name","Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A= Label(frame, text="Security Answer", font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        pswd=Label(frame,text="Password", font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password", font=("times new roman",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #Checkbtn
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree", font=("times new roman",12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #buttons
        img=Image.open(r"F:\Project\Face_Recognition_System\Images\regbtn.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)

        b1=Button(frame,image=self.photoimage,command=self.register_data, borderwidth=0,cursor="hand2",bg="white", font=("times new roman",15,"bold"))
        b1.place(x=10,y=420,width=300)

        img1=Image.open(r"F:\Project\Face_Recognition_System\Images\login.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        b2=Button(frame,image=self.photoimage1,command=self.return_login, borderwidth=0,cursor="hand2",bg="white", font=("times new roman",15,"bold"))
        b2.place(x=330,y=420,width=300)

#=====================Functions================
    def register_data(self):
        if self.var_fname.get=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree the terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Aditya@123",database="register")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","user already exists, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")            

    def return_login(self):
        self.root.destroy()




class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #FirstImage
        img1=Image.open(r"F:\Project\Face_Recognition_System\Images\Stanford.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #secondimage
        img2=Image.open(r"F:\Project\Face_Recognition_System\Images\facialrecognition.png")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=550,height=130)

        #third image
        img3=Image.open(r"F:\Project\Face_Recognition_System\Images\msritcollege.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #BGimage
        img4=Image.open(r"F:\Project\Face_Recognition_System\Images\bgimage.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM", font=("Times New Roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #=====time===========
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font = ('times new roman',14,'bold'),background = 'white', foreground = 'blue')
        lbl.place(x=0,y=0, width=110, height=50)
        time()


        #Student Button
        img5=Image.open(r"F:\Project\Face_Recognition_System\Images\student.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5, command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details", command=self.student_details, cursor="hand2", font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Detect Face Button
        img6=Image.open(r"F:\Project\Face_Recognition_System\Images\facedetection.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data,)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data, font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Attendance Button
        img7=Image.open(r"F:\Project\Face_Recognition_System\Images\attendance.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data, font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        #HelpDesk Button
        img8=Image.open(r"F:\Project\Face_Recognition_System\Images\helpdesk.png")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data, font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #Train Data
        img9=Image.open(r"F:\Project\Face_Recognition_System\Images\traindata.png")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2", command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2", command=self.train_data, font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)

        #Photos
        img10=Image.open(r"F:\Project\Face_Recognition_System\Images\photos.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img, font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40)

        #Developer Btn
        img11=Image.open(r"F:\Project\Face_Recognition_System\Images\developer.png")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data,)
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data, font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40)

        #Exit Btn
        img12=Image.open(r"F:\Project\Face_Recognition_System\Images\exit.png")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.iExit,)
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit, font=("Times New Roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40)

    def open_img(self):
        os.startfile(r"F:\Project\Face_Recognition_System\Data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to Exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


#==============================Fucnction Buttons=================================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__ == "__main__":
    main()
