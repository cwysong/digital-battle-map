import customtkinter
import tkinter
from tkinter import messagebox
import cell
from elements import *
from PIL import Image



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# UI implementation from tutorial
class GUI:

    def __init__(self):
        self.ui = customtkinter.CTk()

        self.map_define()

        self.ui.protocol("WM_DELETE_WINDOW", self.on_close)
        self.ui.mainloop()

    def map_define(self): 
        frame = customtkinter.CTkFrame(master = self.ui)
        frame.pack(pady=20,padx=60,fill="both", expand=True)

        title = customtkinter.CTkLabel(master=frame, text="Enter Image File Name", font=("Arial", 16))
        title.pack(pady=12, padx=10)

        self.entry = customtkinter.CTkEntry(master=frame, placeholder_text="File Name")
        self.entry.pack(pady=12,padx=10)

        button = customtkinter.CTkButton(master = frame, text = "Open", command = self.get_entry_val)
        button.pack(pady=12,padx=10)

        self.ui.protocol("WM_DELETE_WINDOW", self.on_close)
        self.ui.mainloop()

    def get_entry_val(self):
        self.open(self.entry.get())

    def open(self, map:str):
        
        title = map[0:map.index(".")]
        
        image = Image.open(map)
        background_image = customtkinter.CTkImage(dark_image=image, size=image.size)
        self.bg_label = customtkinter.CTkLabel(self.ui, text="", image=background_image)
        self.bg_label.place(x=0,y=0)
        width = image.size[0]
        height = image.size[1]

        self.label = customtkinter.CTkLabel(master=self.ui, text = title, font = ('Arial', 16))
        self.label.pack(padx=10, pady=12)

        self.textbox = customtkinter.CTkTextbox(self.ui, height = 5, font = ('Arial', 16))
        self.textbox.bind("<KeyPress>", self.check_effects)
        self.textbox.pack(padx=10, pady=10)

        self.lastClickX = 0
        self.lastClickY = 0

        self.ui.overrideredirect(True)
        self.ui.attributes('-topmost', True)
        self.bg_label.bind('<Button-1>', self.SaveLastClickPos)
        self.bg_label.bind('<B1-Motion>', self.Dragging)

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

        self.ui.protocol("WM_DELETE_WINDOW", self.on_close)
        self.ui.mainloop()

    def SaveLastClickPos(self, event):
        self.lastClickX = event.x
        self.lastClickY = event.y


    def Dragging(self, event):
        x, y = event.x - self.lastClickX + self.ui.winfo_x(), event.y - self.lastClickY + self.ui.winfo_y()
        self.ui.geometry("+%s+%s" % (x , y))

    def check_cell(self, row, col):
        pass

    def check_effects(self, event):
        # effect = square.entity.status
        # if effect is not None:
        effect = self.textbox.get("1.0",'end-1c')
        if event.state == 4 and event.keysym == "s":
            messagebox.showinfo(title = effect, message = self.effects.define(effect))

    def on_close(self):
        if messagebox.askyesno(title="Quit?", message = "You A Loser?"):
            self.ui.destroy()


