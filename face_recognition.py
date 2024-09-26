from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import os
import mysql.connector
import cv2
import numpy as np
from time import strftime
import ctypes
from datetime import datetime
import skimage.filters.edges

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.iconbitmap("face.ico")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # First image
        img_top = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\face.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # Second image
        img_buttom = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\facial_recognition.jpg")
        img_buttom = img_buttom.resize((950, 700), Image.LANCZOS)
        self.photoimg_buttom = ImageTk.PhotoImage(img_buttom)
        f_lbl = Label(self.root, image=self.photoimg_buttom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.face_recog, font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=365, y=620, width=200, height=40)
        
        
       
    
  

            

    # ================face recognition==================
    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
            roi_gray = gray_image[y:y+h, x:x+w]
            id, confidence = clf.predict(roi_gray)
            confidence = int(100 * (1 - confidence / 300))

            if confidence > 77:  # Adjust the confidence threshold as needed
                conn = mysql.connector.connect(host="localhost", username="root", password="@@@@ashik@@@@200607", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Name, Roll, Student_id, Dep FROM student WHERE Student_id=" + str(id))
                result = my_cursor.fetchone()
                if result:
                    name, roll, student_id, dep = result
                else:
                    name, roll, student_id, dep = "Unknown", "Unknown", "Unknown", "Unknown"



                cv2.putText(img, f"ID: {student_id}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Roll: {roll}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Name: {name}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Department: {dep}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                self.mark_attendence(student_id,roll,name,dep)
            else:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

    def recognize(self, img, clf, faceCascade):
        self.draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), clf)
        return img

    def face_recog(self):
        faceCascade = cv2.CascadeClassifier("har/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("cla/classifier.xml")
        
        # user32 = ctypes.windll.user32
        # screen_width = user32.GetSystemMetrics(0)
        # screen_height = user32.GetSystemMetrics(1)
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = self.recognize(img, clf, faceCascade)
            # cv2.namedWindow("Welcome To Face Recognition", cv2.WINDOW_NORMAL)
            # cv2.resizeWindow("Welcome To Face Recognition", screen_width, screen_height)
            cv2.imshow("Welcome To Face Recognition", img)

            key = cv2.waitKey(1)
            if key == 13:  # Enter key
                break
            elif key & 0xFF == ord('q'):
                # Quit when 'q' is pressed
                break

            # Check if the Tkinter window is closed
            if cv2.getWindowProperty("Welcome To Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break

        video_cap.release()
        cv2.destroyAllWindows()
    
    # ================= Mark Attendance =================
    def mark_attendence(self,student_id,roll,name,dep):
        unknown_value = "Unknown"

        # Check if any of the input parameters is equal to the unknown value
        if student_id == unknown_value or roll == unknown_value or name == unknown_value or dep == unknown_value:
            # If any of the conditions are true, skip writing to the file
            return

        with open("attendance_report/ashik.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.strip().split(",")
                name_list.append(entry[0])

            if (student_id not in name_list) and (roll not in name_list) and (name not in name_list) and (dep not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{student_id},{roll},{name},{dep},{dtString},{d1},Present")





if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()