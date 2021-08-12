import tkinter as tk
import os
import api


root = tk.Tk()

root.title("SetupMaker Revisited")
root.resizable(width=False, height=False)

Path = tk.Text(root, width=30, height=1)
Name = tk.Text(root, width=30, height=1)
Build = tk.Button(root, text="Build Setup", width=34, height=1, command=lambda: BuildSetup())

def onStart():
    Path.insert('end-1c', "enter path here")
    Name.insert('end-1c', "enter the program name here")

def BuildSetup():
    api.create(Path.get("1.0", 'end-1c'), Name.get("1.0", 'end-1c'))

Path.pack()
Name.pack()
Build.pack()

onStart()

root.mainloop()