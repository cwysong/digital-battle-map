import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Constants for the grid size
CELL_SIZE = 60  # Size of each cell in pixels
SCROLL_AMOUNT = 20  # Amount to scroll on each key press


class DndBattleMap(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        self.setup_scroll_bindings()

    def create_widgets(self):
        self.background_image = Image.open("cave.jpg")  # Replace with your image file path
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a canvas widget
        self.canvas = tk.Canvas(self, width=self.background_image.size[0], height=self.background_image.size[1])
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)
        self.canvas.grid()

        # self.lastClickX = 0
        # self.lastClickY = 0

        # self.master.overrideredirect(True)
        # self.master.attributes('-topmost', True)
        # self.canvas.bind('<Button-3>', self.SaveLastClickPos)
        # self.canvas.bind('<B3-Motion>', self.Dragging)
        self.canvas.bind('<Button-1>', self.left_click)
        self.canvas.bind('<Button-2>', self.middle_click)

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
        self.actionmenu.add_command(label = "Add Entity", command = None)
        self.actionmenu.add_separator()
        self.actionmenu.add_command(label = "Add Background", command = None)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Actions")

        self.master.config(menu=self.menubar)

    def on_close(self):
        if messagebox.askyesno(title="Quit?", message = "You A Loser?"):
            self.master.destroy()

    # def SaveLastClickPos(self, event):
    #     self.lastClickX = event.x
    #     self.lastClickY = event.y


    # def Dragging(self, event):
    #     x, y = event.x - self.lastClickX + self.master.winfo_x(), event.y - self.lastClickY + self.master.winfo_y()
    #     self.master.geometry("+%s+%s" % (x , y))

    def left_click(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        cell_left = round(x/CELL_SIZE)*CELL_SIZE
        cell_right = cell_left+CELL_SIZE
        cell_up = round(y/CELL_SIZE)*CELL_SIZE
        cell_down = cell_up+CELL_SIZE
        self.canvas.create_rectangle(cell_left, cell_up, cell_right, cell_down, outline='white')

    def middle_click(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        cell_left = round(x/CELL_SIZE)*CELL_SIZE
        cell_right = cell_left+CELL_SIZE
        cell_up = round(y/CELL_SIZE)*CELL_SIZE
        cell_down = cell_up+CELL_SIZE
        self.canvas.create_rectangle(cell_left, cell_up, cell_right, cell_down, outline='black')

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

def main():
    root = tk.Tk()
    root.title("DND Battle Map")
    app = DndBattleMap(master=root)
    app.master.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()

main()