from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
from main import Face_Recognition_System
import skimage.filters.edges


class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")
        self.root.iconbitmap("face.ico")
        
        # ===========Variables================
        
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        
        
        
        # ============bg image==================
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\reg1.jpeg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ============left image============
        img1 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\reg2.jpg")
        img1 = img1.resize((600, 550), Image.LANCZOS)      
        self.photoimg1 = ImageTk.PhotoImage(img1)
       
        left_lbl = Label(self.root, image=self.photoimg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # Main Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)
        
        
        #====== Label And entry ==========
        
        # ===Row 1===
        
        fname=Label(frame,text="First Name",font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry (frame,textvariable=self.var_fname,font=("times new roman",15, "bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        label_lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_lname.place(x=370, y=100)
        txt_lname = ttk.Entry(frame, textvariable=self.var_lname,font=("times new roman", 15))
        txt_lname.place(x=370, y=130, width=250)

        # Row 2
        label_contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_contact.place(x=50, y=170)
        txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15))
        txt_contact.place(x=50, y=200, width=250)

        label_email =Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_email.place(x=370, y=170)
        txt_email = ttk.Entry(frame, textvariable=self.var_email,font=("times new roman", 15))
        txt_email.place(x=370, y=200, width=250)
        
        # ===== row 3==
        
        security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)


        # ===== row 4=====
        
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show='*')
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show='*')
        self.txt_confirm_pswd.place(x=370, y=340, width=250)
        
        
        # ==========checkbutton========
        self.var_check=IntVar()
        
        self.checkbtn= Checkbutton(frame, variable=self.var_check,text="I Agree The Terms & Conditions", font=("times new roman", 15, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)

        # ============buttons===========
        
        # Register button
        img2 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\registernow.jpg")
        img2 = img2.resize((200, 55), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        b1 = Button(frame, image=self.photoimage2,command=self.register_data, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="white")
        b1.place(x=30, y=420, width=200)

        # Login button
        img3 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\loog.jpg")
        img3 = img3.resize((200, 45), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        b2 = Button(frame, image=self.photoimage3, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="white")
        b2.place(x=375, y=420, width=200)
        
        
        # ========= Function declaration =======
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
           messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
            
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms and conditions")
            
        else:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="@@@@ashik@@@@200607",
            database="face_recognizer"
        )

        my_cursor = conn.cursor()
        query = "SELECT * FROM register WHERE email = %s"
        value = (self.var_email.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()

        if row is not None:
            messagebox.showerror("Error", "User already exists, please try another email")
        else:
        
           my_cursor.execute("INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", (

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

            
                

            
           
        
        
       
                            
        
        



if __name__ == "__main__":
    root = Tk()
    app= Register(root)
    root.mainloop()
