import tkinter
import cv2
from PIL import Image, ImageTk
import PIL
import time,os
 
class Dataset_Generator:
    def __init__(self, window, window_title, video_source=0,data_set_path='dataset',rotation=1):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.lisdir=os.listdir()
        if data_set_path not in self.lisdir:
            self.data_set_path=os.getcwd()+'/'+data_set_path
            os.mkdir(self.data_set_path)

        else:
            print(data_set_path+' folder already exists ')
            self.data_set_path=os.getcwd()+'/'+data_set_path

        self.rotation=rotation
        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source,self.rotation)

         # Create a canvas that can fit the above video source size
        
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.caption=tkinter.Label(self.window,text="Title")
        self.e1=tkinter.Entry(self.window) #Label of the directory       
        self.canvas.pack()
        self.caption.pack()
        self.e1.pack()
        
 
        # Button that lets the user take a snapshot
        self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER)
 
         # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()
        self.classes=os.listdir(self.data_set_path+'/')
        self.window.mainloop()
 
    def snapshot(self):
        # Get a frame from the video source
        clas=self.e1.get()  #class name by the entry text field
        
        print(self.classes ,clas ,self.data_set_path)
        self.newpath=self.data_set_path+'/'+clas

        if clas not in self.classes:
            os.mkdir(self.data_set_path+'/'+clas)
            self.classes.append(clas)
            self.newpath=self.data_set_path+'/'+clas
        
        ret, frame = self.vid.get_frame() 
        frame=frame[1:350,289:638]
        if ret:
            cv2.imwrite(self.newpath+'/'+clas +'_'+str(len(os.listdir(self.newpath)))+ ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
 
    def update(self):
         # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
 
        self.window.after(self.delay, self.update)
 
 
class MyVideoCapture:
    def __init__(self,video_source=0,rotation=0):
         # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.rotation=rotation
      
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            frame=cv2.flip(frame,self.rotation)                  
            cv2.rectangle(frame,(288,0),(639,351),(0,255,0),1)
            
            if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
 
     # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
 
 # Create a window and pass it to the Application object

Dataset_Generator(tkinter.Tk(), "DataSet Gen",rotation=0)