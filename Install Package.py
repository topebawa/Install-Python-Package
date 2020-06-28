import os
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width = 300, height = 350, bg = 'gray11', relief = 'raised')
canvas.pack()

label = tk.Label(root, text='Type Package Name:', bg = 'gray11', fg='royal blue')
label.config(font=('helvetica', 14, 'bold'))
canvas.create_window(150, 80, window=label)

entry= tk.Entry (root, width=27, bg = 'white')
canvas.create_window(150, 120, window=entry)

def installpackage ():
    global installPythonPackage
    installPythonPackage = ('pip install ' + entry.get())
    
    os.system('start cmd /k ' + installPythonPackage)

def uninstallpackage ():
    global uninstallPythonPackage
    uninstallPythonPackage = ('pip uninstall ' + entry.get())
    
    os.system('start cmd /k ' + uninstallPythonPackage)

btn1 = tk.Button(text=' Install Package ', command=installpackage,
                    bg='cornflower blue', fg='white', font=('helvetica', 12, 'bold'))
canvas.create_window(150, 180, window=btn1)



btn2 = tk.Button(text=' Uninstall Package ', command=uninstallpackage,
                    bg='red4', fg='white', font=('helvetica', 12, 'bold'))
canvas.create_window(150, 230, window=btn2)

root.mainloop()
