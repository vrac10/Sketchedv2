from customtkinter import *
from PIL import Image
import cv2
import os
import Logic

class MessageBox():
    def Ok(self, message):
        root = CTkToplevel()
        root.overrideredirect(1)
        root.title('Saved')
        root.geometry('200x160')
        label = CTkLabel(root, text= message)
        label.place(x= 90, y = 45)
        img = CTkImage(dark_image= Image.open('tick.png'), size = (40,40))
        img_label = CTkLabel(root, image= img, text= "")
        img_label.place(x= 20, y=40)
        button = CTkButton(root, text = 'Ok', width= 180,  command= lambda : root.destroy())
        button.place(x=10, y = 120)


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
    Save_button = CTkButton(editing_window, text = "Save", cursor = 'hand2')
    a = MessageBox()

    def save(type, image=img):
        
        if os.path.exists('/Users/rohitkumar/Desktop/Sketched'):
            filename = type + "_" + str(imageFile).split("/")[-1]
            image = image.save(f'/Users/rohitkumar/Desktop/Sketched/{filename}')
            a.Ok('Image saved\nsuccessfully')

        else:
            os.system(' mkdir /Users/rohitkumar/Desktop/Sketched ')
            filename = type + "_" + str(imageFile).split("/")[-1]
            image = image.save(f'/Users/rohitkumar/Desktop/Sketched/{filename}')
            a.Ok('Image saved\nsuccessfully')

    img_cv2 = cv2.imread(imageFile)
    images = Logic.filters(img_cv2)

    def optionmenu_callback(choice):
        
        if choice != "None":

            my_Image.configure(dark_image= Image.fromarray(images[choice]))
            Img_label.configure(image = my_Image)
            Save_button.grid(row= 1, column =0)
            Save_button.configure(command = lambda : save(choice, Image.fromarray(images[choice])))

        else: 
            my_Image.configure(dark_image= img)
            Img_label.configure(image = my_Image)
            Save_button.grid_forget()
            
    optionmenu_var = StringVar(value = "None")
    filter_options = CTkOptionMenu(editing_window, values= ["None", "B&W", "Sepia", "Sketch", "Bilateral", "Emboss"], variable= optionmenu_var, command= optionmenu_callback)
    filter_options.grid(row = 0, column= 1)
    