import tkinter

# UI implementation from tutorial
class GUI:
    def __init__(self):
        self.ui = tkinter.Tk()
        self.ui.geometry("1200x800")
        self.ui.title("Battle Mat")

        self.label = tkinter.Label(self.ui, text = "Battle", font = ('Arial', 16))
        self.label.pack(padx=10, pady=10)

        self.ui.mainloop()

GUI()