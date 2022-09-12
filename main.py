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

import tkinter as tk

window = Tk()
window.title("MSK Abnormality Detector")


# Pop up button
def clicked_pop():
    messagebox.showinfo('Message title', 'Message content')


    # messagebox.showinfo, messagebox.showwarning, messagebox.showerror,
btn_pop = Button(window, text="Show Pop up window",
                 bg="blue", fg="white", command=clicked_pop)
btn_pop.grid(column=3, row=1)

# Progress bar
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 70
bar.grid(column=0, row=4)


# File Uploading Button
def upload_file():
    global img
    f_types = [('Png Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    img_resized = img.resize((400, 200))  # new width & height
    img = ImageTk.PhotoImage(img_resized)
    b2 = tk.Button(window, image=img)  # using Button
    b2.grid(row=3, column=1)


b1 = tk.Button(window, text='Upload File',
               width=20, command=lambda: upload_file())
b1.grid(row=2, column=0)


def menu_info():
    messagebox.showinfo('What is MSK Abnormailty Detector', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.')


menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='About', command=menu_info)
# new_item.add_separator()
# new_item.add_command(label='Edit')
menu.add_cascade(label='About', menu=new_item)
window.config(menu=menu)


window.geometry('700x500')
window.mainloop()
