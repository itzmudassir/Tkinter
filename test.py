import customtkinter
from PIL import ImageTk,Image

# Appearence of the window
customtkinter.set_appearance_mode("Light") #dark mode and light mood
customtkinter.set_default_color_theme("blue")

# Creating the window
app=customtkinter.CTk()
app.wm_attributes('-fullscreen','True')
app.configure(bg="white")

calender = ImageTk.PhotoImage(Image.open("Elements\calendar.png"))
my_image = customtkinter.CTkImage(Image.open("Elements\calendar.png"),
                                  
                                  size=(40, 40))

button = customtkinter.CTkButton(app, image=my_image)
button.pack()

app.mainloop()