import tkinter
from customtkinter import *
from PIL import Image,ImageTk

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
    Save_button = CTkButton(editing_window, text = "Save",command= lambda : save(choice))
    
    def save(type, image=0):
        filename = str(imageFile).split("/")[-1].split(".")
        print(filename)


    def optionmenu_callback(choice):
        
        if choice != "None":
            Save_button.grid(row= 1, column =0)
        else: 
            Save_button.grid_forget()
            
    optionmenu_var = StringVar(value = "None")
    filter_options = CTkOptionMenu(editing_window, values= ["None","B&W", "Sepia", "Sketch", "Bilateral"], variable= optionmenu_var, command= optionmenu_callback)
    filter_options.grid(row = 0, column= 1)
    