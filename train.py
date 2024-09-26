from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from imgaug import augmenters as iaa
import skimage.filters.edges

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.iconbitmap("face.ico")

        # Load banner image
        img_top = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\banner.jpg")
        img_top = img_top.resize((1530, 130), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        # Display banner image
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=130)
        
        # Load background image
        bg1 = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\t_bg1.jpg")
        bg1 = bg1.resize((1530,768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        
        # Display background image
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1530,height=768)
        
        # Title section
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Create buttons
        # Training button
        std_img_btn = Image.open(r"C:\Users\ashik\OneDrive\Desktop\Face_Recognization_System\collect_pic\t_btn1.png")
        std_img_btn = std_img_btn.resize((180,180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.train_classifier, image=self.std_img1, cursor="hand2")
        std_b1.place(x=640,y=240,width=240,height=220)

        std_b1_1 = Button(bg_img, command=self.train_classifier, text="Train Dataset", cursor="hand2", font=("tahoma",15,"bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=640,y=420,width=240,height=45)

    
    

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        # Define the augmentation sequence
        seq = iaa.Sequential([
            iaa.Fliplr(0.5),  # Horizontally flip 50% of the images
            iaa.Affine(rotate=(-20, 20)),  # Rotate images by -20 to 20 degrees
            iaa.GaussianBlur(sigma=(0, 1.0)),  # Apply Gaussian blur with sigma between 0 and 1.0
            iaa.AddToHueAndSaturation((-20, 20)),  # Adjust hue and saturation
            iaa.GammaContrast((0.5, 2.0))  # Adjust gamma and contrast
        ])

        for image in path:
            img = Image.open(image).convert('L')  # Gray Scale image
            imageNp = np.array(img, 'uint8')
            filename = os.path.basename(image)

            try:
                id = int(filename.split('.')[1])
            except (IndexError, ValueError):
                print(f"Skipping file: {filename} (invalid filename format)")
                continue

            # Convert grayscale image to RGB
            imageNp = cv2.cvtColor(imageNp, cv2.COLOR_GRAY2RGB)

            # Augment the image
            augmented_images = seq.augment_images([imageNp])

            # Add the original and augmented images to the training data
            faces.append(cv2.cvtColor(imageNp, cv2.COLOR_RGB2GRAY))
            ids.append(id)
            for augmented_image in augmented_images[1:]:  # Exclude the original image
                faces.append(cv2.cvtColor(augmented_image, cv2.COLOR_RGB2GRAY))
                ids.append(id)

            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, np.array(ids))
        clf.write("cla/classifier.xml")

        # print("Classifier trained and saved as 'classifier.xml'")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed !!!!")
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
