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
    
    # CHECKBOX SECTION STARTS HERE
    checkbox_1 = customtkinter.CTkCheckBox(master=app,
                                           #command=checkbox_event_1,
                                           variable=var1,
                                           hover_color = "#2A2A9C",
                                           fg_color = "#2A2A9C",
                                           border_color = "black",
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_1.place(x=10, y = 155)
    
    checkbox_2 = customtkinter.CTkCheckBox(master=app, 
                                           #command=checkbox_event_2,
                                           variable=var2,
                                           hover_color = "#2A2A9C",
                                           fg_color = "#2A2A9C",
                                           border_color = "black",
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_2.place(x=10, y = 285)
    
    checkbox_3 = customtkinter.CTkCheckBox(master=app, 
                                           #command=checkbox_event_3,
                                           variable=var3,
                                           hover_color = "#2A2A9C",
                                           fg_color = "#2A2A9C",
                                           border_color = "black",
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_3.place(x=10, y = 415)
    # ********** END OF CHECKBOX SECTION **********
    
    # CHECKBOX LABEL SECTION STARTS HERE
    label_1 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, "bold"),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
                                      text_color="white")
                                      
    label_1.place(x=40,y=153)
    
    label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, "bold"),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
                                      text_color="white")
    label_2.place(x=40,y=283)
    
    label_3 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, "bold"),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
                                      text_color="white")
    label_3.place(x=40,y=413)
    # ********** END OF CHECKBOX LABEL SECTION **********
    
    # CREATING STARTING TIME LABELS & BUTTONS
    # First Row Time Buttons & Labels
    inch_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_hours_1
                                            )
                                            
    inch_button_1.place(x=420,y=112)
    
    incm_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_minutes_1
                                            )
    incm_button_1.place(x=480,y=112)
    
    incs_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_seconds_1
                                            )
    incs_button_1.place(x=540,y=112)
    
    
    hour_label_1 = customtkinter.CTkLabel(master=app,
                                         text="00",
                                         text_font=("Arial", 20,BOLD),
                                         bg_color="white",
                                         fg_color="white",
                                         corner_radius=8,
                                         text_color="#2A2A9C",
                                          width=20,
                                          height=10
                                        )
                                         
                                             
    hour_label_1.place(x=416,y=153)
    
    minute_label_1 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    minute_label_1.place(x=476,y=153)
    
    second_label_1 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    second_label_1.place(x=536,y=153)
    
    dech_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            #command=decrease_clock_hours_1
                                            )
    dech_button_1.place(x=420,y=186)
    
    decm_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_minutes_1
                                            )
    decm_button_1.place(x=480,y=186)
    
    decs_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_seconds_1
                                            )
    decs_button_1.place(x=540,y=186)
    # ********** END OF FIRST ROW TIME BUTTONS & LABELS **********
    
    # Second Row Time Buttons & Labels
    inch_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_hours_2
                                            )                                       
    inch_button_2.place(x=420,y=240)
    
    incm_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_minutes_2
                                            )
    incm_button_2.place(x= 480,y=240)
    
    incs_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_seconds_2
                                            )
    incs_button_2.place(x=540,y=240)
    
    
    hour_label_2 = customtkinter.CTkLabel(master=app,
                                         text="00",
                                         text_font=("Arial", 20,BOLD),
                                         bg_color="white",
                                         fg_color="white",
                                         corner_radius=8,
                                         text_color="#2A2A9C",
                                          width=20,
                                          height=10
                                        )
                                                                        
    hour_label_2.place(x=416,y=281)
    
    minute_label_2 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    minute_label_2.place(x=476,y=281)
    
    second_label_2 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",   
                                            width=20,
                                            height=10
                                            )
    second_label_2.place(x=536,y=281)
    
    dech_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_hours_2
                                            )
    dech_button_2.place(x=420,y=314)
    
    decm_button_2 = customtkinter.CTkButton(master=app,
                                            text="",    
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_minutes_2
                                            )
    decm_button_2.place(x=480,y=314)
    
    decs_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_seconds_2
                                            )
    decs_button_2.place(x=540,y=314)
    # ********** END OF SECOND ROW TIME BUTTONS & LABELS **********
    
    # Third Row Time Buttons & Labels
    inch_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_hours_3
                                            )
    inch_button_3.place(x=420,y=368)
    
    incm_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_minutes_3
                                            )
    incm_button_3.place(x= 480,y=368)

    incs_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_seconds_3
                                            )
    incs_button_3.place(x=540,y=368)

    hour_label_3 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    hour_label_3.place(x=416,y=409)

    minute_label_3 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",   
                                            width=20,
                                            height=10
                                            )   
    minute_label_3.place(x=476,y=409)
    
    second_label_3 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    second_label_3.place(x=536,y=409)
    
    dech_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,    
                                            width=30,
                                            #command=decrease_clock_hours_3
                                            )
    dech_button_3.place(x=420,y=442)

    decm_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_minutes_3
                                            )
    decm_button_3.place(x=480,y=442)
    
    decs_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_seconds_3
                                            )
    decs_button_3.place(x=540,y=442)
    # ********** END OF THIRD ROW TIME BUTTONS & LABELS **********
    
    # CREATING ENDING TIME LABELS & BUTTONS
    # First Row Time Buttons & Labels
    inch_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_hours_11
                                            )
                                            
    inch_button_11.place(x=720,y=112)
    
    incm_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_minutes_11
                                            )
    incm_button_11.place(x= 780,y=112)

    incs_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_seconds_11
                                            )
    incs_button_11.place(x=840,y=112)

    hour_label_11 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    hour_label_11.place(x=716,y=153)

    minute_label_11 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    minute_label_11.place(x=776,y=153)

    second_label_11 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    second_label_11.place(x=836,y=153)

    dech_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_hours_11
                                            )
    dech_button_11.place(x=720,y=186)
    
    decm_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_minutes_11
                                            )
    decm_button_11.place(x=780,y=186)
    
    decs_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_seconds_11
                                            )
    decs_button_11.place(x=840,y=186)
    # ********** END OF FIRST ROW TIME BUTTONS & LABELS **********
    
    # Second Row Time Buttons & Labels
    inch_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_hours_22
                                            )
    inch_button_22.place(x=720,y=242)
    
    incm_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_minutes_22
                                            )   
    incm_button_22.place(x=780,y=242)

    incs_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_seconds_22
                                            )
    incs_button_22.place(x=840,y=242)
    
    hour_label_22 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    hour_label_22.place(x=716,y=283)
    
    minute_label_22 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    minute_label_22.place(x=776,y=283)
    
    second_label_22 = customtkinter.CTkLabel(master=app,    
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )   
    second_label_22.place(x=836,y=283)

    dech_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_hours_22
                                            )
    dech_button_22.place(x=720,y=316)

    decm_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_minutes_22
                                            )
    decm_button_22.place(x=780,y=316)
    
    decs_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_seconds_22
                                            )
    decs_button_22.place(x=840,y=316)
    # ********** END OF SECOND ROW TIME BUTTONS & LABELS **********
    
    # Third Row Time Buttons & Labels
    inch_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_hours_33  
                                            )
    inch_button_33.place(x=720,y=372)

    incm_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_minutes_33
                                            )
    incm_button_33.place(x=780,y=372)
    
    incs_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=increase_clock_seconds_33
                                            )
    incs_button_33.place(x=840,y=372)

    hour_label_33 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    hour_label_33.place(x=716,y=413)

    minute_label_33 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD), 
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    minute_label_33.place(x=776,y=413)
    
    second_label_33 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 20,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="#2A2A9C",
                                            width=20,
                                            height=10
                                            )
    second_label_33.place(x=836,y=413)
    
    dech_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_hours_33
                                            )
    dech_button_33.place(x=720,y=446)

    decm_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_minutes_33
                                            )
    decm_button_33.place(x=780,y=446)

    decs_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #command=decrease_clock_seconds_33
                                            )
    decs_button_33.place(x=840,y=446)
    # ********** END OF THIRD ROW TIME BUTTONS & LABELS **********
    
    # CREATING SUMBIT BUTTON
    sub_button_1 = customtkinter.CTkButton(master=app,
                                            text="ꜱᴜʙᴍɪᴛ",
                                            text_color="white",
                                            hover_color="blue",
                                            fg_color="#2A2A9C",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            #command=submit_1
                                            )
    sub_button_1.place(x=950,y=153)
    
    sub_button_2 = customtkinter.CTkButton(master=app,
                                            text="ꜱᴜʙᴍɪᴛ",
                                            text_color="white",
                                            hover_color="blue",
                                            fg_color="#2A2A9C",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            #command=submit_2
                                            )
    sub_button_2.place(x=950,y=283)
    
    sub_button_3 = customtkinter.CTkButton(master=app,
                                            text="ꜱᴜʙᴍɪᴛ",
                                            text_color="white",
                                            hover_color="blue",
                                            fg_color="#2A2A9C",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            #command=submit_3
                                            )
    sub_button_3.place(x=950,y=413)
    
    # CREATING RESET BUTTON
    reset_button_1 = customtkinter.CTkButton(master=app,
                                            text="ʀᴇꜱᴇᴛ",
                                            text_color="white",
                                            hover_color="#F11F32",
                                            fg_color="#F12B3D",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            #command=reset_1
                                            )
    reset_button_1.place(x=1150,y=153)

    reset_button_2 = customtkinter.CTkButton(master=app,
                                            text="ʀᴇꜱᴇᴛ",
                                            text_color="white",
                                            hover_color="#F11F32",
                                            fg_color="#F12B3D",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            #command=reset_2
                                            )
    reset_button_2.place(x=1150,y=283)

    reset_button_3 = customtkinter.CTkButton(master=app,
                                            text="ʀᴇꜱᴇᴛ",
                                            text_color="white",
                                            hover_color="#F11F32",
                                            fg_color="#F12B3D",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            #command=reset_3
                                            )
    reset_button_3.place(x=1150,y=413)
    
    # CREATING FRAME FOR SCHEDULING INFO
    schedule_frame = customtkinter.CTkFrame(master=app,
                                            width=900,
                                            height=230,
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=15)
    schedule_frame.place(x=10,y=500)
    
    # LABELS FOR SCHEDULING INFO
    num_label_1 = customtkinter.CTkLabel(master=schedule_frame,
                                            text="1. ",
                                            text_color="black",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8)
    num_label_1.place(x=0,y=30)
    
    snum_label_2 = customtkinter.CTkLabel(master=schedule_frame,
                                            text="2. ",
                                            text_color="black",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8)
    snum_label_2.place(x=0,y=90)
    
    num_label_3 = customtkinter.CTkLabel(master=schedule_frame,
                                            text="3. ",
                                            text_color="black", 
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8)
    num_label_3.place(x=0,y=150)
    
  
    schedule_label_1 = customtkinter.CTkLabel(master=schedule_frame,
                                            text="NON-SCHEDULED",
                                            text_color="black",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="red",
                                            corner_radius=8)
    schedule_label_1.place(x=90,y=30)
    
    sschedule_label_2 = customtkinter.CTkLabel(master=schedule_frame,
                                            text="NON-SCHEDULED",
                                            text_color="black",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="red",
                                            corner_radius=8)
    sschedule_label_2.place(x=90,y=90)
    
    schedule_label_3 = customtkinter.CTkLabel(master=schedule_frame, 
                                            text="NON-SCHEDULED",
                                            text_color="black", 
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="red",
                                            corner_radius=8)
    schedule_label_3.place(x=90,y=150)
    

    
    

    

    
    
    
    # QUIT BUTTON SECTION STARTS HERE
    quit_button = customtkinter.CTkButton(master=app,
                                            text="X",
                                            text_color="white",
                                            hover_color="#3A3A3A",
                                            fg_color="red",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            command=quit)
    quit_button.place(x=1250,y=10)
    
    # ********** END OF QUIT BUTTON SECTION **********
    
    
    
# Calling the home function
home()

# Running the mainloop
app.mainloop()