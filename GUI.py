from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import tkinter.filedialog

master = tk.Tk()  # Create the main window

master.title("Program do wizualizacji danych")
master.geometry("475x377")


def create_graph():  # tworzenie wykresu
    x, y = np.loadtxt('example.txt', delimiter='\t', unpack=True)
    plt.bar(x, y)
    plt.ylabel('Wartość natężenia ruchu')
    plt.xlabel('Czas od północy [min]')
    plt.title('Natezenie ruchu w systemie w danej minucie')
    plt.show()


def open_file():
    txt_file = tkinter.filedialog.askopenfilename(parent=master,
                                                  initialdir='/Users')
    with open(txt_file) as _file:
        x, y = np.loadtxt(_file, delimiter='\t', unpack=True)
        plt.bar(x, y)
        plt.ylabel('Wartość natężenia ruchu')
        plt.xlabel('Czas od północy [min]')
        plt.title('Natezenie ruchu w systemie w danej minucie')
        plt.show()


Label(master, text='MENU APLIKACJI',
      width=30, font="Times 20 bold").grid(row=0, pady=4, padx=4, column=0, columnspan=3)
Button(master, text='Instrukcja',
       command="", width=30, height=6).grid(row=1, column=0)
Button(master, text='Zaladuj plik',
           command=open_file, width=30, height=6).grid(row=1, column=1)
Button(master, text='Rysuj wykres',
       command=create_graph, width=30, height=6).grid(row=2, column=0)
Button(master, text='Obliczenia',
       command="", width=30, height=6).grid(row=2, column=1, pady=10)
Button(master, text='Informacje',
       command="", width=30, height=6).grid(row=3, column=0)
Button(master, text='O autorach',
       command="", width=30, height=6).grid(row=3, column=1)

master.mainloop()
