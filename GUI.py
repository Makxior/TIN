from tkinter import *
from tkinter import messagebox
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import tkinter.filedialog

master = Tk()  # Create the main window

tekst1 = "1. Parametry wymaganych plików."
tekst2 = "Gdy pliki są już odpowiednio skonfigurowane należy wybrać przycisk 'Załaduj pliki'. \n"
tekst3 = "Autorzy: Grzegorz Dzikowski i Kamil Michalski"
tekst4 = "Aby stworzyć wykres natężenia ruchu, wykorzystujemy wzór:"
tekst5 = "A=λ*h "
tekst6 = "Gdzie: A-natężenie ruchu, λ-intensywność wywołań, h-średnia czasu trwania połączenia.\n" \
         "W celu uzyskania wykresu musimy wykonać następujące kroki. Najpierw z pliku z czasami połączeń należy wyznaczyć śrdenią.\n" \
         "Następnie zgodnie ze wzorem mnożymy aby uzyskać wartości natężenia w danych minutach doby.\n" \
         "Ostatecznie z tych danych tworzymy wykres gdzie osią poziomą jest czas liczony od godziny 00:00 [minuty].\n" \
         "Oraz oś pionową gdzie mamy nasze wyliczone wartośći. "
tekst7 = "Przedmiot: Teoria ruchu w systemach teleinformatycznych.\n" \
         "Prowadzący: Janusz Klink.\n" \
         "Temat: Wizualizacja metod obliczania średniej wartości natężenia ruchu telekom.\n" \
         "Twórcy: Grzegorz Dzikowski, Kamil Michalski. "
tekst8 = "Pierwszy plik powinnien zawierać dwie kolumny.\n W pierwszej kolumnie powinny znajdować się kolejne minuty doby, zaczynając od północy.\n " \
         "W drugiej natomiast zapis intensywności w danej minucie (λ). Kolumny powinny być oddzielone tabulatorem.\n" \
         "Jeśli w danej minucie nie było żadnej intensywności nie należy jej umieszczać w pliku. "
tekst9 = "2. Wczytywanie plików: "
tekst10 = "Teraz należy postępować zgodnie z wyświetlanymi komunikatami."
tekst11 = "W drugim pliku powinny znajdować się wszystkie czasy połączeń.\n " \
          "Kolejne czasy połączeń powinny być oddzielone nową linią"
tekst12 = "3. Wizualizacja natężenia ruchu."
tekst13 = "Aby stworzyć wykres natężenia ruchu należy wybrać przycisk 'Pokaż wykres'."
tekst14 = "Podany wykres można przybliżać, oddalać, powracać do kolejnych przybliżeń\na nawet zapisać wybrane przybliżenie do pliku (patrz rysunek poniżej)."
tekst15 = "4. Pozostałe informacje."
tekst16 = "Aby dowiedzieć się jak obliczane jest natężenie należy wybrać przysick 'Obliczenia'."
tekst17 = "Wszystkie informacje dotyczące aplikacji znajdują się pod przyciskiem 'O programie'."


def obliczenia():
    def zamknij(zdarzenie):
        obliczenia.quit()
        obliczenia.destroy()

    obliczenia = tk.Tk()
    rama = Frame(obliczenia)
    obliczenia.title("Pokazanie jak obrabiane są dane z plików.")
    obliczenia.geometry("950x240")
    rama.pack()
    obliczenia.resizable(0, 0)

    Label(rama, text=tekst4, font="Times 14", justify="left", background='#C0D4EE').grid(row=0, column=0)
    Label(rama, text=tekst5, font="Times 30 bold", justify="center", background='#C0D4EE').grid(row=1, column=0)
    Label(rama, text=tekst6, font="Times 14", justify="left", background='#C0D4EE').grid(row=2, column=0)
    Label.config(rama, background='#C0D4EE')
    przycisk = Button(obliczenia, text="Zamknij", width=20, bg="lightgrey", height=3)
    przycisk.bind("<Button-1>", zamknij)
    przycisk.pack(side="right")
    obliczenia.mainloop()


def info_program():
    def zamknij(zdarzenie):
        info_program.quit()
        info_program.destroy()

    info_program = Toplevel()
    rama = Frame(info_program)
    info_program.title("Informacie o programie.")
    info_program.geometry("1024x180")
    info_program.resizable(0, 0)
    rama.pack()
    Label(rama, text=tekst7, font="Times 20 bold").grid(row=0, column=0, columnspan=2)

    przycisk = Button(info_program, text="Zamknij", width=20, bg="lightgrey", height=3)
    przycisk.bind("<Button-1>", zamknij)
    przycisk.pack(side="right")
    info_program.mainloop()


