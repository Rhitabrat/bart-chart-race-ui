from tkinter import *
import os
from tkinter import filedialog
import pickle

class BCR_UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Bar Chart Race")
        self.window.geometry("500x500")
        self.window.configure(bg="#CDDDFD")
    
    def createVideo(self):
        os.system('python3 main.py')

    def runButton(self):
        btn = Button(self.window, text="Run", command=self.createVideo)
        btn.grid(row=2, column=6)

    def browseData(self):
        file = filedialog.askopenfilename(filetypes = (("CSV Files","*.csv"),))
        if(file):
            label = Label(self.window, text=os.path.basename(os.path.normpath(file)),)
            label.grid(row=1, column=0)
            # return file

            # store the path
            pkfile = open('dir', 'ab')
            pickle.dump(file, pkfile)

        else:
            label = Label(self.window, text="You have not selected any file.")
            label.grid(row=1, column=6)

    def uploadAction(self):
        btn = Button(self.window, text="Browse", command=self.browseData,)
        btn.grid(row=0, column=6)

    def execution(self):
        self.uploadAction()
        self.runButton()
        self.window.mainloop()

    

bcr = BCR_UI()
bcr.execution()