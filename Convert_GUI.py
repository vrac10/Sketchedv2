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
    Img_label = CTkLabel(editing_window, image= my_Image, text="")
    Img_label.grid(padx = 20, pady = 20)

    b_w_checker = IntVar()
    aqua_checker = IntVar()
    sepia_checker = IntVar()
    vintage_checker = IntVar()
    sketch_checker = IntVar()

    b_w = CTkCheckBox(editing_window, text="B&W", variable=b_w_checker)
    b_w.grid(row=1, column=0)

    aqua = CTkCheckBox(editing_window, text="AQUA", variable=aqua_checker)
    aqua.grid(row=1, column=1)

    sketch = CTkCheckBox(editing_window, text="SKETCH", variable=sketch_checker)
    sketch.grid(row=1, column=2)

    sepia = CTkCheckBox(editing_window, text="SEPIA", variable=sepia_checker)
    sepia.grid(row=1, column=3)

    vintage = CTkCheckBox(editing_window, text="VINTAGE", variable=vintage_checker)
    vintage.grid(row=1, column=4)