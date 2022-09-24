import tkinter as tk
from tkinter import ttk
from tkinter import *


def Initialize():

    root = tk.Tk()
    root.geometry("550x220")

    frame = ttk.Frame(root).grid()

    label1 = ttk.Label(frame, text = "baza").grid(column = 0, row = 0)

    entry1 = ttk.Entry(frame).grid(column = 2, row = 0, sticky = "e")

    buttonex = ttk.Button(frame, command = root.destroy).grid(column = 8, row = 8)

    root.mainloop()


