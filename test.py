from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import tkinter.filedialog

master = Tk()  # Create the main window
autorzy = tk.Tk()
rama = Frame(autorzy)
autorzy.title("autorzy obslugi aplikacji")
autorzy.geometry("486x382")
# autorzy.configure(bg="lightpink")
rama.pack()
img = PhotoImage(file='gd.png')
Label(autorzy, image=img).pack()
autorzy.mainloop()