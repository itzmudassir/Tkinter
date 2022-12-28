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
app.configure(fg_color  = "white")

# Defining Main Function
def home():
    # Globalizing the variables
    global i 
    global j
    global k
    global h1
    global m1
    global s1
    global h2 
    global m2
    global s2
    global h3
    global m3
    global s3
    global h11
    global m11
    global s11
    global h22
    global m22
    global s22
    global h33
    global m33
    global s33
   
    i = 0
    j = 0
    k = 0
    h1= 0
    m1 = 0
    s1 = 0
    h2 = 0
    m2 = 0
    s2 = 0
    h3 = 0
    m3 = 0
    s3 = 0
    h11 = 0
    m11 = 0
    s11 = 0
    h22 = 0
    m22 = 0
    s22 = 0
    h33 = 0
    m33 = 0
    s33 = 0
    
    global checkbox_1    # Making the checkbox_1 global
    global checkbox_2    # Making the checkbox_2 global
    global checkbox_3    # Making the checkbox_3 global
    
    global label_1       # Making the label_1 global   
    global label_2       # Making the label_2 global
    global label_3       # Making the label_3 global
    
    global var1         # Making the var1 global
    global var2         # Making the var2 global
    global var3         # Making the var3 global
    
    var1 = customtkinter.IntVar()       # Making the var1 as integer
    var2 = customtkinter.IntVar()       # Making the var2 as integer
    var3 = customtkinter.IntVar()       # Making the var3 as integer
    
    global dec_button_1   # Making the dec_button global
    global inc_button_1  # Making the inc_button global
    global value_label_1  # Making the value_label global
    
    
    global dec_button_2  # Making the second dec_button global
    global inc_button_2  # Making the second inc_button global
    global value_label_2  # Making the second value_label global
    
    
    global dec_button_3  # Making the third dec_button global
    global inc_button_3  # Making the third inc_button global
    global value_label_3  # Making the third value_label global 
    
    global hour_label_1  # Making the first hour_label global
    global minute_label_1  # Making the first minute_label global
    global second_label_1  # Making the first second_label global
    
    global hour_label_2  # Making the second hour_label global
    global minute_label_2  # Making the second minute_label global
    global second_label_2  # Making the second second_label global
    
    global hour_label_3  # Making the third hour_label global
    global minute_label_3  # Making the third minute_label global
    global second_label_3  # Making the third second_label global
    
    global hour_label_11  # Making the first hour_label global
    global minute_label_11  # Making the first minute_label global
    global second_label_11  # Making the first second_label global

    global hour_label_22  # Making the second hour_label global
    global minute_label_22  # Making the second minute_label global
    global second_label_22  # Making the second second_label global
    
    global hour_label_33  # Making the third hour_label global
    global minute_label_33  # Making the third minute_label global
    global second_label_33  # Making the third second_label global
    
    global schedule_label_1  # Making the schedule_label_1 global
    global schedule_label_2  # Making the schedule_label_2 global
    global schedule_label_3  # Making the schedule_label_3 global
    
    global time_label  # Making the time_label global
    global schedule_frame  # Making the schedule_frame global
    
    global light_off # Making the light_off global
    global light_on # Making the light_on global
    
    # IMAGE SECTION STARTS HERE
    
    # Define our images
    up_arrow = ImageTk.PhotoImage(Image.open("Elements\\up-arrow_1.png").resize((35,35)), Image.ANTIALIAS)
    down_arrow = ImageTk.PhotoImage(Image.open("Elements\\chevron.png").resize((35,35)), Image.ANTIALIAS)
    light_off = ImageTk.PhotoImage(Image.open("Elements\\light_off.png").resize((30,30)), Image.ANTIALIAS)
    light_on = ImageTk.PhotoImage(Image.open("Elements\\light_on.png").resize((30,30)), Image.ANTIALIAS)
    calender = customtkinter.CTkImage(Image.open("Elements\calendar.png"),size=(40, 40))
    clock = ImageTk.PhotoImage(Image.open("Elements\\clock.png").resize((40,40)), Image.ANTIALIAS)
    # IMAGE SECTION ENDS HERE
    
    # Creating the title of the window
    title1=customtkinter.CTkLabel(master=app,
                                    text="SCHEDULING ",
                                    font=("Arial", 40, "bold"),
                                    text_color="#2A2A9C")
    title1.place(x=450, y=1)

    title2=customtkinter.CTkLabel(master=app,
                                    text="SYSTEM",
                                    font=("Arial", 40, "bold"),
                                    text_color="black")
    title2.place(x=730, y=1)
    
    schedule_img = customtkinter.CTkButton(master=app,
                                            text="",
                                            image = calender,
                                            height=30,
                                            hover_color = "white",
                                            width=30,
                                            fg_color="white"
                                            )
    schedule_img.place(x=950, y=15)
    
    label_1 = customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      font=("Arial", 15, BOLD),
                                      #bg_color="white",
                                      fg_color="green",
                                      corner_radius=13,
                                      text_color="white")
                                      
    label_1.place(x=40,y=153)
    
home()
app.mainloop()