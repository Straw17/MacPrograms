import tkinter as tk
import random

class App(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.grid()
        self.create_buttons()
        self.create_mines()
        
    def button_press(self, event):
        print(event.widget)
        
    def create_buttons(self):
        self.buttons = []
        for y in range(16):
            self.buttons.append([])
            for x in range(30):
                self.buttons[y].append(x)
                self.buttons[y][x] = tk.Button(command = self.button_press)
                self.buttons[y][x].grid(column = str(x), row = str(y))
                self.buttons[y][x].bind('<Button-1>', self.button_press)

    def create_mines(self):
        self.mine_list = []
        for mines in range(99):
            self.yValue = random.randint(0, 15)
            self.xValue = random.randint(0, 29)
            if self.buttons[self.yValue][self.xValue] in self.mine_list:
                mines += 1
            else:
                self.mine_list.append(self.buttons[self.yValue][self.xValue])

root = tk.Tk()
app = App(master = root)
app.mainloop()
