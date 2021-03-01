from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
from tkinter import filedialog
import main
import ntpath
# from PIL import ImageTk, Image

class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Splash")
        self.configure(bg="#CDDDFD")

        # img = ImageTk.PhotoImage(file = "logo.png")
        # panel = tk.Label(self, image = img)
        # # panel.place(side = "bottom", fill = "both", expand = "yes")
        # panel.pack()
        
        self.geometry("300x300")
        label = tk.Label(self, text="Programiz", bg="#CDDDFD")
        label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.overrideredirect(True)

        ## required to make window show before the program gets to the mainloop
        self.update()


'''
Advanced Options
'''
class PopupWindow(tk.Tk):
    def __init__(self, data):
        tk.Tk.__init__(self)
        self.data = data
        self.withdraw()

        self.title("Advanced Options")
        self.geometry("550x550")
        label = tk.Label(self,text="Select Advanced Options",)
        label.place(relx=0.3, rely=0.1)
        

        self.bg_color = "#CDDDFD"
        self.btn_color = "#0556F3"
        self.hint_color = "#464646"

        self.configure(bg=self.bg_color)

        self.input_frame = tk.LabelFrame(self, text="Get More Details", bd=2, bg=self.bg_color, height=80)
        self.input_frame.pack(fill="both", expand="yes")

        self.submit_frame = tk.LabelFrame(self, text="Submit", bd=2, bg=self.bg_color)
        self.submit_frame.pack(fill="both", expand="yes")

        '''
        Input Fields
        '''
        # get bar size
        self.bar_size = tk.Entry(self.input_frame, textvariable=StringVar(self, value=self.data.get('bar_thickness')))
        self.bar_size.place(relx=0.6, rely=0.05)

        # get text_type_bar_label
        optionList = ["Decimal","Integer"]
        self.dropVar=StringVar()
        self.dropVar.set(optionList[0])
        self.text_type_bar_label = tk.OptionMenu(self.input_frame, self.dropVar, *optionList,)
        self.text_type_bar_label.place(relx=0.6, rely=0.3)

        # get text_after_bar_label
        self.text_after_bar_label = tk.Entry(self.input_frame, textvariable=StringVar(self, value=self.data.get('text_after_bar_label')))
        self.text_after_bar_label.place(relx=0.6, rely=0.5)

        '''
        Functions
        '''
        self.okButton()
        self.barSizeEntry()
        self.barLabelTextType()
        self.textAfterBarLabelEntry()

    # bar_size
    def barSizeEntry(self):
        label_1 = tk.Label(self.input_frame, text="Thickness of the Bar", bg=self.bg_color)
        label_1.place(relx=0.05, rely=0.05)
        label_2 = tk.Label(self.input_frame, text="*The value should be a decimal between 0 and 1. eg: 0.95", bg=self.bg_color, fg=self.hint_color)
        label_2.place(relx=0.05, rely=0.15)

    # bar_label_text_type
    def barLabelTextType(self):
        label_1 = tk.Label(self.input_frame, text="Bar label type", bg=self.bg_color)
        label_1.place(relx=0.05, rely=0.3)
        label_2 = tk.Label(self.input_frame, text="*The type of text for the bar label", bg=self.bg_color, fg=self.hint_color)
        label_2.place(relx=0.05, rely=0.4)

    # text_after_bar_label
    def textAfterBarLabelEntry(self):
        label_1 = tk.Label(self.input_frame, text="Text after the bar label", bg=self.bg_color)
        label_1.place(relx=0.05, rely=0.5)
        label_2 = tk.Label(self.input_frame, text="*Any symbol or text after the bar value. eg: %", bg=self.bg_color, fg=self.hint_color)
        label_2.place(relx=0.05, rely=0.6)

    # ok button
    def okButton(self):
        btn = tk.Button(self.submit_frame, text="OK", command=self.closeWindow,)
        btn.place(relx=0.1, rely=0.4)

    def closeWindow(self):
        self.withdraw()



