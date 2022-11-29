# PROGRAMMED BY: Muhammad Mudassir

# Impoting Libraries
from cProfile import label
from ctypes import resize
from doctest import master
from email.mime import audio
from tkinter import font
from turtle import title, width
import customtkinter
from PIL import ImageTk,Image
from tkinter.font import BOLD
from datetime import datetime
import time
from tkVideoPlayer import TkinterVideo

# Appearence of the window
customtkinter.set_appearance_mode("Light") #dark mode and light mood
customtkinter.set_default_color_theme("blue")

# Creating the window
app=customtkinter.CTk()
app.wm_attributes('-fullscreen','True')
app.configure(bg="white")


# Running the mainloop
app.mainloop()