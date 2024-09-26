from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import skimage.filters.edges


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.iconbitmap("face.ico")

# =============variables======
        
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_search = StringVar()  # Updated line: Added variable for search criteria
        self.var_searchTxt = StringVar() 


    # Load images
        img = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\stand1.jpg")
        img = img.resize((500, 130), Image.LANCZOS)      
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=5, y=0, width=500, height=130)

        # Second image
        img1 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\face11.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)      
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=560, height=130)

        # Third image
        img2 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\standfoed1.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)      
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=990, y=0, width=560, height=130)

        # Big image
        img3 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\photo1.png")
        img3 = img3.resize((1530, 710), Image.LANCZOS)       
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)



        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\studentsdetails1.jpg")
        img_left= img_left.resize((720, 130), Image.LANCZOS)   # ANTIALIAS    
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # current courese information
        current_courese_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_courese_frame.place(x=5,y=135,width=720,height=120)
        
        # Department

        dep_label=Label(current_courese_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox (current_courese_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"), state="readonly",width=20 )
        dep_combo["values"] = ("Select Department", "ICE", "CSE", "EEE", "EECE", "CIVIL")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1,padx=2,pady=10,sticky=W)

        # #  # course
        course_label=Label(current_courese_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_courese_frame,textvariable=self.var_course ,font=("times new roman",13,"bold"), state="readonly",width=20)
        course_combo["values"] = ("Select Course", "ICE-3201", "ICE-3202", "ICE-3203", "ICE-3204","ICE-3205","ICE-3206","ICE-3207","ICE-3208","ICE-3209")
        course_combo.current(0)
        course_combo.grid(row=0, column=3,padx=2,pady=10,sticky=W)


        # # # Year
        year_label=Label(current_courese_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_courese_frame,textvariable=self.var_year ,font=("times new roman",13,"bold"), state="readonly",width=20)
        year_combo["values"] = ("Select year", "2018-19", "2019-20", "2020-21", "2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=1, column=1,padx=2,pady=10,sticky=W)


         # # semester
        semester_label=Label(current_courese_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_courese_frame,textvariable=self.var_semester ,font=("times new roman",13,"bold"), state="readonly",width=20)
        semester_combo["values"] = ("Select Semester", "1.1", "1.2", "2.1", "2.2","3.1","3.2","4.1","4.2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3,padx=2,pady=10,sticky=W)

        
        # # class student information

        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=250,width=720,height=300)
        
         # student id
        StudentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        StudentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        StudentId_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        StudentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

          # student name
        StudentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        StudentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


         # class division
        class_div_label=Label(class_Student_frame,text="Class Slot:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div ,font=("times new roman",13,"bold"), state="readonly",width=19)
        div_combo["values"] = ("Select Slot","1st slot", "2nd slot", "3rd slot")
        div_combo.current(0)
        div_combo.grid(row=1, column=1,padx=2,pady=5,sticky=W)

        
         # Roll No
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        
        #  Gender
        clss_gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        clss_gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
         
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"), state="readonly",width=19)
        gender_combo["values"] = ("Select Gender","Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1,padx=2,pady=5,sticky=W)

        
          
        #  DOB
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


           #  Email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        
           # phone no
        phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

         # Address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


         # Teacher nmae
        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Radio button
        self.var_radio1 = StringVar()
        radionbtn1 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=6, column=0)

        radionbtn2 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radionbtn2.grid(row=6, column=1)
 
        # bbuttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        # # Radio buttons for taking photo samples
        # self.var_radio1 = StringVar()
        # radionbtn1 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        # radionbtn1.grid(row=6, column=0, pady=5, sticky=W)

        # radionbtn2 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        # radionbtn2.grid(row=6, column=1, pady=5, sticky=W)

       
        


        # Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        
        img_right = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\students new.jpg")
        img_right= img_right.resize((720, 130), Image.LANCZOS)   # ANTIALIAS    
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

       

    #    # ====search system ===
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=710, height=70)
        
        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # Modified code for search combo
        self.search_combo = ttk.Combobox(Search_frame, textvariable=self.var_search, font=("times new roman", 13, "bold"), state="readonly", width=15)
        self.search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.search_entry = ttk.Entry(Search_frame, textvariable=self.var_searchTxt, width=15, font=("times new roman", 13, "bold"))
        self.search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        search_btn = Button(Search_frame, command=self.search_data, text="Search", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(Search_frame, command=self.show_all_data, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)


        # tbale freame

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,colum=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

       
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
      
       
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        # ======= function decreation ==========



        # UI components go here (e.g., labels, entries, buttons, etc.)

    # Add data to the database
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="@@@@ashik@@@@200607", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (self.var_dep.get(),
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

                # Verify insertion
                my_cursor.execute("SELECT * FROM student WHERE Student_id = %s", (self.var_std_id.get(),))
                row = my_cursor.fetchone()
                # if row:
                #     print("Data inserted successfully:", row)
                # else:
                #     print("Data insertion failed")

                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    # Fetch data from the database and display it in the table
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="@@@@ashik@@@@200607", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Display selected row data in the input fields
    def get_cursor(self, event=""):
        try:
            cursor_focus = self.student_table.focus()
            if not cursor_focus:
                raise ValueError("No item is selected in the student table.")
            
            content = self.student_table.item(cursor_focus)
            data = content["values"]
            
            if not data or len(data) < 15:
                raise ValueError("The selected item does not contain enough data.")
            
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_div.set(data[6])
            self.var_roll.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])
        except Exception as e:
            print(f"Error: {e}")


    # Update data in the database
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@@@@ashik@@@@200607", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                    UPDATE student 
                    SET Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, 
                    Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, 
                    Teacher=%s, PhotoSample=%s 
                    WHERE Student_id=%s""",
                    (self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                    ))

                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # Delete data from the database
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete >= 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@@@@ashik@@@@200607", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # Reset input fields
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
        
        # ====search data====
        
    # Search data
    def search_data(self):
        if self.search_combo.get() == "Select" or self.var_searchTxt.get() == "":
            messagebox.showerror("Error", "Please select a search criteria and enter a search value.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="@@@@ashik@@@@200607", database="face_recognizer")
                my_cursor = conn.cursor()

                search_by = ""
                if self.search_combo.get() == "Roll_No":
                    search_by = "Roll"
                elif self.search_combo.get() == "Phone_No":
                    search_by = "Phone"
                else:
                    search_by = self.search_combo.get().replace(" ", "").lower()

                search_value = self.var_searchTxt.get()

                query = f"SELECT * FROM student WHERE {search_by} LIKE %s"
                value = (f"%{search_value}%",)
                my_cursor.execute(query, value)
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                else:
                    self.student_table.delete(*self.student_table.get_children())

                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # Show all data
    def show_all_data(self):
        self.fetch_data()

# ...

    # Generate dataset by capturing face images
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="@@@@ashik@@@@200607",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = len(myresult) + 1

                my_cursor.execute("""
                    UPDATE student 
                    SET Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, 
                    Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, 
                    Teacher=%s, PhotoSample=%s 
                    WHERE Student_id=%s
                    """,
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        id,
                        self.var_std_id.get()
                    )
                )

                conn.commit()
                self.fetch_data()  # This method should refresh the displayed data
                conn.close()

                face_classifier = cv2.CascadeClassifier("har/haarcascade_frontalface_default.xml")

                def face_cropped(img, margin=20):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    cropped_faces = []
                    for (x, y, w, h) in faces:
                        x_start = max(x - margin, 0)
                        y_start = max(y - margin, 0)
                        x_end = min(x + w + margin, img.shape[1])
                        y_end = min(y + h + margin, img.shape[0])
                        face_cropped = img[y_start:y_end, x_start:x_end]
                        cropped_faces.append(face_cropped)
                    return cropped_faces

                def generate_dataset(student_id):
                    cap = cv2.VideoCapture(0)
                    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
                    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()
                        if ret:
                            cropped_faces = face_cropped(my_frame)
                            for face in cropped_faces:
                                if isinstance(face, np.ndarray) and face.size > 0:
                                    img_id += 1
                                    try:
                                        face_resized = cv2.resize(face, (250, 250))
                                        face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
                                        file_name_path = f"data/user.{str(student_id)}.{str(img_id)}.jpg"
                                        cv2.imwrite(file_name_path, face_gray)
                                        # print(f"Saved: {file_name_path}")
                                        cv2.putText(face_gray, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                                        cv2.imshow("Cropped Face", face_gray)
                                    except Exception as e:
                                        print(f"Error processing face: {e}")
                                        continue
                        if cv2.waitKey(1) == 13 or img_id == 100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()

                student_id = self.var_std_id.get()
                generate_dataset(student_id)

                messagebox.showinfo("Result", "Generating data sets Completed !!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

        