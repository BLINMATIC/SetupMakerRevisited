import os

def create(path, name):
    e = name
    file = open(name + '-setup.pyw', 'w')
    file.write('''# SetupMakerRevisited file
import os
import tkinter as tk

def make(path):
    try:
        os.chdir(path)
    except:
        os.mkdir(path)
        os.chdir(path)
    
    os.mkdir("''' + path + '''")
''')
    for root, dirs, files in os.walk(path, topdown=True):
        for name in dirs:
            print('dir >> ' + os.path.join(root, name))
            file.write('    os.mkdir("' + os.path.join(root, name) + '")\n')
        for name in files:
            print('file >> ' + os.path.join(root, name))
            try:
                tmpFile = open(os.path.join(root, name), 'r')
                data = tmpFile.read()
                file.write('    file = open("' + os.path.join(root, name) + '", \'w\')\n    file.write(r\'\'\'' + data + '\'\'\')\n')
            except:
                tmpFile = open(os.path.join(root, name), 'rb')
                data = tmpFile.read()
                file.write('    file = open("' + os.path.join(root, name) + '", \'wb\')\n    file.write(b\'\'\'' + str(data) + '\'\'\')\n')
    file.write(f'''

root = tk.Tk()

root.title("setup for {e}")
root.geometry("320x50")
root.resizable(width=False, height=False)

def start():
    txt = Path.get("1.0", \'end-1c\')
    make(txt)

label = tk.Label(root, text="Enter the path to install {e}", width=50, height=1).pack()
Path = tk.Text(root, width=30, height=1, pady=3)
Create = tk.Button(root, text="Install!", width=10, height=1, command=lambda: start())

Path.place(x=0, y=25)
Create.place(x=240, y=25)

root.mainloop()
''')