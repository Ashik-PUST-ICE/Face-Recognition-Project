from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import skimage.filters.edges


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.root.iconbitmap("face.ico")
        
        
         # Title section
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        img_top = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\help-desk.jpg")
        img_top = img_top.resize((1530,720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        # Display banner image
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)
        
        dev_label=Label(f_lbl,text="Email:ashik.200607@s.pust.ac.bd",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=550,y=220)
        
        

if __name__ == "__main__":
    root = Tk()
    obj =Help(root)
    root.mainloop()
