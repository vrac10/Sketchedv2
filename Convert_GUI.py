from customtkinter import *
from PIL import Image
import cv2
import os
import Logic

class MessageBox():

    def __init__(self):
        self.root = CTkToplevel()
        self.root.overrideredirect(1)
        self.root.title('Saved')
        self.root.geometry('200x160')

    def Ok(self, message): 
        label = CTkLabel(self.root, text= message)
        label.place(x= 90, y = 45)
        img = CTkImage(dark_image= Image.open('tick.png'), size = (40,40))
        img_label = CTkLabel(self.root, image= img, text= "")
        img_label.place(x= 20, y=40)
        button = CTkButton(self.root, text = 'Ok', width= 180,  command= lambda : self.root.destroy())
        button.place(x=10, y = 120)


def NewWindow(imageFile):
    editing_window = CTkToplevel()
    editing_window.title("Editing Window")

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
    Img_label.grid(row= 0 , column = 0)

    Save_button = CTkButton(image_frame, text = "Save", cursor = 'hand1')

    new_frame = CTkFrame(editing_window, width = 150, height = 100)
    new_frame.grid(row= 0 , column = 1, pady = 20)
    #a = MessageBox()

    def save(type, image):
        
        if os.path.exists('/Users/rohitkumar/Desktop/Sketched'):
            filename = type + "_" + str(imageFile).split("/")[-1]
            image = image.save(f'/Users/rohitkumar/Desktop/Sketched/{filename}')
            #a.Ok('Image saved\nsuccessfully')

        else:
            os.system(' mkdir /Users/rohitkumar/Desktop/Sketched ')
            filename = type + "_" + str(imageFile).split("/")[-1]
            image = image.save(f'/Users/rohitkumar/Desktop/Sketched/{filename}')
            #a.Ok('Image saved\nsuccessfully')

    img_cv2 = cv2.imread(imageFile)
    images = Logic.filters(img_cv2)

    a = list(images.values())

    def change_image(index):
        
            Img_label.configure(image= CTkImage(dark_image = Image.fromarray(a[index]), size= img_size))
            Save_button.grid(row = 1, column =0)
            Save_button.configure(command = lambda : save(type = list(images.keys())[index], image= Image.fromarray(a[index])))
   

    # #new_image = CTkImage(dark_image= Image.open(imageFile), size = (150,100))
    # #but1 = CTkButton(new_frame,image= new_image, border_width=2, text= "None", corner_radius= 0, fg_color='transparent', border_color= 'black', compound= TOP, command = lambda : change_image(-1))
    # #but1.pack()

    new_image2 = CTkImage(dark_image= Image.fromarray(a[0]), size = (150,100))
    but2 = CTkButton(new_frame,image= new_image2, border_width=2, text= "B&W", corner_radius= 0, fg_color='transparent', border_color= 'black', compound= TOP, command = lambda : change_image(0))
    but2.pack()

    new_image3 = CTkImage(dark_image= Image.fromarray(a[1]), size = (150,100))
    but3 = CTkButton(new_frame,image= new_image3, border_width=2, text= "Emboss", corner_radius= 0, fg_color='transparent', border_color= 'black', compound= TOP, command = lambda : change_image(1))
    but3.pack()

    new_image4 = CTkImage(dark_image= Image.fromarray(a[2]), size = (150,100))
    but4 = CTkButton(new_frame,image= new_image4, border_width=2, text= "Sketch", corner_radius= 0, fg_color='transparent', border_color= 'black', compound= TOP, command = lambda : change_image(2))
    but4.pack()

    new_image5 = CTkImage(dark_image= Image.fromarray(a[3]), size = (150,100))
    but5 = CTkButton(new_frame,image= new_image5, border_width=2, text= "Sepia", corner_radius= 0, fg_color='transparent', border_color= 'black', compound= TOP, command = lambda : change_image(3))
    but5.pack()

    new_image6 = CTkImage(dark_image= Image.fromarray(a[4]), size = (150,100))
    but6 = CTkButton(new_frame,image= new_image6, border_width=2, text= "Bilateral", corner_radius= 0, fg_color='transparent', border_color= 'black', compound= TOP, command = lambda : change_image(4))
    but6.pack()

    

    # def optionmenu_callback(choice):
        
    #     if choice != "None":

    #         my_Image.configure(dark_image= Image.fromarray(images[choice]))
    #         Img_label.configure(image = my_Image)
    #         Save_button.grid(row= 1, column =0)
    #         Save_button.configure(command = lambda : save(choice, Image.fromarray(images[choice])))

    #     else: 
    #         my_Image.configure(dark_image= img)
    #         Img_label.configure(image = my_Image)
    #         Save_button.grid_forget()
            
    # optionmenu_var = StringVar(value = "None")
    # filter_options = CTkOptionMenu(editing_window, values= ["None", "B&W", "Sepia", "Sketch", "Bilateral", "Emboss"], variable= optionmenu_var, command= optionmenu_callback)
    # filter_options.grid(row = 0, column= 1)
    