def _instrukcja():
    instrukcja = Toplevel()
    instrukcja.title("Instrukcja do programu")
    instrukcja.geometry("780x440")
    instrukcja.resizable(0, 0)
    Label(instrukcja, text=tekst1, font="Times 20 bold").pack()
    Label(instrukcja, text=tekst8, font="20").pack()
    imgPath = r"zdjecia/wyglad1a.gif"
    photo = PhotoImage(file=imgPath)
    tk.Label(instrukcja, image=photo).pack()
    Label(instrukcja, text=tekst11, font="20").pack()
    imgPath1 = r"zdjecia/wyglad2a.gif"
    photo1 = PhotoImage(file=imgPath1)
    label = tk.Label(instrukcja, image=photo1)
    label.pack()

    def _instrukcja2():
        instrukcja.destroy()
        instrukcja2 = Toplevel()
        instrukcja2.title("Instrukcja do programu")
        instrukcja2.geometry("740x680")
        instrukcja2.resizable(0, 0)

        Label(instrukcja2, text=tekst9, font="Times 20 bold").pack()
        Label(instrukcja2, text=tekst2, font="20").pack()
        imgPath = r"zdjecia/menu.gif"
        photo = PhotoImage(file=imgPath)
        label = tk.Label(instrukcja2, image=photo)
        label.pack()
        Label(instrukcja2, text=tekst10, font="20").pack()
        Label(instrukcja2, text=tekst12, font="Times 20 bold").pack()
        Label(instrukcja2, text=tekst13, font="20").pack()
        imgPath1 = r"zdjecia/wykres.gif"
        photo1 = PhotoImage(file=imgPath1)
        label = tk.Label(instrukcja2, image=photo1)
        label.pack()
        Label(instrukcja2, text=tekst14, font="20").pack()
        imgPath2 = r"zdjecia/wykres1.gif"
        photo2 = PhotoImage(file=imgPath2)
        label = tk.Label(instrukcja2, image=photo2)
        label.pack()

        def _instrukcja3():
            def zamknij(zdarzenie):
                instrukcja3.quit()
                instrukcja3.destroy()

            instrukcja2.destroy()
            instrukcja3 = Toplevel()
            instrukcja3.title("Instrukcja do programu")
            instrukcja3.geometry("740x440")
            instrukcja3.resizable(0, 0)

            Label(instrukcja3, text=tekst15, font="Times 20 bold").pack()
            Label(instrukcja3, text=tekst16, font="20").pack()
            imgPath = r"zdjecia/wyglad3.gif"
            photo = PhotoImage(file=imgPath)
            label = tk.Label(instrukcja3, image=photo)
            label.pack()
            Label(instrukcja3, text=tekst17, font="20").pack()
            imgPath1 = r"zdjecia/wyglad4.gif"
            photo1 = PhotoImage(file=imgPath1)
            label = tk.Label(instrukcja3, image=photo1)
            label.pack()
            przycisk = Button(instrukcja3, text="Zamknij", width=20, bg="lightgrey", height=3)
            przycisk.bind("<Button-1>", zamknij)
            przycisk.pack(side="right")
            instrukcja3.mainloop()

        Button(instrukcja2, text="Dalej", width=20, bg="lightgrey", height=3, command=_instrukcja3).pack(side="right")

        instrukcja2.mainloop()

    Button(instrukcja, text="Dalej", width=20, bg="lightgrey", height=3, command=_instrukcja2).pack(side="right")
    instrukcja.mainloop()


def wyjscie():
    sys.exit()

def master_setup():
    master.title("Program do wizualizacji danych")
    master.geometry("486x382")
    master.configure(background='#C0D4EE')
    master.resizable(0, 0)


def open_file():
    global x
    global y
    global y2
    global z
    global mean
    messagebox.showinfo("Uwaga", "Wybierz plik z intensywnością wywołań.")
    txt_file = tkinter.filedialog.askopenfilename(parent=master,
                                                  initialdir='')
    with open(txt_file) as _file:
        x, y = np.loadtxt(_file, delimiter='\t', unpack=True)
    messagebox.showinfo("Uwaga", "Wybierz plik z czasami rozmów.")
    txt_file2 = tkinter.filedialog.askopenfilename(parent=master,
                                                   initialdir='')
    with open(txt_file2) as _file2:
        z = np.loadtxt(_file2)
    mean = np.mean(z)
    y2 = [x * mean for x in y]


def create_graph():  # tworzenie wykresu
    plt.bar(x, y2)
    plt.ylabel('Wartość natężenia ruchu')
    plt.xlabel('Czas od północy [min]')
    plt.title('Natezenie ruchu w systemie w danej minucie')
    plt.show()


def show_menu():
    Label(master, text='MENU APLIKACJI',
          width=30, font="Times 20 bold", bg='#C0D4EE').grid(row=0, pady=4, padx=4, column=0, columnspan=3)
    Button(master, text='Instrukcja obsługi',
           command=_instrukcja, width=25, height=5, font=20, bg='lightgreen').grid(row=1, column=0)
    Button(master, text='Załaduj pliki',
           command=open_file, width=25, height=5, font=20, bg="#ff7777").grid(row=1, column=1)
    Button(master, text='Pokaż wykres',
           command=create_graph, width=25, height=5, font=20, bg="#C0D4CC").grid(row=2, column=0)
    Button(master, text='Obliczenia',
           command=obliczenia, width=25, height=5, font=20, bg="#ffcc44").grid(row=2, column=1, pady=10)
    Button(master, text='O programie',
           command=info_program, width=25, height=5, font=20, bg="wheat").grid(row=3, column=0)
    Button(master, text='Wyjście',
           command=wyjscie, width=25, height=5, font=20, bg="lightpink").grid(row=3, column=1)
    master.mainloop()


def main():
    master_setup()
    show_menu()


main()