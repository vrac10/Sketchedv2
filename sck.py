import matplotlib.pyplot as plt
import matplotlib.image as img
from tkinter import messagebox as mb
import numpy as np
import cv2
plt.style.use('seaborn')
from tkinter import filedialog
from tkinter import *

root = Tk()
root.title("Sketched")

ClickChecker = False
def filters(image,checkers):
    if checkers[0]:
        grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return grey_img
    elif checkers[1]:
        
        return 
    elif checkers[2]:
        
        smoothGrayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sketch_img = cv2.adaptiveThreshold(smoothGrayScale, 255, 
                cv2.ADAPTIVE_THRESH_MEAN_C, 
                    cv2.THRESH_BINARY, 9, 9)                  
        # grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # invert_img = cv2.bitwise_not(grey_img)
        # blur_img = cv2.GaussianBlur(invert_img, (21,21),sigmaX=0, sigmaY=0)
        # sketch_img = cv2.divide(grey_img,255 - blur_img,scale= 256.0)
        return sketch_img

    elif checkers[3]:
        sepia_Kernel = np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
        sepia_image = cv2.filter2D(src=image, kernel=sepia_Kernel, ddepth=-1)
        return sepia_image

def file_opener(a=0):
    global ClickChecker
    global fileN

    if a == 0:
        ClickChecker = True

        fileName = filedialog.askopenfile(mode='r', filetypes=[('Image files', '*.jpg'), ('Image files(png)', '*.png'), ('Image files', '*.jpeg') ])
        if fileName is not None:
            print(fileName.name)
            fileN = fileName.name

            entry["width"] = len(fileN) - 20
            entry.insert(0, fileN)
            button1["state"] = NORMAL
    elif a == 1:

        img = cv2.imread(fileN)
        RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        checkers = [b_w_checker.get(), aqua_checker.get(), sketch_checker.get(), sepia_checker.get(), vintage_checker.get()]
        
        if checkers.count(1) > 1:

            mb.showwarning(message="Only one filter at a time is supported!")

        else:
            
                filteredImage = filters(RGB_img, checkers)
            
                #plt.subplot(1, 2, 2) 
                plt.imshow(filteredImage, cmap='gray')
                plt.axis(False)

                # plt.subplot(1, 2, 1) 
                # plt.imshow(RGB_img)
                # plt.axis(False)
                plt.show()

                
        

button = Button(root, text="Browse", command=file_opener, width=5, height=1)
button.grid(column=4, row=1)
button1 = Button(root, text="Convert", command=lambda: file_opener(1), state=DISABLED, width=5, height=1)

button1.grid(column=2, row=2)

entry = Entry(root, background="white", borderwidth=2,
              width=len("/Users/rohitkumar/Downloads/Wallpaper/wallpaperflare.com_wallpaper-2 copy.jpg") - 20,
              fg="black")

entry.grid(column=0, row=1, columnspan=4)

b_w_checker = IntVar()
aqua_checker = IntVar()
sepia_checker = IntVar()
vintage_checker = IntVar()
sketch_checker = IntVar()

b_w = Checkbutton(root, text="B&W", variable=b_w_checker)
b_w.grid(row=0, column=0)

aqua = Checkbutton(root, text="AQUA", variable=aqua_checker)
aqua.grid(row=0, column=1)

sketch = Checkbutton(root, text="SKETCH", variable=sketch_checker)
sketch.grid(row=0, column=2)

sepia = Checkbutton(root, text="SEPIA", variable=sepia_checker)
sepia.grid(row=0, column=3)

vintage = Checkbutton(root, text="VINTAGE", variable=vintage_checker)
vintage.grid(row=0, column=4)
root.mainloop()
