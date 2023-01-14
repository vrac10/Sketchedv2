from tkinter import *
from tkinter import filedialog
from customtkinter import *
import Convert_GUI

root = CTk()
root.title("Sketched")
root.geometry("580x500")

label = CTkLabel(root, text= "Sketched", font= ("helvetica",40))
label.place(x = 165, y = 175)

filename_field = CTkEntry(root, width=280, height= 28)
filename_field.place(x = 110, y = 235)

def browse_convert_function(a):
    
    global fileN
    if len(a) == 0:
        fileName = filedialog.askopenfile(mode='r', filetypes=[('Image files', '*.jpg'), ('Image files(png)', '*.png'), ('Image files', '*.jpeg') ])
        if fileName is not None:
            fileN = fileName.name
            if len(fileN.split('/')[-1]) > 280:
                label.configure(width = len(fileN.split('/')[-1]))
                filename_field.insert(0,fileN.split('/')[-1])
            else:
                filename_field.insert(0,fileN.split('/')[-1])
            Browse_convert.configure(text = "Convert")
            a.append(0)
            

    elif len(a) == 1:
        Convert_GUI.NewWindow(fileN)
        x.clear()
        Browse_convert.configure(text = "Browse")
        filename_field.delete(0,END)


x = []
Browse_convert = CTkButton(root, text = "Browse", command= lambda : browse_convert_function(x))
Browse_convert.place(x = 420, y = 234)

a = IntVar()
Light_mode = CTkSwitch(root, variable= a, command= lambda : set_appearance_mode("light") if a.get() else set_appearance_mode("dark"), text= "Light Mode")
Light_mode.grid()

root.mainloop()