class BCR_UI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        splash = Splash(self)

        ## setup stuff goes here
        self.title("Bar Chart Race")
        ## simulate a delay while loading
        time.sleep(3)

        ## finished loading so destroy splash
        splash.destroy()

        ## show window again
        self.deiconify()

        self.geometry("800x800")

        self.bg_color = "#CDDDFD"
        self.btn_color = "#0556F3"
        self.hint_color = "#464646"

        self.details_frame = tk.LabelFrame(self, text="Get Details", bg=self.bg_color, bd=2)
        self.details_frame.pack(fill="both", expand="yes")
        
        self.parameter_frame = tk.LabelFrame(self, text="Enter Parameters", bg=self.bg_color, bd=2)  
        self.parameter_frame.pack(fill="both", expand="yes")

        self.advanced_frame = tk.LabelFrame(self, text="Advanced Options", bg=self.bg_color, bd=2, height=65)  
        self.advanced_frame.pack(fill="both", )

        self.run_frame = tk.LabelFrame(self, text="Create Video", bg=self.bg_color, bd=2, height=65)  
        self.run_frame.pack(fill="both", )

        self.configure(bg=self.bg_color)
        self.i_flag = False
        self.s_flag = False
        self.c_flag = False
        self.d_flag = False

        '''
        Adjustable parameters
        '''
        # get title
        self.title_entry = tk.Entry(self.parameter_frame, textvariable=StringVar(self, value='Title Name'))
        self.title_entry.place(relx=0.6, rely=0.1)

        # get colors
        self.color_entry = tk.Entry(self.parameter_frame, textvariable=StringVar(self, value="#6ECBCE,#FF2243,#FFC33D,#CE9673"))
        self.color_entry.place(relx=0.6, rely=0.5)

        # self.PopupWindow = PopupWindow()
    
    # call main.py
    def createVideo(self):
        # check if data is uploaded
        if self.d_flag == False:
            messagebox.showwarning("showwarning", "Data is not uploaded")
        else:
            main.BCR_Main(file_path=self.path, image_path=self.i_path, save_location=self.location, title_name=self.title_entry.get(), 
            bar_size=self.advanced_data.get('bar_thickness'), color_palette=self.color_entry.get().split(","),
            bar_label_text_type=self.advanced_data.get('bar_label_text_type'),
            text_after_bar_label=self.advanced_data.get('text_after_bar_label'),)

    @property
    def advanced_data(self):
        options = {}
        try:
            options['bar_thickness'] = float(self.PopupWindow.bar_size.get())
            options['text_after_bar_label'] = self.PopupWindow.text_after_bar_label.get()
            options['bar_label_text_type'] = self.PopupWindow.dropVar.get()
        except Exception as e:
            options['bar_thickness'] = 0.95
            options['text_after_bar_label'] = ''
        return options

    # browser button: upload data
    def uploadData(self):
        btn = tk.Button(self.details_frame, text="Upload Data", command=self.browseData,)
        btn.place(relx=0.1, rely=0.1)
        label = tk.Label(self.details_frame, text="*The data should be in csv format. eg. data.csv", bg=self.bg_color, fg=self.hint_color)
        label.place(relx=0.1, rely=0.21)

    def browseData(self):
        self.d_flag = True
        file = filedialog.askopenfilename(filetypes = (("CSV Files","*.csv"),))
        if(file):
            label = tk.Label(self.details_frame, text=ntpath.basename(file), bg=self.bg_color)
            label.place(relx=0.6, rely=0.1)
            self.path = file
        else:
            self.d_flag = False
            label = tk.Label(self.details_frame, text="You have not selected any file.", bg=self.bg_color)
            label.place(relx=0.6, rely=0.1)

    # button: select image folder
    def uploadImages(self):
        btn = tk.Button(self.details_frame, text="Upload Image Folder", command=self.browseImages,)
        btn.place(relx=0.1, rely=0.3)
        label = tk.Label(self.details_frame, text="*The name of each image should match the column name in the data.\neg. If column name is 'Python', the image name must be 'Python.png'", bg=self.bg_color, fg=self.hint_color)
        label.place(relx=0.1, rely=0.41)

    def browseImages(self):
        i_flag = True
        directory = filedialog.askdirectory()
        if(directory):
            label = tk.Label(self.details_frame, text=ntpath.basename(directory), bg=self.bg_color)
            label.place(relx=0.6, rely=0.3)
            self.i_path = directory
        else:
            self.i_path = None
            label = tk.Label(self.details_frame, text="You have not selected any folder.", bg=self.bg_color)
            label.place(relx=0.6, rely=0.3)

    # button: select location to save the video
    def saveLocation(self):
        btn = tk.Button(self.details_frame, text="Choose Video Destination", command=self.browseLocation,)
        btn.place(relx=0.1, rely=0.55)
        label = tk.Label(self.details_frame, text="*Choose a folder to save the video.", bg=self.bg_color, fg=self.hint_color)
        label.place(relx=0.1, rely=0.65)

    def browseLocation(self):
        s_flag = True
        directory = filedialog.askdirectory()
        if(directory):
            label = tk.Label(self.details_frame, text=ntpath.basename(directory), bg=self.bg_color)
            label.place(relx=0.6, rely=0.55)
            self.location = directory
        else:
            self.location = None
            label = tk.Label(self.details_frame, text="You have not selected any location.", bg=self.bg_color)
            label.place(relx=0.6, rely=0.55)


    '''
    Parameter labels
    '''
    # title
    def titleEntry(self):
        label_1 = tk.Label(self.parameter_frame, text="Title", bg=self.bg_color)
        label_1.place(relx=0.1, rely=0.1)
        label_2 = tk.Label(self.parameter_frame, text="*It is the text that appears at the top of the Video as a heading", bg=self.bg_color, fg=self.hint_color)
        label_2.place(relx=0.1, rely=0.2)

    # color entry
    def colorsEntry(self):
        label_1 = tk.Label(self.parameter_frame, text="Color palette", bg=self.bg_color)
        label_1.place(relx=0.1, rely=0.5)
        label_2 = tk.Label(self.parameter_frame, text="*Enter the hex code of colors separated by a comma. eg: #6ECBCE,#FF2243", bg=self.bg_color, fg=self.hint_color)
        label_2.place(relx=0.1, rely=0.6)
    
    # button: run button
    def advancedButton(self):
        btn = tk.Button(self.advanced_frame, text="Select Advanced Options", command=self.popup, bg=self.btn_color)
        # btn = tk.Button(self, text="Create Video", command=self.createVideo, highlightbackground=self.btn_color)   # for mac
        btn.place(relx=0.35, rely=0.2)

    def popup(self):
        self.PopupWindow = PopupWindow(self.advanced_data)
        self.PopupWindow.deiconify()

    # button: run button
    def runButton(self):
        btn = tk.Button(self.run_frame, text="Create Video", command=self.createVideo, bg=self.btn_color)
        # btn = tk.Button(self, text="Create Video", command=self.createVideo, highlightbackground=self.btn_color)   # for mac
        btn.place(relx=0.4, rely=0.2)

    def execution(self):

        # check if browse image button is clicked
        if self.i_flag == False:
            self.i_path = None

        # check if browse saving button is clicked
        if self.s_flag == False:
            self.location = None

        self.uploadData()
        self.uploadImages()
        self.saveLocation()
        self.titleEntry()
        self.colorsEntry()
        self.advancedButton()
        self.runButton()
        self.mainloop()

if __name__ == "__main__":
    app = BCR_UI()
    app.execution()