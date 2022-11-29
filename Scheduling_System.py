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

def home():
    
    # IMAGE SECTION STARTS HERE
    
    # Define our images
    up_arrow = ImageTk.PhotoImage(Image.open("Elements\\up-arrow_1.png").resize((35,35)), Image.ANTIALIAS)
    down_arrow = ImageTk.PhotoImage(Image.open("Elements\\chevron.png").resize((35,35)), Image.ANTIALIAS)
    light_off = ImageTk.PhotoImage(Image.open("Elements\\light_off.png").resize((30,30)), Image.ANTIALIAS)
    light_on = ImageTk.PhotoImage(Image.open("Elements\\light_on.png").resize((20,20)), Image.ANTIALIAS)
    calender = ImageTk.PhotoImage(Image.open("Elements\calendar.png").resize((40,40)), Image.ANTIALIAS)
    # IMAGE SECTION ENDS HERE

    # Creating the title of the window
    title1=customtkinter.CTkLabel(master=app,
                                    text="ꜱᴄʜᴇᴅᴜʟɪɴɢ ",
                                    text_font=("Arial", 40, "bold"),
                                    text_color="#2A2A9C")
    title1.place(x=450, y=1)

    title2=customtkinter.CTkLabel(master=app,
                                    text="ꜱʏꜱᴛᴇᴍ",
                                    text_font=("Arial", 40, "bold"),
                                    text_color="black")
    title2.place(x=750, y=1)
    
    schedule_img = customtkinter.CTkButton(master=app,
                                            text="",
                                            image = calender,
                                            height=30,
                                            width=30,
                                            bg="white",
                                            fg_color="white")
    schedule_img.place(x=950, y=15)
    
    
# Calling the home function
home()

# Running the mainloop
app.mainloop()