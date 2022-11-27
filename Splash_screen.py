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

# CHECKBOXES FUNCTIONS STARTS HERE
def checkbox_event_1():
    if(var1.get() == 1):
        label_1 = customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="green",
                                      corner_radius=13,
                                      text_color="white")
                                      
        label_1.place(x=40,y=130)
    else:
        label_1 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
                                      text_color="white")
                                      
        label_1.place(x=40,y=130)

               
def checkbox_event_2():
    if(var2.get() == 1):
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="green",
                                      corner_radius=13,
                                      text_color="white")
        label_2.place(x=40,y=260)
    else:
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
                                      text_color="white")
        label_2.place(x=40,y=260)

     
def checkbox_event_3():
    if(var3.get() == 1):
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="green",
                                      corner_radius=13,
                                      text_color="white")
        label_2.place(x=40,y=390)
    else:
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
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
    file = open("i_value_1.txt","w")
    file.write(str(var1.get())+": "+str(i)+"\n"+"Starting Time: ")
    if h1<10:
        file.write("0"+str(h1)+":")
    else:
        file.write(str(h1)+":")
    if m1<10:
        file.write("0"+str(m1)+":")
    else:
        file.write(str(m1)+":")
    if s1<10:
        file.write("0"+str(s1)+"\n")
    else:
        file.write(str(s1)+"\n")
    file.write("Ending Time: ") 
    if h11<10:
        file.write("0"+str(h11)+":")
    else:
        file.write(str(h11)+":")
    if m11<10:
        file.write("0"+str(m11)+":")
    else:
        file.write(str(m11)+":")
    if s11<10:
        file.write("0"+str(s11)+"\n")
    else:
        file.write(str(s11)+"\n")
               
    file.close()
    
    file = open("i_value_1.txt", "r")
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    modified = modified[0][0]
    if modified == "1":
        first_label_11.configure(text="SCHEDULED")
        first_label_11.configure(text_color="white")
        
    else:
        first_label_11.configure(text="NON-SCHEDULED")
        first_label_11.configure(text_color="black")
       

        
def submit_2():
    file = open("i_value_2.txt","w")
    file.write(str(var2.get())+": "+str(j)+"\n"+"Starting Time: ")
    if h2<10:
        file.write("0"+str(h2)+":")
    else:
        file.write(str(h2)+":")
    if m2<10:
        file.write("0"+str(m2)+":")
    else:
        file.write(str(m2)+":")
    if s2<10:
        file.write("0"+str(s2)+"\n")
    else:
        file.write(str(s2)+"\n")
    file.write("Ending Time: ")
    if h22<10:
        file.write("0"+str(h22)+":")
    else:
        file.write(str(h22)+":")
    if m22<10:
        file.write("0"+str(m22)+":")
    else:
        file.write(str(m22)+":")
    if s22<10:
        file.write("0"+str(s22)+"\n")
    else:
        file.write(str(s22)+"\n")
    file.close()
    
    file = open("i_value_2.txt", "r")
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    modified = modified[0][0]
    if modified == "1":
        second_label_11.configure(text="SCHEDULED")
        second_label_11.configure(text_color="white")
        
    else:
        second_label_11.configure(text="NON-SCHEDULED")
        second_label_11.configure(text_color="black")
    
       
def submit_3():
    file = open("i_value_3.txt","w")
    file.write(str(var3.get())+": "+str(k)+"\n"+"Starting Time: ")
    if h3<10:
        file.write("0"+str(h3)+":")
    else:
        file.write(str(h3)+":")
    if m3<10:
        file.write("0"+str(m3)+":")
    else:
        file.write(str(m3)+":")
    if s3<10:
        file.write("0"+str(s3)+"\n")
    else:
        file.write(str(s3)+"\n")
    file.write("Ending Time: ")
    if h33<10:
        file.write("0"+str(h33)+":")
    else:
        file.write(str(h33)+":")
    if m33<10:
        file.write("0"+str(m33)+":")
    else:
        file.write(str(m33)+":")
    if s33<10:
        file.write("0"+str(s33)+"\n")
    else:
        file.write(str(s33)+"\n")
    file.close()
    
    file = open("i_value_3.txt", "r")
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    modified = modified[0][0]
    if modified == "1":
        third_label_11.configure(text="SCHEDULED")
        third_label_11.configure(text_color="white")
        
    else:
        third_label_11.configure(text="NON-SCHEDULED")
        third_label_11.configure(text_color="black")
    
