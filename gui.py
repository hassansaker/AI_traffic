import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,Image

import numpy as np
from keras.models import *

# the main GUI here
def open_main_gui():
    # Destroy the intro window
    intro_window.destroy()  
    ###########################################################
    #load the trained model to classify sign
    model = load_model('traffic_classifier.h5')

    #dictionary to label all traffic signs class.
    classes = { 1:'Speed limit (20km/h)',
                2:'Speed limit (30km/h)',      
                3:'Speed limit (50km/h)',       
                4:'Speed limit (60km/h)',      
                5:'Speed limit (70km/h)',    
                6:'Speed limit (80km/h)',      
                7:'End of speed limit (80km/h)',     
                8:'Speed limit (100km/h)',    
                9:'Speed limit (120km/h)',     
            10:'No passing',   
            11:'No passing veh over 3.5 tons',     
            12:'Right-of-way at intersection',     
            13:'Priority road',    
            14:'Yield',     
            15:'Stop',       
            16:'No vehicles',       
            17:'Veh > 3.5 tons prohibited',       
            18:'No entry',       
            19:'General caution',     
            20:'Dangerous curve left',      
            21:'Dangerous curve right',   
            22:'Double curve',      
            23:'Bumpy road',     
            24:'Slippery road',       
            25:'Road narrows on the right',  
            26:'Road work',    
            27:'Traffic signals',      
            28:'Pedestrians',     
            29:'Children crossing',     
            30:'Bicycles crossing',       
            31:'Beware of ice/snow',
            32:'Wild animals crossing',      
            33:'End speed + passing limits',      
            34:'Turn right ahead',     
            35:'Turn left ahead',       
            36:'Ahead only',      
            37:'Go straight or right',      
            38:'Go straight or left',      
            39:'Keep right',     
            40:'Keep left',      
            41:'Roundabout mandatory',     
            42:'End of no passing',      
            43:'End no passing veh > 3.5 tons' }
                    
    #initialise GUI using Tkinter library
    top =Tk()
    top.geometry('800x500')
    top.title('Traffic Sign Classification')
    top.configure(background='#F0F0F0')
    top.resizable(False,False)
    label = Label(top, background='#F0F0F0', font=('Arial', 15, 'bold'))
    sign_image = Label(top, background='#F0F0F0')
    # the main function to classify the loaded image depended on the model 
    #and use the classes dictionary to identify the image we uploaded to GUI
    def classify(file_path):
        global label_packed
        image = Image.open(file_path)
        image = image.resize((30,30))
        image = np.expand_dims(image, axis=0)
        image = np.array(image)
        print(image.shape)
        pred_probabilities = model.predict(image)
        pred = np.argmax(pred_probabilities, axis=-1)[0]
        sign = classes[pred+1]
        print(sign)
        label.configure(foreground='#011638', text=sign) 
    
    # this function will call if the path of image is loaded to GUI
    def show_classify_button(file_path):
        classify_b=Button(top,text="Classify Image",command=lambda: classify(file_path),padx=10,pady=5)
        classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
        classify_b.place(relx=0.79,rely=0.46)
    # get the pth of an image to be classified using Filedialog
    def upload_image():
        try:
            file_path=filedialog.askopenfilename()
            uploaded=Image.open(file_path)
            uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
            im=ImageTk.PhotoImage(uploaded)
            
            sign_image.configure(image=im)
            sign_image.image=im
            label.configure(text='')
            show_classify_button(file_path)
        except:
            pass

    upload = Button(top, text="Upload an Image", command=upload_image, padx=10, pady=5)
    upload.configure(background='#364156', foreground='white', font=('Arial', 10, 'bold'))

    upload.pack(side=BOTTOM, pady=50)
    sign_image.pack(side=BOTTOM, expand=True)
    label.pack(side=BOTTOM, expand=True)
    heading = Label(top, text="Know Your Traffic Sign", pady=20, font=('Arial', 20, 'bold'))
    heading.configure(background='#F0F0F0', foreground='#364156')
    heading.pack()

    top.mainloop()
def open_intro_gui():
    global intro_window
    intro_window=Tk()
    intro_window.geometry('800x460')
    intro_window.title('Introduction')
    intro_window.resizable(False,False)
    top_frame=Frame(
    intro_window,
    width=800,
    height=80,
    background="#F0F0F0"
    )
    center_frame=Frame(
    intro_window,
    width=800,
    height=300,
    background="#F0F0F0"
    )
    end_frame=Frame(
    intro_window,
    width=800,
    height=80,
    background="#F0F0F0" ,
       
    )
    top_frame.place(x=0,y=0)
    center_frame.place(x=0,y=80)
    end_frame.place(x=0,y=380)
    intro_label=Label(
        top_frame,
        text="Welcome to Traffic Sign Classifier!",
        font=('Arial', 25),
        fg="red",
        bg="#F0F0F0"

    
    )
    intro_label.place(x=140,y=15)
    # display photo in the screen 
    background_img=PhotoImage(file="img.png")
    my_canvas=Canvas(center_frame,width=800,height=300)
    my_canvas.pack(fill='both',expand=True)
    my_canvas.create_image(0,0,image=background_img,anchor="nw")
    # my_canvas.create_text(400,100,text="Welcome to Traffic Sign Classifier!",font=('Arial', 18),fill="black")
    
    # intro_label = tk.Label(intro_window,
    #      text="Welcome to Traffic Sign Classifier!",
    #        font=('Arial', 18),
    #          pady=20,
    #          )
    # intro_label.pack()

    # create the button for open the main program
    open_main_button =Button(end_frame, text="Open Traffic Sign Classifier", command=open_main_gui, padx=10, pady=5)
    open_main_button.configure(background='#364156', foreground='white', font=('Arial', 10, 'bold'))
    open_main_button.place(x=300,y=25)

    intro_window.mainloop()

open_intro_gui()  # To start the introduction GUI
