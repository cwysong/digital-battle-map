import tkinter as tk
from tkinter import PhotoImage, messagebox
from PIL import Image, ImageTk
from elements import *

# Constants for the grid size
CELL_SIZE = 60  # Size of each cell in pixels
SCROLL_AMOUNT = 20  # Amount to scroll on each key press


class dnd_battle_map(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.entities:dict[str, entity] = dict()
        self.create_widgets()
        self.setup_scroll_bindings()
        self.marks:list = []
        self.selected:entity = None
        self.dupes:dict[str,int] = dict()

    def create_widgets(self):
        self.background_image = Image.open("map.jpg")  # Replace with your image file path
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a canvas widget
        self.canvas = tk.Canvas(self, width=self.background_image.size[0], height=self.background_image.size[1])
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)
        self.canvas.grid()

        self.canvas.bind('<Button-1>', self.left_click)
        self.canvas.bind('<Button-2>', self.middle_click)
        self.canvas.bind('<Button-3>', self.right_click)


        # Create grid lines
        for i in range(self.background_image.size[0]):
            x = i * CELL_SIZE
            self.canvas.create_line(x, 0, x, self.background_image.size[0] * CELL_SIZE)
            self.canvas.create_line(0, x, self.background_image.size[0] * CELL_SIZE, x)

        self.menubar = tk.Menu(self.master)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_close)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        
        # add commands
        self.actionmenu.add_command(label = "Add Entity", command = self.add_entity)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Actions")

        self.master.config(menu=self.menubar)

    def on_close(self):
        if messagebox.askyesno(title="Quit?", message = "You A Loser?"):
            self.master.destroy()

    def left_click(self, event):
        if self.selected != None:
            x = self.canvas.canvasx(event.x)
            y = self.canvas.canvasy(event.y)
            cell_left = (x//CELL_SIZE)*CELL_SIZE
            cell_right = cell_left+CELL_SIZE
            cell_up = (y//CELL_SIZE)*CELL_SIZE
            cell_down = cell_up+CELL_SIZE
            try:
                ind = self.marks.index([cell_left,cell_up,cell_right,cell_down])
                self.marks.pop(ind)
                self.canvas.create_rectangle(cell_left, cell_up, cell_right, cell_down, outline='black')
            except:
                self.marks.append([cell_left, cell_up, cell_right, cell_down])
                if len(self.marks)-1 < int(self.selected.speed/5):
                    self.canvas.create_rectangle(cell_left, cell_up, cell_right, cell_down, outline='white')
                elif len(self.marks)-1 < int(self.selected.speed/5)*2:
                    self.canvas.create_rectangle(cell_left, cell_up, cell_right, cell_down, outline='orange')
                elif len(self.marks)-1 < int(self.selected.speed/5)*4:
                    self.canvas.create_rectangle(cell_left, cell_up, cell_right, cell_down, outline='red')

    def middle_click(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        cell_left = (x//CELL_SIZE)*CELL_SIZE
        cell_right = cell_left+CELL_SIZE
        cell_up = (y//CELL_SIZE)*CELL_SIZE
        cell_down = cell_up+CELL_SIZE
        self.canvas.create_rectangle(cell_left, cell_up, cell_right, cell_down, outline='black')
    
    def right_click(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        cell_left = (x//CELL_SIZE)*CELL_SIZE
        cell_right = cell_left+CELL_SIZE
        cell_up = (y//CELL_SIZE)*CELL_SIZE
        cell_down = cell_up+CELL_SIZE
        for key in self.entities.keys():
            if self.entities[key].location[0] == cell_left and self.entities[key].location[1] == cell_up:
                if self.selected is None:
                    self.canvas.create_rectangle(cell_left, cell_up, cell_right, cell_down, outline='white')
                    self.selected = self.entities[key]
                elif self.entities[key] == self.selected:
                    self.selected = None
                    self.canvas.create_rectangle(cell_left, cell_up, cell_right, cell_down, outline='red')
                    self.clear_marks()
                break
            elif self.entities[key] == self.selected:
                prev_left = self.entities[key].location[0]
                prev_up = self.entities[key].location[1]
                prev_right = prev_left+CELL_SIZE
                prev_down = prev_up+CELL_SIZE
                self.entities[key].prev_id = self.entities[key].cur_id
                self.clear_marks()
                # Remove previous sprite
                self.canvas.create_rectangle(prev_left,prev_up,prev_right,prev_down,outline='black')
                self.canvas.delete(self.entities[key].prev_id)
                self.entities[key].cur_id = self.canvas.create_image(cell_left,cell_up, image = self.entities[key].photo, anchor = tk.NW)
                self.canvas.create_rectangle(cell_left,cell_up,cell_right,cell_down, outline='red')
                self.selected = None
                new_location = tuple([cell_left, cell_up])
                self.entities[key].location = new_location
                break

    def clear_marks(self):
        for mark in self.marks:
            cell_left = mark[0]
            cell_up = mark[1]
            cell_right = mark[2]
            cell_down = mark[3]
            self.canvas.create_rectangle(cell_left, cell_up, cell_right, cell_down, outline='black')
        self.marks = []

    def setup_scroll_bindings(self):
        self.canvas.bind("<KeyPress-w>", self.scroll_up)
        self.canvas.bind("<KeyPress-a>", self.scroll_left)
        self.canvas.bind("<KeyPress-s>", self.scroll_down)
        self.canvas.bind("<KeyPress-d>", self.scroll_right)

        self.canvas.focus_set()  # Set focus to the canvas to capture key events

    def scroll_up(self, event):
        self.canvas.yview_scroll(-1, "units")

    def scroll_down(self, event):
        self.canvas.yview_scroll(1, "units")

    def scroll_left(self, event):
        self.canvas.xview_scroll(-1, "units")

    def scroll_right(self, event):
        self.canvas.xview_scroll(1, "units")
        
    def add_entity(self):
        new_entity:entity = entity(name = "kobold", sprite = "kobold.png", size=CELL_SIZE)
        try: 
            self.dupes[new_entity.name] = self.dupes[new_entity.name]+1
        except:
            self.dupes[new_entity.name] = 1
        self.entities[new_entity.name+str(self.dupes[new_entity.name])] = new_entity
        new_entity.cur_id = self.canvas.create_image(0,0, image = new_entity.photo, anchor = tk.NW)
        self.canvas.create_rectangle(0,0,CELL_SIZE, CELL_SIZE, outline='red')

def main():

    root = tk.Tk()
    root.title("DND Battle Map")
    app = dnd_battle_map(master=root)
    app.master.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()