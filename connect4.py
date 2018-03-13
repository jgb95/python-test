import tkinter as tk


class Connect4(tk.Canvas):
    def __init__(self, master=None, size=490, grid=7):
        self.root = master
        self.CANVAS_SIZE = size
        self.GRID_NUM = grid
        self.GRID_SIZE = int(self.CANVAS_SIZE / self.GRID_NUM)

        super(Connect4, self).__init__(self.root, width=self.CANVAS_SIZE, height=self.CANVAS_SIZE, bg="white")
        self.make_grid()
        self.bind_keys()

    def bind_keys(self):
        self.bind("<Button-1>", self.left_click)
        self.bind("<Button-3>", self.right_click)

    def left_click(self, event=None):
        x = int(event.x / self.GRID_SIZE)
        self.drop_piece(x, color="blue")

    def right_click(self, event=None):
        x = int(event.x / self.GRID_SIZE)
        self.drop_piece(x, color="red")

    def make_grid(self):
        self.create_line(1, 1, self.CANVAS_SIZE, 1)
        self.create_line(1, 1, 1, self.CANVAS_SIZE)
        self.create_line(self.CANVAS_SIZE, 1, self.CANVAS_SIZE, self.CANVAS_SIZE)
        self.create_line(1, self.CANVAS_SIZE, self.CANVAS_SIZE, self.CANVAS_SIZE)
        for i in range(0, self.CANVAS_SIZE, self.GRID_SIZE):
            self.create_line(i, self.GRID_SIZE, i, self.CANVAS_SIZE)
            self.create_line(0, i, self.CANVAS_SIZE, i)

    def convert_coords_to_circle(self, coords):
        (xcoord, ycoord) = coords
        x1 = xcoord * self.GRID_SIZE
        y1 = ycoord * self.GRID_SIZE
        x2 = x1 + self.GRID_SIZE
        y2 = y1 + self.GRID_SIZE
        return x1, y1, x2, y2

    def draw_circle(self, coords, color="black", customtag="circle"):
        (x1, y1, x2, y2) = self.convert_coords_to_circle(coords)
        coordtag = str(coords[0]) + ","+  str(coords[1])
        self.create_oval(x1, y1, x2, y2, fill=color)
        self.addtag_enclosed(coordtag, x1 - 1, y1 - 1, x2 + 1, y2 + 1)
        self.addtag_enclosed(customtag, x1 - 1, y1 - 1, x2 + 1, y2 + 1)

    def delete_circle(self, coords):
        coordtag = str(coords[0]) + "," + str(coords[1])
        self.delete(coordtag)

    def is_empty(self, coords):
        (x1, y1, x2, y2) = self.convert_coords_to_circle(coords)
        match = self.find_enclosed(x1 - 1, y1 - 1, x2 + 1, y2 + 1)
        if match:
            return False
        else:
            return True

    def drop_piece(self, col, color="black"):
        xcoord = col
        ycoord = 0
        self.draw_circle((xcoord, ycoord), color)
        while ycoord < self.GRID_NUM - 1:
            if self.is_empty((xcoord, ycoord + 1)):
                self.delete_circle((xcoord, ycoord))
                ycoord += 1
                self.draw_circle((xcoord, ycoord), color)
            else:
                break

        newcoords = (xcoord, ycoord)
        return newcoords


class Application(tk.Frame):
    def __init__(self, master=None, size=490, grid=7):
        self.root = master
        self.size = size
        self.grid = grid
        super(Application, self).__init__(self.root)

        self.menubar = tk.Frame(self)
        self.menubar.pack(side=tk.TOP, fill=tk.X)
        self.startbutton = tk.Button(self.menubar, text="Start", padx=2, pady=2, command=self.start)
        self.startbutton.pack(side=tk.LEFT, anchor=tk.W)
        self.pausebutton = tk.Button(self.menubar, text="Pause", padx=2, pady=2, command=self.pause)
        self.pausebutton.pack(side=tk.LEFT, anchor=tk.W)
        self.quitbutton = tk.Button(self.menubar, text="Quit", padx=2, pady=2, command=self.quit)
        self.quitbutton.pack(side=tk.LEFT, anchor=tk.W)

        self.connect = Connect4(self, size=self.size, grid=self.grid)
        self.connect.pack(side=tk.LEFT, anchor=tk.NW)

        self.pack()

    def start(self):
        self.connect.draw_circle((2,1))
        print("start")

    def pause(self):
        print("pause")


def main():
    root = tk.Tk()
    size = 560
    num_grids = 7

    window_offset = (int((root.winfo_screenwidth() - size) / 2), int((root.winfo_screenheight() - size) / 2))
    print(window_offset)
    root.title("Connect4")
    root.geometry("+%d+%d" % window_offset)

    app = Application(master=root, size=size, grid=num_grids)
    app.mainloop()


if __name__ == '__main__':
    main()
