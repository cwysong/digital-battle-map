import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Constants for the grid size
CELL_SIZE = 50  # Size of each cell in pixels

class DndBattleMap(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.background_image = Image.open("cave.jpg")  # Replace with your image file path
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a canvas widget
        self.canvas = tk.Canvas(self, width=self.background_image.size[0], height=self.background_image.size[1])
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)
        self.canvas.grid()

        self.lastClickX = 0
        self.lastClickY = 0

        self.master.overrideredirect(True)
        self.master.attributes('-topmost', True)
        self.canvas.bind('<Button-1>', self.SaveLastClickPos)
        self.canvas.bind('<B1-Motion>', self.Dragging)

        # Create grid lines
        for i in range(self.background_image.size[0]):
            x = i * CELL_SIZE
            self.canvas.create_line(x, 0, x, self.background_image.size[0] * CELL_SIZE)
            self.canvas.create_line(0, x, self.background_image.size[0] * CELL_SIZE, x)

        # Example: Draw a player token
        self.draw_token(2, 3, 'blue')  # Example position (2, 3) with blue color

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

    def draw_token(self, x, y, color):
        # Draw a token at grid position (x, y)
        x_pix = x * CELL_SIZE
        y_pix = y * CELL_SIZE
        self.canvas.create_oval(x_pix, y_pix, x_pix + CELL_SIZE, y_pix + CELL_SIZE, fill=color)

    def on_close(self):
        if messagebox.askyesno(title="Quit?", message = "You A Loser?"):
            self.master.destroy()

    def SaveLastClickPos(self, event):
        self.lastClickX = event.x
        self.lastClickY = event.y


    def Dragging(self, event):
        x, y = event.x - self.lastClickX + self.master.winfo_x(), event.y - self.lastClickY + self.master.winfo_y()
        self.master.geometry("+%s+%s" % (x , y))

def main():
    root = tk.Tk()
    root.title("DND Battle Map")
    app = DndBattleMap(master=root)
    app.mainloop()

main()