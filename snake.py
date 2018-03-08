import tkinter as tk
import random


class Snake(tk.Canvas):
    CANVAS_SIZE = 500
    GRID_NUM = 25
    GRID_SIZE = int(CANVAS_SIZE / GRID_NUM)
    STARTING_POS = int(GRID_NUM / 2)

    def __init__(self, master=None):
        self.root = master
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

    def draw_square(self, coords, color="black", customtag="square"):
        (x1, y1, x2, y2) = self.convert_coords_to_box(coords)
        self.create_rectangle(x1, y1, x2, y2, fill=color)
        self.addtag_enclosed(customtag, x1 - 1, y1 - 1, x2 + 1, y2 + 1)

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

        return newcoords

    def draw_snake(self):
        for member in self.members:
            self.draw_square(member, customtag="snake")
        self.draw_square(self.head, color="blue", customtag="snake")

    def move_snake(self, event=None):
        newmembers = [self.head]
        for member in self.members[:-1]:
            newmembers.append(member)

        self.head = self.move(self.head, self.direction)

        if self.head == self.food:
            newmembers.append(self.members[-1])
            self.food = (-1, -1)
            self.delete("food")
            self.generate_food()

        self.members = newmembers
        self.delete('snake')
        self.draw_snake()

    def generate_food(self):
        randx = random.randint(0, self.GRID_NUM-1)
        randy = random.randint(0, self.GRID_NUM-1)

        allsnake = [self.head]
        for member in self.members:
            allsnake.append(member)
        for member in allsnake:
            if randx == member[0]:
                randx += 1
            if randy == member[1]:
                randy += 1
        self.food = (randx, randy)
        self.draw_square(self.food, color="red", customtag="food")


class Application:
    def __init__(self, master=None, title="Window Title", window_offset=(50, 50)):
        self.root = master
        self.title = title
        self.window_offset = window_offset
        self.root.title(self.title)
        self.root.geometry("+%d+%d" % self.window_offset)

        self.menubar = tk.Frame(self.root)
        self.menubar.pack(side=tk.TOP, fill=tk.X)
        self.startbutton = tk.Button(self.menubar, text="Start", padx=2, pady=2, command=self.start)
        self.startbutton.pack(side=tk.LEFT, anchor=tk.W)
        self.pausebutton = tk.Button(self.menubar, text="Add food", padx=2, pady=2, command=self.pause)
        self.pausebutton.pack(side=tk.LEFT, anchor=tk.W)
        self.quitbutton = tk.Button(self.menubar, text="Quit", padx=2, pady=2, command=self.quit)
        self.quitbutton.pack(side=tk.LEFT, anchor=tk.W)

        self.snake_canvas = Snake(self.root)
        self.snake_canvas.pack(side=tk.LEFT, anchor=tk.NW)

        self.root.bind('w', self.hit_w)
        self.root.bind('a', self.hit_a)
        self.root.bind('s', self.hit_s)
        self.root.bind('d', self.hit_d)

    def hit_w(self, event=None):
        self.snake_canvas.direction = tk.N
        self.snake_canvas.move_snake()

    def hit_a(self, event=None):
        self.snake_canvas.direction = tk.W
        self.snake_canvas.move_snake()

    def hit_s(self, event=None):
        self.snake_canvas.direction = tk.S
        self.snake_canvas.move_snake()

    def hit_d(self, event=None):
        self.snake_canvas.direction = tk.E
        self.snake_canvas.move_snake()

    def start(self):
        self.snake_canvas.draw_snake()
        print("start")

    def pause(self):
        self.snake_canvas.generate_food()
        print("pause")

    def quit(self):
        print("quit")
        self.root.quit()


def main():
    root = tk.Tk()

    Application(master=root, title="SnakePy", window_offset=(400, 60))

    root.mainloop()


if __name__ == '__main__':
    main()
