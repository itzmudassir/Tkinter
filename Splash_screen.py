# PROGRAMMED BY: Muhammad Mudassir

# Impoting Libraries
from cProfile import label
from ctypes import resize
from doctest import master
from email.mime import audio
import tkinter
from tkinter import font
from turtle import title, width
import customtkinter
from PIL import ImageTk,Image
from matplotlib import image
import threading
import time
from tkinter.font import BOLD


# Appearence of the window
customtkinter.set_appearance_mode("Light") #dark mode and light mood
customtkinter.set_default_color_theme("blue")

# Creating the window
app=customtkinter.CTk()
app.wm_attributes('-fullscreen','True')
app.configure(bg="white")

# Defining the function for the checkbox_1
def checkbox_event_1():
    if(var1.get() == 1):
        label_1 = customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="green",
                                      corner_radius=20,
                                      text_color="white")
                                      
        label_1.place(x=40,y=100)
    else:
        label_1 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")
                                      
        label_1.place(x=40,y=100)
        
# Defining the function for the checkbox_2        
def checkbox_event_2():
    if(var2.get() == 1):
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="green",
                                      corner_radius=20,
                                      text_color="white")
        label_2.place(x=40,y=150)
    else:
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")
        label_2.place(x=40,y=150)
        
# Defining the function for the checkbox_3        
def checkbox_event_3():
    if(var3.get() == 1):
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="green",
                                      corner_radius=20,
                                      text_color="white")
        label_2.place(x=40,y=200)
    else:
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")
        label_2.place(x=40,y=200)
        

# Defining the function for increasing the value of the value label

def increase_value():
    global i
    if i<=99:
        
        i = i + 10
        value_label.configure(text=i)
    
# Creating the decrease function to decrease the value of the value label   
def decrease_value():
    global i
    if i>=1:
        i = i - 10
        value_label.configure(text=i)
# Creating Submit Function to Sava data in the file        
def submit():
    file = open("i_value.txt","a")
    file.write(str(i)+"\n")
    file.close()
    
        
# Defining the function for the Home Page        
def home():
    global i 
    i = 0
    
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
    
    global dec_button   # Making the dec_button global
    global inc_button   # Making the inc_button global
    global value_label  # Making the value_label global
    
    # Creating the title of the window
    title1=customtkinter.CTkLabel(master=app,
                                  text="Tech IQ Smart Packing System",
                                  text_font=("DM Sans", -42,BOLD),
                                  text_color="#3388FF")
    title1.place(x=440,y=10)
    
    # Creating a button to decrease the value of the label
    dec_button = customtkinter.CTkButton(master=app,
                                            text="Decrease",
                                            text_color="white",
                                            hover_color="red",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            command=decrease_value)
                                            
    dec_button.place(x=500,y=100)
    # Creating a label to display the value
    value_label = customtkinter.CTkLabel(master=app,
                                         text="0",
                                         text_font=("System", 15,BOLD),
                                         bg_color="white",
                                         fg_color="gray",
                                         corner_radius=8,
                                         text_color="black",
                                        #  width=20,
                                        #  height=10
                                        )
                                         
                                             
    value_label.place(x=700,y=125)
    # Creating a button to increase the value of the label
    inc_button = customtkinter.CTkButton(master=app,
                                            text="Increase",
                                            text_color="white",
                                            hover_color="green",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            command=increase_value)
                                            
    inc_button.place(x=500,y=150)
    
    
    # Creating the checkbox_1
    checkbox_1 = customtkinter.CTkCheckBox(master=app,
                                           command=checkbox_event_1,
                                           variable=var1,
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_1.place(x=10, y = 100)
    # Creating the label_1
    label_1 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")
                                      
    label_1.place(x=40,y=100)
    # Creating the checkbox_2
    checkbox_2 = customtkinter.CTkCheckBox(master=app, command=checkbox_event_2,
                                           variable=var2,
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_2.place(x=10, y = 150)
    # Creating the label_2
    label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")
    label_2.place(x=40,y=150)
    # Creating the checkbox_3
    checkbox_3 = customtkinter.CTkCheckBox(master=app, command=checkbox_event_3,
                                           variable=var3,
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_3.place(x=10, y = 200)
    # Creating the label_3
    label_3 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")
    label_3.place(x=40,y=200)
    
    # Creating the button to Submit the data
    sub_button = customtkinter.CTkButton(master=app,
                                            text="Submit",
                                            text_color="white",
                                            hover_color="blue",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            command=submit)
    sub_button.place(x=500,y=200)
    

    
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