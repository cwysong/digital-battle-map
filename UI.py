import tkinter
from tkinter import messagebox
import cell
from elements import *

# UI implementation from tutorial
class GUI:

    def __init__(self):
        self.ui = tkinter.Tk()

        self.effects = status_effect()

        # self.ui.geometry("1200x800")
        self.ui.geometry("500x500")
        self.ui.title("Battle Mat")

        self.label = tkinter.Label(self.ui, text = "Battle", font = ('Arial', 16))
        self.label.pack(padx=10, pady=10)

        self.textbox = tkinter.Text(self.ui, height = 5, font = ('Arial', 16))
        self.textbox.bind("<KeyPress>", self.check_effects)
        self.textbox.pack(padx=10, pady=10)

        self.ui.mainloop()

    def check_cell(self, row, col):
        pass

    def check_effects(self, event):
        # effect = square.entity.status
        # if effect is not None:
        effect = "prone"
        if event.state == 4 and event.keysym == "s":
            messagebox.showinfo(title = effect, message = self.effects.define(effect))
