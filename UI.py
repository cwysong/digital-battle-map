import tkinter as tk
from tkinter import messagebox
import cell
from elements import *

# UI implementation from tutorial
class GUI:

    def __init__(self):
        self.ui = tk.Tk()
        self.ui.geometry("1200x800")
        self.ui.title("Battle Mat")

        self.label = tk.Label(self.ui, text = "Battle", font = ('Arial', 16))
        self.label.pack(padx=10, pady=10)

        self.image = tk.PhotoImage("cave.jpg", height = 500, width = 500)
        self.image

        self.ui.mainloop()

def check_cell(self, row, col):
    pass

def check_effects(self, square:cell):
    # effect = square.entity.status
    # if effect is not None:
    effect = "prone"
    if effect == "prone":
        messagebox.showinfo(title = effect, message = status_effect.define(effect))