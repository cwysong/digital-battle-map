import customtkinter
import tkinter
from tkinter import messagebox
import cell
from elements import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# UI implementation from tutorial
class GUI:

    def __init__(self, width:int , height:int, title:str):
        self.ui = customtkinter.CTk()
        
        self.label = customtkinter.CTkLabel(master=self.ui, text = title, font = ('Arial', 16))
        self.label.pack(padx=10, pady=12)

        self.frame = customtkinter.CTkFrame(master=self.ui)
        self.frame.pack(pady=10, padx=40, fill="both", expand=True)

        self.menubar = tkinter.Menu(self.ui)

        self.filemenu = tkinter.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_close)

        self.actionmenu = tkinter.Menu(self.menubar, tearoff=0)
        
        # add commands
        self.actionmenu.add_command(label = "Add Entity", command = None)
        self.actionmenu.add_separator()
        self.actionmenu.add_command(label = "Add Background", command = None)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Actions")

        self.ui.config(menu=self.menubar)

        self.effects = status_effect()

        self.ui.geometry(f"{width}x{height}")
        self.ui.title(title)

        self.textbox = customtkinter.CTkTextbox(self.ui, height = 5, font = ('Arial', 16))
        self.textbox.bind("<KeyPress>", self.check_effects)
        self.textbox.pack(padx=10, pady=10)

        self.ui.protocol("WM_DELETE_WINDOW", self.on_close)
        self.ui.mainloop()

    def check_cell(self, row, col):
        pass

    def check_effects(self, event):
        # effect = square.entity.status
        # if effect is not None:
        effect = "prone"
        if event.state == 4 and event.keysym == "s":
            messagebox.showinfo(title = effect, message = self.effects.define(effect))

    def on_close(self):
        if messagebox.askyesno(title="Quit?", message = "You A Loser?"):
            self.ui.destroy()