from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #========Variables==============
        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #FirstImage
        img1=Image.open(r"F:\Project\Face_Recognition_System\Images\student1.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #secondimage
        img2=Image.open(r"F:\Project\Face_Recognition_System\Images\msrit.png")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=550,height=130)

        #third image
        img3=Image.open(r"F:\Project\Face_Recognition_System\Images\msritclass.jpg")
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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("Times New Roman",35,"bold"),bg="red",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Frame
        main_frame=Frame(bg_img,bd=2, bg="white")
        main_frame.place(x=5,y=55,width=1515,height=600)

        #Left Label Frame
        Left_frame=LabelFrame(main_frame, bd=5, relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=720, height=580)

        img_left=Image.open(r"F:\Project\Face_Recognition_System\Images\student.jpg")
        img_left=img_left.resize((700,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=710,height=130)

        #Current_Course Information
        Current_course_frame=LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current Course Information", font=("times new roman",12,"bold"))
        Current_course_frame.place(x=5,y=135,width=700, height=110)

        #Department Combo Box
        dept_lbl = Label(Current_course_frame, text="Department",font=("times new roman",12,"bold"))
        dept_lbl.grid(row=0, column=0, padx=10)

        dept_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_department, font=("times new roman",12,"bold"),state="readonly", width=17)
        dept_combo["values"]=("Select Department","MCA")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=2, pady=10)

        #Course Combo Box
        course_lbl = Label(Current_course_frame, text="Course",font=("times new roman",12,"bold"))
        course_lbl.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_course, font=("times new roman",12,"bold"),state="readonly", width=17)
        course_combo["values"]=("Select Course","Software Engineering","DevOps","Cloud Computing","Information Security","Computer Networks","Big Data Analytics", "Software project Management")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)

        #Year Combo Box
        year_lbl = Label(Current_course_frame, text="Year",font=("times new roman",12,"bold"))
        year_lbl.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_year, font=("times new roman",12,"bold"),state="readonly", width=17)
        year_combo["values"]=("Select Year","2020-2022","2021-2023","2022-2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10,sticky=W)

        #Semester Combo Box
        semester_lbl = Label(Current_course_frame, text="Semester",font=("times new roman",12,"bold"))
        semester_lbl.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_semester, font=("times new roman",12,"bold"),state="readonly", width=17)
        semester_combo["values"]=("Select Semester","1","2","3","4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10,sticky=W)

        #Class Student Information
        Class_Student_frame=LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Class Student Information", font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=5,y=250,width=700, height=300)
        
        #StudentID Entry Field
        studentid_lbl = Label(Class_Student_frame, text="Student ID:",font=("times new roman",12,"bold"))
        studentid_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentid_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_id, width=20, font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1, padx=10, pady=5,sticky=W)

        #Student NAme Entry Field
        studentname_lbl = Label(Class_Student_frame, text="Student Name:",font=("times new roman",12,"bold"))
        studentname_lbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentname_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name, width=20, font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3, padx=10, pady=5, sticky=W)

        #Class Division Entry Field
        class_div_lbl = Label(Class_Student_frame, text="Class Division:",font=("times new roman",12,"bold"))
        class_div_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_div, width=20, font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=1, padx=10, pady=5, sticky=W)

        #Roll No
        roll_no_lbl = Label(Class_Student_frame, text="Roll No:",font=("times new roman",12,"bold"))
        roll_no_lbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll, width=20, font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3, padx=10, pady=5, sticky=W)

        #Gender Entry Field
        gender_lbl = Label(Class_Student_frame, text="Gender:",font=("times new roman",12,"bold"))
        gender_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_gender, width=20, font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=1, padx=10, pady=5, sticky=W)

        #DOB Entry Field
        dob_lbl = Label(Class_Student_frame, text="DOB:",font=("times new roman",12,"bold"))
        dob_lbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob, width=20, font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3, padx=10, pady=5, sticky=W)

        #Email Entry Field
        email_lbl = Label(Class_Student_frame, text="Email:",font=("times new roman",12,"bold"))
        email_lbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email, width=20, font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1, padx=10, pady=5, sticky=W)

        #Phone_no Entry Field
        phone_no_lbl = Label(Class_Student_frame, text="Phone No:",font=("times new roman",12,"bold"))
        phone_no_lbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone, width=20, font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=3,column=3, padx=10, pady=5, sticky=W)

        #Address Entry Field
        address_lbl = Label(Class_Student_frame, text="Address:",font=("times new roman",12,"bold"))
        address_lbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address, width=20, font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1, padx=10, pady=5, sticky=W)

        #Proctor Entry Field
        proctor_lbl = Label(Class_Student_frame, text="Proctor Name:",font=("times new roman",12,"bold"))
        proctor_lbl.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        proctor_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher, width=20, font=("times new roman",12,"bold"))
        proctor_entry.grid(row=4,column=3, padx=10, pady=5, sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=2)

        #buttons Frame
        btn_frame=Frame(Class_Student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=210, width=690, height=35)

        save_btn=Button(btn_frame, text="Save",command=self.add_data, width=15, font=("times new roman",12,"bold"), bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=10, pady=0)

        update_btn=Button(btn_frame, text="Update",command=self.update_data, width=15, font=("times new roman",12,"bold"), bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=10, pady=0)

        delete_btn=Button(btn_frame, text="Delete",command=self.delete_data, width=16, font=("times new roman",12,"bold"), bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=10, pady=0)

        reset_btn=Button(btn_frame, text="Reset", command=self.reset_data, width=16, font=("times new roman",12,"bold"), bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=10, pady=0)

        btn_frame1=Frame(Class_Student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0,y=245, width=690, height=35)
        
        takephoto_btn=Button(btn_frame1,command=self.generate_dataset, text="Take Photo Sample", width=34, font=("times new roman",12,"bold"), bg="blue",fg="white")
        takephoto_btn.grid(row=0,column=0,padx=10, pady=0)

        update_btn=Button(btn_frame1, text="Update Photo Sample", width=34, font=("times new roman",12,"bold"), bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=10, pady=0)

        




        #Right Label Frame
        Right_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=720, height=580)

        img_right=Image.open(r"F:\Project\Face_Recognition_System\Images\student.jpg")
        img_right=img_right.resize((700,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=710,height=130)

        #=======================SEARCH SYSTMEM============================
        search_frame=LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search System", font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=700, height=70)

        search_lbl = Label(search_frame, text="Search By:",font=("times new roman",12,"bold"))
        search_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman",12,"bold"),state="readonly", width=12)
        search_combo["values"]=("Select","Roll No.","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame, width=15, font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2, padx=10, pady=5, sticky=W)

        search_btn=Button(search_frame, text="Search", width=15, font=("times new roman",12,"bold"), bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=10, pady=0)

        show_all_btn=Button(search_frame, text="Show All", width=15, font=("times new roman",12,"bold"), bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=10, pady=0)

        #Table Frame
        table_frame=LabelFrame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5,y=210,width=700, height=340)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, column=("Department","Course","Year","Sem","Id","Name","Div","Roll","Gender","DOB","Email","Gender","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll",text="Roll")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #========================================Function Declaration===========================
    
    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Enter Valid Details", "All fields required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root", password="Aditya@123",database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_department.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                
                                                                                            
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Students details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            
#==========================Fetch Data===============================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root", password="Aditya@123",database="facerecognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #==================== Get Cursor ========================
    def get_cursor(self,event=""):        
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_department.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    #Update Function
    def update_data(self):
        if self.var_department.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Enter Valid Details", "All fields required",parent=self.root)
        else:
            try:
                updatemessage=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                if updatemessage>0:
                    conn=mysql.connector.connect(host="localhost",username="root", password="Aditya@123",database="facerecognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                        self.var_department.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get(),
                                                                                                                                                                                    ))
                else:
                    if not updatemessage:
                        return
                messagebox.showinfo("Success","Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                                                                                                                                                                   

    #Delete Function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id is must required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root", password="Aditya@123",database="facerecognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)        
                                                                                                                                                                                         
    #reset
    def reset_data(self):
        self.var_department.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


#================================Generate Data set/take photo sample ====================
    def generate_dataset(self):
        if self.var_department.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Enter Valid Details", "All fields required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root", password="Aditya@123",database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                        self.var_department.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()==id+1
                                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #===================== Load predefined data opencv============

                face_classifier=cv2.CascadeClassifier('C:\\Users\\adida\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray, 1.3, 5)
                    #scaling factor=1.3
                    #Minimum neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path=r"F:\Project\Face_Recognition_System\Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==25:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set Completed Successfully!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)        









if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()