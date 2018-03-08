import tkinter as tk


class Snake:
    CANVAS_SIZE = 500
    GRID_NUM = 25
    GRID_SIZE = int(CANVAS_SIZE / GRID_NUM)
    WINDOW_OFFSET = 400, 60
    TITLE = "SnakePy"

    def __init__(self, root=None):
        self.root = root
        self.root.geometry("+%d+%d" % self.WINDOW_OFFSET)
        self.root.title(self.TITLE)
        self.head = (3, 3)

        self.menubar = tk.Frame(root)
        self.menubar.pack(side=tk.TOP, fill=tk.X)
        self.startbutton = tk.Button(self.menubar, text="Start", padx=2, pady=2, command=self.start)
        self.startbutton.pack(side=tk.LEFT, anchor=tk.W)
        self.pausebutton = tk.Button(self.menubar, text="Pause", padx=2, pady=2, command=self.pause)
        self.pausebutton.pack(side=tk.LEFT, anchor=tk.W)
        self.quitbutton = tk.Button(self.menubar, text="Quit", padx=2, pady=2, command=self.quit)
        self.quitbutton.pack(side=tk.LEFT, anchor=tk.W)

        self.canvas = tk.Canvas(self.root, width=self.CANVAS_SIZE, height=self.CANVAS_SIZE, bg="white")
        self.canvas.pack(side=tk.LEFT, anchor=tk.NW)
        self.make_grid()

        self.root.bind('w', self.hit_w)
        self.root.bind('a', self.hit_a)
        self.root.bind('s', self.hit_s)
        self.root.bind('d', self.hit_d)

    def draw_square(self, coords, color="black"):
        (xcoord, ycoord) = coords
        x1 = xcoord * self.GRID_SIZE
        y1 = ycoord * self.GRID_SIZE
        x2 = x1 + self.GRID_SIZE
        y2 = y1 + self.GRID_SIZE
        tag = str(xcoord) + "," + str(ycoord)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.canvas.addtag_enclosed(tag, x1-1, y1-1, x2+1, y2+1)

    def delete_square(self, coords):
        (xcoord, ycoord) = coords
        tag = str(xcoord) + "," + str(ycoord)
        self.canvas.delete(tag)

    def move(self, coords, direction):
        (xcoord, ycoord) = coords
        newcoords = coords
        if direction == tk.N:
            newcoords = (xcoord, (ycoord - 1) % self.GRID_NUM)
        elif direction == tk.W:
            newcoords = ((xcoord - 1) % self.GRID_NUM, ycoord)
        elif direction == tk.S:
            newcoords = (xcoord, (ycoord + 1) % self.GRID_NUM)
        elif direction == tk.E:
            newcoords = ((xcoord + 1) % self.GRID_NUM, ycoord)
        self.delete_square(coords)
        self.draw_square(newcoords)

    def hit_w(self, event=None):
        self.move(self.head, tk.N)
        (x, y) = self.head
        self.head = (x, (y-1) % self.GRID_NUM)

    def hit_a(self, event=None):
        self.move(self.head, tk.W)
        (x, y) = self.head
        self.head = ((x-1) % self.GRID_NUM, y)

    def hit_s(self, event=None):
        self.move(self.head, tk.S)
        (x, y) = self.head
        self.head = (x, (y+1) % self.GRID_NUM)

    def hit_d(self, event=None):
        self.move(self.head, tk.E)
        (x, y) = self.head
        self.head = ((x+1) % self.GRID_NUM, y)


    def start(self):
        self.draw_square(self.head, color="red")
        print("start")

    def pause(self):
        self.delete_square(self.head)
        print("pause")

    def quit(self):
        print("quit")
        self.root.quit()

    def make_grid(self):
        self.canvas.create_line(1, 1, 500, 1)
        self.canvas.create_line(1, 1, 1, 500)
        self.canvas.create_line(500, 1, 500, 500)
        self.canvas.create_line(1, 500, 500, 500)
        for i in range(0, self.CANVAS_SIZE, self.GRID_SIZE):
            self.canvas.create_line(i,0, i, 500)
            self.canvas.create_line(0,i, 500, i)


def main():
    window = tk.Tk()

    Snake(window)

    window.mainloop()


if __name__ == '__main__':
    main()
