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
                     width=11, font=("Arial Bold", 12))
        lbl1.pack(side=LEFT, padx=5, pady=4)


# Classification Button

        def clasify_input():
            final_classification_label.configure(
                text="MSK is Normal", font=("Arial Bold", 11), foreground="Green")
        classify_btn = tk.Button(frame1, text='Classify Image',
                                 width=20, command=lambda: clasify_input())
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
# Classification Results
        final_classification_label = Label(frame3, text="Classification Result ...",
                                           width=20, font=("Arial Bold", 12))
        final_classification_label.pack(side=RIGHT, padx=10, pady=4)

# File Button
        frame4 = Frame(self)
        frame4.pack(fill=X)

        def upload_file():
            global img
            f_types = [('Png Files', '*.png')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = Image.open(filename)
            img_resized = img.resize((500, 500))  # new width & height
            img = ImageTk.PhotoImage(img_resized)
            uploaded_img = tk.Button(frame4, image=img)  # using Button
            uploaded_img.pack(side=LEFT, padx=5, pady=4)

        def restart_program():
            python = sys.executable
            os.execl(python, python, * sys.argv)

        upload_btn = tk.Button(frame3, text='Upload File',
                               width=20, command=lambda: upload_file())
        upload_btn.pack(side=LEFT, padx=5, pady=4)

        Button(frame3, text="Restart", command=restart_program).pack()


def main():

    root = Tk()
    root.geometry("1200x600")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
