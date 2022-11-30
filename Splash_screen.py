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

# FUNCTIONS
# Creating CLOCK Function
def clock():
  string = time.strftime('%H:%M:%S')
  time_label.configure(text=string)
  time_label.after(1000, clock) 
# END OF CLOCK FUNCTION

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
                                      
        label_1.place(x=40,y=153)
    else:
        label_1 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
                                      text_color="white")
                                      
        label_1.place(x=40,y=153)

               
def checkbox_event_2():
    if(var2.get() == 1):
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="green",
                                      corner_radius=13,
                                      text_color="white")
        label_2.place(x=40,y=283)
    else:
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
                                      text_color="white")
        label_2.place(x=40,y=283)

     
def checkbox_event_3():
    if(var3.get() == 1):
        label_3=customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="green",
                                      corner_radius=13,
                                      text_color="white")
        label_3.place(x=40,y=413)
    else:
        label_3=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
                                      text_color="white")
        label_3.place(x=40,y=413)
        
# CHECKBOXES FUNCTIONS ENDS HERE

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
        schedule_label_1.configure(text="SCHEDULED")
        schedule_label_1.configure(text_color="white")
        
    else:
        schedule_label_1.configure(text="NON-SCHEDULED")
        schedule_label_1.configure(text_color="black")
       

        
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
        schedule_label_2.configure(text="SCHEDULED")
        schedule_label_2.configure(text_color="white")
        
    else:
        schedule_label_2.configure(text="NON-SCHEDULED")
        schedule_label_2.configure(text_color="black")
    
       
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
        schedule_label_3.configure(text="SCHEDULED")
        schedule_label_3.configure(text_color="white")
        
    else:
        schedule_label_3.configure(text="NON-SCHEDULED")
        schedule_label_3.configure(text_color="black")
    
# Submit Button Functions Ends Here

# CREATING ALARM FUNCTIONS STARTS HERE
def alarm_on_1():
    global modified_1
    global modified 
    global current_time
    file = open("i_value_1.txt", "r")
    read = file.readlines()
    modified_1 = []
    modified = []
    for line in read:
        modified_1.append(line.strip())
        modified.append(line.strip())
    
    modified_1 = modified_1[1][15:]
    modified_1 = modified_1.split(":")
    modified = modified[0][0]
    
    print(modified_1)
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    print(current_time)
    if modified[0] == "1" and modified_1[0]==current_time[0] and modified_1[1]==current_time[1] and modified_1[2]==current_time[2]:
        print("GPIO 1 ON")
        light_off_b_1 = customtkinter.CTkButton(master=schedule_frame,
                                       text = "",
                                        fg_color = "white",
                                        hover_color = "white",
                                        text_color = "white",
                                        bg_color = "white",
                                        image = light_on,
                                        width = 10,
                                        height = 1)
        light_off_b_1.place(x=300,y=23)
    else:
        print("")
    app.after(1000, alarm_on_1)
    
def alarm_off_1():
    global modified_1
    global current_time
    file = open("i_value_1.txt", "r")
    read = file.readlines()
    modified_1 = []
    for line in read:
        modified_1.append(line.strip())
    modified_1 = modified_1[2][13:]
    modified_1 = modified_1.split(":")
    print(modified_1)
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    print(current_time)
    if modified_1[0]==current_time[0] and modified_1[1]==current_time[1] and modified_1[2]==current_time[2]:
        print("GPIO 1 OFF")
        light_off_b_1 = customtkinter.CTkButton(master=schedule_frame,
                                       text = "",
                                        fg_color = "white",
                                        hover_color = "white",
                                        text_color = "white",
                                        bg_color = "white",
                                        image = light_off,
                                        width = 10,
                                        height = 1)
        light_off_b_1.place(x=300,y=23)
    else:
        print("")
    app.after(1000, alarm_off_1)

def alarm_on_2():
    global modified_1
    global modified 
    global current_time
    file = open("i_value_2.txt", "r")
    read = file.readlines()
    modified_1 = []
    modified = []
    for line in read:
        modified_1.append(line.strip())
        modified.append(line.strip())
    
    modified_1 = modified_1[1][15:]
    modified_1 = modified_1.split(":")
    modified = modified[0][0]
    
    print(modified_1)
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    print(current_time)
    if modified[0] == "1" and modified_1[0]==current_time[0] and modified_1[1]==current_time[1] and modified_1[2]==current_time[2]:
        print("GPIO 2 ON")
        light_off_b_2 = customtkinter.CTkButton(master=schedule_frame,
                                       text = "",
                                        fg_color = "white",
                                        hover_color = "white",
                                        text_color = "white",
                                        bg_color = "white",
                                        image = light_on,
                                        width = 10,
                                        height = 1)
        light_off_b_2.place(x=300,y=83)
    else:
        print("")
    app.after(1000, alarm_on_2)

