import customtkinter
from PIL import ImageTk,Image
from tkinter.font import BOLD

# Appearence of the window
customtkinter.set_appearance_mode("Light") #dark mode and light mood
customtkinter.set_default_color_theme("blue")

# Creating the window
app=customtkinter.CTk()
app.wm_attributes('-fullscreen','True')
app.configure(bg="white")


def increase_clock_hours_1():
    global h1
    if h1<=23:
        h1 = h1 + 1
        hour_label_1.configure(text=h1)
        if h1<10:
            hour_label_1.configure(text="0"+str(h1))
            
def decrease_clock_hours_1():
    global h1
    if h1>=1:
        h1 = h1 - 1
        hour_label_1.configure(text=h1)
        if h1<10:
            hour_label_1.configure(text="0"+str(h1))
def increase_clock_minutes_1():
    global m1
    if m1<=59:
        m1 = m1 + 1
        minute_label_1.configure(text=m1)
        if m1<10:
            minute_label_1.configure(text="0"+str(m1))
            
def decrease_clock_minutes_1():
    global m1    
    if m1>=1:
        m1 = m1 - 1
        minute_label_1.configure(text=m1)
        if m1<10:
            minute_label_1.configure(text="0"+str(m1))
            
def increase_clock_seconds_1():
    global s1
    if s1<=59:
        s1 = s1 + 1
        second_label_1.configure(text=s1)
        if s1<10:
            second_label_1.configure(text="0"+str(s1))
            
def decrease_clock_seconds_1():
    global s1
    if s1>=1:
        s1 = s1 - 1
        second_label_1.configure(text=s1)
        if s1<10:
            second_label_1.configure(text="0"+str(s1))

def home():
    global h1
    global m1
    global s1
    global hour_label_1  # Making the first hour_label global
    global minute_label_1  # Making the first minute_label global
    global second_label_1  # Making the first second_label global
    h1= 0
    m1 = 0
    s1 = 0
    up_arrow = ImageTk.PhotoImage(Image.open("Elements\\up-arrow_1.png").resize((35,35)), Image.ANTIALIAS)
    down_arrow = ImageTk.PhotoImage(Image.open("Elements\\chevron.png").resize((35,35)), Image.ANTIALIAS)
    light_off = ImageTk.PhotoImage(Image.open("Elements\\light_off.png").resize((30,30)), Image.ANTIALIAS)
    light_on = ImageTk.PhotoImage(Image.open("Elements\\light_on.png").resize((30,30)), Image.ANTIALIAS)
    calender = ImageTk.PhotoImage(Image.open("Elements\calendar.png").resize((40,40)), Image.ANTIALIAS)
    clock = ImageTk.PhotoImage(Image.open("Elements\\clock.png").resize((40,40)), Image.ANTIALIAS)
    
    
    inch_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_hours_1
                                            )
                                            
    inch_button_1.place(x=420,y=112)
    
    incm_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_minutes_1
                                            )
    incm_button_1.place(x=480,y=112)
    
    incs_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_seconds_1
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
                                            command=decrease_clock_hours_1
                                            )
    dech_button_1.place(x=420,y=186)
    
    decm_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=decrease_clock_minutes_1
                                            )
    decm_button_1.place(x=480,y=186)
    
    decs_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=decrease_clock_seconds_1
                                            )
    decs_button_1.place(x=540,y=186)
home()
app.mainloop()