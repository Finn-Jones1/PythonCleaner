import os
import tkinter as tk
from tkinter import ttk, filedialog, Checkbutton, IntVar
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Python files", "*.py"), ("all files", "*.*")))
    return filename
  
def main():
    fileName = browseFiles()
    targetFile = open(fileName,"r+")

    if printR.get() == 1:
        targetFile = open(fileName,"r+")
        script = targetFile.readlines()
        targetFile.seek(0)
        for line in script:
            if line.lstrip().startswith("print(") == False:

                targetFile.write(line)
            targetFile.truncate()

    if commentR.get() == 1:
        targetFile = open(fileName,"r+")
        script = targetFile.readlines()
        targetFile.seek(0)
        for line in script:
            if line.lstrip().startswith("#") == False:
                    targetFile.write(line)
            targetFile.truncate()

window = tk.Tk()
window.geometry('200x100')
window.title('Select a file')
printR = IntVar()
commentR = IntVar()
checkComments = Checkbutton(window, text="print", variable = commentR)
checkPrint = Checkbutton(window, text="comments(#)", variable = printR)
button = tk.Button(window, text="Select and Clean", command=main)
checkComments.place(x=10, y = 40)
checkPrint.place(x=10, y = 70)
button.place(x=50, y=10)
window.mainloop()