import tkinter as tk
import time
from tkinter import filedialog
import main
import ntpath

class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Splash")

        ## required to make window show before the program gets to the mainloop
        self.update()

class BCR_UI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        splash = Splash(self)

        ## setup stuff goes here
        self.title("Main Window")
        ## simulate a delay while loading
        time.sleep(3)

        ## finished loading so destroy splash
        splash.destroy()

        ## show window again
        self.deiconify()

        self.geometry("500x450")
        self.bg_color = "#CDDDFD"
        self.configure(bg=self.bg_color)

    def createVideo(self):
        main.BCR_Main(self.path, self.i_path, self.location)

    # browser button: upload data
    def uploadData(self):
        btn = tk.Button(self, text="Upload Data (.csv)", command=self.browseData,)
        # btn.grid(row=0, column=6)
        # btn.place(x=150, y=50)
        btn.place(relx=0.3, rely=0.1)

    # button: 
    def browseData(self):
        file = filedialog.askopenfilename(filetypes = (("CSV Files","*.csv"),))
        if(file):
            label = tk.Label(self, text=ntpath.basename(file))
            # label.grid(row=1, column=0)
            # label.place(x=150, y=100)
            label.place(relx=0.3, rely=0.2)

            self.path = file

        else:
            label = tk.Label(self, text="You have not selected any file.", bg="#CDDDFD")
            # label.grid(row=1, column=6)
            # label.place(x=150, y=100)
            label.place(relx=0.3, rely=0.2)

    # button: select image folder
    def uploadImages(self):
        btn = tk.Button(self, text="Browse Image Folder", command=self.browseImages,)
        # btn.grid(row=3, column=6)
        # btn.place(x=150, y=150)
        btn.place(relx=0.3, rely=0.3)

    def browseImages(self):
        directory = filedialog.askdirectory()
        if(directory):
            label = tk.Label(self, text=ntpath.basename(directory))
            # label.grid(row=2, column=0)
            # label.place(x=150, y=200)
            label.place(relx=0.3, rely=0.4)

            self.i_path = directory

        else:
            label = tk.Label(self, text="You have not selected any folder.")
            # label.grid(row=2, column=6)
            # label.place(x=150, y=200)
            label.place(relx=0.3, rely=0.4)

    # button: select location to save the video
    def saveLocation(self):
        btn = tk.Button(self, text="Browse Save Location", command=self.browseLocation,)
        # btn.grid(row=5, column=6)
        # btn.place(x=150, y=250)
        btn.place(relx=0.3, rely=0.5)

    def browseLocation(self):
        directory = filedialog.askdirectory()
        if(directory):
            label = tk.Label(self, text=ntpath.basename(directory))
            # label.grid(row=4, column=0)
            # label.place(x=150, y=300)
            label.place(relx=0.3, rely=0.6)

            self.location = directory

        else:
            label = tk.Label(self, text="You have not selected any location.")
            # label.grid(row=4, column=6)
            # label.place(x=150, y=300)
            label.place(relx=0.3, rely=0.6)

    # button: run button
    def runButton(self):
        btn = tk.Button(self, text="Create Video")
        # btn.grid(row=6, column=6)
        # btn.place(x=150, y=350)
        btn.place(relx=0.3, rely=0.7)

    def execution(self):
        self.uploadData()
        self.uploadImages()
        self.saveLocation()
        self.runButton()
        self.mainloop()

if __name__ == "__main__":
    app = BCR_UI()
    app.execution()