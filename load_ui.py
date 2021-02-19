from tkinter import *
import tkinter as tk
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

        self.geometry("500x450")
        self.bg_color = "#CDDDFD"
        self.configure(bg=self.bg_color)

        '''
        Adjustable parameters
        '''
        # get title
        self.title_entry = tk.Entry(self, textvariable=StringVar())
        self.title_entry.place(relx=0.6, rely=0.4)
        
        # get bar size
        self.bar_size = tk.Entry(self, textvariable=StringVar())
        self.bar_size.place(relx=0.6, rely=0.5)

    def createVideo(self):
        main.BCR_Main(self.path, self.i_path, self.location, self.title_entry.get(), float(self.bar_size.get()))

    # browser button: upload data
    def uploadData(self):
        btn = tk.Button(self, text="Upload Data (.csv)", command=self.browseData,)
        # btn.grid(row=0, column=6)
        # btn.place(x=150, y=50)
        btn.place(relx=0.2, rely=0.1)

    def browseData(self):
        file = filedialog.askopenfilename(filetypes = (("CSV Files","*.csv"),))
        if(file):
            label = tk.Label(self, text=ntpath.basename(file), bg=self.bg_color)
            # label.grid(row=1, column=0)
            # label.place(x=150, y=100)
            label.place(relx=0.6, rely=0.1)

            self.path = file

        else:
            label = tk.Label(self, text="You have not selected any file.", bg=self.bg_color)
            # label.grid(row=1, column=6)
            # label.place(x=150, y=100)
            label.place(relx=0.6, rely=0.1)

    # button: select image folder
    def uploadImages(self):
        btn = tk.Button(self, text="Upload Image Folder", command=self.browseImages,)
        # btn.grid(row=3, column=6)
        # btn.place(x=150, y=150)
        btn.place(relx=0.2, rely=0.2)

    def browseImages(self):
        directory = filedialog.askdirectory()
        if(directory):
            label = tk.Label(self, text=ntpath.basename(directory), bg=self.bg_color)
            # label.grid(row=2, column=0)
            # label.place(x=150, y=200)
            label.place(relx=0.6, rely=0.2)

            self.i_path = directory

        else:
            label = tk.Label(self, text="You have not selected any folder.", bg=self.bg_color)
            # label.grid(row=2, column=6)
            # label.place(x=150, y=200)
            label.place(relx=0.6, rely=0.2)

    # button: select location to save the video
    def saveLocation(self):
        btn = tk.Button(self, text="Choose Saving Location", command=self.browseLocation,)
        # btn.grid(row=5, column=6)
        # btn.place(x=150, y=250)
        btn.place(relx=0.2, rely=0.3)

    def browseLocation(self):
        directory = filedialog.askdirectory()
        if(directory):
            label = tk.Label(self, text=ntpath.basename(directory), bg=self.bg_color)
            # label.grid(row=4, column=0)
            # label.place(x=150, y=300)
            label.place(relx=0.6, rely=0.3)

            self.location = directory

        else:
            label = tk.Label(self, text="You have not selected any location.", bg=self.bg_color)
            # label.grid(row=4, column=6)
            # label.place(x=150, y=300)
            label.place(relx=0.6, rely=0.3)


    '''
    Parameter labels
    '''
    # title
    def titleEntry(self):
        label = tk.Label(self, text="Enter title", bg=self.bg_color)
        label.place(relx=0.2, rely=0.4)

    # bar_size
    def barSizeEntry(self):
        label = tk.Label(self, text="Enter bar size (0 to 1)", bg=self.bg_color)
        label.place(relx=0.2, rely=0.5)

    # button: run button
    def runButton(self):
        btn = tk.Button(self, text="Create Video", command=self.createVideo)
        # btn.grid(row=6, column=6)
        # btn.place(x=150, y=350)
        btn.place(relx=0.2, rely=0.9)

    def execution(self):
        self.uploadData()
        self.uploadImages()
        self.saveLocation()
        self.titleEntry()
        self.barSizeEntry()
        self.runButton()
        self.mainloop()

if __name__ == "__main__":
    app = BCR_UI()
    app.execution()