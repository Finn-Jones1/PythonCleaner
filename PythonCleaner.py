import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Python files", "*.py"), ("all files", "*.*")))
    return filename
    
def main():
    with open(browseFiles(),"r+") as python:
        script = python.readlines()
        python.seek(0)
        for line in script:
            if "print" not in line:
                python.write(line)
        python.truncate()

window = tk.Tk()
window.geometry('200x100')
window.title('Select a file')
button = tk.Button(window, text="Select and Clean", command=main)
button.place(x=50, y=10)
window.mainloop()

