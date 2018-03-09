import tkinter as tk
import random


class Snake(tk.Canvas):
    def __init__(self, master=None, size=500, grid=25):
        self.root = master
        self.CANVAS_SIZE = size
        self.GRID_NUM = grid
        self.GRID_SIZE = int(self.CANVAS_SIZE / self.GRID_NUM)
        self.STARTING_POS = int(self.GRID_NUM / 2)

        super(Snake, self).__init__(self.root, width=self.CANVAS_SIZE, height=self.CANVAS_SIZE, bg="white")
        self.make_grid()

        self.head = (self.STARTING_POS, self.STARTING_POS)
        self.members = [(self.STARTING_POS, self.STARTING_POS + 1)]
        self.food = (-1, -1)
        self.direction = tk.N

    def make_grid(self):
        self.create_line(1, 1, self.CANVAS_SIZE, 1)
        self.create_line(1, 1, 1, self.CANVAS_SIZE)
        self.create_line(self.CANVAS_SIZE, 1, self.CANVAS_SIZE, self.CANVAS_SIZE)
        self.create_line(1, self.CANVAS_SIZE, self.CANVAS_SIZE, self.CANVAS_SIZE)
        for i in range(0, self.CANVAS_SIZE, self.GRID_SIZE):
            self.create_line(i, 0, i, self.CANVAS_SIZE)
            self.create_line(0, i, self.CANVAS_SIZE, i)

    def convert_coords_to_box(self, coords):
        (xcoord, ycoord) = coords
        x1 = xcoord * self.GRID_SIZE
        y1 = ycoord * self.GRID_SIZE
        x2 = x1 + self.GRID_SIZE
        y2 = y1 + self.GRID_SIZE
        return x1, y1, x2, y2

    def draw_box(self, coords, color="black", customtag="square"):
        (x1, y1, x2, y2) = self.convert_coords_to_box(coords)
        self.create_rectangle(x1, y1, x2, y2, fill=color)
        self.addtag_enclosed(customtag, x1 - 1, y1 - 1, x2 + 1, y2 + 1)

    def move_box(self, coords, direction):
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

        return newcoords

    def draw_snake(self):
        print(" ")
        print("*****")
        print(self.head)
        for member in self.members:
            self.draw_box(member, customtag="snake")
            print(member)
        self.draw_box(self.head, color="blue", customtag="snake")

    def move_snake(self):
        newmembers = [self.head]
        for member in self.members[:-1]:
            newmembers.append(member)

        self.head = self.move_box(self.head, self.direction)

        if self.head == self.food:
            newmembers.append(self.members[-1])
            self.food = (-1, -1)
            self.delete("food")
            self.generate_food()

        self.members = newmembers
        self.delete('snake')
        self.draw_snake()

    def generate_food(self):
        allsnake = [self.head] + self.members
        randx = 0
        randy = 0
        isfound = False
        while not isfound:
            randx = random.randint(0, self.GRID_NUM - 1)
            randy = random.randint(0, self.GRID_NUM - 1)
            for member in allsnake:
                if randx == member[0] and randy == member[1]:
                    isfound = False
                    break
                else:
                    isfound = True

        self.food = (randx, randy)
        self.draw_box(self.food, color="red", customtag="food")


class Application(tk.Frame):
    def __init__(self, master=None, size=500, grid=25):
        self.root = master
        self.size = size
        self. grid = grid
        super(Application, self).__init__(self.root)

        self.menubar = tk.Frame(self)
        self.menubar.pack(side=tk.TOP, fill=tk.X)
        self.startbutton = tk.Button(self.menubar, text="Start", padx=2, pady=2, command=self.start)
        self.startbutton.pack(side=tk.LEFT, anchor=tk.W)
        self.pausebutton = tk.Button(self.menubar, text="Add food", padx=2, pady=2, command=self.pause)
        self.pausebutton.pack(side=tk.LEFT, anchor=tk.W)
        self.quitbutton = tk.Button(self.menubar, text="Quit", padx=2, pady=2, command=self.quit)
        self.quitbutton.pack(side=tk.LEFT, anchor=tk.W)

        self.snake_canvas = Snake(self, size=self.size, grid=self.grid)
        self.snake_canvas.pack(side=tk.LEFT, anchor=tk.NW)

        self.bind_keys()
        self.pack()

    def bind_keys(self):
        self.root.bind('w', self.press_up)
        self.root.bind('a', self.press_left)
        self.root.bind('s', self.press_down)
        self.root.bind('d', self.press_right)
        self.root.bind('<Up>', self.press_up)
        self.root.bind('<Left>', self.press_left)
        self.root.bind('<Down>', self.press_down)
        self.root.bind('<Right>', self.press_right)

    def press_up(self, event=None):
        if self.snake_canvas.direction != tk.S:
            self.snake_canvas.direction = tk.N
            self.snake_canvas.move_snake()

    def press_down(self, event=None):
        if self.snake_canvas.direction != tk.N:
            self.snake_canvas.direction = tk.S
            self.snake_canvas.move_snake()

    def press_left(self, event=None):
        if self.snake_canvas.direction != tk.E:
            self.snake_canvas.direction = tk.W
            self.snake_canvas.move_snake()

    def press_right(self, event=None):
        if self.snake_canvas.direction != tk.W:
            self.snake_canvas.direction = tk.E
            self.snake_canvas.move_snake()

    def start(self):
        self.snake_canvas.draw_snake()
        print("start")

    def pause(self):
        self.snake_canvas.generate_food()
        print("pause")


def main():
    root = tk.Tk()
    size = 500
    num_grids = 25

    window_offset = (int((root.winfo_screenwidth() - size) / 2), int((root.winfo_screenheight() - size) / 2))
    print(window_offset)
    root.title("SnakePy")
    root.geometry("+%d+%d" % window_offset)

    app = Application(master=root, size=size, grid=num_grids)
    app.mainloop()


if __name__ == '__main__':
    main()
