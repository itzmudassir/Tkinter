from tkVideoPlayer import TkinterVideo
import customtkinter
import time
import threading
from tkinter.font import BOLD
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.wm_attributes('-fullscreen', 'True')
app.title("IUB Management System")
app.configure(bg="white")
def checkbox_event_1():
    if(var1.get() == 1):
        label_1 = customtkinter.CTkLabel(master=app,
                                      text="Activated",
                                      text_font=("Arial", 20, BOLD),
                                      bg_color="white",
                                      fg_color="green",
                                      corner_radius=20,
                                      text_color="white")
                                      
        label_1.place(x=40,y=130)
    else:
        label_1 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 20, BOLD),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=16,
                                      text_color="white")
                                      
        label_1.place(x=40,y=130)

def home():
    global var1         # Making the var1 global
    var1 = customtkinter.IntVar()       # Making the var1 as integer
    # Creating a Frame for title
    title_frame = customtkinter.CTkFrame(master = app,
                                            fg_color = "white",
                                            border_color = "white",
                                            border_width = 1,
                                            width = 550,
                                            height = 70)
    title_frame.place(x = 420, y = 10)
        
        # Creating the title of the window
    title1=customtkinter.CTkLabel(master=title_frame,
                                    text="ꜱᴄʜᴇᴅᴜʟɪɴɢ ",
                                    text_font=("Arial", 40, "bold"),
                                    text_color="#2A2A9C")
    title1.place(x=28, y=1)

    title2=customtkinter.CTkLabel(master=title_frame,
                                    text="ꜱʏꜱᴛᴇᴍ",
                                    text_font=("Arial", 40, "bold"),
                                    text_color="black")
    title2.place(x=330, y=1)





    quit_button = customtkinter.CTkButton(master=app,
                                                text="X",
                                                text_color="white",
                                                hover_color="#3A3A3A",
                                                fg_color="black",
                                                corner_radius=8,
                                                text_font=("System", 15,BOLD),
                                                command=quit)
    quit_button.place(x=1250,y=10)

    # CHECKBOX SECTION STARTS HERE
    checkbox_1 = customtkinter.CTkCheckBox(master=app,
                                           command=checkbox_event_1,
                                           variable=var1,
                                           hover_color = "#2A2A9C",
                                           fg_color = "#2A2A9C",
                                           border_color = "black",
                                           onvalue=1,
                                           offvalue=0)                    
    checkbox_1.place(x=10, y = 130)
    
    # CHECKBOX LABEL SECTION STARTS HERE
    label_1 = customtkinter.CTkLabel(master=app,
                                      text="Non Active",
                                      text_font=("Arial", 16, "bold"),
                                      bg_color="white",
                                      fg_color="red",
                                      corner_radius=20,
                                      text_color="white")

home()
app.mainloop()