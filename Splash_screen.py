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


# Appearence of the window
customtkinter.set_appearance_mode("Light") #dark mode and light mood
customtkinter.set_default_color_theme("blue")

# Creating the window
app=customtkinter.CTk()
app.wm_attributes('-fullscreen','True')
app.configure(bg="#F21350")

# CHECKBOXES FUNCTIONS STARTS HERE
def checkbox_event_1():
    if(var1.get() == 1):
        label_1 = customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("System", 15,BOLD),
                                      bg_color="#F21350",
                                      fg_color="yellow",
                                      corner_radius=20,
                                      text_color="black")
                                      
        label_1.place(x=40,y=130)
    else:
        label_1 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="#F21350",
                                      fg_color="black",
                                      corner_radius=20,
                                      text_color="white")
                                      
        label_1.place(x=40,y=130)

               
def checkbox_event_2():
    if(var2.get() == 1):
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("System", 15,BOLD),
                                      bg_color="#F21350",
                                      fg_color="yellow",
                                      corner_radius=20,
                                      text_color="black")
        label_2.place(x=40,y=260)
    else:
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="#F21350",
                                      fg_color="black",
                                      corner_radius=20,
                                      text_color="white")
        label_2.place(x=40,y=260)

     
def checkbox_event_3():
    if(var3.get() == 1):
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("System", 15,BOLD),
                                      bg_color="#F21350",
                                      fg_color="yellow",
                                      corner_radius=20,
                                      text_color="black")
        label_2.place(x=40,y=390)
    else:
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="#F21350",
                                      fg_color="black",
                                      corner_radius=20,
                                      text_color="white")
        label_2.place(x=40,y=390)
        
# CHECKBOXES FUNCTIONS ENDS HERE
        
# INCREMENT BUTTONS FUNCTIONS STARTS HERE
def increase_value_1():
    global i
    if i<=99:
        
        i = i + 10
        value_label_1.configure(text=i)
        
def increase_value_2():
    global j
    if j<=99:
        
        j = j + 10
        value_label_2.configure(text=j)        
        
def increase_value_3():
    global k
    if k<=99:
        
        k = k + 10
        value_label_3.configure(text=k)
# INCREMENT BUTTONS FUNCTIONS ENDS HERE

# DECREMENT BUTTONS FUNCTIONS STARTS HERE
def decrease_value_1():
    global i
    if i>=1:
        i = i - 10
        value_label_1.configure(text=i)        
        
def decrease_value_2():
    global j
    if j>=1:
        j = j - 10
        value_label_2.configure(text=j)        
        
def decrease_value_3():
    global k
    if k>=1:
        k = k - 10
        value_label_3.configure(text=k)        
# DECREMENT BUTTONS FUNCTIONS ENDS HERE

# Submit Button Functions Starts Here            
def submit_1():
    file = open("i_value_1.txt","a")
    file.write(str(var1.get())+": "+str(i)+"\n")
    file.close()

        
def submit_2():
    file = open("i_value_2.txt","a")
    file.write(str(var2.get())+": "+str(j)+"\n")
    file.close()
    
       
def submit_3():
    file = open("i_value_3.txt","a")
    file.write(str(var3.get())+": "+str(k)+"\n")
    file.close()
# Submit Button Functions Ends Here

# Clock Hours INCREMENT functions Starts Here
def increase_clock_hours_1():
    global h
    if h<=23:
        h = h + 1
        hour_label_1.configure(text=h)
        
        
        
# Clock Hours DECREMENT functions Starts Here
def decrease_clock_hours_1():
    global h
    if h>=1:
        h = h - 1
        hour_label_1.configure(text=h)
    
    
    
    
 # Clock Minutes INCREMENT functions Starts Here
def increase_clock_minutes_1():
    global m
    if m<=59:
        m = m + 1
        minute_label_1.configure(text=m)
        
        
        
        
# Clock Minutes DECREMENT functions Starts Here
def decrease_clock_minutes_1():
    global m    
    if m>=1:
        m = m - 1
        minute_label_1.configure(text=m)
        
        
        
