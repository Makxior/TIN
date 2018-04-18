from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import tkinter.filedialog
from instrukcja import instrukcja,autorzy

master = Tk()  # Create the main window


def master_setup():
    master.title("Program do wizualizacji danych")
    master.geometry("486x382")
    master.configure(background='#C0D4EE')

def open_file():
    global x
    global y
    global y2
    global z
    global mean
    txt_file = tkinter.filedialog.askopenfilename(parent=master,
                                                  initialdir='/Users')
    with open(txt_file) as _file:
        x, y = np.loadtxt(_file, delimiter='\t', unpack=True)
    txt_file2 = tkinter.filedialog.askopenfilename(parent=master,
                                                   initialdir='/Users')
    with open(txt_file2) as _file2:
        z = np.loadtxt(_file2)
    mean =np.mean(z)
    y2 = [x * mean for x in y]

def create_graph():  # tworzenie wykresu
    plt.bar(x, y2)
    plt.ylabel('Wartość natężenia ruchu')
    plt.xlabel('Czas od północy [min]')
    plt.title('Natezenie ruchu w systemie w danej minucie')
    plt.show()


def show_menu():
    Label(master, text='MENU APLIKACJI',
          width=30, font="Times 20 bold",bg='#C0D4EE').grid(row=0, pady=4, padx=4, column=0, columnspan=3)
    Button(master, text='Instrukcja',
           command=instrukcja, width=25, height=5, font=20,bg='lightgreen').grid(row=1, column=0)
    Button(master, text='Zaladuj pliki',
           command=open_file, width=25, height=5, font=20,bg="#ff7777").grid(row=1, column=1)
    Button(master, text='Rysuj wykres',
           command=create_graph, width=25, height=5, font=20, bg="#C0D4CC").grid(row=2, column=0)
    Button(master, text='Obliczenia',
           command="", width=25, height=5, font=20,bg="#ffcc44").grid(row=2, column=1, pady=10)
    Button(master, text='Informacje',
           command="", width=25, height=5, font=20,bg="wheat").grid(row=3, column=0)
    Button(master, text='O autorach',
           command=autorzy, width=25, height=5, font=20,bg="lightpink").grid(row=3, column=1)
    master.mainloop()


def main():
    master_setup()
    show_menu()


main()
