# from customtkinter import *
# from PIL import Image,ImageTk

# editing_window = CTk()
# img = Image.open('/Users/rohitkumar/Desktop/Screenshots/Screenshot 2022-11-28 at 10.52.13 PM.png')

# height = img.height
# width = img.width
# editing_window.wm_attributes('-transparent', True)
# i = 1
# while height > 500 and width > 500:
#     height = height / i
#     width = width / i
#     i += 0.1

# img_size = (width, height)
# my_Image = CTkImage(dark_image=img, size= img_size)
# image_frame = CTkFrame(editing_window, width= 500, height = 500)
# image_frame.grid(row= 0 , column = 0)
# label = CTkLabel(image_frame, image= my_Image)
# label.grid(row = 0 , column = 0)
# savebutton = CTkButton(image_frame, text="save")
# savebutton.grid(row = 1 , column = 0)
# new_frame = CTkFrame(editing_window, width = 150, height = 100)
# new_frame.grid(row= 0 , column = 1, pady = 20)


# a = ['/Users/rohitkumar/Desktop/Screenshots/Screenshot 2022-11-28 at 10.52.13 PM.png','/Users/rohitkumar/Desktop/Sketched/B&W_Screenshot 2022-11-28 at 10.52.13 PM.png', '/Users/rohitkumar/Desktop/Sketched/Sepia_Screenshot 2022-11-28 at 10.52.13 PM.png', '/Users/rohitkumar/Desktop/Sketched/Emboss_Screenshot 2022-11-28 at 10.52.13 PM.png']

# def change_image(index):
#     label.configure(image= CTkImage(dark_image = Image.open(a[index]), size= img_size))
   

# new_image = CTkImage(dark_image= Image.open(a[0]), size = (150,100))
# but1 = CTkButton(new_frame,image= new_image, border_width=2, text= "None", corner_radius= 0, fg_color='transparent', border_color= 'black', compound= TOP, command = lambda : change_image(0))
# but1.pack()

# new_image2 = CTkImage(dark_image= Image.open(a[1]), size = (150,100))
# but2 = CTkButton(new_frame,image= new_image2, border_width=2, text= "B&W", corner_radius= 0, fg_color='transparent', border_color= 'black', compound= TOP, command = lambda : change_image(1))
# but2.pack()

# editing_window.mainloop()
import platform
print(platform.uname())