# Submit Button Functions Ends Here

# Clock Hours INCREMENT functions Starts Here
def increase_clock_hours_1():
    global h1
    if h1<=23:
        h1 = h1 + 1
        hour_label_1.configure(text=h1)
        if h1<10:
            hour_label_1.configure(text="0"+str(h1))
        
def increase_clock_hours_2():
    global h2
    if h2<=23:
        h2 = h2 + 1
        hour_label_2.configure(text=h2)
        if h2<10:
            hour_label_2.configure(text="0"+str(h2))
        
def increase_clock_hours_3():
    global h3
    if h3<=23:
        h3 = h3 + 1
        hour_label_3.configure(text=h3)
        if h3<10:
            hour_label_3.configure(text="0"+str(h3))
# Clock Hours INCREMENT functions Ends Here
        
              
# Clock Hours DECREMENT functions Starts Here
def decrease_clock_hours_1():
    global h1
    if h1>=1:
        h1 = h1 - 1
        hour_label_1.configure(text=h1)
        if h1<10:
            hour_label_1.configure(text="0"+str(h1))
        
def decrease_clock_hours_2():
    global h2
    if h2>=1:
        h2 = h2 - 1
        hour_label_2.configure(text=h2)
        if h2<10:
            hour_label_2.configure(text="0"+str(h2))
        
def decrease_clock_hours_3():
    global h3
    if h3>=1:
        h3 = h3 - 1
        hour_label_3.configure(text=h3)
        if h3<10:
            hour_label_3.configure(text="0"+str(h3))
# Clock Hours DECREMENT functions Ends Here
    
     
 # Clock Minutes INCREMENT functions Starts Here
def increase_clock_minutes_1():
    global m1
    if m1<=59:
        m1 = m1 + 1
        minute_label_1.configure(text=m1)
        if m1<10:
            minute_label_1.configure(text="0"+str(m1))
        
def increase_clock_minutes_2():
    global m2
    if m2<=59:
        m2 = m2 + 1
        minute_label_2.configure(text=m2)
        if m2<10:
            minute_label_2.configure(text="0"+str(m2))
        
def increase_clock_minutes_3():
    global m3
    if m3<=59:
        m3 = m3 + 1
        minute_label_3.configure(text=m3)
        if m3<10:
            minute_label_3.configure(text="0"+str(m3))
# Clock Minutes INCREMENT functions Ends Here
        
        
# Clock Minutes DECREMENT functions Starts Here
def decrease_clock_minutes_1():
    global m1    
    if m1>=1:
        m1 = m1 - 1
        minute_label_1.configure(text=m1)
        if m1<10:
            minute_label_1.configure(text="0"+str(m1))
        
def decrease_clock_minutes_2():
    global m2
    if m2>=1:
        m2 = m2 - 1
        minute_label_2.configure(text=m2)
        if m2<10:
            minute_label_2.configure(text="0"+str(m2))
        
def decrease_clock_minutes_3():
    global m3
    if m3>=1:
        m3 = m3 - 1
        minute_label_3.configure(text=m3)
        if m3<10:
            minute_label_3.configure(text="0"+str(m3))
# Clock Minutes DECREMENT functions Ends Here
        
        
        
# Clock Seconds INCREMENT functions Starts Here
def increase_clock_seconds_1():
    global s1
    if s1<=59:
        s1 = s1 + 1
        second_label_1.configure(text=s1)
        if s1<10:
            second_label_1.configure(text="0"+str(s1))
        
def increase_clock_seconds_2():
    global s2
    if s2<=59:
        s2 = s2 + 1
        second_label_2.configure(text=s2)
        if s2<10:
            second_label_2.configure(text="0"+str(s2))
        
