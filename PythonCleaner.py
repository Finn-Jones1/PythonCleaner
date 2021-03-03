import os
import tkinter as tk
from tkinter import ttk, filedialog, Checkbutton, IntVar
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/Users/finnw/Documents/GitHub/", title = "Select a File", filetypes = (("Python files", "*.py"), ("all files", "*.*")))
    return filename
  
def main():
    deldic = {"print":[], "comment":[]}
    deldic["print"].append(printR.get())
    deldic["comment"].append(commentR.get())


    
    with open(browseFiles(),"r+") as python:
        script = python.readlines()
        python.seek(0)

        
        for line in script:
            print(deldic["print"])
            if deldic["print"] == 1:
                if "print" not in line:
                    python.write(line)
            python.truncate()

        for line in script:
            print(deldic["comment"])
            if deldic["comment"] == 1:
                if "#" not in line:
                    python.write(line)
            python.truncate()


window = tk.Tk()
window.geometry('200x100')
window.title('Select a file')
printR = IntVar()
commentR = IntVar()


checkComments = Checkbutton(window, text="print", variable = commentR)
checkPrint = Checkbutton(window, text="comments(#)", variable = printR)
print(printR.get())

button = tk.Button(window, text="Select and Clean", command=main)
checkComments.place(x=10, y = 40)
checkPrint.place(x=10, y = 70)

button.place(x=50, y=10)
window.mainloop()