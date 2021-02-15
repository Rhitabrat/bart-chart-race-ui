from tkinter import *
from tkinter import filedialog
import main
import ntpath

class BCR_UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Bar Chart Race")
        self.window.geometry("500x450")
        self.bg_color = "#CDDDFD"
        self.window.configure(bg=self.bg_color)
    
    def createVideo(self):
        main.BCR_Main(self.path, self.i_path, self.location)

    # browser button: upload data
    def uploadData(self):
        btn = Button(self.window, text="Upload Data (.csv)", command=self.browseData,)
        # btn.grid(row=0, column=6)
        # btn.place(x=150, y=50)
        btn.place(relx=0.3, rely=0.1)

    # button: 
    def browseData(self):
        file = filedialog.askopenfilename(filetypes = (("CSV Files","*.csv"),))
        if(file):
            label = Label(self.window, text=ntpath.basename(file))
            # label.grid(row=1, column=0)
            # label.place(x=150, y=100)
            label.place(relx=0.3, rely=0.2)

            self.path = file

        else:
            label = Label(self.window, text="You have not selected any file.", bg="#CDDDFD")
            # label.grid(row=1, column=6)
            # label.place(x=150, y=100)
            label.place(relx=0.3, rely=0.2)

    # button: select image folder
    def uploadImages(self):
        btn = Button(self.window, text="Browse Image Folder", command=self.browseImages,)
        # btn.grid(row=3, column=6)
        # btn.place(x=150, y=150)
        btn.place(relx=0.3, rely=0.3)

    def browseImages(self):
        directory = filedialog.askdirectory()
        if(directory):
            label = Label(self.window, text=ntpath.basename(directory))
            # label.grid(row=2, column=0)
            # label.place(x=150, y=200)
            label.place(relx=0.3, rely=0.4)

            self.i_path = directory

        else:
            label = Label(self.window, text="You have not selected any folder.")
            # label.grid(row=2, column=6)
            # label.place(x=150, y=200)
            label.place(relx=0.3, rely=0.4)

    # button: select location to save the video
    def saveLocation(self):
        btn = Button(self.window, text="Browse Save Location", command=self.browseLocation,)
        # btn.grid(row=5, column=6)
        # btn.place(x=150, y=250)
        btn.place(relx=0.3, rely=0.5)

    def browseLocation(self):
        directory = filedialog.askdirectory()
        if(directory):
            label = Label(self.window, text=ntpath.basename(directory))
            # label.grid(row=4, column=0)
            # label.place(x=150, y=300)
            label.place(relx=0.3, rely=0.6)

            self.location = directory

        else:
            label = Label(self.window, text="You have not selected any location.")
            # label.grid(row=4, column=6)
            # label.place(x=150, y=300)
            label.place(relx=0.3, rely=0.6)

    # button: run button
    def runButton(self):
        btn = Button(self.window, text="Run", command=self.createVideo)
        # btn.grid(row=6, column=6)
        # btn.place(x=150, y=350)
        btn.place(relx=0.3, rely=0.7)

    def execution(self):
        self.uploadData()
        self.uploadImages()
        self.saveLocation()
        self.runButton()
        self.window.mainloop()

    

bcr = BCR_UI()
bcr.execution()