import tkinter as tk
from tkinter import ttk
from tkinter import *

def Initialize():

    root = tk.Tk()
    root.geometry("350x220")
    root.title("Calc")

    label1 = ttk.Label(root, text = "baza").place(x = 10, y = 10)
    label2 = ttk.Label(root, text = "actions").place(x = 200, y = 10)

    entry1 = ttk.Entry(root, width = 15).place(x = 40, y = 10)
    entry2 = ttk.Entry(root, width = 15).place(x = 40, y = 30)
    
    buttonex = ttk.Button(command = root.destroy, text = "Exit", width = 9).place(x = 280, y = 190)

    root.mainloop()