def increase_clock_seconds_3():
    global s3
    if s3<=59:
        s3 = s3 + 1
        second_label_3.configure(text=s3)
        if s3<10:
            second_label_3.configure(text="0"+str(s3))
# Clock Seconds INCREMENT functions Ends Here
          
        
# Clock Seconds DECREMENT functions Starts Here
def decrease_clock_seconds_1():
    global s1
    if s1>=1:
        s1 = s1 - 1
        second_label_1.configure(text=s1)
        if s1<10:
            second_label_1.configure(text="0"+str(s1))
        
def decrease_clock_seconds_2():
    global s2
    if s2>=1:
        s2 = s2 - 1
        second_label_2.configure(text=s2)
        if s2<10:
            second_label_2.configure(text="0"+str(s2))
def decrease_clock_seconds_3():
    global s3
    if s3>=1:
        s3 = s3 - 1
        second_label_3.configure(text=s3)
        if s3<10:
            second_label_3.configure(text="0"+str(s3))
# Clock Seconds DECREMENT functions Ends Here


# Second Clock Hours INCREMENT functions Starts Here
def increase_clock_hours_11():
    global h11
    if h11<=23:
        h11 = h11 + 1
        hour_label_11.configure(text=h11)
        if h11<10:
            hour_label_11.configure(text="0"+str(h11))
        
def increase_clock_hours_22():
    global h22
    if h22<=23:
        h22 = h22 + 1
        hour_label_22.configure(text=h22)
        if h22<10:
            hour_label_22.configure(text="0"+str(h22))
        
def increase_clock_hours_33():
    global h33
    if h33<=23:
        h33 = h33 + 1
        hour_label_33.configure(text=h33)
        if h33<10:
            hour_label_33.configure(text="0"+str(h33))
# Clock Hours INCREMENT functions Ends Here
        
              
# Clock Hours DECREMENT functions Starts Here
def decrease_clock_hours_11():
    global h11
    if h11>=1:
        h11 = h11 - 1
        hour_label_11.configure(text=h11)
        if h11<10:
            hour_label_11.configure(text="0"+str(h11))
        
def decrease_clock_hours_22():
    global h22
    if h22>=1:
        h22 = h22 - 1
        hour_label_22.configure(text=h22)
        if h22<10:
            hour_label_22.configure(text="0"+str(h22))
        
def decrease_clock_hours_33():
    global h33
    if h33>=1:
        h33 = h33 - 1
        hour_label_33.configure(text=h33)
        if h33<10:
            hour_label_33.configure(text="0"+str(h33))
# Clock Hours DECREMENT functions Ends Here
    
     
 # Clock Minutes INCREMENT functions Starts Here
def increase_clock_minutes_11():
    global m11
    if m11<=59:
        m11 = m11 + 1
        minute_label_11.configure(text=m11)
        if m11<10:
            minute_label_11.configure(text="0"+str(m11))
        
def increase_clock_minutes_22():
    global m22
    if m22<=59:
        m22 = m22 + 1
        minute_label_22.configure(text=m22)
        if m22<10:
            minute_label_22.configure(text="0"+str(m22))
        
def increase_clock_minutes_33():
    global m33
    if m33<=59:
        m33 = m33 + 1
        minute_label_33.configure(text=m33)
        if m33<10:
            minute_label_33.configure(text="0"+str(m33))
# Clock Minutes INCREMENT functions Ends Here
        
        
# Clock Minutes DECREMENT functions Starts Here
def decrease_clock_minutes_11():
    global m11    
    if m11>=1:
        m11 = m11 - 1
        minute_label_11.configure(text=m11)
        if m11<10:
            minute_label_11.configure(text="0"+str(m11))
        
def decrease_clock_minutes_22():
    global m22
    if m22>=1:
        m22 = m22 - 1
        minute_label_22.configure(text=m22)
        if m22<10:
            minute_label_22.configure(text="0"+str(m22))
        
def decrease_clock_minutes_33():
    global m33
    if m33>=1:
        m33 = m33 - 1
        minute_label_33.configure(text=m33)
        if m33<10:
            minute_label_33.configure(text="0"+str(m33))
