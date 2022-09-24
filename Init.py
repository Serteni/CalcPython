import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.geometry("550x220")

def init():
    frame = ttk.Frame(root).grid()

    label1 = ttk.Label(frame, text = "baza").grid(column = 0, row = 0)

    entry1 = ttk.Entry(frame).grid(column = 1, row = 0)

root.mainloop()