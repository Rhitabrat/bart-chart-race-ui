from tkinter import *
from tkinter import filedialog
import main
import ntpath

class BCR_UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Bar Chart Race")
        self.window.geometry("500x500")
        self.window.configure(bg="#CDDDFD")
    
    def createVideo(self):
        main.BCR_Main(self.path, self.i_path, self.location)

    def uploadData(self):
        btn = Button(self.window, text="Browse Data", command=self.browseData,)
        btn.grid(row=0, column=6)

    def browseData(self):
        file = filedialog.askopenfilename(filetypes = (("CSV Files","*.csv"),))
        if(file):
            label = Label(self.window, text=ntpath.basename(file))
            label.grid(row=1, column=0)

            self.path = file

        else:
            label = Label(self.window, text="You have not selected any file.")
            label.grid(row=1, column=6)

    def browseImages(self):
        directory = filedialog.askdirectory()
        if(directory):
            label = Label(self.window, text=ntpath.basename(directory))
            label.grid(row=2, column=0)

            self.i_path = directory

        else:
            label = Label(self.window, text="You have not selected any folder.")
            label.grid(row=2, column=6)

    def uploadImages(self):
        btn = Button(self.window, text="Browse Image Folder", command=self.browseImages,)
        btn.grid(row=3, column=6)

    def browseLocation(self):
        directory = filedialog.askdirectory()
        if(directory):
            label = Label(self.window, text=ntpath.basename(directory))
            label.grid(row=4, column=0)

            self.location = directory

        else:
            label = Label(self.window, text="You have not selected any location.")
            label.grid(row=4, column=6)

    def saveLocation(self):
        btn = Button(self.window, text="Browse Location", command=self.browseLocation,)
        btn.grid(row=5, column=6)

    def runButton(self):
        btn = Button(self.window, text="Run", command=self.createVideo)
        btn.grid(row=6, column=6)

    def execution(self):
        self.uploadData()
        self.uploadImages()
        self.saveLocation()
        self.runButton()
        self.window.mainloop()

    

bcr = BCR_UI()
bcr.execution()