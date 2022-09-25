import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

def Main():
    
    root = tk.Tk()
    root.geometry("350x220")
    root.title("Calc")

    num1 = tk.IntVar()
    num2 = tk.IntVar()
    numDec = tk.IntVar(root, 0)
    numBin = tk.StringVar(root, "0")
    numOct = tk.StringVar(root, "0")
    numHex = tk.StringVar(root, "0")

    def ButPlus(num1, num2):
        n = num1 + num2
        numDec.set(n)
        numBin.set(bin(n))
        numOct.set(oct(n))
        numHex.set(hex(n))
        
    def ButMinus(num1, num2):
        n = num1 - num2
        numDec.set(n)
        numBin.set(bin(n))
        numOct.set(oct(n))
        numHex.set(hex(n))

    def ButMult(num1, num2):
        n = num1 * num2
        numDec.set(n)
        numBin.set(bin(n))
        numOct.set(oct(n))
        numHex.set(hex(n))

    def ButDiv(num1, num2):
        if (num2 == 0):
            numDec.set("Деление на ноль!")
        else:
            n = num1 / num2
            numDec.set(n)
            numBin.set(bin(n))
            numOct.set(oct(n))
            numHex.set(hex(n))
    
    label1 = ttk.Label(root, text = " 1st num:").place(x = 10, y = 10)
    label2 = ttk.Label(root, text = "2nd num:").place(x = 10, y = 35)

    label10 = ttk.Label(root, text = "Dec:").place(x = 10, y = 80)
    label11 = ttk.Label(root, text = "Bin:").place(x = 10, y = 105)
    label12 = ttk.Label(root, text = "Oct:").place(x = 10, y = 130)
    label13 = ttk.Label(root, text = "Hex:").place(x = 10, y = 155)

    entry1 = ttk.Entry(root, width = 15, textvariable = num1).place(x = 70, y = 10)
    entry2 = ttk.Entry(root, width = 15, textvariable = num2).place(x = 70, y = 35)

    label10 = ttk.Label(root, width = 15, textvariable = numDec).place(x = 70, y = 80)
    label11 = ttk.Label(root, width = 15, textvariable = numBin).place(x = 70, y = 105)
    label12 = ttk.Label(root, width = 15, textvariable = numOct).place(x = 70, y = 130)
    label13 = ttk.Label(root, width = 15, textvariable = numHex).place(x = 70, y = 155)

    buttonplus = ttk.Button(root, text = "+", width = 3, command = ButPlus(num1.get(), num2.get())).place(x = 280, y = 8)
    buttonminus = ttk.Button(root, text = "-", width = 3, command = ButMinus(num1.get(), num2.get())).place(x = 310, y = 8)
    buttonmult = ttk.Button(root, text = "*", width = 3, command = ButMult(num1.get(), num2.get())).place(x = 280, y = 35)
    buttondiv = ttk.Button(root, text = "/", width = 3, command = ButDiv(num1.get(), num2.get())).place(x = 310, y = 35)

    buttonex = ttk.Button(command = root.destroy, text = "Exit", width = 9).place(x = 280, y = 190)

    root.mainloop()


