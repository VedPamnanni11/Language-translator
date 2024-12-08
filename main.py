from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title('Language Translator')
root.geometry('590x370')

framel = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#F7DC6F')
framel.place(x=0, y=0)

Label(root, text="Language Translator", font=("Helvertica 20 bold"), fg="black", bg='#F7DC6F').pack(pady=10)

root.mainloop()