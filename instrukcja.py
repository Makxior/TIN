from tkinter import *
import tkinter as tk

tekst1 = "Instrukcja obsługi aplikacji"
tekst2 = "1.Wczytywanie plików: " \
    "\n a) najpierw wybierz plik w którym znajdują się informacje intensywnośći wywołań.\n" \
    "Plik musi zawierać dwie kolumny. W pierwszej kolumnie są kolejne minuty doby zaczynając od północy.\n "\
    "W drugiej natomiast zapisz intensywności w danej minucie (λ). Kolumny muszą być oddzielone tabulatorem.\n"\
    "Jeśli w danej minucie nie było żadnej intensywności nie należy jej umieszczać w pliku.\n"\
    "b)następnie proszę wybrać plik w którym znajdują się wszytskie czasy połączeń (w minutach).\n"\
    "Kazda wartosc powinna sie znajdowac w nowym wierszu"
tekst3 ="Autorzy: Grzegorz Dzikowski i Kamil Michalski"

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

def autorzy():
    autorzy = tk.Tk()
    rama = Frame(autorzy)
    autorzy.title("autorzy obslugi aplikacji")
    autorzy.geometry("650x100")
    rama.pack()
    autorzy.configure(bg="lightpink")
    Label(rama, text=tekst3,font="Helvetica 20 bold",bg="lightpink").grid(row=0,column=0,columnspan=2)