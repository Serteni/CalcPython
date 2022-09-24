import tkinter as tk
from tkinter import ttk
from tkinter import *

def butPlus(num1, num2)
    n = num1 + num2
    return n

def butMinus(num1, num2)
    n = num1 + num2
    return n

def butMult(num1, num2)
    n = num1 + num2
    return n

def butDiv(num1, num2)
    n = num1 + num2
    return n

def Initialize():

    root = tk.Tk()
    root.geometry("350x220")
    root.title("Calc")

    label1 = ttk.Label(root, text = "1st num").place(x = 10, y = 10)
    label2 = ttk.Label(root, text = "2nd num").place(x = 10, y = 35)

    buttonplus = ttk.Button(root, text = "+", width = 3).place(x = 280, y = 8)
    buttonminus = ttk.Button(root, text = "-", width = 3).place(x = 310, y = 8)
    buttonmult = ttk.Button(root, text = "*", width = 3).place(x = 280, y = 35)
    buttondiv = ttk.Button(root, text = "/", width = 3).place(x = 310, y = 35)

    entry1 = ttk.Entry(root, width = 15).place(x = 70, y = 10)
    entry2 = ttk.Entry(root, width = 15).place(x = 70, y = 35)
    
    buttonex = ttk.Button(command = root.destroy, text = "Exit", width = 9).place(x = 280, y = 190)

    root.mainloop()