# Clock Seconds INCREMENT functions Starts Here
def increase_clock_seconds_1():
    global s
    if s<=59:
        s = s + 1
        second_label_1.configure(text=s)
        
        
        
# Clock Seconds DECREMENT functions Starts Here
def decrease_clock_seconds_1():
    global s
    if s>=1:
        s = s - 1
        second_label_1.configure(text=s)
        
# Main Function to run the program      
def home():
    global i 
    global j
    global k
    global h
    global m
    global s
    i = 0
    j = 0
    k = 0
    h = 0
    m = 0
    s = 0
    
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
    
    
    
    # Creating the title of the window
    title1=customtkinter.CTkLabel(master=app,
                                  text="Tech IQ Smart Packing System",
                                  text_font=("DM Sans", -42,BOLD),
                                  text_color="white")
    title1.place(x=440,y=10)
    
    # IMAGE SECTION STARTS HERE
    
    # Define our images
    up_arrow = ImageTk.PhotoImage(Image.open("up_squared.png").resize((20,20)), Image.ANTIALIAS)
    down_arrow = ImageTk.PhotoImage(Image.open("down_squared.png").resize((20,20)), Image.ANTIALIAS)
    
    
    # CHECKBOX SECTION STARTS HERE
    checkbox_1 = customtkinter.CTkCheckBox(master=app,
                                           command=checkbox_event_1,
                                           variable=var1,
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_1.place(x=10, y = 130)
    
    checkbox_2 = customtkinter.CTkCheckBox(master=app, command=checkbox_event_2,
                                           variable=var2,
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_2.place(x=10, y = 260)
    
    checkbox_3 = customtkinter.CTkCheckBox(master=app, command=checkbox_event_3,
                                           variable=var3,
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_3.place(x=10, y = 390)
    # ********** END OF CHECKBOX SECTION **********
    
    # CHECKBOX LABEL SECTION STARTS HERE
    label_1 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="#F21350",
                                      fg_color="black",
                                      corner_radius=20,
                                      text_color="white")
                                      
    label_1.place(x=40,y=130)
    
    label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="#F21350",
                                      fg_color="black",
                                      corner_radius=20,
                                      text_color="white")
    label_2.place(x=40,y=260)
    
    label_3 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="#F21350",
                                      fg_color="black",
                                      corner_radius=20,
                                      text_color="white")
    label_3.place(x=40,y=390)
    # ********** END OF CHECKBOX LABEL SECTION **********
    
    # INCREMENT BUTTON SECTION STARTS HERE
    inc_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            #width=200, height=50,
                                            command=increase_value_1)
                                            
    inc_button_1.place(x=300,y=100)
    
    inc_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            #width=200, height=50,
                                            command=increase_value_2)
                                            
    inc_button_2.place(x=300,y=230)
    
    inc_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            #width=200, height=50,
                                            command=increase_value_3)
                                            
    inc_button_3.place(x=300,y=360)
    # ********** END OF INCREMENT BUTTON SECTION **********
    
    # DECREMENT BUTTON SECTION STARTS HERE
    dec_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            #width=200, height=50,
                                            command=decrease_value_1)
                                            
    dec_button_1.place(x=300,y=160)
    
    dec_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            #width=200, height=50,
                                            command=decrease_value_2)
                                            
    dec_button_2.place(x=300,y=290)
    
    dec_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            #width=200, height=50,
                                            command=decrease_value_3)
                                            
    dec_button_3.place(x=300,y=420)
    # ********** END OF DECREMENT BUTTON SECTION **********
    
    # INREMENR/DECREMENT VALUE LABEL SECTION STARTS HERE
    value_label_1 = customtkinter.CTkLabel(master=app,
                                         text="0",
                                         text_font=("System", 15,BOLD),
                                         bg_color="#F21350",
                                         fg_color="gray",
                                         corner_radius=8,
                                         text_color="black",
                                        #  width=20,
                                        #  height=10
                                        )
                                         
                                             
    value_label_1.place(x=300,y=130)
    
    value_label_2 = customtkinter.CTkLabel(master=app,
                                         text="0",
                                         text_font=("System", 15,BOLD),
                                         bg_color="#F21350",
                                         fg_color="gray",
                                         corner_radius=8,
                                         text_color="black",
                                        #  width=20,
                                        #  height=10
                                        )
                                         
                                             
    value_label_2.place(x=300,y=260)
    
    value_label_3 = customtkinter.CTkLabel(master=app,
                                         text="0",
                                         text_font=("System", 15,BOLD),
                                         bg_color="#F21350",
                                         fg_color="gray",
                                         corner_radius=8,
                                         text_color="black",
                                        #  width=20,
                                        #  height=10
                                        )
                                         
                                             
    value_label_3.place(x=300,y=390)
    # ********** END OF INCREMENT/DECREMENT VALUE LABEL SECTION **********
    
    # SUBMIT BUTTON SECTION STARTS HERE
    sub_button_1 = customtkinter.CTkButton(master=app,
                                            text="Submit",
                                            text_color="white",
                                            hover_color="blue",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            command=submit_1)
    sub_button_1.place(x=450,y=130)
    
    sub_button_2 = customtkinter.CTkButton(master=app,
                                            text="Submit",
                                            text_color="white",
                                            hover_color="blue",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            command=submit_2)
    sub_button_2.place(x=450,y=260)
    
 
    sub_button_3 = customtkinter.CTkButton(master=app,
                                            text="Submit",
                                            text_color="white",
                                            hover_color="blue",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            command=submit_3)
    sub_button_3.place(x=450,y=390)
    # ********** END OF SUBMIT BUTTON SECTION **********
    
    # CREATING A CLOCK
    # CLOCK HOUR LABEL SECTION STARTS HERE
    hour_label_1 = customtkinter.CTkLabel(master=app,
                                         text="00",
                                         text_font=("System", 15,BOLD),
                                         bg_color="#F21350",
                                         fg_color="gray",
                                         corner_radius=8,
                                         text_color="black",
                                          width=20,
                                          height=10
                                        )
                                         
                                             
    hour_label_1.place(x=800,y=130)
    
    hour_label_2 = customtkinter.CTkLabel(master=app,
                                         text="00",
                                         text_font=("System", 15,BOLD),
                                         bg_color="#F21350",
                                         fg_color="gray",
                                         corner_radius=8,
                                         text_color="black",
                                          width=20,
                                          height=10
                                        )
                                         
                                             
    hour_label_2.place(x=800,y=260)
    
    hour_label_3 = customtkinter.CTkLabel(master=app,
                                         text="00",
                                         text_font=("System", 15,BOLD),
                                         bg_color="#F21350",
                                         fg_color="gray",
                                         corner_radius=8,
                                         text_color="black",
                                          width=20,
                                          height=10
                                        )
                                         
                                             
    hour_label_3.place(x=800,y=390)
    # ********** END OF CLOCK HOUR LABEL SECTION **********
    
    
    # CLOCK MINUTE LABEL SECTION STARTS HERE
    minute_label_1 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("System", 15,BOLD),
                                            bg_color="#F21350",
                                            fg_color="gray",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    minute_label_1.place(x=860,y=130)
    
    minute_label_2 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("System", 15,BOLD),
                                            bg_color="#F21350",
                                            fg_color="gray",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    minute_label_2.place(x=860,y=260)
    
    minute_label_3 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("System", 15,BOLD),
                                            bg_color="#F21350",
                                            fg_color="gray",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    minute_label_3.place(x=860,y=390)
    # ********** END OF CLOCK MINUTE LABEL SECTION **********
     
    
    # CLOCK SECOND LABEL SECTION STARTS HERE
    second_label_1 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("System", 15,BOLD),
                                            bg_color="#F21350",
                                            fg_color="gray",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    second_label_1.place(x=920,y=130)
    
    second_label_2 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("System", 15,BOLD),
                                            bg_color="#F21350",
                                            fg_color="gray",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    second_label_2.place(x=920,y=260)
    
    second_label_3 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("System", 15,BOLD),
                                            bg_color="#F21350",
                                            fg_color="gray",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    second_label_3.place(x=920,y=390)
    
    
    
    
    
    
    
    
    # CLOCK HOUR INCREMENT BUTTON SECTION STARTS HERE
    inch_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_hours_1
                                            )
                                            
    inch_button_1.place(x=800,y=100)
    
    inch_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_hours_1
                                            )
                                            
    inch_button_2.place(x=800,y=230)
    
    inch_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_hours_1
                                            )
                                            
    inch_button_3.place(x=800,y=360)
    # ********** END OF CLOCK HOUR INCREMENT BUTTON SECTION **********
    
    
    # CLOCK HOUR DECREMENT BUTTON SECTION STARTS HERE
    dech_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_hours_1
                                            )
    dech_button_1.place(x=800,y=150)
    
    dech_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_hours_1
                                            )
    dech_button_2.place(x=800,y=280)
    
    dech_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_hours_1
                                            )
    dech_button_3.place(x=800,y=410)
    # ********** END OF CLOCK HOUR DECREMENT BUTTON SECTION **********
    
    # CLOCK MINUTE INCREMENT BUTTON SECTION STARTS HERE
    incm_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_minutes_1
                                            )
    incm_button_1.place(x=860,y=100)
    
    incm_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_minutes_1
                                            )
    incm_button_2.place(x=860,y=230)
    
    incm_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_minutes_1
                                            )
    incm_button_3.place(x=860,y=360)
    # ********** END OF CLOCK MINUTE INCREMENT BUTTON SECTION **********
    

    # CLOCK MINUTE DECREMENT BUTTON SECTION STARTS HERE
    decm_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_minutes_1
                                            )
    decm_button_1.place(x=860,y=150)
    
    decm_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_minutes_1
                                            )
    decm_button_2.place(x=860,y=280)
    
    decm_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_minutes_1
                                            )
    decm_button_3.place(x=860,y=410)
    # ********** END OF CLOCK MINUTE DECREMENT BUTTON SECTION *********
    
    
    # CLOCK SECOND INCREMENT BUTTON SECTION STARTS HERE
    incs_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_seconds_1
                                            )
    incs_button_1.place(x=920,y=100)
    
    incs_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_seconds_1
                                            )
    incs_button_2.place(x=920,y=230)
    
    incs_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_seconds_1
                                            )
    incs_button_3.place(x=920,y=360)
    # ********** END OF CLOCK SECOND INCREMENT BUTTON SECTION **********
    
    
    # CLOCK SECOND DECREMENT BUTTON SECTION STARTS HERE
    decs_button_1 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_seconds_1
                                            )
    decs_button_1.place(x=920,y=150)
    
    decs_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_seconds_1
                                            )
    decs_button_2.place(x=920,y=280)
    
    decs_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_seconds_1
                                            )
    decs_button_3.place(x=920,y=410)
    # ********** END OF CLOCK SECOND DECREMENT BUTTON SECTION *********
    

    # QUIT BUTTON SECTION STARTS HERE
    quit_button = customtkinter.CTkButton(master=app,
                                            text="X",
                                            text_color="white",
                                            hover_color="#3A3A3A",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            command=quit)
    quit_button.place(x=1250,y=10)
    
    
    
    

    
# Creating the Splash Screen
frame1=customtkinter.CTkFrame(master=app,           # Creating the frame for the splash screen
                              width=240,
                              corner_radius=20,
                              fg_color="white")
frame1.place(x=0 ,y=0,width=1366,height=768)
logo=ImageTk.PhotoImage(Image.open("Elements\iub_logo_1.png"))  # Importing the logo
label_photo= customtkinter.CTkLabel(master=frame1,image=logo)
label_photo.pack()

app.after(3000,frame1.destroy)    # Destroying the splash screen after 3 seconds
app.after(3000,home)              # Calling the home function after 3 seconds



# Running the mainloop
app.mainloop()