def alarm_off_2():
    global modified
    global current_time
    file = open("i_value_2.txt", "r")
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    modified = modified[2][13:]
    modified = modified.split(":")
    print(modified)
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    print(current_time)
    if modified[0]==current_time[0] and modified[1]==current_time[1] and modified[2]==current_time[2]:
        print("GPIO 2 OFF")
        light_off_b_2 = customtkinter.CTkButton(master=schedule_frame,
                                        text = "", 
                                        fg_color = "white",
                                        hover_color = "white",
                                        text_color = "white",
                                        bg_color = "white",
                                        image = light_off,
                                        width = 10,
                                        height = 1)
        light_off_b_2.place(x=300,y=83)
    else:
        print("")
    app.after(1000, alarm_off_2)

def alarm_off_3():
    global modified_1
    global modified
    global current_time
    file = open("i_value_3.txt", "r")
    read = file.readlines()
    modified = []
    for line in read:
        modified.append(line.strip())
    modified = modified[2][13:]
    modified = modified.split(":")
    print(modified)
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    print(current_time)
    if modified[0]==current_time[0] and modified[1]==current_time[1] and modified[2]==current_time[2]:
        print("GPIO 3 OFF")
        light_off_b_3 = customtkinter.CTkButton(master=schedule_frame,
                                        text = "",
                                        fg_color = "white",
                                        hover_color = "white",
                                        text_color = "white",
                                        bg_color = "white",
                                        image = light_off,
                                        width = 10,
                                        height = 1)
        light_off_b_3.place(x=300,y=143)
    else:
        print("")
    app.after(1000, alarm_off_3)
    
    
def alarm_on_3():
    global modified_1
    global modified 
    global current_time
    file = open("i_value_3.txt", "r")
    read = file.readlines()
    modified_1 = []
    modified = []
    for line in read:
        modified_1.append(line.strip())
        modified.append(line.strip())
    
    modified_1 = modified_1[1][15:]
    modified_1 = modified_1.split(":")
    modified = modified[0][0]
    
    print(modified_1)
    global current_time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_time = current_time.split(":")
    print(current_time)
    if modified[0] == "1" and modified_1[0]==current_time[0] and modified_1[1]==current_time[1] and modified_1[2]==current_time[2]:
        print("GPIO 3 ON")
        light_off_b_3 = customtkinter.CTkButton(master=schedule_frame,
                                       text = "",
                                        fg_color = "white",
                                        hover_color = "white",
                                        text_color = "white",
                                        bg_color = "white",
                                        image = light_on,
                                        width = 10,
                                        height = 1)
        light_off_b_3.place(x=300,y=143)
    else:
        print("")
    app.after(1000, alarm_on_3)
    
# READ FROM TEXT FILE
def read_from_text_file_1():
    global modified_text_1
    file = open("i_value_1.txt", "r")
    read = file.readlines()
    modified_text_1 = []
    for line in read:
        modified_text_1.append(line.strip())

def read_from_text_file_2():
    global modified_text_2
    file = open("i_value_2.txt", "r")
    read = file.readlines()
    modified_text_2 = []
    for line in read:
        modified_text_2.append(line.strip())

def read_from_text_file_3():
    global modified_text_3
    file = open("i_value_3.txt", "r")
    read = file.readlines()
    modified_text_3 = []
    for line in read:
        modified_text_3.append(line.strip())
        
# CREATING RESET BUTTON
def reset_1():
    file = open("i_value_1.txt", "w")
    file.write("0: 0"+"\n"+ "Starting Time: 00:00:00" + "\n" + "Ending Time: 00:00:00")
    file.close() 
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
    
    
    
