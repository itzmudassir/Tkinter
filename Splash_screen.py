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
app.configure(bg="white")

# FUNCTIONS SECTION
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
                                      
        label_1.place(x=40,y=130)
    else:
        label_1 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")
                                      
        label_1.place(x=40,y=130)
# ********** END OF THIS FUNCTION **********
        
# Defining the function for the Checkbox_2        
def checkbox_event_2():
    if(var2.get() == 1):
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="green",
                                      corner_radius=20,
                                      text_color="white")
        label_2.place(x=40,y=260)
    else:
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")
        label_2.place(x=40,y=260)
# ********** END OF THIS FUNCTION **********
        
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
        label_2.place(x=40,y=390)
    else:
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")
        label_2.place(x=40,y=390)
        
# ********** END OF THIS FUNCTION **********
        
# Creating the Functions for the First increment/decrement and Submit buttons

# Function for first Increment Button
def increase_value_1():
    global i
    if i<=99:
        
        i = i + 10
        value_label_1.configure(text=i)
# Function for the first decrement button    
def decrease_value_1():
    global i
    if i>=1:
        i = i - 10
        value_label_1.configure(text=i)
# Function for the first Submit Button       
def submit_1():
    file = open("i_value_1.txt","a")
    file.write(str(var1.get())+": "+str(i)+"\n")
    file.close()
# ********** END OF First increment/decrement and Submit buttons **********    
    
# Creating the functions for the second increment/decrement and Submit buttons

# Function for the second Increment Button 
def increase_value_2():
    global j
    if j<=99:
        
        j = j + 10
        value_label_2.configure(text=j)
    
# Function for the second decrement button
def decrease_value_2():
    global j
    if j>=1:
        j = j - 10
        value_label_2.configure(text=j)
# Function for the second Submit Button        
def submit_2():
    file = open("i_value_2.txt","a")
    file.write(str(var2.get())+": "+str(j)+"\n")
    file.close()
    
# ********** END OF Second increment/decrement and Submit buttons **********    
    
# Creating the functions for the third increment/decrement and Submit buttons
# Function for the third Increment Button
def increase_value_3():
    global k
    if k<=99:
        
        k = k + 10
        value_label_3.configure(text=k)
    
# Function for the third decrement button  
def decrease_value_3():
    global k
    if k>=1:
        k = k - 10
        value_label_3.configure(text=k)
# Function for the third Submit Button       
def submit_3():
    file = open("i_value_3.txt","a")
    file.write(str(var3.get())+": "+str(k)+"\n")
    file.close()
    
# ********** END OF Third increment/decrement and Submit buttons **********
    
        
# Main Function to run the program      
def home():
    global i 
    global j
    global k
    i = 0
    j = 0
    k = 0
    
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
    
    
    # Creating the title of the window
    title1=customtkinter.CTkLabel(master=app,
                                  text="Tech IQ Smart Packing System",
                                  text_font=("DM Sans", -42,BOLD),
                                  text_color="#3388FF")
    title1.place(x=440,y=10)
    
    # IMAGE SECTION STARTS HERE
    
    # Define our images
    up_arrow = ImageTk.PhotoImage(Image.open("Elements/up.png").resize((20,20)), Image.ANTIALIAS)
    down_arrow = ImageTk.PhotoImage(Image.open("Elements/down.png").resize((20,20)), Image.ANTIALIAS)
    
    
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
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")
                                      
    label_1.place(x=40,y=130)
    
    label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")
    label_2.place(x=40,y=260)
    
    label_3 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("System", 15,BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")
    label_3.place(x=40,y=390)
    # ********** END OF CHECKBOX LABEL SECTION **********
    
    # INCREMENT BUTTON SECTION STARTS HERE
    inc_button_1 = customtkinter.CTkButton(master=app,
                                            text="Increase",
                                            image=up_arrow,
                                            compound="left",
                                            text_color="white",
                                            hover_color="white",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            command=increase_value_1)
                                            
    inc_button_1.place(x=300,y=160)
    
    inc_button_2 = customtkinter.CTkButton(master=app,
                                            text="Increase",
                                            text_color="white",
                                            hover_color="green",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            command=increase_value_2)
                                            
    inc_button_2.place(x=300,y=290)
    
    inc_button_3 = customtkinter.CTkButton(master=app,
                                            text="Increase",
                                            text_color="white",
                                            hover_color="green",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            command=increase_value_3)
                                            
    inc_button_3.place(x=300,y=420)
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
                                            
    dec_button_1.place(x=300,y=100)
    
    dec_button_2 = customtkinter.CTkButton(master=app,
                                            text="Decrease",
                                            text_color="white",
                                            hover_color="red",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            command=decrease_value_2)
                                            
    dec_button_2.place(x=300,y=230)
    
    dec_button_3 = customtkinter.CTkButton(master=app,
                                            text="Decrease",
                                            text_color="white",
                                            hover_color="red",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("System", 15,BOLD),
                                            command=decrease_value_3)
                                            
    dec_button_3.place(x=300,y=360)
    # ********** END OF DECREMENT BUTTON SECTION **********
    
    # INREMENR/DECREMENT VALUE LABEL SECTION STARTS HERE
    value_label_1 = customtkinter.CTkLabel(master=app,
                                         text="0",
                                         text_font=("System", 15,BOLD),
                                         bg_color="white",
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
                                         bg_color="white",
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
                                         bg_color="white",
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