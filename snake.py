from tkinter import *
from tkinter import messagebox
import random


class Snake(Canvas):
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
        self.running = False
        self.speed = 50
        self.direction = N

    def make_grid(self):
        for i in range(0, self.CANVAS_SIZE, self.GRID_SIZE):
            self.create_line(i, 0, i, self.CANVAS_SIZE)
            self.create_line(0, i, self.CANVAS_SIZE, i)

    def reset(self):
        self.delete("square")
        self.head = (self.STARTING_POS, self.STARTING_POS)
        self.members = [(self.STARTING_POS, self.STARTING_POS + 1)]
        self.food = (-1, -1)
        self.running = False
        self.speed = 50
        self.direction = N

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
        self.addtag_enclosed("square", x1 - 1, y1 - 1, x2 + 1, y2 + 1)

    def move_box(self, coords, direction):
        (xcoord, ycoord) = coords
        newcoords = coords

        if direction == N:
            newcoords = (xcoord, (ycoord - 1))
        elif direction == W:
            newcoords = ((xcoord - 1), ycoord)
        elif direction == S:
            newcoords = (xcoord, (ycoord + 1))
        elif direction == E:
            newcoords = ((xcoord + 1), ycoord)

        return newcoords

    def draw_snake(self):
        print(" ")
        print("*****")
        print(self.head)
        for member in self.members:
            self.draw_box(member, customtag="snake")
            print(member)
        self.draw_box(self.head, color="blue", customtag="snake")

    def tick(self):
        newhead = self.move_box(self.head, self.direction)
        newmembers = []

        if newhead == self.food:
            newmembers.append(self.head)
            self.head = newhead
            for member in self.members:
                newmembers.append(member)
            self.members = newmembers
            self.delete("food")
            self.generate_food()
        elif (newhead in [self.head] + self.members) and self.running:
            self.running = False
            messagebox.showinfo("Game Over!", "Game Over! You ate yourself!")
            self.root.new_game()
        elif (newhead[0] < 0 or
              newhead[1] < 0 or
              newhead[0] >= self.GRID_NUM or
              newhead[1] >= self.GRID_NUM) \
                and self.running:
            self.running = False
            messagebox.showinfo("Game Over!", "Game Over! You ran into a wall!")
            self.root.new_game()
        else:
            newmembers.append(self.head)
            self.head = newhead
            for member in self.members[:-1]:
                newmembers.append(member)
            self.members = newmembers

        if self.running:
            self.delete("snake")
            self.draw_snake()
            self.after(self.speed, self.tick)

    def change_direction(self, newdirection):
        self.direction = newdirection

    def change_speed(self, newspeed):
        self.speed = newspeed

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


class Application(Frame):
    def __init__(self, master=None, size=500, grid=25):
        self.root = master
        self.size = size
        self.grid = grid
        super(Application, self).__init__(self.root)

        self.menubar = Frame(self)
        self.menubar.pack(side=TOP, fill=X)
        self.startbutton = Button(self.menubar, text="Start", padx=2, pady=2, command=self.start)
        self.startbutton.pack(side=LEFT, anchor=W)
        self.pausebutton = Button(self.menubar, text="Pause", padx=2, pady=2, command=self.pause)
        self.pausebutton.pack(side=LEFT, anchor=W)
        self.newgamebutton = Button(self.menubar, text="New Game", padx=2, pady=2, command=self.new_game)
        self.newgamebutton.pack(side=LEFT, anchor=W)

        self.quitbutton = Button(self.menubar, text="Quit", padx=2, pady=2, command=self.quit)
        self.quitbutton.pack(side=RIGHT, anchor=E)

        self.snake_canvas = Snake(self, size=self.size, grid=self.grid)
        self.snake_canvas.pack(side=LEFT, anchor=NW)

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
        self.root.bind('<Return>', self.start_or_pause)

    def press_up(self, event=None):
        if self.snake_canvas.direction != S:
            self.snake_canvas.change_direction(N)

    def press_down(self, event=None):
        if self.snake_canvas.direction != N:
            self.snake_canvas.change_direction(S)

    def press_left(self, event=None):
        if self.snake_canvas.direction != E:
            self.snake_canvas.change_direction(W)

    def press_right(self, event=None):
        if self.snake_canvas.direction != W:
            self.snake_canvas.change_direction(E)

    def start_or_pause(self, event=None):
        if self.snake_canvas.running:
            self.pause()
        else:
            self.start()

    def start(self):
        self.snake_canvas.draw_snake()
        self.snake_canvas.generate_food()
        self.snake_canvas.running = True
        self.snake_canvas.tick()
        print("start")

    def pause(self):
        self.snake_canvas.running = False
        messagebox.showinfo("Game Paused", "Paused. Click OK to resume.")
        self.snake_canvas.running = True
        self.snake_canvas.tick()
        print("pause")

    def new_game(self):
        newgame = messagebox.askyesno("New Game?", "Would you like to start a new game?")
        if newgame:
            self.snake_canvas.reset()
            messagebox.showinfo("New Game Created", "New game started."
                                                    "\nPress Enter or click the Start button to begin")
        else:
            self.root.destroy()

    def quit(self):
        self.snake_canvas.running = False
        answer = messagebox.askyesno("Really Quit?", "Are you sure you want to quit?")
        if answer:
            self.root.destroy()
        else:
            self.snake_canvas.running = True
            self.snake_canvas.tick()


def main():
    root = Tk()
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
