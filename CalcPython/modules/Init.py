import tkinter as tk
from tkinter import ttk
from tkinter import *

def ButPlus(num1, num2)
    n = num1 + num2

def ButMinus(num1, num2)
    n = num1 + num2

def ButMult(num1, num2)
    n = num1 + num2

def ButDiv(num1, num2)
    n = num1 + num2

def Initialize():

    root = tk.Tk()
    root.geometry("350x220")
    root.title("Calc")

    label1 = ttk.Label(root, text = "1st num").place(x = 10, y = 10)
    label2 = ttk.Label(root, text = "2nd num").place(x = 10, y = 35)

    entry1 = ttk.Entry(root, width = 15).place(x = 70, y = 10)
    entry2 = ttk.Entry(root, width = 15).place(x = 70, y = 35)

    entry10 = ttk.Entry(root, width = 15).place(x = 70, y = 80)
    entry11 = ttk.Entry(root, width = 15).place(x = 70, y = 105)
    entry12 = ttk.Entry(root, width = 15).place(x = 70, y = 130)
    entry13 = ttk.Entry(root, width = 15).place(x = 70, y = 155)s

    buttonplus = ttk.Button(root, text = "+", width = 3, command = ButPlus(entry1.get(), entry2.get())).place(x = 280, y = 8)
    buttonminus = ttk.Button(root, text = "-", width = 3, command = ButMinus(entry1.get(), entry2.get())).place(x = 310, y = 8)
    buttonmult = ttk.Button(root, text = "*", width = 3, command = ButMult(entry1.get(), entry2.get())).place(x = 280, y = 35)
    buttondiv = ttk.Button(root, text = "/", width = 3, command = ButDiv(entry1.get(), entry2.get())).place(x = 310, y = 35)

    buttonex = ttk.Button(command = root.destroy, text = "Exit", width = 9).place(x = 280, y = 190)

    root.mainloop()


