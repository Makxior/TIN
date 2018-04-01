from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import tkinter.filedialog

master = Tk()  # Create the main window

tekst1 = "Instrukcja obsługi aplikacji"
tekst2 ="1.Wczytywanie pliku: " \
        "\n a)najpierw proszę wybrać plik z <tutaj to co jest w pierwszym pliku xd>\n" \
        "b)następnie proszę wybrać plik z <tutaj to co jest w drugim pliku> xd>"
tekst3 ="Autorzy: Grzegorz Dzikowski i Kamil Michalski"


def master_setup():
    master.title("Program do wizualizacji danych")
    master.geometry("486x382")
    master.configure(background='#B0C4DE')

def instrukcja():
    instrukcja = tk.Tk()
    rama = Frame(instrukcja)
    instrukcja.title("Instrukcja obslugi aplikacji")
    instrukcja.geometry("488x260")
    #instrukcja.configure(bg="lightpink")
    rama.pack()
    Label(rama, text=tekst1,font="Times 20 bold").grid(row=0,column=0,columnspan=2)
    Label(rama, text=tekst2,font="20").grid(row=1,column=0,sticky=W)
    instrukcja.mainloop()

def open_file():
    global x
    global y
    global z
    txt_file = tkinter.filedialog.askopenfilename(parent=master,
                                                  initialdir='/Users')
    with open(txt_file) as _file:
        x, y = np.loadtxt(_file, delimiter='\t', unpack=True)
    txt_file2 = tkinter.filedialog.askopenfilename(parent=master,
                                                   initialdir='/Users')
    with open(txt_file2) as _file2:
        z = np.loadtxt(_file2, delimiter='\n', unpack=True)


def create_graph():  # tworzenie wykresu
    # x, y = np.loadtxt('example.txt', delimiter='\t', unpack=True)
    plt.bar(x, y)
    plt.ylabel('Wartość natężenia ruchu')
    plt.xlabel('Czas od północy [min]')
    plt.title('Natezenie ruchu w systemie w danej minucie')
    plt.show()
def obliczenia():
    

def autorzy():
    autorzy = tk.Tk()
    rama = Frame(autorzy)
    autorzy.title("autorzy obslugi aplikacji")
    autorzy.geometry("650x100")
    rama.pack()
    autorzy.configure(bg="lightpink")
    Label(rama, text=tekst3,font="Helvetica 20 bold",bg="lightpink").grid(row=0,column=0,columnspan=2)

def show_menu():
    Label(master, text='MENU APLIKACJI',
          width=30, font="Times 20 bold",bg='#B0C4DE').grid(row=0, pady=4, padx=4, column=0, columnspan=3)
    Button(master, text='Instrukcja',
           command=instrukcja, width=25, height=5, font=20,bg='#308844').grid(row=1, column=0)
    Button(master, text='Zaladuj pliki',
           command=open_file, width=25, height=5, font=20).grid(row=1, column=1)
    Button(master, text='Rysuj wykres',
           command=create_graph, width=25, height=5, font=20).grid(row=2, column=0)
    Button(master, text='Obliczenia',
           command="", width=25, height=5, font=20).grid(row=2, column=1, pady=10)
    Button(master, text='Informacje',
           command="", width=25, height=5, font=20).grid(row=3, column=0)
    Button(master, text='O autorach',
           command=autorzy, width=25, height=5, font=20).grid(row=3, column=1)
    master.mainloop()


def main():
    master_setup()
    show_menu()


main()
