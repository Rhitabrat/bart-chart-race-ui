from tkinter import *
import os

window = Tk()

window.title("Bar Chart Race")



def createVideo():
    os.system('python3 main.py')


btn = Button(window, text="Click Me", command=createVideo)
btn.grid(column=0, row=0)

window.mainloop()