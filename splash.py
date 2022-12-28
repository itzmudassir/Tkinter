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
app1=customtkinter.CTk()
app1.wm_attributes('-fullscreen','True')
app1.configure(bg="white")

def splash_screen():
    frame_video=customtkinter.CTkFrame(master=app1,width=240,corner_radius=20,fg_color="white")
    frame_video.place(x=0, y=0, width=1366, height=768)
    videoplayer = TkinterVideo(frame_video, scaled=True)
    videoplayer.load(r'Elements\Scheduling_1.mp4')
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()

    #app.after(2000,frame_video.destroy)    # Destroying the splash screen after 3 seconds


    