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

light_off = ImageTk.PhotoImage(Image.open("Elements\\light_off.png").resize((100,100)), Image.ANTIALIAS)
label = customtkinter.CTkLabel(master=app,
                               image=light_off,
                                 bg_color="white",
                                 corner_radius=8)
label.place(x=10,y=10)


app.mainloop()