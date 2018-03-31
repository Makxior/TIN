from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

master = tk.Tk()  # Create the main window

def create_graph(): #tworzenie wykresu
    x, y = np.loadtxt('example.txt', delimiter='\t', unpack=True)
    plt.bar(x, y)
    plt.ylabel('Wartość natężenia ruchu')
    plt.xlabel('Czas od północy [min]')
    plt.title('Natezenie ruchu w systemie w danej minucie')
    plt.show()

Label(master, text='Aplikacja',width=30).grid(row=0,pady=4,column=0)
Button(master, text='Narysuj wykres', command=create_graph,width=30,height=6).grid(row=1,column=0)
Button(master, text='Obliczenia', command=create_graph,width=30,height=6).grid(row=1,column=1)
Button(master, text='Informacje', command=create_graph,width=30,height=6).grid(row=2,column=0)
Button(master, text='O autorach', command=create_graph,width=30,height=6).grid(row=2,column=1)

master.mainloop()
