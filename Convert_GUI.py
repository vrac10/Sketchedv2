import tkinter
from customtkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import asksaveasfile
import os
import Logic

def NewWindow(imageFile):
    editing_window = CTkToplevel()
    editing_window.title("Editing Window")
    print(imageFile)
    img = Image.open(imageFile)
    height = img.height
    width = img.width
    
    i = 1
    while height > 500 and width > 500:
        height = height / i
        width = width / i
        i += 0.1
    img_size = (width, height)
    my_Image = CTkImage(dark_image=img, size= img_size)
    image_frame = CTkFrame(editing_window, width= 500, height = 500)
    image_frame.grid(row= 0 , column = 0)
    Img_label = CTkLabel(image_frame, image= my_Image, text="")
    Img_label.pack()
    Save_button = CTkButton(editing_window, text = "Save")
    
    def save(type, image=img):
        os.system('cd /Users/rohitkumar/Desktop/')
        filename = type + "_" + imageFile.split("/")[-1]
        image = image.save(f'/Users/rohitkumar/Desktop/{filename}')


    def optionmenu_callback(choice):
        
        if choice != "None":
            
            Save_button.grid(row= 1, column =0)
            Save_button.configure(command = lambda : save(choice))
        else: 
            Save_button.grid_forget()
            
    optionmenu_var = StringVar(value = "None")
    filter_options = CTkOptionMenu(editing_window, values= ["None","B&W", "Sepia", "Sketch", "Bilateral"], variable= optionmenu_var, command= optionmenu_callback)
    filter_options.grid(row = 0, column= 1)
    