def reset_2():
    file = open("i_value_2.txt", "w")
    file.write("0: 0"+"\n"+ "Starting Time: 00:00:00" + "\n" + "Ending Time: 00:00:00")
    file.close() 
    
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

    
def reset_3():
    file = open("i_value_3.txt", "w")
    file.write("0: 0"+"\n"+ "Starting Time: 00:00:00" + "\n" + "Ending Time: 00:00:00")
    file.close()
    
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
    calender = ImageTk.PhotoImage(Image.open("Elements\calendar.png").resize((40,40)), Image.ANTIALIAS)
    clock = ImageTk.PhotoImage(Image.open("Elements\\clock.png").resize((40,40)), Image.ANTIALIAS)
    # IMAGE SECTION ENDS HERE
    
    # Reading i_value_1
    read_from_text_file_1()
    text_read_1 = modified_text_1[0][0]
    text_read_2 = modified_text_1[1][15:]
    text_read_3 = modified_text_1[2][13:]
    text_read_2 =  text_read_2.split(":")
    text_read_3 =  text_read_3.split(":")
    var1 = customtkinter.IntVar(value = text_read_1)
    
    # Reading i_value_2
    read_from_text_file_2()
    text_read_11 = modified_text_2[0][0]
    text_read_22 = modified_text_2[1][15:]
    text_read_33 = modified_text_2[2][13:]
    text_read_22 =  text_read_22.split(":")
    text_read_33 =  text_read_33.split(":")
    var2 = customtkinter.IntVar(value = text_read_11)
    
    # Reading i_value_3
    read_from_text_file_3()
    text_read_111 = modified_text_3[0][0]
    text_read_222 = modified_text_3[1][15:]
    text_read_333 = modified_text_3[2][13:]
    text_read_222 =  text_read_222.split(":")
    text_read_333 =  text_read_333.split(":")
    var3 = customtkinter.IntVar(value = text_read_111)
    
    # SHOWING THE TIME
    time_label = customtkinter.CTkLabel(master=app,
                                        text_font=("calibri", 40, "bold"),
                                        text_color="#2A2A9C",
                                        bg_color="white")

    time_label.place(x=10, y=10)
  
    # Clock Image
    clock_image_button = customtkinter.CTkButton(master=app,
                                                  text = "",
                                                  fg_color = "white",
                                                  hover_color = "white",
                                                  text_color = "white",
                                                  bg_color = "white",
                                                  image = clock,
                                                  width = 10,
                                                  height = 1
                                                  )
    clock_image_button.place(x=210, y=20)
    # TIME SECTION ENDS HERE

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
                                           command=checkbox_event_1,
                                           variable=var1,
                                           hover_color = "#2A2A9C",
                                           fg_color = "#2A2A9C",
                                           border_color = "black",
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_1.place(x=10, y = 155)
    
    checkbox_2 = customtkinter.CTkCheckBox(master=app, 
                                           command=checkbox_event_2,
                                           variable=var2,
                                           hover_color = "#2A2A9C",
                                           fg_color = "#2A2A9C",
                                           border_color = "black",
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_2.place(x=10, y = 285)
    
    checkbox_3 = customtkinter.CTkCheckBox(master=app, 
                                           command=checkbox_event_3,
                                           variable=var3,
                                           hover_color = "#2A2A9C",
                                           fg_color = "#2A2A9C",
                                           border_color = "black",
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_3.place(x=10, y = 415)
    # ********** END OF CHECKBOX SECTION **********
    
    # CHECKBOX LABEL SECTION STARTS HERE
    if text_read_1 == "1":
        label_1 = customtkinter.CTkLabel(master=app,
                                        text="Activated",
                                        text_font=("Arial", 15, BOLD),
                                        bg_color="white",
                                        fg_color="green",
                                        corner_radius=13,
                                        text_color="white")
        label_1.place(x=40,y=153)
    else:
        label_1 = customtkinter.CTkLabel(master=app,
                                        text="Non Active",
                                        text_font=("Arial", 15, BOLD),
                                        bg_color="white",
                                        fg_color="red",
                                        corner_radius=13,
                                        text_color="white")
        label_1.place(x=40,y=153)
    
    if text_read_11 == "1":
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="green",
                                      corner_radius=13,
                                      text_color="white")
        label_2.place(x=40,y=283)
    else:
        label_2=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=13,
                                      text_color="white")
        label_2.place(x=40,y=283)
    
    if text_read_111 == "1":
        label_3=customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("Arial", 15, BOLD),
                                      bg_color="white",
                                      fg_color="green",
                                      corner_radius=13,
                                      text_color="white")
        label_3.place(x=40,y=413)
    else:
        label_3=customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 15, BOLD),
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
                                         text=text_read_2[0],
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
                                            text=text_read_2[1],
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
                                            text=text_read_2[2],
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
    # ********** END OF FIRST ROW TIME BUTTONS & LABELS **********
    
    # Second Row Time Buttons & Labels
    inch_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_hours_2
                                            )                                       
    inch_button_2.place(x=420,y=240)
    
    incm_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_minutes_2
                                            )
    incm_button_2.place(x= 480,y=240)
    
    incs_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_seconds_2
                                            )
    incs_button_2.place(x=540,y=240)
    
    
    hour_label_2 = customtkinter.CTkLabel(master=app,
                                         text=text_read_22[0],
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
                                            text=text_read_22[1],
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
                                            text=text_read_22[2],
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
                                            command=decrease_clock_hours_2
                                            )
    dech_button_2.place(x=420,y=314)
    
    decm_button_2 = customtkinter.CTkButton(master=app,
                                            text="",    
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=decrease_clock_minutes_2
                                            )
    decm_button_2.place(x=480,y=314)
    
    decs_button_2 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=decrease_clock_seconds_2
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
                                            command=increase_clock_hours_3
                                            )
    inch_button_3.place(x=420,y=368)
    
    incm_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_minutes_3
                                            )
    incm_button_3.place(x= 480,y=368)

    incs_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_seconds_3
                                            )
    incs_button_3.place(x=540,y=368)

    hour_label_3 = customtkinter.CTkLabel(master=app,
                                            text=text_read_222[0],
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
                                            text=text_read_222[1],
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
                                            text=text_read_222[2],
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
                                            command=decrease_clock_hours_3
                                            )
    dech_button_3.place(x=420,y=442)

    decm_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=decrease_clock_minutes_3
                                            )
    decm_button_3.place(x=480,y=442)
    
    decs_button_3 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=decrease_clock_seconds_3
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
                                            command=increase_clock_hours_11
                                            )
                                            
    inch_button_11.place(x=720,y=112)
    
    incm_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_minutes_11
                                            )
    incm_button_11.place(x= 780,y=112)

    incs_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_seconds_11
                                            )
    incs_button_11.place(x=840,y=112)

    hour_label_11 = customtkinter.CTkLabel(master=app,
                                            text=text_read_3[0],
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
                                            text=text_read_3[1],
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
                                            text=text_read_3[2],
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
                                            command=decrease_clock_hours_11
                                            )
    dech_button_11.place(x=720,y=186)
    
    decm_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=decrease_clock_minutes_11
                                            )
    decm_button_11.place(x=780,y=186)
    
    decs_button_11 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=decrease_clock_seconds_11
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
                                            command=increase_clock_hours_22
                                            )
    inch_button_22.place(x=720,y=242)
    
    incm_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_minutes_22
                                            )   
    incm_button_22.place(x=780,y=242)

    incs_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_seconds_22
                                            )
    incs_button_22.place(x=840,y=242)
    
    hour_label_22 = customtkinter.CTkLabel(master=app,
                                            text=text_read_33[0],
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
                                            text=text_read_33[1],
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
                                            text=text_read_33[2],
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
                                            command=decrease_clock_hours_22
                                            )
    dech_button_22.place(x=720,y=316)

    decm_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=decrease_clock_minutes_22
                                            )
    decm_button_22.place(x=780,y=316)
    
    decs_button_22 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=decrease_clock_seconds_22
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
                                            command=increase_clock_hours_33  
                                            )
    inch_button_33.place(x=720,y=372)

    incm_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_minutes_33
                                            )
    incm_button_33.place(x=780,y=372)
    
    incs_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=up_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=increase_clock_seconds_33
                                            )
    incs_button_33.place(x=840,y=372)

    hour_label_33 = customtkinter.CTkLabel(master=app,
                                            text=text_read_333[0],
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
                                            text=text_read_333[1],
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
                                            text=text_read_333[2],
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
                                            command=decrease_clock_hours_33
                                            )
    dech_button_33.place(x=720,y=446)

    decm_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=decrease_clock_minutes_33
                                            )
    decm_button_33.place(x=780,y=446)

    decs_button_33 = customtkinter.CTkButton(master=app,
                                            text="",
                                            image=down_arrow,
                                            hover_color="white",
                                            fg_color="white",
                                            corner_radius=8,
                                            width=30,
                                            command=decrease_clock_seconds_33
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
                                            command=submit_1
                                            )
    sub_button_1.place(x=950,y=153)
    
    sub_button_2 = customtkinter.CTkButton(master=app,
                                            text="ꜱᴜʙᴍɪᴛ",
                                            text_color="white",
                                            hover_color="blue",
                                            fg_color="#2A2A9C",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            command=submit_2
                                            )
    sub_button_2.place(x=950,y=283)
    
    sub_button_3 = customtkinter.CTkButton(master=app,
                                            text="ꜱᴜʙᴍɪᴛ",
                                            text_color="white",
                                            hover_color="blue",
                                            fg_color="#2A2A9C",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            command=submit_3
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
                                            command=reset_1
                                            )
    reset_button_1.place(x=1150,y=153)

    reset_button_2 = customtkinter.CTkButton(master=app,
                                            text="ʀᴇꜱᴇᴛ",
                                            text_color="white",
                                            hover_color="#F11F32",
                                            fg_color="#F12B3D",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            command=reset_2
                                            )
    reset_button_2.place(x=1150,y=283)

    reset_button_3 = customtkinter.CTkButton(master=app,
                                            text="ʀᴇꜱᴇᴛ",
                                            text_color="white",
                                            hover_color="#F11F32",
                                            fg_color="#F12B3D",
                                            corner_radius=8,
                                            text_font=("Arial", 15,BOLD),
                                            command=reset_3
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
    
    num_label_2 = customtkinter.CTkLabel(master=schedule_frame,
                                            text="2. ",
                                            text_color="black",
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8)
    num_label_2.place(x=0,y=90)
    
    num_label_3 = customtkinter.CTkLabel(master=schedule_frame,
                                            text="3. ",
                                            text_color="black", 
                                            text_font=("Arial", 15,BOLD),
                                            bg_color="white",
                                            fg_color="white",
                                            corner_radius=8)
    num_label_3.place(x=0,y=150)
    
    if text_read_1 == "1":
        schedule_label_1 = customtkinter.CTkLabel(master=schedule_frame,
                                                text="SCHEDULED",
                                                text_color="white",
                                                text_font=("Arial", 15,BOLD),
                                                bg_color="white",
                                                fg_color="red",
                                                corner_radius=8)
        schedule_label_1.place(x=90,y=30)
    else:
        schedule_label_1 = customtkinter.CTkLabel(master=schedule_frame,
                                                text="NON-SCHEDULED",
                                                text_color="black",
                                                text_font=("Arial", 15,BOLD),
                                                bg_color="white",
                                                fg_color="red",
                                                corner_radius=8)
        schedule_label_1.place(x=90,y=30)
    
    if text_read_11 == "1":
        schedule_label_2 = customtkinter.CTkLabel(master=schedule_frame,
                                                text="SCHEDULED",
                                                text_color="white",
                                                text_font=("Arial", 15,BOLD),
                                                bg_color="white",
                                                fg_color="red",
                                                corner_radius=8)
        schedule_label_2.place(x=90,y=90)
    else:
        schedule_label_2 = customtkinter.CTkLabel(master=schedule_frame,
                                                text="NON-SCHEDULED",
                                                text_color="black",
                                                text_font=("Arial", 15,BOLD),
                                                bg_color="white",
                                                fg_color="red",
                                                corner_radius=8)
        schedule_label_2.place(x=90,y=90)
    
    
    if text_read_111 == "1":
        schedule_label_3 = customtkinter.CTkLabel(master=schedule_frame,
                                                text="SCHEDULED",
                                                text_color="white",
                                                text_font=("Arial", 15,BOLD),
                                                bg_color="white",
                                                fg_color="red",
                                                corner_radius=8)
        schedule_label_3.place(x=90,y=150)
    else:
        schedule_label_3 = customtkinter.CTkLabel(master=schedule_frame,
                                                text="NON-SCHEDULED",
                                                text_color="black",
                                                text_font=("Arial", 15,BOLD),
                                                bg_color="white",
                                                fg_color="red",
                                                corner_radius=8)
        schedule_label_3.place(x=90,y=150)
    
    # DISPLAYING IMAGES
    light_off_b_1 = customtkinter.CTkButton(master=schedule_frame,
                                       text = "",
                                        fg_color = "white",
                                        hover_color = "white",
                                        text_color = "white",
                                        bg_color = "white",
                                        image = light_off,
                                        width = 10,
                                        height = 1)
    light_off_b_1.place(x=300,y=23)
    
    light_off_b_2 = customtkinter.CTkButton(master=schedule_frame,
                                        text = "", 
                                        fg_color = "white",
                                        hover_color = "white",
                                        text_color = "white",
                                        bg_color = "white",
                                        image = light_off,
                                        width = 10,
                                        height = 1)
    light_off_b_2.place(x=300,y=83)
    
    light_off_b_3 = customtkinter.CTkButton(master=schedule_frame,
                                        text = "",
                                        fg_color = "white",
                                        hover_color = "white",
                                        text_color = "white",
                                        bg_color = "white",
                                        image = light_off,
                                        width = 10,
                                        height = 1)
    light_off_b_3.place(x=300,y=143)
    # END OF SCHEDULING INFO
    

    
    

    

    
    
    
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
# Calling Clock function
clock()
# Calling ALARM functions
alarm_on_1()
alarm_off_1()
alarm_on_2()
alarm_off_2()
alarm_on_3()
alarm_off_3()
# Running the mainloop
app.mainloop()