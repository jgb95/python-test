import tkinter as tk
import random


class Snake:
    CANVAS_SIZE = 500
    GRID_NUM = 25
    GRID_SIZE = int(CANVAS_SIZE / GRID_NUM)
    WINDOW_OFFSET = 400, 60
    TITLE = "SnakePy"
    STARTING_POS = int(GRID_NUM / 2)

    def __init__(self, root=None):
        self.root = root
        self.root.geometry("+%d+%d" % self.WINDOW_OFFSET)
        self.root.title(self.TITLE)

        self.head = (self.STARTING_POS, self.STARTING_POS)
        self.members = [(self.STARTING_POS, self.STARTING_POS+1)]
        self.food = (-1, -1)
        self.direction = tk.N

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
        self.root.bind('<space>', self.move_snake)

    def convert_coords_to_box(self, coords):
        (xcoord, ycoord) = coords
        x1 = xcoord * self.GRID_SIZE
        y1 = ycoord * self.GRID_SIZE
        x2 = x1 + self.GRID_SIZE
        y2 = y1 + self.GRID_SIZE
        return x1, y1, x2, y2

    def draw_square(self, coords, color="black", customtag="square"):
        (x1, y1, x2, y2) = self.convert_coords_to_box(coords)
        tag = self.tag(coords)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        self.canvas.addtag_enclosed(tag, x1 - 1, y1 - 1, x2 + 1, y2 + 1)
        self.canvas.addtag_enclosed(customtag, x1 - 1, y1 - 1, x2 + 1, y2 + 1)

    def delete_square(self, coords):
        tag = self.tag(coords)
        self.canvas.delete(tag)

    def move(self, coords, direction):
        (xcoord, ycoord) = coords
        tag = self.tag(coords)
        newcoords = coords

        if direction == tk.N:
            newcoords = (xcoord, (ycoord - 1) % self.GRID_NUM)
        elif direction == tk.W:
            newcoords = ((xcoord - 1) % self.GRID_NUM, ycoord)
        elif direction == tk.S:
            newcoords = (xcoord, (ycoord + 1) % self.GRID_NUM)
        elif direction == tk.E:
            newcoords = ((xcoord + 1) % self.GRID_NUM, ycoord)

        newtag = self.tag(newcoords)
        (x1, y1, x2, y2) = self.convert_coords_to_box(newcoords)
        self.canvas.coords(tag, x1, y1, x2, y2)
        self.canvas.dtag(tag, tag)
        self.canvas.addtag_enclosed(newtag, x1 - 1, y1 - 1, x2 + 1, y2 + 1)
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
            self.canvas.delete("food")
            self.generate_food()

        self.members = newmembers
        self.canvas.delete('snake')
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

    def tag(self, coords):
        tag = str(coords[0]) + "," + str(coords[1])
        return tag

    def hit_w(self, event=None):
        self.direction = tk.N
        self.move_snake()

    def hit_a(self, event=None):
        self.direction = tk.W
        self.move_snake()

    def hit_s(self, event=None):
        self.direction = tk.S
        self.move_snake()

    def hit_d(self, event=None):
        self.direction = tk.E
        self.move_snake()

    def start(self):
        self.draw_snake()
        print("start")

    def pause(self):
        self.generate_food()
        print("pause")

    def quit(self):
        print("quit")
        self.root.quit()

    def make_grid(self):
        self.canvas.create_line(1, 1, self.CANVAS_SIZE, 1)
        self.canvas.create_line(1, 1, 1, self.CANVAS_SIZE)
        self.canvas.create_line(self.CANVAS_SIZE, 1, self.CANVAS_SIZE, self.CANVAS_SIZE)
        self.canvas.create_line(1, self.CANVAS_SIZE, self.CANVAS_SIZE, self.CANVAS_SIZE)
        for i in range(0, self.CANVAS_SIZE, self.GRID_SIZE):
            self.canvas.create_line(i, 0, i, self.CANVAS_SIZE)
            self.canvas.create_line(0, i, self.CANVAS_SIZE, i)


def main():
    window = tk.Tk()

    Snake(window)

    window.mainloop()


if __name__ == '__main__':
    main()
