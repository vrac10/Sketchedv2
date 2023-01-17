import numpy as np
import cv2
from tkinter import filedialog
from tkinter import *

def filters(image):

    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    Emboss_Kernel = np.array([[0,-1,-0.8],[1,0,-1],[1,1,0]])
    Emboss_Effect_Img = cv2.filter2D(src=image, kernel=Emboss_Kernel, ddepth=-1)       
    invert_img = cv2.bitwise_not(grey_img)
    blur_img = cv2.GaussianBlur(invert_img, (21,21),sigmaX=0, sigmaY=0)
    sketch_img = cv2.divide(grey_img,255 - blur_img,scale= 256.0)
    sepia_Kernel = np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
    sepia_image = cv2.filter2D(src=image, kernel=sepia_Kernel, ddepth=-1)
    bilateral_img = cv2.bilateralFilter(image, 15, 75, 75)

    images = {'B&W' : grey_img, 'Emboss' : Emboss_Effect_Img, 'Sketch' : sketch_img, 'Sepia' : sepia_image, 'Bilateral' : bilateral_img }
    return images
