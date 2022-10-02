from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry
from os import path
from distutils.command.upload import upload
from tkinter import *
from tkinter import messagebox
from tkinter.font import ITALIC
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu
from PIL import Image, ImageTk
import os
import sys
import tkinter as tk


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("MSK Abnormality Detector")
        self.pack(fill=BOTH, expand=True)


# Welcome Text

        frame1 = Frame(self)
        frame1.pack(fill=X)
        Welcome = Label(frame1, text="Welcome to MSK Abnormality Detector",
                        width=11, font=("Arial Bold", 12))
        Welcome.pack(fill=X, padx=5, pady=10, expand=True)

# Procedure Text
        procedure_label = Label(frame1, text="Classification Procedure",
                                width=11, font=("Arial", 11))
        procedure_label.pack(fill=X, padx=5, pady=5, expand=True)

# Model Selection
        lbl1 = Label(frame1, text="Choose Model",
                     width=11, font=("Arial Bold", 12), highlightbackground="black", highlightthickness=1)
        lbl1.pack(side=LEFT, padx=5, pady=4)


# Classification Button

        def clasify_input():
            classification_result.configure(text="MSK is Normal", font=("Arial Bold", 11), foreground="Green", width=20)
            probability_result.configure(text="Probability is 30%", font=("Arial Bold", 11), width=20)

        classify_btn = tk.Button(frame1, text='Classify Image', width=20, command=lambda: clasify_input())
        classify_btn.pack(side=RIGHT, padx=5, pady=4)

# Classification Label
        clasify_label = Label(frame1, text="Classify",
                              width=11, font=("Arial Bold", 12))
        clasify_label.pack(side=RIGHT, padx=5, pady=4)

# Radio Buttons
    # Radio Functions

        def procedure_with_CLAHE():
            procedure_label.configure(
                text="Procedure WITH CLAHE", font=("Arial Bold", 11), foreground="Green")

        def procedure_without_CLAHE():
            procedure_label.configure(
                text="Procedure WITHOUT CLAHE", font=("Arial Bold", 11), foreground="Red")
    # Acutal Buttons
        rad1 = Radiobutton(frame1, text='With CLAHE',
                           value=1, command=procedure_with_CLAHE)
        rad1.pack(side=LEFT, padx=15, pady=2)

        rad2 = Radiobutton(frame1, text='Without CLAHE',
                           value=2, command=procedure_without_CLAHE)
        rad2.pack(side=LEFT, padx=15, pady=2)


# File Uploading
        frame3 = Frame(self)
        frame3.pack(fill=X)

        lbl3 = Label(frame3, text="File Upload",
                     width=11, font=("Arial Bold", 12))
        lbl3.pack(side=LEFT, padx=5, pady=4)

# File Button

        # Frame Main
        frame_main = Frame(self,bg="black", pady=30, padx=30)
        frame_main.pack(fill=X)

        # Classification Results
        frame_results = Frame(frame_main, bg="black", pady=10, padx=10)
        frame_results.grid(row=1, column=2)

        classification_result = Label(frame_results, text="Classification Result ...", font=("Arial Bold", 12), width=18)
        classification_result.grid(row=1,  padx=10, pady=100)

        probability_result = Label(frame_results, text="Probability is...", font=("Arial Bold", 12), width=18)
        probability_result.grid(row=2, padx=10, pady=100)
 
        # Frame for Preview Image
        frame_preview = Frame(frame_main, bg="black", width=500, height=500, highlightbackground="white", highlightthickness=1, pady=100, padx=100)
        frame_preview.grid(row=1, column=1)
 
        # Frame for Cam Image
        frame_cam = Frame(frame_main, bg="black", width=500, height=500, highlightbackground="white", highlightthickness=1, pady=100, padx=100)
        frame_cam.grid(row=1, column=3)

        def upload_file():
            global img
            f_types = [('Png Files', '*.png')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = Image.open(filename)
            img_resized = img.resize((300, 300))  # new width & height
            img = ImageTk.PhotoImage(img_resized)
            uploaded_img = tk.Button(frame_preview, image=img)  # using Button
            uploaded_img.pack()

        def restart_program():
            python = sys.executable
            os.execl(python, python, * sys.argv)

        upload_btn = tk.Button(frame3, text='Upload File',
                               width=20, command=lambda: upload_file())
        upload_btn.pack(side=LEFT, padx=5, pady=4)

        Button(frame3, text="Restart", command=restart_program).pack(side=RIGHT, padx=5)

def main():

    root = Tk()
    root.geometry("1280x720")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