# Clock Minutes DECREMENT functions Ends Here
        
        
        
# Clock Seconds INCREMENT functions Starts Here
def increase_clock_seconds_11():
    global s11
    if s11<=59:
        s11 = s11 + 1
        second_label_11.configure(text=s11)
        if s11<10:
            second_label_11.configure(text="0"+str(s11))
        
def increase_clock_seconds_22():
    global s22
    if s22<=59:
        s22 = s22 + 1
        second_label_22.configure(text=s22)
        if s22<10:
            second_label_22.configure(text="0"+str(s22))
        
def increase_clock_seconds_33():
    global s33
    if s33<=59:
        s33 = s33 + 1
        second_label_33.configure(text=s33)
        if s33<10:
            second_label_33.configure(text="0"+str(s33))
# Clock Seconds INCREMENT functions Ends Here
          
        
# Clock Seconds DECREMENT functions Starts Here
def decrease_clock_seconds_11():
    global s11
    if s11>=1:
        s11 = s11 - 1
        second_label_11.configure(text=s11)
        if s11<10:
            second_label_11.configure(text="0"+str(s11))
        
def decrease_clock_seconds_22():
    global s22
    if s22>=1:
        s22 = s22 - 1
        second_label_22.configure(text=s22)
        if s22<10:
            second_label_22.configure(text="0"+str(s22))
def decrease_clock_seconds_33():
    global s33
    if s33>=1:
        s33 = s33 - 1
        second_label_33.configure(text=s33)
        if s33<10:
            second_label_33.configure(text="0"+str(s33))
# Clock Seconds DECREMENT functions Ends Here

# READ FROM TEXT FILE
def read_from_text_file():
    global modified
    file = open("i_value_1.txt", "r")
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    print(modified[1][15:])

# Read Time From PC
def read_time_from_pc():
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
# Read Time From PC Ends Here

# Alarm ON Function Starts Here
def alarm_on_1():
    global modified
    global current_time
    file = open("i_value_1.txt", "r")
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    modified = modified[1][15:]
    modified = modified.split(":")
    print(modified)
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    print(current_time)
    if modified[0]==current_time[0] and modified[1]==current_time[1] and modified[2]==current_time[2]:
        print("GPIO 1 ON")
    else:
        print("GPIO 1 OFF")
    app.after(1000, alarm_on_1)
    
def alarm_on_2():
    global modified
    global current_time
    file = open("i_value_2.txt", "r")
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    modified = modified[1][15:]
    modified = modified.split(":")
    print(modified)
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    print(current_time)
    if modified[0]==current_time[0] and modified[1]==current_time[1] and modified[2]==current_time[2]:
        print("GPIO 2 ON")
    else:
        print("GPIO 2 OFF")
    app.after(1000, alarm_on_2)
    
    
def alarm_on_3():
    global modified
    global current_time
    file = open("i_value_3.txt", "r")
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    modified = modified[1][15:]
    modified = modified.split(":")
    print(modified)
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    print(current_time)
    if modified[0]==current_time[0] and modified[1]==current_time[1] and modified[2]==current_time[2]:
        print("GPIO 3 ON")
    else:
        print("GPIO 3 OFF")
    app.after(1000, alarm_on_3)
# Alarm ON Function Ends Here


# Alarm OFF Function Starts Here
def alarm_off_1():
    global modified
    global current_time
    file = open("i_value_1.txt", "r")
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    modified = modified[2][12:]
    modified = modified.split(":")
    print(modified)
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    print(current_time)
    if modified[0]==current_time[0] and modified[1]==current_time[1] and modified[2]==current_time[2]:
        print("GPIO 1 OFF")
    else:
        print("GPIO 1 ON")
    app.after(1000, alarm_off_1)
    
    
def alarm_off_2():
    global modified
    global current_time
    file = open("i_value_2.txt", "r")
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    modified = modified[2][12:]
    modified = modified.split(":")
    print(modified)
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    print(current_time)
    if modified[0]==current_time[0] and modified[1]==current_time[1] and modified[2]==current_time[2]:
        print("GPIO 2 OFF")
    else:
        print("GPIO 2 ON")
    app.after(1000, alarm_off_2)
    
