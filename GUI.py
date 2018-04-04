from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import tkinter.filedialog

master = Tk()  # Create the main window

tekst1 = "Instrukcja obsługi aplikacji"
tekst2 = "1.Wczytywanie plików: " \
    "\n a) najpierw wybierz plik w którym znajdują się informacje intensywnośći wywołań.\n" \
    "Plik musi zawierać dwie kolumny. W pierwszej kolumnie są kolejne minuty doby zaczynając od północy.\n "\
    "W drugiej natomiast zapisz intensywności w danej minucie (λ). Kolumny muszą być oddzielone tabulatorem.\n"\
    "Jeśli w danej minucie nie było żadnej intensywności nie należy jej umieszczać w pliku.\n"\
    "b)następnie proszę wybrać plik w którym znajdują się wszytskie czasy połączeń (w minutach).\n"\
    "Kazda wartosc powinna sie znajdowac w nowym wierszu"
tekst3 ="Autorzy: Grzegorz Dzikowski i Kamil Michalski"


def master_setup():
    master.title("Program do wizualizacji danych")
    master.geometry("486x382")
    master.configure(background='#B0C4DE')

def instrukcja():
    instrukcja = tk.Tk()
    rama = Frame(instrukcja)
    instrukcja.title("Instrukcja obslugi aplikacji")
    instrukcja.geometry("800x200")
    #instrukcja.configure(bg="lightpink")
    rama.pack()
    Label(rama, text=tekst1,font="Times 20 bold").grid(row=0,column=0,columnspan=2)
    Label(rama, text=tekst2,font="20").grid(row=1,column=0,sticky=W)
    instrukcja.mainloop()

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
           command=instrukcja, width=25, height=5, font=20,bg='lightgreen').grid(row=1, column=0)
    Button(master, text='Zaladuj pliki',
           command=open_file, width=25, height=5, font=20,bg="#ff3333").grid(row=1, column=1)
    Button(master, text='Rysuj wykres',
           command=create_graph, width=25, height=5, font=20, bg="lightblue").grid(row=2, column=0)
    Button(master, text='Obliczenia',
           command="", width=25, height=5, font=20,bg="#ffbb33").grid(row=2, column=1, pady=10)
    Button(master, text='Informacje',
           command="", width=25, height=5, font=20,bg="wheat").grid(row=3, column=0)
    Button(master, text='O autorach',
           command=autorzy, width=25, height=5, font=20,bg="lightpink").grid(row=3, column=1)
    master.mainloop()


def main():
    master_setup()
    show_menu()


main()
