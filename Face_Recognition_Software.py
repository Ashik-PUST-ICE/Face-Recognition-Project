from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import random
import datetime
import mysql.connector
import cv2
import numpy as np
from main import Face_Recognition_System
from tkinter import Label
from PIL import Image, ImageTk
import skimage.filters.edges



def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.iconbitmap("face.ico")

        # Load images
        img = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\stand1.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg9)
        f_lbl.place(x=0, y=0, width=500, height=130)

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
        f_lbl.place(x=1000, y=0, width=560, height=130)

        # Big image
        img3 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\photo1.png")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=220, width=340, height=450)

        img2 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\images.png")
        img2 = img2.resize((90, 90), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img2)
        lb1img1 = Label(image=self.photoimg11, bg="black", borderwidth=0)
        lb1img1.place(x=730, y=225, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Username Label and Entry
        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username_lbl.place(x=70, y=155)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Password Label and Entry
        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password_lbl.place(x=70, y=225)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*')
        self.txtpass.place(x=40, y=250, width=270)

        # =====icon image===
        img3 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\images.png")
        img3 = img3.resize((23, 23), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img3)
        lb1img2 = Label(image=self.photoimg12, bg="black", borderwidth=0)
        lb1img2.place(x=645, y=375, width=40, height=23)

        img4 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\passs.jpg")
        img4 = img4.resize((23, 23), Image.LANCZOS)
        self.photoimg13 = ImageTk.PhotoImage(img4)
        lb1img3 = Label(image=self.photoimg13, bg="black", borderwidth=0)
        lb1img3.place(x=645, y=445, width=40, height=23)

        #   ===== Log in Button====
        loginbtn = Button(frame, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, command=self.login,
                          fg="white", bg="red", activeforeground="red", activebackground="red")
        loginbtn.place(x=40, y=300, width=270, height=35)

        # =====registerbutton======
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"),
                             borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=20, y=350, width=160)

        # =====forgetpassword======
        forgetbtn = Button(frame, text="Forget Password", command=self.forgot_password_window, font=("times new roman", 10, "bold"),
                           borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetbtn.place(x=15, y=380, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="@@@@ashik@@@@200607",
                database="face_recognizer"
            )

            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email = %s AND password = %s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))

            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the Email & Password")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="@@@@ashik@@@@200607",
                database="face_recognizer"
            )

            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("My Error", "Please enter the Valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=("times new roman", 15, "bold"), fg="white", bg="green")
                btn.place(x=100, y=290)

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select the Security question")
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please Enter the Answer")
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please Enter the New Password")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="@@@@ashik@@@@200607",
                database="face_recognizer"
            )

            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s")
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Please Enter the Correct Answer")
            else:
                query = ("UPDATE register SET password=%s WHERE email=%s")
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your Password has been reset, please login with new password")


class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")

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
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        label_lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_lname.place(x=370, y=100)
        txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        txt_lname.place(x=370, y=130, width=250)

        # Row 2
        label_contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_contact.place(x=50, y=170)
        txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        txt_contact.place(x=50, y=200, width=250)

        label_email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        label_email.place(x=370, y=170)
        txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        txt_email.place(x=370, y=200, width=250)

        # ===== row 3==
        security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # ===== row 4=====
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show='*')  # Added show='*'
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)
        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show='*')  # Added show='*'
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ==========checkbutton========
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions",
                                    font=("times new roman", 15, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)

        # ============buttons===========
        # Register button
        img2 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\registernow.jpg")
        img2 = img2.resize((200, 55), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        b1 = Button(frame, image=self.photoimage2, command=self.register_data, borderwidth=0, cursor="hand2",
                    font=("times new roman", 15, "bold"), fg="white")
        b1.place(x=30, y=420, width=200)

        # Login button
        img3 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\loog.jpg")
        img3 = img3.resize((200, 45), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        b2 = Button(frame,command=self.root.destroy,image=self.photoimage3, borderwidth=0, cursor="hand2",
                    font=("times new roman", 15, "bold"), fg="white")
        b2.place(x=375, y=420, width=200)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "password & confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and condition")
        else:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="@@@@ashik@@@@200607",
                database="face_recognizer"
            )

            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exist, please try another email")
            else:
                my_cursor.execute(
                    "INSERT INTO register VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get()
                    )
                )
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Register Successfully")


if __name__ == "__main__":
    main()