def alarm_off_3():
    global modified
    global current_time
    file = open("i_value_3.txt", "r")
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    modified = modified[2][12:]
    modified = modified.split(":")
    print(modified)
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    print(current_time)
    if modified[0]==current_time[0] and modified[1]==current_time[1] and modified[2]==current_time[2]:
        print("GPIO 3 OFF")
    else:
        print("GPIO 3 ON")
    app.after(1000, alarm_off_3)
# Alarm OFF Function Ends Here


        


# Main Function to run the program      
def home():
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
    
    global first_label_11  # Making the first_label_11 global
    global second_label_11  # Making the second_label_11 global
    global third_label_11  # Making the third_label_11 global
    
    
    
    # Creating the title of the window
    title1=customtkinter.CTkLabel(master=app,
                                  text="ꜱᴄʜᴇᴅᴜʟɪɴɢ ꜱʏꜱᴛᴇᴍ",
                                  text_font=("Arial", 40, "bold"),
                                  text_color="#0D9986")
    title1.place(x=440,y=10)
    
    # IMAGE SECTION STARTS HERE
    
    # Define our images
    up_arrow = ImageTk.PhotoImage(Image.open("Elements\\up-arrow_1.png").resize((25,25)), Image.ANTIALIAS)
    down_arrow = ImageTk.PhotoImage(Image.open("Elements\\chevron.png").resize((25,25)), Image.ANTIALIAS)
    light_off = ImageTk.PhotoImage(Image.open("Elements\\light_off.png").resize((30,30)), Image.ANTIALIAS)
    light_on = ImageTk.PhotoImage(Image.open("Elements\\light_on.png").resize((100,100)), Image.ANTIALIAS)
    
    
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
                                      text_font=("Arial", 15, "bold"),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
                                      text_color="white")
                                      
    label_1.place(x=40,y=130)
    
    label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, "bold"),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
                                      text_color="white")
    label_2.place(x=40,y=260)
    
    label_3 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, "bold"),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
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
                                         text_font=("Arial", 18,BOLD),
                                         bg_color="white",
                                         fg_color="white",
                                         corner_radius=8,
                                         text_color="black",
                                        #  width=20,
                                        #  height=10
                                        )
                                         
                                             
    value_label_1.place(x=300,y=130)
    
    value_label_2 = customtkinter.CTkLabel(master=app,
                                         text="0",
                                         text_font=("Arial", 18,BOLD),
                                         bg_color="white",
                                         fg_color="white",
                                         corner_radius=8,
                                         text_color="black",
                                        #  width=20,
                                        #  height=10
                                        )
                                         
                                             
    value_label_2.place(x=300,y=260)
    
    value_label_3 = customtkinter.CTkLabel(master=app,
                                         text="0",
                                         text_font=("Arial", 15,BOLD),
                                         bg_color="white",
                                         fg_color="white",
                                         corner_radius=8,
                                         text_color="black",
                                        #  width=20,
                                        #  height=10
                                        )
                                         
                                             
    value_label_3.place(x=300,y=390)
    # ********** END OF INCREMENT/DECREMENT VALUE LABEL SECTION **********
    
    # SUBMIT BUTTON SECTION STARTS HERE
    sub_button_1 = customtkinter.CTkButton(master=app,
                                            text="ꜱᴜʙᴍɪᴛ",
                                            text_color="black",
                                            hover_color="blue",
                                            fg_color="#08ECFF",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            command=submit_1)
    sub_button_1.place(x=1150,y=130)
    
    sub_button_2 = customtkinter.CTkButton(master=app,
                                            text="ꜱᴜʙᴍɪᴛ",
                                            text_color="black",
                                            hover_color="blue",
                                            fg_color="#08ECFF",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            command=submit_2)
    sub_button_2.place(x=1150,y=260)
    
 
    sub_button_3 = customtkinter.CTkButton(master=app,
                                            text="ꜱᴜʙᴍɪᴛ",
                                            text_color="black",
                                            hover_color="blue",
                                            fg_color="#08ECFF",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            command=submit_3)
    sub_button_3.place(x=1150,y=390)
    # ********** END OF SUBMIT BUTTON SECTION **********
    
    # CREATING A CLOCK
    # CLOCK HOUR LABEL SECTION STARTS HERE
    hour_label_1 = customtkinter.CTkLabel(master=app,
                                         text="00",
                                         text_font=("Arial", 15,BOLD),
                                         bg_color="white",
                                         fg_color="white",
                                         corner_radius=8,
                                         text_color="black",
                                          width=20,
                                          height=10
                                        )
                                         
                                             
    hour_label_1.place(x=600,y=130)
    
    hour_label_2 = customtkinter.CTkLabel(master=app,
                                         text="00",
                                         text_font=("Arial", 15,BOLD),
                                         bg_color="white",
                                         fg_color="white",
                                         corner_radius=8,
                                         text_color="black",
                                          width=20,
                                          height=10
                                        )
                                         
                                             
    hour_label_2.place(x=600,y=260)
    
    hour_label_3 = customtkinter.CTkLabel(master=app,
                                         text="00",
                                         text_font=("Arial", 15,BOLD),
                                         bg_color="white",
                                         fg_color="white",
                                         corner_radius=8,
                                         text_color="black",
                                          width=20,
                                          height=10
                                        )
                                         
                                             
    hour_label_3.place(x=600,y=390)
    # ********** END OF CLOCK HOUR LABEL SECTION **********
    
    
    # CLOCK MINUTE LABEL SECTION STARTS HERE
    minute_label_1 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    minute_label_1.place(x=660,y=130)
    
    minute_label_2 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    minute_label_2.place(x=660,y=260)
    
    minute_label_3 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    minute_label_3.place(x=660,y=390)
    # ********** END OF CLOCK MINUTE LABEL SECTION **********
     
    
    # CLOCK SECOND LABEL SECTION STARTS HERE
    second_label_1 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    second_label_1.place(x=720,y=130)
    
    second_label_2 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    second_label_2.place(x=720,y=260)
    
    second_label_3 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    second_label_3.place(x=720,y=390)
    
    
    
    
    
    
    
    
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
                                            
    inch_button_1.place(x=605,y=100)
    
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
                                            command=increase_clock_hours_2
                                            )
                                            
    inch_button_2.place(x=605,y=230)
    
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
                                            command=increase_clock_hours_3
                                            )
                                            
    inch_button_3.place(x=605,y=360)
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
    dech_button_1.place(x=605,y=160)
    
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
                                            command=decrease_clock_hours_2
                                            )
    dech_button_2.place(x=605,y=290)
    
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
                                            command=decrease_clock_hours_3
                                            )
    dech_button_3.place(x=605,y=420)
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
    incm_button_1.place(x=665,y=100)
    
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
                                            command=increase_clock_minutes_2
                                            )
    incm_button_2.place(x=665,y=230)
    
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
                                            command=increase_clock_minutes_3
                                            )
    incm_button_3.place(x=665,y=360)
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
    decm_button_1.place(x=665,y=160)
    
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
                                            command=decrease_clock_minutes_2
                                            )
    decm_button_2.place(x=665,y=290)
    
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
                                            command=decrease_clock_minutes_3
                                            )
    decm_button_3.place(x=665,y=420)
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
    incs_button_1.place(x=725,y=100)
    
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
                                            command=increase_clock_seconds_2
                                            )
    incs_button_2.place(x=725,y=230)
    
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
                                            command=increase_clock_seconds_3
                                            )
    incs_button_3.place(x=725,y=360)
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
    decs_button_1.place(x=725,y=160)
    
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
                                            command=decrease_clock_seconds_2
                                            )
    decs_button_2.place(x=725,y=290)
    
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
                                            command=decrease_clock_seconds_3
                                            )
    decs_button_3.place(x=725,y=420)
    # ********** END OF CLOCK SECOND DECREMENT BUTTON SECTION *********
    
    
    # CREATING A Second CLOCK
    # CLOCK HOUR LABEL SECTION STARTS HERE
    hour_label_11 = customtkinter.CTkLabel(master=app,
                                         text="00",
                                         text_font=("Arial", 15,BOLD),
                                         bg_color="white",
                                         fg_color="white",
                                         corner_radius=8,
                                         text_color="black",
                                          width=20,
                                          height=10
                                        )
                                         
                                             
    hour_label_11.place(x=900,y=130)
    
    hour_label_22 = customtkinter.CTkLabel(master=app,
                                         text="00",
                                         text_font=("Arial", 15,BOLD),
                                         bg_color="white",
                                         fg_color="white",
                                         corner_radius=8,
                                         text_color="black",
                                          width=20,
                                          height=10
                                        )
                                         
                                             
    hour_label_22.place(x=900,y=260)
    
    hour_label_33 = customtkinter.CTkLabel(master=app,
                                         text="00",
                                         text_font=("Arial", 15,BOLD),
                                         bg_color="white",
                                         fg_color="white",
                                         corner_radius=8,
                                         text_color="black",
                                          width=20,
                                          height=10
                                        )
                                         
                                             
    hour_label_33.place(x=900,y=390)
    # ********** END OF CLOCK HOUR LABEL SECTION **********
    
    
    # CLOCK MINUTE LABEL SECTION STARTS HERE
    minute_label_11 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    minute_label_11.place(x=960,y=130)
    
    minute_label_22 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    minute_label_22.place(x=960,y=260)
    
    minute_label_33 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    minute_label_33.place(x=960,y=390)
    # ********** END OF CLOCK MINUTE LABEL SECTION **********
     
    
    # CLOCK SECOND LABEL SECTION STARTS HERE
    second_label_11 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    second_label_11.place(x=1020,y=130)
    
    second_label_22 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    second_label_22.place(x=1020,y=260)
    
    second_label_33 = customtkinter.CTkLabel(master=app,
                                            text="00",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            text_color="black",
                                            width=20,
                                            height=10
                                            )
    second_label_33.place(x=1020,y=390)
    
    
    
    
    
    
    
    
    # CLOCK HOUR INCREMENT BUTTON SECTION STARTS HERE
    inch_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_hours_11
                                            )
                                            
    inch_button_11.place(x=905,y=100)
    
    inch_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_hours_22
                                            )
                                            
    inch_button_22.place(x=905,y=230)
    
    inch_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_hours_33
                                            )
                                            
    inch_button_33.place(x=905,y=360)
    # ********** END OF CLOCK HOUR INCREMENT BUTTON SECTION **********
    
    
    # CLOCK HOUR DECREMENT BUTTON SECTION STARTS HERE
    dech_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_hours_11
                                            )
    dech_button_11.place(x=905,y=160)
    
    dech_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_hours_22
                                            )
    dech_button_22.place(x=905,y=290)
    
    dech_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_hours_33
                                            )
    dech_button_33.place(x=905,y=420)
    # ********** END OF CLOCK HOUR DECREMENT BUTTON SECTION **********
    
    # CLOCK MINUTE INCREMENT BUTTON SECTION STARTS HERE
    incm_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_minutes_11
                                            )
    incm_button_11.place(x=965,y=100)
    
    incm_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_minutes_22
                                            )
    incm_button_22.place(x=965,y=230)
    
    incm_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_minutes_33
                                            )
    incm_button_33.place(x=965,y=360)
    # ********** END OF CLOCK MINUTE INCREMENT BUTTON SECTION **********
    

    # CLOCK MINUTE DECREMENT BUTTON SECTION STARTS HERE
    decm_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_minutes_11
                                            )
    decm_button_11.place(x=965,y=160)
    
    decm_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_minutes_22
                                            )
    decm_button_22.place(x=965,y=290)
    
    decm_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_minutes_33
                                            )
    decm_button_33.place(x=965,y=420)
    # ********** END OF CLOCK MINUTE DECREMENT BUTTON SECTION *********
    
    
    # CLOCK SECOND INCREMENT BUTTON SECTION STARTS HERE
    incs_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_seconds_11
                                            )
    incs_button_11.place(x=1025,y=100)
    
    incs_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_seconds_22
                                            )
    incs_button_22.place(x=1025,y=230)
    
    incs_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=increase_clock_seconds_33
                                            )
    incs_button_33.place(x=1025,y=360)
    # ********** END OF CLOCK SECOND INCREMENT BUTTON SECTION **********
    
    
    # CLOCK SECOND DECREMENT BUTTON SECTION STARTS HERE
    decs_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_seconds_11
                                            )
    decs_button_11.place(x=1025,y=160)
    
    decs_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_seconds_22
                                            )
    decs_button_22.place(x=1025,y=290)
    
    decs_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            #text_color="white",
                                            #compound="center",
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            #height=10,
                                            command=decrease_clock_seconds_33
                                            )
    decs_button_33.place(x=1025,y=420)
    # ********** END OF CLOCK SECOND DECREMENT BUTTON SECTION *********

    # QUIT BUTTON SECTION STARTS HERE
    quit_button = customtkinter.CTkButton(master=app,
                                            text="X",
                                            text_color="white",
                                            hover_color="#3A3A3A",
                                            fg_color="black",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            command=quit)
    quit_button.place(x=1250,y=10)
    
    # ********** END OF QUIT BUTTON SECTION **********
    
    # Frame for the SCHEDULE LABEL at the bottom of the screen
    schedule_frame = customtkinter.CTkFrame(master=app,
                                            width=900,
                                            height=230,
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8)
    schedule_frame.place(x=10,y=500)
    
    # LABEL FOR THE SCHEDULE/NOT SCHEDULED
    first_label_1 = customtkinter.CTkLabel(master=schedule_frame,
                                            text="1. ",
                                            text_color="black",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8)
    first_label_1.place(x=0,y=30)
    
    second_label_2 = customtkinter.CTkLabel(master=schedule_frame,
                                            text="2. ",
                                            text_color="black",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8)
    second_label_2.place(x=0,y=90)
    
    third_label_3 = customtkinter.CTkLabel(master=schedule_frame,
                                            text="3. ",
                                            text_color="black", 
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8)
    third_label_3.place(x=0,y=150)
    
    

    
    first_label_11 = customtkinter.CTkLabel(master=schedule_frame,
                                            text="NON-SCHEDULED",
                                            text_color="black",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="red",
                                            corner_radius=8)
    first_label_11.place(x=90,y=30)
    
    second_label_11 = customtkinter.CTkLabel(master=schedule_frame,
                                            text="NON-SCHEDULED",
                                            text_color="black",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="red",
                                            corner_radius=8)
    second_label_11.place(x=90,y=90)
    
    third_label_11 = customtkinter.CTkLabel(master=schedule_frame, 
                                            text="NON-SCHEDULED",
                                            text_color="black", 
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="red",
                                            corner_radius=8)
    third_label_11.place(x=90,y=150)
    # ********** END OF SCHEDULE LABEL SECTION **********
    
    
    
# Creating the Splash Screen
frame_video=customtkinter.CTkFrame(master=app,width=240,corner_radius=20,fg_color="white")
frame_video.place(x=0, y=0, width=1366, height=768)
videoplayer = TkinterVideo(frame_video, scaled=True)
videoplayer.load(r'Elements\welcome_video.mp4')
videoplayer.pack(expand=True, fill="both")
videoplayer.play()

app.after(3000,frame_video.destroy)    # Destroying the splash screen after 3 seconds
app.after(3000,home)              # Calling the home function after 3 seconds
# alarm_on_1()                      # Calling the alarm_on_1 function after 3 seconds
# alarm_off_1()                     # Calling the alarm_off_1 function after 3 seconds
# alarm_on_2()                      # Calling the alarm_on_2 function after 3 seconds
# alarm_off_2()                     # Calling the alarm_off_2 function after 3 seconds
# alarm_on_3()                      # Calling the alarm_on_3 function after 3 seconds
# alarm_off_3()                     # Calling the alarm_off_3 function after 3 seconds







    



# Running the mainloop
app.mainloop()