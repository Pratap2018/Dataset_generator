import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import threading
CAP=False
counter=0
window = tk.Tk()  #Makes main window
window.wm_title("Digital Microscope")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=400, height=400)
imageFrame.grid(row=0, column=0, padx=0, pady=0)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)
def capture():
  
    global CAP
    global counter
    CAP=True   
    counter+=1
    print(counter)
    show_frame()
    
def show_frame():
    global CAP
    _, frame = cap.read()
    if CAP:
        cv2.imwrite('test'+str(counter)+'.jpg',frame)
        CAP=False
    frame = cv2.flip(frame, 0)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, show_frame) 
   



#Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row = 600, column=0, padx=10, pady=2)
button = tk.Button(sliderFrame, 
                   text="QUIT", 
                   fg="red",
                   command=capture())
button.pack(side=tk.LEFT)

show_frame()  #Display 2
window.mainloop()